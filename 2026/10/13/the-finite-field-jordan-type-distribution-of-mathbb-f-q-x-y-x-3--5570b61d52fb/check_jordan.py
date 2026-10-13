"""Independent finite-field checks for nilpotent multiplication in k[X,Y]/(X^3,Y^3)."""
from collections import Counter
from itertools import product

BASIS=[(i,j) for i in range(3) for j in range(3)]
I={u:k for k,u in enumerate(BASIS)}
ZERO=(0,0)

def field(q):
    if q==4:
        mul=[[0]*q for _ in range(q)]
        for a in range(q):
            for b in range(q):
                z=0
                for i in range(2):
                    for j in range(2):
                        if ((a>>i)&(b>>j)&1):z ^= 1<<(i+j)
                # a field with t^2+t+1
                if z&4: z ^= 7
                mul[a][b]=z
        return lambda a,b:a^b, lambda a,b:mul[a][b]
    return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q

def rank(M,q):
    add,mul=field(q)
    a=[list(row) for row in M];nr=len(a);nc=len(a[0]);i=0
    for j in range(nc):
        pivot=next((k for k in range(i,nr) if a[k][j]),None)
        if pivot is None:continue
        a[i],a[pivot]=a[pivot],a[i]
        inv=next(z for z in range(1,q) if mul(z,a[i][j])==1)
        a[i]=[mul(inv,x) for x in a[i]]
        for k in range(i+1,nr):
            if a[k][j]:
                c=a[k][j]; a[k]=[add(x,mul(c,y)) if q==4 else (x-mul(c,y))%q for x,y in zip(a[k],a[i])]
        i+=1
        if i==nr:break
    return i

def multiply(f,g,q):
    add,mul=field(q); out=[0]*9
    for k,(i,j) in enumerate(BASIS):
        if not f[k]:continue
        for h,(u,v) in enumerate(BASIS):
            if g[h] and i+u<3 and j+v<3:
                t=I[i+u,j+v];out[t]=add(out[t],mul(f[k],g[h]))
    return out

def matrix(f,q):
    rows=[[0]*9 for _ in range(9)]
    for j,(u,v) in enumerate(BASIS):
        g=[0]*9;g[j]=1
        col=multiply(f,g,q)
        for i in range(9):rows[i][j]=col[i]
    return rows

def partition(f,q):
    pw=[0]*9; pw[I[0,0]]=1
    ranks=[9];r=9
    for k in range(1,6):
        pw=multiply(pw,f,q)
        r=rank(matrix(pw,q),q);ranks.append(r)
        if r==0:break
    ranks.extend([0]*(7-len(ranks)))
    cols=[ranks[i]-ranks[i+1] for i in range(5)]
    return tuple(sum(c>i for c in cols) for i in range(cols[0]))

def predicted(f,q):
    char=2 if q in (2,4) else q
    a=f[I[1,0]]; b=f[I[0,1]]
    c=f[I[2,0]];d=f[I[1,1]];e=f[I[0,2]]
    add,mul=field(q)
    if a or b:
        if a and b:
            return (3,3,3) if char==3 else ((4,4,1) if char==2 else (5,3,1))
        if char==3:return (3,3,3)
        return (4,3,2) if ((a and e) or (b and c)) else (3,3,3)
    if c or d or e:
        delta=add(mul(d,d), mul((q-1) if q!=4 else 1,mul(c,e)))
        gamma=add(mul(d,d), mul(2%char,mul(c,e)))
        R=3 if delta==0 else 4
        S=0 if gamma==0 else 1
        return {(3,0):(2,2,2,1,1,1),(3,1):(3,2,1,1,1,1),(4,0):(2,2,2,2,1),(4,1):(3,2,2,1,1)}[R,S]
    h=f[I[2,1]];i=f[I[1,2]];j=f[I[2,2]]
    if h or i:return (2,2,1,1,1,1,1)
    if j:return (2,1,1,1,1,1,1,1)
    return (1,1,1,1,1,1,1,1,1)

def formula(q):
    p=2 if q in (2,4) else q
    result=Counter()
    result[(1,)*9]=1
    result[(2,)+(1,)*7]=q-1
    result[(2,2)+(1,)*5]=(q*q-1)*q
    if p==3:
        result[(2,2,2,1,1,1)]=(q*q-1)*q**3
        result[(3,2,2,1,1)]=(q**3-q*q)*q**3
    else:
        result[(2,2,2,1,1,1)]=2*(q-1)*q**3
        result[(3,2,1,1,1,1)]=(q-1)**2*q**3
        result[(2,2,2,2,1)]=(q-1)**2*q**3
        result[(3,2,2,1,1)]=(q-1)*(q*q-q+1)*q**3
    if p==3:
        result[(3,3,3)]=(q*q-1)*q**6
    else:
        result[(3,3,3)]=2*(q-1)*q**5
        result[(4,3,2)]=2*(q-1)**2*q**5
        result[(4,4,1) if p==2 else (5,3,1)]=(q-1)**2*q**6
    assert sum(result.values())==q**8,(q,sum(result.values()),q**8)
    return result

def run(q,exhaustive):
    print('q',q,'formula', sorted(formula(q).items()))
    if exhaustive:
        ctr=Counter();cnt=0
        for x in product(range(q),repeat=8):
            f=[0]+list(x)
            got=partition(f,q)
            expected=predicted(f,q)
            if got!=expected:raise RuntimeError((q,f,got,expected))
            ctr[got]+=1;cnt+=1
        if ctr!=formula(q):raise RuntimeError(('mismatch',q,ctr,formula(q)))
        print('EXHAUSTIVE_OK',q,cnt)
    else:
        import random
        rng=random.Random(20261010+q)
        for k in range(2000):
            f=[0]+[rng.randrange(q) for i in range(8)]
            got=partition(f,q);expected=predicted(f,q)
            if got!=expected:raise RuntimeError((q,f,got,expected))
        print('SAMPLE_OK',q,2000)
if __name__=='__main__':
    for q in [2,3,4,5,7]:run(q,q<=3)
    print('VERIFY_OK_JORDAN_CI33')
