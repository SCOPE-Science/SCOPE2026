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

# Reproducibility

Run `python3 verify.py` using Python 3 and the standard library. It enumerates every edge configuration in the three-state ring model for \(3\le n\le8\), counts kernels using the exact independence/outgoing-domination conditions, and aggregates probabilities using `fractions.Fraction` at five reciprocal-edge probabilities.

The executed script reported `VERIFY_OK 9828 graphs, 60 exact rational expectation/nonexistence equalities; gadget flips 3/3` with no assertion failures. It also checks the complete no-kernel classification and exact unique-kernel classification of noncoherent one-way rings across these finite sizes. Each of the three possible ninth-edge boundary states of an eight-edge doubling gadget was checked explicitly.

The all-\(n\) conclusions require the structural kernel proof, formal-power-series enumeration, Perron-root calculation and binomial concentration proof in `RESULT.md`. Finite tests alone cannot establish them. No outside scientific audit or validation is claimed.
