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

# Reproduction and limits

Run `python padovan_perrin_3adic_verifier.py` with Python 3. The script uses no external packages, reproduces the complete matrix computations, the exceptional normalized Hensel increment, and exhaustively verifies all zero indices in one full least period for every exponent \(1\le k\le10\). It also checks the 3-power matrix lift coefficients for \(1\le m\le6\). The total window at the largest exponent contains \(255879\) indices per recurrence; the theorem for arbitrary \(k\) follows from the written congruence proof and does not follow merely from these finite tests.

The proof treats the initial vectors \((1,1,1)^T\) and \((3,0,2)^T\). Different Padovan indexing conventions must be shifted to these exact initial vectors before comparing residue classes. The paper's exact all-exponent zero-count assertions have not been independently audited.
