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

# Verification of the cyclic progression theorem

Run `python verification/check_ap.py` from the directory containing these files, with a Python 3 interpreter and SymPy installed. `verification/checked_output.txt` contains an actual execution and ends in `VERIFY_OK`.

The checker independently enumerates all distinct modular progression triples and the complete one-skeleton; it reconstructs the signed integer simplicial boundary matrix, calculates its integral Smith normal form, and verifies both predicted free Betti numbers and every nontrivial torsion invariant factor for the primes \(5,7,11,13,17,19,23,29,31,37,41,43\). It also checks the signed-doubling orbit partition and expected cell counts. It uses no stored boundary matrix, precomputed homology, or other files.

The integer Smith checks support the all-prime theorem but do not certify it at untested primes; the group-theoretic proof in `RESULT.md` covers every prime \(p\ge5\). The calculation does not determine higher homotopy or cover composite moduli. No independent external mathematical review has taken place.
