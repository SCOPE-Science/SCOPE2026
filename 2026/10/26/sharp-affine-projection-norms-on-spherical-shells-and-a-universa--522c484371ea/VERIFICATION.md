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

# Verification and reproducibility

The exact definitions and analytical proof are in `RESULT.md`. The included `CHECK.py` is self-contained apart from standard Python, SciPy and mpmath. Run `python3 CHECK.py` from the folder containing this file and the executable. The program recomputes the cap moment by independent one-dimensional quadrature for dimensions two through nine; checks its elementary planar primitive; integrates the planar projection kernel directly in radial and angular coordinates; checks the planar contact root and the known full-disk and limiting boundary values; and evaluates eight high-precision contact scaling ratios in dimensions two through five.

Observed execution result: `PASS 205 independent quadrature and formula assertions` and `CUSP PASS 8 high-precision scaling assertions`.

These finite computational checks support internal consistency. The all-dimensional theorem, uniqueness of contact and exact regularity loss rely on the written analytic arguments, not on extrapolation from the tests. The numerical quadrature tolerances and tested dimensions are visible in the source. No third-party independent audit or validation is asserted. Bibliographic priority remains provisional, especially for uncatalogued analyses of annular polynomial projections.
