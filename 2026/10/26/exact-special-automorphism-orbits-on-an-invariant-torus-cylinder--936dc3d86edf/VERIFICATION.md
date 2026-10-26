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

# Verification of the stated boundary-orbit theorem

The general proof in `RESULT.md` is the primary evidence. The standalone `verify.py` is a SymPy checker for the weight-zero formulas and identities that the proof uses. It was executed as `python3 verify.py` after extraction from the embedded artifact set.

Observed result:

```text
VERIFY_OK n=1: invariance, degrees, derivation and boundary-monomial reductions
VERIFY_OK n=2: invariance, degrees, derivation and boundary-monomial reductions
VERIFY_OK n=3: invariance, degrees, derivation and boundary-monomial reductions
VERIFY_OK n=4: invariance, degrees, derivation and boundary-monomial reductions
VERIFY_OK affine-complement gauge x=1
VERIFY_OK boundary restriction delta(C)=-3 and delta(B)=delta(U_i)=0
```

For each checked \(n\), the script verifies that the triangular derivation annihilates the source hypersurface equation, the weight-zero relations are correct, and the Laurent exponent reduction preserves monomials in a bounded range. It also checks the affine-chart substitution. It does **not** enumerate all locally nilpotent derivations, prove an infinite universal statement through testing, establish historical priority, or perform an independent audit. The universal conclusions follow from the lattice proof, the group-action unit lemma and the nonzero translation field in `RESULT.md`, conditional on the cited source's geometric quotient and invariance results.
