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

The proof in `RESULT.md` is universal. The attached checker stress-tests every admissible tuple
\[
1\le s\le20,\qquad1\le n,r\le12,\qquad1\le k\le6,
\]
and every \(|t|<s\) with \(\gcd(s,t)=1\). It checks that \(r+s-1\) is the first allowed summand count in the relevant residue class, that the obstruction differs by exactly \(s\), and that \(M_k\ge M_1\).

The finite replay is corroborative only. The universal theorem follows from the symbolic residue-class proof.
