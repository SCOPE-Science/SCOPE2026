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

The mathematical argument covers all integers \(d\geq1\), \(q\geq2\) and every choice of root. The binary upper bound groups adjacent vertices into pairs that lie on one root-to-farther geodesic; the binary lower bound constructs a diameter geodesic visiting only two consecutive distance layers. For nonbinary alphabets, the diameter geodesic stays entirely in the farthest sphere. These are finite structural arguments valid uniformly, not inductive extrapolations from calculations.

The standalone reproducibility command is `python3 verify.py` (Python 3 standard library only). It enumerates all shortest paths in the specified small Hamming graphs and solves exact rooted-path set cover using a subset dynamic program. Expected last output line: `VERIFY_OK`. The provided `verification_output.txt` records detailed histograms and 7,210 tested geodesic vertex sets. The script covers only the ten listed parameter pairs and does not prove untested dimensions or alphabet sizes.

The graphs are vertex-transitive; enumerating a root at the all-zero word does not lose other root cases. No external independent validation or formal proof-assistant certification was performed.
