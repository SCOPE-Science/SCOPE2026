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

The attached `verify.py` uses only the Python standard library and calculates the multinomial-power sums by a recurrence independent of the binary-digit result. Run:

```sh
python3 verify.py
```

The adjacent `verification_output.txt` reports successful checks for all indices \(0\le n\le512\), all levels \(1\le\ell\le32\), and heights \(2,4,6,8\); exact independent factorial enumeration for \(1\le\ell\le6\), \(0\le n\le10\); exact count of valuation-one terms through \(n=12\); and exact dyadic four-residue frequency counts through \(2^{10}\) for eight representative levels.

The proof relies on the exact Legendre identity \(\nu_2\binom n{k_1,\ldots,k_\ell}=\sum_{i\ge1}c_i\), carry-free and single-carry enumeration, and arithmetic modulo eight. The code supplies finite consistency checks, not independent validation of an infinite statement. Moduli \(16\) and above, odd heights, and originality outside the inspected sources have not been established.
