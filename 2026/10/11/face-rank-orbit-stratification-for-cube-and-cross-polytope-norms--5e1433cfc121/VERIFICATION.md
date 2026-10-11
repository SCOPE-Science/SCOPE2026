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

The mathematical assertion is established by the four analytic steps in `RESULT.md`, not by numeric sampling. The norm-one matrix construction on \(\ell_1^n\) is a weighted barycentric perturbation of columns in a positive simplex face. The norm-one matrix construction on \(\ell_\infty^n\) has a leading active diagonal block and a lower \(\varepsilon I\) block, hence full rank.

The standalone `check_orbits.py` requires Python's standard library only. Executing `python check_orbits.py` produced:

`PASS l1_instances=119 linfty_instances=119 dimensions=2..8 exact_rational=True analytic_proof_required=True`

All tested instances use exact rational arithmetic to check matrix rank, input-output equations, and all column (respectively row) sums of absolute values. The script does not exhaust all real or complex coordinate values, and the proof does not depend on the script. Independent audit has not been performed.
