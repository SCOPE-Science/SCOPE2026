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

The analytic proof in `RESULT.md` is decisive. The determinant factorization uses the standard Cauchy identity and the exact root-of-unity resultant, valid for all positive orbit cardinalities. The phase derivative is strictly negative for all interior radii. Differentiating the exact logarithmic deficit establishes a universal sharp coefficient, including the collision boundary as a limit.

Execute `python CHECK.py` with Python 3 and NumPy. The checker constructs normalized Szegő Gram matrices for eight orbit-size pairs, four radius pairs, and five phases (160 direct determinant and stability tests). It then verifies three near-optimal phase-loss ratios in a non-coprime example. Expected output: `PASS: 160 direct determinant and sharp-stability comparisons, 3 local-limit checks`. The finite cases cannot prove any universal quantifier and are not used to infer optimality by enumeration.

Source inspection: the author-uploaded primary preprint arXiv:2606.00912 was read through its frame definitions, theorem statement, proof and model-space construction; the closest public one-radius Szegő determinant theorem was read in full. The general kernel \(D\)-optimality paper arXiv:2609.15556 was available only through its public abstract. The 2010 two-circle Fekete question and accompanying answer were inspected for the differences in object and quantifiers. No independent mathematical audit has been performed.
