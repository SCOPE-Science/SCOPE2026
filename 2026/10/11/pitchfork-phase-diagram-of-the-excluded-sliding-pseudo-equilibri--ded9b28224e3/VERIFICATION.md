---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For kappa<=0 the strict cone forces ds/dt<0. For kappa>0 d=0 produces the sole central point; d!=0 requires s=(1+H)/(2mu), and substitution gives d²/s²=(kappa-kappa_c)/(kappa+4mu), yielding exactly two additional strict-cone zeros iff kappa>kappa_c. Central Jacobian eigenvalues kappa/2 and (1+H)(kappa-kappa_c)/(2(1-H)); off-axis determinant is negative. Formal expansion at threshold independently gives center manifold u=(4mu/((1-H)(1+H))) d²+O(d⁴), and cubic reduced coefficient -16mu³/((1-H)(1+H)²), nonzero opposite sign to unfolding. Thus an exact supercritical pitchfork on the center direction; the transverse direction is unstable.

## originality

PASS

The motivating Filippov paper proves no interior sliding zeros precisely for nonpositive kappa and exhibits the central obstruction for positive kappa. It does not establish the two additional off-axis saddle branches, threshold kappa_c or pitchfork cubic normal form; the source-specific structural classification survives.

## value

PASS

The bifurcation threshold completes the previously excluded physically natural positive-kappa sector of the exact model and distinguishes one central saddle from three equilibria with different stability. The exact center-manifold normal form captures the symmetry-breaking mechanism and is an independently useful local structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
