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

# Verification of the finite binary filling-curve census

Run the following commands with Python 3 and SymPy installed from the directory containing the `code/` and `data/` subdirectories:

```sh
python code/biquartic_census.py
python code/biquartic_independent.py
python code/check_agreement.py
```

The first checker row-reduces nine rational evaluation conditions and enumerates 65,535 nonzero solutions; it tests 3,648 rationally nonsingular forms, divides them into 54 orbits, and uses exact characteristic-two SymPy Gröbner ideals on four charts. The second builds the 16-dimensional equation space from the geometric filling ideal generators, uses a separate characteristic-two Buchberger implementation on orbit representatives, and enumerates the full 72-element surface symmetry. The last checker compares all 2,328 smooth coefficient masks exactly, checks the projective-orbit distribution, and matches the 34 representatives in `data/ORBIT_REPRESENTATIVES.json`. On replay it prints `PASS: 2,328 identical smooth coefficient masks in 34 orbits (31x72,2x36,1x24)`.

No bounded search over extension-field points is used as a substitute for geometric smoothness: the unit-ideal tests exclude singular zeros over the algebraic closure. This is an exhaustive finite-field result only, not an externally independent scientific audit.
