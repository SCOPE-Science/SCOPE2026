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

The proof in `RESULT.md` is deductive and has two external mathematical inputs: Li's exact complex ranks for the double and triple direct sums, and Lovitz's explicit rational decompositions for the single copy. Those inputs were checked in the primary arXiv full texts.

The characteristic-zero transfer was checked at the level of quantifiers: a decomposition has finitely many coordinates, so it is defined over a finitely generated subfield of the ambient characteristic-zero field; such a field embeds into \(\mathbb C\), preserving every polynomial tensor-decomposition equation.

The positive-characteristic transfer was checked by writing rank-at-most conditions as finite polynomial systems. The argument uses only the standard implication that a finite rational polynomial system with no complex zero has a rational Nullstellensatz certificate after scalar descent; clearing denominators loses finitely many primes. The same finite exclusion also protects the rational upper decompositions.

`transfer_check.py` checks the numerical rank pairs, gaps, and the finite sizes of the forbidden decomposition systems for dimensions \(54\) and \(81\). It does not recompute the source lower bounds and does not construct the unspecified Nullstellensatz certificates.

Expected final verifier line: `CHECK_OK`.
