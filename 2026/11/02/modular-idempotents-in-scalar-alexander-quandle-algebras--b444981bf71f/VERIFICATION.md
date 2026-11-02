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
# Reproducibility and verification

Run `python verify_modular_alexander.py` with Python 3 and NumPy. `verification_output.txt` contains the output of that checker executed on the packaged version of the code.

The checker performs exhaustive direct multiplication for all coefficient tuples over \(\mathbb F_5\) and \(\mathbb F_7\) in the one-dimensional scalar Alexander quandle algebra, for all admissible scalars. Direct element-by-element idempotent counts are \(6\) at every admissible \(p=5\) parameter, and \(8,50,50,50,8\) for \(p=7\), parameters \(2,3,4,5,6\). The exact search sizes are \(5^5\) and \(7^7\) elements per parameter.

An independent modular Gaussian-elimination computation forms \(T_\lambda+T_{1-\lambda}-I\) on the additive group-ring augmentation ideal in dimension two and measures its kernel for selected parameters \(p=5,7,11\). The recorded dimensions agree with the asserted \(r(p^d-1)/(p-1)\). Finally, the program checks closure of all nonzero idempotents under quandle multiplication for \(p=7,d=1\) at scalar values \(2\) and \(4\). The run terminates with `VERIFY_OK`.

None of these finite enumerations is used as a proof for untested dimensions, characteristics, or extension fields. The universal proof is the separate unit-group representation argument in RESULT.md. There is no independent mathematical audit or machine-formalized infinite proof.
