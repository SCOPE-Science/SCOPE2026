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

# Verification and reproducibility

`verify.py` enumerates all fixed-size draw sequences of lengths one, two and three on \(3\le n\le6\) for every permissible \(k\), then checks exact zero-count moments, exact nonzero-twin expectations, and the equivalence between signatures and both recovery predicates. It uses Python's integer combinatorics and rational arithmetic, with no third-party packages. Its recorded run in `verification_output.txt` passed 57,768 assertions.

The numerical table in the output evaluates the exact finite intensities when \(k\approx cn/\log n\); convergence in \(\log n\) is slow, and the table is not used as proof. The infinitely many \(n\) statements are justified instead by the separate factorial-moment and multiplicative hypergeometric-to-Bernoulli arguments in `RESULT.md`. No independent validation has been undertaken. Run `python verify.py` in the directory containing the extracted files.
