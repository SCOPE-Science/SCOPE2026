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

# Verification record

The mathematical proof uses positivity of the metric-tree consistent mass, positive definiteness of \(H=M+tK\), exact branch elimination, and a distance-two sign witness. The crucial branch inequality \(g^{-1}\geq h/3+t/h\) follows from the variational Schur complement applied to the principal submatrix for the detached component: all its other edge contributions are positive semidefinite. This also proves strict positivity of diagonal and neighbor entries at every positive step.

Run `python3 verify.py` with Python 3.9 or later. It constructs **57 distinct trees on 3–8 vertices**, at seven rational step choices per tree, and **12 additional two-vertex edge/step combinations**, for 411 exact rational matrix checks. It verifies \((M+tK)P=M\), row sums, diagonal signs, strict neighbor signs, negative two-hop witnesses below threshold, and nonnegative matrices at and above threshold. All checked identities use `fractions.Fraction`; no numerical tolerances or floating-point inference are used.

Result: `PASS: 57 distinct trees (3-8 vertices), 411 exact rational step/matrix checks; two-vertex exception included.`

The sample does not exhaust arbitrary trees, edge lengths, or real steps, and so does not substitute for the universal proof. Independent validation has not been performed.
