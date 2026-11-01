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

# Reproducibility and verification

Run `python3 verify_kneser.py` with Python 3 and no third-party packages. The embedded `verification_output.txt` records the exact successful output. The checker independently constructs all simplices of the actual neighborhood complex by subsets of allowable support, computes equivariant signed traces of oriented simplex chains, then computes the same traces from fixed chains in the rank-selected Boolean poset. The two calculations are genuinely separate finite constructions, although both test the same topological model.

Every ground-set permutation is checked for \(n=4,5,6\); the identity, one transposition, a full cycle, and a three-cycle are checked for \(n=7\). Exact crown connectivity and graph cycle-rank calculations agree with predicted ranks. Calculated nonempty-face counts are \(6,50,710,17724\) and homology ranks are \(5,11,19,29\), respectively. Finite checks cannot establish the theorem at larger sizes; the uniform proof in `RESULT.md` supplies the general argument, including the necessary integral saturation statement. The symmetry-module identification is subject to later independent mathematical audit.
