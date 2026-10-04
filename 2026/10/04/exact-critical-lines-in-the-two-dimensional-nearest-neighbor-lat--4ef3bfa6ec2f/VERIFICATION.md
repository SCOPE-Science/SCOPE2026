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

The proof is analytic. The following checks were performed on the packaged claim.

1. Re-derived the source normalizations \(E(p)=\sum_j(1-\cos p_j)\), \(s(0)=\langle\sin^2p_1/E\rangle\), and \(c(0)-d(0)=\frac12\langle(\cos p_1-\cos p_2)^2/E\rangle\).
2. Verified symbolically that permutation symmetry gives \(B_2+(n-1)C_2=1\) and \(L=B_2-C_2\), hence \(s(0)=(1-(n-1)L)/n\).
3. Recomputed the \(n=2\) reduction to \((2/\pi)\int_0^1\sqrt{(1-u)/(1+u)}\,du\) and the antiderivative value \(\pi/2-1\).
4. Checked the hyperbola substitutions \((\lambda-1)(\mu-2)=2\) at the two exact critical couplings.
5. Replayed `verify_threshold_constants.py` from the actual embedded bytes. It numerically checks the reduced integral and all displayed algebraic identities. The numerical test is corroborative only; it is not an infinite proof.

The result does not claim generic-potential or upper-threshold statements. Originality remains subject to the explicitly recorded inaccessible 2021 full-text risk.
