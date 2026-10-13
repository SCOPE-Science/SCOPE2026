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

The claim is verified by symbolic proof rather than computation.

1. The primary source was checked in full text for the definition of \(I_{\mathrm{ref}}(A)\), Example 3.15, Theorem 5.5, and the statement that every reflexive module is a second syzygy.
2. For a hereditary algebra, every second syzygy is projective, so \(\operatorname{ref} A=\operatorname{proj} A\).
3. For a simple projective \(S\), \(\operatorname{Hom}_A(S,A)\ne0\).
4. For a simple nonprojective \(S\), use \(0\to P_1\to P_0\to S\to0\). If \(\operatorname{Ext}^1_A(S,A)=0\), every map \(P_1\to A\) extends to \(P_0\). Extending the coordinate maps of a split embedding \(P_1\to A^m\) produces a retraction \(P_0\to P_1\), so the sequence splits and \(S\) is projective, contradiction.
5. Therefore every simple index lies in \(I_{\mathrm{ref}}(A)\). Theorem 5.5 then forces any reflexively equivalent algebra to be Morita equivalent.

No finite experiment, database absence, or computational log is used as a correctness premise. The literature searches are used only for originality comparison.
