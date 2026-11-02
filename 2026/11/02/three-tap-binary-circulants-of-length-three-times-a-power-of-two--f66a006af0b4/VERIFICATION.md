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
# Reproducibility of exact checks

Run `python3 verify.py` with only the Python standard library. The checker evaluates gcds in binary polynomial arithmetic directly on all \(\binom{3\cdot 2^k}{3}\) possible three-tap supports for every \(0\le k\le4\), compares the resulting nullity histogram with the claimed closed census, and then explicitly enumerates every codeword in the kernel ideal for all \(0\le k\le3\). It checks the annihilator condition and the complete Hamming weight distribution for each kernel stratum.

Observed final line on the packaged standalone program:

`VERIFY_OK three_tap_matrices 19561 kernel_words 66112`

The calculations cover finitely many sizes. The algebraic theorem for all \(k\ge0\), including the generalized-weight hierarchy, rests on the written proof, not a finite sample or an external computational certificate. Independent review has not been performed.
