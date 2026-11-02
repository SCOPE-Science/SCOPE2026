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

# Reproduction and scope

Run `python verify.py` from the directory containing the script. No downloads or third-party packages are required. The script reconstructs every labelled simple graph of order one through five, computes rational greedy-occupancy expectations using the conditioning recurrence, and independently checks those expectations by enumerating every possible vertex ordering. It compares every missing-edge addition and computes orbit representatives under all relabellings. It also checks the infinite-family formula at 25 exact parameter pairs and the pointwise coupling on small parameter pairs.

Observed execution:

`VERIFY_OK graphs=1099 direct_permutations=124469 improving_marked_pairs=240 isomorphism_types=3 family_parameter_pairs=25`

The analytic coupling and integral in `RESULT.md` establish the theorem for all stated integer parameters. Small-parameter testing is only corroborative. In contrast, the five-vertex comparison is genuinely finite and covered completely by the exhaustive enumeration. No independent audit has been carried out.
