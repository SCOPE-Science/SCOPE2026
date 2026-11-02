---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For every fixed 0<a<1, let m=min(a,1-a), r=m/16, rho=m^2/256. Expanding the cubic g_a about binary s_i gives slope -alpha_i in {a,1-a}; the map on complex l-infinity v has sup bound [rho(2+4r)+(2+r)r^2]/m<r and Lipschitz [4rho+4r+3r^2]/m<1/2. Banach contraction and analytic iteration construct the unique ball solution for |d|<rho, uniformly for all two-sided binary codes. The coefficient recurrence has dependency radius n at order n. At first reachable order R the only changed terms follow the unique left/right paths; repeated divisions by alpha_j give exact leading coefficient (s_{i-R}-t_{i-R})/prod_{j=i-R+1}^{i}alpha_j+(s_{i+R}-t_{i+R})/prod_{j=i}^{i+R-1}alpha_j. Single endpoint flips are nonzero, opposite flips cancel precisely at equal path weights; at a!=1/2 this is equal zero counts, at a=1/2 automatically. Uniform Cauchy bounds give 2r (|d|/rho)^R/(1-|d|/rho). The independent rational Taylor recursion checked 60 bounded heterogeneous/single/two-boundary instances, not the infinite proof.

## originality

PASS

Qualified best-of-knowledge PASS for the explicit all-code weighted shortest-path Taylor response and exact two-defect cancellation criterion. Weak-coupling holomorphic existence and symbolic coding are prior concepts. Hesoun–Stehlik–Volek treats the identical Nagumo model and may conceivably contain an equivalent localization formula; current full text was unavailable after OA attempts and authorized VPN check, so no assertion of whole-document noncoverage. The stated unique leading paths are more specific than symbolic existence, stability, and qualitative front decay in the accessible material.

## value

PASS

The first nonvanishing effect of a distant flipped bistable code symbol is a natural and operationally meaningful pinned-lattice localization invariant; precise products of stable slopes reveal heterogeneous asymmetry and robust exact cancellation at order R. It is not merely a finite experiment or the routine implicit-function continuation, and it distinguishes neutralized two-sided defects from isolated defects in arbitrary aperiodic backgrounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
