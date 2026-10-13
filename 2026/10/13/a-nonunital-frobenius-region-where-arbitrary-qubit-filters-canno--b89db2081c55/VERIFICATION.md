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

The proof of the universal statement is analytic. For a filter \(\Psi=(N,d)\), recomposition gives \(A=MNM\) and \(b=MNc+Md+c\). The two nontrivial imported facts were checked in the primary full text of arXiv:1411.2517: Proposition 5 gives the sufficient qubit entanglement-breaking condition \(\|A\|_1+\|b\|_2\le1\), and Lemma 7 gives \(\|Md\|_2+\|MN\|_{\mathrm F}\le\|M\|_{\mathrm F}\) for every positive trace-preserving qubit filter. Schatten Hölder supplies the remaining matrix inequality.

The companion `verify.py` uses exact integer and rational arithmetic to check the explicit generalized amplitude-damping witness \(p=1/5\), \(\gamma=3/5\): the affine norm condition is strict, the source's PPT entanglement-breaking inequality is violated, and the algebraically equivalent form of that threshold is consistent. The checker is evidence for the explicit witness, not a substitute for the universal proof.

The theorem is limited to non-entanglement-breaking qubit channels satisfying \(\|M\|_{\mathrm F}+\|c\|_2\le1\). No exhaustive claim is made outside that region, for higher dimensions, or for filtered index larger than two.
