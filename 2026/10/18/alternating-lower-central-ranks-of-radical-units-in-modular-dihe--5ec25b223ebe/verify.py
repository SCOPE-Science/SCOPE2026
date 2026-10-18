from fractions import Fraction

def rank_basis(rows,p):
    piv={}
    for vec in rows:
        a=[v%p for v in vec]
        for j in sorted(piv):
            if a[j]:
                f=a[j]
                a=[(x-f*y)%p for x,y in zip(a,piv[j])]
        lead=next((i for i,x in enumerate(a) if x),None)
        if lead is not None:
            inv=pow(a[lead],-1,p)
            a=[x*inv%p for x in a]
            piv[lead]=a
    return [piv[k] for k in sorted(piv)]

def simulate(p):
    l=(p-1)//2
    bs=[('P',i) for i in range(1,l+1)]+[('M',i) for i in range(1,l+1)]+[('E',i) for i in range(l)]+[('F',i) for i in range(l)]
    ix={v:i for i,v in enumerate(bs)}
    def mul_basis(a,b):
        t,i=a;u,j=b; k=i+j
        if t=='P' and u=='P' or t=='M' and u=='M': return (t,k) if k<=l else None
        if t=='P' and u=='E' or t=='E' and u=='M': return ('E',k) if k<l else None
        if t=='M' and u=='F' or t=='F' and u=='P': return ('F',k) if k<l else None
        if t=='E' and u=='F':return ('P',k+1) if k+1<=l else None
        if t=='F' and u=='E':return ('M',k+1) if k+1<=l else None
        return None
    def br(v,w):
        res=[0]*len(bs)
        for i,a in enumerate(v):
            if not a:continue
            for j,b in enumerate(w):
                if not b:continue
                u=mul_basis(bs[i],bs[j]);t=mul_basis(bs[j],bs[i])
                if u is not None:res[ix[u]]+=a*b
                if t is not None:res[ix[t]]-=a*b
        return [x%p for x in res]
    L=[[int(i==j) for j in range(len(bs))] for i in range(len(bs))]
    dim=[len(L)]
    while L:
        L=rank_basis([br(a,b) for a in L for b in [[int(i==j) for j in range(len(bs))] for i in range(len(bs))]],p)
        dim.append(len(L))
    predicted=[4*l]+[(3*(l-k)+1 if j%2==0 else 3*(l-k)) for j in range(2,2*l+2) for k in [(j//2)]]
    assert dim==predicted, (p,dim,predicted)
    print('VERIFY_LIE',p,'dimensions=',dim,'factors=',[dim[i]-dim[i+1] for i in range(len(dim)-1)])
for p in [3,5,7,11,13,17]:simulate(p)

# A direct group-algebra calculation, independent of the matrix-block brackets.
import itertools, random

def group_mul(x,y,p):
    # (a+b*s)(c+d*s), s*u=-u*s, with coefficient polynomials mod u^p.
    n=p
    a=x[:n];b=x[n:]; c=y[:n];d=y[n:]
    out=[0]*(2*n)
    for i in range(n):
        for j in range(n-i):
            out[i+j]=(out[i+j]+a[i]*c[j]+b[i]*d[j]*(-1 if j%2 else 1))%p
            out[n+i+j]=(out[n+i+j]+a[i]*d[j]+b[i]*c[j]*(-1 if j%2 else 1))%p
    return tuple(out)

def identity(p):
    return (1,)+(0,)*(2*p-1)

def radical_vectors(p):
    for vals in itertools.product(range(p),repeat=2*(p-1)):
        a=(0,)+vals[:p-1];b=(0,)+vals[p-1:]
        yield tuple(a+b)

def add(x,y,p):return tuple((a+b)%p for a,b in zip(x,y))
def scale(x,f,p):return tuple((a*f)%p for a in x)

def group_exp(x,p):
    w=identity(p);v=identity(p)
    for n in range(1,p):
        v=group_mul(v,x,p)
        w=add(w,scale(v,pow(__import__('math').factorial(n),-1,p),p),p)
    return w

def group_log(g,p):
    x=add(g,scale(identity(p),-1,p),p)
    w=(0,)*(2*p);v=identity(p)
    for n in range(1,p):
        v=group_mul(v,x,p)
        w=add(w,scale(v,(-1 if n%2==0 else 1)*pow(n,-1,p),p),p)
    return w

def group_inverse(g,p):
    x=add(g,scale(identity(p),-1,p),p)
    out=identity(p);v=identity(p)
    for n in range(1,p):
        v=group_mul(v,x,p)
        out=add(out,scale(v,(-1)**n,p),p)
    return out

def group_comm(g,h,p):
    return group_mul(group_mul(group_mul(group_inverse(g,p),group_inverse(h,p),p),g,p),h,p)

def direct_group_tests():
    p=3; elements=[add(identity(p),x,p) for x in radical_vectors(p)]
    cset={group_comm(x,y,p) for x in elements for y in elements}
    assert len(cset)==p,('commutator-set',len(cset))
    assert all(group_comm(c,g,p)==identity(p) for c in cset for g in elements)
    print('VERIFY_GROUP p=3 full pairs',len(elements)**2,'derived_subgroup_order',len(cset),'class',2)
    rng=random.Random(921)
    for p in (3,5,7):
        for _ in range(45):
            x=tuple([0]+[rng.randrange(p) for i in range(p-1)]+[0]+[rng.randrange(p) for i in range(p-1)])
            y=tuple([0]+[rng.randrange(p) for i in range(p-1)]+[0]+[rng.randrange(p) for i in range(p-1)])
            ex=group_exp(x,p);ey=group_exp(y,p)
            assert group_log(ex,p)==x
            assert group_log(ey,p)==y
            comm=group_log(group_comm(ex,ey,p),p)
            xy=group_mul(x,y,p);yx=group_mul(y,x,p)
            bracket=add(xy,scale(yx,-1,p),p)
            # Highest terms cannot perturb radical degree two, independently of p.
            for k in (0,1,2,p,p+1,p+2):
                if k<p: assert comm[k]==bracket[k]
                else: assert comm[k]==bracket[k]
        print('VERIFY_GROUP p=',p,'random_log_commutator_checks',45)

direct_group_tests()
print('VERIFY_OK_LOWER_CENTRAL')
