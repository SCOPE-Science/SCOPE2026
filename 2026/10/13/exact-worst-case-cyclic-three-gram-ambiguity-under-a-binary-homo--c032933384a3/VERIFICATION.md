---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For the cyclic binary constraint prohibiting triple 000 and111, allowed order-two de Bruijn graph has six arcs 001,010,011,100,101,110. Flow balance forces profile (a,s-b,b,a,s-a,b), s>=1, 0<=a,b<=s, n=2s+a+b. Mark an occurrence of vertex 01 (exactly s such indices), traverse s outward 01-to-10 and return 10-to-01 excursions, with independent binary detour choices in exactly b outward and a return legs. There are C(s,a)C(s,b) marked walks; double-counting (word,index) gives n/s times this product, no disconnected Euler-support exception. At fixed s, log-concavity balances a,b; feasible s range ceil(n/4)..floor(n/2), so stated finite max holds for every n>=2. Independent direct complete profile enumeration of 5,774 valid indexed cyclic words n=2..16 agrees. At n=2 the two alternating words correctly form a fiber of size 2.

## originality

PASS

The general restricted de Bruijn Euler-circuit/flow formula and cyclic Markov class notions are prior mathematics. A complete six-edge homopolymer-forbidden excursion reduction gives exact n/s binomial fiber multiplicity and optimized worst-case cyclic length-three list for every n; those are not supplied as a closed all-length theorem by inspected general flow papers.

## value

PASS

Worst-case cyclic three-gram multiplicity ambiguity under the most natural binary homopolymer length-three exclusion is an intrinsic reconstruction list invariant. The exact finite 1D maximization over s is complete and computationally effective for each length; it need not supply closed elementary argmax to have value. No claim of noise correction or asymptotic not proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
