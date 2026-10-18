# Independent mathematical audit

## correctness

PASS

For Cr_n=K_{n,n} minus a perfect matching, n>=3, compute d(a_i,a_j)=2 for i!=j, d(a_i,b_j)=1 for i!=j and d(a_i,b_i)=3. Every same-side pair i,j is distinguished exactly by P_i union P_j, every opposite-side pair by all 2n vertices. A set S is k-metric exactly when all c_i+c_j>=k with c_i=|S intersect P_i| in {0,1,2}; these constraints imply |S|>=k for the other pair type. Optimizing the smallest two c_i proves minimum sizes (n-1,n,2n-1,2n) and, crucially, ALL minimum occupancy profiles and exact counts (n*2^(n-1), 2^n,2n,1) for k=1..4; k>4 impossible. Independent fresh BFS and subset enumeration at n=3..6 reproduced distances, minimal sizes, profile types and counts. It is corroboration; the proof is the all-n integer-inequality reduction.

## originality

PASS

Vertex-pair k-metric dimension on matching-deleted bicliques is not the edge metric dimension or ordinary complete-bipartite dimension. The primary k-metric framework already proves a general bound on maximal k and treats complete bipartite graphs. Its stated theorems do not specialize directly to this deleted-matching profile/ALL bases. The nearest semantic corpus crown record is specifically EDGE metric bases; apparent coincidence of n-1 and n2^(n-1) at k=1 does not entail the full vertex k-hierarchy. Search and full-text inspection found no theorem directly implying all four dimensions and optimizer counts; best-of-knowledge only.

## value

PASS

A complete k-metric hierarchy for a canonical sparse perturbation of K_{n,n}, including ALL metric bases and the fault-tolerant k=2 row, is a natural exact graph invariant. The same-side pair distinction and occupancy inequalities also give a reusable characterization rather than an isolated small-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
