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

# Reproducibility

Run `python3 verify.py` with an ordinary Python 3 interpreter. The checker uses only the standard library and prints `VERIFY_OK` if all assertions hold.

The checker exhaustively enumerates all perfect matchings of the four-cube by least-unmatched-vertex recursion, separately computes the \(8\)-by-\(8\) bipartite permanent via subset dynamic programming, evaluates forcing subsets against the entire matching universe, computes optimal anti-forcing deletions through a directed feedback-arc recurrence, enumerates all \(384\) hypercube automorphisms, and verifies each orbit representative by checking all \(40320\) possible directed-vertex orderings. The smaller-dimensional spectra are enumerated directly.

Finite exhaustion proves only the dimensions and graph families explicitly enumerated. Independent external validation has not been performed. The relevant published maximum anti-forcing theorem already proves the extremal value and the four coordinate extremizers; the new census does not replace or independently establish a claim of literature novelty.
