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

# Reproduction and scope

Run `python verify.py` with Python 3.10 or later and SciPy installed. The verification program independently evaluates one-dimensional positive integrals using adaptive quadrature; compares both sides of the sharp global Bessel enclosure for a positive parameter grid; checks the elementary tilted first-passage transform and its mean; checks reflection symmetry; and compares finite-rate switching profiles against the derived asymptotic coefficient. Its execution completed with `PASS: 816 deterministic checks`.

The numerical calculations do **not** establish an infinite-range theorem by themselves. The proof is analytic and uses the exact renewal decomposition, a pointwise complementary-error-function inequality, integral identities for modified Bessel functions, their standard large-positive-argument expansion, and a characteristic-function convergence argument. The numerical tests cover selected finite parameter values only. The limiting temporal law is about the duration of the last **successful** excursion, not the total time spent in all failed excursions.

To independently check the proof numerically for other parameters, change the deterministic grids in `verify.py`. No external data files, simulations, downloaded papers, or third-party source code are needed for execution.
