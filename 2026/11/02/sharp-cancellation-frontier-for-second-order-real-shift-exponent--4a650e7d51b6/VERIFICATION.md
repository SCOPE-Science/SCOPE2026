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

# Reproducibility of analytic and exact-rational checks

The proof is the degree-two dual polynomial and feasible signed-atomic construction stated in `RESULT.md`. The file `check_residue_tradeoff.py` checks, using the Python standard library `fractions.Fraction`, both algebraic branches on 2,560 rational parameter triples, including endpoint values and a symmetric exact benchmark. It verifies mass, first moment, second moment, support, signs, dual objective, and the uniform-on-interval dual bound by the parabola's vertex and interval endpoints. The last property follows analytically because \(q(s)=1-2((s-u)/\rho)^2\) is within \([-1,1]\) whenever \(\rho\ge\max\{|u-a|,|u-b|\}\).

Run `python check_residue_tradeoff.py`. Expected output begins `EXACT_RATIONAL_CHECKS_PASS 2560` and ends `special_tv 26`. This experiment is not an exhaustive numerical search over a continuum. The global statement and uniqueness follow from the analytic dual matching and support of its contact points; no solver, floating-point tolerance, formal prover or independent validation is claimed.
