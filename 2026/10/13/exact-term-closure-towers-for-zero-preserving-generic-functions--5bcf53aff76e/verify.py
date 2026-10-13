#!/usr/bin/env python3
from itertools import product

def recurrence(q,m,arities,steps):
    s=len(arities); d=m; out=[d]
    for _ in range(steps):
        d=m-s+sum(q**(r*d) for r in arities)
        out.append(d)
    return out

def direct_counts(q,m,arities,steps):
    # Count basis growth from the stage construction: at stage n+1, for each
    # operation of arity r add one fresh basis symbol per input tuple in
    # V_n^r \ V_{n-1}^r; the zero tuple is omitted at the first stage.
    dims=[m]
    prev_size=1  # |V_{-1}|, where V_{-1}={0}
    for n in range(steps):
        cur_size=q**dims[-1]
        new=sum(cur_size**r - prev_size**r for r in arities)
        dims.append(dims[-1]+new)
        prev_size=cur_size
    return dims

def check_case(q,m,arities,steps):
    a=recurrence(q,m,arities,steps)
    b=direct_counts(q,m,arities,steps)
    assert a==b,(q,m,arities,a,b)
    # Check telescoping invariant at every constructed step.
    s=len(arities)
    for n in range(len(a)-1):
        assert a[n+1] - sum(q**(r*a[n]) for r in arities) == m-s
    return a

def main():
    cases=[
        (2,1,[1],4),
        (2,2,[1],3),
        (3,1,[1],3),
        (2,1,[2],3),
        (2,1,[1,1],3),
        (2,2,[1,2],2),
        (3,1,[1,2],2),
    ]
    for c in cases:
        vals=check_case(*c)
        print(c, vals)
    assert recurrence(2,1,[1],4)==[1,2,4,16,65536]
    assert recurrence(2,2,[1],3)==[2,5,33,8589934593]
    assert recurrence(2,1,[1,1],3)==[1,3,15,65535]
    print('VERIFY_OK')
if __name__=='__main__': main()
