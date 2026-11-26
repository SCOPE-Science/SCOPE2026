---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For half-angle α=γ/2 and nonzero mean direction m, write the two unit Bloch vectors as cos(α)m ± sin(α)e, with e perpendicular to m (arbitrary there if γ=0). The mean has length cos(α). For a unit transverse n, factorization gives zero cross covariance and variance [1−sin²(α)(e·n)²]/2. Its global minimum is cos²(α)/2, attained at n=e; at γ=0 all transverse axes tie. Both normalizations give the stated values, and taking γ→π gives an infimum but not a value at the undefined endpoint. The review's explicit product uses opposite transverse components ±√3/2 and common longitudinal component 1/2; the dot product is −1/2 and the variance minimum is 1/8. This exact witness is in the 2011 review, not the qualitative product paragraph of the 2003 preprint; correct the attribution when citing the example. The analytic minimization, not the recorded numerical output, supports the result.

## originality

PASS

The qualitative counterexample and a particular point were known. The supported distinct contribution is the complete relative-angle profile under the original collective definitions, including the optimal variance and vanishing infimum of ξ₁ with ξ₂ exactly one. This also resolves the apparent over-unity claim for nonsymmetric products in the pure two-qubit discussion of the motivating source.

## value

PASS

A known false-positive example becomes a complete diagnostic boundary: every misaligned nonantipodal pure product is classified, and one can make the apparent Kitagawa–Ueda squeezing arbitrarily strong without genuine entanglement or Wineland squeezing. The exact normalization and endpoint matter to interpreting the witness, and the full classification also resolves a conflicting qualitative statement in the motivating discussion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
