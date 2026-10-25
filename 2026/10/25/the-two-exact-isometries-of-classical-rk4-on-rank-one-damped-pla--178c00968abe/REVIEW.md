# Scientific review

**Correctness (PASS).** The Cayley–Hamilton reduction makes the matrix update a scalar plus scalar times the generator. Its Euclidean Gram matrix has off-diagonal entry \(xyV^2\), which eliminates every nonscalar orthogonal possibility when damping and coupling are positive. The two sign cases are determined by complete real polynomial-root arguments, and derivatives give the frequency-perturbation signs. The accompanying verifier checks algebra and high-precision roots, while the proof covers infinitely many parameter values.

**Originality (PASS, best-knowledge).** Relevant main results and examples in Achleitner–Arnold–Jüngel (arXiv:2308.05689v1), Sun–Wei–Wu (arXiv:2201.06501v1), and Sun–Shu (arXiv:1811.10680v1) were compared by implication. Their general RK strong-stability and energy identities do not state this exact two-point ±identity classification together with the opposite perturbative signatures. Scalar stability-polynomial level curves are a close equivalent viewpoint; a classical table of all left conjugate pairs might already imply the result and remains a substantive literature risk.

**Value (PASS).** The object is the natural rank-one damped harmonic oscillator, and the invariant is full Euclidean energy preservation, not a contrived coordinate check. Completing the classification reveals both falsely frozen and falsely periodic numerical dynamics despite strict exact decay, and the first-order analysis separates robustness regimes.

Limitations: exact arithmetic, fixed step, two dimensions, positive parameters, and full isometry only; no result about all stable steps, arbitrary RK methods, or floating-point behavior. Independent proof/literature audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
