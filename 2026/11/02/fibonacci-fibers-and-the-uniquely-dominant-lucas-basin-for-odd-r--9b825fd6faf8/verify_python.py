from collections import Counter

def F(x,n):
    return sum(int(not ((x>>((i-1)%n))&1) and not ((x>>((i+1)%n))&1))<<i for i in range(n))

def fib(k):
    if k<0:raise ValueError(k)
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a

def predicted_fiber(y,n):
    z=[(y>>(2*j%n))&1 for j in range(n)]
    if not any(z):return fib(n-1)+fib(n+1)
    if all(z):return 1
    run=[]
    for j in range(n):
        if z[j] and not z[(j+1)%n]:
            L=0;k=(j+1)%n
            while not z[k]: L+=1;k=(k+1)%n
            if L==1:return 0
            run.append(L)
    res=1
    for L in run:res*=fib(L-1)
    return res

def perrin(n):
    a,b,c=3,0,2
    for k in range(3,n+1):a,b,c=b,c,a+b
    return (3,0,2)[n] if n<=2 else c

def A(n):
    arr=[0,2,2,5]
    for k in range(4,n+1):arr.append(2*arr[k-1]-arr[k-2]+arr[k-3])
    return arr[n]
for n in range(3,20,2):
    fibers=Counter(F(x,n) for x in range(1<<n))
    assert all(predicted_fiber(y,n)==fibers[y] for y in range(1<<n)), ('fiber',n)
    assert len(fibers)==A(n), ('A',n)
    fixed=sum(F(y,n)==y for y in fibers)
    assert fixed==perrin(n),('P',n,fixed,perrin(n))
    mx=0;largest=[]
    for y in fibers:
        z=F(y,n)
        if y>z:continue
        bas=fibers[y]+(fibers[z] if z!=y else 0)
        if bas>mx:mx=bas;largest=[(y,z)]
        elif bas==mx:largest.append((y,z))
    assert mx==fib(n-1)+fib(n+1)+1 and largest==[(0,(1<<n)-1)],(n,mx,largest)
    print(f'n={n:2d} states={1<<n:7d} periodic={A(n):5d} fixed={fixed:3d} two={(A(n)-fixed)//2:5d} max_basin={mx:5d} PASS')
