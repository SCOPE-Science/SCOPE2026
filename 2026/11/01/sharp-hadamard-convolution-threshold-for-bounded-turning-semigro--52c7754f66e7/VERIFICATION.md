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

# Verification scope
The analytic proof in `RESULT.md` handles every pair of normalized bounded-turning functions, every parameter in the closed unit interval, and every interior radius. It uses standard Herglotz representation, convergent coefficient expansions, positivity of the integral weights, a strictly monotone angular kernel, and exact evaluations of boundary moments. The sharp extremizer is explicitly analytic on the open disk. No external certification or independent validation has been carried out.

`checker.py` uses only Python 3 standard library. Run `python3 checker.py` to check exact rational identities for the first 34 Hadamard coefficients at three rational parameter values, the boundary threshold relation, a bisection evaluation of the smallest radius, selected pointwise angular inequalities, and exclusion of prior sufficient convex/half-plane hypotheses for the extremal factor. The finite checks do not prove infinite-dimensional assertions, exhaustive coverage or historical priority.
