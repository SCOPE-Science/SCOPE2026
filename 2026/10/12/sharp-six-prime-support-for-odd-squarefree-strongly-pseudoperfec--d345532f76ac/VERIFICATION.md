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

# Verification and reproducibility
Run `python3 verify.py` next to `cases.csv`; no third-party modules or internet connection are needed. The program tests exact arithmetic rather than floating-point approximations. It reproduces all 87 cases implied by the proof's exact prime bounds, independently verifies the prime list with trial division, compares a bitset recurrence against a complete meet-in-the-middle search, and confirms the six-prime omitted-pair witness. The corresponding output is preserved in `check_output.txt`.

The numerical step is **exhaustive** only because the preceding mathematical inequality restricts all five-prime candidates to \(q\in\{11,13,17,19\}\) and \(r\le384,64,30,25\), respectively. A bounded numerical search without that reduction would not establish the theorem for every odd squarefree integer. The result does not concern nonsquarefree inputs or the numerical minimum of all possible witnesses.
