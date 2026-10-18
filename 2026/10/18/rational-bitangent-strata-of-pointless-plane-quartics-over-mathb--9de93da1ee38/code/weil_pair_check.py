"""Independent finite-field point counts for two quartics. Pure stdlib."""
from itertools import product

def field(m):
    p=7; q=p**m
    modulus={1:(0,1),2:(1,0,1),3:(1,1,0,1)}[m]
    v=[tuple((a//(p**i))%p for i in range(m)) for a in range(q)]
    def add_(a,b):return sum(((v[a][i]+v[b][i])%p)*p**i for i in range(m))
    def mul_(a,b):
        h=[0]*(2*m-1)
        for i in range(m):
            for j in range(m): h[i+j]=(h[i+j]+v[a][i]*v[b][j])%p
        for k in range(len(h)-1,m-1,-1):
            h0=h[k]
            if h0:
                for j in range(m):h[k-m+j]=(h[k-m+j]-h0*modulus[j])%p
        return sum(h[i]*p**i for i in range(m))
    add=[[add_(a,b) for b in range(q)] for a in range(q)]
    mul=[[mul_(a,b) for b in range(q)] for a in range(q)]
    sq=[mul[a][a] for a in range(q)]
    fourth=[sq[sq[a]] for a in range(q)]
    def eval_(idx,x,y):
        xx,yy=sq[x],sq[y]
        if idx==30:
            return add[add[add[fourth[x]][fourth[y]]][mul[5][add[xx][yy]]]][3]
        else:
            return add[add[add[add[fourth[x]][fourth[y]]][mul[4][mul[xx][yy]]]][add[xx][yy]]][3]
    ans=[]
    for idx in (30,31):
        affine=sum(eval_(idx,x,y)==0 for x in range(q) for y in range(q))
        inf=sum(eval_(idx,x,1)==0 for x in range(q)) if idx==30 else sum(add[add[fourth[x]][mul[4][sq[x]]]][1]==0 for x in range(q))
        ans.append((idx,affine,inf,affine+inf))
    print('degree',m,'field_size',q,'results',ans)
    assert [t[-1] for t in ans]=={1:[0,0],2:[60,60],3:[384,384]}[m]
for m in (1,2,3):field(m)
print('all independent finite-extension checks passed')
