"""Independent four-block Pasch and equitable-partition checks; stdlib only."""
from itertools import combinations
from collections import defaultdict, Counter


def projective_blocks():
    return [frozenset((a,b,a^b)) for a in range(1,16) for b in range(a+1,16) if a < (a^b) and b < (a^b)]


def bose_blocks():
    output=[]
    for n in range(5): output.append(frozenset(((n,0),(n,1),(n,2))))
    for level in range(3):
        for x in range(5):
            for y in range(x+1,5):
                output.append(frozenset(((x,level),(y,level),(3*(x+y)%5,(level+1)%3))))
    return output


def block_quad_pasch(blocks):
    found=[]
    for i,j,k,l in combinations(range(len(blocks)),4):
        four=[blocks[i],blocks[j],blocks[k],blocks[l]]
        merged=set().union(*four)
        if len(merged)!=6: continue
        if all(sum(v in B for B in four)==2 for v in merged):
            found.append((i,j,k,l))
    return found


def validate_equitable(blocks, marks):
    all_points=set().union(*blocks)
    chosen_line=next(B for B in blocks if set(marks).issubset(B))
    outside=all_points-chosen_line
    remainder=chosen_line-set(marks)
    point_cells={('mark',i):{a} for i,a in enumerate(marks)}
    if remainder: point_cells[('remainder',)]=remainder
    if outside: point_cells[('outside',)]=outside
    block_cells={('chosen',):{i for i,B in enumerate(blocks) if B==chosen_line}}
    for i,a in enumerate(marks):
        block_cells[('through_mark',i)]={j for j,B in enumerate(blocks) if a in B and B != chosen_line}
    if remainder:
        block_cells[('through_remainder',)]={j for j,B in enumerate(blocks) if B != chosen_line and bool(B & remainder)}
    block_cells[('away',)]={j for j,B in enumerate(blocks) if not B & chosen_line}
    assert sum(len(cell) for cell in point_cells.values())==len(all_points)
    assert sum(len(cell) for cell in block_cells.values())==len(blocks)
    assert all(not A.intersection(B) for A,B in combinations(point_cells.values(),2))
    assert all(not A.intersection(B) for A,B in combinations(block_cells.values(),2))
    # Compute all incidence degree matrices, requiring each cell to be uniform.
    table={}
    for key,pts in point_cells.items():
        if not pts: continue
        row=[]
        for label,ids in block_cells.items():
            degrees=[sum(p in blocks[i] for i in ids) for p in pts]
            assert len(set(degrees)) == 1, (key,label,Counter(degrees))
            row.append((str(label),degrees[0],len(ids)))
        table[str(key)]=(len(pts),tuple(row))
    return table


def main():
    A=projective_blocks()
    B=bose_blocks()
    assert len(A)==len(set(A))==len(B)==len(set(B))==35
    pa=block_quad_pasch(A)
    pb=block_quad_pasch(B)
    assert len(pa)==105 and len(pb)==0,(len(pa),len(pb))
    print('FOUR-BLOCK PASCH PASS: projective=105, Bose=0')
    PA=sorted(set().union(*A),key=repr)
    PB=sorted(set().union(*B),key=repr)
    for t in (1,2,3):
        # t=3 uses whole blocks as anchors; for t=1,2 any point choice lies in some block.
        ans=[]
        for blocks,points in ((A,PA),(B,PB)):
            anchor_sets=list(combinations(points,t)) if t<3 else [tuple(sorted(L,key=repr)) for L in blocks]
            profiles=[validate_equitable(blocks,s) for s in anchor_sets]
            assert all(p==profiles[0] for p in profiles)
            ans.append(profiles[0])
        assert ans[0]==ans[1]
        print(f'UNIFORM EQUITABLE PASS: {t} collinear mark(s), all choices in both systems')
    print('INDEPENDENT CERTIFICATE PASS')

if __name__=='__main__':main()
