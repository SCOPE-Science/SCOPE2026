---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Every weight-three cross-bifix-free codeword must be primitive: proper period produces a nontrivial border. Distinct codewords cannot be distinct rotations (one rotation yields a cross prefix/suffix overlap). The number of primitive weight-three necklaces is [binom(n,3)-1_(3|n)*n/3]/n = floor((n-1)(n-2)/6). Proposed C_n has ones at 0,a,b with 1<=a<=floor(n/3)=k and a<b<=n-k-1. All proper suffixes either start at 0 (cannot if proper), start at b and contain one 1 while comparable prefixes contain >=2, or start at a and contain two 1s while comparable prefixes contain three; suffixes starting at zeros cannot match prefixes starting at one. Its cardinality sums to exact upper bound for n mod 3=0,1,2. Every primitive cyclic gap triple has at least one short and one long gap and a unique long-to-short transition (the gap sequence has length 3), selecting exactly the canonical C_n representative. Independent direct generation checked cardinality/nonoverlap/necklace-one-representative for each n=4..34, including n divisible by 3; infinity follows from the gap proof.

## originality

PASS

Targeted Resultary semantic searches and primary literature comparisons, with specific mathematical implication checks and residual priority risks, support qualified best-of-knowledge originality of the final scoped claim.

## value

PASS

A fixed-weight 3, all-blocklength exact optimal constant-composition cross-bifix-free code with a canonical primitive-necklace transversal is a natural complete construction/theorem, useful for synchronization codes. Unlike a generic primitive-necklace upper bound, it proves simultaneous attainability with a simple explicit family for every length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
