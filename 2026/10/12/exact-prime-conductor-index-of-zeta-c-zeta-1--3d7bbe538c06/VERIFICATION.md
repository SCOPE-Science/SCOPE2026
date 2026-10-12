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

The proof in `RESULT.md` is the verification of the infinite statement. Its critical steps are:

1. For \(a\neq b\), the exact identity
   \[
   u_a-u_b=(\zeta^a-\zeta^b)(1-c\zeta^{-a-b})
   \]
   shows that a conjugate collision at odd prime conductor with integer \(c\) forces \(c=1\).
2. Since \(\mathcal O_{\mathbb Q(\zeta)}=\mathbb Z[\zeta]\), the discriminant-index identity converts the quotient of Vandermonde discriminants into the product of the factors \(1-c\zeta^{-a-b}\).
3. Unordered pair sums in \(\mathbb F_p^\times\) occur \((p-1)/2\) times at sum zero and \((p-3)/2\) times at each nonzero sum.
4. The product \(\prod_{t=1}^{p-1}(1-c\zeta^t)=(1-c^p)/(1-c)\) gives the closed index formula.
5. The integer equation making that index equal to one gives the stated classification, with \(p=3\) treated separately.

`verify.py` performs bounded consistency checks of pair-sum counts, the index-one arithmetic classification, and representative numerical Vandermonde quotients. These finite checks do not prove the universal quantifiers and are not used to infer novelty.

Unproved limits: no composite-conductor analogue and no nonintegral-parameter analogue are claimed. Independent audit has not been performed.
