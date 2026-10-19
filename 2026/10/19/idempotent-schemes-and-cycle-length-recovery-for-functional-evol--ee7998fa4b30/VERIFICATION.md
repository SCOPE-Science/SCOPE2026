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
# Verification

The standalone Python 3 file `verify.py` was run from the delivered package source with direct elementwise multiplication in explicit finite fields, not by fitting the claimed formula. It exhaustively tested all endofunctions on one through four vertices over the prime fields of order 2 and 3 (288 graph-field instances each), and one through three vertices over fields of orders 4, 8, 5, and 9 (32 instances each), a total of 704 exhaustive graph-field instances. Thirty-two additional five-vertex functions over the field of order 4 were sampled with a fixed pseudorandom seed. All finite instances matched the count formula and reconstructed their exact cycle multisets. The nonreconstruction witness was checked via its two different image-set cardinalities (1 and 2). Forty squarefreeness comparisons in prime characteristics 2, 3, 5, 7, and 11 for cycle lengths one through eight passed using polynomial gcd when SymPy was present.

Exact successful output includes `VERIFY_OK_FUNCTIONAL_EVOLUTION_IDEMPOTENTS`. Tests of low dimensions and finitely many fields do not prove any general statement; full field/dimension generality is supplied by the algebraic and Möbius inversion arguments in `RESULT.md`. The underlying idempotent schemes and claims have not undergone independent mathematical audit.
