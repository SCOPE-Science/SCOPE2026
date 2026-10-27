---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof derives the admissible coefficient range from \(D(x^m)=m x^{m-1}D(x)\), then computes the rank from the monomial image of the formal derivative and the kernel ideal of multiplication by \(D(x)\). The valuation strata are counted exactly. The finite tests are auxiliary only.

The accompanying script uses only the Python standard library. It exhaustively checks every admissible coefficient vector over \(\mathbb F_2\) for \(m=2,\ldots,7\), over \(\mathbb F_3\) for \(m=2,\ldots,5\), and over \(\mathbb F_5\) for \(m=2,\ldots,4\). All 13 cases pass. The script does not test non-prime finite fields; the proof handles all \(q=p^e\).

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
