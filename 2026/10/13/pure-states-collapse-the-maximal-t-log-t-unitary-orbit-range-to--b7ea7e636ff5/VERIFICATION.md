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

The finding is proved analytically; no finite experiment is used as an infinite proof.

For distinct rank-one projectors \(P,Q\), set \(c=\operatorname{Tr}(PQ)\). Then \(0\le c<1\). The two-outcome measurement \(\{Q,I-Q\}\) maps \(P\) to \((c,1-c)\) and \(Q\) to \((1,0)\). The classical divergence for \(f(t)=t\log t\) is \(+\infty\) because its second reference mass is zero while \(1-c>0\). Data processing for maximal quantum \(f\)-divergence gives the same lower bound in the quantum problem, hence the quantum divergence is \(+\infty\). Equal projectors give \(0\).

The source's Corollary 3.3 was checked in the public full text: it is stated for arbitrary quantum states and asserts the entire interval between spectral endpoints. Its proof explicitly uses continuity of the orbit objective. The singular extension in the same source is by epsilon regularization. Foundational literature was checked for the monotonicity and singular extended-value premises.

Limits: this verifies the rank-one \(t\log t\) counterexample and the failure of the all-state interval conclusion. It does not classify all singular states or claim that the source's extremal-value formulas fail in this example.
