"""Exact finite checks for a facet-gap extremal law in ranked posets.

No external packages needed. Models pure graded posets by full-rank adjacent
cover matrices with no zero row or column. Integer dynamic programming counts
maximal chains. Exhaustive at heights one through seven.
"""
from itertools import product

def covers(a,b):
    out=[]
    for mask in range(1,1 << (a*b)):
        rows=[0]*a
        cols=[0]*b
        for i in range(a):
            for j in range(b):
                if mask & (1 << (i*b+j)):
                    rows[i] += 1
                    cols[j] += 1
        if min(rows)>0 and min(cols)>0:
            out.append(mask)
    return out

def gap(rs, ms):
    c=[1]*rs[0]; e=0
    for i,mask in enumerate(ms):
        a,b=rs[i],rs[i+1]
        v=[0]*b
        for x in range(a):
            for y in range(b):
                if mask & (1 << (x*b+y)):
                    e+=1
                    v[y]+=c[x]
        c=v
    return sum(c)+sum(rs)-rs[0]-rs[-1]-e

def predicted(h,m):
    return 2**m-m-1-max(0,2*m-h-1)

def run():
    total=0; profiles=0; tight=0
    for h in range(1,8):
        for rs in product((1,2),repeat=h):
            profiles+=1
            m=rs.count(2)
            choices=[covers(rs[i],rs[i+1]) for i in range(h-1)]
            maxseen=-10**6
            bestmasks=[]
            for ms in product(*choices):
                total+=1
                val=gap(rs,ms)
                assert val<=predicted(h,m),(rs,ms,val,predicted(h,m))
                if val>maxseen:
                    maxseen=val;bestmasks=[ms]
                elif val==maxseen:
                    bestmasks.append(ms)
                if val==predicted(h,m):
                    tight+=1
                    if h>=3:
                        full=tuple((1<<(rs[i]*rs[i+1]))-1 for i in range(h-1))
                        assert ms==full,(h,rs,ms,val,'incomplete tie')
                        adjacent=sum(rs[i]==2 and rs[i+1]==2 for i in range(h-1))
                        assert adjacent==max(0,2*m-h-1)
            adj=sum(rs[i]==2 and rs[i+1]==2 for i in range(h-1))
            full=tuple((1<<(rs[i]*rs[i+1]))-1 for i in range(h-1))
            assert gap(rs,full)==2**m-m-1-adj
            assert maxseen==gap(rs,full)
        print('height',h,'done')
    print('PASS exhaustive pure cover arrangements:',total,'rank profiles:',profiles,'attaining global bound:',tight)
    for h,m in [(3,2),(3,3),(4,3),(5,3),(6,4),(7,6)]:
        print('sample',h,m,'max_gap',predicted(h,m))
if __name__=='__main__':run()
