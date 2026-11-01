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

# Reproduction and scope

Run `python3 verify.py` using a standard Python 3 installation without additional packages. The checker recomputes parallel firing from the binary initial state (rather than assuming its closed formula), constructs every new simplicial attachment, compares its entire face-set intersection with the stated formula, and computes boundary ranks over \(\mathbb F_2\) for small complete filtrations.

The recorded local execution produced `PASS 192 integer-parameter pairs for exact firing shifts and every attaching intersection; all finite mod-2 Betti checks passed`. The exhaustive parameter pairs are \(1\le k\le12\), \(k+4\le n\le k+19\); the additional homology checks concern \(1\le k\le6\) and admissible \(n<18\).

The proof covers all \(k\ge1\), \(n\ge k+4\) through the closed support formula and exhaustive symbolic overlap cases. Finite checking alone would not justify an infinite-family or integral persistence claim. No independent audit or external certification is represented by this file.
