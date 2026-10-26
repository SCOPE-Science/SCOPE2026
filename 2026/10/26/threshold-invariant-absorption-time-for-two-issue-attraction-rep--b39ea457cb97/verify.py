from fractions import Fraction as F
from itertools import product
from math import comb

def compositions(n):
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                yield (a,b,c,n-a-b-c)

def transition(counts,w,alpha):
    N=sum(counts)
    p={}
    for s in range(4):
        for q in range(4):
            if not counts[s] or not counts[q]: continue
            sim=sum(w[j] for j in range(2) if ((s>>j)&1)==((q>>j)&1))
            for j in range(2):
                old=(s>>j)&1
                new=old
                if sim>alpha: new=(q>>j)&1
                elif sim<alpha: new=1-((q>>j)&1)
                if new==old: continue
                to=s ^ (1<<j)
                dest=list(counts);dest[s]-=1;dest[to]+=1
                dest=tuple(dest)
                p[dest]=p.get(dest,F(0))+F(counts[s]*counts[q],2*N*N)
    return p

def check():
    checked=0
    for w in [(F(2,3),F(1,3)),(F(1,2),F(1,2)),(F(3,5),F(2,5))]:
      for alpha in [F(1,10),F(2,5),F(1,2),F(7,10),F(9,10)]:
        if alpha in w:continue
        for N in range(2,8):
          for c in compositions(N):
            a=c[0]+c[3] # bit representations 0=00, 3=11 even; 1=01,2=10 odd
            p=transition(c,w,alpha)
            plus=sum((v for dest,v in p.items() if dest[0]+dest[3]==a+1), F(0))
            minus=sum((v for dest,v in p.items() if dest[0]+dest[3]==a-1), F(0))
            expected=F(a*(N-a),2*N*N)
            assert plus==minus==expected,(c,w,alpha,plus,minus,expected)
            assert all(dest[0]+dest[3] in (a-1,a+1) for dest in p)
            checked+=1
    print('PASS original-rule microstate lumping checks:',checked)
    for N in range(2,50):
       H=[F(0)]
       for i in range(1,N):H.append(H[-1]+F(1,i))
       E=[F(0)]*(N+1)
       for a in range(1,N):E[a]=2*N*sum((H[N-i]-H[i-1] for i in range(1,a+1)),F(0))
       for a in range(1,N):
          p=F(a*(N-a),2*N*N)
          assert E[a] == 1 +p*E[a-1]+p*E[a+1]+(1-2*p)*E[a]
       assert E[0]==E[N]==0
    print('PASS exact harmonic hitting-time recurrence N=2..49')
    # With two agents holding adjacent strings, the first successful update is
    # a match under low thresholds, but a complement under high thresholds.
    low=transition((1,1,0,0),(F(2,3),F(1,3)),F(1,10))
    high=transition((1,1,0,0),(F(2,3),F(1,3)),F(9,10))
    assert low and high and all(z[0]+z[3] in (0,2) for z in list(low)+list(high))
    assert set(low)!=set(high), (low,high)
    frozen=transition((1,1,0,0),(F(2,3),F(1,3)),F(1,3))
    assert frozen=={},frozen
    print('PASS endpoint-type reversal and threshold-equality freezing')
if __name__=='__main__':check()
