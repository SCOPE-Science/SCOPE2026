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

## Reproduction
Run `python3 verify.py` using the included standalone Python script. It uses `Fraction` to evaluate the recurrence \(n a_{k,n}=\lambda\sum_{j=1}^{\min(k,n)}j a_{k,n-j}\) exactly at rational endpoints for fourteen orders. It asserts that the candidate coefficient crosses one between adjacent millionth endpoints and that **every other** positive-index coefficient through \(40k\) remains below one at the upper endpoint. The script also checks \(kB_k<4\) and the integer inequality \(2\cdot4^{41}<41!\); the proof in `RESULT.md` converts those into a uniform bound for every index beyond \(40k\).

## Observations
The program completed with `VERIFY_OK: 14 rational brackets, complete finite prefixes and global tails`. For order fourteen, the highest alternative coefficient at its upper endpoint is at index \(23\), approximately \(0.9804140877\); for order fifteen the highest alternative is index \(26\), approximately \(0.9994719538\), strictly below one. Those decimals are illustrative: all asserted signs are checked as **exact rationals**. At order fifteen, the unique crossing coefficient belongs to index \(25\) and its root lies between \(0.250227\) and \(0.250228\).

## Limits
Exact finite recurrences alone would not prove a global-mode statement on an infinite support. The mathematical proof supplies the infinite-tail bound, strict monotonicity, and the argument for all real intensities in the certified neighborhoods. No numerical simulation is used as a substitute for these steps. The result covers only initial transitions for orders two through fifteen. Independent validation has not been performed.
