#!/usr/bin/env python3
from math import comb

def best_blackburn(q):
    vals=[]
    for a in range(1,q):
        b=q-a
        vals.append((a**5*b,a))
    return max(vals)

def solve(q):
    best=-1; wins=[]; states=0
    # reversal symmetry: x1<=y1
    for x1 in range(1,q//2+1):
        y1=q-x1
        m2=x1*y1
        for x2 in range(m2+1):
            y2=m2-x2
            m3=x1*y2+x2*y1
            for x3 in range(m3+1):
                y3=m3-x3
                states += 1
                m4=x1*y3+x2*y2+x3*y1
                for x4 in (0,m4) if m4 else (0,):
                    y4=m4-x4
                    m5=x1*y4+x2*y3+x3*y2+x4*y1
                    # Objective for n=6 is x1*y5+x2*y4+x3*y3+x4*y2+x5*y1.
                    # Since y5=m5-x5, its x5 coefficient is y1-x1 >=0.
                    # Taking x5=m5 is optimal; if equality, all x5 tie.
                    x5=m5; y5=0
                    val=x1*y5+x2*y4+x3*y3+x4*y2+x5*y1
                    tup=(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
                    if val>best:
                        best=val; wins=[tup]
                    elif val==best:
                        wins.append(tup)
    return best, wins, states

def count_codes(q,wins):
    total=0
    for w in wins:
        x=[None,w[0],w[2],w[4],w[6],w[8]]
        y=[None,w[1],w[3],w[5],w[7],w[9]]
        ways=comb(q,x[1])
        for i in range(2,6):
            mi=sum(x[j]*y[i-j] for j in range(1,i))
            ways*=comb(mi,x[i])
        # each reduced profile with x1<y1 has a distinct reversal partner
        total += 2*ways if x[1] < y[1] else ways
    return total

expected={
 7:(7776,14,(1,6,6,0,36,0,216,0,1296,0)),
 8:(16807,16,(1,7,7,0,49,0,343,0,2401,0)),
 9:(33872,6552,(2,7,12,2,88,0,640,0,4656,0)),
}
for q in (7,8,9):
    best,wins,states=solve(q)
    # Deduplicate endpoints where m4=0 (handled above), then retain exact tuples.
    wins=sorted(set(wins))
    count=count_codes(q,wins)
    bb,bba=best_blackburn(q)
    assert best==expected[q][0]
    assert count==expected[q][1]
    assert wins==[expected[q][2]], (q,wins)
    print(f"q={q} S={best} N={count} reduced_profile={wins[0]} states={states} best_k5_Blackburn={bb} gap={best-bb}")
print("VERIFY_OK")
