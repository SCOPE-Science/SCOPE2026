---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The letter counts require at least pn of each symbol, and with exactly those counts the opposite terminal-letter requirements are incompatible. At length 2pn+1 a supersequence with pn+1 zeros ends in zero; removing it leaves a balanced word ending in one that must have an opposite symbol between occurrences kp and kp+1 of each letter for 1<=k<n. These conditions also suffice, because each heavy-letter group then has its own separator. The immediate successor of every such boundary is a distinct forced position and cannot be the last position, since another occurrence of the boundary letter follows it. Deleting these positions leaves h copies of each letter and a final one. In greedy expansion, each boundary forces exactly one opposite symbol, including cascades. If fewer than n-1 events fire for at least one letter, let m be the smaller event count: that letter has at least h+m occurrences, reaching p(m+1) and contradicting the missing next event. Before the final base symbol the same argument works with h-1+m, since (p-1)(n-m-1)-1>=0 for p>=2 and m<=n-2. Thus the expansion terminates with the required counts and final one and inverts deletion. Complementation makes the two terminal-letter classes disjoint and equal, giving 2*binom(2h-1,h)=binom(2h,h), demonstrating length attainment and giving LCS length 2n-1. The counts are distinct words, not embeddings, and do not extend to arbitrary longer deletion-minimal outputs. The supplied script was inspected, not rerun; verification_output.txt records 84 DP parameter pairs, 14706 bridge checks and 5960 short-word tests, which are finite corroboration.

## originality

PASS

The supported distinct claim is the closed form and explicit balanced-word bijection for the specified complemented periodic inputs with p,n>=2. The general binomial bound and even equality with exactly the same input lengths and nonzero LCS length are already known for other pairs. Neither that numerical extremality nor its existence is credited as new.

## value

PASS

The useful new structure is a nontrivial periodic extremal family in which the letters interact throughout the inputs; it is not obtained by adding a common terminal word to the trivial complementary constant pair. The all-parameter bijection gives explicit factorizable choices for every shortest output and explains why interspersed matching requirements need not reduce the extremal count. This is a natural supplement to the general bound even though existence of nonempty-LCS extremizers was already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
