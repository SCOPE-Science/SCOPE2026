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

The proof has one source-backed ingredient and one elementary bridge. Balbiani--Fernández-Duque--Herzig--Iliev Theorem 6.1 supplies the universal lower bound on modal complexity for \((m,n)\)-transfer. The bridge specializes to \(m=2^q,n=1\) and represents exact \(2^q\)-step reachability by repeated first-order squaring.

Run `python3 artifacts/verify.py`. The script exhausts all directed frames on one, two, and three vertices, allowing loops. It checks that recursively squaring the relation gives exactly \(R^{2^q}\) for \(q\le4\), and for \(q=1,\ldots,4\) it exhausts all propositional valuations to verify that \(\Diamond^{2^q}p\to\Diamond p\) is frame-valid exactly when \(R^{2^q}\subseteq R\). It also checks the rank/depth arithmetic through \(q=24\).

Expected output:

`VERIFY_OK 4818 exact assertions`

The script does not attempt to enumerate all modal formulas and therefore does not independently prove the minimal-depth lower bound; that is the cited theorem.
