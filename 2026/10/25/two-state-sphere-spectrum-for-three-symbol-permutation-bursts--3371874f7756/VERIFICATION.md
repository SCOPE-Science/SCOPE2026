---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For q>=2,n>=3, every nonidentity S3 permutation of one nonwrapping triple either swaps one unequal pair at distance <=2 (one uniquely identified changed support), or changes three positions and then necessarily acts on three distinct letters, yielding exactly two three-cycles. This proves B=1+sum(adjacent unequal)+sum(distance-2 unequal)+2sum(triple all distinct), avoiding duplicate outputs across windows. Tracking only equal/unequal final pair gives initial v=(q,q(q-1)), transfer M=[[1,(q-1)t],[t²,t+(q-2)t^4]], final w=(1,t)^T and P=t v M^(n-2)w. For iid uniform letters the score Z_i depends on three letters, is stationary and 2-dependent; conditioning on a shared pair and relabeling symmetry yields mean 1+(q-1)/q+4(q-1)^2(n-2)/q² and variance (q-1)[n(34q²-88q+48)-75q²+208q-128]/q^4. The computed asymptotic variance 2(q-1)(17q²-44q+24)/q^4>0 permits the standard bounded finite-dependence CLT (fixed q). For q>=3 maximal 4n-6 requires all triples distinct, counted by q(q-1)(q-2)^(n-2); for q=2 the explicitly established polynomial characteristic recurrence gives floor((3n-2)/2) with counts 2 (even n), n+3 (odd n). Min=1 exactly q constant words. Independently enumerated 17308 centers in 18 cases, directly generated distinct actual permutation outputs and matched all distribution coefficients, moments, and extrema. Finite test corroborates, not an all-parameter proof.

## originality

PASS

The channel model and binary pointwise sphere expressions are prior material from Chen–Milenkovic 2026 and expressly excluded. A related publicly accessible all-alphabet cyclic 3-cycle burst theorem treats only identity and two 3-cycles and has a distinct 3-state transfer and ball size 2n-3-2H-K; it neither gives nor is equivalent to the full six-permutation B formula. The claimed novel component is the evaluated unrestricted S3 alphabet-wide population law and its moment/CLT/extremal refinements. Targeted Resultary and published literature searches did not identify a dominating distribution formula. Chen–Milenkovic primary full text remained inaccessible after OA/arXiv attempts and authorized institutional access was disconnected, so possible unseen stronger coverage is a genuine residual priority risk. Best-of-knowledge originality PASS, not a priority certification.

## value

PASS

Burst-sphere size variability is a natural channel invariant that controls finite-length packing and average ball volume; tracking the full nonbinary population, rather than one sampled value or binary special case, yields an exact rational transfer structure, fluctuations, and complete sharp extreme populations for every alphabet size and word length. The 2-state compression and unique changed-support partition are nontrivial structural combinatorics, not renaming a known table. No novel code size, practical decoder, or multiburst performance is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
