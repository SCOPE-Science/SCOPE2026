---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Reconstructed q-overlap normalization, phase/unitary symmetry, and the rank-(n-1) isometric initial space of J_n. Equality in norm forces first coordinate zero, reducing the plateau exactly to the circular numerical range W(J_{n-1}) of radius cos(pi/n). For t>0, the top eigenvector of the irreducible positive-offdiagonal tridiagonal (J+tI)^*(J+tI) is simple and positive; paired left singular vector has real overlap s_n'(t), attaining the dual norm bound at the matching q. A common norming pair at two distinct t would force nilpotent J to have eigenvalue s(t)-t>0, so s strictly convex. Schur complement on e1 versus e2..en, followed by simple eigenvalue perturbation of J_{n-1}+J_{n-1}*, gives s(t)=1+q_n t+[(n+2)/(2n)]sin^2(pi/n)t^2+O(t^3); Legendre minimization gives the claimed coefficient. Checked q=1 separately and numerical SVD/minimizations n=4..8 for small delta, observed ratios tending to exact coefficients. Tests do not prove arbitrary n.

## originality

PASS

Bounded novelty of the explicit all-size plateau edge and its exact second-order coefficient; the general Davis–Wielandt shell machinery is not claimed as original. Li–Nakazato (1998) is plausibly overlapping at the level of general q-numerical functions; its full text was unavailable and leaves a material publication risk, but the abstract gives no all-n Jordan transition or coefficient and no decisive equivalence has been established.

## value

PASS

The nilpotent Jordan shift is the canonical matrix numerical-range model. A sharp dimension-dependent first loss beyond a nontrivial norm plateau and a variational profile for all dimensions are motivated spectral-geometric data, not a renaming of the ordinary w(J_n) endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
