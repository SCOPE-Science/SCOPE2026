# Independent mathematical audit

## correctness

PASS

PASS. For an injective ordered tuple, meet closure has n+k points with 0<=k<=n-1. Marking tuple entries black and additional meet points white gives exactly a rooted Greg tree: every white generated point is a meet of black descendants in at least two child cones, and conversely every white Greg vertex is generated as a meet of black descendants from distinct children. In the generic graph/meet-tree Fraisse age, an arbitrary simple graph relation may be placed on the same n+k-element meet-tree carrier. A tuple-preserving isomorphism fixes every black generator and hence every meet term, so there is no further automorphism quotient: each closure shape contributes exactly 2^{binom(n+k,2)} orbits. The species root decomposition gives G=x exp(G)+u(exp(G)-1-G). The k=n-1 term gives the lower exponential scale and the labeled-tree bound gives the stated O(n log n) upper correction, so log2(a_n)/n^2 -> 2. The bundled exact recurrence/species agreement is a finite arithmetic check, not the proof.

## originality

PASS

PASS with an explicit access residual. The Rado meet-tree paper defines the structure as the Fraisse limit of finite graphs that are also meet-trees and is about automorphism-group simplicity; its accessible primary abstract does not state a tuple-orbit enumeration. OEIS A048160 exactly covers the refined Greg-tree counts g_{n,k}, including the same white-vertex condition and recurrence, so that enumeration is prior art. The submitted contribution is the implication-level bridge that each meet-closure shape carries every graph decoration and that tuple labels freeze all meet terms, yielding the factor 2^{binom(n+k,2)} and the weighted profile. Exact-value web searches and a Resultary orbit-profile query found no prior weighted sequence/profile. The complete same-paper text could not be reliably retrieved after lawful public-access attempts; that access gap is retained as a residual risk rather than treated as evidence of novelty.

## value

PASS

PASS. The oligomorphic profile of a named homogeneous expansion is a natural invariant, and the theorem gives an exact all-n formula plus a sharp quadratic logarithmic growth constant. It cleanly separates known Greg-tree combinatorics from the new graph-decoration step. This is a structurally motivated classification, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
