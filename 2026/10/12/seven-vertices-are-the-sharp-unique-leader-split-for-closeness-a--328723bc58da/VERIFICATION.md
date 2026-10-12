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
The embedded `verify_closeness_harmonic_boundary.py` performs an exact finite replay using only the Python standard library and the embedded connected Graph Atlas table.

For every connected Atlas graph through seven vertices, all-pairs shortest-path distances are computed independently by breadth-first search and Floyd--Warshall and must agree.

Classical closeness maximizers are obtained by minimizing exact integer farness
\\[
F(v)=\\sum_{u\\ne v}d(u,v),
\\]
while harmonic scores are exact rational sums
\\[
H(v)=\\sum_{u\\ne v}\\frac1{d(u,v)}.
\\]

The replay verifies:
- connected unlabeled counts \\(1,2,6,21,112,853\\);
- maximizing-set disagreement counts \\(0,0,0,0,3,22\\) for orders \\(2,\\ldots,7\\);
- distinct singleton disagreement counts \\(0,0,0,0,0,2\\);
- the two displayed seven-vertex representatives;
- the common distance profiles \\((1,1,2,2,2,3)\\) and \\((1,1,1,2,3,4)\\);
- exact competing scores \\((11,23/6)\\) and \\((12,49/12)\\);
- seven-vertex orbit sizes \\(2520,2520\\), totaling \\(5040\\);
- six-vertex tie-level orbit sizes \\(360,180,360\\), totaling \\(900\\).

Run:

`python3 verify_closeness_harmonic_boundary.py`

The first output line must be:

`VERIFY_OK`

The graph list is a compact connected subset of the documented Read--Wilson Graph Atlas through seven vertices.
