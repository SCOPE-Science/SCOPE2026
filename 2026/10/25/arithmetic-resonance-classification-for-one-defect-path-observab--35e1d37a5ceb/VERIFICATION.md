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

# Reproduction and scope

Run `python verify.py` with a working installation of SymPy. The expected output is embedded in `verify_output.txt`. The program forms the weighted path Laplacian's tridiagonal characteristic polynomial and the product of the two characteristic polynomials obtained by deleting the sensor vertex. Because the weighted path is an irreducible symmetric Jacobi matrix, its spectrum is simple and a common characteristic root is exactly a zero-at-sensor eigenmode. SymPy computes exact greatest common divisors over rational polynomial coefficients; no floating eigenvalue or rank tolerance is involved in this algebraic observability decision.

The 462 observed decisions are compared to the analytic exceptional-set formula evaluated numerically away from denominator zeros; the code separately checks all 22 second-vertex test cases at central conductance \(1/2\) or \(1\). The finite range is \(2\le m\le12\). The infinite result, all positive real conductances, period law, and exact trigonometric equalities are established by the analytic argument in `RESULT.md`, not by this finite program.

The code uses the normalized convention that each ordinary path edge has conductance one, the unique central edge has conductance \(w>0\), and the sensor is numbered from the left endpoint. The code and its output are package-local and do not require earlier datasets or external downloads.
