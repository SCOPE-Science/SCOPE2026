---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The flag-rank weight is sum of ranks of north-east crossing submatrices of an upper-triangular n-by-n matrix. At total four, a rank-two cut must have adjacent rank-one cuts, and all others zero, forcing a three-index local block with central 2x2 invertible submatrix: (n-2)q^2|GL(2,q)|. Otherwise exactly four rank-one cuts: maximal nonzero superdiagonal 0,1 (single or two disjoint adjacent edges),2,3 yields five disjoint classes, respectively C(n,4)(q-1)^4; (n-1)C(n-2,2)q^2(q-1)^3; C(n-2,2)q^4(q-1)^2; (n-2)(n-3)q^4(q-1)^2; (n-3)q^6(q-1). Direct rank-elimination and complete enumeration over q=2 for n=3,4,5, and q=3 for n=3,4, reproduced each six-class count (including s_2(4,4)=173 and s_3(4,4)=3526). The six-class structural proof is uniform over prime-power q and n>=3. The radius <=4 ball congruence is sum of diagonal-only binomial terms modulo q, yielding C(n-1,4), a NECESSARY condition for nontrivial linear perfect distance-nine codes, not existence.

## originality

PASS

Prior flag-rank metric papers construct the metric and count spheres to radius three in the accessible 2026 source description, but the exact radius-four rank-two stratum was not found. Full same-object predecessor manuscript could not be accessed; this is a qualified best-of-knowledge O pass with an explicit priority risk, not a claim it lacks an appendix.

## value

PASS

The first nontrivial rank-two crossing stratum gives a natural exact sphere size beyond known lower radii, directly relevant to packing/perfect-code necessary arithmetic conditions. An all-q all-n finite-degree polynomial is independently reusable coding data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
