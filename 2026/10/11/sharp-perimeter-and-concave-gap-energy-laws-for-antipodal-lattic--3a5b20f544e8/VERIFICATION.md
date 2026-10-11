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

Let \(n\ge3\), and let an antipodal transversal of the regular \(2n\)-gon have cyclic positive integer gaps \(g_1,\ldots,g_n\) summing to \(2n\). The key strict mathematical certificate is the integer-majorization comparison with the extreme vectors
\[
(n+1,1,\ldots,1),\qquad (2,\ldots,2),\qquad
(3,2,\ldots,2,1).
\]
Strict discrete concavity and one-unit transfers prove the inequalities for every \(n\). For even \(n\), the antipodal parity constraint permits the last vector only when its \(1\) and \(3\) occur half a cycle apart in gap position.

The program `verify.py` enumerates all \(2^n\) antipodal transversals for each \(3\le n\le14\). It checks the exact integer objective \(f(k)=-k^2\) and compares the *entire* predicted sets of extremizing configurations, not only the extremal values. It also checks the exact chord-derived formulas numerically. SymPy independently confirms the perimeter-defect identity and its leading asymptotic. These finite computations are regression evidence and are not a substitute for the infinite proof.
