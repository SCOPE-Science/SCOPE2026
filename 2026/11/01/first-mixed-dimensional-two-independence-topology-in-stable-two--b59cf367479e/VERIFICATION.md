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

Execute `python3 verify_stable_kneser_two_independence.py` with Python 3.10 or later. The checker needs no third-party packages and asserts the complete finite Morse and integral certificate for `SG(2,k)`, `0<=k<=6`.

It constructs the stable two-subset graph from the cyclic-polygon rule; enumerates faces by a proven complete increasing-index recursion; matches all possible face pairs in the embedded explicit orders; confirms acyclicity by a full directed-Hasse topological sort; reconstructs signed integral Morse differentials from recursive gradient-path expansions; verifies consecutive differentials compose to zero; and certifies the integral invariant factors using unimodular row/column operations at unit pivots. An independent mod-two reduction of the original simplicial boundaries checks the resulting Betti ranks.

Actual output of the saved checker is provided as `verification_output.txt`. Its final marker is `STABLE_KNESER_TWO_INDEPENDENCE_TRANSITION_VERIFIED`. This verifies only the finite cases explicitly named; it is not a proof of any untested infinite continuation. The geometric wedge conclusion uses the mathematical Hurewicz/cellular-attachment argument in `RESULT.md`.

Independent audit has not been performed.
