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

The scientific proof is in RESULT.md and the runnable, self-contained supporting checker is `verify_wheel_frontier.py`.

Run `python3 verify_wheel_frontier.py` with Python 3. The checker uses only the standard library; its independent baseline solves a 3-variable linear program by enumerating all triples of active linear constraints, not by restating the proposed phase formulas. It compares both LP values and reconstructed Fourier spectra. An exact `Fraction` branch checks rim lengths 4 and 6 without floating-point rounding. A successful run reports 1,833 numerical comparisons and 48 exact-rational LP checks.

No finite test can certify an all-real-parameter or all-network-size assertion; the universal proof consists of the symmetry reduction, Fourier spectrum, rim minimax, radial domination bound and three threshold comparisons in RESULT.md. The constrained assertion is distinct from the previously known unconstrained wheel solution. Independent expert assessment has not been carried out.
