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

# Reproducibility and limits

Run `python3 verify.py` from the directory holding this document and the checker. The checker uses only the standard library. It recomputes complete power-value histograms, their additive convolutions, normalized residue fibres and exact rational collision moments for exponents \(6,10,14,18\) through the stated levels, including levels after the first singular descent. It also checks the multiplicity of the odd-unit power image modulo \(2^n\) for \(3\le n\le13\).

The completed run reported: `PASS: dyadic fibre counts, exact energy, and odd-unit image laws`, `Comparisons: 31818`, and `C(6,6)=13/2, C(6,12)=57/2`.

These are finite experiments. The infinite claims, including the sharp \(L^s\) threshold, are proved by the uniform unit-power image, disjoint parity decomposition, exact recursion and convergent/divergent geometric series in RESULT.md; no infinite claim rests on extrapolation from the checks. Independent audit is not performed.
