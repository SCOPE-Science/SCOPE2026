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
# Verification and exact scope

The theorem is analytic. The indispensable steps are (1) the strict negative incident-normal criterion for entering a quadrilateral at a vertex; (2) the absence of a disjoint pair of simultaneously illuminable vertex pairs; (3) the resulting three-vertex incidence lower bound; (4) an explicit three-direction covering construction for non-parallelograms, and four directions for parallelograms; and (5) the same counting inequality with fractional weights.

To reproduce finite checks, run `python verify.py` using Python 3. The checker enumerates complete illumination sign cells for \(275\) rational normal-turn fans, with meshes \(N=10,12,14\), verifies the star pattern, and solves each of the four multiplicities \(m=1,2,3,4\) by exact finite breadth-first search over capped vertex-incidence states. Reported output:

```
PASS: 275 finite normal-fan/multicover instances per multiplicity
PASS: four multiplicities, opposite-pair prohibition and common-pivot tests
```

Floating-point trigonometry is used only to classify the finite test cells. The general proof is independent of the checker and does not infer all-real parameter coverage from a finite mesh. No external or independent audit has been performed.
