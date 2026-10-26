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

# Reproduction and proof boundary

Install the Python requirements in `requirements.txt`, then run `python verify.py` from the extracted file directory. The code compares graph types using exact isomorphism and enumerates every admissible trace mask, giving a fully deterministic finite certificate.

Observed output from the actual embedded checker:

```
SIX_EDGE_KERNEL unlabeled_graphs 68 maximum_patterns 49 ... PASS
SMALL 2 VC 1 no_larger_sets 0 ... PASS
SMALL 3 VC 2 no_larger_sets 1 ... PASS
SMALL 4 VC 2 no_larger_sets 20 ... PASS
SMALL 5 VC 3 no_larger_sets 210 ... PASS
SMALL 6 VC 4 no_larger_sets 3003 ... PASS
STAR_WITNESS 7 patterns 32 PASS
STAR_WITNESS 8 patterns 32 PASS
STAR_WITNESS 9 patterns 32 PASS
STAR_WITNESS 10 patterns 32 PASS
VERIFY_OK graph_isomorphism_kernel=PASS small_cases=PASS all_dimension_upper=REDUCTION star_lower=PASS
```

The executable enumerates the \(68\) graph-isomorphism classes of graphs with exactly six edges and no isolated vertices and proves at most \(49\) traces in the generous model. This is exhaustive for the kernel, not an incomplete sample. The separate mathematical reduction in `RESULT.md` proves why all dimensions reduce to that kernel. Small-dimensional computations range only over anchored weight-two points, justified by XOR symmetry, and thus exhaust every possible shattered family at the tested cardinalities. The star-witness argument is symbolic for all \(d\ge7\); checks for dimensions seven through ten corroborate it.

Scientific limits: independent implementation and human publication-priority review have not been performed. A code or dependency failure would invalidate the computational certificate, not prove any impossibility theorem. This record neither asserts independent certification nor substitutes finite experiments for the stated all-dimensional reduction.
