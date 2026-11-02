"""Construct finite quartet-shattering certificates (standard-library only)."""
import json
from itertools import combinations
from functools import lru_cache
from pathlib import Path

N = 7

def all_unrooted_binary_trees(n):
    """Label n leaves 0..n-1, generate by inserting the largest leaf."""
    initial = {0: {-1}, 1: {-1}, 2: {-1}, -1: {0, 1, 2}}
    trees = [initial]
    for newest in range(3, n):
        newtrees = []
        for adjacency in trees:
            for u in adjacency:
                for v in adjacency[u]:
                    if u >= v:
                        continue
                    copy = {vertex: set(neighbors) for vertex, neighbors in adjacency.items()}
                    w = -newest
                    copy[u].remove(v)
                    copy[v].remove(u)
                    copy[u].add(w)
                    copy[v].add(w)
                    copy[w] = {u, v, newest}
                    copy[newest] = {w}
                    newtrees.append(copy)
        trees = newtrees
    return trees

def all_quartets(n):
    return [pairing for a,b,c,d in combinations(range(n), 4)
            for pairing in ((a,b,c,d), (a,c,b,d), (a,d,b,c))]

def splits_of_tree(adjacency):
    splits = []
    for u in adjacency:
        for v in adjacency[u]:
            if u >= v:
                continue
            visited = {u}
            stack = [u]
            while stack:
                x = stack.pop()
                for y in adjacency[x]:
                    if (x == u and y == v) or (x == v and y == u):
                        continue
                    if y not in visited:
                        visited.add(y)
                        stack.append(y)
            splits.append({x for x in visited if x >= 0})
    return splits

def displayed(splits, q):
    a,b,c,d = q
    return any((a in s and b in s and c not in s and d not in s)
               or (c in s and d in s and a not in s and b not in s)
               for s in splits)

def build():
    trees = all_unrooted_binary_trees(N)
    quartets = all_quartets(N)
    assert len(trees) == 945 and len(quartets) == 105
    masks = [0]*len(quartets)
    for idx,t in enumerate(trees):
        splits = splits_of_tree(t)
        for qindex,q in enumerate(quartets):
            if displayed(splits,q):
                masks[qindex] |= 1 << idx
    all_hypotheses = (1 << len(trees)) - 1
    assert set(mask.bit_count() for mask in masks) == {315}

    # Every shattered nonempty query support can be relabeled so that it contains
    # query zero; subsequent columns are enumerated in increasing index order.
    upper_nodes = 0
    def vc_find(depth, pattern_blocks, last, chosen):
        nonlocal upper_nodes
        upper_nodes += 1
        if len(chosen) == depth:
            return chosen
        for j in range(last+1,len(masks)):
            mask = masks[j]
            next_blocks=[]
            for block in pattern_blocks:
                plus,minus = block & mask, block & ~mask
                if not plus or not minus:
                    break
                next_blocks.extend((minus,plus))
            else:
                answer=vc_find(depth,next_blocks,j,chosen+[j])
                if answer is not None:return answer
        return None

    six_support = vc_find(6,[all_hypotheses & ~masks[0], all_hypotheses & masks[0]],0,[0])
    assert six_support is not None
    upper_nodes=0
    seven_support=vc_find(7,[all_hypotheses & ~masks[0],all_hypotheses & masks[0]],0,[0])
    assert seven_support is None
    assert upper_nodes == 206992,upper_nodes

    pattern_witnesses=[]
    for pattern in range(1<<6):
        s=all_hypotheses
        for bit,j in enumerate(six_support):
            s &= masks[j] if (pattern>>bit)&1 else ~masks[j]
        assert s
        pattern_witnesses.append((s & -s).bit_length()-1)
    assert len(set(pattern_witnesses))==64

    @lru_cache(None)
    def can(s, depth):
        if depth == 0:return s!=0
        if s.bit_count() < (1<<depth):return False
        for j,mask in enumerate(masks):
            yes=s&mask;no=s&~mask
            if min(yes.bit_count(),no.bit_count()) < (1<<(depth-1)):
                continue
            if can(no,depth-1) and can(yes,depth-1):
                return True
        return False

    assert can(all_hypotheses,9)
    assert (1<<10)>len(trees)
    decision_nodes=[None]*511
    leaf_witnesses=[None]*512
    def build_tree(s,depth,idx):
        if depth==0:
            leaf_witnesses[idx-511] = (s & -s).bit_length()-1
            return
        for j,mask in enumerate(masks):
            no=s&~mask;yes=s&mask
            if min(no.bit_count(),yes.bit_count()) < 1<<(depth-1):continue
            if can(no,depth-1) and can(yes,depth-1):
                decision_nodes[idx]=j
                build_tree(no,depth-1,2*idx+1)
                build_tree(yes,depth-1,2*idx+2)
                return
        raise AssertionError('Unable to extract a branch')
    build_tree(all_hypotheses,9,0)
    assert None not in decision_nodes and None not in leaf_witnesses
    assert len(set(leaf_witnesses))==512
    obj={
        'schema_version':1,
        'object':'Unrooted binary phylogenetic trees on seven named leaves; Boolean displayed-quartet membership',
        'leaf_labels':list(range(7)),
        'tree_indexing':'Start from the three-leaf star; insert leaves 3,4,5,6 successively onto edges in adjacency insertion order as implemented in construct.py',
        'quartet_indexing':'For each increasing quadruple a<b<c<d, in lexicographic order, query (a,b)|(c,d), then (a,c)|(b,d), then (a,d)|(b,c)',
        'concept_count':len(trees), 'query_count':len(quartets),
        'vc_lower_query_indices':six_support,
        'vc_pattern_tree_indices':pattern_witnesses,
        'vc_upper_seven_supports_from_fixed_first_query':0,
        'vc_upper_search_nodes':upper_nodes,
        'littlestone_depth':9,
        'littlestone_internal_query_indices_heap_order':decision_nodes,
        'littlestone_leaf_tree_indices_heap_order':leaf_witnesses,
        'littlestone_recursion_states':can.cache_info().currsize,
    }
    return obj

if __name__=='__main__':
    output=Path(__file__).with_name('quartet_certificate.json')
    data=build()
    output.write_text(json.dumps(data,separators=(',',':'),sort_keys=True)+'\n',encoding='utf-8')
    print('CONSTRUCTION_PASS',len(data['littlestone_internal_query_indices_heap_order']), len(data['littlestone_leaf_tree_indices_heap_order']), 'VC_upper_states',data['vc_upper_search_nodes'])
