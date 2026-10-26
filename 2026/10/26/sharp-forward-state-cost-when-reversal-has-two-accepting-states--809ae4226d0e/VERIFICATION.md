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

# Reproducibility

Execute `python3 verify.py` from the directory containing the provided file. Standard-library Python 3 is sufficient.

The program constructs the edge-action automaton for every integer \(m\) from 2 through 12, checks forward reachability, checks the forward minimal-DFA state count through an independent partition-refinement algorithm, builds all reachable reverse subset states from first principles, and checks reverse minimality and exactly two reverse final states. It also verifies that the reachable reverse states are precisely the vertex-stars.

For the finite cases \(m=2,3\), the program exhausts ordered pairs of permutation-letter actions on all state sets smaller than the asserted optimum, including every possible size-\(m\) accepting set with initial state fixed by relabeling. For every such reachable and minimal forward automaton it verifies that the reverse minimal automaton does not have two final states. This is a bounded check, not a proof for larger parameters.

Expected last line: `VERIFY_OK`. The uniform theorem rests on the combinatorial orbit-incidence proof in RESULT.md; no full-group enumeration or external certificate is assumed. Independent external review is not recorded.
