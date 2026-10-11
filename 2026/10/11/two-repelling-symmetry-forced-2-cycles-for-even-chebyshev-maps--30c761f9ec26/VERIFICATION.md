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

The proof is analytic. The packaged `verify.py` replays the algebraic steps that are easiest to mistranscribe:

- the identity converting \(Q_n(x)=-x\) to \(E_n(x^n)=0\);
- the cubic discriminant \(4n^6(n+1)(4n^2-63n-59)\);
- the multiplier test polynomial \(H_n\);
- the exact resultant of \(E_n\) and \(H_n\);
- the rational \(n=18\) bracket \(1/28<y_+<1/27\);
- exact positivity values used to anchor the outer multiplier; and
- the derivative-chain certificate that the resultant's quartic factor stays positive for \(n\ge18\).

Running `python verify.py` with the dependency in `requirements.txt` returns `VERIFY_OK`.

The verifier does not prove the logical steps that use Descartes' rule, continuity of simple ordered roots, or the invariant-line conjugacy; those are supplied explicitly in `RESULT.md`. No finite experiment is used to infer an infinite statement, and no numerical orbit iteration is part of the proof.
