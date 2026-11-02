"""Reproduce an exact aperiodic autocorrelation census for order-five de Bruijn cycles.
No external libraries or data files required. Run with Python 3.10+.
"""
from collections import Counter

N=32

def feedback_cycles():
    """Each 4-bit suffix has an independently chosen complementary-output rule."""
    out={}
    for table in range(65536):
        x=0; seen=0; letters=[]
        for t in range(N):
            if (seen>>x)&1: break
            seen |= 1<<x
            letters.append((x>>4)&1)
            low=x&15
            x=(low<<1)|((x>>4)^((table>>low)&1))
        if x==0 and seen==(1<<N)-1:
            s=''.join(map(str,letters))
            assert s not in out
            out[s]=table
    return out


def euler_cycles():
    """Independently enumerate edge-simple closed trails in the 4-bit de Bruijn graph.
    Their 32 edge labels form every order-five cycle, uniquely rooted at 00000.
    """
    found=set()
    # First directed edge 00000 from vertex 0000 must occur, fixing the root.
    def dfs(vertex, used, letters):
        if len(letters)==32:
            if vertex==0:
                s=''.join(map(str,letters))
                assert s[:5]=='00000'
                assert s not in found
                found.add(s)
            return
        for bit in (0,1):
            edge=vertex*2+bit
            if not (used>>edge)&1:
                dfs(((vertex<<1)&15)|bit,used|(1<<edge),letters+[int(vertex>>3)])
    dfs(0,1,[0])
    return found


def correlation_multiply(s):
    x=[1 if v=='0' else -1 for v in s]
    return tuple(sum(x[j]*x[j+k] for j in range(N-k)) for k in range(1,N))


def correlation_mismatch(s):
    return tuple((N-k)-2*sum(s[j]!=s[j+k] for j in range(N-k)) for k in range(1,N))

EXPECTED_ROOT={4:40,5:972,6:3612,7:10338,8:12284,9:12582,10:6264,11:8240,12:2590,13:3840,14:776,15:1756,16:470,17:1004,18:216,19:392,20:80,21:80}
EXPECTED_MIN={4:32,5:344,6:476,7:666,8:236,9:174,10:20,11:8,12:20,15:64,16:8}

def main():
    fc=feedback_cycles()
    ec=euler_cycles()
    assert len(fc)==len(ec)==2048
    assert set(fc)==ec
    roots=Counter(); minima=Counter(); pairs=Counter()
    for s in ec:
        ps=[]
        for k in range(N):
            r=s[k:]+s[:k]
            corr=correlation_multiply(r)
            assert corr==correlation_mismatch(r)
            a=max(map(abs,corr))
            roots[a]+=1;ps.append(a)
        minima[min(ps)]+=1
        pairs[min(ps),max(ps)]+=1
    assert dict(roots)==EXPECTED_ROOT
    assert dict(minima)==EXPECTED_MIN
    assert sum(roots.values())==65536
    assert sum(minima.values())==2048
    print('PASS 2 independent complete de Bruijn enumerations: 2048 necklaces')
    print('PASS 2 independent aperiodic-correlation implementations at all 31 lags of 65536 roots')
    print('Root PSL histogram:',dict(sorted(roots.items())))
    print('Cycle root-minimum PSL histogram:',dict(sorted(minima.items())))
    print('Distinct cycle (minimum,maximum) pairs:',len(pairs))
    print('Extremes: global minimum',min(roots),'best-cycle count',minima[min(roots)],'root attainers',roots[min(roots)])
    print('Worst optimal phase',max(minima),'attaining cycles',minima[max(minima)])

if __name__=='__main__':main()
