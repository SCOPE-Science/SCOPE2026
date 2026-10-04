#!/usr/bin/env python3
from itertools import product

MAX_ORDER = 10

def compositions(n):
    if n == 0:
        yield ()
        return
    for mask in range(1 << (n - 1)):
        out=[]
        last=0
        for j in range(n-1):
            if (mask >> j) & 1:
                out.append(j+1-last)
                last=j+1
        out.append(n-last)
        if len(out) >= 2:
            yield tuple(out)

def part_of(ns):
    p=[]
    for i,a in enumerate(ns):
        p += [i]*a
    return p

def is_sdf(vals, parts):
    n=len(vals)
    totals=[0]*len(set(parts))
    for x,p in zip(vals,parts): totals[p]+=x
    whole=sum(vals)
    for v in range(n):
        # N[v] is v together with every vertex outside v's part.
        if whole - totals[parts[v]] + vals[v] < 1:
            return False
    return True

def is_minimal(vals, parts):
    if not is_sdf(vals,parts):
        return False
    for v,x in enumerate(vals):
        if x == 1:
            w=list(vals); w[v]=-1
            if is_sdf(w,parts):
                return False
    return True

def theorem(ns):
    N=sum(ns); L=max(ns); c=N-L
    return N - 2*(c//2)

def construction(ns):
    N=sum(ns); L=max(ns); c=N-L; m=c//2
    ell=ns.index(L)
    parts=part_of(ns)
    vals=[1]*N
    chosen=0
    for v,p in enumerate(parts):
        if p != ell and chosen < m:
            vals[v]=-1; chosen += 1
    assert chosen == m
    return vals,parts

def main():
    profiles=labelings=minimal_count=construction_checks=0
    for n in range(2,MAX_ORDER+1):
        for ns in compositions(n):
            profiles += 1
            parts=part_of(ns)
            best=None
            for bits in product((-1,1), repeat=n):
                labelings += 1
                if is_minimal(bits,parts):
                    minimal_count += 1
                    w=sum(bits)
                    if best is None or w > best: best=w
            want=theorem(ns)
            if best != want:
                raise AssertionError((ns,best,want))
            vals,p=construction(ns)
            construction_checks += 1
            if not is_minimal(vals,p) or sum(vals) != want:
                raise AssertionError(('construction',ns,sum(vals),want))
    print(f'VERIFY_OK graph_profiles={profiles} labelings={labelings} minimal_functions={minimal_count} construction_checks={construction_checks} max_order={MAX_ORDER}')
if __name__ == '__main__': main()
