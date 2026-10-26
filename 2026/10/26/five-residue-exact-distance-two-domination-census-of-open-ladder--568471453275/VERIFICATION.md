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

The standalone `verify.py` checks the exact ladder metric against its two parities for all pairs of vertices in orders \(1\le n\le20\), counts dominating center sequences of the squared path independently for \(1\le n\le18\), and brute-forces all vertex subsets of the original ladder for \(1\le n\le9\). Each result matches the coefficient theorem. It further checks \(H_{5m}=1\) and \(H_{5m-1}=(m+1)^2\) for \(1\le m\le30\). The script requires only the Python standard library.

The checks are finite corroboration; the interval, parity, and deficit-bijection arguments prove the formula for every positive integer \(n\).

Recorded output is in `verify_output.txt` and is reproducible by `python verify.py`. Independent mathematical audit has not been performed.
