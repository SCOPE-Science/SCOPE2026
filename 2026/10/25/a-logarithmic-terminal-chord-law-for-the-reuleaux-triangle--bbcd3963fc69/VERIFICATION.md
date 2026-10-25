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

# Verification of the terminal long-chord law

Run `python verify_reuleaux_tail.py` with NumPy and SciPy. On the packaged copy, the checks completed with:

```
THREE_DISK_CHORD_INTERVAL_GEOMETRY_OK
TAIL_SCALED_REMAINDER 1e-03 0.6819772
TAIL_SCALED_REMAINDER 1e-04 0.6804441
TAIL_SCALED_REMAINDER 1e-05 0.6802437
TAIL_SCALED_REMAINDER 1e-06 0.6802171
LOG_COEFFICIENT_DIFFERENCE_OK 1e-03 0.95426385
LOG_COEFFICIENT_DIFFERENCE_OK 1e-04 0.95484264
SHARP_EPSILON_LOG_EPSILON_CHORD_TAIL_CHECKS_OK
ALL_REULEAUX_CHORD_TAIL_CHECKS_OK
```

The three-disk calculation uses elementary circle intervals, bisection and angular quadrature; the difference estimate cancels the unknown \(O(\varepsilon)\) contribution at leading order. The infinite-dimensional asymptotic assertion follows only from the uniform analytical proof in `RESULT.md`; finite numerical checks do not prove it. The available scientific comparison was restricted by access to the full 1987 Gates article.
