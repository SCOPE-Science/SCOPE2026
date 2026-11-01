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
# Verification

`python check.py` requires Python 3 with SymPy and verifies primitive-order Fourier zeros by exact remainders modulo integer cyclotomic polynomials. For each \(2\le N\le10\), every signed difference vector with coordinates in \(\{-1,0,1\}\) was checked for every deleted divisor class; the exact minimum weights match \((N/d)2^{\omega(d)}\). Explicit CRT product witnesses were independently checked for all divisor classes at lengths \(12,15,18,20,24,30,36,45,60,72\). The script reported `PASS: 103 exact primitive-shell checks, including exhaustive ternary differences for N <= 10.`

The all-length conclusion is deduced analytically from cyclotomic conjugacy, prime-power zero-sum blocks and the tensor-product support inequality. Finite enumeration cannot establish the all-length theorem. No external mathematical audit or numerical noise test was performed.
