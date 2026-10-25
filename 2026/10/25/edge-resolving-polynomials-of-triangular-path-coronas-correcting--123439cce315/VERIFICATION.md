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

Execute `python3 verify_edge.py`. The program builds graph edges and BFS distances from first principles, compares all edge-pair distance signatures, independently constructs the auxiliary vertex-cover condition, and checks every subset for \(n=2,\ldots,9\). It checks all \(174{,}760\) candidate subsets, identifies exact two-landmark witness sets for \(n=4,\ldots,14\), and tests the claimed optimum and multiplicities for \(61\) further sizes. Expected stdout is embedded in `verify_edge.out`. No external package is needed. This finite testing does not prove unrestricted \(n\), and does not certify priority or independent mathematical review.
