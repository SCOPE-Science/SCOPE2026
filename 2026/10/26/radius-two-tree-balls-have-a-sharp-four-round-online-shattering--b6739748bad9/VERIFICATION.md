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

# Reproducible checks and their scope

The radius-two theorem for all finite trees has a direct geometric proof in RESULT.md. The finite computations are used only for the exact isomorphism-class census at order sixteen and explicit lower-bound certificates.

Run `python verify_pure.py` with `WITNESS.json` beside it. The standard-library program constructs every free tree through order sixteen, checking the complete list of known tree counts and using the AHU center-rooted canonical code to deduplicate leaf extensions. It directly evaluates all distinct closed radius-two balls and the full shattering recurrence on each of the 19,320 representatives, then verifies all four explicit complete decision trees.

Independently run `python verify_networkx.py` with NetworkX 3.x installed. It uses NetworkX's nonisomorphic-tree generator, shortest-path distances, a separate concept representation, and a separate exact recurrence. The output of both checks is preserved in `CHECKS.txt`.

Both computations return the dimension distribution 1, 7, 227, 18516, 569 for dimensions 0, 1, 2, 3, 4 respectively, totaling 19,320. The depth-four witness has sixteen distinct consistent root-to-leaf hypotheses. The original machine's execution output is not itself a proof of the universal theorem; each program and its mathematical completeness argument must be read to assess the finite census. No independent external audit has been performed.
