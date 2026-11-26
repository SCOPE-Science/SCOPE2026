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

For K complete greedy arches, every K-letter target embeds, but the K terminal letters followed by a letter missing from the rest do not. Greedily scanning any absent target of length K+1 must make at least one match in every arch and exactly K matches overall. Thus absence is equivalent to one match per arch and none in the rest. Recounting transitions: if x=y the terminal letter either is x, or a unique x is inserted in a fully supported word on q−2 symbols; the length-plus-one insertion weight produces G+zG'. If x≠y an arch terminating in y is forbidden, one ending in x contributes zG_(q−1), and all other terminal choices require a y before the first x and no y after it, with full support among the q−3 other symbols across both sides. Inclusion–exclusion gives the displayed H. Summing constant row sums over K and adding the rest avoiding the last target letter yields the claimed rational series, including K=0. In the ternary simplification J=D₃+2E₃ has positive coefficients at degrees 3 and 4; Q(1/3)=−16/243, so the crossing of J=1 lies below 1/3. The nonnegative series is strictly increasing and its consecutive degrees exclude another pole on that circle. The derivative is positive and the numerator nonzero there. Independent bisection and the simple-pole residue give ρ≈0.3087879767626592, growth factor 1.079489353270837 and prefactor 1.692088487255384. Independent enumeration by building the set of all distinct subsequences of each host (without arch factorization) recovered every ternary coefficient through n=8, the q=4 values through n=6, and A₅(5)=6920.

## originality

PASS

Pass for the fixed-ambient q≥3 aggregate first moment and the ternary specialization, not the arch characterization, individual-word enumeration, or a binary law. The closest inspected primary results give structural or extremal statements, and the closest indexed first moment is binary. In particular its transition rules do not count the new case in which the terminal letter differs from both successive target letters. No equivalent or dominating q≥3 result was found in the bounded comparison.

## value

PASS

The shortest absence multiplicity differs from the universality index and is a natural statistic of a random word. The result computes it without enumerating host words, identifies a rational recurrence at each alphabet size, and quantifies the nontrivial exponential growth of the ternary mean. This is useful beyond per-word algorithms and worst-case bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
