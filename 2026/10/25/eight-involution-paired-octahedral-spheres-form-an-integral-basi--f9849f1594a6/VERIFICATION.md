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

# Reproducible finite verification

Install dependencies with `python3 -m pip install -r requirements.txt`, then execute `python3 verify_tietze_central_lattice.py` and `python3 verify_tietze_independent.py` from the extracted package directory. The main script uses exact integer simplicial chains, an exhaustive directed-Hasse acyclicity check, gradient-path elimination over unit coefficients, an integer determinant of \(-1\), and automorphism enumeration. The second script uses an independent presentation of the Tietze graph, exact finite-field ranks, and signed Lefschetz traces. The success markers are `VERIFY_OK_TIETZE_SHORTEST_OCTAHEDRAL_REGULAR_C2_LATTICE` and `VERIFY_OK_INDEPENDENT_TIETZE_J3_AND_LEFSCHETZ`, respectively.

The complete finite computation is a proof certificate for this one finite graph in conjunction with the flag-support argument and discrete-Morse homotopy theorem stated in `RESULT.md`. Modular ranks alone would not prove the integral result; the determinant and integral chain transformations provide that step. Neither program is an external independent scientific audit, and exhaustive finite computations do not establish assertions for an infinite family.
