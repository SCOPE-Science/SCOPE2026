"""Check the three-cone cover identity independently on finite tournament examples."""
from itertools import combinations

def subset_masks(mask):
    out = {0}
    bit = 1
    while bit <= mask:
        if mask & bit:
            out |= {x | bit for x in tuple(out)}
        bit <<= 1
    return out

def neighborhood_faces(rows):
    family = {0}
    for row in rows:
        mask = sum(1 << j for j in row)
        family |= subset_masks(mask)
    return family

def cases():
    yield 'cyclic_3', [{(i+1)%3} for i in range(3)]
    yield 'transitive_3', [set(range(i+1,3)) for i in range(3)]
    yield 'cyclic_5', [{(i+1)%5,(i+2)%5} for i in range(5)]
    b=[{(i+1)%3} for i in range(3)]
    r=[]
    for h in range(3):
        for u in range(3):
            r.append({h*3+v for v in b[u]} | {(h+1)%3*3+v for v in range(3)})
    yield 'cyclic_3_squared', r

def test(name, rows):
    m=len(rows)
    out=[]
    for h in range(3):
        for u in range(m):
            out.append({h*m+v for v in rows[u]}|{((h+1)%3)*m+v for v in range(m)})
    direct=neighborhood_faces(out)
    local=neighborhood_faces(rows)
    cover=[]
    full=(1<<m)-1
    for h in range(3):
        k=set()
        for a in local:
            for b in subset_masks(full):
                k.add((a << (h*m)) | (b << (((h+1)%3)*m)))
        cover.append(k)
    assert set.union(*cover)==direct
    for h in range(3):
        intersection=cover[h] & cover[(h+1)%3]
        expected={a << (((h+1)%3)*m) for a in local}
        assert intersection==expected, (name,h)
    assert cover[0]&cover[1]&cover[2]=={0}
    print(name, 'direct_faces=', len(direct), 'union_faces=', len(set.union(*cover)), 'pair_faces=', len(local),'PASS')

if __name__=='__main__':
    for name,rows in cases():
        test(name, rows)
    print('ALL_COVER_CHECKS_PASS')
