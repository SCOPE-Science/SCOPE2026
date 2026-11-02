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

# Reproducible checks

Run `python verify_squarezero_evolution.py` with Python 3 (standard library only) from the same directory. It prints 13 rank-spectrum comparisons for \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\) and directly checks the defining Leibniz equations in all \(2^9\) and \(2^{16}\) candidate linear maps for the graph evolution algebras of \(K_{1,2}\) and \(K_{2,2}\), respectively. The recorded successful end marker is `EVOLUTION_SQUARE_ZERO_RANK_OK 13 spectra; 2 full Leibniz enumerations`.

For each symmetric side block the program exhaustively enumerates the independent off-diagonal entries, reconstructs the diagonal from zero row sums, multiplies matrices in the given finite field, tests \(P^2=0\), and computes the actual linear rank independently of the closed formula. The direct Leibniz tests do not use the block-derivation characterization.

These computations cover only the specified small finite fields and dimensions. The all-field proof is in `RESULT.md`, notably the symplectic-isotropic image classification and the even-side triple analysis. No formal proof assistant, external checker, or independent mathematical audit was used.
