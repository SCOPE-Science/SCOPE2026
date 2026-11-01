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

# Verification

Run the packaged file `verify.py` using Python 3 and its standard library. The script constructs faces directly from the three explicit maximal-clique vertex masks, computes reduced simplicial boundary ranks over \(\mathbb F_2\) in eight configurations, and compares them with the claimed binomial formula. It separately computes signed fixed-face Lefschetz traces for every product conjugacy class in three cases, comparing against characters obtained from exterior powers of the integral augmentation lattices. The eight homology cases and \(182\) symmetry character comparisons passed.

The spectral-sequence proof in `RESULT.md` establishes the integral and unrestricted assertions; computational agreement in finite instances is not a proof of infinite quantifiers or freedom from torsion. The final nonequivariant homotopy upgrade relies on the block-graph shellability theorem in arXiv:2602.09623v1, Corollary 3.4, and the nonpure shellability homotopy theorem of Björner–Wachs, Theorem 4.1. No external or independent audit has been performed.
