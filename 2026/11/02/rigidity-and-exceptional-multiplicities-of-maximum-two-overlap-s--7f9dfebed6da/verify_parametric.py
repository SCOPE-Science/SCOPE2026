from math import comb

def a_star(q):
    return (q+1)//3  # q=3k+1 -> k; q=3k+2 -> k+1

def evaluate(q):
    best=-1; winners=[]; count=0
    for a in range(1,q):
        b=q-a
        for t in range(a*b+1):
            val=(a*a+t)*(b*b+a*b-t)
            if val>best:
                best=val; winners=[(a,t)];count=comb(q,a)*comb(a*b,t)
            elif val==best:
                winners.append((a,t));count+=comb(q,a)*comb(a*b,t)
    return best,winners,count

for q in range(2,36):
    best,winners,count=evaluate(q)
    a=a_star(q)
    assert best==q*a*(q-a)**2
    expected={2:4,3:6,4:44,5:140}.get(q,2*comb(q,a))
    assert count==expected, (q,count,expected)
    if q>=6:assert len(winners)==2
    if q<=12: print(q,best,winners,count)
print('PARAMETRIC_VERIFIED_q_2_through_35')
