from itertools import product

def partitions(n, r, lo=1):
    if r == 0:
        if n == 0:
            yield ()
        return
    for x in range(lo, n + 1):
        if n - x < x * (r - 1):
            break
        for q in partitions(n-x, r-1, x):
            yield (x,) + q

def labels(parts):
    out=[]
    for i,a in enumerate(parts):
        out += [i]*a
    return out

def valid(vals, lab):
    n=len(vals)
    zeros=[v for v,x in enumerate(vals) if x==0]
    # zero set independent
    for a in range(len(zeros)):
        for b in range(a+1,len(zeros)):
            if lab[zeros[a]] != lab[zeros[b]]:
                return False
    # every zero sees a 2
    twos=[v for v,x in enumerate(vals) if x==2]
    for v in zeros:
        if not any(lab[u] != lab[v] for u in twos):
            return False
    return True

def poly_add(a,b):
    m=max(len(a),len(b)); out=[0]*m
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return out

def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def poly_pow(a,n):
    out=[1]
    for _ in range(n): out=poly_mul(out,a)
    return out

def poly_sub(a,b):
    m=max(len(a),len(b)); out=[0]*m
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]-=x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def predicted(parts):
    N=sum(parts)
    zpz2=[0,1,1]
    onezpz2=[1,1,1]
    z=[0,1]
    out=poly_pow(zpz2,N)
    for ni in parts:
        A=poly_sub(poly_pow(onezpz2,ni), poly_pow(zpz2,ni))
        B=poly_sub(poly_pow(zpz2,N-ni), poly_pow(z,N-ni))
        out=poly_add(out, poly_mul(A,B))
    return out

types=assignments=valid_count=0
for N in range(2,10):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            lab=labels(parts)
            coeff=[0]*(2*N+1)
            for vals in product(range(3), repeat=N):
                assignments += 1
                if valid(vals,lab):
                    valid_count += 1
                    coeff[sum(vals)] += 1
            while len(coeff)>1 and coeff[-1]==0: coeff.pop()
            pred=predicted(parts)
            assert coeff==pred,(parts,coeff,pred)
            total=sum(coeff)
            total_formula=2**N+sum((3**ni-2**ni)*(2**(N-ni)-1) for ni in parts)
            assert total==total_formula,(parts,total,total_formula)
            minw=next(i for i,c in enumerate(coeff) if c)
            known=N-max(parts)+1
            assert minw==known,(parts,minw,known)
            types+=1

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("ternary_labelings_checked =",assignments)
print("valid_functions_checked =",valid_count)
print("orders = 2..9")
print("all enumerator coefficients matched")
print("all total-function counts matched")
print("published minimum-value formula recovered")
