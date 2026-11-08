---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Inspected pinned RESULT.md, verify.py and full tree. Q_{ij}=(-1)^(i-j) C(2alpha,alpha+i-j). Conjugating D by checkerboard diagonals yields positive binomial convolution E, product of alpha nonnegative bidiagonal rectangular maps; Cauchy-Binet makes B=E^T E totally nonnegative. Direct complementary (d-1)-minor of B has an explicit positive Cauchy-Binet summand, so the inverse cofactor checkerboard signs cancel and K_{ij}>0 for all i,j. For d=1 scalar case separate. Polynomial Landau vector v_j=C(j+alpha-1,alpha)C(d+alpha-j,alpha), with alpha boundary zeros at both ends, satisfies Qv=C(2alpha,alpha)1 by 2alpha-th difference; Vandermonde sum yields original sharp constant C^2. Riesz-energy projection to span(Ks) gives exact shape decomposition and G(s)=sum K_jk|s_j-s_k|^2. All phases equal iff G=0 for d>1, and Q-projection zero fixes scalar multiple v, including zero coordinates. Independent 28 exact rational Q inverses for alpha<=4,d<=7 confirmed strict entries, Qv and phase kernel formula. Entire universal proof rests on complementary minors/polynomial identities not finite testing.

## originality

PASS

Best-of-knowledge PASS for the all-order strict positive inverse and phase/shape identity, while the exact constant and Landau example are explicitly prior in Hindov et al. 2026. No claim of independently inventing classical total positivity or Cauchy projection.

## value

PASS

Adds mathematically motivated rigidity and a quantitative identity to a sharp finite Sobolev inequality: phase frustration and distance to the optimizer line are distinct, nonnegative and exactly exhaustive, with all complex equality cases. The strict Green positivity explains uniqueness structurally. Researchers studying discrete higher-order derivative extremizers and stability could need this precise decomposition; not merely recomputation of known best constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
