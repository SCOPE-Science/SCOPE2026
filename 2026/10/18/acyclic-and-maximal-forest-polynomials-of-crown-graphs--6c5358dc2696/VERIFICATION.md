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

# Verification and scope

The attached program `verify_crown_forests.py` uses standard Python modules only. Run `python verify_crown_forests.py` from the folder containing the script; it prints the independently computed induced-forest and maximal-forest totals by graph order and finishes with `VERIFICATION_OK`. The full output generated in this instance appears in `verification_output.txt`.

The program independently enumerates every induced subgraph of \(H_n\) for \(3\le n\le9\), testing for cycles using the disjoint-set union algorithm on actual graph edges, and tests maximality by examining all omitted vertices. It counts left-side and right-side occupancies separately and asserts equality with the theorem's bivariate formulas. In total it examines exactly \(349{,}504\) subsets. These tests validate all recorded coefficients in the finite tested range and are independent of the structural classification; they do not constitute an exhaustive infinite proof.

The infinite theorem is justified by the induced edge identity \(ab-t\), the necessary forest edge bound \((a-1)(b-1)\le t\le\min(a,b)\), direct sufficiency checks for the surviving small profiles, and complete one-vertex-extension arguments. Cases \(n=3\) and \(n=4\) are separated from the nonpure regime. There are no numerical optimizations or external datasets on which the theorem depends.

Independent scientific audit has not been performed.
