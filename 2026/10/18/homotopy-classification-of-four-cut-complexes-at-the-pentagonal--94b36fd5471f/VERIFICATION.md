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

# Verification information
The complete argument is in `RESULT.md`. The standard-library program `checks/check_girth5_cut.py` can be run with `python3 checks/check_girth5_cut.py` from the package root. It reconstructs all tested graph edges from definitions, enumerates the dual complex's possible faces of sizes four, five, and six, checks induced-pentagon classification and the degree-based connected-four-set formula, constructs actual mod-two boundary columns, and independently replays legal elementary simplicial collapses. `checks/check_output.txt` contains the recorded deterministic output.

Representative exact checks: on the Petersen graph the connected-four-set count is 70 and pentagon count is 12; mod-two ranks of the 3- and 4-boundary operators are 58 and 12; 58 remaining tetrahedra collapse along free triangles; the predicted four-cut sphere rank is 26. On the dodecahedron the respective values are 140, 12, 128, 12, 128, and 841. Cycles, Heawood, a disconnected graph, and two graphs with pentagons sharing one or two edges furnish additional tests.

The computation does not establish the theorem for infinitely many graphs, does not prove the final nonequivariant Whitehead step, and does not constitute an independent mathematical audit. The generic free-face, Alexander-dual, and Hurewicz/Whitehead arguments in `RESULT.md` supply those deductive steps. No external code dependencies are required beyond the Python standard library.
