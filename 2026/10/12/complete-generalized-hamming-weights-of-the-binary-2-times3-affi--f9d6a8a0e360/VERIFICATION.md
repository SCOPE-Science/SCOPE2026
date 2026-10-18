---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The ten coefficient-mask evaluations are injective by 1024 distinct 64-bit patterns. Every r-dimensional subspace of F_2^10 has a unique reduced-row-echelon basis; enumeration over all ordered increasing pivot tuples and every allowable nonpivot right-of-pivot entry therefore visits all Gaussian-binomial [10 choose r]_2 subspaces exactly once. The subcode support is the bitwise OR of evaluations of its basis; population-count minimum and number attaining it are exact. Independently compiled a new Gray-code-driven C++ enumerator (distinct from inspected artifacts/verify.cpp) for ALL r=1..10, including 53,743,987 4-spaces and 109,221,651 5-spaces; reproduced all 10 weights and minimizer counts (112,448,64,28,1120,24,1456,2016,64,1). Thus this exhaustive finite certificate legitimately proves all claimed minima; no extrapolation to other codes.

## originality

PASS

Datta–Ghorpade 2015 full text arXiv:1503.02196, Theorems 2.5 and 3.3, gives first three generalized weights and last five (ranks6–10) for these parameters, leaving precisely ranks4,5. Their theorems do not determine those 2 numbers or counts of minimizing subcodes. The closest same-object Yadav arxiv 2609.10274 (2026-09) describes individual codeword weight spectra, not generalized weights of subcodes; abstract read but full PDF not accessible from arXiv or OA and authorized Oxford returned vpn_disconnected. That source is explicit possible hidden-appendix/priority risk. Resultary returned higher-weight spectra for DIFFERENT generator-code families. On available primary comparisons O passes best-of-knowledge with named caveat.

## value

PASS

The previously missing two ranks lie in a published partial higher-weight hierarchy of a natural Grassmann-evaluation code. Completing this exact code hierarchy and providing exact numbers of minimizing r-subcodes determines fundamental higher-support exposure invariants useful for coding/secret-sharing, and is neither an arbitrary derived table nor mere codeword weight spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
