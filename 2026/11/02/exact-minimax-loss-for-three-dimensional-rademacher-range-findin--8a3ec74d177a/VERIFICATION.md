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

The proof is an exact projective-sign occupancy argument together with two finite tight-frame identities and two Cauchy--Schwarz inequalities. Its quantifiers cover all invertible real \(3\times3\) matrices and all positive integer sketch widths \(\ell\).

Run `python verify.py` with SymPy installed. In its executed test, six invertible integer matrices were each checked at widths one through five by exhaustively enumerating \(4^\ell\) projective-sign words, forming direct exact-rational orthogonal projectors, and comparing their squared residuals with the formula. The execution passed 180 exact-rational comparisons plus eight exact rank-distribution consistency checks. This checks the algebra on representative inputs; it does not establish generality in place of the proof or certify numerical floating-point stability.

The sharp equality construction is \(A=I_3\). The uniqueness argument follows because equality of the four singleton Cauchy--Schwarz inequalities forces all four nonorthogonal sign representatives to be eigenvectors of the same symmetric Gram matrix, hence that Gram matrix is scalar.

Independent mathematical audit has not been performed.
