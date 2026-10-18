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

The exact-one-burst channel was checked directly: for each enumerated word and burst length, the program builds the **set** of distinct words after deletion of each consecutive block. It separately calculates the proposed distance-edge mismatch statistic and checks equality. The program constructs empirical joint tables for every pair of distinct burst lengths, checks the sharp independence threshold on all occupied **and unoccupied** table cells, checks the exact simultaneous-minimum count, and computes covariance by exact `fractions.Fraction` arithmetic. It also enumerates every triple of distinct burst lengths and checks the stated centered mixed moment with rational arithmetic.

Reproduction: extract `checker.py` and run `python3 checker.py` with Python 3 standard library. Tested on all words over alphabet sizes \(2,3,4\), respectively up to lengths \(9,7,6\) (19 complete alphabet/length cases). The expected terminal line is `ALL_BURST_JOINT_STATISTICS_PASSED 19 parameter_cases`. The finite tests do not certify unbounded parameters; the proof in `RESULT.md` establishes them.

No independent audit or expert validation was carried out. The originality assessment is based on inspected scientific literature and actual research-record searches, with residual risk from terminology outside burst-deletion coding theory.
