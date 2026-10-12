from itertools import product


def compose(f,g,p,n):
    # f,g coefficient tuples (a2,...,an), representing x+sum a_i x^i.
    # Return f(g(x)) mod x^(n+1).
    # polys indexed 0..n
    gp=[0]*(n+1); gp[1]=1
    for i,a in enumerate(g, start=2): gp[i]=a%p
    out=gp[:]  # leading g(x)
    # powers of g
    power=[0]*(n+1); power[0]=1
    def mul(A,B):
        C=[0]*(n+1)
        for i,ai in enumerate(A):
            if not ai: continue
            for j,bj in enumerate(B):
                if bj and i+j<=n: C[i+j]=(C[i+j]+ai*bj)%p
        return C
    for deg,a in enumerate(f,start=2):
        if deg==2:
            power=mul(gp,gp)
        elif deg>2:
            power=mul(power,gp)
        if a:
            for k,c in enumerate(power): out[k]=(out[k]+a*c)%p
    return tuple(out[2:])


def center(p,n):
    els=list(product(range(p), repeat=n-1))
    Z=[]
    for f in els:
        if all(compose(f,g,p,n)==compose(g,f,p,n) for g in els): Z.append(f)
    return Z

def predicted(p,n):
    dim=2 if (n>=3 and (n-3)%p==0) else 1
    # G_n includes n-1 nonlinear coefficients. top dim entries free.
    return p**dim

cases=[]
for p,maxn in [(2,7),(3,6),(5,5)]:
    for n in range(2,maxn+1):
        z=center(p,n)
        pr=predicted(p,n)
        assert len(z)==pr,(p,n,len(z),pr)
        cases.append((p,n,len(z),pr))
print('EXHAUSTIVE_CENTER_CASES')
for row in cases: print(*row)
print('CHECK_OK')
