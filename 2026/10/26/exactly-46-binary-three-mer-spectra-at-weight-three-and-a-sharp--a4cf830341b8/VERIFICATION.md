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

Every weight-three word has a unique gap quadruple (a,b,c,d), total N=n-3; all 7 nonzero-containing trigram counts depend only on truncated gaps in {0,1,2}^4, and the eighth 000 count is determined by n-2 minus their sum. Independently reconstructed all 81 state fingerprints, yielding 59 classes, 46 persistent with at least one extensible gap and 13 transient; checked reported first-appearance counts. For a signature with r entries equal to 2 and minimum sum m, stars-and-bars gives binom(N-m+r-1,r-1), or indicator N=m if r=0. The deepest signature (2,2,2,2) has one fingerprint and binom(N-5,3)=binom(n-8,3) preimages. Every rival has at most three extensible gaps, so for N>=15 rival fibers have degree ≤2; independently computed 45 cubic differences at N=15 with min successive forward differences (10,23,8,1), all strictly positive, giving unique dominance at n>=18 by Newton formula; N=14 rival 90 vs 84. Direct trigram enumeration for 2401 gap quadruples and all 81 signatures matched the formula, and the ratio binom(n-8,3)/binom(n,3) tends to one analytically. Finite exhaustive signature enumeration is mathematically exhaustive because the 3^4 reduction was proven, not because of bounded word sampling.

## originality

PASS

Qualified PASS: Karhumäki–Puzynina–Rao–Whiteland arXiv:1605.03319 proves general k-abelian class cardinality via BEST/Eulerian approach, but standard 3-abelian equivalence also fixes prefixes/suffixes and shorter factors, a STRICTLY richer observation than raw trigram counts alone. Cassaigne–Karhumäki–Puzynina–Whiteland DLT 2016 original full text establishes regular representative languages and rationality for the richer equivalence, not this fixed-Hamming-three count 46 or sharp maximal coarser fiber. Pevzner–Tang–Waterman 2001 is general DNA-read Eulerian assembly. Prior 2017 extended journal version was not materially read and remains a bounded historical risk.

## value

PASS

Trigram count spectra form a natural restricted string-assembly observation channel. An exact all-length profile census, sharp stabilization at 46, largest ambiguity fiber and almost-sure information collapse for three markers are motivated finite-combinatorial reconstruction facts, neither a generic k-abelian count nor an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
