# Review: Every proper nonface in Kühnel's nine-vertex \(\mathbb{CP}^{2}\) collapses to a tetrahedral sphere

## Correctness
**PASS.** The object is fixed by the published \(H_{54}\)-orbit description and is reconstructed independently by `verify.py`, which checks the group order \(54\), the \(36\) facets, face vector \( (9,36,84,90,36)\), and complementarity. For each of all \(255\) proper nonfaces, the checker replays a certificate of elementary collapses and validates the free codimension-one condition at every deletion before checking that the residue is exactly \(\partial\Delta^3\). The other \(255\) proper vertex sets are verified to be faces and hence induce full simplices. The proof is exhaustive over all \(510\) nonempty proper subsets, not a sample.

Risk: correctness depends on the published identification of the orbit presentation with Kühnel's triangulation and on the finite checker. Both are exposed: the construction is cited, and the checker rebuilds rather than imports the face list.

## Originality
**PASS.** The closest exact-object literature proves complementarity, the face vector, uniqueness, and rich incidence structure. The 2001 paper explicitly observes that the complement of each facet induces a standard four-vertex two-sphere, covering the \(36\) smallest target spheres. Tightness literature controls induced homology maps. None of the inspected sources states or implies, at statement level, that every larger proper nonface-induced subcomplex simplicially collapses to a tetrahedral sphere, nor supplies the complete collapse census. Focused semantic-index and web searches for induced-subcomplex collapsibility, simple-homotopy, and equivalent sphere reductions returned no covering statement.

Risk: Arnoux--Marin's long 1991 crystallographic treatment is highly relevant and its open-access PDF timed out during retrieval; metadata and later citations were inspected, but the full text was not. This leaves a genuine residual risk of an older unindexed equivalent observation.

## Value
**PASS.** Induced subcomplexes are intrinsic to the definition and use of tight triangulations, so classifying their simple-homotopy types is a natural structural question for the canonical minimal triangulation of \(\mathbb{CP}^2\). The result upgrades a homological/complementarity picture to explicit elementary collapses for every proper vertex subset and gives a sharp two-type landscape: simplex versus \(S^2\). This is a complete classification, not an arbitrary parameter slice or a recomputation of a known table.

## Closest literature and limitations
Bagchi--Datta (2001) is the closest statement-level source: complementarity and the induced four-vertex sphere complementary to a facet explain the minimal cases, but not collapse reductions of the larger induced complexes. Bagchi--Datta (1994) gives a detailed exact combinatorial description and face/incidence counts, but no collapse or simple-homotopy theorem was found in the inspected full text. The result remains specific to the nine-vertex model and makes no claim about arbitrary triangulations.

Same-model review: passed. Independent audit: not yet performed.
