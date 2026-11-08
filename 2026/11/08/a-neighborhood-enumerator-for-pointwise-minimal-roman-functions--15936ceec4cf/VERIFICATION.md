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
# Verification record

The accompanying source `verify_roman_corona.py` implements direct exhaustive enumeration rather than relying on a recurrence or theorem-specific state restrictions. Roman feasibility is calculated from the actual adjacency sets of the corona. Each feasible function is subjected to every single decrement of a positive label; because feasibility is monotone in labels, this is equivalent to pointwise minimality. The program compares its full weight histogram with the subset formula on every labeled graph of order one through four and eleven more graphs on five vertices.

Observed result:

`VERIFY_OK graphs=86 labelings=1075446 minimal_functions=4370 full_polynomials=PASS extremal_weights=PASS independent_set_bridge=PASS bicliques=16`

The calculation additionally checks that the least occupied exponent is \(n+\gamma(H)\), the leading coefficient is the product of \(2^{|V(Q)|}+1\) over connected components, that the total count matches independent sets of the defined bipartite auxiliary graph for bases of order at most four, and that all 16 complete-bipartite formulas for \(1\le a,b\le4\) agree with the core-subset calculation.

The computation checks finite instances only. Unlimited order, arbitrarily disconnected graphs, and every complete-bipartite pair are justified by the proof in `RESULT.md`. Neither an independent audit nor a claim of exhaustive literature priority is implied by these calculations.
