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
# Reproducibility and scope

Run `python3 verify.py` using a standard Python 3 installation. The program uses only integer arithmetic, bit operations, and the standard library. It multiplies the coefficient product in \(\mathbb F_2[x]\) and compares the resulting exact parity counts to the matrix recurrence for \(b=2,\ldots,10\) at 63 complete tested blocks. It separately compares 35,258 individual polynomial coefficient parities with a generalized Stern recurrence, checks all three-state matrix identities through level 100, and checks the binary divisibility-by-three parity condition on indices 0 through 50,000. The program prints `CERTIFICATE_OK` if and only if its assertions succeed.

These are finite, exact consistency tests. The proof for every \(b\ge2\), all block levels, and the infinite counting-function asymptotic is in `RESULT.md`; no independent audit is asserted.
