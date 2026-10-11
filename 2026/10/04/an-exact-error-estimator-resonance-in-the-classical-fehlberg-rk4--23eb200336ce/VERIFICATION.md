---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The six Fehlberg stages were reconstructed independently over exact rationals. They give \(R_4(z)=1+z+z^2/2+z^3/6+z^4/24+z^5/104\) and \(R_5(z)=1+z+z^2/2+z^3/6+z^4/24+z^5/120+z^6/2080\), hence \(E(z)=R_5(z)-R_4(z)=z^5(3z-8)/6240\). The unique nonzero estimator zero is therefore \(z_*=8/3\), where both formulas equal \(1613/117\). Independent exact evaluation also gives \(E'(z_*)=1024/15795\). The sixth Taylor partial sum already exceeds the common numerical multiplier by \(139264/426465>0\), so \(e^{8/3}>1613/117\); the one-step local defect is nonzero while the embedded estimate vanishes. Repeating an externally fixed resonant step leaves the estimate identically zero and multiplies the numerical/exact ratio by a fixed factor strictly below one, so the relative global error tends to one. The unbounded local effectivity ratio follows from the simple zero of \(E\) and the nonzero defect at \(z_*\).

## originality

PASS

Best-of-knowledge originality survives statement-level comparison. The 1990 Higham--Hall paper analyzes equilibrium/stability behavior of embedded fourth/fifth-order pairs and explicitly compares the Fehlberg pair, but the inspected paper does not state the positive-real common-multiplier resonance \(z=8/3\), its zero embedded estimator with nonzero exact defect, or the resulting fixed-step blind-error trajectory. Higham's later regular-pair work concerns simultaneous spurious fixed points of the two formulas under adaptive error control; the inspected workshop precursor likewise frames regularity in terms of common fixed points, whereas the submitted resonance has common multiplier \(1613/117\neq1\). Fresh Resultary and web searches found no prior statement of the exact \(8/3\) resonance. The full 1997 journal article remained an access risk rather than being treated as novelty evidence.

## value

PASS

An embedded estimator that vanishes exactly while the accepted one-step map has a nonzero local defect is a motivated reliability boundary for a classical adaptive pair. The exact resonance, simple-zero effectivity blow-up, and repeated externally fixed-step failure together give a concrete reproducible stress test rather than a generic numerical warning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
