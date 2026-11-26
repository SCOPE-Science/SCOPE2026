---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the ternary relational signature without constants or functions, Duplicator's available replies to the second move are exactly the atomic diagrams in the first choice's extension set; matching sets of those profiles is necessary and sufficient. For a transient first element the transient extension diagrams are equality, doubling, halving, and generic, with the generic always available for m>=5. Mixed diagrams are determined by residue, parity and the low/high doubling test. For tail first elements the diagrams depend on their residue and on which residues occur in the two transient intervals. Both intervals have at least L=lcm(p,2) consecutive exponents at m>=2L+1, realizing every required parameter. The rank-two sentence forces a nonidempotent x fixing the unique idempotent, hence transient and divisible by p; it is a square only if its exponent is even, and its own square is nonidempotent exactly when 2x<m under those constraints. Its least candidate is L, proving separation for every subthreshold index, including m=1. The independent multiplication-table check passed for periods 1–14 (378 formula cases, 56 counted profile comparisons plus the boundary check); the universal conclusion rests on the interval argument.

## originality

PASS

The profile criterion and monogenic index-period decomposition are established tools. The closest inspected results do not yield the exact fixed-period threshold or its parity split in the unnamed multiplication-graph language. This is a bounded best-of-knowledge judgment.

## value

PASS

This is an exact logical cutoff for a basic algebraic family, with one separator for every smaller index. Fixed period leaves an unbounded size parameter; detecting the parity-driven change through two rounds exposes an interaction of modular absorption and transient squaring rather than only cataloguing small semigroups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
