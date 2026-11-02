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

Finite affine-shift lemma is rigorous: if m initial shifted equalities k_(N+i)=k_i+i+N/2 hold, subtracting the same linear shift from k_(n+N) produces a second solution of the deterministic tropical recurrence, so equality propagates to all n. c_n=2Nk_n-n² is N-periodic, and any period d makes successive integer differences d/N integral, hence N|d. An independently implemented C integer recurrence enumerated every eligible triple and checked ALL m checkpoint identities, not just a sampling of n. Independent generated output had 11052 entries (10977 outside prior (1,2) family), sum N=84412414, maximum N=36556 at (13,26,41); SHA256 of the actual checkpoint data exactly d95345c93044969f924f10fe37245a3424b72994f639951da7ff37365777058c, matching source expected certificate. All-index result rests on the lemma plus exhaustive finite parameter certificate.

## originality

PASS

Can 2026 full primary manuscript explicitly labels all-parameter quadratic-periodic statement Conjecture 1 and proves Theorem 3 only for p=1,q=2; the present exact exhaustive certification covers 10977 additional triples, with all n proved via induction and minimality of N. General R-systems degree-growth estimates (Galashin-Pylyavskyy) do not entail this exact correction period for every bounded-order triple. Romanov 2021 study 2021 original ten-page Russian paper was located and inspected in full: its theorem explicitly evaluates two three-term parameter examples (k=8, i=(1,3,4)) and (k=9, i=(2,3,4)), with quadratic coefficients and respective periodic scales 38 and 31 plus a parity term (combined scale 62). Those are important prior special cases, not a theorem over all 11052 triples; the present statement uses a max-tropical normalization rather than Romanov 2021 study min-exponent normalization, so identity of the individual sequences without translating conventions is not asserted. Priority credit is confined to the all-parameter bounded-order certificate beyond those known special instances.

## value

PASS

A finite but mathematically motivated exhaustive frontier (all primitive three-term recurrences of order <=80) resolves 11052 distinct infinite-time cases of a live conjecture, including 10977 beyond the known analytic family. The key finite affine-shift lemma turns an exact large certificate into true all-index proofs, and least-period determination is a natural additional invariant. This is neither a finite-time heuristic nor an arbitrary unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
