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

The primary theorem was checked in Reider's full article: in the exceptional dimension-one case it gives \(K_X\sim2E_\xi\), \(q=2\), \(K_X^2=\tfrac23c_2\), and a smooth irreducible \(E_\xi\) with split normal sequence. The article also records Noether's formula \(K_X^2+c_2=12\chi(\mathcal O_X)\).

From these premises the proof is exact: integrality yields \(5\mid\chi(\mathcal O_X)\); adjunction yields \(g(E_\xi)=9m+1\) and \(N_{E_\xi/X}^{\otimes3}\cong K_{E_\xi}\); compact-Kähler identities yield the stated Hodge and intersection ranks.

`verify.py` checks the formal coefficient identities rather than testing finitely many surfaces. The stored output is `verification_output.txt` and ends with `VERIFY_OK`. The checker does not independently prove the primary source theorem or establish existence of any exceptional surface.
