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

The proof uses two exact local models. First, after fixing the marked double line, the relative quadric is \(d^2-4ce=0\), whose singular locus is exactly \(c=d=e=0\). This gives the rank-two kernel projective bundle and, together with the hypersurface Serre criterion, normality.

Second, a nearby second line \(m=x+\beta y+\gamma z\) gives projective coordinates \([2\beta:2\gamma:\beta^2:2\beta\gamma:\gamma^2]\). The two blow-up charts extend this map across \(\beta=\gamma=0\) as \([2:2t:s:2st:st^2]\) and \([2t:2:st^2:2st:s]\), and the overlap is projectively identical. Their exceptional loci map exactly to \(c=d=e=0\).

`verify_target.py` checks these identities using exact integer polynomial arithmetic and returns `VERIFY_OK` when every check succeeds.

Limits: the verifier certifies the local formulas, not the general theorems that proper plus quasi-finite implies finite or Serre's criterion for normality. Those are standard algebraic-geometric deductions used explicitly in the proof.
