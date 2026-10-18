---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

PASS: In the complete five-vertex graph, every four-distinct even-degree edge multiset is one of 15 squares; exact quartic expansion gives 3S²−2T+24*sum_C(product a_e). Every pair of ten edges belongs to exactly two squares, yielding the explicit positive quartic sum-of-squares identity at 32/5. The uniform array gives moments EQ²=10 and EQ^4=640, so bound is sharp; nonzero equality implies common magnitudes and balanced 4-cycle signs, hence a global switched-cut signing (32 sign arrays). Vertex sign switches and permutations force the optimal ellipsoid to be proportional to the coefficient l2 norm. Independent exact sign-cube moment/SOS evaluations for n=5 corroborated the symbolic certificate.

## originality

PASS

PASS best-of-knowledge: Theorems of Ivanisvili–Tkocz provide general homogeneous Walsh moment inequalities depending only on degree and p,q, e.g. degree-two L4/L2 at most 3, not sharp (32/5)^(1/4). The newly audited n>=6 complete quadratic family has an analogous uniform moment formula but explicitly excludes n=5, so it is not a literal prior-specialization theorem; while extending its method to n=5 may be possible, the pair-balanced K5 SOS certificate and equality classification are explicitly distinct finite-boundary results. No earlier published K5 exact norm or BM table was identified; residual historical equivalence remains.

## value

PASS

PASS: K5 is the smallest complete-edge Walsh support where every adjacent and disjoint edge pair appears in precisely two 4-cycles, enabling a particularly explicit 90-square global certificate and full sign-extremizer classification. The ten-dimensional L4 Banach space and exact BM distance are canonical, motivated finite-dimensional invariants, not an arbitrary calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
