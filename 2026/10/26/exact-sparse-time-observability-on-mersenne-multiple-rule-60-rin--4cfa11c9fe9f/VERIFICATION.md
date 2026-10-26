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
# Verification of the exact sparse-sampling rank law

Run `python verify.py` with Python 3. The program computes \(\mathcal O_{n,q}\) from the actual Rule-60 binary update coefficients, using cyclic bit-vector convolutions and independently implemented Gaussian pivot elimination. It compares this directly computed rank against the claimed formula.

Exact verifier output:
```
VERIFY_OK exhaustive_parameter_cases=528 random_cases=216
example n=7 q=1 rank=7
example n=7 q=7 rank=2
example n=14 q=3 rank=13
example n=14 q=7 rank=3
example n=30 q=3 rank=11
example n=30 q=7 rank=29
```
The fixed grid contains \(r\in\{2,3,4,5\}\), the explicitly chosen \(a\)-ranges in the code, and every \(q\) from \(1\) through \(44\), excluding rings larger than \(128\) sites. The additional 216 tests are deterministically pseudorandom, with a documented seed and a ring-size ceiling of \(300\). These checks verify finite instances, including strides longer than some rings and even/odd sampling intervals. They do not establish the unrestricted theorem by enumeration: the polynomial/group-algebra local-factor proof supplies that step. No independent audit is asserted.
