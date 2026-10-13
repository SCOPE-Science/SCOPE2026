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
# Verification

The complete proof in `RESULT.md` is algebraic over all \(p_1,p_2,\eta\in[0,1]\) and every parity-preserving two-qubit unitary. It relies on the exact 16-branch Pauli decomposition and the 4-mode Majorana-conjugation overlap matrix.

For the nontrivial even pairs \((a_1a_2,b_1b_2)\) and \((a_1b_2,b_1a_2)\), the products of the two weights are both \(a_1b_1a_2b_2\), and the first absolute difference is at least the second. The largest minus remaining seven singular values therefore equals the bracket displayed in `RESULT.md`. Repeated odd pair types force \(C_-=0\). The four-mode fermionic state criterion then gives the Gaussian Choi region.

At \(\eta=1\), direct factorization gives \(C_+=[1-p_1-p_2+5p_1p_2/8]_+\). Setting \(p_1=p_2=p\) recovers the original common-noise concurrence \([1-2p+5p^2/8]_+\) and threshold \((8-2\sqrt6)/5\).

The bundled `artifacts/verify.py` uses only the Python standard library. It independently builds the 16-dimensional Gaussian-reference vector, system Pauli branches, and four-mode Majorana-conjugation matrix; checks the predicted overlap sparsity and block magnitudes for multiple gate phases; reconstructs all weighted block singular values for boundary and interior noise pairs; and compares the resulting concurrences with the theorem. These finite computations are supporting checks only, not an exhaustive or infinite proof.

No assertion is made about a channel-level convex-Gaussian equivalence or a circuit-level noise ceiling.
