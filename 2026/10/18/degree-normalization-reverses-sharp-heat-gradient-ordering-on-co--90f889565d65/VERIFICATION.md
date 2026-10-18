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

# Reproducibility and limits

The proof derives the exact coefficient from the two-state block-mass chain and the two within-part fluctuation eigenspaces, then uses the fixed sign pattern of adjacent transition-row differences. The partition comparison is an application of strictly convex integral functions for the combinatorial generator, and a reciprocal-part-size identity for the unit-exit-rate generator. The intermediate-exponent crossover is proved by strict convexity of negative powers and comparison of dominant exponential decay rates; the small-exponent crossing branch is established by the analytic implicit-function theorem.

Execute `python3 verify.py` in the same directory as this document. The verifier has no external dependencies beyond Python 3's standard library. It forms the finite-state generator via its Poissonized embedded transition chain, evolves the two signed initial point masses, sums absolute heat-row differences, and compares them to the proposed formula. It also checks finite samples of the ordering, short-time derivative, and dominant decay exponents. The completed run returned `PASS 4880 independent finite numerical/analytic-identity assertions`.

Finite numerical assertions verify only those selected parameter cases. They do not certify the universal theorem, global novelty, or any independent audit. The analytical proof in `RESULT.md` is the source of the infinite-family conclusions.
