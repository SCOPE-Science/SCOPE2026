"""Independent state-transfer and recurrence check with exact integers.
No external dependencies. Run: python3 verify_transfer.py
"""
from itertools import product


def transfer(n):
    states = ['00','01','10','11']
    counts = {t:int(t != '11') for t in states}
    for _ in range(n-2):
        new = {t:0 for t in states}
        for t,v in counts.items():
            for bit in '01':
                if t + bit != '111':
                    new[t[1]+bit] += v
        counts = new
    return sum(counts[t] for t in states if t != '11')


def recurrence(n):
    a={2:3,3:5,4:9}
    for k in range(5,n+1):
        a[k] = a[k-1]+a[k-2]+a[k-3]
    return a[n]


if __name__=='__main__':
    for n in range(2,101):
        tr=transfer(n)
        assert tr==recurrence(n),(n,tr,recurrence(n))
        if n<=17:
            direct=sum(1 for t in product('01',repeat=n)
                       if '111' not in ''.join(t)
                       and t[:2] != ('1','1') and t[-2:] != ('1','1'))
            assert tr==direct,(n,tr,direct)
    print('TRANSFER_VERIFICATION_OK')
    print('M2..M16',*[transfer(i) for i in range(2,17)])
