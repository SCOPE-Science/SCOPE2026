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
# Reproducibility and verification

Execute `python3 verify.py` with standard Python 3.9 or later. The complete checker separately derives antichain conditions from the original coordinatewise order, verifies every possible orbit simplex up to dimension two for chains \(1\le n\le16\), computes mod-two boundary ranks, and tests every orbit subset for all 19 labeled partial orders on three elements. The observed pass totals are 83,572 chain cases and 9,728 general-poset cases.

These finite checks cannot establish the all-\(Q\) statement or integral all-\(n\) homology. Those derive from the orbit-barycenter PL construction and the exact integral long-exact-sequence argument; crucially, the link-cycle image is a primitive sublattice of the fundamental-cycle lattice of a graph. Direct independent mathematical validation has not been performed. No external audit evidence is asserted.
