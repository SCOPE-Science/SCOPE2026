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

# Verification

The analytic verification consists of four independent logical stages: (i) the finite-field Gauss/Salié transform with an internal Fourier-in-the-discriminant proof; (ii) the exact smooth-lift character average at imprimitive frequencies; (iii) stationary-fibre orthogonality and Hensel lifting of the two primitive stationary points; and (iv) complete quadratic-value counting in three variables.

The local checker `certificate.py` independently enumerates every shell point and accumulates integral coefficients of \(\zeta_{p^2}\). It compares the predicted and observed multiplier coefficient vectors modulo the exact cyclotomic polynomial \(\Phi_{p^2}\), without floating-point thresholds. The whole frequency spaces were checked for a residue and a nonresidue unit level at each of \(p=3\) and \(p=5\), confirming ranks \(345,177,7585,5065\). At \(p=7\), two deterministic samples of 371 frequencies each were checked. The cases beyond those finite moduli follow from the proof, not from computation.

The precise Fourier convention is unnormalized and positive-sign, and the operator is additive convolution on \(R^3\). The level must be a unit and \(p\) odd. Independent audit has not been performed.
