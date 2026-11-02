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

Necessity: if both cliques begin with two white vertices, no blue vertex can force, so a one-leak set requires a full or nearly-full layer. For n>=4 and layer A missing i, the available initial A forcers are precisely a_j at selected B indices j!=i; one leak can suppress all if <=1 such j, and B cannot initiate while there are >=2 white B. With >=2 such indices a non-leaked A forcer completes A; thereafter cross-layer forces all B except perhaps one, completed within B. Full layer is always forcing even with one A leak. n=3 gives additional precisely 9 two-and-two configurations. Counting disjoint full-layer configurations and the two near-full orientations, with the both-near-full overlap n^2 counted once, gives exactly L_n=2z^n(1+z)^n-z^(2n)+2n*C(n-1,2)z^(n+1)+2n*sum_{t=3}^{n-2}C(n,t)z^(n-1+t)+n^2 z^(2n-2) for n>=4; L3=2z^3+15z^4+6z^5+z^6. Minimal sets are exactly two full layers and 2n*C(n-1,2) near-full plus two sets for n>=4, or two layers plus nine 4-sets for n=3. Independently exhaustive bit-mask sequential-forcing closure with every leak and all subsets for n=3,4,5,6 matched both polynomials and inclusion-minimal histograms. This is finite corroboration; case argument proves all n.

## originality

PASS

Leaky forcing, resilience, and generic all-set polynomials predate this record. The surviving contribution is the explicit all-cardinality complete-prism one-leak polynomial together with exact labeled minimal-set classification, not generic algebraic compression or the already known minimum forcing number.

## value

PASS

A full forcing polynomial, entire family classification and inclusion-minimal census for complete prisms is a natural graph reliability/infection invariant that cannot be recovered from the forcing number alone. The n=3 exceptional layer pair and n>=4 exact nonminimum minimal-set coefficients are useful combinatorial structure, not arbitrary small samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
