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

The exact checker is `verify.py`. A fresh replay from the package path produced:

```text
VERIFY_OK
E_size=8
Ref_size=16
Ref_invertibles=2
ambient_n1_subspaces=2 counterexamples=0
ambient_n2_subspaces=67 counterexamples=0
```

The checker uses only exact binary arithmetic. For the main example it tests every one of the \(512\) linear endomorphisms against the defining pointwise reflexive-hull condition on all \(8\) vectors, then verifies that the resulting hull is exactly \(E\cup(I_3+E)\) and that exactly two hull elements are invertible. For minimality it generates every linear subspace of the full endomorphism spaces in ambient dimensions \(1\) and \(2\) and tests the same property without sampling.

The symbolic proof in `RESULT.md` independently derives the hull relation \(r+s=t\) and proves the block extension for every \(n\ge3\). No computation is used as evidence for an infinite family beyond what is proved symbolically.

Limits: the exhaustive minimality statement is only over \(\mathbf F_2\); odd finite fields and classification of all dimension-three counterexamples are not checked or claimed. Independent audit has not been performed.
