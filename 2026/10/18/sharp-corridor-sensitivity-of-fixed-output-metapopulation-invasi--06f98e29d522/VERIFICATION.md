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

The proof is self-contained. To corroborate the matrix calculations, install NumPy for Python 3 and run `python verify_capacity.py` in the same directory. The script assembles the symmetric matrix \(H_G\) directly from adjacency, degrees and patch qualities, evaluates its Perron root with `numpy.linalg.eigvalsh`, and compares the original graph with the graph after one edge addition. It checks seven values of the exact three-vertex formula, then exhausts all connected labelled graphs with \(3\le n\le5\), their nonedges, and each assignment from \(\{1/3,1,3\}^n\); the independently calculated total is 769,905 comparisons. The program concluded with `All numerical tests passed.`

The finite tests do **not** prove the universal lower bound or exhaustion of the real attainable interval. Those statements follow from the positive Perron vector/Rayleigh argument and the analytical three-vertex family. No independent external audit or stochastic simulation has been performed. The main remaining risk is equivalent prior literature under another formulation of degree-normalized patch movement; some plausible sources were accessible only in part.
