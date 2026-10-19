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

# Reproducibility of the finite-horizon path result

The standalone file `verify.py` needs only Python 3 and its standard-library `fractions` and `decimal` modules. Run it from the same directory with `python3 verify.py`. On success it prints the literal message `VERIFY_OK: exact P4 blocks and symmetrization, exact P3 determinants, optimizer bracket`.

The checker constructs each edge-averaging matrix as an exact rational orthogonal projection. It checks the one- and two-update formulas on the zero-sum subspaces using the stated explicit invariant vectors; evaluates all polynomial matrix identities at sufficiently many rational parameters to confirm their coefficients; verifies the exact mean-square expressions on the three-vertex path; and establishes strict opposite signs of the analytic derivative at the rational endpoints \(302839075823/10^{12}\) and \(302839075824/10^{12}\) by exact rational square comparisons (and independently with 75-place decimal arithmetic). It also checks the one-step optimal witness and endpoint derivative values.

The mathematical proof, including strict convexity and strict global reflection symmetrization, is supplied in `RESULT.md` and is not delegated to finite checks. This verification does not establish uniqueness among unknown published claims or replace independent mathematical review. Calculations use no randomly generated examples, external datasets, network calls, or external packages.
