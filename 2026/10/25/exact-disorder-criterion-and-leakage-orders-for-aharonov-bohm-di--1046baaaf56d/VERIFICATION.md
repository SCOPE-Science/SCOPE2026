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

# Verification record

The supporting executable `verify.py` checks the two minimal hub-to-hub moments with exact SymPy algebra. It then generates random finite periodic diamond chains with complex bond amplitudes, balanced interference, and independently varying real hub and arm energies. It constructs both the original Hamiltonian and a separately assembled direct sum of three-site matrices, tests their unitary equivalence and eigenvalue agreement, and verifies no dynamically propagated amplitude escapes the prescribed five original sites.

For perturbed systems it separately breaks the complex interference balance and the arm-energy equality, confirms the leading Taylor coefficients, and tests actual short-time transition probabilities using matrix exponentials. The reproducibility program requires Python 3, NumPy, SciPy and SymPy. Run `python3 verify.py`; the reference execution returned `TOTAL_ASSERTION_GROUPS= 3378` with no failed assertions (650 each for exact blocks, eigenvalues, confinement dynamics, path errors and energy errors; 125 direct small-time comparisons; two symbolic moment identities and one fixed example).

The finite calculations are not exhaustive over unbounded lattice sizes or continuous parameters. Infinite-chain conclusions are established by the analytic invariant-space decomposition and the bounded-operator Taylor expansion in `RESULT.md`. No formal-machine or independent third-party proof review has been performed.
