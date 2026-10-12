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
# Verification and scope

Reproduce the finite checks by executing `python3 verify.py`. The script uses only the Python standard library. It checks the adjacency ranks of the twin blowups of \(K_3\) and \(K_4\) over \(\mathbb F_2\), exhaustively counts the \(2825\) subspaces of \(\mathbb F_2^6\) and tests each of them for the ideal property, and verifies the actual count \(68\) against the Gaussian formula. It also enumerates all nontrivial cuts of the two small blowup graphs and confirms the Cheeger constants \(2\) and \(3\).

Over \(\mathbb F_5\), it checks invertibility of the \(K_4\) adjacency matrix, verifies pairwise orthogonality of the eight sum-and-difference basis vectors and closure of the four-dimensional square ideal, and checks the exact Gaussian-ideal count \(1121\). A successful run prints `VERIFY_OK`.

The arbitrary-field ideal-lattice result uses the symbolic argument in `RESULT.md`; its general finite-field count uses the theorem on Gaussian binomial coefficients. The expander-family theorem uses the regular-graph Cheeger inequalities and the spectrum of a Kronecker product. The finite runs are **not** exhaustive for arbitrary \(N\), \(q\), or graph families, and there has been no external independent audit.
