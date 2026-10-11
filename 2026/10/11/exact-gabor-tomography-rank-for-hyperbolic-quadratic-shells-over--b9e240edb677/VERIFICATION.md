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

# Verification of the quadratic-shell Gabor-lifting theorem

Execute `python3 checks/verify.py` from the directory containing this document. The script requires Python 3 and NumPy. It constructs every shift and frequency in the three prime-field cases, and counts additive-character residues exactly: over prime characteristic, a root-of-unity sum vanishes exactly when each of the prime residue-class multiplicities is equal. It also independently samples prime-power extension-field cases with a trace character.

Observed results: \(q=3,r=2\) gives \(3393\) nonzero ambiguity entries out of \(6561\); \(q=5,r=2\) gives \(208225\) out of \(390625\); \(q=3,r=3\) gives \(285741\) out of \(531441\). An independently coded \(\mathbb F_9\) implementation checks \(501\) pairs covering all four geometric cases. Thus \(929128\) exact coefficients were checked. Full mathematical justification for arbitrary odd prime powers and every \(r\ge2\) is the finite-field Gauss/Salié and Weyl-coordinate argument in `RESULT.md`, not these examples.

Same-model review examined the character-sum normalizations, radical-free sectional decompositions, boundary cases \(c=0\) and \(w=0\), the norm-fiber multiplicities, and the Weyl-rank correspondence. Independent audit has not been performed.
