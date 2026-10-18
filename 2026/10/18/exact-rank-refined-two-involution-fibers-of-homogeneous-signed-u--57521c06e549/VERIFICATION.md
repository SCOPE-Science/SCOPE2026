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

The file `checker.py` is self-contained Python 3. Execute `python checker.py`. It enumerates every coefficient matrix in the listed finite configurations over the prime fields of orders 3 and 5, checks the truncated-ring semilinear involution equation, and computes the residual sign and positive-eigenspace dimension. Its expected ending line is `ALL_EXACT_CHECKS_PASSED 13`.

The general proof is independent of enumeration. In particular, the lift-conjugacy induction and stabilizer filtration work for every odd prime-power field. The program does not test extension fields or prove exhaustive validity over unbounded dimensions.

Status: self-review passed; independent audit not performed.
