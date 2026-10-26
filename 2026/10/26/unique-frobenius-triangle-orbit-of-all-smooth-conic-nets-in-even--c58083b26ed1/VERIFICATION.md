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
# Verification instructions and scope

From a directory containing the two standalone Python programs, run:

```sh
python verify_nets.py
python verify_frobenius.py
```

The first enumerates all linear graphs over polar-form coefficient space for \(q=2,4\), tests every rational parameter point, and independently enumerates the full \(\mathbf F_2\) conic-vector-space census. The second builds the cubic extension fields and enumerates degree-three Frobenius orbits and collinearity by determinants. Both give counts \(8\) and \(960\). The output of these commands is retained in `verification_output.txt`.

These finite tests check sample cases, not the theorem's universal quantification. The uniform proof is in `RESULT.md`. The previously published maximum-dimension/existence assertions are not asserted as new.
