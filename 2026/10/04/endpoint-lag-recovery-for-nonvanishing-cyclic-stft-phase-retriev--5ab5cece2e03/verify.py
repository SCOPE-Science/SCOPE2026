import cmath, math, random


def stft(g, f):
    d=len(f)
    w=cmath.exp(2j*math.pi/d)
    out=[]
    for k in range(d):
        row=[]
        for ell in range(d):
            s=0j
            for j in range(d):
                s += f[j]*g[(j-k)%d].conjugate()*(w**(-j*ell))
            row.append(s)
        out.append(row)
    return out


def recover_endpoint_products(g, magsq, L):
    d=len(g)
    w=cmath.exp(2j*math.pi/d)
    den=g[L].conjugate()*g[0]
    vals=[]
    for k in range(d):
        c=sum(magsq[k][ell]*(w**(L*ell)) for ell in range(d))/d
        vals.append(c/den)
    return vals


def reconstruct_from_products(p, L):
    d=len(p)
    q=[p[(n*L)%d] for n in range(d)]
    c=[abs(x) for x in q]
    alt=1.0
    for n,x in enumerate(c):
        alt *= x if n%2==0 else 1/x
    z=[0j]*d
    z[0]=math.sqrt(alt)+0j
    for n in range(d-1):
        z[n+1]=q[n]/z[n].conjugate()
    f=[0j]*d
    for n in range(d):
        f[(n*L)%d]=z[n]
    return f

rng=random.Random(20261002)
cases=0
for d in range(3,32,2):
    for L in range(1,(d-1)//2+1):
        if math.gcd(d,L)!=1:
            continue
        # endpoint nonzero; allow interior zeros as theorem does
        g=[0j]*d
        g[0]=2+1j
        g[L]=-1+2j
        for j in range(1,L):
            if (j+L+d)%3:
                g[j]=(j+1)+(2-j)*1j
        f=[]
        for j in range(d):
            z=(rng.randint(1,5)+rng.randint(-4,4)*1j)
            if abs(z)==0: z=1+1j
            f.append(z)
        V=stft(g,f)
        magsq=[[abs(z)**2 for z in row] for row in V]
        p=recover_endpoint_products(g,magsq,L)
        target=[f[(k+L)%d]*f[k].conjugate() for k in range(d)]
        err=max(abs(a-b) for a,b in zip(p,target))
        assert err < 2e-8*max(1,max(abs(x) for x in target)), (d,L,err)
        fr=reconstruct_from_products(p,L)
        # align global phase
        phase=f[0]/fr[0]
        phase/=abs(phase)
        err2=max(abs(phase*fr[j]-f[j]) for j in range(d))
        assert err2 < 2e-7*max(1,max(abs(x) for x in f)), (d,L,err2)
        cases+=1
print('VERIFY_OK', cases)
