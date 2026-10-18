#!/usr/bin/env python3
"""Independent finite stress test of ordered doubleton matching rigidity."""
import itertools

def relation_matrix(r,digits):
    # 0 full (all four), 1 straight matching, 2 crossed matching.
    n=2*r
    rows=[0]*n
    t=0
    for i in range(r):
        for j in range(i+1,r):
            typ=digits[t];t+=1
            for a in range(2):
                for b in range(2):
                    if typ==0 or b==(a ^ (typ-1)):
                        rows[2*i+a] |= 1<<(2*j+b)
    return rows

def transitive(rows):
    n=len(rows)
    return all((rows[i] | rows[j])==rows[i]
               for i in range(n) for j in range(n) if rows[i] >> j & 1)

def switches(digits,r):
    out=[]; k=0
    for i in range(r):
        for j in range(i+1,r):
            out.append((i,j,digits[k]));k+=1
    return out

def equivalent(a,b,r):
    pairs_a=switches(a,r); pairs_b=switches(b,r)
    for flip in itertools.product((0,1),repeat=r):
        if all(t==0 or ((t-1) ^ flip[i] ^ flip[j]) == (u-1)
               for (i,j,t),(_,_,u) in zip(pairs_a,pairs_b)):
            return True
    return False

def main():
    for r in range(1,6):
        groups={}; accepted=0
        for digits in itertools.product((0,1,2),repeat=r*(r-1)//2):
            rows=relation_matrix(r,digits)
            if not transitive(rows): continue
            accepted+=1
            shape=tuple(d==0 for d in digits)
            if shape not in groups: groups[shape]=digits
            else: assert equivalent(groups[shape],digits,r),(r,groups[shape],digits)
        print(f'doubleton_classes={r} transitive_oriented_templates={accepted} comparison_profiles={len(groups)}')
    print('MATCHING_SKELETONS_OK')
if __name__=='__main__':main()
