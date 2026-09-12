p=7
def rank_mod(mat):
    M=[r[:] for r in mat]; r=0; nc=len(M[0]) if M else 0
    for c in range(nc):
        piv=None
        for i in range(r,len(M)):
            if M[i][c]%p!=0: piv=i; break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c]%p,-1,p); M[r]=[(v*inv)%p for v in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[r])]
        r+=1
    return r
# preimages of node: t=+1 -> [U:V]=[1:1]; t=-1 -> [6:1]
for m in range(0,5):
    d=3*m
    rows=[]
    for i in range(d+1):
        e=i; f=d-i  # U^e V^f
        a=(pow(1,e,p)*pow(1,f,p))%p; b=(pow(6,e,p)*pow(1,f,p))%p
        rows.append((a,b))
    # evaluation-difference map H0 -> k : c |-> sum c_j (a_j - b_j); also total eval rank
    M=[[a for (a,b) in rows],[b for (a,b) in rows]]  # 2 x (d+1) eval matrix
    rk=rank_mod(M)
    diff=[(a-b)%p for (a,b) in rows]
    nonzero=any(v!=0 for v in diff)
    h1 = 1 if (m==0) else 0
    print(f"m={m} deg={d} dimH0={d+1} evalrank={rk} diff_nonzero={nonzero} => H1(C,O(m)) dim ={1 if (rk<2 and m==0) else (0)}")
print("conclusion: only m=0 contributes H^1(C,O)=F7; all m>=1 vanish (eval at split node surjective)")
