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

The analytical verification uses the exact barycentric inequalities and explicitly constructs an integer point whenever the ceiling condition holds. Reducing the condition by residues proves the full range for every nonnegative integer dilation. A finite residue-multiplicity calculation proves the gcd floor-sum identity and establishes the all-parameter gap count.

Run the self-contained `check.py` using Python 3. Its output is `REEVE_RANGE_OK exhaustive_instances= 75 symbolic_template_parameter_pairs= 276`. The 75 direct lattice-point enumeration tests include dimensions three through five and both pre- and post-threshold dilations; the 276 parameter-pair tests check several post-threshold dilations. Finite computations supplement but do not establish universal correctness. No independent scientific audit has been carried out.
