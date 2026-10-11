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

# Exact computational verification

Run `python3 verify.py` with Python 3 standard library. It reconstructs the 15 vertices and graph adjacency; enumerates every face by the full 15-neighborhood union; verifies the entire 710-face set; creates 345 disjoint Morse pairs; checks the complete 2,430-arrow directed Hasse graph for acyclicity by a 710-face topological sort; derives all eleven signed oriented-simplex traces; checks Murnaghan–Nakayama irreducible character orthogonality; and recovers the two exact unit multiplicities. Output ends with `verified`.

Run `python3 check_independent.py` with Python 3 and SymPy. This independent route evaluates all 32,767 nonempty candidate duad subsets with the exact endpoint-support predicate. Finite-field boundary elimination gives augmented \(d_0\) rank 1 and other boundary ranks \((14,91,150,75,15)\) in each characteristic two, three, and five. The sole nonzero reduced Betti number is nineteen in dimension two. A separate fixed-face signed trace calculation produces the same eleven rational Lefschetz values, and the irreducible-character table is obtained using Kostka matrices and Young permutation characters (not Murnaghan–Nakayama). Output ends with `Independent check complete`.

Both source files were executed successfully from their actual package source paths and can be rerun without any other embedded file. The character formula uses rational coefficients and does not claim that modular checks independently certify integral torsion-freeness. The original domain is finite; no computation is extrapolated to general parameters or infinite families. The pre-existing ordinary homotopy wedge count is explicitly not claimed as a new result.
