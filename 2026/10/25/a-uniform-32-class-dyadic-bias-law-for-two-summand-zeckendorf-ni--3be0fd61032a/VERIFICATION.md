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

# Reproducibility

Run `python3 verify.py` with Python 3 and no additional packages. It verifies the exact base-32 frequency distribution, the full pair convolution, residues of each recurrence period for seven moduli from 32 through 2048, and direct legal-pair enumerations. Successful execution prints:

`VERIFY_OK powers=5..11 residue_cells=4064 mod32_pair_convolution=PASS exact_index_pairs=16 class_bias=PASS`

These checks are finite, exact integer tests. They do not establish the all-exponent induction, originality, or an independent mathematical audit. The universal claim depends on the proof in RESULT.md.
