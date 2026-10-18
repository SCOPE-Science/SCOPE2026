from itertools import product

def rank_mod(a,p):
    a=[list(row) for row in a]; n=len(a); rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,n) if a[i][col]%p),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank][col:]=[(x*inv)%p for x in a[rank][col:]]
        for i in range(rank+1,n):
            m=a[i][col]
            if m:
                a[i][col+1:]=[(x-m*y)%p for x,y in zip(a[i][col+1:],a[rank][col+1:])]
                a[i][col]=0
        rank+=1
        if rank==n:break
    return rank

def mul(x,y,p,c,d):
    a,b=x;e,f=y
    return ((a*e-d*b*f)%p,(a*f+b*e-c*b*f)%p)

def order_z(p,c,d):
    z=(-1%p,-c*pow(d,-1,p)%p)
    cur=(1,0)
    for t in range(1,p+2):
        cur=mul(cur,z,p,c,d)
        if cur==(1,0):return t
    raise AssertionError(('order',p,c,d))

def predicted(p,t):
    if t%2:return p-1
    if t==2:delta=(p-1)//2
    elif t==4:delta=(p+1)//4-2
    else:delta=(p+1)//t
    return p-1-delta

count=0; examples={}
for p in [5,7,11,13,17,19,23]:
    local=0
    for c,d in product(range(p),range(1,p)):
        dis=(c*c-4*d)%p
        if pow(dis,(p-1)//2,p)!=p-1:continue
        t=order_z(p,c,d)
        actual=rank_mod([[pow((i*i+c*i*j+d*j*j)%p,p-2,p) for j in range(p)] for i in range(p)],p)
        expected=predicted(p,t)
        assert actual==expected,(p,c,d,t,actual,expected)
        examples.setdefault((p,t),(c,d,actual))
        count+=1;local+=1
    print('p',p,'cases',local)
print('ALL_OK',count)
print('examples',examples)
