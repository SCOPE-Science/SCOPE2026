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
# Verification

The standalone program `verify_cuboctahedron_rips.py` reconstructs the twelve points from the coordinate definition and verifies that the nonzero squared pairwise distances are exactly \(2,4,6,8\). It enumerates every nonempty subset of the twelve vertices and retains exactly the Vietoris--Rips simplices at each threshold.

At squared threshold \(2\), it verifies face vector \((12,24,8)\), maximal simplices equal to the eight triangular faces, mod-two boundary ranks \((11,8)\), Betti vector \((1,5,0)\), and an acyclic Morse matching with one critical \(0\)-cell and five critical \(1\)-cells.

At squared threshold \(4\), it verifies face vector \((12,36,32,6)\), maximal simplices equal to the eight triangular and six square face vertex sets, ranks \((11,25,6)\), Betti vector \((1,0,1,0)\), and an acyclic Morse matching with one critical \(0\)-cell and one critical \(2\)-cell.

At squared threshold \(6\), it verifies that the only absent pairs are the six antipodal pairs and that every maximal simplex chooses one vertex from each pair. It obtains face vector \((12,60,160,240,192,64)\), ranks \((11,49,111,129,63)\), Betti vector \((1,0,0,0,0,1)\), and an acyclic Morse matching with one critical \(0\)-cell and one critical \(5\)-cell.

At squared threshold \(8\), it verifies the full simplex on twelve vertices. The executable check ends with `VERIFY_OK`.

The program verifies the finite combinatorial inputs. The homotopy identifications at squared thresholds \(2\) and \(4\) additionally use the nerve arguments stated in `RESULT.md`; at squared threshold \(6\), the join description is direct from the antipodal-pair classification. No claim is made about untested point sets or an infinite family.
