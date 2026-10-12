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

# Reproduction and boundaries of verification

The complete derivation is in `RESULT.md`. Install the dependency listed in `requirements.txt` and execute `python3 verify.py` with a Python interpreter and NumPy available.

The packaged checker builds the triangular-network adjacency matrix from intersections of unordered pairs rather than from the incidence identity used in the proof. For each detector set it diagonalizes that adjacency matrix and directly computes the ranks of detector restrictions on the numerically resolved eigenspaces. Every nonempty set is checked for \(N=3,4,5\); additional deterministic pseudo-random samples are tested for \(N=6,7,8\). It independently checks positive-rate non-Hermitian loss eigenvalues on \(N=3,4,5,6\), tests explicit minimizing sets for \(3\le N\le12\), and enumerates the minimum sizes directly for \(3\le N\le6\).

Actual packaged check:

```text
VERIFY_OK spectral_ranks=1760 threshold_checks=14 loss_spectrum=80
```

All equality comparisons of discrete spectral dimensions were exact integer comparisons after numerical rank determination with a stated tolerance. Floating-point spectral checks are corroboration only and may suffer from numerical conditioning in other regimes. They do **not** establish a theorem for unbounded \(N\), nor do finitely many random cases exhaust arbitrary large detector subsets. The analytical unsigned-incidence lemma, sector decomposition, and dissipativity argument prove the full claim. No external independent validation or certification is asserted.
