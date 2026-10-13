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

The computational certificate checks the exact optimization underlying the finding.

For small values of \(N\) and \(m\), it enumerates every weak composition of \(N\) into \(m-1\) nonnegative transition weights and confirms that the minimum possible largest part is

\[
\left\lceil\frac{N}{m-1}\right\rceil.
\]

For a larger grid it constructs the quotient-remainder balanced distribution and directly checks: total outgoing weight \(N\); zero root self-weight; maximum part equal to the claimed ceiling; satisfiability of the two graded thresholds; and the \(0/1\)-weight condition exactly when \(m\ge N+1\).

Replay with:

`python3 artifacts/verify.py`

The expected output begins with `VERIFY_OK` and includes the exact assertion count.

Observed output: `VERIFY_OK 199425 exact assertions`
