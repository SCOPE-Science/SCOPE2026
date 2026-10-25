# Independent mathematical audit

## correctness

PASS

Depth-j types are exactly finite sets of depth-(j-1) child types, so 2,4,16 possible depth-1,2,3 codes. For each code t the level-two reduction beta(t) follows by mapping child level-two type 0 to level-one 0 and 1,2,3 to 1. Summing distinct-child-demand weights lambda=(1,2,3,4) over all tree edges establishes |V| >= sum_v h(t_v) + lambda_{beta(type(root))}, h=1+D-lambda_beta. Independently reproduced h=(0,0,0,0,1,1,3,3,2,2,4,4,5,5,7,7), all >=0 and 16-distinct-types sum=44. Type 4 forces a path of length three, hence the root must have type >=4, giving root weight >=3, lower bound 47. Independently parsed witness.json: 47 vertices, 46 edges, unique root, all vertices reachable, actual computed tau_3 labels equal supplied labels and cover 0..15; 44+3=47. This verifies constructive upper bound and universal lower bound without enumerating all smaller trees.

## originality

PASS

The finite-model type recursion and bounded bisimulation characteristic formulae are standard, but the simultaneous realization of all sixteen depth-three theories inside one rooted tree minimizes a different resource than pointwise model contraction or inclusion-minimal Herbrand models. No earlier exact 47-node cover was identified in targeted published research.

## value

PASS

Sharp resource cost for one finite rooted tree realizing all depth-three atom-free modal types is a natural finite-model-theory invariant, distinct from the trivial type count and provably larger than shared-state DAG realization; weighted dual inequality and explicit witness explain the gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
