---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

On X=0 partials exclude singularities. On X=1, affine f(u,v) has partials 1-u^4v and -lambda+u^5-v^4, forcing v=u^-4, lambda=u^5-u^-16. Substitution into f gives -(u-1)^3(u+1)^2 P7(u)P19(u)/u^28: the equation itself is essential because characteristic divides degree. Exact F3 polynomial checks separately verified f, partials, factorization and irreducibility of P7,P19,Q7,Q19; the package quotient-field congruences identify lambda minimum polynomials of prime degrees 7 and 19, giving one singular point per parameter. Hessian determinant -lambda u^3 is nonzero except lambda=0, where completed-square local expansion W^2+unit*V^3 gives a cusp. Bezout and at most one delta-one singularity exclude geometric reducibility; arithmetic genus 10 decreases to 9. Finite F3 rational checks alone do not prove the geometric classification.

## originality

PASS

Qualified PASS: the exact geometric discriminant of this fixed q=3 pencil, nonrational Frobenius orbits and complete degeneration basket are not supplied by the prior Fq-rational smoothness result read in full.

## value

PASS

The finite geometric discriminant and exact orbit degrees are natural invariants of a named plane-filling pencil; exact cusp-versus-node degeneration and genus profile fill a concrete moduli arithmetic gap inaccessible from rational-parameter smoothness checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
