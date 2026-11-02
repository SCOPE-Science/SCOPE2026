# Independent mathematical audit

## correctness

PASS

In a complete multipartite graph, deg(v)=N-part_size(v). A defender in another part has sufficient degree exactly if its part is no larger. This yields gamma_st=1 when a singleton exists, =2 when the smallest part m>=2 has multiplicity>=2, and =m when it is unique. Deleting all k singleton parts is uniquely minimal if k>0. Without singletons, single deletions change gamma except at repeated m=3; then deleting two vertices from the same size-three part is necessary and sufficient, yielding 3a minimum pairs. Other eligible singleton deletions are classified by m,a and part sizes m+1. Direct brute force recomputed degrees and all minimizers for 86 part profiles with 3–9 vertices, including K_2,2,2 (6 singletons) and K_3,3,3 (9 pairs). The proof, not the finite tests, covers all sizes.

## originality

PASS

The January 2026 primary paper studies the SAME stability parameter on balanced multipartite graphs but asserts an incompatible p+1 result for K_{p,p,p}. Already K_{2,2,2} has gamma_st=2 and, after deleting one vertex, gamma_st=1, disproving that assertion under the stated definition. The new theorem proves an exact arbitrary-part classification and every minimizing labeled deletion set; the older general 2022 vertex-deletion bounds cannot imply this. One foundational 2023 article remains incompletely accessible.

## value

PASS

Complete structural determination of a natural critical vertex-deletion invariant, including a unique exception at repeated minimum-part size three, corrects a prominent contrary assertion and identifies every minimal deletion witness across unbalanced families. The exception and all-set classification have mathematical content beyond an isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
