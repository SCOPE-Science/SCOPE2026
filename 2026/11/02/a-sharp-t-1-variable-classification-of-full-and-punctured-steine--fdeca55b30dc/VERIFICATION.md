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

# Reproducible checks and proof boundaries

The classification is proved by the five mathematical steps in `RESULT.md`, not by computation. In particular, the proof relies on the following two identities for a punctured \(S(t,t+1,v)\), where \(A\) is a distinct surviving \(t\)-set:

* If \(A\) is missing, the \(v-t-1\) outside points all leave exactly one missing \(t\)-subset and make no surviving block.
* If \(A\) is covered, the numbers of outside points producing, respectively, a surviving block, exactly one missing \(t\)-subset, or neither are \(1\), \(t\), and \(v-2t-2\).

Run the two Python 3 standard-library scripts in the same directory:

```sh
python local_extension_checker.py
python pebble_fixedpoint_checker.py
```

`local_extension_checker.py` constructs full Steiner systems of strengths two and three, exhaustively verifies the defining Steiner covering property for its test systems, and tests every single-point deletion. It checks all 8,757 possible distinct anchor cases across 50 deletions. The expected output is `local_extension_output.json`.

`pebble_fixedpoint_checker.py` computes exact stabilized counting-free \(k\)-variable types of tuples on the selected finite test systems, through the fixed point of the single-coordinate replacement relation. It checks 73,683 four-variable tuples in the quadruple-system tests and 1,071 three-variable tuples in the triple-system tests. Its fixed points stabilize after five and three rounds respectively. It checks the predicted full-versus-punctured and small-versus-large equivalences and separations. The expected output is `pebble_fixedpoint_output.json`.

The scripts do not enumerate every Steiner system of a given order or all values of \(t\); their finite conclusions cannot by themselves prove unrestricted quantifier-depth equivalence. The unrestricted statements follow from the permanent pebble strategies in the mathematical proof. No independent audit has been performed.
