"""Complete exact census of binary length-six comma-free codebooks.

The binary alphabet, the 9 cyclic primitive necklace classes, and the
unrestricted and one-bit-detecting constraint systems are generated anew.
Requires only Python's standard library.
"""
import collections
import itertools
import pathlib
import sys

def rotate(s,j):
    return s[j:]+s[:j]

def necklaces():
    unused={format(i,'06b') for i in range(64) if len({rotate(format(i,'06b'),j) for j in range(6)})==6}
    groups=[]
    while unused:
        w=min(unused)
        group=tuple(sorted({rotate(w,j) for j in range(6)}))
        unused.difference_update(group)
        groups.append(group)
    assert len(groups)==9 and all(len(g)==6 for g in groups)
    assert sum(map(len,groups))==54
    return groups

def cross(a,b):
    return {a[k:]+b[:k] for k in range(1,6)}

def hamming(a,b):
    return sum(u!=v for u,v in zip(a,b))

def valid(C,detect):
    assert all(len(w)==6 and set(w)<={'0','1'} for w in C)
    if detect and any(hamming(a,b)<2 for a,b in itertools.combinations(C,2)):
        return False
    return all(a[k:]+b[:k] not in C for a in C for b in C for k in range(1,6))

def enumerate_all(detect):
    groups=necklaces()
    counter=collections.Counter()
    output=[]
    def search(index,selected,forbidden):
        if index==len(groups):
            counter[len(selected)]+=1
            if (not detect and len(selected)==9) or (detect and len(selected)==7):
                output.append(tuple(sorted(selected)))
            return
        if detect:
            search(index+1,selected,forbidden)
        for w in groups[index]:
            if w in forbidden:
                continue
            if detect and any(hamming(w,p)<2 for p in selected):
                continue
            new_cross=cross(w,w)
            for p in selected:
                new_cross.update(cross(w,p))
                new_cross.update(cross(p,w))
            if any(v in new_cross for v in selected) or w in new_cross:
                continue
            search(index+1,selected+(w,),forbidden|new_cross)
    search(0,(),set())
    assert len(output)==len(set(output))
    return counter, sorted(output)

def image(C,reverse,complement):
    def transform(w):
        if reverse:w=w[::-1]
        if complement:w=''.join('1' if x=='0' else '0' for x in w)
        return w
    return tuple(sorted(transform(w) for w in C))

def inspect_group(codes):
    collection=set(codes)
    assert all(all(image(C,r,c) in collection for r in (0,1) for c in (0,1)) for C in codes)
    fixed=collections.Counter()
    orbits=set()
    for C in codes:
        orbit={image(C,r,c) for r in (0,1) for c in (0,1)}
        fixed[len(orbit)]+=1
        orbits.add(min(orbit))
    return fixed,len(orbits)

def main():
    unrestricted,full=enumerate_all(False)
    detected,good=enumerate_all(True)
    assert unrestricted=={9:1972},unrestricted
    assert detected=={0:1,1:54,2:1090,3:8410,4:23892,5:22374,6:5712,7:272},detected
    assert len(full)==1972 and len(good)==272
    assert inspect_group(full)==(collections.Counter({4:1972}),493)
    assert inspect_group(good)==(collections.Counter({4:272}),68)
    assert all(valid(C,False) for C in full)
    assert all(valid(C,True) for C in good)
    assert all(min(hamming(a,b) for a,b in itertools.combinations(C,2))==1 for C in full)
    for filename,items in [('full_codebooks.tsv',full),('detecting_codebooks.tsv',good)]:
        path=pathlib.Path(__file__).resolve().parent/filename
        expected=''.join('\t'.join(C)+'\n' for C in items)
        assert path.read_text(encoding='utf-8')==expected,(filename,'wrong inventory')
    print('VERIFY_OK: unrestricted=9 / 1972 codebooks / 493 symmetry orbits; detecting=7 / 272 codebooks / 68 symmetry orbits')

if __name__=='__main__':main()
