---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For symmetric stochastic Φ, ||Φ||₂≤1 and I-rΦ² is positive definite. K=rΦ²+r(ζ-1)vvᵀ with v=Φe is positive semidefinite. Rank-one congruence makes ρ(K)<1 equivalent to r(ζ-1)vᵀ(I-rΦ²)^(-1)v<1; the trivial eigenmode contributes precisely 1/[M(1-r)], yielding the stated H_r threshold and equality/strict-reversal cases. Rayleigh on the all-ones vector gives ρ(K)≥r(M-1+ζ)/M; equality forces Φe uniform and that condition is sufficient by constant K-row sums. Exact reconstruction of five-by-five rational examples yields H=529543/11008272>1/24 versus 245/5956<1/24, with identical fifth columns and opposite determinant signs. Numerical checks of 120 further symmetric stochastic matrices corroborate only finite instances. The all-size conclusions rest on the rank-one and Rayleigh proof.

## originality

PASS

Best-of-knowledge PASS for the arbitrary nonuniform-hotspot spectral budget and rigorously equal-hub-column/opposite-invasion pair. Classical rank-one secular tests, equitable quotient theory, and all uniform-hotspot special cases are prior mathematics. A new quantitative application is a substantive motivated finding, though broader epidemic literature could encode the test under a different notation.

## value

PASS

The observable full hotspot column and its variance are shown insufficient for invasion: two exact five-neighborhood networks with identical hotspot mobility have opposite threshold outcomes as background travel changes. The all-size spectral budget supplies a precise invasion test, sharp uniform-column optimum and variance bounds. This directly advances motivated SIR mobility modelling beyond the special uniform-hub cases without claiming a new matrix theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
