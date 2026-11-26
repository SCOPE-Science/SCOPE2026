---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The fixed-point equations give the complete integer sine preimages, with distinct branches for c>1. Their Jacobian has trace -1 and determinant D=2 pi c x y cos(pi y), of magnitude 2 pi sqrt(c-1)|y|. The frozen proof's endpoint statement for the radial bound is incorrect at order one (the bound tends to zero, not a positive limit), and an if-only citation is not sufficient to infer necessity for decay or exclude boundary points. The repaired proof uses the actual shifted Caputo-delta recurrence to obtain the generating matrix (1-z)^(nu-1)[(1-z)^nu I-zM]^(-1). When the denominator is zero-free on the closed disk, this has integrable radial boundary data, since |t|^(nu-1) is integrable, and its coefficients vanish by Riemann–Lebesgue, including a repeated eigenvalue. An interior denominator root is incompatible with decay on an eigendirection; a boundary root away from 1 is simple and gives a nonzero Abel limit after multiplication by 1-rho, which again excludes decay. A zero eigenvalue admits a constant mode. On each relevant ray the unit-circle boundary map has exactly one crossing; small radii on a strict angle ray are root-free, large radii have a root by Rouché, and crossing can only occur on that boundary. Positive real eigenvalues have an interior real root. Thus the determinant interval is exactly 0<D<d_nu, with the limiting radial behavior corrected and d_1=1. The positive-determinant states occur exactly in pairs at |y|=n+arctan(sqrt(c-1))/pi, n>=0. Counting strict inequality at the threshold with a ceiling yields the stated asymptotic and uniformly bounded rounding error near c=1. No reported numerical samples were needed or independently reproduced.

## originality

PASS

The pass is for the full real-state, order-dependent equilibrium census of the frozen Nov. 2 finding, not its model, the general spectral sector, the integer-order predecessor, or a claim that the census is absent from the present catalogue. A separate Nov. 22 Resultary entry demonstrably contains the same all-order census and more: an exact ceiling formula and inverse-square transition accumulation. Its listing follows the frozen record and gives no evidence of an earlier version supplying this full claim. The comparison establishes equivalent coverage in that later entry, not who originated the result. Earlier accessible material gives the criterion and the map but does not substantiate this all-order stable-branch law. The repair makes the overlap explicit and does not claim its proof clarification or ceiling formula as a separate novelty.

## value

PASS

The full unbounded state space changes a natural equilibrium and local-stability invariant of the published map: the same few principal equilibria do not describe its stable branches, and the number of linearly stable nonzero states diverges at a specified order-dependent rate. The strict count includes exact boundary exclusions and clarifies that this is a variational result, not a conclusion about actual basins or nonlinear sinks. This is a motivated full model census, not a general stability theorem or a plotting-window artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
