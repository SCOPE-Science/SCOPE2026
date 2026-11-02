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

# Reproduction and limits
Run `python3 verify.py` using Python 3.10 or later with no third-party dependencies. The deterministic output is stored in `verification_output.txt`.

The checker constructs the actual binary honeycomb cross-adjacency matrix and recomputes binary ranks after independently toggling each removed bond. It exhausts all \(297\) disjoint two-bond pairs at \(L=3\) and all \(10{,}437\) pairs at \(L=7\); it further checks deterministic selected pairs at \(L=15,31\), single faults at four sizes, and quotient monomial-character separation up to \(L=63\). These are **finite checks only**; the proof for arbitrarily large \(k\) is the finite-field argument in `RESULT.md`, including the polynomial root-count contradiction when \(3\mid L\). The graph-state cut-rank identity is credited to [1]. Independent scientific validation has not been performed.
