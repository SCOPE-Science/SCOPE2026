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

# Reproducibility

Run `python3 verify.py` from the extracted directory. The checker uses only the Python standard library. It enumerates all order-preserving extensive partial injections on \([n]\) by independent domain and image subsets; compositions are computed as partial-function dictionaries and compared directly. The checker verifies the Narayana-convolution distribution of the number of strict edges for \(1\le n\le8\), the Catalan total sizes, and the exact commutation count with one independently selected partial identity through \(n=7\), with two through \(n=5\), and with three through \(n=4\). Expected final output:

`VERIFY_OK: all rank histograms n=1..8; direct products k=1 n<=7, k=2 n<=5, k=3 n<=4`

These checks are exhaustive only in the displayed finite ranges. The universal generating function and singularity regimes require, and are established by, the symbolic arguments in `RESULT.md`; the checker does not constitute exhaustive or independent proof for arbitrary dimension. The one-idempotent count equals the known OEIS A225887 sequence and is not presented as a novel numerical result. Independent mathematical audit has not been performed.
