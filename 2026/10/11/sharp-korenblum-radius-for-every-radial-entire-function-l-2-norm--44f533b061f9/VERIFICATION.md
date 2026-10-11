---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification and reproducibility

The proof is deductive. It uses the coefficient representation \(\|f\|_W^2=\sum m_j|a_j|^2\), positivity of all moments, their Cauchy–Schwarz log-convexity, the rational-quotient lemma, the reverse-polynomial identity, and von Neumann's rational functional-calculus inequality for a Hilbert-space contraction.

`CHECK.py` is an optional, independently executable standard-library exact-fraction illustration. Executed with `python3 CHECK.py`; observed `EXACT_CHECK_OK`, `R_squared= 9/16`, positive strict norm gaps for three rational finite test pairs, and sharpness norm gap `39/80`. The test weight was \(W(t)=e^{-t}+(28/5)e^{-4t}\) with \(m_1/m_0=9/16\). A uniform narrow-ring weight was separately checked by rational moments. The checker does not perform exhaustive infinite verification and does not validate originality.

Critical nonstandard steps are reconstructed in `RESULT.md`: the quotient has no poles on the comparison circle because it is bounded from the exterior; consequently its inverted rational denominator has no zeros on the closed unit disk. Formal backward shifting of the polynomial identity is justified coefficientwise, independently of whether multiplying the functions by polynomials preserves membership in the weighted space. Completion of polynomials supplies a legitimate Hilbert-space operator even for compactly supported weights.

Limits: the result does not address the disk-annular Korenblum problem, nonradial measures, or exponents different from two. Exact sharpness uses the entire test pair of a constant and the identity function, not finite numerics. The same-model mathematical review passed; independent audit has not been performed.
