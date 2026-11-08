---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For binary circular w length n, the full cyclic contiguous-window weight histogram H_w(k,j) has complement-row identity H_w(n-k,M-j)=H_w(k,j), so short rows k<=floor(n/2) plus total weight suffice. Exact exhaustive enumeration of all 2^n words, one minimal dihedral representative per orbit, computes each deck by two independent direct/rolling methods and groups every bracelet. Recomputed n12 224 bracelets/223 decks with one complement collision, n14 687/686 one complement collision, and n15 1224/1220 with four two-element fibers none equivalent by global bit swap, as source six pairs. This proves finite classification n<=15 when full exhaustive code is understood. For each length-15 collision pair u,v of equal weight six, periodic powers satisfy H_{u^m}(k,j)=m H_u(r,j-q*6) for k=15q+r and remain inequivalent as bracelets even after bit exchange, providing all multiples of 15. Finite exhaustion is exact for n<=15; arbitrary multiples follow from repetition identity.

## originality

PASS

Primary circular-string reconstruction paper Ota–Manada uses multiplicities of ORDERED substrings, rather than composition-weight histograms; Acharya et al. classify linear contiguous substring compositions, where boundaries matter, not multiplicity-preserving circular decks. Published Resultary r=2 and two-multispectrum records observe different shorter channels. No direct exact circular full-deck collision table found; original best of knowledge.

## value

PASS

The complete first-intrinsic-failure threshold for a natural noise-free cyclic observation and full n<=15 collision list identifies its finite zero-error reconstruction capacity and an infinite propagation obstruction, beyond a tiny negative sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
