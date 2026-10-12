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

# Reproduction and verification

Execute `python3 check_theta.py` from the directory containing this file and the included checker. It uses only Python's standard library (`fractions.Fraction`) and no external files or network access. The checker constructs 63 strongly connected integer-rate generators (orders two through eight); verifies stationary mass by independent linear algebra and regeneration; independently compares the post-departure second return moments with resolvent deviation coefficients; verifies strict monotonicity at six exact rational resolvent arguments; and checks endpoint \(\theta\)-steps on a rational grid. It separately tests the three-cycle and complete three-state process at a shared stationary distribution.

Recorded output from the included code:

`VERIFY_OK 63 irreducible generators; 2205 stationarity/return-moment/diagonal checks; 2205 exact-rational theta matrices; two distinct cutoffs at common stationary law`

The general theorem is proved analytically through the strong Markov property, renewal transforms, and strict monotonicity; the finite program is an algebraic consistency check, not an exhaustive proof over all dimensions, rates, implicitness parameters, or timesteps. No separate independent audit has been performed.
