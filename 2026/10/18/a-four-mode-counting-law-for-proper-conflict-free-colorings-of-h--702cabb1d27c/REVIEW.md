# Scientific review: hairy-cycle PCF counting law

## Correctness — PASS
The precise object is the uniformly leaf-decorated simple cycle with integers \(n\ge3\), \(a\ge1\) and a labeled palette of \(q\ge3\) colors. The proof first counts local pendant extensions according to whether the two core-neighbor colors agree, including all singleton and no-singleton cases. The resulting pair-color transfer has an exact four-family invariant splitting whose dimensions sum to its full dimension; this proves the trace formula for arbitrary length. The special three-color weights follow from direct binary choices. The complete attached verifier reproduces local weights and counts by structurally different exact procedures, including full coloring enumeration; those tests do not replace the proof.

## Originality — PASS, qualified
Caro–Petruševski–Škrekovski (arXiv:2203.01088, Observation 3) already study ordinary coronas and cover the chromatic-number statement in the one-leaf specialization. This is explicitly not asserted to be novel. Qi–Song–Cao (arXiv:2609.11249) establish large-girth list-colorability, not counting. Related crown-graph counting formulas and complete-multipartite results concern different graph families. No covering all-palette formula or core-independent two-pendant extension identity was found in the inspected full primary texts, published research search or published related claims. Unindexed equivalent work and unpublished overlap remain possible; there is no claim of certified uniqueness.

## Value — PASS
The result gives the full \(q\)-color enumerator for a two-parameter natural outerplanar family, reducing an exponentially large coloring count to two explicit local weights and a four-mode spectral formula. The striking identity for two leaves and three colors identifies an exactly uniform extension multiplicity across all properly colored cycle cores, rather than merely identifying the least number of colors. A generic fixed-graph transfer construction would not itself provide this closed all-parameter splitting or explain the cancellation. It does not solve arbitrary unicyclic/list-coloring enumeration.

## Limits
The result counts labeled palette assignments for uniform pendant counts only. The algebraic proof, not computational extrapolation, supports the infinite scope. Historical sources are used for overlap, without a claim of independent examination of other results. Scientific residual risk is recorded in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
