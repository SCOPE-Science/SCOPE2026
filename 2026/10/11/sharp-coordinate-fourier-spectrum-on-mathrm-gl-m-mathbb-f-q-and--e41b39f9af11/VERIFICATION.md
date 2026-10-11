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

# Verification record

Run `python3 verify.py` with Python 3.10+; no nonstandard packages are required. The script builds finite fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), enumerates invertible matrices, computes every relevant Gram entry from exact additive-character counts, and checks the predicted rook-decomposition eigenspaces and the two-dimensional compression. It tests seven complete examples: \((q,m)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)\), with group sizes 6, 168, 20160, 48, 11232, 180, 480 respectively. It also tests exact rational determinant/crossover signs for \(2\le q\le100\) and \(2\le m<2q+15\) (including non-prime-power integer parameters as algebraic stress tests only). Successful execution emits `VERIFY_OK`.

These finite checks support the computations but do not establish the unrestricted quantifiers. The proof in RESULT.md independently derives the requisite rank Fourier sums and the rook-graph decomposition, then proves positivity and the strict \(m=2q\) threshold for every prime power. Source [1] was inspected at the original arXiv full-text §§1–2.1; [3] at its introduction and §4.2; [4] at its original full-text introduction and harmonic-frame discussion. Historical equivalence through [2] cannot be excluded by the material available. This is not independent mathematical audit or certification.
