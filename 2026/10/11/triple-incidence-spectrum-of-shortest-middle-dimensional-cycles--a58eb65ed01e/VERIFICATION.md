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

`verify.py` reconstructs the complex solely from the fourteen published facet-orbit representatives and the two published permutation generators. It checks group order, every facet-orbit size, the complete f-vector, and complement-of-facet equality for the 490 missing six-sets.

The binary chain calculation uses exact integer bit vectors. It verifies ranks \(1001\) and \(2001\) for the relevant boundary maps and hence \(\dim H_4(K;\mathbf F_2)=1\). Each missing-six-set boundary is reduced against the exact \(5\)-boundary span and is nonzero.

The support-minimality step is mathematical rather than enumerative: a nonzero simplicial \(4\)-cycle needs at least six vertices, and on six vertices the cycle equations force the full boundary of the \(5\)-simplex. Because all five-subsets are faces, the 490 missing six-sets are exactly the minimum-support nonzero cycles.

The program then exhausts all block incidences. It checks uniform vertex multiplicity \(196\), uniform pair multiplicity \(70\), the complete triple spectrum, the five minimum triples, their disjoint union of all fifteen vertices, invariance under the generated group, and transitivity on the five triples.

Limit: the verifier certifies this labeled complex and mod-two claim only. It does not search other fifteen-vertex triangulations or certify literature originality.
