from itertools import product
from fractions import Fraction
from math import factorial, comb

def rook_adj(n):
    N=n*n
    adj=[set() for _ in range(N)]
    def idx(i,j): return i*n+j
    for i in range(n):
        for j in range(n):
            v=idx(i,j)
            for jj in range(n):
                if jj!=j: adj[v].add(idx(i,jj))
            for ii in range(n):
                if ii!=i: adj[v].add(idx(ii,j))
    return adj

def is_pdid(n, lab):
    rows=[0]*n
    cols=[0]*n
    for i in range(n):
        for j in range(n):
            x=lab[i*n+j]
            rows[i]+=x
            cols[j]+=x
    for i in range(n):
        for j in range(n):
            x=lab[i*n+j]
            if x<=1:
                s=rows[i]+cols[j]-x
                if not (3<=s<=4):
                    return False
    return True

def bounded_vectors(length,total,maxv=3):
    vec=[0]*length
    def rec(i,rem):
        if i==length:
            if rem==0:
                yield tuple(vec)
            return
        for x in range(min(maxv,rem)+1):
            vec[i]=x
            yield from rec(i+1, rem-x)
    yield from rec(0,total)

def count_formula(n):
    # (n!)^2 [z^n] e^(z/2)/sqrt(1-z)
    s=Fraction(0,1)
    for j in range(n+1):
        s += Fraction(1,2**j*factorial(j)) * Fraction(comb(2*(n-j), n-j), 4**(n-j))
    x=s*factorial(n)*factorial(n)
    assert x.denominator==1
    return x.numerator

print("VERIFY_OK")
tested=0
for n in range(2,5):
    target=2*n
    minima=[]
    below=0
    for w in range(target+1):
        for lab in bounded_vectors(n*n,w):
            tested+=1
            if is_pdid(n,lab):
                if w<target:
                    below+=1
                else:
                    minima.append(lab)
    assert below==0,(n,below)
    predicted=[]
    for lab in minima:
        rows=[sum(lab[i*n:(i+1)*n]) for i in range(n)]
        cols=[sum(lab[i*n+j] for i in range(n)) for j in range(n)]
        assert rows==[2]*n and cols==[2]*n,(n,lab,rows,cols)
    assert len(minima)==count_formula(n),(n,len(minima),count_formula(n))
    print(f"n={n}: gamma_pDI={target}, minimum_functions={len(minima)}")

# coefficient formula values beyond brute-force range
vals=[count_formula(n) for n in range(1,11)]
print("minimum_count_formula_n1_to_n10 =", vals)
print("bounded_labelings_checked =",tested)
print("all brute-force minima matched row-sum=column-sum=2")
