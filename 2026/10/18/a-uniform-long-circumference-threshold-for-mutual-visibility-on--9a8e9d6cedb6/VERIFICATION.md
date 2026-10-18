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
# Verification instructions and limits

Run `python3 verify.py` in the directory containing that file. It requires only Python 3 standard-library modules. A successful run prints `PASS: 89 pairs (s,t), 26904 endpoint pairs, explicit routes and independent shortest-path BFS.`

The check covers \(3\le s\le10\) and \(6s\le t\le6s+9\), plus \(s\in\{12,16,20\}\) at \(t=6s,6s+1,6s+2\). For each pair of selected vertices it constructs the advertised gap-crossing or within-window route, verifies shortest path length using the Cartesian distance formula, checks every step is adjacent and every internal vertex unselected, and separately runs BFS on the graph with all other selected vertices removed. This is not a substitute for the stated infinite proof.

The exact hypotheses are \(s\ge3\), \(t\ge6s\). The proof of the lower bound uses \(h=\lfloor t/3\rfloor\ge2s\) and \(0\le r=t-3h\le2\) to make every chosen gap-crossing arc geodesic. Neither the proof nor the script certifies a sharp threshold or solves the remaining dimensions. Independent scientific audit was not performed.
