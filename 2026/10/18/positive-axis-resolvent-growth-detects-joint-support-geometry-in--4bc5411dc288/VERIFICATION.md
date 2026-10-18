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

The analytic proof (see `RESULT.md`) establishes the power formula, quasinilpotence, positive resolvent integral representation, sharp exponential type of \(E_d\), and matching upper/lower growth rates for each fixed dimension and every nonzero nonnegative input. The support-patch lower bound uses a fixed positive-measure set and is not based on extrapolating numerical data.

Run `python3 check_resolvent.py` using the Python standard library. The checker returns `FINITE_DIAGNOSTICS_OK 42` for selected dimensions and parameters and prints sampled scaled logarithms of the resolvent applied to two explicitly given rectangle-union inputs. These are **finite illustrative diagnostics** and do not certify the infinitely quantified theorem or publication priority. The approximations converge only at the usual logarithmically corrected rate.

Scientific limits: only real positive approach to zero, nonnegative real input, and fixed finite dimension. No independent scientific audit has been carried out.
