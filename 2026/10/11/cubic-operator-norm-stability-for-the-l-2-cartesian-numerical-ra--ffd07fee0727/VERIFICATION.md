---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Independently reconstructed the entire dimension-free argument from RESULT.md. For nonzero T, R=w(T)>0; the compact centrally symmetric closure C=conv(overline{W(T)} union -overline{W(T)}) has support h(theta)=||Re(e^{-i theta}T)|| and maximum radius R. Phase rotation puts the maximizing ±R points on the real axis, forcing h(theta)≥R|cos theta| and Delta=(1/pi)integral_0^pi[h²−R²cos²]≥0. Choose a top support point a+ib with b=h(pi/2)≥0 and b≤R. On a one-sided arc of length alpha=atan(b/R)≤pi/4 the support dominates b cos t≥R sin t. Exact integration gives Delta≥R²/(2pi)[s+(s²−1)atan(s)]≥R²s³/(2pi)=b³/(2pi R)≥d(T)³/(2pi R), since s−atan(s)≥0. For each phase the closest self-adjoint operator is its real part, yielding d=min_phi||Im(e^{-i phi}T)|| with attained minimum. Delta=0 iff a phase makes T self-adjoint; converse follows from a segment support. For T_eps=diag(1,-1,i eps,-i eps), 0<eps≤1, h=max(|cos|,eps|sin|), Delta=[eps+(eps²−1)atan eps]/pi=4eps³/(3pi)+O(eps⁵), and d=eps/sqrt(1+eps²)~eps. Therefore no deficit exponent q<3 (no inverse distance exponent >1/3) is universal. Source tree verified by reconstructing seven-entry Git tree. The proof does not depend on quadrature.

## originality

PASS

Best-of-knowledge PASS for the new quantitative all-bounded-operator inverse stability and optimal cubic exponent, not for the earlier sharp inequality Q²≥R²/2 or angular supremum representation. The main arXiv:2610.04844v1 text was materially inspected through its lower-comparison proof, later Cartesian bounds and associated conclusions; arXiv:1511.02094v1 full HTML and the nearby arXiv:2610.15242v1 were checked. An exact published SCOPE rank-one L²-Cartesian formula was read in full; its limited domain does not imply the general theorem. Resultary self-match was excluded from priority evidence. A covering theorem in older quantitative convex-support theory remains an explicit residual risk, not a reason for automatic failure without contrary evidence.

## value

PASS

The 2026 L²-Cartesian numerical radius has a sharp lower bound but previously only exhibited equality examples. This finding supplies an explicit homogeneous, dimension-free inverse near-equality modulus in operator norm for the natural phase-self-adjoint equality class, together with a normal four-dimensional degeneration proving the exact 1/3 Hölder stability exponent is optimal. The requirement that near-minimizers be close in a strong operator norm is a motivated structural stability question, not a routine scalar recomputation. No claim is made that the coefficient 1/(2pi) is numerically optimal or that the theorem concerns Schatten/unbounded operators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
