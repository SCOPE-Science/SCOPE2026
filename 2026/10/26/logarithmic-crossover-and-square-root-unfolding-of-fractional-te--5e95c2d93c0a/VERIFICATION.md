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

# Reproduction and verification

Run `python check.py` in the same folder with Python 3.10 or newer and the `mpmath` package (see `requirements.txt`). The executable defines the Fourier transform using the exact lower incomplete gamma function, not the asymptotic formula under test. It computes bracketed real roots at 70 decimal digits, compares fixed-index splitting factors for three independent integers and four increasingly large frequencies at a logarithmic scaling value close to \(0.5\), and tests four exact triangular-transform values. The saved `check_output.txt` is its recorded standard output; the checker was executed successfully to produce that output.

For finite \(n\), the two offsets approach \(\pm\sqrt{2C_n\varepsilon}\). In the larger-frequency tests the predicted limit is \(\pm\arccos(e^{-0.5})\). The observed left/right asymmetry decreases with the exponent difference; it is not set to zero at finite parameters. Relative test tolerances are declared in the code.

The proof of infinitely many paired-root transitions relies on the uniform incomplete-gamma asymptotic expansion, the fixed-index analytic implicit-function theorem, and the \(C^1\) convergence argument. Finite numerical tests do not prove the asymptotic remainder, global completeness, novelty, or independent verification.
