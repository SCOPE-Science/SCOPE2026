---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Condition on each specified H-component vertex set A: all crossing edges are absent, exterior Bernoulli(p) graph is independent, inside H contributes t_F(H), and connected F cannot straddle A. Subtract unconditional motif expectation and sum indicators to derive exact Cov(C_H,X_F)=E[C_H](t_F(H)-Q_F p^e(1-p)^s), with E[C_H]>0 and Q_F>0. The p-factor is monotone if s=0 and strictly unimodal if s>0; all endpoints t=0, t=Q and r=M are treated. For P3 inside an h-tree t=W=sum_v C(d_v,2); degree-excess transfer gives sharp unique path/star extremes, and the n>=h+1 induced ratio lies below 4/27. Independent complete rational G(n,p) enumerations reproduce eight mixed component/motif examples for n=4,5, both induced and noninduced. This is a universal conditional-expectation proof, not a deduction from those eight tests.

## originality

PASS

Qualified best-of-knowledge PASS for the connected-component-versus-connected-motif Palm factorization, exact induced sign phases, and sharp tree-shape extremes, not for generic overlap/covariance conditioning or already-known isolated-edge/triangle special cases. Exact basic covariance techniques are old; the mathematical content is the unified local t_F(H) law with the two-switch and tree envelope. A broad old moment theorem could conceivably imply it implicitly.

## value

PASS

Connected-component type versus motif occurrence are natural random-graph observables; the exact sign of their dependence matters for motif-based inference. The full all-connected H,F identity gives a reusable component Palm law, while induced motifs exhibit a genuinely different two-transition regime, and paths/stars are uniquely extremal tree shapes. These exact structural boundaries are more than a normalization check, although the conditional expectation technique is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
