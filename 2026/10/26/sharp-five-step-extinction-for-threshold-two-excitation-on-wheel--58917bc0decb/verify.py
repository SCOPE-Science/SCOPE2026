"""Independent replay for the sharp deterministic wheel excitable-map extinction theorem.
Standard Python 3. No external packages.
"""
from itertools import product


def update(state):
    """Hub at coordinate 0, rim at coordinates 1,...,n in cyclic order."""
    n = len(state)-1
    hub, ring = state[0], state[1:]
    if hub == 0:
        nxt_hub = int(sum(z == 1 for z in ring) >= 2)
    elif hub == 1:
        nxt_hub = 2
    else:
        nxt_hub = 0
    result=[nxt_hub]
    for i, cur in enumerate(ring):
        if cur == 0:
            stimulated = (hub == 1) + (ring[(i-1)%n] == 1) + (ring[(i+1)%n] == 1)
            result.append(int(stimulated >= 2))
        elif cur == 1:
            result.append(2)
        else:
            result.append(0)
    return tuple(result)


def depth(x):
    z=x
    for t in range(6):
        if not any(z):
            return t
        z=update(z)
    raise AssertionError('no extinction by time five')


def witness(n):
    if n == 4:
        marks={0}
    elif 5 <= n <= 8:
        marks={0,4}
    else:
        marks={0,4,8}
    return (1,)+tuple(int(i in marks) for i in range(n))


def main():
    expected={3:3,4:4,5:4,6:4,7:4,8:5}
    counts={}
    for n in range(3,9):
        histogram=[0]*6
        for state in product(range(3),repeat=n+1):
            d=depth(state)
            histogram[d]+=1
        counts[n]=histogram
        assert max(i for i,c in enumerate(histogram) if c)==expected[n], (n,histogram)
        assert sum(histogram)==3**(n+1)
        print('n=',n,'states=',3**(n+1),'depth histogram=',histogram)
    for n in range(4,81):
        desired=4 if n<=7 else 5
        v=witness(n)
        actual=depth(v)
        assert actual==desired, (n,actual,v)
    print('Witnesses verified for every circumference 4..80')
    print('VERIFY_OK')

if __name__=='__main__':main()
