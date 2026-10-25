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
# Verification and reproducibility

`VERIFY.py` runs under Python 3 with only the standard library. Execute `python VERIFY.py` in a directory containing the script. The included `VERIFY_output.txt` records the complete stdout of a successful run.

The program independently constructs maximal simplices of \(N_r(X_{n,k})\), lists all nonempty subfaces, and computes reduced mod-two homology from explicit simplicial boundary matrices. For all \(3\le n\le7\), \(2\le k<n\), and \(r\in\{2,k,k+1,k+2\}\), it compares every degree to the predicted contractible or sphere-wedge reduced Betti vector. For \(n\le4\), it additionally enumerates every vertex subset directly against intersections of actual finite-Alexandrov minimal open neighborhoods, without using the facet criterion under test. For each tested case and each permutation cycle type, it computes the signed reduced simplicial Lefschetz number and compares with the exterior-power character formula.

Recorded stdout:
```
FINITE_NEIGHBORHOOD_CASES 60
TOTAL_ENUMERATED_NONEMPTY_FACES 15318
LITERAL_TOPOLOGY_COMPARISONS 12
SIGNED_EQUIVARIANT_LEFSCHETZ_CHECKS 612
VERIFY_OK
```

The independent finite computations establish no all-size theorem, cannot by themselves certify integral torsion absence, and do not establish historical originality. The geometric and integral chain proofs in RESULT.md address the infinite statement. Independent scientific audit and verification have not been performed.
