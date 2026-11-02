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

For odd n, n>=3, the normalized width-one Reuleaux polygon is the intersection of unit disks centered on a regular n-gon of radius R=1/(2cos(pi/(2n))). Its t-erosion is intersection of disks of radius rho=1-t, and odd n symmetry yields radial radius -R cos(theta)+sqrt(rho^2-R^2 sin^2(theta)) for |theta|<=pi/n. Integrating its square gives exact F_n(rho) and monotone Cheeger equation F_n(1-t)=pi t^2. In z=pi/n, t=1/4+a z^2+b z^4, independently recomputed symbolic radial coefficients -a+u^2/12-1/16 and -b-2a u^2/9+7u^4/432-u^2/96-5/768. Angular moments yield residual coefficients -a-5/288 and 7a/216-b-107/69120; hence a=-5/288 and b=-1313/622080. Reciprocal gives h_n=4+5pi^2/(18n^2)+2063pi^4/(38880n^4)+O(n^-6). Direct finite-n exact integral root solves at n=11,31,101,301,1001 agree, with scaled n^6 residual bounded; leading area deficit pi^3/(48n^2) yields gap ratio 40/(3pi). The analytic implicit function and uniform radial expansion, not finite n, prove asymptotic.

## originality

PASS

QUALIFIED PASS: The convex Cheeger erosion identity is classical; Henrot-Lucardesi prove triangle extremality and discuss exact computation of regular Reuleaux polygons, and Pan-Yao-Zhang (2026) prove regular n-gon minimization in a finite complexity class. The available full Henrot text does not give the displayed n^-2/n^-4 Cheeger coefficients or normalized ratio. Pan full article was inaccessible (arXiv/OA search failed; authorized institutional access reported vpn_disconnected), so its possible asymptotic appendix remains a material priority risk, not automatic failure.

## value

PASS

Quantitative convergence of a canonical sequence of constant-width bodies to the disk is a natural shape-optimization invariant, especially because each polygon is a finite-complexity Cheeger extremal by published results. The fourth-order term distinguishes exact geometry beyond leading-area deficit; the explicit ratio calibrates optimal Cheeger decay against area loss. The result is not a mere restatement of qualitative extremality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
