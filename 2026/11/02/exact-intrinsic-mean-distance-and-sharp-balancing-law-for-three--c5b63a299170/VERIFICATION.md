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

The analytical claim follows from the four-route shortest-path formulas, integrated same-edge and cross-edge rectangles, and the exact nonnegative polynomial gap; these arguments apply to every positive real triple and are not inferred from finite test results.

Run `python3 verify.py` from the directory containing the research files. The script is self-contained and uses only Python standard-library modules. It reassembles the cubic from exact rational edge-pair integrals independently of the polynomial statement, checks the sharp lower-bound certificate and equality cases across a rational grid, verifies exact values in the isosceles family, and compares the independently coded four-route metric with pseudorandom arclength samples.

The script actually ran and printed `PASS: 330 exact assertions and 750000 independently sampled point-pairs`. The five sampled positive-length triples were \((1,1,1)\), \((0.5,0.5,2)\), \((0.2,1.3,1.5)\), \((1,2,3)\), and \((0.03,0.12,2.85)\), using 150,000 sample pairs each. All five absolute discrepancies were below 0.002.

The exact-rational assertions exhaust only the specified finite parameter grid; Monte Carlo simulations are not an infinite-dimensional proof. The original 1982 paper's full text was unavailable for direct historical-priority verification; a later public paper describes its constrained-length coverage. No external independent audit is claimed.
