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

The analytic proof reduces the claim to four exact identities after affine normalization:

1. The coefficients of \(|K+sL|\) give \(3V(K,K,L)=8(a_1a_2+a_1a_3+a_2a_3)\) and \(3V(K,L,L)=8(a_1+a_2+a_3)\).
2. For any two coordinate ratios, the omitted third ratio is their reciprocal product, so both inequalities defining \(\mathcal B_3(K,L)\) are equalities.
3. Weighted Cauchy--Schwarz and the coordinate half-space constraints identify \(M_0\) exactly as the box with half-lengths \(\sqrt{a_q}\).
4. Writing the half-lengths of \(M_1\) as \(\sqrt{a_q}\lambda_q\) makes both conjectural right sides identical to \(3V(M_0,M_0,M_1)\).

`artifacts/verify.py` uses exact rational arithmetic on representative choices \(a_q=s_q^2\) with \(s_1s_2s_3=1\). It checks all three generalized-radius choices and the corresponding mixed-volume identities, then prints `VERIFY_OK`. These finite checks are consistency tests only and do not replace the universal proof.

The proof does not address parallelotopes with different normal fans or arbitrary origin-symmetric convex bodies.
