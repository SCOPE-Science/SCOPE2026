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
# Reproducible checks

Run `python verify.py` with Python 3.10 or newer. Optional SymPy enables two additional exact symbolic coefficient identities; without SymPy the script prints that the symbolic check was skipped. The primary mathematical verification consists of the displayed circle-intersection identity, erosion and segment-area decomposition, monotone scalar root, and implicit-function expansion.

The script compares exact eroded areas to an independently derived angular-ray area integral for five representative configurations and four erosion levels, checks the required radius/width identity, root area balance, the parallel-body perimeter/area identity, and the convergence constant at four radii. The expected terminal line is `CHEEGER_DISK_TRIANGLE_CHECKS_OK`. These finite checks are supplementary evidence, not exhaustive verification of an infinite parameter domain.

Independent audit is not performed. The all-radius theorem and first-order coefficient rely on the explicit analytic proof, not on inference from sampled values.
