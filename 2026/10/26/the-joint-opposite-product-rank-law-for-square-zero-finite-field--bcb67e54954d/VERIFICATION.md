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
# Reproducibility and checks

Run `python3 CHECK.py` using standard Python 3. The program enumerates every matrix over the specified finite fields, checks the square-zero condition through actual matrix multiplication, determines rank by finite-field Gaussian elimination, tabulates both ordered product ranks and compares their exact rational frequencies with the independently encoded Gaussian flag probabilities. The \(\mathbb F_4\) arithmetic uses the irreducible modulus \(T^2+T+1\) over \(\mathbb F_2\).

The verified output is embedded separately as `CHECK_OUTPUT.txt`. In total, \(111719\) ordered pairs were checked across dimensions one to four over \(\mathbb F_2\), dimensions two and three over \(\mathbb F_3\), and dimension two over \(\mathbb F_4\). This verifies the finite instances only. The infinite probability formula, sharpness for all dimensions, and odd-dimensional limit are supplied by the proof in `RESULT.md` and not certified by finite computation. No independent mathematical audit has been performed.
