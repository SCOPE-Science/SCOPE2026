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

# Verification record

The all-parameter proof has two independent mathematical halves: a conditional-negative-definiteness lower bound and a constructive orbit-averaged nonnegative cut-metric upper bound. The quantitative constants are checked symbolically by counting all intersecting and disjoint unordered pairs of two-subsets and their crossings with the edge set of a Hamiltonian cycle.

The executable `verify_kneser.py` uses Python 3 standard-library modules only. Reproduction: extract the file beside this record and run `python3 verify_kneser.py`. The replay returned `CHECK_OK 8462 exact finite assertions; n=5..11; permutation orbit n=5..7`. Its checks include independently reconstructed shortest-path graph distances and full permutation averages for small orders. Every numerical equality used by the proof is rational and checked by `fractions.Fraction`; the code does not use floating point for certificates.

Finite checks cover only finitely many graph sizes and therefore are not a replacement for the all-\(n\) proof in RESULT.md. No proof is given for higher-rank Kneser graphs, weighted edges, uniqueness, or minimum embedding dimension. Independent audit has not been performed.
