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

The accompanying `power_dual_verify.py` uses only the Python 3 standard library. It independently constructs the two graphs from their edge descriptions (the dodecahedral graph has \(20\) vertices, \(30\) edges, degree \(3\); the icosahedral graph has \(12\) vertices, \(30\) edges, degree \(5\)). It checks that no singleton succeeds. Each of the \(190\) dodecahedral and \(66\) icosahedral pairs is tested twice, using set differences and bitwise masks for the simultaneous propagation rule. Independent BFS calculations give all base-graph distances and the full minimum-set exchange distances.

The verified per-distance wave-size sequences are \(D: (6), (7,10), (8,10,14,18,20), (8), (8)\) for distances \(1,2,3,4,5\), and \(I: (8,10,12), (10,12), (12)\) for distances \(1,2,3\). Thus exactly \(60\) dodecahedral pairs and all \(66\) icosahedral pairs work. The complete exchange distributions are \(D: (300,870,600)\) and \(I: (660,1485)\).

Run `python3 power_dual_verify.py` after extracting the package. Expected final line: `VERIFY_OK`.

The observation-round index starts after the initial closed-neighborhood observation; papers that count the initial observation as round one give round counts larger by one. No claims are made about larger graph families, physical robustness, independent peer review, or absence of unindexed prior work.
