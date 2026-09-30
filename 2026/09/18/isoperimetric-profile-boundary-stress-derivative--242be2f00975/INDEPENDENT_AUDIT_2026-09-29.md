# Independent audit — Boundary-stress directional derivatives and a metric kink criterion for isoperimetric uniqueness

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/isoperimetric-profile-boundary-stress-derivative--242be2f00975`
**Audited tree:** `f68f748b274042e032475fb2edd245ba720371b1`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The envelope argument is correct. Freezing a base minimizer gives the upper one-sided bound, while minimizers for the perturbed metrics, the quoted uniform quadratic fixed-set perimeter remainder, strict-BV compactness, and weak-* stress convergence give the matching lower bound. Applying the right-derivative formula to -A gives the left derivative with the stated max/min signs. Equality of all directional one-sided derivatives forces all minimizing stress measures to agree; Niu's stress-rigidity input then gives uniqueness up to complement. The global exponential estimate follows directly from the exact hypersurface-Jacobian factor for the trace-free Ebin slice.

### Independent checks

- Reconstructed the right derivative by the two-sided envelope squeeze: a maximizing base minimizer gives limsup <= -max<T,A>, and perturbed minimizers give liminf >= -max<T,A> after strict-BV/stress convergence and the O(t^2) remainder.
- Checked the left derivative by substituting -A and reversing t, yielding -min<T,A>.
- Checked that equality of the max and min pairing for every smooth trace-free A forces equality of the trace-free tensor-valued Radon measures, after which the cited stress-rigidity proposition gives equality up to complement.
- Checked the half-volume boundary case: a complement has the same prescribed volume only at m=Vol(M)/2, so the uniqueness statement is consistent.
- Checked the exact global bound from |e^{-A/2} nu| between exp(-||A||/2) and exp(||A||/2), using the unchanged volume form.

## Originality

PASS to the best of current searchable knowledge. The full 16-page v1 of Niu's September 17, 2026 preprint was independently retrieved and inspected in this audit. It develops the same trace-free Ebin deformation, the fixed-set perimeter expansion, boundary stress, stress rigidity, and the support function Phi used to select minimizers, but it does not state the submitted right/left directional derivatives of the optimized isoperimetric profile, the iff differentiability/uniqueness criterion, or the global two-sided profile bound. General envelope theorems and differentiation of isoperimetric profiles in the volume variable are prior art and are excluded from the novelty claim.

### Literature checked

- https://arxiv.org/abs/2609.20790 — Gongping Niu, Generic Uniqueness of Isoperimetric Regions in Arbitrary Dimension, arXiv:2609.20790v1. Full 16-page preprint independently inspected through authorized retrieval; it contains the Ebin deformation, stress tensor, rigidity, strict-BV continuity, and generic support-function selection, but not the audited optimized-value derivative theorem.
- https://doi.org/10.1111/1468-0262.00296 — Milgrom--Segal, Envelope Theorems for Arbitrary Choice Sets; general value-function envelope principles are prior art and are not claimed as new.

## Scientific value

The record promotes the boundary-stress device from a minimizer-selection mechanism to a complete first-order sensitivity law for the optimized isoperimetric value and turns noncomplementary multiplicity into an exact directional-kink diagnostic. The support-function formulation and global metric stability bound are useful geometric consequences, and the result remains meaningful in dimensions with singular isoperimetric boundaries.

## Limitations

- The result is restricted to trace-free, volume-form-preserving ambient metric directions and gives only first-order sensitivity.
- The derivative theorem is a new synthesis of ingredients that already appear explicitly in Niu's very recent v1, so the originality claim is narrower than the mathematical statement itself.
- Very recent or unindexed parallel work could still affect priority; the originality verdict is not a guarantee of first discovery.

## Publication guard

The current source tree on `main` matched the assignment tree exactly during this audit. This guarded change-set adds only the independent-audit evidence pair and updates the independent-audit channel in `VERIFICATION.md`; the Lean and expert-attestation channels are preserved unchanged.
