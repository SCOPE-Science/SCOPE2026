---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Reexpanded the successive noisy Picard iterates to D=(1-rho)^2 s-(2-rho)e0+e1, W=((1-rho)s-e0)^2 and Z=s-W/D. The support minimum Dmin=d-(3-rho)eta gives the sharp eta_c. Below it the transform is continuous on the compact error square. At equality D vanishes at precisely one corner and W has positive limit; two-dimensional triangle scaling gives tail K t^-2 (K=2s^2/[(2-rho)(3-rho)^2]); for eta>eta_c the pole cuts a positive-length line, giving T_eta t^-1 via conditional widths. Tail integration proves exact p-moment thresholds p<2 at equality and p<1 above. Exact reciprocal-square quadrant integral gives precritical EZ^2=2K log(eta_c/(eta_c-eta))+O(1). Independently verified rational rho=1/2,s=1: eta_c=1/10, K=16/75, 2K=32/75 and T_(1/5)=403/1296; these checks corroborate, not replace, the asymptotic proof.

## originality

PASS

Classical Aitken Δ², approximate Anderson acceleration and inaccurate-evaluation convergence results were distinguished from a fully specified stochastic, unregularized two-evaluation tail and moment phase diagram. In particular, deterministic convergence safeguards do not determine the corner t^-2 and interior t^-1 pole geometry. Toth et al. 2017 is a plausible full-text priority risk, not declared noncovering.

## value

PASS

It is mathematically natural to ask when an unregularized extrapolation denominator admits finite risk under bounded computation error. The dimension change of the zero set from no pole to corner to interior line yields sharp changes in moment existence, with explicit tail constants and logarithmic mean-square blow-up. These facts are meaningful for deciding whether clipping/regularization is needed, without claiming generic noisy Anderson convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
