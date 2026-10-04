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

The exact checker `artifacts/verify.py` implements the SQN recurrence for length six. It uses reversal symmetry only. For each fixed choice through level three, it proves that the objective is affine in the fifth-level split and then affine in the fourth-level split, so testing the fourth-level endpoints is exhaustive rather than heuristic.

The archived run reports:

- `q=7 S=7776 N=14 reduced_profile=(1, 6, 6, 0, 36, 0, 216, 0, 1296, 0) states=1109 best_k5_Blackburn=7776 gap=0`
- `q=8 S=16807 N=16 reduced_profile=(1, 7, 7, 0, 49, 0, 343, 0, 2401, 0) states=2950 best_k5_Blackburn=16807 gap=0`
- `q=9 S=33872 N=6552 reduced_profile=(2, 7, 12, 2, 88, 0, 640, 0, 4656, 0) states=4762 best_k5_Blackburn=33614 gap=258`
- `VERIFY_OK`

A second implementation check compiled and ran the public `compute_sqn.c` companion solver. It returned the same three optimum sizes and the same reduced profiles. This corroboration is not needed for the exhaustiveness argument.

The count uses the exact product formula for partition choices. At \(q=9\), one orientation contributes \(\binom{9}{2}\binom{14}{12}=3276\) codes; reversal doubles this to \(6552\). Since \(q\ge3\), distinct partition systems for maximal codes are unique, so this counting has no duplication.

No claim is made for alphabet sizes outside \(q\in\{7,8,9\}\) or for lengths other than six.
