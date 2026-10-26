"""Independent shortest-path checks for the four-Mersenne pseudo-Frobenius classification.
Run: python verify.py
"""
import heapq

def greedy_coins(t):
    q, r = divmod(t, 7)
    return q + r // 3 + r % 3

def distances(m):
    a = 2**m - 1
    gens = (a, 2*a + 1, 4*a + 3, 8*a + 7)
    infinity = 10**100
    dist = [infinity] * a
    dist[0] = 0
    pq = [(0, 0)]
    while pq:
        w, r = heapq.heappop(pq)
        if w != dist[r]:
            continue
        for x in gens[1:]:
            z = (r+x)%a
            if w+x < dist[z]:
                dist[z] = w+x
                heapq.heappush(pq, (w+x,z))
    return a, gens, dist

def verify():
    for m in range(5, 14):
        a, gens, dist = distances(m)
        assert all(w == a*(r + greedy_coins(r)) + r for r,w in enumerate(dist)), m
        # Apéry maximum criterion, independent from classification rule:
        observed = sorted((dist[r]-a for r in range(a)
            if all(dist[r]+v-a >= dist[(r+v)%a] for v in gens[1:])))
        F = max(dist)-a
        q,s=divmod(a,7)
        if s == 1:
            predicted = sorted((F,F-1,F-2))
        elif s == 3:
            predicted = sorted((F,F-4*(a+1)))
        else:
            predicted = sorted((F,F-1))
        assert observed == predicted, (m, observed, predicted)
        # Check gap property explicitly through residues and positive generators.
        for f in observed:
            assert f < dist[f%a]
            for v in gens:
                assert f+v >= dist[(f+v)%a]
        print('m=%d a=%d type=%d PF=%s' % (m,a,len(observed),observed))
    print('All independently computed Apéry sets and pseudo-Frobenius sets agree.')

if __name__=='__main__':
    verify()
