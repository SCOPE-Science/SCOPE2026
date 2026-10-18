# Scientific review: mixed-dimensional Euclidean Rips homotopy of type-\(B_n\) roots

## Correctness — PASS

The claim is an integral homotopy classification for every \(n\ge3\) and every Euclidean diameter bound \(0\le r<\sqrt3\), with equality included at \(1\) and \(\sqrt2\). The length convention is essential: short roots have norm \(1\), long roots norm \(\sqrt2\). Pairwise squared distances show that no additional faces enter between the stated critical thresholds. The first graph is exactly the once-subdivided crosspolytope graph, of cycle rank \(2n(n-2)+1\).

At the squared threshold two, maximal cliques fall into exactly four families: short-root crosspolytope faces, signed-coordinate cone faces, exceptional long-root triangles, and uniquely determined mixed bridging triangles. Each signed-coordinate cone collapses to its radial spoke tree relative to pairwise intersections. The exceptional triangles attach the two-cells of the crosspolytope two-skeleton, which is simply connected. The bridges yield a homotopy pushout of two null-homotopic graph maps into simply connected complexes. Its splitting gives \(\left(\bigvee^{8\binom n3}S^2\right)\vee S^{n-1}\). The proof uses actual integral homotopy equivalences; there is no unsupported inference from finite mod-prime Betti numbers to homotopy type.

The included self-contained verifier constructs the roots, checks all maximal cliques against the four families, enumerates all faces, and computes binary simplicial homology for \(n=3,4,5,6\). It was executed successfully with `VERIFY_OK`. Its finite role is made explicit.

## Originality — PASS, with limitations

The closest accessible source claims on Euclidean roots treat the long-root type-\(D_n\) configuration and the type-\(A\) configuration. Neither statement includes the unrescaled short roots of type \(B_n\), nor determines their coning, mixed triangles or the added crosspolytope sphere. Adamaszek–Adams, arXiv:1503.03669, provides exact Rips changes for circles and does not contain this root family. Their hypercube paper, arXiv:2103.01040, uses the Hamming metric on binary strings rather than this unequal-length Euclidean root metric. The published source was compared at the theorem, metric definitions and proof-object level, not merely by title.

Actual searches for type-\(B\) roots, doubled crosspolytope edge sums, root-system clique homotopy, and Rips sphere wedges retrieved related but non-covering claims. A failed search does not prove global uniqueness. Residual risk: an equivalent calculation under Coxeter-complex, graph-flag or signed-incidence terminology may be unindexed. The mathematical statement is nevertheless distinct from the strongest accessible implications.

## Value — PASS

Type-\(B_n\) roots form a canonical infinite family, and their two natural root lengths generate a genuinely nontrivial first Rips transition. The result shows a uniform mixed-dimensional wedge with a cubic number of two-spheres and one high-dimensional crosspolytope sphere. The specific top homology class is explained by the short-root sphere and bridging attachments, not an arbitrary selection of a small parameter. It provides an exact structural benchmark for the persistent topology of an unequal-radius Coxeter point configuration, and it distinguishes the complete root set from the long-root-only subconfiguration. No full-filtration, integrality of a group representation, or downstream theorem is claimed.

## Closest literature, boundary and remaining risks

Adamaszek–Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (original 2015-03-12); Adamaszek–Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (original 2021-03-01); accessible earlier claim on the Euclidean type-\(D_n\) long-root subconfiguration, identifier `7b5415da-1fee-4381-b7e4-7fff0fb9929d`. The latter is a different point cloud and is not being recertified here. Only \(0\le r<\sqrt3\) is established; the verifier is finite, and no independent external audit was carried out. Bibliographic incompleteness remains possible.

Self-review: passed. Independent audit: not yet performed.
