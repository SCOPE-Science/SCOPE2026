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

Execute `python checker.py` with Python 3.10 or later. Standard-library modules only. The program recomputes all \(35{,}280\) admissible distinct balanced six-subset systems, verifies exact orbit sizes \(5{,}040,20{,}160,3{,}360,6{,}720\), builds the \(1{,}260\) possible four-set balanced forbidden configurations, and derives contradictions in \(4,5,3,3\) unit-propagation steps for the four representatives. Its last line is `ALL_CHECKS_OK`.

Coverage is complete for the specified eight-point *distinct-six-coalition* domain. Neither random tests nor arbitrary bounds are used to justify the universal finite theorem. Earlier supplementary enumeration of the same objects via completion of a five-family recovered the same total. The proof does not exclude obstruction sequences with repeated coalitions and is not an independent audit.
