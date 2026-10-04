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

`verify.py` checks the stated binary \((3,2)\) read map in two direct implementations, exhaustively reconstructs all fibers for \(m=1,\ldots,9\) (through source length \(19\)), and compares every realized fiber with an independent endpoint-state dynamic program. It also checks the two Fibonacci extremal recurrences through \(m=100\) and the induction inequalities over all reachable endpoint-count pairs through prefix length \(15\). The recorded run ends with `VERIFY_OK`.

The finite computation is not used as proof for arbitrary \(m\). The unbounded claim rests on the recurrence and induction written in `RESULT.md`. No statement is made for other window/shift pairs, nonbinary alphabets, or noisy read vectors.
