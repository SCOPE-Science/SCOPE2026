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

# Reproducible verification and boundaries

Run `python3 verifier.py` with Python 3 (standard library only). The supplied `verifier_output.txt` is the actual successful output, ending `VERIFY_OK`.

The script constructs the branch incidence graph for odd \(n=3,5,7,9,11,13,15\). It checks the vertex/edge counts, the seven fixed vertices and six fixed edges, builds a stable spanning tree from that fixed tree, and verifies that the remaining \(2n^2-2\) fundamental cycles form \(n^2-1\) exchanged pairs. This is an exhaustive graph check for each listed degree; the argument for arbitrary odd degree is in `RESULT.md`.

It enumerates all \(q^2+q+1\) projective points over ten prime fields, with \(n=5,7,9,11,13\) and both \(q\equiv1\) and \(q\equiv-1\pmod n\). For those ten instances direct counts agree with the two point-count formulas. It also performs an independent formal logarithmic-derivative check of the zeta expressions through extension degree eight. This is finite experimental corroboration, not an exhaustive enumeration over all parameters.

Local normalization and truncated-logarithm arguments are given in `RESULT.md`. The characteristic hypothesis \(p>n\) is essential to this argument. The group-scheme claim requires the proof of the integral Frobenius cycle lattice, not merely its characteristic polynomial. No outside scientific audit or machine-checked infinite formalization has been performed.
