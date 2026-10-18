---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Read and reconstructed exact F_t,H and P_A quantifiers in RESULT.md. For disjoint m-blocks A,B, direct evaluation from definitions (not just source citation) gives H(1_A)=m log m, H(1_A−1_B)=0, hence lower ratio (1+θlog m)/2. For arbitrary finite A of k≤m indices, after ||P_A x||1=1 set r_i=|y_i| and u=|Σy_i|≤1. At t≥1 every logarithm is common log t and F_t(y)=0. At 0<t<1 weighted coordinate log magnitudes are bounded by Shannon entropy ≤log k and |u log max(u,t)|≤1/e. Therefore H(P_A x)≤||P_A x||1(log k+1/e); ||P_A x||1≤||x||1≤||x||θ yields upper for every x,A, including complex vectors; homogeneity and density extend to completion. m=1 lower max1 valid; no conjectured exact leading coefficient claimed.

## originality

PASS

The focal Berná paper arXiv:2610.05052 states a semi-greedy non-quasi-greedy basis and its lower projection growth; the newly audited global all-A entropy upper bound is not stated in the accessible abstract. Results for conditional quasi-greedy Banach bases do not imply it because both applicability hypotheses fail. Exact-source full text could not be read here, so a direct no-overlap assertion for its complete theorems would be unjustified; residual possibility of an unobserved upper bound is explicit. Best-of-knowledge value and originality rely on checked statement-level distinctions, not a failed-search novelty proof.

## value

PASS

k_m is a standard quantitative invariant of basis coordinate projections. For the new semi-greedy but non-quasi-greedy example, global logarithmic upper bound is not supplied by classical quasi-greedy Banach theorems and shows the surprising phenomenon that severe greedy failure coexists with only borderline-logarithmic suppression growth. The full growth order, not merely an artificial finite norm, is a mathematically motivated basis benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
