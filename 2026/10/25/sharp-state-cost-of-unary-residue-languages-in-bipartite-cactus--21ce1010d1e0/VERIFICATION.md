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

The proof was checked symbolically for all integers \(p\ge1\) and residues \(0\le r<p\). The lower bound selects an accepted run of length at least the number of states, extracts a shortest repeated-state interval to obtain a simple directed cycle, and applies cycle pumping. In the constrained class the cycle length is both a multiple of \(p\) and even. The matching construction has \(\operatorname{lcm}(p,2)\) states and was checked directly against the accepted-length congruence. The unrestricted lower and upper bounds both equal \(p\); the one-state construction for \(p=1\) uses a self-loop.

The edge cases \(p=1\) and \(\operatorname{lcm}(p,2)=2\) are handled explicitly. No computational enumeration is used as proof. Limitations: the theorem concerns only single-residue unary languages and does not settle state complexity for arbitrary regular languages. Independent audit and independent validation have not been performed.
