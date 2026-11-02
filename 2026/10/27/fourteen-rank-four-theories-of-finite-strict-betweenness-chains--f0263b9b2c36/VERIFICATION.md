---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

In the language of equality and STRICT B(a,b,c) only, the complete T_0 atomic diagram records equality and all oriented triples. Recursing T_(r+1)=(T_0,{T_r with each possible one-point extension}) exactly characterizes formulas of quantifier rank <=r, because first-order quantification observes existence not multiplicity. Independent reimplementation exhaustively enumerated all tuples of n=1..15, including repeats, and reproduced class counts [1,2,6,14] for ranks 1..4: at rank 4 types of 1..14 are distinct and types 14 and 15 agree. This finite range is not extrapolated: for all n>=15 the standard four-round EF interval-splitting strategy for pure linear orders (threshold 2^4-1=15) gives equivalence, and quantifier-free reduct to B preserves rank equivalence. Transitivity covers n>=14, so min(n,14) exactly classifies all n>=1. The independent finite checker cached 211372 complete assignment states. It says nothing about higher ranks, counting extensions, constants, or arbitrary betweenness structures.

## originality

PASS

Pure linear-order rank-four equivalence at threshold fifteen is classical, but forgetting orientation can merge the additional B14/B15 boundary; that strict-reduct equality is not a formal consequence of order equivalence at the size fourteen. Courcelle 2021 defines the same strict betweenness relation and axiomatizes it for tree orders, rather than computing finite-chain rank-four types. Resultary searches and adjacent one-red ordered-chain and directed-successor findings use different languages, so neither supplies the exact fourteen class count. Siders 2010 order equivalence full text and a 2009 thesis remain uninspected priority risks; qualified PASS.

## value

PASS

Bounded quantifier-rank spectra and minimal representatives are natural finite-model-theory invariants. The exact fourteen-class rank-four result, optimal small-model representative, and one-point savings relative to oriented orders isolate the logical effect of forgetting orientation; the global EF argument makes it a complete theorem, not an arbitrary enumeration of finite n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
