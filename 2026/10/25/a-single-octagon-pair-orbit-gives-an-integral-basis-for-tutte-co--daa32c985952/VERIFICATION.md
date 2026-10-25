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

# Verification of the integer-cycle theorem

Run `python verify_tutte_coxeter.py` in a Python 3 environment with SymPy 1.14.0. All necessary source data are constructed from six symbols; the code imports no graph or research databases. The exact script in this package was executed successfully on the claimed graph.

The script confirms: 30 vertices, 45 edges, girth eight; 90 distinct shortest cycles; 1,125 disjoint shortest-cycle pairs; 435/1,260/900 unoriented quotient cells; vanishing \(\partial_1\partial_2\) and every torus boundary; \(\operatorname{rank}_{\mathbb F_{101}}\partial_2=810\); exactly four \(S_6\) torus-orbits of sizes \(45,360,360,360\); orbit binary ranks \(35,89,89,90\); distinguished 360-pair geometric profile \((3,3)\); signed determinant \(-1\) of its deterministic 90-by-90 coordinate minor. The program prints both zero-based index lists defining that minor.

The finite-field rank is used only as a lower bound on characteristic-zero boundary rank. The integral unimodular minor independently proves primitiveness. Combining these with the signed cycle condition and the rank count yields \(H_2\cong\mathbb Z^{90}\) and integral generation. Neither finite-field ranks nor graph searches alone would justify the integral theorem. No independent validation or publication-priority guarantee is implied.
