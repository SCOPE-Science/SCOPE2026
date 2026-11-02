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
# Verification of the finite-field affine-group rank-two classification

The complete arithmetic proof is in `RESULT.md`. The finite computational checker `verify.py` evaluates the *complete* eight-atom two-move invariant for every specified finite field; it is not used to extrapolate the infinite theorem. It constructs two independent descriptions: an exact cyclic-multiplier formula for every prime power, and direct field/group multiplication for fifteen test cases.

Run `python3 verify.py` from the folder containing the embedded files. The program requires only Python's standard library. It asserts pairwise distinction of the fifteen reference spectra, matches the arithmetic classifier on all 98 prime-power fields of order at most 401, and checks exact ordered-pair atomic diagrams by direct group multiplication for the listed small fields. See `verification_output.txt` for exact output.

The mathematical argument separately proves the complete infinite field partition using the cyclic complement, conjugacy, roots and characteristic cases. No finite bound is claimed to prove all prime powers; the independent test cases check implementation and boundary behavior. Independent audit is not performed.
