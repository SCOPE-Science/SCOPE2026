"""Independent vertex-level colour refinement on unequal odd cycle products."""
from collections import Counter, defaultdict


def graph(m, n):
    assert m >= 5 and n > m and m % 2 == n % 2 == 1
    adjacency = [[] for _ in range(m*n)]
    for x in range(m):
        for y in range(n):
            i = x*n+y
            adjacency[i] = [((x+1)%m)*n+y, ((x-1)%m)*n+y,
                            x*n+(y+1)%n, x*n+(y-1)%n]
    return adjacency


def stabilize(adjacency):
    colors = [0] + [1]*(len(adjacency)-1)
    rounds = 0
    while True:
        signatures = [(colors[i], tuple(sorted(Counter(colors[j] for j in nbr).items())))
                      for i, nbr in enumerate(adjacency)]
        ids = {s: k for k, s in enumerate(sorted(set(signatures)))}
        newer = [ids[s] for s in signatures]
        if len(set(newer)) == len(set(colors)):
            return colors, rounds
        colors = newer
        rounds += 1


def check():
    cases = vertices = classes = 0
    for m in range(5, 24, 2):
        for n in range(m+2, 36, 2):
            adjacency = graph(m, n)
            colors, rounds = stabilize(adjacency)
            classes_by_color, colors_by_profile = defaultdict(set), defaultdict(set)
            for x in range(m):
                for y in range(n):
                    i = x*n+y
                    profile = (min(x, m-x), min(y, n-y))
                    classes_by_color[colors[i]].add(profile)
                    colors_by_profile[profile].add(colors[i])
            assert all(len(s) == 1 for s in classes_by_color.values()), (m,n,rounds,'merged')
            assert all(len(s) == 1 for s in colors_by_profile.values()), (m,n,rounds,'split')
            count = ((m+1)//2)*((n+1)//2)
            assert count == len(classes_by_color), (m, n, count)
            cases += 1
            vertices += m*n
            classes += count
    print(f'DIRECT_PASS cases={cases} vertices={vertices} profiles={classes}')


if __name__ == '__main__':
    check()
