# Scientific review: Sharp normal-to-tangent leakage for two-sided sketched low-rank projections

## Correctness — PASS
The source projector formula was reconstructed from its two one-sided, basis-invariant oblique projectors. The decomposition into tangent and normal blocks shows that the two tangent projectors agree on the entire tangent space. Their difference on the normal space has exactly three mutually Frobenius-orthogonal terms; the same rank-one normal matrix saturates all three operator-norm bounds. The one-sided norm-distortion lemma follows from compressing the embedding error to a trial/normal orthonormal pair and maximizing an elementary rational function at the interior point \(a=1-\varepsilon^2\). The explicit \(2\times2\) Gram witnesses attain both bounds for every distortion pair and extend to dimension-reducing sketches. A packaged standard-library checker verifies exact rational cases and a finite grid; the general assertion relies on the complete proof, not on tests.

## Originality — PASS, subject to identified literature risk
Carrel–Grigori (arXiv:2607.03402v1, §§4.1–4.2) is explicitly credited with the two-sided oblique tangent projector, a qualitative equivalence condition and its related residual perturbations. Inspection of its full accessible mathematical sections shows that the exact operator norm, sharp paired distortion coefficient and universal equality construction are not stated there. Published-literature comparisons checked the operator, residual, aliases and parameter form, finding no established dominating statement. The 2020 Brust–Marcia–Petra oblique-projector SVD paper was accessible only through its abstract; an earlier equivalent formula is a genuine residual risk, not ruled out. The result has not received independent originality validation.

## Value — PASS
The motivating numerical method can deviate from ordinary dynamical low-rank approximation when its normal residual is large. This result provides an exact normal-to-tangent amplification measure and a sharp deterministic embedding-accuracy budget for that naturally occurring mechanism. It identifies how left and right sketch errors interact multiplicatively, rather than reporting an arbitrary small case or merely restating projector algebra. No whole-trajectory, finite-precision or random-failure guarantee is asserted.

## Sources and limitations
The primary source is Carrel and Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections*, arXiv:2607.03402v1 (first public date 2026-07-03), especially Lemma 4.2, Proposition 4.4 and §4.2. Related context: Balabanov–Grigori, *Randomized Gram–Schmidt Process with Application to GMRES* (2022). Relevant inaccessible full-text comparison: Brust–Marcia–Petra, *Computationally Efficient Decompositions of Oblique Projection Matrices* (2020), DOI:10.1137/19M1288115.

The exact sharp bound assumes separate squared-norm embeddings of both full *combined* trial-and-realized-normal spaces, with distortions less than one. It does not follow if only the trial bases are embedded. The interpretation concerns exact instantaneous tangent-projector discrepancies, not accumulated numerical integrator error. One older original SVD source remains a literature comparison risk.

Self-review: passed. Independent audit: not yet performed.
