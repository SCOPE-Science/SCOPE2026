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

# Reproducibility
Run `python3 verify.py` from the directory containing the extracted package files. The script uses only the Python standard library. It constructs independently the least reachable value in every residue modulo the smallest generator, using weighted shortest paths; computes pseudo-Frobenius membership by the defining criterion; and checks the closed formulas and branch selection. It covers 640 parameter pairs for integers \(4\le h\le11\), eight exact prethreshold counterexamples, and 196 additional base-three comparisons outside the theorem. The expected final line is `PASS 640 stable pairs h=4..11, 8 sharp boundary failures, 196 h=3 boundary checks`.

The finite test is not a proof of infinitely many cases. The exact normalization, monotonicity and maximality arguments in RESULT.md prove all stated parameters. The proof does not establish the Apéry formula for smaller parameters, and no independent mathematical audit has been performed.
