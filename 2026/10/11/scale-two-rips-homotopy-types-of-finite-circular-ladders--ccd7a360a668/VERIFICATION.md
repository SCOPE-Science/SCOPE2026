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

The package's `verify_prism.py` uses only the Python standard library. In the directory containing the three standalone artifacts, execute `python3 verify_prism.py`. Its outputs assert exact simplex memberships, elementary collapses, small-complex mod-two ranks, and the all-parameter local freeness comparisons.

Actual replay result: `VERIFY_OK small_collapses=25+18 universal_local=True orbit_collapses=3996 n=7..30`.

For \(n=5,6\), the script verifies all 25 and 18 dimension-reducing collapse pairs from `cert_small.json`. For \(n\ge7\), `symbolic_phase_check()` enumerates only the six possible incident facets in integer coordinates, deleting prior translated pair templates, and confirms that precisely the designated free face and unique coface remain in every one of nine phases. The seven-column locality proof in `RESULT.md` makes these checks valid for **all** \(n\ge7\), not just the numerical sample. Numerical replay separately checks all \(9n\) elementary pairs and the residual rim for \(7\le n\le30\), and full reduced mod-two homology for \(3\le n\le6\). This is a same-model verification, not an independent review. Larger scales and full continuous metric graphs were not computed.
