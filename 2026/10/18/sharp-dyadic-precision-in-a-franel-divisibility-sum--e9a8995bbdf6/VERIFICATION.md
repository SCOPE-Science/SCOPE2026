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

Execute `python VERIFY.py` with Python 3.9 or later and the standard library, within this directory. Expected terminal line: `VERIFY_OK`.

The program reconstructs the Franel recurrence from initial values, checks it independently against the defining sum at small indices, tests Guo's exact finite quotient identity against direct convolution for every \(2\le n\le26\), and checks the binary-digit valuation identity for all transformed summands at dyadic heights \(2\le r\le12\). It also evaluates the original convolution for \(2\le r\le10\) without using the transformed terms and checks its residue modulo \(2^{3r+2}\). It tests the exceptional \(n=2\) boundary.

All checks use integer or exact rational arithmetic; there are no external dependencies or downloaded datasets. Finite reproduction is not an independent proof of the infinite statement, which is supplied in `RESULT.md`. The public source for the key transformed identity is Guo, arXiv:1404.6978v1, equation (2.4), with its induction proof in section 2.
