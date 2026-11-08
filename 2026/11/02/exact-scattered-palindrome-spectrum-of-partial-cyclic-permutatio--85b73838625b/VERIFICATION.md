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

The actual cyclic-word RESULT.md supplies an all-size greedy subsequence proof: earliest symbol v1 occurs at index v1; each successive letter change advances by least strictly positive cyclic distance. Reflected transitions of palindrome cost q for unequal symbols and 2q for equal, plus a central q for even lengths. Thus greedy terminal index is v1+q(m+e(h)); containment iff m+e<k or cost=k and v1<s. Counting half-words by equal-adjacency locations gives both binomial spectra. Formal power-series summation yields F_{q,s}=q u z(1+uz)/((1-z)(1-u²z(q-1+z)))+s u²z(1+u(q-1+z))/(1-u²z(q-1+z)), with maximal lengths 2k-1 if s=0 and 2k+1 if s>0. Independently enumerated literal index subsequences of W_(3,2,1), grouped distinct palindromic targets by length {1:3,2:3,3:7,4:2,5:4}, exactly matching formula. Finite test only corroborates infinite proof.

## originality

PASS

Best-knowledge PASS: full length-by-length spectrum for nonbinary cyclic-permutation powers and incomplete final prefix, not generic scattered-palindrome bounds or the known binary alternating case.

## value

PASS

Powers of the alphabet permutation are a canonical highly structured word family; the exact distinct scattered-palindrome spectrum is a motivated fine complexity statistic. The membership test, all k,q,s binomial profile and rational generating function solve the entire nonbinary family rather than one arbitrary finite slice; the uniform per-added-prefix-symbol correction gives an exact benchmark for word-combinatoric comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
