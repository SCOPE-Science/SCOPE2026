"""Exact rational verification of a two-agent, two-good variance-minimization phase classification."""
from fractions import Fraction as F
from itertools import combinations


def solve(matrix, rhs):
    n = len(matrix)
    z = [[F(x) for x in row] + [F(rhs[i])] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if z[i][k]), None)
        if pivot is None:
            return None
        z[k], z[pivot] = z[pivot], z[k]
        factor = z[k][k]
        z[k] = [v/factor for v in z[k]]
        for i in range(n):
            if i != k and z[i][k]:
                mult = z[i][k]
                z[i] = [z[i][j]-mult*z[k][j] for j in range(n+1)]
    return tuple(z[i][-1] for i in range(n))


def data(a, b):
    return ((a, 1-b), (1-a, b), (F(1), F(0)), (F(0), F(1)))


def moments(p, values):
    means = [sum(p[j]*values[j][i] for j in range(4)) for i in range(2)]
    varsum = sum(sum(p[j]*values[j][i]**2 for j in range(4))-means[i]**2 for i in range(2))
    return means, varsum


def enumerate_vertices(a, b):
    values = data(a, b)
    rows = [tuple(F(i==j) for i in range(4)) for j in range(4)]
    rows += [tuple(values[j][i] for j in range(4)) for i in range(2)]
    targets = [F(0)]*4 + [F(1, 2)]*2
    found = set()
    for active in combinations(range(6), 3):
        p = solve([tuple(F(1) for _ in range(4))]+[rows[j] for j in active],
                  [F(1)]+[targets[j] for j in active])
        if p is None or min(p) < 0 or min(moments(p, values)[0]) < F(1, 2):
            continue
        found.add(p)
    return found


def predicted(a, b):
    t1 = 1/(2*(1-a))
    t2 = 1/(2*(1-b))
    return {
        (F(1,2), F(1,2), F(0), F(0)),
        (F(0), F(0), F(1,2), F(1,2)),
        (F(0), t1, F(0), 1-t1),
        (F(0), t2, F(0), 1-t2),
    }


def main():
    tested = 0
    for denominator in range(5, 23):
        for i in range(1, (denominator-1)//2+1):
            for j in range(i+1, (denominator-1)//2+1):
                if j*2 >= denominator:
                    continue
                a,b = F(i,denominator),F(j,denominator)
                verts = enumerate_vertices(a,b)
                assert verts == predicted(a,b), (a,b,verts,predicted(a,b))
                values = data(a,b)
                S = (F(1,2),F(1,2),F(0),F(0))
                Q = (F(0),F(0),F(1,2),F(1,2))
                t1, t2 = 1/(2*(1-a)),1/(2*(1-b))
                H1, H2 = (F(0),t1,F(0),1-t1),(F(0),t2,F(0),1-t2)
                vals = {p:moments(p,values)[1] for p in verts}
                assert vals[Q] > vals[S] and vals[H1] > vals[H2]
                assert min(vals.values()) == min(vals[S],vals[H2])
                x,y=1-2*a,1-2*b
                g = y*(1+(1+x)**2/(1+y)**2)-x*x-y*y
                assert g == 4*(vals[H2]-vals[S])
                tested += 1
    a,b=F(1,10),F(2,5)
    vs=data(a,b); t=1/(2*(1-b))
    ps=(F(1,2),F(1,2),F(0),F(0))
    ph=(F(0),t,F(0),1-t)
    assert t==F(5,6) and moments(ps,vs)[1]==F(17,100)
    assert moments(ph,vs)[1]==F(13,80)
    assert moments(ph,vs)[0]==[F(3,4),F(1,2)]
    print(f'VERIFY_OK exact_parameter_pairs={tested} active_sets_per_pair=20 witness_t={t} fair_variance=17/100 risky_variance=13/80')
if __name__=='__main__': main()
