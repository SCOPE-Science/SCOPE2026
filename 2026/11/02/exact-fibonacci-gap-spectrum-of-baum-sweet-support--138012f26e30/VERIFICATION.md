---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. Positive Baum–Sweet positions are exactly canonical binary words in the unambiguous language 1(1|00)*; fixed length m accepted words are F_m, yielding |S_M|=F_(M+2) including zero. Every lexicographically adjacent same-length accepted pair has a unique first differing bit after an accepted prefix p, with the maximal p0 successor and minimal p1 successor producing difference d_r=2^(r-1)+[2 if r odd else 1]; their multiplicity at length m is F_(m-r-1). r=1,2 both yield gap three, with 3<=r<=M-2 producing the remaining infinite gaps. Cross-length accepted-word extremes supply floor((M-1)/2) gaps one and floor(M/2) gaps two, plus (0,1) initial gap one. Summing Fibonacci tails proves complete H_M counts and telescoping length 2^M-1. Binet limits give mass φ^-1 at gap three and φ^-(r+1) at d_r, summing to one; tail exponent log₂φ and infinite mean follow from 2^r gap growth. Both M=2 and absent r ranges are covered; no arbitrary-truncation claim.

## originality

PASS

PASS, qualified. OEIS A060142 and the foundational Baum–Sweet work establish exactly the same support and recurrence. Merta 2018 studies indices of ones of Baum–Sweet and Fibonacci-word/parity structure, while its Theorem 4.6 explicit gap differences pertain to a different sequence: positions of ones in a composition inverse, not the original support. The independently derived dyadic frequency histogram and limiting heavy-tailed law were not found as an implication in the inspected primary results; the original 1976 full text was not inspected, and equivalent automatic-word return-gap literature could exist.

## value

PASS

PASS. The location of ones in a canonical automatic sequence is intrinsically meaningful, and the theorem classifies every gap size and exact Fibonacci multiplicity under all dyadic cutoffs rather than tabulating a few samples. Its nontrivial infinite-mean power-law limiting gap distribution is a useful return-time invariant distinct from the known automatic support recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
