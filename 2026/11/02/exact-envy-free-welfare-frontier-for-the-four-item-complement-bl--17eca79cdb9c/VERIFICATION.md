---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The proof identifies complete blocks and derives sharp integer bounds on their number under each fairness criterion. Both extremal constructions specify the destination of every physical good, including otherwise zero-value primed goods. Their envy constraints are verified for all directed agent pairs. The EF-\(\ell\) proof uses only disjointness of complement pairs to bound the effect of \(\ell\) deletions.

A second implementation, `verify_spoc_frontier.cpp`, independently enumerated \(1,722,355\) complete allocations and evaluated each agent's value on every other bundle. It tested EF, explicit removal of **every** individual good for EFX, and all feasible deletions for EF-\(\ell\) using the disjoint-pair count identity for \(\ell=1,2,3\). It matched the displayed optima on ten parameter combinations: \(n=2\), \(t=1,2,3,4,5\); \(n=3\), \(t=1,2,3\); \(n=4\), \(t=1,2\).

Replay from the embedded C++ source using `c++ -std=c++17 -O2 verify_spoc_frontier.cpp -o verifier && ./verifier`. The last line must report `VERIFY_OK complete_allocations=1722355`. These checks do not constitute a general proof; the universal proof is contained in RESULT.md. No independent scientific audit has been performed.
