---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Before threshold activation, direct induction gives y^k=-(kb/(1+a^2))(1,a) and Ry^k=((k+2)b/(1+a^2))(1,a). The first-coordinate strict crossing k+2>gamma(1+a^2)/b yields the exact floor formula, and gamma>=b/(1-a) ensures the second reflected coordinate is still within threshold at that first crossing. In the identified cell the error matrix is (1/(1+a^2))[[a^2,-a],[a,a^2]], whose transpose product is a^2/(1+a^2) times identity. The entry error lies strictly within the distance-b ball around the reflected fixed point, while all relevant cell-boundary distances are at least b; the reflector is orthogonal on errors and the linear map contracts, so the cell remains invariant. A fresh direct nonlinear replay on a representative parameter set recovered the exact first entry and the package checker tests several further cases. The analytic proof, not finite testing, establishes the continuum claim.

## originality

PASS

Demanet--Zhang prove eventual linear convergence for basis pursuit with the same principal-angle rate and explicitly state that they make no attempt to characterize the preceding transient. Liang--Fadili--Peyré--Luke prove finite activity identification and local linear convergence under partial smoothness but give qualitative identification time. The audited two-variable family supplies an exact threshold-controlled entry index and invariant-cell proof, which is not covered by those broader asymptotic/local theorems.

## value

PASS

The motivating primary paper explicitly leaves transient characterization open. This exact family shows a sharp separation between an arbitrarily long threshold-controlled identification delay and an unchanged principal-angle asymptotic rate, a useful structural warning for algorithm tuning rather than an arbitrary toy iteration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
