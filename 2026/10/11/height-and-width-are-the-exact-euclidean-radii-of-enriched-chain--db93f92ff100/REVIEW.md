# Same-model review

## Correctness
PASS. The complete signed maximal-chain facet description was reconstructed directly from the literature. For a maximal chain \(C\), the facet normal has norm \(\sqrt{|C|}\). Maximizing the signed support value at an arbitrary center gives \(\sum_{v\in C}|c_v|\), so the radius-\(r\) center condition is exact rather than merely sufficient. A longest chain forces \(r\le1/\sqrt{h(P)}\), and the origin attains this bound. Substitution gives the complete incenter set and proves the longest-chain-cover uniqueness criterion in both directions. The circumradius proof separately uses the signed-antichain generating set, an antipodal maximum-antichain pair, and strict convexity to classify every outer contact point.

## Originality
PASS. The selected middle-period source, Okada--Tsuchiya's *Two Enriched Poset Polytopes*, was inspected through its object definitions, transfer map, vertex/inequality material, and triangulations; it contains no occurrence of “inradius,” “circumradius,” or “radius.” Ohsugi--Tsuchiya's facet theorem and Kohl--Olsen--Sanyal's unconditional-polytope treatment were also inspected because together they are the strongest plausible implication sources. They supply structural ingredients but not the Euclidean radius optimization, full incenter locus, or contact classifications. Direct and equivalent-formulation searches under both “enriched chain polytope” and “unconditional chain polytope” found no covering statement. Residual folklore risk is retained because the final formulas become short once both structural descriptions are combined.

## Value
PASS. The finding gives a direct Euclidean interpretation of poset height and width:
\[
h(P)=r_{\mathrm{in}}^{-2},
\qquad
w(P)=R_{\mathrm{out}}^2.
\]
It also determines all largest-ball centers, exactly when the incenter is unique, every centered inball-contact facet, and every outer-sphere contact point. The result is uniform over all finite posets and distinguishes pure from genuinely nonpure behavior through a geometric uniqueness criterion.

## Closest literature and limitations
The closest exact-object papers emphasize lattice points, transfer maps, triangulations, reflexivity, and facet/vertex descriptions. The present theorem uses those descriptions but adds the canonical Euclidean metric classification. It does not claim affine invariance or a closed formula for the dimension of the incenter set. An equivalent folklore observation under anti-blocking terminology remains a residual literature risk.

Same-model review: passed. Independent audit: not yet performed.
