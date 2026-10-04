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
The universal statement is verified analytically in `RESULT.md`. The critical checks are: (1) exact cancellation of party-relative pure Gaussian modes; (2) the replica integral identity \(Z=\lambda^{r/2}/\sqrt{\det(I+tK)}\); (3) \(0\le K\le2NI\); (4) the top eigenspace at \(2N\) is one-dimensional because the relevant cyclic replica shifts have only the constant vector as a common invariant; and (5) \(\lambda=(N-1)/(N^2a^2)+O(a^{-4})\).

`artifacts/verify.py` performs independent finite arithmetic checks. It reconstructs the replica matrices directly from the row/column permutations, compares the resulting genuine multi-entropy with two closed forms printed in Table 1 of arXiv:2609.30754v1, checks the asymptotic scaling of \(\lambda\), and checks transitivity of the replica-shift action for several \(n\). These tests corroborate the derivation but do not establish the infinite family by enumeration.

Limits: the proof is for fixed finite \(N\), integer \(n\ge3\), nonempty tripartitions, and the real fully symmetric pure Gaussian family. It does not establish analytic continuation in \(n\) or a general result for nonsymmetric Gaussian states.