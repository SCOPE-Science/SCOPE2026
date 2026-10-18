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

# Reproducing the finite integral proof

Run `python3 checks/petersen_verify.py` with a standard Python 3 installation. No external packages, web access, proprietary programs, or saved intermediate files are needed.

The program independently enumerates face masks and undirected path forests and checks equality of all 10 cardinality counts. It checks the complete 59,203-vertex directed Hasse diagram for acyclicity (333,390 incidences), records 29,464 matched pairs, constructs every signed critical-to-critical differential, and verifies integer unit-pivot elimination leaves no nonzero block. It also verifies consecutive boundary compositions vanish and independently obtains identical reduced Betti ranks by direct mod-two elimination on the original simplicial complex.

The expected final output line is `VERIFIED_BIDIRECTED_PETERSEN_INTEGRAL_HOMOLOGY`; a record of the computed quantities appears in `checks/verification_output.txt`. The exact integer computation, rather than equality of mod-two and rational ranks alone, supports all-prime torsion-freeness. Acyclicity of the augmented matching gives an ordinary CW model by treating the vertex matched to the empty face as the critical base vertex.

These are finite deterministic, reproducible checks for the stated graph. They do not prove any infinite family statement or provide an independently performed mathematical audit. No complete wedge homotopy decomposition is asserted.
