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

PASS. With B=beta uu*, define a=beta^(1-t) A^t u and b=beta^t A^(1-t)u. Then C=a u*+u b* has at most two singular values and H=(a+b)u* has rank one. Hilbert–Schmidt expansion yields 2 beta K for ||H||_2^2-||C||_2^2; exterior-square Gram determinants give s1*s2=beta sqrt(V_F V_G), hence trace defect 2 beta(sqrt(V_F V_G)-K). Increasing power functions yield K>0 exactly for nonsingleton spectral support. Cauchy–Schwarz equality means two powers are affinely related on spectral support, and strict convexity/concavity forces at most two support points unless t=1/2. With strictly positive second singular value, Schatten-p norm of C is strictly decreasing whereas H norm is constant, yielding one crossover in (1,2) for >=3 supports and t≠1/2. Independent 3x3 matrix SVD agrees with 1004/3, 952/3 and exact trace defect. Boundary t=1/2 and 1/2-point supports checked analytically. Finite SVD only corroborates the universal proof.

## originality

PASS

PASS best of knowledge. Sababheh–Bourin provide two-dimensional crossed-Heinz results and distinct comparison with A+B, not the rank-one versus ordinary-Heinz trace reversal and complete spectral-support Schatten transition. Related central-interval Frobenius results cannot imply the trace deficit or unique threshold. Resultary published common-two-point-spectra theorem compares a different quantity and does not cover the arbitrary spectral measure supporting the rank-one input.

## value

PASS

PASS. The direction of Schatten inequality changes exactly once with p, controlled by spectral support and two covariance invariants; a sharp three-dimensional example demonstrates a genuine failure of a natural majorization ordering, not merely restatement of a standard Heinz mean inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
