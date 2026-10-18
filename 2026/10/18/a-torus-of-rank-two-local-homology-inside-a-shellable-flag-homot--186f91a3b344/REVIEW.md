# Self-review

## Correctness — PASS

The precise domain is the independence complex on residues modulo sixteen with forbidden cyclic gaps \(1\), \(4\) and \(8\). Exhaustive enumeration gives 80 four-vertex facets and 321 faces including the empty face; a new explicit 80-facet shelling order passes every required earlier-facet comparison in `verify_shelling.py`. The standard shelling theorem therefore proves all links have torsion-free, top-degree-only reduced integral homology. `verify_singular_torus.py` independently enumerates every dihedral face orbit, checks top link Betti numbers over two primes and verifies a coherent integer fundamental cycle on the rank-two triangle locus. The local-homology/link shift, surface incidence and Euler characteristic give the exact pointwise theorem and the torus identification. The proof is finite but **exhaustive** on its explicitly fixed graph; modular boundary ranks alone are not misrepresented as an integral proof.

## Originality — PASS

The 2015 Earl–Vander Meulen–Van Tuyl preprint, arXiv:1505.02837v1, Theorem 6.1(iii), already establishes shellability, 80 facets and failure of vertex decomposability; all are treated here as previously known. Its complete relevant theorem, shelling proof, discussion and Table 1 were inspected. The companion expansion paper arXiv:1505.02838v1, especially Theorems 1.1 and 4.4, extends the original combinatorial phenomenon but does not identify pointwise local homology. A local homology profile is not logically implied by the global shellability assertion or a sphere-wedge homotopy type. Direct searches for this circulant and for alternate singular-link, cyclic-torus and homology-manifold formulations, together with comparison to relevant indexed research, identified no covering result. Priority in unindexed literature is a residual risk, not a proved negative.

## Value — PASS

The graph is the established minimal circulant example separating shellability from vertex decomposability. Its global topology is as simple as a sphere, yet a full two-dimensional **torus** rather than isolated points supports doubled top local homology. The theorem completely locates the intrinsic homological nonmanifold set and determines its topology. This is a motivated structural refinement of a canonical example, not merely a new facet count or a computational substitute for known shellability.

## Limits

No ambient PL-local-link classification, ambient homeomorphism to a sphere, integral torsion for unrelated graph families, or priority against inaccessible unindexed sources is asserted. Two finite checker programs and explicit combinatorial proof data accompany the finding.

Self-review: passed. Independent audit: not yet performed.
