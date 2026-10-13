#!/usr/bin/env python3
"""Independent transfer-state polynomial and small Möbius sum check."""
from math import factorial
from verify_recurrence import polynomials, formula

def add(a,b):
    q=[0]*max(len(a),len(b))
    for i,v in enumerate(a):q[i]+=v
    for i,v in enumerate(b):q[i]+=v
    return q

def times_x(a,c=1):return [0]+[v*c for v in a]

def transfer(m):
    state={(0,0):[1],(1,0):[0,-2],(1,1):[0,2]}
    for site in range(2,m+1):
        new={}
        for (old_s,old_t),coef in state.items():
            for new_s,new_t in ((0,0),(1,0),(1,1)):
                if old_t==0 and new_t==0:continue
                weight=2 if new_s and not old_s else 1
                if new_s and not new_t:weight*=-1
                candidate=times_x(coef,weight) if new_s else coef
                new[(new_s,new_t)]=add(new.get((new_s,new_t),[]),candidate)
        state=new
    ans=[]
    for coeff in state.values():ans=add(ans,coeff)
    return ans

def direct_mobius(m):
    out=[0]*(m+1)
    for S in range(1<<m):
        runs=sum((S>>i&1) and (i==0 or not (S>>(i-1)&1)) for i in range(m))
        coeff=0
        T=S
        while True:
            if all((T>>j&3)!=0 for j in range(m-1)):
                coeff+=(-1)**(S.bit_count()-T.bit_count())
            if T==0:break
            T=(T-1)&S
        out[S.bit_count()]+=coeff*2**runs
    return out

def main():
    rec=polynomials(81)
    for m in range(1,60):
        got=transfer(m)
        expect=rec[m]
        assert (got+[0]*max(0,len(expect)-len(got))) == (expect+[0]*max(0,len(got)-len(expect))),(m,got,expect)
        if m<=9:assert got==direct_mobius(m),(m,got,direct_mobius(m))
    print('TRANSFER_OK m=1..59, MOBIUS_OK m=1..9')
    print('N20',formula(20,rec))
if __name__=='__main__':main()
