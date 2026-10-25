"""Exact finite checks for moments of adjacent arcs and opener-closer peaks in random perfect matchings.
No external dependencies. Run: python verify.py
"""
from fractions import Fraction as Q


def matchings(vertices):
    if not vertices:
        yield ()
        return
    first, *tail = vertices
    for j, partner in enumerate(tail):
        for rest in matchings(tail[:j] + tail[j+1:]):
            yield ((first, partner),) + rest


def score(matching, n):
    openers = {a for a, _ in matching}
    closers = {b for _, b in matching}
    s = sum(b == a + 1 for a, b in matching)
    l = sum(i in openers and (i + 1) in closers for i in range(1, 2*n))
    return s, l


def moments(n):
    total = sx = lx = ss = ll = sl = 0
    count_short = [0] * (2*n-1)
    count_A_short = [0] * (2*n-1)
    for m in matchings(list(range(1, 2*n+1))):
        total += 1
        s, l = score(m, n)
        sx += s; lx += l; ss += s*s; ll += l*l; sl += s*l
        short = {a for a, b in m if b == a+1}
        for i in short:
            count_short[i-1] += 1
            count_A_short[i-1] += l-s
    E_S, E_L = Q(sx,total), Q(lx,total)
    V_S, V_L = Q(ss,total)-E_S*E_S, Q(ll,total)-E_L*E_L
    C_SL = Q(sl,total)-E_S*E_L
    C_SA = C_SL-V_S
    assert E_S == 1
    assert E_L == Q(n+2, 3)
    assert V_S == Q(2*n-2, 2*n-1)
    assert V_L == Q(2*(n*n-1), 9*(2*n-1))
    assert C_SL == Q(n-1, 2*n-1)
    assert C_SA == -Q(n-1, 2*n-1)
    assert C_SL/V_S == Q(1,2)
    assert  C_SL*C_SL/(V_S*V_L) == Q(9,4*(n+1))
    for i in range(1, 2*n):
        assert Q(count_short[i-1], total) == Q(1, 2*n-1)
        observed = Q(count_A_short[i-1], count_short[i-1])
        if i in (1, 2*n-1): expected = Q(n-2,3)
        elif n == 2: expected = Q(0)
        else: expected = Q(n-2,3)-Q((i-2)*(2*n-i-2),(2*n-3)*(2*n-5))
        assert observed == expected, (n,i,observed,expected)
    return total


def check_eulerian_recurrence(limit=200):
    mu=Q(1)
    sec=Q(1)
    for n in range(2,limit+1):
        old_mu,old_sec=mu,sec
        mu=Q(2*n-2,2*n-1)*old_mu+Q(n,2*n-1)
        sec=Q(2*n-3,2*n-1)*old_sec+old_mu+Q(n,2*n-1)
        assert mu == Q(n+2,3)
        assert sec-mu*mu == Q(2*(n*n-1), 9*(2*n-1))


def main():
    c=0
    for n in range(2,8):
        c+=moments(n)
    check_eulerian_recurrence()
    print(f'VERIFY_OK {c} exhaustively enumerated perfect matchings; exact positional, covariance, regression, Eulerian recurrence checks')

if __name__=='__main__': main()
