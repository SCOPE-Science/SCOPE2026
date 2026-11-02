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

Run `python verify.py` with Python 3 and SymPy. The actual standalone checker performs exact polynomial Gröbner membership over \(\mathbb F_5\), checks the four projective singular charts, verifies nonzero Hessian determinants, and enumerates every projective point of \(\mathbb F_5\) and \(\mathbb F_{25}\) on the specified sextic. It independently repeats the \(\mathbb F_{25}\) calculation through square-root-fiber weights. Successful execution ends with `VERIFY_OK`.

Verified singular chart counts: \((55,7,3,0)\); every singular coordinate satisfies \(t^5-t=0\), and every node has a nonzero local Hessian determinant. Verified projective surface counts: \(91\) and \(1651\). The resolution has \(416\) and \(3276\) points, respectively, because each of \(65\) nodes is replaced by a conic with \(q+1\) points. The all-extension formulas and Frobenius eigenvalues are supplied by the mathematical proof using the dimension \(b_2=106\) and equality in the Weil bound, not by finite tests alone.

The checker establishes finite, exact calculations for this polynomial only; the cited background on rational double points, characteristic-five étale cohomology, and Weil conjectures is mathematical input, not certified by the program. No independent audit has been performed.
