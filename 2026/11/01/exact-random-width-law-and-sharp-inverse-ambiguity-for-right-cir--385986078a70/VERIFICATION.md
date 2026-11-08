---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For any R,H>0, writing a=2R,b=H, the cylinder is a Minkowski disk-plus-axial-interval and its exact one-dimensional directional width is g(t)=a sqrt(1-t^2)+b t with t=|u_3| uniform on [0,1]. The unique interior maximizer t=b/s gives s=sqrt(a^2+b^2); concavity shows the minimum is m=min(a,b). Solving g(t)=w produces t_±=(bw±a sqrt(s^2-w^2))/s^2. Counting each valid inverse branch on w between m,max(a,b),s gives the four claimed CDF regimes, including the a=b boundary with no intermediate regime and continuity/no atoms. Integrating against uniform t yields mean πa/4+b/2. (m,s) identifies the unordered pair {a,b}; swapping them changes the mean by (π-2)|a-b|/4=(π-2)sqrt(s^2-2m^2)/4. Nearest-candidate discrimination is guaranteed for exact endpoints and absolute mean error below half that gap; equality is a non-robust tie. At a=b the candidates coincide and the gap vanishes as square root. Independent 100001-sample monotone t-mesh CDF counts for a,b=(1,2),(2,1),(1,1),(.1,10) differ from exact CDF by at most 2.0e-5, the expected grid discretization error; the continuum proof is analytic, not the grid.

## originality

PASS

Qualified best-of-knowledge PASS for the complete cylinder line-width law and its three-observable inverse condition. Neither the nearby cone theorem nor planar cylinder-shadow results implies this CDF; elementary Minkowski support additivity itself is known and not counted as novel. Classic Feret-diameter stereology could conceivably contain this exact formula.

## value

PASS

Unlabeled directional width is a natural stereological observable. This result gives a full forward distribution, a rigid but sharply two-to-one inverse problem from endpoint data, and an exact nonuniform stability margin for adding one mean measurement. These are precise independently useful facts for a natural two-parameter body, beyond the elementary support-function formula; it does not solve noisy-support inference or general body reconstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
