from itertools import product

def is_rid(n, lab):
    A=lab[:n]; B=lab[n:]
    X=sum(A); Y=sum(B)
    for i,x in enumerate(A):
        if x==0 and Y-B[i] < 2:
            return False
    for i,y in enumerate(B):
        if y==0 and X-A[i] < 2:
            return False
    for i,x in enumerate(A):
        if x==0 and not any(B[j]==0 for j in range(n) if j!=i):
            return False
    for i,y in enumerate(B):
        if y==0 and not any(A[j]==0 for j in range(n) if j!=i):
            return False
    return True

def expected_minima(n):
    out=set()
    for z in product(range(3), repeat=n):
        if sum(z)==2:
            lab=tuple(z+z)
            # for n>=4 every such vector has zero graph with no isolated vertices
            out.add(lab)
    return out

total=0
print("VERIFY_OK")
for n in range(3,7):
    best=10**9
    mins=[]
    for lab in product(range(3), repeat=2*n):
        total += 1
        w=sum(lab)
        if w>best:
            continue
        if is_rid(n,lab):
            if w<best:
                best=w; mins=[]
            mins.append(tuple(lab))
    if n>=4:
        exp=expected_minima(n)
        assert best==4,(n,best)
        assert set(mins)==exp,(n,len(mins),len(exp),set(mins)^exp)
        assert len(mins)==n*(n+1)//2
    print(f"n={n}: gamma_rI={best}, minimum_functions={len(mins)}")
print("ternary_labelings_checked =",total)
print("for n=4,5,6 every minimum function was an identical-side vector of side weight 2")
