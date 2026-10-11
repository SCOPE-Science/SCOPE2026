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

The direct source check located Theorem 5 in the full 2017 article and confirmed that its proof uses a lower estimate for \(\|Tx\|\) based only on \(\|T\|\). That step is invalid for a general bounded operator.

The counterexample was checked symbolically with \(H=\mathbb R^2\), \(K=I\), \(\Lambda_1=I\), and \(T=\operatorname{diag}(1,0)\). The original family is Parseval and the commutation hypothesis holds, while \(\|\Lambda_1Te_2\|=0\) and \(\|K^*e_2\|=1\).

For the repaired theorem, the sufficient direction uses only the assumed inequality \(\|Tx\|\ge m\|x\|\) on \(R(K^*)\), the commutation relation, and the original frame bounds. The necessary direction tests universal preservation on \(\Lambda_1=K^*\), which is a \(K\)-\(g\)-frame with lower bound \(1\). The resulting lower frame inequality is exactly a lower bound for \(T\) on \(R(K^*)\).

No numerical experiment, finite enumeration, closed-range assumption, or external certification is used. The conclusion is limited to the commuting case and to the universal preservation property stated in the finding.
