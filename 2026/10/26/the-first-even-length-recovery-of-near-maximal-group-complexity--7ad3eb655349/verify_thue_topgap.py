"""Exhaustive finite verification of top group-complexity gaps.
Only Python standard library is required. Coordinate permutations use 0-based indexing.
"""
from itertools import permutations

def mu(s):
    return ''.join('01' if x=='0' else '10' for x in s)

def morph(s,t):
    for _ in range(t): s=mu(s)
    return s

def factors(n):
    assert set(morph('0',5)[i:i+2] for i in range(31)) == {'00','01','10','11'}
    # Every two-letter factor occurs in the fixed point; length-32 images
    # of adjacent letters cover ALL factors of length <= 32.
    blocks=[morph(u+v,5) for u in '01' for v in '01']
    return set().union(*(set(t[i:i+n] for i in range(len(t)-n+1)) for t in blocks))

def action(s,p):
    return ''.join(s[p[i]] for i in range(len(p)))

def cyclic_class_count(F,p):
    visited=set();k=0
    for s in F:
        if s in visited:continue
        orbit={s};t=action(s,p)
        while t!=s:
            orbit.add(t); t=action(t,p)
        intersection=orbit.intersection(F)
        assert intersection
        visited.update(intersection);k+=1
    return k

def main():
    for n in (4,6,8):
        F=factors(n);target=len(F)-1
        longword=morph('0',12)
        check={longword[i:i+n] for i in range(len(longword)-n+1)}
        assert check==F, (n,F^check)
        para={s.count('1') for s in F}
        perms=list(permutations(range(n))) if n<=6 else []
        qualifying=[p for p in perms if cyclic_class_count(F,p)==target]
        print('n',n,'factor_count',len(F),'abelian',len(para),'tested_permutations',len(perms),'p_minus_1_cyclic_witnesses',len(qualifying) if n<=6 else 'not_tested')
        if n<=6:assert not qualifying
    F=factors(8)
    sigma=(1,0,7,4,3,6,5,2)
    assert tuple(sigma[sigma[i]] for i in range(8))==tuple(range(8))
    inter=[]; seen=set()
    for s in sorted(F):
        if s in seen:continue
        t=action(s,sigma)
        C={s,t}.intersection(F)
        seen.update(C)
        if len(C)>1:inter.append(sorted(C))
    assert inter==[['01001011','10110100']],inter
    assert cyclic_class_count(F,sigma)==21
    assert len(F)==22
    print('n8 involution:',sigma,'only_moved_factor_pair:',inter,'orbit_count:',cyclic_class_count(F,sigma))
    print('n8 factors:',','.join(sorted(F)))
    print('VERIFIED')
if __name__=='__main__':main()
