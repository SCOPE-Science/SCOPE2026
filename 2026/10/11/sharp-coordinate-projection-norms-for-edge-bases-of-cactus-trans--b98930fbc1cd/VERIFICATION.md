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

# Reproducibility
The embedded `verify_cactus.py` is a standalone Python 3 program using only `fractions.Fraction` and `itertools`. Run `python verify_cactus.py`; the checked invocation reported:

```
EXACT_CACTUS_CHECK_OK 8 128
```

The test evaluates each graph's transportation norm directly by enumerating graph spanning trees and calculating exact rational flows by leaf elimination, then checks all coordinate-projection images of graph edge generators and compares with the closed formula. It includes nongeodesic long edges and two cycles sharing an articulation point. There are eight finite graphs and 128 tested coordinate-subsets; this count is not an exhaustive enumeration of all cactus graphs.

For arbitrary size, the proof proceeds through the edge-flow metric quotient, edge-disjoint cycle-kernel decomposition, metric-quotient operator norm identity, and an exact two-point weighted-median minimization. No finite numeric output is used as an infinite proof. The primary source arXiv:1207.1583 was publicly posted on 2012-07-06. External independent mathematical validation has not been performed.
