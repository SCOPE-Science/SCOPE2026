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
# Verification record

The self-contained `verify.py` uses `fractions.Fraction` and complete Cartesian enumeration for four customer arrivals with three gaps in \(\{0,1/4,1,2\}\), four downstream requirements in \(\{c,c+1/4,c+1\}\), and \(c\in\{0,1/4,1/2,1\}\). It checks 20,736 exact path instances, including ties and the service-floor boundary. The scripted strict violation checks arrivals \((0,1/10)\), first downstream service \(1/5\), first-stage service \(1/2\), and an arbitrary later requirement \(1\). Script terminates with `exact verified paths: 20736` if all conditions hold.

The stationary finite-\(c\) mean formula is obtained analytically from the pathwise identity and Pollaczek–Khinchine. The general small-duration theorem uses the displayed mass-transport identity, the Borel law, uniform branching bound, empty-station probability limit and absolute-continuity integration. Finite tests cannot establish this limiting theorem. A related source's differentiation/mass-transport steps were examined independently against the assumptions; they are not asserted as an externally audited certificate.

Independent audit status: not performed.
