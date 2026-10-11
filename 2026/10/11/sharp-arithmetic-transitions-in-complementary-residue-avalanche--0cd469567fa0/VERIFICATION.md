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
# Reproducible scientific checks

From the directory containing `verify.py`, run `python3 verify.py` with Python 3.8 or later; there are no third-party dependencies. The program independently simulates simultaneous parallel firing from each finite binary support, establishes period \(n\) in each tested case, transports complete firing sets under inverse-modulus relabeling, and compares exact facet sets with cyclic-interval facets. It then enumerates faces and computes augmented simplicial boundary ranks over \(\mathbb F_2\), independently checking the predicted circle, odd-sphere and equality-branch wedge homology ranks.

Recorded replay:

```
VERIFY_OK
exact_firing_and_nerve_cases= 3252
independent_mod2_homology_cases= 52
boundary_n8_k3_3spheres2_vs_1sphere3=TRUE
first_counterexample_n5_k2_S1=TRUE
```

These are finite checks; the unbounded homotopy theorem follows from the exact firing-orbit identification and the fully stated hypotheses of the previously proved cyclic-arc nerve classification. Binary field checks cannot detect odd torsion or establish homotopy equivalence on their own. The primary-source date and the original published statements are documented in the references.
