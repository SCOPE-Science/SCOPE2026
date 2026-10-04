#!/usr/bin/env python3
import itertools

def formula(a,b,u,k):
    vals=[(a+b)*(u-1)]
    if k>=u:
        vals.append(a*u+min(b*(u-1),k-u))
        vals.append(b*u+min(a*(u-1),k-u))
    if k>=2*u:
        vals.append(min(a*u,k-u)+min(b*u,k-u))
    return max(vals)

def feasible(vals,a,b,u,k):
    A=vals[:a]
    B=vals[a:]
    SA=sum(A); SB=sum(B)
    for x in A:
        if x==u and x+SB>k:
            return False
    for y in B:
        if y==u and y+SA>k:
            return False
    return True

def brute(a,b,u,k):
    best=-1
    for vals in itertools.product(range(u+1), repeat=a+b):
        if feasible(vals,a,b,u,k):
            best=max(best,sum(vals))
    return best

def main():
    cases=0
    assignments=0
    for a in range(1,4):
        for b in range(1,4):
            for u in range(1,4):
                for k in range(0,u*(a+b+1)+1):
                    cases+=1
                    assignments+=(u+1)**(a+b)
                    got=brute(a,b,u,k)
                    want=formula(a,b,u,k)
                    if got!=want:
                        raise SystemExit(f"FAIL a={a} b={b} u={u} k={k}: brute={got} formula={want}")
    assert formula(3,1,2,2)==6
    witness=(2,2,2,0)
    assert feasible(witness,3,1,2,2) and sum(witness)==6
    print(f"ALL CHECKS PASSED; parameter_cases={cases}; assignments_checked={assignments}; a,b_range=1..3; u_range=1..3")

if __name__=='__main__':
    main()
