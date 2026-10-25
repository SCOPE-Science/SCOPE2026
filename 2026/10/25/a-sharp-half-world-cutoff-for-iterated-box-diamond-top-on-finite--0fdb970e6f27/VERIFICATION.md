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

Run `python3 checker.py` using Python 3 and no third-party dependencies. The checker independently evaluates recursive \(\Box\Diamond\) semantics on selected finite relations, computes exact stage sets by bitmasks, and tests the structural invariant \(T_i\cap U_j=\varnothing\) at all computed stages. It exhaustively enumerates 2, 16, 512 and 65,536 directed relations for 1, 2, 3 and 4 labelled worlds respectively. It also samples 35,000 larger frames using a stated pseudorandom seed and checks the directed-path witness family through 80 worlds.

The actual replay emitted `FULL_CENSUS {1: {0: 2}, 2: {0: 12, 1: 4}, 3: {0: 374, 1: 138}, 4: {0: 52056, 1: 12712, 2: 768}}`, followed by `PATH_SHARPNESS_N1_TO_80 OK`, `RANDOM_FRAMES_N5_6_9 35000 OK`, `RECURSIVE_SEMANTICS_AND_TWO_SIDED_DISJOINTNESS OK`, and `ALL_CHECKS_OK`.

The count for five or more worlds is **not** exhaustive. Finite experiments do not prove an all-size theorem. The result instead follows from the induction and counting argument in `RESULT.md`, which uses no unverified computation or external lemma. No independent audit has been performed.
