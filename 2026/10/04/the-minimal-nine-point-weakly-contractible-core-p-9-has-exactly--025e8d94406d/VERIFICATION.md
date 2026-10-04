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

The verifier `verify.py` reconstructs the finite order from the thirteen covering relations of \(P(9)\). It then exhausts all \(2^9=512\) subsets and accepts a subset as open exactly when it is a lower set.

For each nonempty open, contractibility is checked by recursively applying only valid beat-point deletions until either a singleton is reached or no successful reduction exists. Every deletion in a successful certificate is revalidated in the stage at which it occurs. The final space \(P(9)\) is separately checked to have no beat point.

The expected result is exactly \(27\) opens, \(11\) nonempty contractible opens, two inclusion-maximal contractible opens,
\[
\{c_0,c_1,c_2,p,q,g\}
\quad\text{and}\quad
\{c_0,c_1,c_2,p,q,y,h,k\},
\]
and one unordered pair of contractible opens whose union is the entire space.

The calculation is finite and exhaustive. It does not certify any statement about other nine-point spaces, the order dual, or larger families.
