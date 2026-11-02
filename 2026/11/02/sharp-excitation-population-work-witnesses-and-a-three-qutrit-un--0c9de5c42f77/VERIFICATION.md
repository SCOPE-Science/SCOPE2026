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

The self-contained finite-dimensional checker is `verification/check.py`. Execute from the file bundle root using `python verification/check.py`. It requires Python 3, NumPy and SciPy (used only for a null-space basis and eigenvalues), and uses fixed pseudorandom seeds.

The checker constructs every normalized symmetric occupation basis vector for three, four, and five cells; explicitly maps the higher-excitation symmetric blocks into previously unused lower-excitation eigenspaces; verifies the columns are orthonormal and that the transformed compressed Hamiltonian is the exact diagonal operator with \(q\mapsto q-1\) for \(q\ge2\); and verifies work gain equals the two-or-more-excitation weight for sixteen random positive density matrices at each size. It checks the sharp two-cell mixed state, an exact three-cell equality case, a three-cell state with passive dephasing but positive work, and the integer dimension inequality for all \(3\le N\le29\).

Observed replay status: PASS. Matrix identity errors are at floating-point roundoff (below \(10^{-10}\)). The proof of the all-integer statement is the dimension inequality in `RESULT.md`; numerical verification at finitely many sizes is not an exhaustive infinite certification. The eigenvalue arguments at \(N=2\) and the fixed-unitary impossibility are analytical; the checker tests their stated exact witnesses but not an exhaustive search over all unitaries.

The closest contemporary two-cell three-level battery manuscript was not accessible in complete text. Scientific originality remains a self-review rather than an independent priority certification.
