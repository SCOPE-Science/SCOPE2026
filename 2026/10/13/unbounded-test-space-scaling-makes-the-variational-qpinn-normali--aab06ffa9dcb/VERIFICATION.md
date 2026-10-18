---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The source defines H_M as a full finite-dimensional span (p35 Eq4.13) and E(Theta,v) as a linear functional in v (Eq4.14). A8 on p36 states a finite unit maximum of the diagonal second moments over w∈H_M×∂B; E(Theta,c v)=c E(Theta,v) gives second moment c² times the original for any c, so every nontrivial variational moment makes this supremum infinite. The parameter derivatives remain linear in v, hence the first-component discrepancy D_t(v) in Theorem4.3 p46 Eq4.109 is homogeneous and has infinite supremum unless D_t≡0. The proof Lemmas4.1–4.2 explicitly assume ||v||_{1,B}≤1 (p37–38), whereas A10 merely bounds each chosen basis test v_i. The paper A12 also stipulates positive covariance diagonal for all v, including v=0, another related incompatibility. Full relevant source pages 34–48 actually read using authorized institutional extraction. Pure scaling argument covers every c without numerical sampling.

## originality

PASS

This is a precise domain inconsistency in the initiating 59-page article, not claimed as a new general functional-analysis lemma. VPINN frameworks with normalized finite tests and dual norms are prior, and mathematical homogeneity is elementary; the nontrivial incremental finding is identifying failure of the particular paper’s A8 and its central variational lazy-training theorem as literally written. No identical erratum was identified in Resultary or inspected source, but later author correction remains possible.

## value

PASS

The literal unbounded test domain makes an explicit probabilistic normalization and the advertised uniform-in-input variational approximation logically degenerate except for trivial variational outputs. Identifying that the local proof hypotheses ||v||≤1 are not the theorem domains materially affects interpretation and validity of a central result in an applied-math analysis. A unit-ball repair is proposed only as necessary, without claiming to prove a corrected theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
