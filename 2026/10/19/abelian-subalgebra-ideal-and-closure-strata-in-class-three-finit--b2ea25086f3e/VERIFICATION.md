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

# Reproducibility and boundaries

The proof is given in `RESULT.md` and depends only on the displayed bracket, field arithmetic with \(2\) invertible, Gaussian subspace counts, and explicit Lie-ideal generation. In particular, the extension-degree statements are symbolic and not inferred from enumeration.

The standalone `verify_abelian_breadth.py` uses Python's standard library. Running `python verify_abelian_breadth.py` exhausts all \(2664\) subspaces of \(\mathbb F_3^5\) and all \(42176\) subspaces of \(\mathbb F_5^5\), testing every basis commutator, ideal stability, and closure under iterated brackets. The computed abelian dimension profiles are \((1,121,157,13)\) and \((1,781,931,31)\). The abelian-ideal profiles are \((1,4,1,1)\) and \((1,6,1,1)\). The generated-ideal dimension profiles are \((1,4,1,22,264)\) and \((1,6,1,56,1680)\), indexed from dimension zero in each case.

The script constructs \(\mathbb F_9\) using the irreducible polynomial \(T^2+1\) over \(\mathbb F_3\), enumerates all \(91\) one-dimensional \(\mathbb F_9\)-subspaces of \(\mathbb F_9^3\), tests all pairs on each, checks \(90\) normalizers of \(\mathbb F_3\)-dimension eight and one of dimension ten, and runs \(12000\) deterministic vector-pair cross-checks. This does not exhaust all \(\mathbb F_3\)-subspaces of the ten-dimensional algebra.

Limitations: no computational experiment certifies historical priority or all extension degrees. The finite checker does not constitute an independent mathematical audit. Publication of the result should distinguish the prior structural classification from the new quantitative formulas.
