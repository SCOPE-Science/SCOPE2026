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
# Verification record

The closed-form claim and all-length recurrence follow from a written combinatorial proof: exact forced-succession block count, Boolean-lattice Möbius inversion, and a three-state rational transfer matrix. Independent software checks corroborate only finite instances.

Run `python verify_recurrence.py`. Its direct exhaustive enumeration checks all \(n!\) permutations for \(2\le n\le10\), and its independent subset DP checks \(2\le n\le14\). It prints `VERIFIED unit two-neighbor formula via brute and subset DP` after all assertions pass. The recurrence additionally evaluates \(n=20,30,50,100\).

Run `python transfer_check.py` from the same directory. It checks the three-state transition matrix against the recurrence for \(1\le m\le59\) and checks a literal Möbius expansion for \(1\le m\le9\). Its success line is `TRANSFER_OK m=1..59, MOBIUS_OK m=1..9`.

These computations are not an independent external audit and do not prove correctness for unbounded parameters by themselves. The all-length result depends on the symbolic proof. Uninspected historical literature could affect originality; the exact claimed scientific scope does not extend to higher tolerance or channel-error corrections.
