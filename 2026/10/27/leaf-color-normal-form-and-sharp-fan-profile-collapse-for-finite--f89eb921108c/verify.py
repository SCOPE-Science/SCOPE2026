"""Independent finite verification of rooted-tree / fan-frame bounded-morphism formulas.

All computations use Python's standard library. Execute: python fan_frame_verify.py
"""
import itertools
import json
from math import factorial


def data(parents):
    n = len(parents) + 1
    child = [[] for _ in range(n)]
    for v, p in enumerate(parents, start=1):
        child[p].append(v)
    desc = [set() for _ in range(n)]
    for v in reversed(range(n)):
        desc[v].add(v)
        for u in child[v]:
            desc[v].update(desc[u])
    leaves = [v for v in range(n) if not child[v]]
    return child, desc, leaves


def direct(parents, k):
    child, desc, leaves = data(parents)
    n = len(child)
    ans = 0
    for labels in itertools.product(range(k+1), repeat=n):
        # Colors 1..k are the maximal worlds; color 0 is the root of the target fan.
        valid = True
        for v in range(n):
            c = labels[v]
            if c == 0:
                if any(not any(labels[w] == i for w in desc[v]) for i in range(1, k+1)):
                    valid = False
                    break
            elif any(labels[w] != c for w in desc[v]):
                valid = False
                break
        if valid:
            ans += 1
    return ans


def from_leaves(parents, k):
    child, desc, leaves = data(parents)
    ans = 0
    for col in itertools.product(range(k), repeat=len(leaves)):
        mapping = dict(zip(leaves, col))
        if all(len({mapping[w] for w in leaves if w in desc[v]}) in (1, k)
               for v in range(len(child))):
            ans += 1
    return ans


def recurrence(parents, k):
    child, _, _ = data(parents)
    f = [0] * len(child)
    def onto(n, r):
        return sum((-1)**j * __import__('math').comb(r, j) * (r-j)**n for j in range(r+1))
    for v in reversed(range(len(child))):
        if not child[v]:
            f[v] = k
        else:
            prod = 1
            for w in child[v]:
                prod *= f[w]
            f[v] = k + prod - k**len(child[v]) + onto(len(child[v]), k)
    return f[0]


def run():
    direct_checks = 0
    spectrum_checks = 0
    ternary_checks = 0
    max_strict_checks = 0
    for n in range(1, 7):
        choices = [range(i) for i in range(1, n)]
        for parents in itertools.product(*choices):
            child, desc, leaves = data(parents)
            ell = len(leaves)
            delta = max(map(len, child))
            for k in (2, 3, 4):
                exact = direct(parents, k)
                leaf_ct = from_leaves(parents, k)
                rec = recurrence(parents, k)
                assert exact == leaf_ct == rec, (parents, k, exact, leaf_ct, rec)
                direct_checks += 1
                assert (exact > k) == (k <= delta), (parents,k,exact,delta)
                spectrum_checks += 1
                if k == 2:
                    assert exact == 2**ell, (parents, exact)
                if k == 3 and sum(len(v)==3 for v in child) == 1 and all(len(v)<=3 for v in child):
                    q = next(i for i, x in enumerate(child) if len(x)==3)
                    b = sum(len(child[v])==2 and q in desc[v] and q != v for v in range(n))
                    assert exact == 3 + 6*(3**b), (parents,exact,b)
                    ternary_checks += 1
                if k >= 3 and ell >= k:
                    # Maximum is obtained at a star, with unary subdivisions allowed.
                    star = k + sum((-1)**j * __import__('math').comb(k,j)*(k-j)**ell for j in range(k+1))
                    assert exact <= star
                    is_subdivided_star = not any(
                        len(child[v])>=2 and any(len({w for w in leaves if w in desc[u]})>=2 for u in child[v])
                        for v in range(n))
                    assert (exact == star) == is_subdivided_star, (parents,k,exact,star,is_subdivided_star)
                    max_strict_checks += 1
    # Two distinct full-binary rooted trees with equal four-leaf spectra.
    balanced = (0,0,1,1,2,2) # 7 vertices: root has two internal children, each two leaf children
    caterpillar = (0,0,1,1,3,3) # a nonisomorphic full-binary rooted shape
    bchild, _, bl = data(balanced)
    cchild, _, cl = data(caterpillar)
    assert len(bl) == len(cl) == 4
    for k in range(2,7):
        assert recurrence(balanced,k) == recurrence(caterpillar,k) == (2**4 if k==2 else k)
    print(json.dumps({"status":"ALL_CHECKS_PASS", "independent_direct_map_vs_leaf_and_recursion":direct_checks,
                      "branch_threshold":spectrum_checks,
                      "unique_trivalent_depth_formula":ternary_checks,
                      "sharp_star_extremizers":max_strict_checks,
                      "binary_shape_collision_four_leaves":True}, sort_keys=True))

if __name__ == '__main__':
    run()
