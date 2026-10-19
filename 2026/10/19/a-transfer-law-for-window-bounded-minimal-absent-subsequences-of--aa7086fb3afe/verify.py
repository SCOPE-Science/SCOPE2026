"""Independent finite verification of periodic-window subsequence antidictionaries.

Uses direct window subsequence enumeration, separate from the cyclic-distance
characterization and transfer-matrix expression.
"""
from itertools import combinations, product
from fractions import Fraction

def direct_mas(q,p):
    alphabet=range(q)
    observed=set([()])
    for off in range(q):
        window=[(off+j)%q for j in range(p)]
        for k in range(1,p+1):
            for idx in combinations(range(p),k):
                observed.add(tuple(window[i] for i in idx))
    absent=set()
    for k in range(2,p+2):
        for a in product(alphabet,repeat=k):
            if a in observed:continue
            if all(a[:i]+a[i+1:] in observed for i in range(k)):
                absent.add(a)
    return absent

def predicted_mas(q,p):
    result=set()
    for k in range(2,p+2):
        for seq in product(range(q),repeat=k):
            ds=[(seq[j+1]-seq[j])%q or q for j in range(k-1)]
            excess=1+sum(ds)-p
            if not (1<=excess<=min(ds[0],ds[-1])):continue
            if all(ds[j]+ds[j+1]>q for j in range(len(ds)-1)):
                result.add(seq)
    return result

def binary_histogram_recurrence(max_p):
    """Coefficient recurrence of 2*t^2*z*(2+z+t*z^2)/(1-t*z^2-t^2*z^3)."""
    F=[{} for _ in range(max_p+1)]
    for p in range(1,max_p+1):
        hist={}
        for lag,shift in ((2,1),(3,2)):
            if p>=lag:
                for length,n in F[p-lag].items():
                    hist[length+shift]=hist.get(length+shift,0)+n
        for power,length,count in ((1,2,4),(2,2,2),(3,3,2)):
            if p==power:
                hist[length]=hist.get(length,0)+count
        F[p]=hist
    return F

def recurrence(p):
    if p<=0:return 0
    if p==1:return 4
    if p==2:return 2
    if p==3:return 6
    return recurrence(p-2)+recurrence(p-3)

if __name__=='__main__':
    count=0
    F=binary_histogram_recurrence(11)
    for q,ps in ((2,range(1,12)),(3,range(1,9)),(4,range(1,7))):
        for p in ps:
            direct=direct_mas(q,p)
            predicted=predicted_mas(q,p)
            assert direct==predicted,(q,p,len(direct),len(predicted),list(direct^predicted)[:5])
            if q==2:
                assert len(direct)==recurrence(p),(p,len(direct),recurrence(p))
                direct_hist={}
                for word in direct:
                    length=len(word)
                    direct_hist[length]=direct_hist.get(length,0)+1
                assert direct_hist==F[p],(p,direct_hist,F[p])
            count+=1
    print('PASS cyclic-window minimal-absent direct exhaustive vs distance characterization and binary recurrence; cases',count)
