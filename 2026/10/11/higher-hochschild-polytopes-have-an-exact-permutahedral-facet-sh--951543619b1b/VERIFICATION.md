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
The theorem is proved symbolically in `RESULT.md`.

Critical checks:
- the affine total is \(\binom{d+1}{2}\);
- the source tight value is \(z_J=\binom{u+1}{2}+b\);
- the doubled uniform-center slack is \(s(d-s)+b(s+u-1)\);
- the intrinsic subset-normal squared norm is \(s(d-s)/d\);
- the exact shell formula follows by division;
- the correction term is nonnegative;
- \(s(d-s)\ge d-1\), with equality only for \(s=1\) or \(s=d-1\);
- singleton inequalities give the matching universal upper bound and force the center uniquely;
- equality among tight subset inequalities occurs exactly for singletons, or for co-singletons with \(b=0\).

`verify.py` enumerates all nonempty proper subsets for \(2\le m\le7\) and \(1\le n\le7\), verifies the algebraic slack identity and squared distance formula with exact rational arithmetic, and checks the complete equality classification. Finite computation is corroborative only and does not assess originality.
