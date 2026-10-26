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

# Mathematical verification

All enumerations use exact arithmetic in the finite field with three elements, and the package includes all finite coefficient identifiers. Run `python verify_pencils.py`, `python verify_rref.py`, `python verify_profiles.py`, and `python verify_inert_graph.py` after installing SymPy. The first enumerates all projective pairs of squarefree binary quintics, takes unique four-member spans, constructs the full source-coordinate group of order 24, and compares all 54 orbit representatives against `orbit_representatives.csv`. The second independently enumerates all 11011 row-reduced two-planes and uses SymPy polynomial gcd to compare complete pencil identifiers against `pencils.txt`. The additional profile checker validates all 15 Frobenius factorization types and the two size-24 irreducible-divisor orbits. The independent graph checker computes the irreducible degree-five forms and their 192 compatible pairs and checks `inert_compatibility.json`. Each program was replayed successfully using these actual package files.

The profile table `fiber_profiles.csv` was calculated by exact modular factorization of each verified projective fibre and compared with the orbit data. All fibre partitions have total degree five, and their 15 frequencies sum to 1098. These finite verifications do not constitute a uniform theorem over arbitrary finite fields; no independent external audit has been performed.
