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
# Verification

`verify.py` is a standalone Python-standard-library replay. For every tested tuple \((q,\ell,n)\), it enumerates all \(q^n\) source words and all legal duplication positions. It then performs four checks:

1. Direct tandem duplication agrees position-by-position with insertion of \(0^\ell\) in the independently computed derivative tail.
2. Every pair of source error sets is intersected directly; every nonempty intersection for distinct sources has size exactly one.
3. The direct number of conflicting unordered pairs equals the theorem's closed formula, including tested cases with \(n\le2\ell\).
4. For the binary \(\ell=2\) specialization through \(n=10\), the general formula equals \(2^{n-5}(n-4)(n-1)\) whenever \(n\ge5\).

The bundled `verification_output.txt` is the stdout from this replay and ends with `VERIFY_OK`.

The finite replay does not prove the theorem for untested parameters. Universal correctness rests on the derivative bijection, the unique zero-run transfer characterization, the weak-composition count, and the binomial identity in `RESULT.md`.
