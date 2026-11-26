# Independent mathematical audit

## correctness

PASS

A graph of statically shattered queries has no cycle: a consistent label choice on the cycle would force cyclic strict inequalities. Consecutive descending blocks, each reversed and using only its own values, give involutions realizing all adjacent labels, proving VC=n−1 even at n=1. Fixed-or-transposed status of the largest letter gives the involution recurrence, and distinct permutations induce distinct strict rank comparisons. Each hypothesis follows one path through a complete tree, so cardinality gives the depth upper bound. Independent replay (python3 /workspace/branches/ec09e412-d310-43a9-af98-389cbfbd9ed6/verify_involutions_independent.py --max-n 10 --output /workspace/branches/ec09e412-d310-43a9-af98-389cbfbd9ed6/independent_check_n1-10.json) validated the frozen JSON under its sorted involution catalogue and explicit query/branch indexing. All paths and distinct witnesses passed; n=10 had 8191 queries and 8192 leaves. The depths are 0,1,2,3,4,6,7,9,11,13. Disjoint contiguous ten-letter blocks with their own shifted value sets allow independent involutions, hence concatenation yields 13s and a gap at least 3s+1. No exact adaptive value beyond n=10 is claimed.

## originality

PASS

The comparison framework, cardinalities and direct-sum technique are not the contribution. The supported distinct result is adaptive saturation for the full involution class through ten, together with the resulting static/adaptive gap for this family; the closest catalogue records concern different hypothesis classes.

## value

PASS

Involutions are a natural inverse-symmetric restriction on total orders, and static shattering does not decide whether a full adaptive tree saturates the information bound. Exact witnesses through ten pin down the first separation and a depth ratio strictly larger than one that can be amplified, rather than just reporting a small numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
