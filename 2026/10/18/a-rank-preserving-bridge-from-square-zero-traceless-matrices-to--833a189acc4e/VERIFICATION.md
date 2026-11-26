---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Fix the uniformizer. If s is the minimum entry valuation of a nonzero traceless X, multiplication by pi^s identifies R/(pi^(m-s)) with (pi^s), using ann(pi^s)=(pi^(m-s)), so there is a unique primitive traceless preimage Y at length ell=m-s. Reduction of the inputs and multiplication by pi^s identify the two additive images. A primitive 2-by-2 matrix has a unit pivot, and hence elementary divisors 1 and its determinant up to units; writing v=min(ell,val(det Y)), its image exponent is 2ell-v. Cayley–Hamilton in every characteristic tests X^2=0 by pi^(2s) det(lift Y)=0, i.e. v>=m-2s, since m-2s<=ell and reduction to length ell preserves that test (also when m-2s<=0). The criterion is exactly 2ell-v<=m. For the enumeration, a^2+bc=0 over F_q has q^2 roots (q(q-1) for b nonzero, q for b=0), and at every nonzero root one of b,c is nonzero, giving q^2 lifts for each prescribed next digit, regardless of characteristic. Grouping valuation v=ell, v=0, and 0<v<ell gives, respectively, (q^2-1)T/(1-q^2T), (q-1)q^2T^2/(1-q^3T^2), and (q^2-1)(q-1)q^2T^3/[(1-q^2T)(1-q^3T^2)]; with the zero matrix these sum to the stated rational function. At exponent r every contributing length is at most r, giving stabilization and the field boundary m=1. The proof is exact and does not rely on the bundled finite verifier.

## originality

PASS

The primitive image-zeta rational function is already known and is explicitly not presented as new. The supported distinct result is the uniformizer-relative bijection, with exact preservation of image size, that identifies the finite square-zero trace-zero stratum with a disjoint union of bounded primitive image strata. No statement giving that transfer was identified in the inspected sources.

## value

PASS

The exact bijection identifies which primitive finite-ring data survive a nonlinear square-zero constraint at each ambient length, explains the landscape of image sizes and stabilization of every fixed-size fiber, and makes an existing explicit zeta series usable in both equal and mixed characteristic. It is more informative than a fresh computation of known coefficients or a coincidence of closed forms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
