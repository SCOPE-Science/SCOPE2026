---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS: Independent symbolic expansion of det(lambda I-J) equals (lambda+a)^3+(1-3t^2/4)(lambda+a)+rho-t-t^3/4 exactly. Cubic Routh–Hurwitz for a>0 yields B>0, C=rho-rho_->0, H=3aB-C=rho_+-rho>0. B=0 exclusion and H/C equality factorizations give the stated simple imaginary pair and simple zero eigenvalue. For fixed rho, H(0)<0, C(0)>0 for small a; Hprime(t)=(3/4)(t-2a)^2+1-3a^2>0 and Cprime<0 make unique boundary roots and no missing stability islands. IFT at t0 solves q(t0)=0, giving first-order widths 3va/s below threshold, inverted ordering above, and at t*=2/sqrt(3), rho*=8/(3sqrt(3)), exact cubic roots t_H=t*-4a^3+O(a^4), t_Z=t*+a^3/2+O(a^4) and width 9a^3/2; B=3a^2+O(a^3) on critical interval. Equal-damping instability follows from the conjugate roots of mu^3+mu+rho and shift by -a. This is an exact linear result; no nonlinear Hopf claim.

## originality

PASS

Best-of-knowledge noncoverage after actual subject/statement/implication comparisons. Relevant known special cases and technical mechanisms credited; no proof of universal publication priority is claimed.

## value

PASS

PASS: A specified minimal signed network with competing length-two and length-three feedback has an exact global parameter stability tongue and a sharp weak-damping phase transition, including a nonroutine cubic collapse and two different crossing mechanisms. This adds a motivated solvable boundary case to non-Hermitian disorder-stabilization theory rather than presenting the Routh-Hurwitz test itself as novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
