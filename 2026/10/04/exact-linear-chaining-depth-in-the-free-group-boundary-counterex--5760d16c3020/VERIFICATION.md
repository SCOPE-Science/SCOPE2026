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

The claim was checked directly against the definitions and the full proof of Proposition 6.13 in arXiv:2609.18061v2.

The lower bound is source-backed: for the witness \(B_n=[a^{2n+2}]\), the paper proves that no \(n\)-chain from \(L\) reaches \(B_n\). The case \(n=0\) also follows directly because \(P(a,a)=0\), so \(L\cap[a^2]\) is empty.

The upper bound was reconstructed step by step. A positive legal cylinder beginning with \(ab\) lies in \(L\cap a^2L\): after applying \(a^{-2}\), its initial pair is \(a^{-1}b\), another positive transition in the source matrix. Nonsingularity preserves positivity of its translates, giving every consecutive overlap in
\[
L,\ a^2L,\ a^4L,\ldots,\ a^{2n+2}L.
\]
A positive legal cylinder beginning with \(b\), translated by \(a^{2n+2}\), lies in the final overlap with \(B_n\). Hence the displayed chain has exactly \(n+1\) links.

No numerical experiment or finite enumeration is used. The proof does not establish exact depths for other cylinders or other transition matrices. The originality comparison included the full source, predecessor work on weak double ergodicity, and targeted searches for equivalent exact-chain statements; absolute priority outside the inspected literature remains a residual risk.
