"""Exact finite check for adjacency-level and size-spectrum covariances
in Ewens--Pitman exchangeable partitions.

No simulation: all set partitions of each tested size are enumerated and
all EPPF probabilities are accumulated as exact rational numbers.
"""
from fractions import Fraction as F
from math import comb

def parts(n):
    def build(seq, top):
        if len(seq)==n:
            blocks=[[] for _ in range(top+1)]
            for i,b in enumerate(seq): blocks[b].append(i)
            yield blocks
        else:
            for j in range(top+2):
                yield from build(seq+[j], max(j,top))
    yield from build([0],0)

def rising(x,k,step=1):
    out=F(1)
    for i in range(k): out*=x+i*step
    return out

def prob(blocks, alpha, theta, n):
    k=len(blocks)
    return (rising(theta+alpha,k-1,alpha) / rising(theta+1,n-1) *
            __import__('functools').reduce(lambda x,b:x*rising(1-alpha,len(b)-1),blocks,F(1)))

def check(n,alpha,theta):
    graphs={
      'path': [(i,i+1) for i in range(n-1)],
      'star': [(0,j) for j in range(1,n)],
      'cycle': [(i,(i+1)%n) for i in range(n)] if n>=3 else [(0,1)],
      'complete': [(i,j) for i in range(n) for j in range(i+1,n)]
    }
    psum=F(0); lmean={g:F(0) for g in graphs}; tmeans=[F(0)]*(n+1)
    mixed={g:[F(0)]*(n+1) for g in graphs}
    for blocks in parts(n):
        z=prob(blocks,alpha,theta,n)
        labels=[-1]*n
        for k,block in enumerate(blocks):
            for i in block: labels[i]=k
        levels={g:sum(labels[i]==labels[j] for i,j in edges) for g,edges in graphs.items()}
        sizes=[len(b) for b in blocks]
        psum+=z
        for g in graphs: lmean[g]+=z*levels[g]
        for r in range(1,n+1):
            count=sizes.count(r)
            tmeans[r]+=z*count
            for g in graphs: mixed[g][r]+=z*levels[g]*count
    assert psum==1,(n,alpha,theta,'total',psum)
    p=(1-alpha)/(theta+1)
    q=(1-alpha)/(theta+alpha+1)
    for g,edges in graphs.items():
        assert lmean[g]==len(edges)*p,(n,alpha,theta,'levels',g)
    for r in range(1,n+1):
        e=F(comb(n,r))*rising(1-alpha,r-1)*rising(theta+alpha,n-r)/rising(theta+1,n-1)
        assert tmeans[r]==e,(n,alpha,theta,r,'mean',tmeans[r],e)
        for g,edges in graphs.items():
            covariance=mixed[g][r]-lmean[g]*tmeans[r]
            expression=(F(len(edges))*e*(r*(r-1)+(n-r)*(n-r-1)*q-n*(n-1)*p)/(n*(n-1)))
            assert covariance==expression,(n,alpha,theta,r,g,'covariance',covariance,expression)
    return n

if __name__=='__main__':
    cases=[(F(0),F(1)),(F(0),F(3)),(F(1,2),F(1,2)),(F(1,3),F(2)),(F(3,4),F(-1,2))]
    assertions=0
    for a,t in cases:
        for n in range(2,9):
            check(n,a,t)
            assertions+=5*n+4
    print('PASS',assertions,'exact moment/covariance comparisons over 35 complete finite laws and four graph families')
