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

The standalone `verify.py` re-evaluates the graph support formula and independently constructs the simultaneous Lie bracket matrices. Its matrix ranks are computed by finite-field Gaussian elimination, including arithmetic in \(\mathbb F_4\) via a quadratic irreducible polynomial.

**Executed checks:** 132 graph/field/tuple-length cases, comprising 400389 explicitly enumerated vertex coefficient tuples. Ten representative graphs are tested across applicable \(q\in\{2,3,4\}\) and \(t\in\{1,2,3\}\); all 64 labeled four-vertex graphs are checked at \((q,t)=(2,2)\). Polynomial totals were also checked against \(q^{t(n+m)}\), and the one-element versus two-element maximum ranks were checked on connected and disconnected test graphs.

**Replay command:** `python3 verify.py`. Expected successful marker: `VERIFY_OK_JOINT_GRAPH`.

**Scope of verification:** The finite calculation does not prove the arbitrary-graph and arbitrary-prime-power formula, which follows from the componentwise common-kernel proof in `RESULT.md`. No separate proof-assistant or independent audit was performed.
