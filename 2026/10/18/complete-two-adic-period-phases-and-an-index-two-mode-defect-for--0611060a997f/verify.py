"""Exact integer-matrix checks of the two-site cat-map order formulas.
Run with Python 3: python verify.py
The proof is in RESULT.md. Finite tests alone are not its replacement.
"""

def mul(a,b,mod):
    n=len(a)
    return [[sum(a[i][j]*b[j][k] for j in range(n))%mod
             for k in range(n)] for i in range(n)]

def ident(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def power(a,e,mod):
    n=len(a); out=ident(n)
    while e:
        if e&1: out=mul(out,a,mod)
        a=mul(a,a,mod); e//=2
    return out

def matrix(k,c):
    z=[[k,c],[c,k]]
    zz=[[sum(z[i][h]*z[h][j] for h in range(2)) for j in range(2)] for i in range(2)]
    return [[(int(i==j) if i<2 and j<2 else
              z[i][j-2] if i<2 else
              z[i-2][j] if j<2 else
              int(i==j)+zz[i-2][j-2]) for j in range(4)] for i in range(4)]

def v2(x):
    if x==0: return 10**12
    x=abs(x)
    return (x & -x).bit_length()-1

def order(k,c,s):
    if (k-c)&1:
        return 3*(1 << max(0,s-2))
    if k&1:
        return 1 << s
    if k==0 and c==0:
        return 1
    r=min(v2(k),v2(c))
    return 1 << max(0,s-r)

def mod_i(a,m):
    return [[v%m for v in row] for row in a]

def check(a,b):
    global checks
    checks+=1
    assert a==b,(a,b)

checks=0
E=ident(4)
# These residues exactly cover the polynomial congruence classes modulo 8.
for k in range(8):
  for c in range(8):
    M=matrix(k,c)
    b=mod_i(M,8)
    b2=power(M,2,8)
    b3=power(M,3,8)
    b4=power(M,4,8)
    if (k+c)&1:
        check(power(M,3,2),ident(4))
        check(power(M,1,2)!=ident(4),True)
        check(mod_i(b3,4),E)
        check(b3!=E,True)
    elif k&1:
        check(power(M,2,2),E)
        check(power(M,1,2)!=E,True)
        check(mod_i(b2,2),E)
        check(mod_i(b2,4)!=E,True)
        check(mod_i(b4,4),E)
        check(b4!=E,True)
    else:
        check(mod_i(b,2),E)
        if (k%4==2 or c%4==2):
            check(mod_i(b,4)!=E,True)
            check(mod_i(b2,4),E)
            check(b2!=E,True)
        else:
            check(mod_i(b,4),E)
# Dense regression with independently computed matrix powers and proper-divisor tests.
for k in range(-12,13):
  for c in range(-12,13):
    M=matrix(k,c)
    for s in range(1,9):
        modulus=1<<s
        t=order(k,c,s)
        check(power(M,t,modulus),E)
        for p in (2,3):
            if t%p==0:
                check(power(M,t//p,modulus)!=E,True)
        # Diagonal (non-unimodular) scalar modes; compare exact orders.
        scalar_order=lambda d:(3*(1<<max(0,s-2)) if d&1
                               else (1<<max(0,s-v2(d))))
        mode=max(scalar_order(k+c),scalar_order(k-c))
        val=min(v2(k),v2(c))
        factor=(2 if val<s and v2(k)==v2(c) else 1)
        check(t,mode*factor)
# Independently check lifting: if B=I mod 4 and B!=I mod 8,
# each squaring raises the exact 2-valuation one step.
for k,c,m in [(1,0,3),(0,1,3),(1,1,4),(3,5,4),(2,0,2),(2,2,2)]:
    M=matrix(k,c)
    for s in range(3,10):
        assert power(M,m*(2**(s-2)),2**s)==E
        checks+=1
print('VERIFY_OK; exact assertions:',checks)
