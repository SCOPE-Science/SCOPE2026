---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The Schur-complement projection determinant is det(A)/Q(u), hence conditional line directions are brightness-weighted by sqrt(Q(u)), not uniform. Homothetic (d-1)-ball volume yields P(L>t)=H^{-1} int sqrt(Q)(1-t^2Q/4)_+^((d-1)/2) d sigma. Local coordinates transverse to the S^(k-1) maximum-axis sphere give exactly a^2Q=1+sum beta_j z_j^2, the change z_j=sqrt(2eps/beta_j)y_j, a dominated beta-ball integral, exponent (2d-k-1)/2 and stated Gamma constant. The sphere case reduces identically to (2eps-eps^2)^((d-1)/2). An independent 3D oblate quadrature for two axis triples gave ratios tending to 1. This numeric test is not the general proof.

## originality

PASS

Best-of-knowledge statement-and-implication comparison after querying Resultary and checking relevant primary literature: the actual full claim, not just title, is not entailed by an inspected stronger theorem. Any acknowledged known special cases are explicitly excluded from novelty. Residual risks are itemized below.

## value

PASS

A geometrically natural, sampling-convention-sensitive endpoint statistic reads off the dimension of the maximum-axis eigenspace and has an explicit shape coefficient, allowing shape-multiplicity inference from rare long chords. The nonuniform coalescing-axis limit and invariant-line rather than center-chord law make this a substantive geometric classification, not a relabeling of a standard one-axis calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
