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

# Reproducible checks and limits

Execute `python3 verify_motif.py` using the standard Python 3 library only. The script:

1. Enumerates all perfect matchings on \(2n\) endpoints for \(n=2,3,4,5,6\), with counts \(3,15,105,945,10395\).
2. Computes isolated-chord counts and induced connected intersection-graph motifs of size \(2\), \(3\), and \(4\), canonicalized up to isomorphism.
3. Verifies each motif's exact rational expectation, covariance, and negative sign against the analytic finite sum; separately verifies the positive sign for the disconnected two-isolate motif.
4. Checks strict negativity of the normalized exact finite sum for \(2\le n\le69\), \(2\le r\le\min(n,10)\).

Observed output: `PASS: 684 exact assertions`.

The proof, not enumeration, establishes all integer sizes and all connected induced realizable motifs. The large-size expansion assumes fixed motif size. Historical originality is qualified by incomplete access to older chord-enumeration texts. This package has received self-review; an independent audit has not been performed.
