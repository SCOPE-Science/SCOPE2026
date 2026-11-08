# Independent mathematical audit

## correctness

PASS

For all n>=1 and 2n strictly convex cyclic vertices, an all-positive support can extend to a noncrossing perfect matching iff its chords are disjoint noncrossing and each chord face has an even number of unused vertices. If a selected chord has no unused vertices on either adjacent face, deleting it while fixing all others yields a forced forbidden edge; this proves necessity of face activity. Conversely, choose a full completion M, and for any prescribed positive subset P rotate M one vertex in each P-face with >=4 free vertices; rotation is noncrossing and edge-disjoint from M, while two-free-vertex faces cannot contain a forbidden edge by activity. This realizes all Boolean labelings. The all-positive argument bounds VCdim<=n-1, a boundary-edge construction attains n-1; an online algorithm makes at most n-1 mistakes by identifying n-1 positive edges, proving Ldim=n-1. The face-dual tree and single active face show maximal supports have n-1 adjacent boundary chords and correspond bijectively to n² opposite-parity pairs of free vertices. Independent exhaustive Boolean-projection enumeration confirmed the entire shattered support table for n<=6, including n=6 [1,36,318,860,567,36,0] across 3,876 compatible supports; universal proof is not finite enumeration.

## originality

PASS

Mantas–Savić–Schrezenmaier give single-chord feasible parity and geometric matching optimization, which does not decide all positive/negative patterns of a fixed multi-chord query support. Milich–Mütze–Pergel analyze flips/degree/connectedness and Aichholzer–Asinowski–Miltzow disjoint compatibility of whole matchings, different predicates. Matching-edge incidence concepts are not matroid bases, so matroid VC/Ldim theorems do not imply this classification. Resultary shattering search found no directly comparable record. Old Catalan matching combinatorics remain a priority risk.

## value

PASS

A complete local geometric feasibility theorem for all shattered edge-query supports in a canonical Catalan concept family, plus exact offline and adaptive dimensions and maximum-support multiplicity, is a motivated structural combinatorics and learning-theory classification. It detects obstructions beyond noncrossing and even face parity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
