import cmath, math

def isprime(n):
    if n<2:return False
    for d in range(2,int(n**0.5)+1):
        if n%d==0:return False
    return True

def check(p):
    w=cmath.exp(2j*math.pi/p)
    q=[1+0j for _ in range(p)]
    q[(-2)%p]=w
    q[(-1)%p]=w**-1
    h=[]
    for x in range(p):
        h.append(sum(q[m]*(w**(m*x)) for m in range(p))/p)
    # exact combinatorial support surrogate: exponent map is permutation iff x=1
    perm=[]
    for x in range(p):
        phi={(-2)%p:1,(-1)%p:-1}
        vals=[(x*m+phi.get(m,0))%p for m in range(p)]
        perm.append(len(set(vals))==p)
    assert [i for i,v in enumerate(perm) if v]==[1]
    assert abs(h[1])<1e-10
    assert all(abs(h[x])>1e-8 for x in range(p) if x!=1)
    # DFT h
    hh=[sum(h[x]*(w**(-m*x)) for x in range(p))/p for m in range(p)]
    assert max(abs(hh[m]-q[m]/p) for m in range(p))<1e-10
    # translation Gram
    for a in range(p):
        for ap in range(p):
            s=sum(h[(x-a)%p]*h[(x-ap)%p].conjugate() for x in range(p))
            target=1 if a==ap else 0
            assert abs(s-target)<1e-9
    # g and full Gabor Gram
    g={(x,y):h[(x-y*y)%p]/math.sqrt(p) for x in range(p) for y in range(p)}
    norm=sum(abs(z)**2 for z in g.values())
    assert abs(norm-1)<1e-9
    E=[xy for xy,z in g.items() if abs(z)>1e-8]
    assert len(E)==p*(p-1)
    assert p*p % len(E) !=0
    # row supports vary => not product
    row0={x for x in range(p) if abs(g[x,0])>1e-8}
    row1={x for x in range(p) if abs(g[x,1])>1e-8}
    assert row0!=row1
    # nonconstant modulus on support
    mods=[abs(h[x]) for x in range(p) if x!=1]
    assert max(mods)-min(mods)>1e-7
    # nonreal
    assert max(abs(z.imag) for z in h)>1e-7
    # Gabor atom Gram using A=Fp x {0}, B={0} x Fp
    atoms=[]
    for a in range(p):
        for b in range(p):
            atoms.append([g[((x-a)%p,y)]*(w**(b*y)) for x in range(p) for y in range(p)])
    for i,u in enumerate(atoms):
        for j,v in enumerate(atoms):
            s=sum(uu*vv.conjugate() for uu,vv in zip(u,v))
            target=1 if i==j else 0
            assert abs(s-target)<3e-8
    # normalized 2D Fourier magnitude pattern
    vals={}
    for m in range(p):
        for n in range(p):
            s=sum(g[x,y]*(w**(-m*x-n*y)) for x in range(p) for y in range(p))/(p*p)
            vals[m,n]=abs(s)
            if m==0 and n==0:
                target=p**(-1.5)
            elif m==0:
                target=0.0
            else:
                target=p**(-2)
            assert abs(abs(s)-target)<2e-9
    nonzero=[v for v in vals.values() if v>1e-10]
    assert max(nonzero)-min(nonzero)>1e-8
    return len(atoms)

ps=[p for p in range(5,24) if isprime(p)]
count=0
for p in ps:
    count+=check(p)
print('VERIFY_OK primes=%s atom_systems=%d' % (','.join(map(str,ps)),count))
