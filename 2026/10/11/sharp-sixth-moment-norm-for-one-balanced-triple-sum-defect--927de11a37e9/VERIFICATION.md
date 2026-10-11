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

The proof in `RESULT.md` is analytic. The bundled `verify.py` is a standalone corroborative checker using only the Python standard library. It performs four exact checks:

1. it enumerates every size-three multiset of \(\{0,1,4,9\}\) and confirms that the sole repeated sum is \(0+0+9=1+4+4\);
2. it reconstructs the sixth moment by direct cubic convolution for several integer coefficient vectors and compares it with the closed Parseval formula;
3. it checks in the quadratic field \(\mathbb Q(\sqrt{97})\) that \(p_*=(\sqrt{97}-5)/9\) solves \(9p^2+10p-8=0\);
4. it checks exactly that the reduced cubic at \(p_*\) equals \((97\sqrt{97}-260)/162\).

Run `python3 verify.py`. The expected terminal line is `VERIFY_OK collisions=1 algebra=exact convolution_cases=5`. No finite test is used to infer the general theorem or the literature comparison.
