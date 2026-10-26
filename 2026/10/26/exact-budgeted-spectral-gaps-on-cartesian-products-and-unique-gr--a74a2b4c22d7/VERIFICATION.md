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

# Verification of the mathematical assertions

The analytic proof in `RESULT.md` is the source of the universal claim. The standalone `verify.py` checks sample consequences independently using SymPy exact rational arithmetic and NumPy symmetric eigensolvers. Run `python3 verify.py` with Python 3, SymPy and NumPy installed in the directory containing this document.

Executed results recorded in `verification_output.txt`: eight grid sizes; twenty exact coordinate eigenvector identities; four exact characteristic-polynomial factorizations and four numerical full-spectrum comparisons; 1,440 separately sampled nonseparable conductance vectors checked against the sharp bound; one exact non-path factor example \(K_3\square P_4\) with optimal gap \(1/19\). The script also recomputes every sample budget. Numerical comparisons are finite checks, not an exhaustive characterization of every design. Universality and uniqueness follow from the stated Rayleigh equality conditions and linear recurrence, not randomized enumeration.

No independent mathematical audit or external verification is reported.
