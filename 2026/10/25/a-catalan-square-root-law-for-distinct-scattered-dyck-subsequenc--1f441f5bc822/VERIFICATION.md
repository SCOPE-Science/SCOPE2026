---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Greedy first embedding time of any fixed string is the sum of independent geometric waits, so its probability-of-subsequence-by-length GF is ∏g_{letter}(z)/(1-z). Exactly Catalan_m distinct Dyck strings have m zeros and m ones; linearity of expectation, not independence of pattern indicators, gives [C(tz²/(1−z+tz²))−1]/(1−z). The dominant nonnegative real r solves 3tr²+r−1=0. Positive aperiodic coefficients of u enforce strict modulus inequality elsewhere on |z|=r; its other rational poles lie beyond the disk. The derivative 4r u_prime(r)=3(2−r)/(4(1−r)) gives the asserted unique square-root singularity and transfer coefficient; at p=q=1/2 r=2/3,h=3. An independent Python/SymPy implementation enumerated all 255 source words through n=7 for each of p=1/2 and 1/3, and matched every exact rational expectation coefficient to the derived series. These bounded checks corroborate, not replace, the proof.

## originality

PASS

Best-of-knowledge qualified PASS. Biers-Ariel–Godbole–Kelley Theorem 2.9 gives unrestricted distinct scattered subsequences of random words with exponential 1+√(pq) and no Dyck constraint. Collins likewise treats unrestricted patterns. Mol–Rampersad–Shallit count contiguous Dyck factors in automatic fixed words. Dyck filtering is not implied by the unrestricted total: composition of geometric completion weights with a Catalan language yields a different singularity and explicit n^-3/2 correction. Basic Catalan enumeration and singularity transfer are acknowledged as classical; a published general weighted-context-free-language theorem deriving this as a special case remains possible.

## value

PASS

The Dyck language is a canonical grammar of balanced parentheses; asking how many distinct well-nested strings occur as scattered patterns in a random source is a natural nonregular-language subsequence statistic. The exact all-n expectation and bias-dependent growth constant, including an n^-3/2 suppression and unique fair-source growth optimizer, are reusable quantitative invariants, beyond arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
