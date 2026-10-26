"""Exact checks for a bond-percolation epidemic monitoring theorem on cycles.

Only standard-library Python is required. All probabilities are exact rational numbers.
"""
import itertools
import json
from fractions import Fraction


def H(ell, p):
    return sum(((1-p**j)*(1-p**(ell+1-j)) for j in range(1, ell+1)), Fraction(0))


def gap_vector(n, sensors):
    s = sorted(sensors)
    return tuple((s[(i+1)%len(s)]-s[i]-1) % n for i in range(len(s)))


def components(n, edge_mask):
    parent = list(range(n))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(n):
        if (edge_mask >> i) & 1:
            u, v = root(i), root((i+1)%n)
            parent[u] = v
    return tuple(sum(1<<v for v in range(n) if root(v) == root(u)) for u in range(n))


def check():
    cases = 0
    incidence_evaluations = 0
    placement_optima = 0
    two_sensor_moment_cases = 0
    for n in range(3,9):
        for a in (1,2,3):
            q = 4
            p = Fraction(a,q)
            graph_states = []
            for edge_mask in range(1<<n):
                number_open = edge_mask.bit_count()
                weight = a**number_open*(q-a)**(n-number_open)
                graph_states.append((weight,components(n,edge_mask)))
            T = 1 + 2*sum((p**j for j in range(1,n)),Fraction(0)) - (n-1)*p**n
            for k in range(1,n):
                for sensors in itertools.combinations(range(n),k):
                    smask = sum(1<<s for s in sensors)
                    detection_num = 0
                    infected_sensor_num = 0
                    all_sensor_num = 0
                    for weight,comp in graph_states:
                        for root_component in comp:
                            reached = (root_component&smask).bit_count()
                            detection_num += weight*(reached>0)
                            if k == 2:
                                infected_sensor_num += weight*reached
                                all_sensor_num += weight*(reached==2)
                            incidence_evaluations += 1
                    detection = Fraction(detection_num,n*q**n)
                    gaps = gap_vector(n,sensors)
                    expected = 1-sum((H(ell,p) for ell in gaps),Fraction(0))/n
                    assert detection == expected, (n,k,sensors,detection,expected)
                    if k == 2:
                        mean = Fraction(infected_sensor_num,n*q**n)
                        two = Fraction(all_sensor_num,n*q**n)
                        assert mean == 2*T/n
                        assert two == mean-detection
                        two_sensor_moment_cases += 1
                    cases += 1
                    if max(gaps)-min(gaps)<=1:
                        target_H = min(sum((H(g,p) for g in gap_vector(n,S)),Fraction(0)) for S in itertools.combinations(range(n),k))
                        assert sum((H(g,p) for g in gaps),Fraction(0)) == target_H
                        placement_optima += 1
            for ell in range(n-2):
                assert H(ell+2,p)-2*H(ell+1,p)+H(ell,p) == (ell+2)*p**(ell+1)*(1-p)**2
    for n in range(3,80):
        for k in range(1,n):
            N=n-k
            balanced=[N//k+(i<N%k) for i in range(k)]
            clustered=[N]+[0]*(k-1)
            for a in (1,2,3):
                p=Fraction(a,4)
                bh=sum((H(g,p) for g in balanced),Fraction(0))
                ch=sum((H(g,p) for g in clustered),Fraction(0))
                assert bh<=ch
    p=Fraction(1,2)
    n=6
    T=1+2*sum((p**j for j in range(1,n)),Fraction(0))-(n-1)*p**n
    E=2*T/n
    D_cluster=1-(H(0,p)+H(4,p))/n
    D_balanced=1-2*H(2,p)/n
    assert (D_cluster,D_balanced,E-D_cluster,E-D_balanced)==(Fraction(5,8),Fraction(3,4),Fraction(21,64),Fraction(13,64))
    return {
        'status':'exact_checks_passed',
        'cycle_orders_exhausted':'3..8',
        'edge_retention_probabilities':['1/4','1/2','3/4'],
        'sensor_placements_exactly_checked':cases,
        'weighted_seed_component_evaluations':incidence_evaluations,
        'balanced_optimality_checks':placement_optima,
        'two_sensor_moment_checks':two_sensor_moment_cases,
        'additional_integer_range':'3<=n<80; 1<=k<n',
        'six_cycle_at_p_half':{
            'adjacent_P_any':'5/8',
            'balanced_P_any':'3/4',
            'adjacent_P_both':'21/64',
            'balanced_P_both':'13/64'
        }
    }

if __name__ == '__main__':
    print(json.dumps(check(),sort_keys=True,separators=(',',':')))
