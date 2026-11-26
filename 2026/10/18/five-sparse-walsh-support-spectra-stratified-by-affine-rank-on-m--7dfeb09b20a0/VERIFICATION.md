---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two canonical affine supports are exhaustive: rank four gives a simplex, and in the affine three-plane the complementary triple is always affinely independent. Ambient translation multiplies by a nonvanishing character and restriction to the rank-r span repeats local support counts by 2^(d−r). The row-span criterion covers every complex vector: a coordinate in the span forces a zero coefficient, and otherwise a finite union of proper hyperplanes cannot force any additional zero on the annihilator. All augmented rank tests can be reduced to matrices of original Walsh rows and coordinate rows, whose nonzero minors have absolute value below 101. An independent exact rational replay recovered 95 and 537 proper generated spans and the respective eligible histograms (8,32,24,8,1) and (80,160,80,16,1). Replay: python3 /workspace/branches/0522a46b-b045-4c3d-8231-d74a2679d256/independent_walsh_check.py. There is also a direct bound: rank three has Walsh form A(s,t)+d u with d≠0, so each sign pair (s,t) permits at most one zero in u. In rank four project complex coefficients generically to real coefficients without sending any of the five nonzero coefficients to zero, and absorb the four nonconstant signs into the variables. The zeros are contained in a positive-weight subset-sum family on four elements at a noncentral target (the constant is nonzero). This is an antichain: if it contains a singleton or triple it has size at most four by the three-element antichain bound and complementation, and if it has only pairs, five equal-sum edges would force all weights equal and yield the forbidden central target. Empty or full subsets can occur only alone. Thus rank four has at most four zeros as claimed. The exhaustive rational replay gives every count and the frozen script has explicit witnesses. Frozen checker inspected, not run. Its advertised Python 3.8 minimum is a documentation issue: int.bit_count requires Python 3.10 or later as written; this does not affect the exact mathematical classification or independent replay.

## originality

PASS

The two affine types and the size-nine gap in dimension four are already covered and receive no novelty credit. The strongest checked exact source proves that gap by classifying seven prescribed zeros but does not settle the complete local spectra by rank, fixed-support attainability, or the size-eleven gap. The earlier numerical uncertainty diagram is a global union, not an exact proof by affine rank. The distinct contribution supported here is the full rigorous rank-stratified spectrum.

## value

PASS

The motivating uncertainty question is what the geometry of a small time support buys beyond its cardinality. Affine rank distinguishes the two actual support shapes and changes the sharp spectral minimum by a factor of 3/2 in fixed ambient dimension. The full list and fixed-support realizability decide all five-sparse possibilities uniformly in d; this is stronger and more reusable than counting one arbitrarily selected Fourier-zero configuration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
