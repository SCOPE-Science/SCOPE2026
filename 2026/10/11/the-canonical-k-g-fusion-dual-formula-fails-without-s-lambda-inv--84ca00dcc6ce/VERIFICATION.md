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

PASS. The restricted inverse C^{-1} of C=S|_{R(K)} maps S(R(K)) back to R(K); its adjoint reverses these spaces. C^*(C^{-1})^*=I_{R(K)} is true, but the source replaces C^*=P_R S with unprojected S. Exact H=C^2, K=projection onto e1, Lambda=[[sqrt2,1/sqrt2],[0,sqrt(3/2)]] yields S=[[2,1],[1,2]], bounded lower/upper bounds 1,3 and S(C^{-1})^*e1=e1+(4/5)e2 !=Ke1. Algebraically S(C^{-1})^*|_R=I_R iff S^2R subset R; S positive and self-adjoint implies invariance under S via functional calculus. Hence theorem fails even under its closed-range and frame hypotheses; the equivalence concerns the displayed first reconstruction identity, not unrelated infinite-dimensional closedness claims.

## originality

PASS

PASS, best-of-knowledge. Original Sadri–Ahmadi–Rahimi arXiv:1806.03595v1 Theorem 3.3 and the 2020 journal Theorem 8 were materially read and use the exact false first identity. Later K-fusion (not K-g-fusion) theory reconstructs with P_{R(K)}S(C^{-1})^*, which diagnoses the type issue but neither states the source-specific two-dimensional K-g-fusion counterexample nor the iff invariance criterion. Generic K-frame theory admits noninvariant ranges, but this by itself does not prove the canonical dual formula fails. No exact correction/erratum found; unindexed coverage remains risk.

## value

PASS

PASS. The missing projection invalidates an advertised canonical K-g-fusion dual even in C^2 with all hypotheses satisfied, and the exact invariance boundary identifies when the reconstruction does hold. This is a structural defect affecting an actual dual frame construction, not an unmotivated matrix type test. The projected restricted-adjoint distinction makes the correction mathematically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
