# Independent mathematical audit

## correctness

PASS

For any generator matrix of the fixed code, every set of k columns is independent, so the check subspace supported on T is the nullspace of the columns in T and has dimension max(|T|−k,0). In particular a (k+1)-set has a one-dimensional check space and every nonzero such check has full support. A cut S with |S|<k would split the rowspace into checks supported on A∪S or B∪S; the sum of their dimensions is less than n−k, whether both, one, or neither contributes a positive dimension. This shows necessity without chordality. A simplicial vertex cannot join different surviving components after fewer than k deletions, because its surviving neighbors form a clique. Repeated deletion therefore gives induced k-connected chordal graphs down to K_{k+1}. At each reverse step a check on the added vertex and k neighbors increases the check rank by one via its nonzero new coordinate; all checks on the smaller graph are exactly checks of the fixed code vanishing off that graph. All edges are covered by (k+1)-cliques inductively, including each edge at the new vertex. The base contributes binom(k+1,2) edges and each step at least k, with equality exactly when all steps have degree k; the resulting k-tree's n−k creation-clique checks are independent by their new coordinates. This includes k=1 and k=n−1. The frozen finite verifier and output were inspected, not executed; its graph loop prefilters on the claimed bound. Independent replay `python3 /workspace/audit_replay.py 2` makes no such prefilter, enumerates graphs and dual vectors for evaluation codes at (n,q)=(4,4),(5,5) for each k, and checks full span and edge agreement on all accepted graphs, with counts (35,7,1) and (541,111,11,1). The proof establishes the all-code and all-field claims.

## originality

PASS

The distinct contribution supported by the comparison is the exact topology classification for every fixed existing linear MDS code over its original field, including the exact characterization of extremal parity-check presentations. The graph-only edge minimum follows from the standard chordal elimination argument, and constructing one systematic split example is not new.

## value

PASS

Feasible graph topology is natural for parity-check representations with sparsity constraints. The result gives both a precise obstruction and a constructive converse without changing the field or the code, and returns all sharp configurations with a minimum-weight basis. This is genuinely structural, even though the graph-only edge bound is standard and is not a decoder-runtime claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
