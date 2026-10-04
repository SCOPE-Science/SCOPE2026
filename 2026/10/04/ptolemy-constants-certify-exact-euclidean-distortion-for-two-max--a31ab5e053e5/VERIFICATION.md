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

The proof has two independent ingredients. First, for each linear isomorphism \(T\) to Euclidean space, apply the equivalent-norm Ptolemy estimate to the Euclidean pullback norm \(|x|_T=\|Tx\|_2\). This yields \(C_{\mathrm{Pt}}(X)\le(\|T\|\|T^{-1}\|)^2\), and therefore \(C_{\mathrm{Pt}}(X)\le d_{\mathrm{BM}}(X,\ell_2^2)^2\). Second, the identity map gives the upper distortions \(\sqrt2\lambda\) for \(A_\lambda\) and \(\lambda\) for \(B_\lambda\). The exact source Ptolemy constants are the squares of these upper bounds, forcing equality.

Boundary checks: \(A_{2^{-1/2}}\) and \(B_1\) are Euclidean; \(A_1\) is \(\ell_1^2\); and \(B_{\sqrt2}\) has both the Ptolemy constant and squared Euclidean distance equal to \(2\). No computational certificate is needed.

Scientific limits: no uniqueness of the optimizing isomorphism is claimed, and no assertion is made outside the two parameter ranges. The 2010 renorming source was not available in full text during the literature check; its accessible publisher material was used only as supporting context, not to certify novelty.
