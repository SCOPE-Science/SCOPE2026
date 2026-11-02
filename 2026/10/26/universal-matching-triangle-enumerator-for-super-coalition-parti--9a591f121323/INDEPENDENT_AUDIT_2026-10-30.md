# Independent mathematical audit

## correctness

PASS

For isolate-free finite simple G with N≥7 and γ_sp(G)≥N-2, every (proper) super-dominating set omits exactly one vertex or a pair constituting an H-edge, since larger omissions are excluded and single omissions have a witness. A coalition between two partition blocks omits ≤2 vertices, so at most four blocks. For two blocks, all nonempty bipartitions unite to V(G), but exactly N+e pairs contain a super-dominating block, and N≥7 ensures at most one such block; hence c2=2^(N-1)-1-N-e. For three blocks, one large block A and two disjoint blocks B,C of sizes ≤2 (A≥N-4≥3). Both B,C must partner A, so they are either (1,1) with a nonedge of H, (1,2) with an H-edge and an outside singleton, or (2,2) with disjoint H-edges; exact counts give c3=C(N,2)-e+(N-2)e+m2=C(N,2)+(N-3)e+m2. For four blocks, the only possible pattern is one large block and three singleton omissions forming an H-triangle, giving c4=t; converses satisfy every block-partner condition. For K_{a_i}, |U|≥3 cannot be witnessable, and an omitted pair is valid iff its members lie in distinct non-singleton parts; this yields H multipartite, e=sum a_i a_j, m2=C(e,2)-sum a_i C(Q-a_i,2), t=sum a_i a_j a_l. N=6 has extra three (2,2,2) patterns and is expressly excluded.

## originality

PASS

Best-of-knowledge original universal partition enumerator for all graphs under high super-domination deficiency. Earlier 2026 originating super-coalition paper defines invariant and provides graph-family bounds in available abstract; its full text could not be inspected (specific priority risk). A published Resultary theorem already determines the entire super-dominating SET cardinality enumerator for complete multipartite graphs, including the exact H-edge criterion; that fact is not claimed as new. Current theorem instead counts unordered super-COALITION PARTITIONS for all qualifying (including nonmultipartite) graphs, with independent matching/triangle dependence; no covering statement found in inspected material.

## value

PASS

The super-coalition partition invariant is naturally defined for arbitrary graphs; under a meaningful high-deficiency condition this result gives the *complete* polynomial at every N≥7, not merely a maximum number. Two disjoint edges and triangles in the admissible deletion graph control distinct coefficients and the exact four-block obstruction, exposing structure invisible to γ_sp. The multipartite case yields explicit universal part-size formulas and a sharp three-nonsingleton-part criterion. The N=7 threshold is mathematically meaningful due to a concrete N=6 counterexample to the stable polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
