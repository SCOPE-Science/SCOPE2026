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

The standalone `verify.py` independently traces each orbit in the residue rings modulo \(2^k\) for all \(1\le k\le15\). It compares per-point minimal preperiod and eventual period with the exact formulas, verifies the complete cycle and odd-tail census at each precision, and checks the odd-incoming leaf counts on each nonfixed cycle (including the fact that exactly two cycles are incident when an odd-tail period is present). It also evaluates 99 independent integer starting points across repeated doubling of iterate counts and checks the valuations against the lifting identity. All computations use exact integer arithmetic and modular reduction; no external packages are needed.

Expected successful output: `VERIFY_OK: 65534 independently traced dyadic starting states; 15 cycle and tail censuses; 99 valuation-lifting samples and 40 distinguished leaf-bearing cycles`.

Finite exhaustive computations at the stated precisions do not prove the formulas for arbitrary precision; the universal proof appears in `RESULT.md`. Earlier literature establishes the even-state Chebyshev period classification; that known portion is separated from the new odd-branch incidence conclusion. Independent audit has not been performed.
