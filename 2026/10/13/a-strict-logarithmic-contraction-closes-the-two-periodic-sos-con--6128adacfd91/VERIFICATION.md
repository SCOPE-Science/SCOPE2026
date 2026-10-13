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

The analytic proof uses the exact scalar map stated in the source on its invariant set \(I\). The critical algebraic checks are:

1. \(N'Q-NQ'=-2(\theta^2-1)P\), with \(P>0\) on the positive domain.
2. \(NQ-2u(\theta^2-1)P=R\), where every monomial coefficient of \(R\) displayed in `RESULT.md` is positive.
3. For \(\theta>1\), these identities imply \(-1<g'(x)<0\) for \(g(x)=\log f(e^x)\).
4. A nontrivial two-cycle would force \(1=-g'(\xi)\) at an intermediate point by the mean value theorem, contradicting item 3.

`verify.py` uses exact rational arithmetic to check both algebraic identities on a deterministic test family and to replay representative sign inequalities. These tests are supplemental; universal correctness rests on the explicit symbolic identities and positivity argument.

The claim is restricted to the invariant set \(I\). No independent audit has been performed.
