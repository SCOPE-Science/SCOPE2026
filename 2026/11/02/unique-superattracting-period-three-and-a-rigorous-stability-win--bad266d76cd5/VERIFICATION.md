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

Run `python3 verify.py` using a standard Python 3 installation; no third-party packages are required. The program represents \(\mathbb Q(\sqrt2)\) exactly as pairs of rational coefficients and determines surd signs by integer-square comparisons. It verifies the complete critical-return factorization, transformed-polynomial coefficients, root uniqueness sign variations, rational parameter bracket, all uniform cyclic trapping inclusions and derivative bounds. The additional high-precision orbit printout is not a proof. A successful run prints `PASS` followed by the computed superstable parameter and cycle. The proof of the full infinite parameter interval rests on exact endpoint inequalities, monotonicity, and the contraction theorem, not numerical sampling. Independent mathematical verification remains unperformed.
