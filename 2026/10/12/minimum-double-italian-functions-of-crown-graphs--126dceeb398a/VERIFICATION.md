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
The checker exhausts every map \(f:V(\operatorname{Cr}_n)\to\{0,1,2,3\}\) for \(2\le n\le5\), tests the exact double Italian inequalities, and for \(n=4,5\) compares the complete minimum-family with the copied compositions of side total \(3\).

```text
VERIFY_OK
n=2: gamma_dI=6, minimum_functions=16
n=3: gamma_dI=6, minimum_functions=18
n=4: gamma_dI=6, minimum_functions=20
n=5: gamma_dI=6, minimum_functions=35
quaternary_labelings_checked = 1118464
for n=4,5 all minima matched identical-side compositions of total side weight 3
```
The finite computation is corroborative only; the arbitrary-order theorem follows from the analytic side-weight proof.
