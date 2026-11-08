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

For n>=4, with T counting triangles and W counting *induced open* wedges on unordered triples, split ordered pairs of three-label supports into equal, shared-edge (exactly two common vertices), or edge-disjoint (at most one common vertex) classes. Equal supports contribute E[I_A J_A]=0, shared-edge supports give 2(q4-q5), and disjoint ones give 3(q5-q6), where qj=(m)_j/(N)_j and qj=0 for m<j. There are 3(n-3) shared-edge supports per triangle and B-1-3(n-3) disjoint supports. Subtract 3 B^2 q3(q2-q3) to obtain exact covariance; common-denominator factorization yields negative numerator -48 B q3 (N-m)(N-m-1)[m(n^2-3n-8)+(n-1)(n^2-n-4)] divided by product (n+1)(n+2)(n^2-n-10)(n^2-n-8)(n^2-n-4). All denominator factors positive n>=4; final bracket positive in 3<=m<=N-2 including n=4, and all other levels vanish by deterministic/absent triangle cases. Under G(n,p) disjoint edge supports independent, same-triple covariance -3p^5(1-p), shared-edge covariance p^4(1-p)(2-3p), giving 3Bp^4(1-p)[(n-3)(2-3p)-p] with threshold 2(n-3)/(3n-8). Independently recomputed exact factor for EVERY n=4..40 and m, with direct exhaustive 64+1024 graph counts for n=4,5; checked the submitted n=6 enumeration algorithm from actual verify.py. Finite checks corroborate, symbolic support-orbit proof covers all n,m,p; equality at p threshold is not statistical independence.

## originality

PASS

Novelty lies in the sharp sign contrast between induced open wedge and triangles for all fixed-edge graph levels and the exact G(n,p) crossing. Existing wedge-sampling work defines open versus closed wedges for estimation, while Chatterjee–Varadhan studies triangle large deviations and Klusowski–Wu studies sampling motifs from fixed graphs. None of the materially inspected relevant primary text states this precise joint covariance law. Broader subgraph-count moment formulas could imply it after specialization, so originality remains best-knowledge and not a negative claim about uninspected texts.

## value

PASS

Triangle and induced open-wedge counts are complementary triadic closure statistics. Their joint covariance calibrates tests/uncertainty for fixed-edge vs independent-edge nulls. A universal strict anticorrelation in G(n,m), versus a positive sparse-regime covariance and a sharp binomial threshold, is a natural structural contrast not given by marginal moments or a routine known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
