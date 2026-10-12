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

The theorem is proved analytically in `RESULT.md`. The executable checker `verify_barbell_zero_forcing.py` is a finite corroboration only.

For each \(3\le p,q\le6\), the checker constructs the two cliques and the single bridge, enumerates every vertex subset \(S\), directly runs the standard zero forcing closure, and compares the result with the claimed criterion
\[
|V\setminus S|\le3,\qquad |(V\setminus S)\cap X|\le1,\qquad |(V\setminus S)\cap Y|\le1.
\]
It then verifies the four claimed polynomial coefficients and checks every minimum set against the complement classification.

Expected deterministic output:

`VERIFY_OK parameter_pairs=16 subset_checks=14400 minimum_checks=504 max_order=12`

The computation covers only the listed finite range. The infinite statement for all \(p,q\ge3\) rests on the proof, not on extrapolation from the computation.
