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

Independently enumerated all 9840 ternary words of lengths1..8 against both orientations of the seven literal patterns {00,11,22,20,212,0101,121012}; exact T_n sets and first emptiness at T_8 established, so longer both-direction permitted factors impossible by subfactor inheritance. Verified all T_1..T_7 words and reverses occur in h^7(0) of length65; standard prefix inclusion holds since h(0) starts 0. Inspected Currie et al Theorem14 avoiding a superset of F and Theorem1 rho(n)=2n+1. Pair-count formula r(n)=rho(n)−nonpalindromic_reflected(n)/2 yields all counts. Finite exhaustive obstruction plus published infinite avoidance/complexity theorems, not finite prefix extrapolation, establish the all-length result.

## originality

PASS

Best of knowledge after current primary-source reading and searches: Theorem6 already gives sharp palindrome length7, a covered subclaim explicitly acknowledged. Theorem14 forbids ten patterns; deriving T8 emptiness and exact T1..T7 includes fresh exhaustive combinatorial work.

## value

PASS

Reflection complexity is a natural recently studied factor invariant. Exact all-length spectrum, complete short reflected-word list, and sharp absence threshold turn the qualitative eventual-separation theorem into a concrete classification of a canonical ternary morphic word; not merely restating known palindrome counts. Worthwhile exact object-specific boundary despite finite forbidden-pattern certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
