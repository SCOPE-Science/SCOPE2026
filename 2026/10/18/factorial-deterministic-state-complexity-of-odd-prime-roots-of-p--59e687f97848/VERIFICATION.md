---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In a complete permutation DFA the word transformations form a subgroup G of S_n since the inverse of each generator is one of its nonnegative powers. For Root_p track g in G by left multiplication and accept if g^p(q_0) is final. For the witness the n-cycle and adjacent transposition generate S_n; with initial and sole final state 0 the input states are reachable and separated by permutations sending just one of a distinct pair to 0. In the root let B be the permutations with 0-cycle of size 1 or p. For h nonidentity fixing 0, choose a moved point a and b=h(a), and take a p-cycle g starting 0,a and ending b; p-3 filler points exist even at n=p. Then gh has 0-cycle of size 2, so g is in B and gh is not. If h moves 0 and is outside B take g=e; if h moves 0 and is in B take g=(h(0) h^{-1}(0)), which fixes 0 and makes gh have 0-cycle of size 2. Oddness excludes both failures from B. For any distinct u,v, h=u^{-1}v and the continuation realizing gu^{-1} sends them to g and gh, so every reachable state in S_n is separated. Unary minimal input has a single n-cycle and at most n group states. This covers n=p=3 and the full stated range, not composite exponents or primes above n. Frozen prime_root_checker.py was inspected, not executed; frozen checks.txt reports 137,778 stabilizer tests and exact finite minimizations through n=6. The symbolic proof, not those recorded results, establishes the unbounded finding.

## originality

PASS

The transformation-monoid root construction and unrestricted root complexity work are established. No compared result covers the sharp odd-prime bound with a binary minimal permutation input or mechanically supplies the needed separations of the group states. The credited novelty is the permutation-restricted sharp lower bound and the exact alphabet threshold, not the root construction itself.

## value

PASS

Permutation automata are a natural reversible subclass, and tight membership-state complexity sharply tests whether the reachable group-state construction collapses under minimization. The two-letter witness uses standard generators but requires separation of every pair of permutations. The trivial right-stabilizer criterion and the concrete p-cycle/2-cycle construction explain both the factorial blowup and why unary input cannot attain it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
