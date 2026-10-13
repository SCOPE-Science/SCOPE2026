from itertools import product

def wstate(s):
    return (1 if s & 1 else 0) + (1 if s & 2 else 0)

def valid_direct(n, st):
    A=st[:n]; B=st[n:]
    for i,x in enumerate(A):
        if x==0:
            u=0
            for j,y in enumerate(B):
                if j!=i: u |= y
            if u!=3: return False
    for i,x in enumerate(B):
        if x==0:
            u=0
            for j,y in enumerate(A):
                if j!=i: u |= y
            if u!=3: return False
    return True

def valid_criterion(n, st):
    A=st[:n]; B=st[n:]
    A1={i for i,s in enumerate(A) if s&1}; A2={i for i,s in enumerate(A) if s&2}
    B1={i for i,s in enumerate(B) if s&1}; B2={i for i,s in enumerate(B) if s&2}
    for i,s in enumerate(A):
        if s==0 and (not (B1-{i}) or not (B2-{i})): return False
    for i,s in enumerate(B):
        if s==0 and (not (A1-{i}) or not (A2-{i})): return False
    return True

def predicted_minimum(n, st):
    if sum(map(wstate,st)) != 4:
        return False
    A=st[:n]; B=st[n:]
    # Core type D-D: one {1,2} on each side at the same index.
    for i in range(n):
        if A[i]==3 and B[i]==3 and sum(s!=0 for s in A)==1 and sum(s!=0 for s in B)==1:
            return True
    # Core type S-S: common two-index support, one singleton of each color on each side.
    SA={i for i,s in enumerate(A) if s!=0}; SB={i for i,s in enumerate(B) if s!=0}
    if len(SA)==len(SB)==2 and SA==SB and set(A[i] for i in SA)=={1,2} and set(B[i] for i in SB)=={1,2}:
        return True
    if n==4:
        # One side empty; the other has four singleton labels, two of each color.
        if all(s==0 for s in A) and all(s in (1,2) for s in B) and B.count(1)==2 and B.count(2)==2:
            return True
        if all(s==0 for s in B) and all(s in (1,2) for s in A) and A.count(1)==2 and A.count(2)==2:
            return True
    if n==3:
        # One side empty; the other is a permutation of {1},{2},{1,2}.
        if all(s==0 for s in A) and sorted(B)==[1,2,3]: return True
        if all(s==0 for s in B) and sorted(A)==[1,2,3]: return True
        # Side weights 1 and 3: the heavy side has three singletons; its unique color occurs at the light-side index.
        for lightA in (True,False):
            L=A if lightA else B; H=B if lightA else A
            if sum(map(wstate,L))==1 and sum(map(wstate,H))==3 and all(s in (1,2) for s in H):
                supp=[i for i,s in enumerate(L) if s!=0]
                if len(supp)==1:
                    i=supp[0]
                    if H.count(H[i])==1 and H.count(3-H[i])==2:
                        return True
    return False

def gen_weight_leq4(N):
    st=[0]*N
    def rec(pos,w):
        if pos==N:
            yield tuple(st); return
        for s,ws in ((0,0),(1,1),(2,1),(3,2)):
            if w+ws<=4:
                st[pos]=s
                yield from rec(pos+1,w+ws)
        st[pos]=0
    yield from rec(0,0)

subset_checks=criterion_checks=class_checks=count_checks=0
for n in range(3,13):
    mins=[]
    any_below=False
    for st in gen_weight_leq4(2*n):
        subset_checks += 1
        d=valid_direct(n,st); c=valid_criterion(n,st)
        criterion_checks += 1
        assert d==c,(n,st,d,c)
        w=sum(map(wstate,st))
        if d and w<4: any_below=True
        if d and w==4:
            mins.append(st)
            p=predicted_minimum(n,st)
            class_checks += 1
            assert p,(n,st)
    assert not any_below,n
    expected = 51 if n==3 else 40 if n==4 else 2*n*n-n
    assert len(mins)==expected,(n,len(mins),expected)
    # Ensure predicted families have no extras within all weight-4 labelings.
    pred_count=0
    for st in gen_weight_leq4(2*n):
        if sum(map(wstate,st))==4 and predicted_minimum(n,st):
            pred_count += 1
            assert valid_direct(n,st),(n,st)
    assert pred_count==expected,(n,pred_count,expected)
    count_checks += 1

# Full-state brute force for the two exceptional small orders.
full_checks=0
for n in (3,4):
    best=99; cnt=0
    for st in product(range(4),repeat=2*n):
        full_checks += 1
        if valid_direct(n,st):
            w=sum(map(wstate,st))
            if w<best: best=w; cnt=1
            elif w==best: cnt+=1
    expected = 51 if n==3 else 40
    assert best==4 and cnt==expected,(n,best,cnt)

print(f"VERIFY_OK n_range=3..12 low_weight_labelings={subset_checks} criterion_checks={criterion_checks} minimum_class_checks={class_checks} count_checks={count_checks} full_small_checks={full_checks} max_order=24")
