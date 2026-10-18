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

The exact finite-d formula is reconstructed from the standard simplex: sign-orthant decomposition yields vol(K_t)=Σ binom(d,k)^2 t^k/d!. The symmetry-fixed Santaló point is the centered origin. Sorting the d+1 simplex vertex-support values into gaps gives the polar chamber simplex with volume n^n/P_d(t), P_d=∏[j+(n-j)t], n=d+1. Both factors have degree-d palindromic coefficients. Legendre-polynomial zeros, by the classical strict Stieltjes comparison against roots of U_d and cos(jπ/(d+1))>=(d+1-2j)/(d+1), dominate corresponding roots of P_d, including the odd-d common factor (t+1). For positive t the difference of logarithmic derivatives of each paired reciprocal quadratic has the sign of (1-t²), proving strict increasing for 0<t<1 and decreasing t>1; d>=2 ensures at least one pair. At t=1 the product is (d+1)binom(2d,d)/d!, and the quadratic coefficient in log M_d(e^u)/M_d(1) is -d(d-1)(d+4)/[24(2d-1)(d+1)], with evenness giving O_d(u^4). I independently reconstructed the numerator derivative and exact curvature symbolically for d=2..7; those finite tests do not replace the cited all-degree strict zero comparison and analytic proof.

## originality

PASS

Best-of-knowledge original: the parameterized exact Santaló volume-product formula, strictly unimodal all-d profile, and sharp curvature are not statements of the examined simplex local-minimum, symmetric-body lower-bound, or primal-volume unbalanced-difference literature. General lower bounds or convexity do not imply the new strict finite-t maximum; uninspected Barthe–Fradelizi full text is a residual risk, not a premise for asserting global priority.

## value

PASS

A natural one-parameter family interpolates between the simplex and its reflected difference body, connecting central topics in the Santaló/Mahler problem. The exact all-dimensional product and global unique-maximizer profile with curvature quantify a mathematically motivated deformation; these do not follow routinely from known simplex local minimality or volume-only formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
