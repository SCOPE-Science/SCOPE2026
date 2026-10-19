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

The accompanying `verify.py` uses only the Python standard library. Run `python3 verify.py` alongside these extracted files. The program independently forms sorted irrational-rotation orbits with 90-digit Decimal arithmetic and compares observed circular gap lengths and multiplicities against the exact formulas. It also independently compares 180 finite Rényi entropy values and tests the large-cutoff lower and upper empirical-density limits for four orders. The expected successful diagnostic is `VERIFY_OK 45 high-precision independent orbit-gap cylinders; 180 entropy comparisons; 8 level-density boundary checks`.

All of these tests are finite. The logical proof of universal finite-block formulas rests on the classical three-distance theorem, and the infinite asymptotics use Binet estimates, uniform block convergence, transverse threshold crossings, Fibonacci summation and harmonic Riemann sums. The diagnostic program alone cannot establish novelty, infinite validity or the stated limiting densities. An external independent audit has not been performed.
