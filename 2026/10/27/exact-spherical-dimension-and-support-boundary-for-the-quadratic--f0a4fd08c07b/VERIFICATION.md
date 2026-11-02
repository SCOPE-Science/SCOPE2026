---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For c>0, d>=1 and usual geodesic angular distance, positive definite iff d<=3 or c>=pi, with strict PD in the positive cases. C_n^(3/2)=P_(n+1)' and the derivative recurrence reduce the S4 Schoenberg integral to (n+1)(n+2)/(2n+3) times J_n-J_(n+2). Mehler--Dirichlet gives an Abel cosine transform. Its cutoff s^(5/2) term gives n^(-7/2) for each J; adjacent-frequency subtraction gives the claimed n^(-5/2) oscillatory coefficient, while the t^2 log t origin term cancels to n^(-3) after the prefactor. Beta(1/2,3)=16/15 and Gamma(7/2)=15 sqrt(pi)/8 fix the amplitude; geometric Cesaro means of cos and cos^2 force infinitely many negative coefficients. For c>=pi, arcsin(cos(theta)) has positive odd monomial coefficients and Schur positivity of the square gives strictly positive power coefficients; for d<=3 the cited Gneiting theorem gives the low-dimensional claim. A new independent checker verified 36 exact Legendre recurrences and sign changes in three finite cutoff samples. Numeric samples are not the infinite sign proof. Pointwise O_c error not uniform near c=0 or pi.

## originality

PASS

The first part is a genuine low-dimensional sufficiency from Gneiting, not a new theorem; the cutoff negative-side necessity at S4 for every c<pi and its explicit infinitely-oscillating leading coefficient are the assessed addition. Beatson--zu Castell--Xu formulate the general delta>=lambda+1 all-support claim as Conjecture 1.4; with lambda=3/2, delta=2, this does not establish negative coefficients. The 2026 odd-dimensional positive preservation theorem does not imply a sharp negative S4 classification. Fresh Resultary similarity search returned related sphere/Gegenbauer results but no logically dominating same-family theorem. Best-of-knowledge positive with unindexed-priority and Abel symbol regularity risks retained.

## value

PASS

Geodesic truncated-power covariance kernels are standard positive-definiteness design objects. The exact dimension/support phase boundary d=3 versus d=4 for every shorter cap and the all-dimensional support c>=pi regime are useful, structurally motivated kernel facts; the explicit signed high-degree obstruction is not a textbook renaming or finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
