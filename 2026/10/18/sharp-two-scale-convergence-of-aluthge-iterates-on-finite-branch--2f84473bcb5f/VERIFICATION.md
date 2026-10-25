---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The operator has one root with d≥2 outgoing infinite rays, positive root weights a_i and constant positive tail weights c_i, and fixed 0<t<1. Distinct input columns have disjoint images, so |S_m| is diagonal and the polar recursion is exactly a_{i,m+1}=a_{i,m}c_i^t R_m^{-t/2}, while all tail weights remain c_i. Normalized squared root weights follow softmax ratios proportional to a_i²(c_i/C)^{2tm}; their log-normalization z_m tends to zero as Q rho^{2m}, with rho=max_{c_i<C}(c_i/C)^t and Q the total leading normalized slow mass. The remaining root-column logarithm satisfies h_{m+1}=(1-t)h_m+z_{m+1}-z_m, whence h_m→0. Since all nonroot columns agree throughout, the squared operator-norm error is exactly C²{[e^{(h_m-z_m)/2}-1]^2+e^{h_m}(1-e^{-z_m})}. Comparing the scalar eta=1-t mode with the slow-ray rho mode yields precisely the four nonzero limits, including the quadrature constant at eta=rho and the cancellation H=0 when eta>rho. The series H converges for eta≥rho because the forcing decays as rho^{2m}; root rescaling changes H by 2log(s) without changing rho,Q. The all-equal-tail boundary reduces to a scalar exponential. An independent 35-iterate four-regime recurrence comparison passed; its finite nature is explicitly distinguished from norm-convergence proof.

## originality

PASS

Trepkowski supplies the one-step tree polar weight update, but not its infinite iteration phase diagram; the same one-branch tree appears in contractivity/hyponormality literature, whose static hypotheses do not imply the exact two-scale asymptotics. A general finite-matrix convergence theorem cannot handle these noncompact ray operators. The historical Rion unilateral-shift paper is a plausible uninspected source, but its abstract addresses strong-limit alternatives for eventually lower-bounded one-ray weights; it does not decisively cover this distinct multi-ray exact-rate classification.

## value

PASS

The exact competition between intrinsic slow-ray contraction rho and Aluthge relaxation eta has an operator-norm resonance not visible from one-step formulas; the tunable root-weight normalization that kills the nominal slower eta mode exposes a substantive boundary phenomenon in noncompact operator iteration. A fully quantified finite-branch family with explicit positive constants is a motivated tractable model rather than renaming a scalar recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
