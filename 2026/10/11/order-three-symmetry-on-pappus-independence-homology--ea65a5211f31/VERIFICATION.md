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

Run `python3 verify_pappus_c3.py` from the package directory. The script requires only the Python standard library.

It reconstructs the standard Pappus graph from \([5,7,-7,7,-7,-5]^3\), verifies \(18\) vertices, \(27\) edges, and cubic degree, and enumerates all \(2597\) nonempty independent sets. It checks the complete discrete-Morse certificate: \(1293\) matched Hasse covers, \(11430\) total nontrivial Hasse covers, acyclicity of the full Forman orientation, and critical-cell profile consisting of one \(0\)-cell and ten \(4\)-cells.

As a separate chain-level check, the script constructs every simplicial boundary matrix and computes its exact rank over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). Each coefficient field gives Betti vector \((1,0,0,0,10,0,0,0,0)\).

For the automorphism \(r(i)=i+6\pmod{18}\), the script checks the graph edge set is invariant under \(r\) and \(r^2\). It then evaluates the signed trace on every simplicial chain group by enumerating all setwise fixed oriented simplices. The chain traces are \((18,126,438,801,756,348,90,18,2)\) for the identity and \((0,0,6,0,0,9,0,0,2)\) for each nonidentity element. Thus the Lefschetz numbers are \((11,-1,-1)\), and after subtracting the trace-one connected \(H_0\), the \(H_4\)-character is \((10,-2,-2)\). The final two linear character equations are checked explicitly and give two trivial plus four two-dimensional cyclotomic summands.

The computation is exhaustive for this finite graph and this specified subgroup. It does not compute the full automorphism-group representation or the integral \(\mathbb Z[C_3]\)-module structure.
