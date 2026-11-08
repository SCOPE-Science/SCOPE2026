---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The exact theorem is alpha(Gamma_{7,2,2})=11 for binary length-seven codewords with received length-five subsequences, duplicate embeddings counted only once. Independently enumerated D_2(x) by every choice of five retained coordinates for all 128 length-seven words, without running the packaged verifier. The eleven displayed distinct codewords have 32 received-word loads: twenty-six 2, five 1, one 0, so all loads <=2. The 32 listed nonnegative integer weights sum to 326. Independent exact enumeration establishes S(x)>=59 for each of the 126 nonconstant x, with minimum 59 (attained 34 times); each of the two constant words has S(x)=52, hence S(x)+7*1_{constant}(x)>=59 for all 128 words. For any feasible code summing the 128 universal inequalities over chosen x gives 59|C| <= sum_y w_y m_C(y)+7*c <= 2*326+14=666. Since 666/59=11.288...<12 and cardinality integral, |C|<=11. This is a complete finite dual certificate with a matching independently checked witness, not sampled experimentation or a solver log. Domain does not extend to other n,k,t.

## originality

PASS

The original claim is the exact finite packing optimum A^{del}_{2,2}(7)=11. An independently checked 11-word witness and rational packing dual establish it. Exact-parameter/alias searches and direct comparison with the full nearby Resultary n=6 published record, the full Lin 2026 paper text and Guruswami–Håstad Section 4 found no statement or stronger theorem implying this value. This is best-of-knowledge originality with an explicit risk from unindexed finite tables, not an assertion that no other proof exists.

## value

PASS

For deletion-channel coding the maximum list-decodable size is a natural extremal invariant: it calibrates the n-versus-list tradeoff beyond asymptotic existence bounds. Parameters k=t=2 are specifically motivated by Guruswami–Håstad and Lin, and n=7 is the immediate next finite case after the already published n=6 optimum seven, whose rational certificate does not mechanically imply eleven. The new independent 32-coordinate rational packing dual is a short reproducible benchmark for testing proposed finite methods, and the precise integer optimum can be cited directly in future studies of deletion hypergraphs. This is an exact self-contained finite finding, not a claimed general theorem or code classification; the value does not rest solely on reproducibility or novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
