"""Exact integer checks of the two-band quadratic variation of elliptic finite-field extension.

The test checks polynomial coefficients, not an infinite theorem. Run with Python 3.
"""


def finite_field(q):
    if q != 27:
        assert q in (3, 7, 11)
        return (list(range(q)), lambda a,b:(a+b)%q,
                lambda a,b:(a-b)%q, lambda a,b:(a*b)%q)

    def digits(x):
        return (x % 3, (x // 3) % 3, x // 9)

    def number(a):
        return a[0] + 3*a[1] + 9*a[2]

    def add(x,y):
        a,b=digits(x),digits(y)
        return number(tuple((a[i]+b[i])%3 for i in range(3)))

    def sub(x,y):
        a,b=digits(x),digits(y)
        return number(tuple((a[i]-b[i])%3 for i in range(3)))

    def mul(x,y):
        a,b=digits(x),digits(y)
        v=[0]*5
        for i in range(3):
            for j in range(3):
                v[i+j]+=a[i]*b[j]
        # Irreducible polynomial X^3-X+1 over F_3: X^3=X-1.
        for i in (4,3):
            z=v[i]
            v[i]=0
            v[i-2]+=z
            v[i-3]-=z
        return number(tuple(v[i]%3 for i in range(3)))
    return list(range(27)),add,sub,mul


def check(q, patterns=2):
    fld,add,sub,mul=finite_field(q)
    if q==27:
        assert all(mul(a,b)!=0 for a in fld[1:] for b in fld[1:])
    points=[(a,b) for a in fld for b in fld]
    ind={u:i for i,u in enumerate(points)}
    def plus(u,v): return (add(u[0],v[0]), add(u[1],v[1]))
    def minus(u,v): return (sub(u[0],v[0]), sub(u[1],v[1]))
    shells=[[] for _ in fld]
    for v in points:
        shells[add(mul(v[0],v[0]),mul(v[1],v[1]))].append(v)
    assert [len(s) for s in shells] == [1]+[q+1]*(q-1)
    assert sum(len(s)**2 for s in shells) == q**3+q**2-q
    for seed in range(patterns):
        h=[((i*i*(seed+3)+11*i+7*seed)%17)-8 for i in range(q*q)]
        h[0]-=sum(h)
        assert sum(h)==0
        H=sum(a*a for a in h)
        real_T2=imag_T2=0
        constant_T=0
        for center in points:
            for shell in shells:
                L=len(shell)
                B=2*sum(h[ind[plus(center,v)]] for v in shell)
                C=sum(h[ind[plus(center,v)]]*h[ind[minus(center,v)]] for v in shell)
                real_T2+=B*B+2*L*C
                imag_T2+=B*B-2*L*C
                constant_T+=L*L
        assert constant_T==q*q*(q**3+q**2-q)
        assert real_T2==q*(4*q-6)*H,(q,seed,real_T2,H)
        assert imag_T2==q*(4*q-2)*H,(q,seed,imag_T2,H)
    print('PASS q=%s, %s mean-zero patterns, %s centers, exact real/imag coefficients' %
          (q,patterns,q*q))

if __name__=='__main__':
    for q in (3,7,11,27):
        check(q,patterns=2 if q!=27 else 1)
