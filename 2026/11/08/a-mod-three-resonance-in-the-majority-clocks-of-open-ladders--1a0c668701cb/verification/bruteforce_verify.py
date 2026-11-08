"""Independent full-state-space majority verification on finite open ladders."""

def fib(k):
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a

def luc(k):
    if k==0:return 2
    return fib(k-1)+fib(k+1)

def edges(n):
    neighbor=[[] for _ in range(2*n)]
    for i in range(n):
        for rail in (0,1):
            v=2*i+rail
            neighbor[v].append(2*i+1-rail)
            if i>0:neighbor[v].append(2*(i-1)+rail)
            if i+1<n:neighbor[v].append(2*(i+1)+rail)
    return [(sum(1<<u for u in adj),len(adj)) for adj in neighbor]

def simulate(x, masks):
    y=0
    for i,(mask,degree) in enumerate(masks):
        ones=(x&mask).bit_count()
        if 2*ones>degree or (2*ones==degree and x>>i&1):y|=1<<i
    return y

for n in range(2,11):
    masks=edges(n); fixed=two_periodic=all_flip=0
    full=(1<<(2*n))-1
    for x in range(1<<(2*n)):
        y=simulate(x,masks)
        if y==x:fixed+=1
        if y==full^x:all_flip+=1
        if simulate(y,masks)==x:two_periodic+=1
    theory=(2*(fib(n+1)+1),luc(2*n)+1+3*(n%3==0),2*fib(n-1))
    assert (fixed,two_periodic,all_flip)==theory,(n,(fixed,two_periodic,all_flip),theory)
    print(n,fixed,two_periodic,all_flip,'checked',1<<(2*n),'configurations')
print('All complete state spaces n=2,...,10 agree.')
