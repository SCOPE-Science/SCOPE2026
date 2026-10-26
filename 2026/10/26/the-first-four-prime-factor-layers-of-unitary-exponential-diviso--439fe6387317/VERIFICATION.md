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

# Verification protocol

Run `python verify.py` from the directory containing this file. The program uses only Python's standard library, computes prime factorizations, and independently evaluates the multiplicative formulas \(\sigma^*(p^a)=1+p^a\) and \(\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d\) for all integers through \(10^6\). It checks every instance with \(\Omega(n)\le4\), including the complete \(p^2qr\) subfamily within that bound, and verifies that the only equality cases are \(1,20,45\).

Expected terminal marker:

`VERIFY_OK: n<= 1000000; omega<=4 tested=737449; p^2*q*r instances=87338; matches=[1, 20, 45]`

The explicit congruence and forced-factor proof in `RESULT.md` establishes the infinite theorem. The finite computation does **not** certify any number beyond its tested range or establish originality. Independent audit has not been performed.
