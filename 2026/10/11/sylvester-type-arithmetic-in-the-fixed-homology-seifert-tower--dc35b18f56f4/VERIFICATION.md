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

The verification is symbolic and uses the exact source operation.

1. At stage \(k\), the printed denominator is \(P_kH+1\). Since
\[
\gcd(H,P_kH+1)=1,
\]
the coefficient \(-H^2/(P_kH+1)\) is reduced, so the new exceptional-fiber order really is \(d_{k+1}=P_kH+1\).
2. The source proves \(H_1(Y_{k+1})\cong H_1(Y_k)\). Thus the same positive integer \(H\) is used at every stage.
3. Adjoining the new fiber changes the product of exceptional orders from \(P_k\) to \(P_{k+1}=P_kd_{k+1}\). Hence, with \(Q_k=HP_k\),
\[
Q_{k+1}=Q_k(Q_k+1).
\]
4. From \(P_k=P_0\prod_{j=1}^k d_j\),
\[
d_{k+1}=1+Q_0\prod_{j=1}^k d_j.
\]
Thus each later \(d_j\) is congruent to \(1\) modulo every earlier \(d_i\) and modulo every prime divisor of \(Q_0\), proving the stated coprimality.
5. Since \(Q_{k+1}=Q_k^2+Q_k>Q_k^2\), induction yields \(Q_k\ge Q_0^{2^k}\), and therefore \(d_{k+1}>Q_0^{2^k}\).

No computational search, finite enumeration, or timeout is used to establish the infinite result. The unproved limit is deliberately narrow: nothing here classifies different Seifert constructions that preserve the same first homology group.
