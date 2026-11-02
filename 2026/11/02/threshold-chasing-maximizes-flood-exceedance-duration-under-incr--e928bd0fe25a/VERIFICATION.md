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

# Verification scope

`checker.py` was run with Python 3 using only the standard library and returned `PASS exact-rational assertions: 36006`. It independently constructs 9,000 admissible pulse-parameter sets across \(n=2,3,4,5,6,7\). For each case it checks the global upper bound for arbitrary gaps and exact attainment by the threshold-triggered largest-first schedules for both linear recession \(f(q)=q\) (via exponentiated duration products) and nonlinear recession \(f(q)=q^2\) (via direct rational durations). Six permutation checks independently confirm the exact \(2,3,5\) example and its ordering.

The proof covers arbitrary strictly increasing locally Lipschitz recession functions satisfying the stated hypotheses, whereas tests cover only two representative recession laws and finitely many parameters. The script does not certify historical priority or physically validate the hydrological idealization. Independent mathematical audit has not been performed.
