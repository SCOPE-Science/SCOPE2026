"""Exact integer verification of the displayed seven-class and parity law.
Run: python checker.py [prime_upper_bound]
"""
import sys

SETS = {1:(-1,(0,1)), 2:(-1,(1,)),3:(-1,(1,2,5)),
        4:(1,(2,5,6)), 5:(1,(6,)),6:(1,(0,6))}

def primes_through(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[0:2]=b'\x00\x00'
    for p in range(2,int(n**.5)+1):
        if sieve[p]:sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return (p for p in range(2,n+1) if sieve[p])

def check(q):
    r=q%7
    assert r in SETS
    sg, cls=SETS[r]
    squares={pow(a,2,q) for a in range(1,q)}
    chi=lambda x: (1 if x in squares else -1)
    inv=pow(q,-1,7)
    total=0
    # Directly construct the CRT subgroup using its local projections.
    for x in range(1,q):
        eps=chi(x)
        y=x+q*(((eps-x)*inv)%7)
        assert y%q==x and y%7==eps%7 and 1<=y<7*q
        total+=y
    defect=total-7*q*(q-1)//2
    E=sum(chi(x) for x in range(1,q) if x%7 in cls)
    assert 2*defect==sg*7*q*E,(q,defect,E)
    assert E%2==0
    assert defect%(7*q)==0
    assert (defect//(7*q))%2 == (1 if q%28 in (9,13,25) else 0)
    return defect, E

if __name__=='__main__':
    b=int(sys.argv[1]) if len(sys.argv)>1 else 3000
    checked=[]
    for q in primes_through(b):
        if q==7 or q%4!=1:continue
        checked.append((q,*check(q)))
    print('VERIFY_OK', 'prime_upper_bound', b, 'instances',len(checked),
          'balanced_primes',[q for q,d,_ in checked if d==0],
          'examples',checked[:10])
