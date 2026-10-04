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

The theorem is proved symbolically in `RESULT.md`; the finite program is a regression and boundary check, not an infinite certificate.

Running `python3 verify.py` performs two exact-integer checks. First, for every odd prime \(q<5000\), every \(2\le A<25\), and every \(1\le\beta<9\), it compares the truth of \(q^\beta=2^A\pm1\) with the theorem's classified branches. Second, it scans all \(2\le n\le200000\), identifies triangular numbers whose exact prime support is \(\{2,q\}\), and checks every resulting tuple against the classification.

Expected output:

`VERIFY_OK structural=245824 direct=11 q3=2`

The verifier uses only exact integer arithmetic. Its bounded search cannot establish the universal theorem and is not presented as doing so. The critical infinite steps are the coprime-factor allocation, the two factorization arguments for odd \(\beta>1\), the neighboring-powers-of-two argument for even \(\beta\) in the plus branch, and the modulo-\(8\) obstruction for even \(\beta\) in the minus branch.
