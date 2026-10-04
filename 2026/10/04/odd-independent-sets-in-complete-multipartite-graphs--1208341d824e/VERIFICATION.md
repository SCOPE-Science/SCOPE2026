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

The proof is exact and finite at each logical step: any nonempty independent set is confined to one part; same-part outside vertices see zero selected vertices; different-part vertices see the entire selected set. Thus the parity condition is equivalent to odd set size.

`verify.py` independently constructs adjacency matrices and checks the original definition rather than reusing the proof shortcut. It enumerates every complete-multipartite isomorphism type with at least two parts through order \(11\), all vertex subsets of each type, and compares the resulting size distribution and maximum with the claimed formulas.

Expected replay summary:

`ALL CHECKS PASSED; multipartite_types=183; subsets=177556; max_order=11`

The computation does not certify novelty and is not used to extrapolate the infinite statement. The theorem’s universal scope comes from the analytic proof.
