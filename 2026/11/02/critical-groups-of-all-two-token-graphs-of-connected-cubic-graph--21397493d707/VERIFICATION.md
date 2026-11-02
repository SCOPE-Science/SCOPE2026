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

Install Python 3, NetworkX and SymPy. From the same directory run `python verify.py` and `python verify_alt.py`. Both operate on the literal representative edge lists in `verify.py`, require no network or external data, and use only integer arithmetic. The primary checker enumerates 19,355 labeled cubic graphs on eight vertices, finds 19,320 connected labeled graphs and five connected isomorphism classes; it checks reduced Laplacian Hermite determinants and prime-adic local Smith valuations. The alternative checker constructs token edges by an independent incidence procedure, uses an exact domain Gaussian determinant, and recovers the elementary divisors by successive unit-pivot elimination and division by primes. Both output full numerical factors and explicit success markers.

These finite certificates prove only the five-class order-eight classification; they do not imply a formula for higher graph orders or alternative definitions of token adjacency. Independent scholarly validation has not been performed.
