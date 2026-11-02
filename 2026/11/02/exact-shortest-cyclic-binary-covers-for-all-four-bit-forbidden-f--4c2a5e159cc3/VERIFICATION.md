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

# Reproducible finite proof checks

Place `certificates.json`, `verify.py`, and `check_small.py` in the same directory. Run `python3 verify.py certificates.json` and `python3 check_small.py certificates.json` with a normal Python 3 interpreter. The former checks each integer primal arc multiset against every mandatory binary word, all vertex-balance and dual inequalities, primal/dual equality, connectedness, and the actual circular factor coverage of a reconstructed Euler tour. It checks exactly 72 cases at orders 4 through 15 and reports `VERIFY_OK 72 exact optima`. The latter directly enumerates indexed binary circles at lengths 15 and 16 for all six order-four representatives and reports `CROSSCHECK_OK`.

Neither verifier runs an optimization solver. All mathematical certificate inputs are embedded in the package and are checked as exact integers. These checks prove only the 72 finite minima; they do not prove an all-order pattern, exclude unidentified historical earlier computations, or constitute an independent external scientific audit.
