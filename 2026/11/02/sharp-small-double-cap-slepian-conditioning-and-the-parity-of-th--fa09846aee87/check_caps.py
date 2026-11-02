"""Independent numerical consistency checks for the double-polar-cap Slepian asymptotics.
Run: python check_caps.py. Requires mpmath. Numerical tests supplement the proof.
"""
import math
import mpmath as mp
mp.mp.dps = 85

def beta(a,b):
    return mp.beta(a,b)

def block_eigenvalues(m, parity, r, S):
    """Generalized Gram eigenvalues in monomial coordinates, full-sphere vs caps."""
    n = r+1
    a = mp.matrix(n); b = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            expo = m+i+j+1
            a[i,j] = mp.betainc(expo, parity+mp.mpf('0.5'), 0, S, regularized=False)
            b[i,j] = beta(expo, parity+mp.mpf('0.5'))
    eig = mp.eigsy(mp.cholesky(b)**-1 * a * (mp.cholesky(b).T)**-1, eigvals_only=True)
    # Eigenvalues may be ordered, return real sorted.
    return sorted([mp.re(eig[i]) for i in range(n)])

def blocks(L, S):
    vals=[]
    for m in range(L+1):
        for parity in (0,1):
            r=(L-m-parity)//2
            if r<0: continue
            for v in block_eigenvalues(m,parity,r,S):
                vals.append((v,m,parity))
                if m: vals.append((v,-m,parity))
    return sorted(vals,key=lambda z:z[0])

def predicted_min(L,S):
    r=L//2
    return S**(L+1)/((L+1)*math.comb(L,r)**2*beta(L+1,mp.mpf('.5')))

num=0
for L in range(1,7):
    for S in [mp.mpf('.04'),mp.mpf('.02'),mp.mpf('.01')]:
        vs=blocks(L,S)
        assert len(vs)==(L+1)**2
        assert all(0<z[0]<1 for z in vs)
        num+=len(vs)+1
        rat=vs[0][0]/predicted_min(L,S)
        assert abs(rat-1)<mp.mpf('.40')
        num+=1
        assert abs(vs[-1][0]/(mp.mpf((L+1)*(L+2))/4*S)-1)<mp.mpf('.30')
        num+=1
        least_abs_m=0 if L%2==0 else 1
        assert abs(vs[0][1])==least_abs_m
        if L%2:
            assert abs(vs[1][1])==1 and abs(vs[1][0]-vs[0][0])<mp.mpf('1e-60')
        elif L>=2:
            assert vs[1][0]>vs[0][0]
        num+=1
# Verify exactly the shifted Jacobi leading-coefficient/norm relation.
for m in range(6):
    for r in range(6):
        norm=mp.quad(lambda u:u**m*(sum(math.comb(r,j)*math.comb(r+m,j)*(u-1)**j*u**(r-j) for j in range(r+1))/math.comb(m+2*r,r))**2,[0,1])
        assert abs(norm-1/(mp.mpf(m+2*r+1)*math.comb(m+2*r,r)**2))<mp.mpf('1e-60')
        num+=1
print('PASS:',num,'numerical and exact-identity consistency assertions')
