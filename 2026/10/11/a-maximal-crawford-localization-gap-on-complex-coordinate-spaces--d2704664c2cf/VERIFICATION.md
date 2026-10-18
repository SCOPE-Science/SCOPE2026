---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. For norm-one x in c_0(I;C) and norm-one complex-linear functional f with f(x)=1, equality in the triangle inequality forces nonnegative t_j=f_jx_j summing to one. For diagonal isometry U with phases r ± i sqrt(1-r²) at p,q and 1 elsewhere, every state value is a convex combination whose real part is >=r; x=e_p+e_q, f=(e_p*+e_q*)/2 attains r. Coordinate-state restricted values have modulus exactly 1. Thus c(U)=r, c_beta(U)=||U||=1, saturating the universal norm-one deficit 1-r. Lipschitz estimates on state infima prove perturbative positivity for ||E||<min(r,(1-r)/2). This handles arbitrary index sets, r in (0,1), and complex field. Independently checked 231 exact rational simplex states at r=3/5.

## originality

PASS

PASS best of knowledge. Choi–Lee’s published Question 3.4 asks whether their property-beta norming coordinate family suffices for Crawford infima; the family constructed here gives strict sharp positive-Crawford failure, not implied by their finite-dimensional attainment theorem or density results. Numerical-range convex-hull geometry is classical and used as tool, but its combination with the specified restricted beta-family, all positive r, sharp gap and robust perturbations is not located in the primary paper. Elementary unindexed prior counterexamples remain a risk.

## value

PASS

PASS. A sharp norm-one obstruction at every positive Crawford number resolves the precise question and rules out a tempting coordinate-localization proof of density, while the explicit stability margin gives a nonisolated family of witnesses. It does not overclaim anything about Crawford-attainment density itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
