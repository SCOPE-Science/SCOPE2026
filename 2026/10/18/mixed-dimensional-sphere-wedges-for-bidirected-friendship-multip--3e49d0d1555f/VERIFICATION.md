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

# Reproducible checks and scope

`verify.py` implements face generation directly from allowable center arcs and independent outer-arc choices; it checks every generated face against indegree, outdegree and cycle constraints. It constructs the explicit lexicographic discrete-Morse involution, confirms every pair is a cover, and topologically sorts the complete reversed-matching Hasse digraph to certify acyclicity for each integer \(1\le n\le6\). At \(n=6\) it enumerates 54,188 nonempty simplices, 27,087 matched pairs, and 295,128 Hasse covers. It also checks the distinguished top facets have no cofaces. See `verify_output.txt`.

`homology_check.py` separately constructs all faces by increasing subsets of arcs (without calling the other program), and computes exact mod-two boundary ranks for \(1\le n\le5\). The reduced positive-degree Betti numbers agree with the predicted rank one in degree \(n-1\) and rank \(2n\) in degree \(n\). See `homology_output.txt`.

Run both with `python3 verify.py` and `python3 homology_check.py` in the artifact directory. Python 3 and the standard library suffice. The finite calculations are exhaustive only in the listed sizes. Integer homotopy for all sizes is proved analytically in `RESULT.md` via a fiberwise acyclic matching, explicit integral join cycles, and nullhomotopic attaching maps; mod-two checks alone do not establish integer torsion-freeness or the infinite claim.
