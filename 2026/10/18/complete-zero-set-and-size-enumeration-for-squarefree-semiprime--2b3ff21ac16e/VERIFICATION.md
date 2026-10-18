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

# Verification and reproducibility

The theorem follows from five mathematical steps: Fourier idempotents correspond bijectively to zero-one frequency masks; the three Galois time strata reduce to prime-root cancellation; the rational primitive cyclotomic kernel consists of additive CRT matrices; additive zero-one matrices must be coordinate cylinders; and uniform CRT row and column sums cannot coexist on a nontrivial mask when the dimensions are coprime. Counting uniform columns and uniform rows gives the seven claimed generating polynomials.

Run `python3 checker.py` alongside this document. The program is standalone and uses integer arithmetic only. For each mask it tests Fourier vanishing at representatives of the three time strata using divisibility by the exact cyclotomic polynomial, not numerical near-zero thresholds. It exhaustively checks all masks for prime pairs (2,3), (2,5), (2,7), (3,5) and independently compares the exact size-by-class enumeration with the formulas. Its expected final output is `CHECK_PASS`.

Limits: Exhaustive finite checks do not prove the theorem for larger primes. The mathematical argument requires two distinct primes and zero-one Fourier multipliers. The reviewed claim makes no assertion of independent validation or originality certification by a third party.
