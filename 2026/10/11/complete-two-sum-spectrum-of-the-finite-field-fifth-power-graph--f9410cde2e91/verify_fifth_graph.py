"""Exact finite-field checks for fifth-power graph two-sum multiplicities.

Usage: python verify_fifth_graph.py
All tests use integer arithmetic in explicitly represented quotient fields.
"""
from collections import Counter, defaultdict


def field(p, modulus):
    """F_p[t]/(modulus) where modulus is monic, coefficients ascending."""
    degree = len(modulus) - 1
    q = p ** degree
    def coeffs(a):
        out = []
        for _ in range(degree):
            out.append(a % p)
            a //= p
        return out
    v = [coeffs(a) for a in range(q)]
    def encode(c):
        return sum((x % p) * p**i for i, x in enumerate(c))
    def add(a,b):
        return encode([(v[a][i]+v[b][i]) % p for i in range(degree)])
    def mul(a,b):
        pol = [0] * (2 * degree-1)
        for i in range(degree):
            for j in range(degree):
                pol[i+j]=(pol[i+j]+v[a][i]*v[b][j])%p
        for k in range(2*degree-2, degree-1, -1):
            c=pol[k]
            if c:
                for j in range(degree):
                    pol[k-degree+j]=(pol[k-degree+j]-c*modulus[j])%p
        return encode(pol[:degree])
    def power(a,n):
        r=1
        while n:
            if n&1:r=mul(r,a)
            a=mul(a,a); n//=2
        return r
    return q,add,mul,power


def verify_case(p,modulus):
    q,add,mul,power=field(p,modulus)
    fifth=[power(a,5) for a in range(q)]
    fibers=defaultdict(int)
    for u in range(q):
        for v in range(q):
            fibers[(add(u,v),add(fifth[u],fifth[v]))]+=1
    if p==5:
        assert len(fibers)==q
        assert set(fibers.values())=={q}
        assert sum(m*m for m in fibers.values())==q**3
        print(f'q={q:3d} (characteristic 5): image={q}, energy={q**3}, all fibers={q}')
        return
    minus_one=p-1
    eps=1 if power(minus_one,(q-1)//2)==1 else -1
    eta=1 if power((p-2)%p,(q-1)//2)==1 else -1
    k1=(1-eta)//2
    k2=(q+3*eps)//4
    k3=(1+eta)//2
    k4=(q-4-3*eps-2*eta)//8
    assert min(k1,k2,k3,k4)>=0
    assert k1+2*k2+3*k3+4*k4==q
    for s in range(q):
        current=Counter(v for (ss,_),v in fibers.items() if ss==s)
        expected=Counter({q:1}) if s==0 else Counter({1:k1,2:k2,3:k3,4:k4})
        expected=Counter({j:n for j,n in expected.items() if n})
        assert current==expected,(q,s,current,expected)
    image=1+(q-1)*(k1+k2+k3+k4)
    energy=q*q+(q-1)*3*(q-1-eps)
    assert len(fibers)==image
    assert sum(m*m for m in fibers.values())==energy
    assert energy==4*q*q-6*q+3-3*eps*(q-1)
    print(f'q={q:3d}: eps={eps:+d}, eta={eta:+d}, [k1,k2,k3,k4]={[k1,k2,k3,k4]}, |C+C|={image}, E={energy}')


def main():
    for p in [3,5,7,11,13,17,19,23,29,31,37,41]:
        verify_case(p,[0,1])
    for p,mod in [(3,[1,0,1]),(5,[3,0,1]),(7,[4,0,1]),(3,[1,2,0,1]),(5,[1,1,0,1])]:
        verify_case(p,mod)
    print('All exact tests passed.')


if __name__=='__main__':
    main()
