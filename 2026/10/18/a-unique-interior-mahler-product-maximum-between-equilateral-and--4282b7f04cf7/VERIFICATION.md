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

Run `python verify_square_volume.py` with a standard-library Python 3 interpreter. The code constructs the original six metric-pair inequalities and twelve signed molecular points in three exact rational coordinates. It enumerates every dual vertex by invertible triples of active planes; each facet polygon is sorted in a rational coordinate plane and triangulated by exact determinants. It compares independently enumerated volume and face-count data against the claimed formulas for the six interior rational parameters \(101/100\), \(11/10\), \(6/5\), \(3/2\), \(9/5\), and \(199/100\).

The package verifier completed with `ALL EXACT POLYHEDRAL AND DERIVATIVE CERTIFICATES PASSED` at all six parameters. The continuum theorem depends on the explicit cube/polar geometry and the strict derivative sign proof in `RESULT.md`; no finite experiment certifies the whole interval. No third-party code, external files or independent validation is assumed.
