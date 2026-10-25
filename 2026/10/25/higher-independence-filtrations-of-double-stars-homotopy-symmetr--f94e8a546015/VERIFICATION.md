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

# Reproducibility and limitations

Run `python3 verify.py` in the directory containing this document; no nonstandard Python libraries are required. The supplied `verify_output.txt` records the completed result.

The verifier independently generates each labeled double-star graph from its edges, enumerates all induced vertex subsets and tests their largest connected component, constructs the associated simplicial complexes, and obtains reduced mod-two Betti numbers by augmented boundary ranks using exact binary arithmetic. It tests all \(1\le a,b\le3\) and all \(1\le r\le a+b+2\). It also enumerates every center-preserving automorphism in these ranges and every permitted center exchange, independently evaluates its signed invariant-face Lefschetz sum, and compares it against the predicted exterior-power cycle-character coefficient.

Recorded output: `VERIFY_OK configs=54 nonempty_faces=4174 signed_lefschetz_checks=892`.

These are exhaustive checks only **within the declared finite ranges**. They do not by themselves prove the infinite parameter theorem, integral torsion-freeness, or the integral lattice structure. Those conclusions follow from the simplicial decomposition, cofibration argument, and integral relative-chain proof in `RESULT.md`. No machine verification of every infinite case and no independent audit are claimed.
