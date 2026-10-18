"""Direct finite checks for the loose-hypercycle edge-status theorem.
No third-party packages required: python3 verify.py.
"""
from collections import Counter
from itertools import product


def predicted_fiber(k, r, status):
    """Status 0=empty edge, 1=mixed edge, 2=full edge."""
    assert k >= 3 and r >= 3 and len(status) == r
    b = (1 << (k - 1)) - 1
    definite = [i for i, s in enumerate(status) if s != 1]
    if not definite:
        return b ** r + (-1) ** r
    ans = 1
    for j, i in enumerate(definite):
        nxt = definite[(j + 1) % len(definite)]
        ell = (nxt - i - 1) % r
        same = status[i] == status[nxt]
        ans *= (b ** ell + ((-1) ** ell if same else -(-1) ** ell)) // 2
    return ans


def observed_fibers(k, r):
    # r cyclic core vertices, (k-2) private vertices on each edge.
    vertices = r * (k - 1)
    groups = [tuple([i, (i + 1) % r] + list(range(r+i*(k-2), r+(i+1)*(k-2)))) for i in range(r)]
    result = Counter()
    for mask in range(1 << vertices):
        code = 0
        power = 1
        for e in groups:
            pop = sum((mask >> v) & 1 for v in e)
            s = 0 if pop == 0 else (2 if pop == k else 1)
            code += s * power
            power *= 3
        result[code] += 1
    return result


def check(k, r):
    obs = observed_fibers(k, r)
    b = (1 << (k-1))-1
    all_mixed = sum(3**j for j in range(r))
    big = b**r + (-1)**r
    second = (b**(r-1) + (-1)**(r-1))//2
    ones = [sum((2 if j==i and bit else 0 if j==i else 1)*3**j for j in range(r)) for i in range(r) for bit in (0,1)]
    assert obs[all_mixed] == big
    assert set(ones) == {c for c,v in obs.items() if v == second}
    assert all((v < second) for c,v in obs.items() if c != all_mixed and c not in ones)
    # c_r=(1+sqrt(2))^r+(1-sqrt(2))^r + 1, recurrence pell lucas: 2,2,6,14,...
    pell_0,pell_1=2,2
    if r==0: pell=pell_0
    else:
        for _ in range(2,r+1): pell_0,pell_1=pell_1,2*pell_1+pell_0
        pell=pell_1
    assert len(obs)==pell+1,(len(obs),pell+1)
    assert sum(obs.values())==2**(r*(k-1))
    for symbols in product((0,1,2), repeat=r):
        code = sum(s*3**i for i,s in enumerate(symbols))
        expected = predicted_fiber(k,r,symbols)
        assert obs.get(code,0)==expected,(k,r,code,obs.get(code,0),expected)
    print('CASE',k,r,'subsets',1<<(r*(k-1)), 'observations',len(obs), 'maximum',big,'runnerup',second,'runnerup_count',2*r,'PASS')
    return 1 << (r*(k-1))


if __name__=='__main__':
    total=0
    for k,r_values in ((3,range(3,8)),(4,range(3,6)),(5,range(3,5)),(6,range(3,4))):
        for r in r_values:
            total += check(k,r)
    print('VERIFY_OK subsets',total, 'all_status_fibers=PASS','unique_maximum=PASS','exact_runnerup=PASS','observation_count=PASS')
