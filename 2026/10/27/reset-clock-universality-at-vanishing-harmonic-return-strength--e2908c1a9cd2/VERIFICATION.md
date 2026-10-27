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

# Reproduction and limits

Run `python verify_weak_return.py` with Python 3, NumPy, and SciPy. The script reconstructs the killed-Brownian search endpoint density for independent exponential and deterministic clocks, computes return splitting probabilities and mean durations from the OU backward equations, and evaluates exact one-cycle renewal means for four small positive stiffnesses per clock. Five reset-clock choices yield 20 independent mean calculations; 59 deterministic numerical assertion groups passed.

The proof—not finite numerical sampling—establishes the theorem for all independent identically distributed renewal clocks with finite positive mean. The numerical checks do not verify the full quantifier or establish originality. The source equations, stopped-martingale argument, and Brownian hitting-time tail should receive independent assessment before external certification. No independent audit has been performed.
