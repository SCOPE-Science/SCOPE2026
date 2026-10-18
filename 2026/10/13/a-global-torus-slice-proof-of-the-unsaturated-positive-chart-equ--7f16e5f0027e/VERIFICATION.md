---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Let G=(G_m)^r act by integer weight vectors w_j on S=C[u_j] and F_i have the standard basis weight e_i. On D(F_1...F_r), the evaluation Phi(u)=(F_1(u),...,F_r(u)) belongs to G and obeys Phi(lambda.u)=lambda Phi(u). The maps (y,lambda)->lambda.y and u->(Phi(u)^(-1).u,Phi(u)) are mutually inverse regular scheme morphisms, since negative weights only invert Phi_i on the indicated principal open. D is a nonempty integral smooth open of affine n-space, and the isomorphism with Y×G implies S/J is a domain and dim Y=n-r; the split Euler derivations E_a(F_b)=delta_ab F_b at Y give Jacobian rank r, proving smooth complete intersection. Base change to alg closed extensions likewise preserves geometric integrality. If Y has a coordinate-torus point, prime J contains no coordinate variable and hence J:(prod u_j)^infinity=J. The toric Assumption 1 unimodular extension gives integer K with R K=0, A K=I, so each Cox homogenization F_i has basis multidegree. Cox-torus positive chart points exist, and the paper's saturation formula then implies the exact unsaturated chart ideal. The integral-basis hypothesis is essential (r=n=1,F=u² of weight 2 yields two points), and claims beyond it are excluded.

## originality

PASS

The paper Calvo Cortes–Telen expressly poses Conjecture 3.11 asserting that the saturated ideal (f_i^h-1):coordinates^infty equals its unsaturated equations under Assumption 1. Their prime-on-the-dense-torus result and saturation formula do not establish boundary primeness; they report an example whose saturation computation did not terminate. The proof here provides an explicit global torus slice before any coordinate inversion, closing that logical gap for all unimodular data. Cox's toric homogeneous-coordinate construction and more specialized post-localization graded factorizations are related foundations but do not state this general polynomial ideal identity. The simple equivariant algebra lemma may exist implicitly in invariant theory, a serious originality alias risk; the explicit resolution of the source conjecture survives as an application.

## value

PASS

This is a complete positive answer to an explicit currently stated geometric conjecture, replacing infeasible symbolic saturations by an elementary global scheme isomorphism. The result yields primeness, smoothness, complete-intersection dimension and a uniform ideal equality under an exact natural unimodularity condition, with explicit failure at nonprimitive degrees. This is substantive structural value independent of example computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
