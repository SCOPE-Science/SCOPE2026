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

# Verification procedures and scope
The standalone `verify.py` tests the exact Hamiltonian directly against the domain-wall characterization for spin lengths \(3\le N\le10\), multiple deterministic bond-order permutations, and cooperative budgets \(1\le r\le\min(4,N)\). Every spin state and every allowed flip subset are checked; positive integer bond strengths make equality tests exact. The script additionally enumerates all permutations of the union of two sliding bond windows for representative radii and separations, comparing frequencies to the claimed rational joint probabilities. The program uses only Python's standard library. Run `python verify.py` in the directory containing this document and the script.

These are genuine finite reproducibility checks; they cannot establish an all-size theorem or the Gaussian limit. The exact proof in `RESULT.md` supplies those implications via boundary-energy identities, exchangeability and finite-dependence probability theory. No independent audit has been conducted.
