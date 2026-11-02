"""Independent exact finite extension-set computation for graph 1-subdivisions."""
from functools import lru_cache

def representative_moves(n, sequence):
    used = {x for obj in sequence for x in obj[1:]}
    spare = [i for i in range(n) if i not in used][:2]
    old = sorted(used)
    moves = [('point',i) for i in old]
    if spare: moves.append(('point',spare[0]))
    from itertools import combinations
    moves += [('line',i,j) for i,j in combinations(old,2)]
    if spare: moves += [('line',*sorted((i,spare[0]))) for i in old]
    if len(spare)>1: moves.append(('line',*spare))
    return tuple(moves)

def support(obj): return obj[1:]
def incident(a,b):
    return (a[0]!=b[0] and
            ((len(support(a))==1 and support(a)[0] in support(b)) or
             (len(support(b))==1 and support(b)[0] in support(a))))

@lru_cache(maxsize=None)
def qtype(n,sequence,rounds):
    atoms = tuple((a==b,incident(a,b)) for a in sequence for b in sequence)
    if rounds==0: return (atoms, frozenset())
    children=frozenset(qtype(n,sequence+(move,),rounds-1) for move in representative_moves(n,sequence))
    return (atoms,children)

def main():
    for r,cut in ((1,1),(2,3),(3,4),(4,5),(5,7)):
        reps=[];classes=[]
        for n in range(1,11):
            typ=qtype(n,(),r)
            if typ not in reps:reps.append(typ)
            classes.append(reps.index(typ)+1)
            print(f'r={r} n={n} vertices={n*(n+1)//2} class={classes[-1]}')
        assert classes==[min(n,cut) for n in range(1,11)], (r,classes)
        print(f'RANK_{r}_PASS cutoff={cut} classes={len(reps)}')
    print(f'COMPLETE_PROFILE_PASS states={qtype.cache_info().currsize}')
if __name__=='__main__':main()
