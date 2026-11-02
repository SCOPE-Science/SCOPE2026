"""Exact, finite consistency checks for the Chebyshev plane-curve flex theorem.

Run with Python 3 (standard library only). The mathematical proof is general;
this program checks its polynomial identities and finite test instances.
"""

def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])


def scale(a,c):
    return trim([c*x for x in a])


def sub(a,b):
    return add(a,scale(b,-1))


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)


def derivative(a):
    return trim([i*a[i] for i in range(1,len(a))] or [0])


def mod_poly(a,p):
    return trim([x%p for x in a])


def gcd_degree_mod(a,b,p):
    a=mod_poly(a,p);b=mod_poly(b,p)
    while b != [0]:
        r=a[:]
        inv=pow(b[-1],-1,p)
        while r != [0] and len(r)>=len(b):
            c=r[-1]*inv % p
            s=len(r)-len(b)
            for j in range(len(b)):
                r[s+j]=(r[s+j]-c*b[j])%p
            r=trim(r)
        a,b=b,r
    return len(a)-1


def chebyshev(d):
    a,b=[2],[0,1]
    if d==0: return a
    for _ in range(1,d):
        a,b=b,sub(mul([0,1],b),a)
    return b


def eval_int(poly,x):
    v=0
    for c in reversed(poly):
        v=v*x+c
    return v


def run():
    prime=1000003
    for d in range(4,25):
        f=chebyshev(d)
        fp=derivative(f);fpp=derivative(fp)
        ode=add(add(mul([-4,0,1],fpp),mul([0,1],fp)),scale(f,-d*d))
        assert ode==[0], (d,'ODE')
        g=sub(scale(mul(f,fpp),d),scale(mul(fp,fp),d-1))
        assert len(g)-1==2*d-4 and g[-1]==-2*d*d, (d,'degree')
        assert gcd_degree_mod(g,derivative(g),prime)==0, (d,'squarefree modulo prime')
        assert gcd_degree_mod(g,f,prime)==0, (d,'coprime modulo prime')
        assert 2*d*(d-2)+d==d*(2*d-3), (d,'number of inflections')
        assert d*(d-2)+2*d*(d-2)==3*d*(d-2), (d,'Pluecker weight')
        for x in range(-4,5):
            assert eval_int(g,x)<0, (d,'real spot test',x)
    print('VERIFY_OK: Chebyshev ODE, G leading term, modular coprimality, inflection counts; d=4..24')

if __name__=='__main__':
    run()
