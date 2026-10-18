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

# Reproducibility of the two-landmark Hamming classification

Run `python3 checks/check_refinement.py` and `python3 checks/check_local_statistic.py`, in an environment with the Python 3 standard library. Each program generates its graphs from the displayed parameters and uses no external data or probabilistic hashing.

`check_refinement.py` independently builds graph edges for every \(q=3\) with \(1\le d\le6\), \(q=4\) with \(1\le d\le5\), \(q=5\) with \(1\le d\le4\), and \(q=6\) with \(1\le d\le3\), testing all anchor distances \(1\le b\le d\). It iterates injectively coded exact neighbourhood-colour multisets until stabilization. It checks that each resulting class exactly equals one \((s,r,t)\) set; checks the predicted number and sizes of classes; and checks stabilization by round \(d+1\). Expected final output includes `PASS cases=52 aggregate_vertices=16043 max_refinement_rounds=5`.

`check_local_statistic.py` independently constructs each possible single-coordinate neighbour, compares ordered distances from the two anchors, and verifies that precisely \(s\) neighbours lower both distances. It additionally tests that ordered pair distances together with this statistic recover the orbit label, and checks two explicit ternary-cube vertices with identical distance pairs but different local counts. Expected outputs include `PASS independent_distance_tests=52 aggregate_vertices=16043 distance_pair_ambiguous_cells=83` and `PASS explicit_ternary_cube_distance_collision: same_distances=(2,2), decrement_counts=(0,1)`.

The accompanying `.log` files contain the executions' recorded outputs. Both scripts were also executed after extraction from the completed package. Finite experiments do not establish the theorem for arbitrarily large dimensions or alphabets; the proof in `RESULT.md` provides that justification.
