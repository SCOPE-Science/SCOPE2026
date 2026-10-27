#!/usr/bin/env python3
"""Exact finite-state integer verification for prefix extrema of 7-rarefied Thue-Morse sums."""

def next_state(state,depth):
    T,H,B=state
    shift=pow(2,depth,7)
    return ([T[j]-T[(j-shift)%7] for j in range(7)],
            [max(H[j],T[j]-B[(j-shift)%7]) for j in range(7)],
            [min(B[j],T[j]-H[(j-shift)%7]) for j in range(7)])

def generate(depth):
    state=([1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0]*7)
    out=[state]
    for r in range(depth):
        state=next_state(state,r)
        out.append(state)
    return out

def check_direct(depth):
    states=generate(depth)
    for r in range(depth+1):
        t=[0]*7
        maxima=[0]*7
        minima=[0]*7
        for n in range(1<<r):
            j=n%7
            t[j]+= 1 if n.bit_count()%2==0 else -1
            maxima[j]=max(maxima[j],t[j]);minima[j]=min(minima[j],t[j])
        assert (t,maxima,minima)==states[r],('direct',r)
    return states

def main():
    states=check_direct(16)
    states=generate(125)
    for s in (7,8):
        T,H,B=states[s]; TT,HH,BB=states[s+12]
        assert TT==[49*x for x in T]
        assert HH==[49*x+32 for x in H]
        assert BB==[49*x-32 for x in B]
    for r in range(7,114):
        T,H,B=states[r];TT,HH,BB=states[r+12]
        assert TT==[49*x for x in T]
        assert HH==[49*x+32 for x in H]
        assert BB==[49*x-32 for x in B]
    print('TABLE r7',states[7]);print('TABLE r19',states[19])
    print('EXAMPLES r7',states[7][1][0],states[7][2][0],'r19',states[19][1][0],states[19][2][0])
    print('VERIFY_OK: 7-residue integer depth-7/19 certificate, direct 131071-prefix test, 107 further levels')
if __name__=='__main__':main()
