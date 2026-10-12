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

The verifier constructs the tree \(T_q^{(2)}\) directly with center \(c\) and paths
\[
c-u_i-v_i-w_i.
\]

For every labeling it checks the two defining conditions independently of the proof:

1. each label-\(0\) vertex has exactly one neighbor labeled \(2\);
2. every positive-labeled vertex has a positive-labeled neighbor.

It exhaustively checks all labelings for
\[
q=2,3,4,
\]
namely
\[
3^7+3^{10}+3^{13}=1{,}655{,}559
\]
labelings. For \(q=3,4\), the exact minimum values and the complete minimum-function sets agree with the theorem. The boundary \(q=2\) is recorded separately.

It also constructs every theorem-predicted minimum function for
\[
3\le q\le50
\]
and directly verifies the definition, weight, and count.

Recorded output:

```text
VERIFY_OK
q=2: gamma_tRp=7, minimum_functions=24
q=3: gamma_tRp=9, minimum_functions=6
q=4: gamma_tRp=11, minimum_functions=8
full_labelings_checked = 1655559
constructed_parameter_range = 3..50
all exhaustive q>=3 minima matched the two exceptional-arm types
```

The finite checks do not establish the arbitrary-\(q\) theorem. The proof for all \(q\ge3\) is the symbolic center-label and arm-cost argument in `RESULT.md`.
