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

# Reproducibility and checks
The standalone `verify_star_characters.py` uses exact integer arithmetic in Python 3.10+ with standard-library modules only. Running `python3 verify_star_characters.py` reconstructs all finite cubical cells and every signed arm-permutation cellular trace for the five \((m,n)\) cases listed in `RESULT.md`. There are 66 permutation tests on 566, 5551, 1518, 21927, and 55785 cubical cells. Separately, the program checks binomial ordinary first Betti numbers, compares direct full permutation-group character averages to partition formulas for \(3\le m\le6\) and \(1\le n\le7\), and evaluates the partition-derived invariant multiplicities for arm counts three through eight and particle counts one through nine. Its output has been compared byte-for-byte with `verification_output.txt` and ends with `VERIFY_OK`.

The proof of the unrestricted theorem relies on the radial-tree one-dimensional Morse model, the homeomorphism description of fixed configurations, finite-order Lefschetz traces, and formal permutation cycle indices. No finite set of executable tests can establish the theorem for all arm and particle counts. The accepted scientific review is not an independent mathematical audit.
