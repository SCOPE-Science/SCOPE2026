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
# Reproduction and limits

The accompanying standard-library Python program `verify_odd_kneser_hom.py` constructs the bipartite middle-levels graph for \(k=2,3,4,5\) and verifies graph connectivity, cycle ranks, hook-length dimensions and rational character equality for all permutation cycle types in \(S_{2k+1}\) and both source-swap parities. Execute `python3 verify_odd_kneser_hom.py`; it prints the tested cycle-type counts and ranks. The predicted irreducible characters are independently evaluated by Frobenius's alternating-polynomial coefficient formula; the actual characters are computed from fixed graph cells, not from the proposed decomposition. The observed counts are 7, 15, 30, 56 cycle types and ranks 11, 71, 379, 1849 respectively.

The proof for every \(k\ge3\) is a mathematical argument and is not established by these finite tests. The known \(k=2\) case is a regression test only. The integer kernel representation is defined explicitly in the result and needs no unpublished package or external computation. It does not assert an integral Specht direct sum, a proof for general \(\operatorname{KG}(n,k)\), or independent mathematical validation.
