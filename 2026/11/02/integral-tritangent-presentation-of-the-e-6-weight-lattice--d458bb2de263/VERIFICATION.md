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

# Exact checks and reproducibility

Run `python verify_tritangent.py` using Python 3.10 or later. The file needs no nonstandard dependencies. It enumerates the six exceptional labels, fifteen pair-line labels, six conic labels and the forty-five tritangent triples; checks all forty-five as anticanonical sections; constructs the twenty-one selected columns and the specified twenty-one rows; computes their exact determinant \(+1\) using rational Gauss–Jordan elimination; verifies integral recovery of all forty-five columns, checking every coordinate; and prints `INCIDENCE_OK`, `LATTICE_OK`, `GEOMETRY_OK`, and `SMITH_OK`.

This is a finite exact certificate for the incidence lattice, independent of floating-point calculations or numerical rank tests. The theorem's geometric universality follows from the six-point blowup description and the elementary abelian-group elimination in the proof, not from sampling cubic surfaces. The calculation does not verify originality, cubic-surface moduli applications, or any extension to positive characteristic. No independent scientific audit has been performed.
