#!/usr/bin/env python3

def profiles(n):
    out=[]
    def rec(rem,last,cur):
        if rem==0:
            if len(cur)>=2:
                out.append(tuple(cur))
            return
        for x in range(last,rem+1):
            rec(rem-x,x,cur+[x])
    rec(n,1,[])
    return out


def restricted_growth_strings(n):
    a=[0]*n
    def rec(i,m):
        if i==n:
            yield tuple(a)
            return
        for x in range(m+2):
            a[i]=x
            yield from rec(i+1,max(m,x))
    if n:
        a[0]=0
        yield from rec(1,0)


def part_labels(profile):
    labels=[]
    for i,size in enumerate(profile):
        labels.extend([i]*size)
    return labels


def is_strong_odd(labels, coloring):
    n=len(labels)
    # Properness in a complete multipartite graph.
    for u in range(n):
        for v in range(u+1,n):
            if labels[u] != labels[v] and coloring[u] == coloring[v]:
                return False
    # Every color present in every open neighborhood has odd multiplicity.
    for u in range(n):
        counts={}
        for v in range(n):
            if labels[v] != labels[u]:
                counts[coloring[v]]=counts.get(coloring[v],0)+1
        if any(mult % 2 == 0 for mult in counts.values()):
            return False
    return True


def brute_force(profile):
    labels=part_labels(profile)
    best=len(labels)
    checked=0
    for coloring in restricted_growth_strings(len(labels)):
        checked += 1
        if is_strong_odd(labels,coloring):
            best=min(best,1+max(coloring))
    return best,checked


def formula(profile):
    return len(profile)+sum(size % 2 == 0 for size in profile)


def main():
    profile_count=0
    colorings_checked=0
    for n in range(2,9):
        for profile in profiles(n):
            got,checked=brute_force(profile)
            want=formula(profile)
            assert got == want,(profile,got,want)
            profile_count += 1
            colorings_checked += checked
    print(f"ALL CHECKS PASSED; profiles={profile_count}; canonical_colorings_checked={colorings_checked}; orders=2..8")

if __name__ == '__main__':
    main()
