---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For even n, central symmetry forces all asymmetries to 1. For odd regular n-gon, side-normal supports at center are r=R*cos(pi/n) outward and R inward, with equal side lengths and sum of side normals zero. For any x inside, t_i=<x,u_i>; the exact cone-volume mass is (r-t_i)/(nr). Guo mu_p^p becomes (nr)^-1 sum (R+t_i)^p (r-t_i)^(1-p). For p=1 the sum equals R/r at every x. For 1<p<infty the summand has strictly positive second derivative p(p-1)(R+r)^2 (R+t)^(p-2)(r-t)^(-p-1); Jensen and sum t_i=0 show lower bound (R/r)^p with equality only if all t_i=0, i.e. x=center. The Minkowski sup endpoint is R/r at center by R/r support bounds; any other center is excluded by the p>1 lower bound and as_p<=as_infty. Jin log endpoint is average log(R/r) on n equal cone-volume atoms. For 0<p<1, the same at-center normalized V_p value is conditional on taking Jin Section 4 proof's V_p convention, NOT an unconditional unambiguous Definition 4.1. Taylor sec(pi/n) expansion is standard. Independent support/Taylor checks odd 3..39 and actual verifier numerical support tests n=3..31 support the exact proof, but do not establish infinitely many n.

## originality

PASS

A crucial PRIOR result in Guo--Guo--Su 2015, Remark 1.2, already proves FOR ALL convex bodies that mu_1 is center-independent and every p>1 finite critical set is a singleton; these standalone critical-set facts are thus not original on polygons. Guo et al explicitly ask for classes with as_1=as_infty, which then collapses every intermediate p. The candidate original remainder is the concrete infinite non-centrally-symmetric family of regular odd polygons satisfying equality at sec(pi/n), its log endpoint and interpreted lower-p extension. Jin's accessible text studies log and p mixed-volume asymmetry but not an explicit regular polygon evaluation. The original Guo 2012 primary article could not be retrieved by OA/arXiv routes; authorized Oxford attempt returned VPN disconnected. Best-known finding limited to the regular-polygon evaluation, not the general p-critical uniqueness phenomenon.

## value

PASS

The hierarchy p=1..infty normally separates convex bodies, and Guo et al explicitly pose equality between endpoints as a structural question. Exact equality for all odd regular polygons supplies a canonical infinite non-symmetric witness, with a computable log endpoint, geometric secant parameter, and center locus interpretation. Useful as benchmark and classification example; does not claim p-critical uniqueness as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
