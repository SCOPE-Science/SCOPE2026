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

`verify.py` reconstructs the numerical part of the claim from exact rational inputs. It implements rigorous intervals for natural logarithms by powers-of-two range reduction followed by the positive atanh series, with an explicit geometric tail bound. Binary entropy intervals are then formed using directed rational bounds.

The script checks the exact parameters \(p=1/2\), \(q=39/200\), and \(t=4/299\); forms a lower bound on Bob's exact mutual information and upper bounds on Eve's two coin-information branches; and verifies that their difference is strictly larger than \(0.0002101\). It also bounds the published value \(3\ln2/10927\) from above and verifies the new lower endpoint is more than \(1.1\) times that upper endpoint.

The finite computation is only a rigorous evaluation of transcendental expressions already derived analytically. It does not search over all protocols or establish optimality of the chosen rational parameters.
