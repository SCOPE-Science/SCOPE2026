---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For W_n with b(i)=i+1 mod n, c(0)=c(1)=2 and c(i)=i+1 for i>=2, inverse preimage c^-1 differs from b^-1 only at state 0. On P, a c^-1 step reduces cardinality precisely if 1∈P and 2∉P; otherwise replace by b^-1 without increasing any later inverse set, so a shortest avoiding path can be normalized to exactly k deletions. Each deletion after r cyclic inverse shifts is an occupied→empty cyclic boundary p=r+1 with cost p (p>=1) or n (p=0), new set (P\{p})-p. Exactly one k-set B={0}∪{n-k+1,...,n-1} has only boundary p=0, so it first pays n and then k-1 forced (n-1) steps, giving k(n-1)+1; any other set admits a nonzero boundary in <=n-1 and all later sets omit 0,1 hence total <=k(n-1). The explicit word (cb^(n-2))^(k-1)cb^(n-1) realizes equality. Independently constructed exact BFS reachable image-subset distances for n=3,...,10, ALL k and ALL target subsets; verified unique maximizer and sharp formula. Finite computation corroborates but does not prove every n.

## originality

PASS

Ananichev–Gusev–Volkov introduced this same W_n family and its reset threshold n²−3n+3, but their inspected Theorem 2 and proof do not classify avoidance of arbitrary k-subsets. Ferens–Szykuła–Vorel give general avoiding definitions and bounds, plus other examples, with no W_n appearance in the inspected 14-page primary text. A published Černý-series k-avoiding theorem yields kn on a different automaton, and a related W_n initial image-rank theorem is a different optimization (exists some compressed image rather than avoids a prescribed target). The exact all-k profile and unique worst targets appear best-knowledge novel.

## value

PASS

Avoiding thresholds are a natural exact automata invariant distinct from synchronization/reset length. A complete all-n, all-k sharp formula and uniqueness of hardest target distinguish Wielandt from the Černý series and give an explicit worst-case profile for a standard slow synchronizer. The cyclic boundary mechanism is a structural explanation, not a computation of arbitrary tiny instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
