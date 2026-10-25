---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For K_{2,m}, m≥3, each pair of branch edges has the same r_i>0. A cut gradient exactly satisfies s_1=⋯=s_m for s_i=(x_i1+x_i2)/2; all independent d_i=(x_i1−x_i2)/2 belong to the range. Averaging any real projection over independent within-branch edge swaps preserves its range/identity and cannot increase weighted ℓ1 norm; character decomposition forces form Pα(s,d)=((∑α_j s_j)1,d) with ∑α=1, even for initially nonsymmetric projections. Its two edge-column weighted norms in branch j equal F_j=max(1,|α_j|)+(R−r_j)|α_j|/r_j. The inequality max_jF_j≥1+max_jc_j|α_j|≥1+1/H (H=∑1/c_j, c_j=(R−r_j)/r_j) holds for all signs and is attained by α_j=(1/c_j)/H∈(0,1). Strict Jensen for x/(R−x) gives λ≤2−1/m iff equal weights, and an overwhelmingly long branch gives λ↓1; the stated one-defect derivative is a rational identity. I independently formed rational edge columns for weights (1,1,1),(1,2,5),(1,1,3,7), reproducing exact norms 5/3,22/15,481/316. Source verify_exact.py and verify_lp.py were inspected, but log labels do not prove universal quantifiers.

## originality

PASS

General weighted graph cut/cycle machinery and averaging methods are established, but the claimed exact *relative cut-space* projection norm for arbitrary positive paired branch weights is not the unweighted *cycle-space* value for K_{2,m}, nor a hyperplane theorem. Best-of-knowledge searches and full relevant sections support a distinct candidate contribution.

## value

PASS

Finite graph cut and cycle projection norms encode the geometry of graph Lipschitz-free spaces. The exact minimum over all linear projections, in an entire dimension and weight family, is a natural structural invariant rather than a chosen-symmetry estimate. Its strict equal-weight worst case, quantified anisotropic approach to 1, and cut/cycle distinction solve nontrivial geometry-of-weights questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
