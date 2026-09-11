import pickle, numpy as np, time, random
with open("ord_d2.pkl","rb") as f:
    D=pickle.load(f)
rows_list=D["rows"]; vals_list=D["vals"]; R=D["nrows"]; C=D["ncols"]
print(R,C)
# Sparse CSR for matvec: build row->cols? For Wiedemann need both A and A^T matvecs. Build col-major (have) and row-major.
from collections import defaultdict
row_cols=[[] for _ in range(R)]
row_vals=[[] for _ in range(R)]
for j in range(C):
    for r,v in zip(rows_list[j],vals_list[j]):
        row_cols[r].append(j); row_vals[r].append(v)
print("built transpose")
def rank_mod(p, trials=3):
    # Randomized rank via sampling: compute rank of A mod p using block Wiedemann? Simpler: use random projection to square + ... Actually simplest certified LOWER bound: find full-rank submatrix via greedy? For UPPER bound use elimination on Gram? Let's do: Wiedemann minimal polynomial degree of A^T A gives rank lower bound (number of nonzero... ). Alternative pragmatic: Gaussian elimination with min-degree heuristic in Python may still work: 56k x 32k with 4 nnz/col.
    # Try sparse elimination col-by-col with row sparsity tracking using sets; choose pivot row with min nnz. Let's attempt and watch fill-in.
    # Represent rows as dict col->val for active submatrix; process columns in order, maintain pivot rows.
    # Use array of dicts? 56k dicts heavy but ok.
    import time
    pivcol=[-1]*R  # pivot col for each row
    # active columns: process j in order; maintain column as dict row->val, initially sparse
    # To avoid O(C*R), do standard: for j in range(C): col = initial entries; eliminate using existing pivots (for each row in col with pivcol set, subtract). Then pick new pivot.
    col_init=[dict(zip(rr,vv)) for rr,vv in zip(rows_list,vals_list)]
    # reduce modulus
    for d in col_init:
        for k in list(d):
            d[k]%=p
            if d[k]==0: del d[k]
    rank=0
    t0=time.time()
    for j in range(C):
        d=col_init[j]
        # eliminate
        # iterate over rows in d that have pivots; need pivot row's representation? Standard structured elimination: keep pivots as row ops. We need for pivot row r (with pivot col q<j), the relation to eliminate r from d requires knowing... This is fan-in elimination needing both row and col structures. Simpler to do ROW-oriented: maintain rows; for j, gather rows containing j, pick pivot, eliminate j from other rows. Cost sum over row lengths. Let's do that.
        pass
    return None
# Row-oriented sparse elimination:
def rank_mod_row(p):
    import time
    rws=[dict(zip(a,b)) for a,b in zip(row_cols,row_vals)]
    for d in rws:
        for k in list(d):
            d[k]%=p
            if d[k]==0: del d[k]
    # column to pivot row
    cpiv={}
    rank=0
    t0=time.time()
    # order rows by nnz
    for r in range(R):
        d=rws[r]
        # eliminate using existing pivots: for Pagd... need pivot rows in row-echelon: each pivot row has leading col. Eliminate those cols from d.
        # To keep pivot rows sparse, store them normalized (leading 1) and only eliminate leading cols present in d.
        while d:
            c=min(d)
            q=cpiv.get(c)
            if q is None: break
            # d -= d[c]*prow
            prow=rws[q]
            f=d[c]
            for cc,vv in prow.items():
                nv=(d.get(cc,0)-f*vv)%p
                if nv: d[cc]=nv
                elif cc in d: del d[cc]
        if d:
            c=min(d)
            inv=pow(d[c],-1,p)
            for cc in list(d): d[cc]=(d[cc]*inv)%p
            cpiv[c]=r
            rank+=1
    print("rank",rank,"time",time.time()-t0)
    return rank

for p in [2,3,5]:
    print("p=",p,flush=True)
    print(rank_mod_row(p),flush=True)
