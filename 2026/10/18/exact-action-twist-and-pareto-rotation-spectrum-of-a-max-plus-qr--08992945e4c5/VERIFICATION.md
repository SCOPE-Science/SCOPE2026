---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The final claim is about F(x,y)=(y,max(0,y+1)−x), H=max(1−x−y,2−x,2−y,1+x−y,1−x+y,x,y), all c≥3 for area and all c>1 for rotation, with 2D Lebesgue-uniform cutoff law at C>3. In each half-plane y≥−1 and y≤−1, both H∘F and H reduce to identical max lists; F has continuous inverse and determinant +1 in both affine branches. Seven half-space constraints define the outer convex contour: eight MARKED boundary points are correctly listed, though B=(c−2,−1) lies on the straight segment between A=(c,1) and C=(1,2−c), so strictly there are only seven extreme vertices, not a geometric octagon. This harmless nomenclature error does not alter the shoelace polygon-area formula A=(5c²−6c−3)/2; A(3)=12. For outer c>3, Takahashi–Iwao §5 supplies a rigid return rotation h=2/(c−1) and roof times 6 on interval fraction h, 5 on complement. For rational and irrational h the return-time mean is 5+h (rational counting and uniquely ergodic irrational circle rotation), with one clockwise circuit per return, giving rho=1/(5+h)=(c−1)/(5c−3); inner F is order-six about (1,1). Differentiate with I=A/(2π) to obtain 4π/(5c−3)^3>0. On {H≤C}, the exact cutoff mass at rho=1/6 is 12/A(C), and differentiating A(c(r)) gives density 4/[A(C)(1−5r)^3] for 1/6<r<rho(C), integrating to 1−12/A(C). Scaling H/C→T with CDF t² gives C(1/5−rho(H))→2/(25T), with Pareto-two threshold 2/25 and density 8/(625w³). Independent symbolic identities verified area, derivative, density integral, limiting CDF, and exact rational orbit periods/geometric windings at five levels; separate grid tests corroborated global H invariance. Finite samples do not replace all-real branch proof, irrational unique ergodicity, or weak-convergence proof.

## originality

PASS

Qualified best-of-knowledge PASS for the COMPLETE planar-area law (the exact period-six frequency atom, cubic exterior density, and Pareto-two large-area gap limit), NOT for the original map, first integral, marked polygon or 5/6 roof times and not for mere physical rotation formula, which follows quickly from these inputs. The closest exact-object Takahashi–Iwao primary 10-page manuscript was read and visually inspected, and its full §4–5 dynamics do not state the area-pushforward probability theorem. Another QRT primary (Nobe 2008) was compared at worked examples and has a different map with (4,4) period 24 rather than 17. General polygonal Hamiltonian theory and relevant Resultary entries do not exhibit this law in inspected material. A closely relevant Iwao 2005 JPSJ primary is inaccessible owing to disconnected authorized institutional access; it is retained as material residual risk, not called noncovering or used as automatic failure. Overall originality is narrow and not a certification of universal historical priority.

## value

PASS

The natural invariant measure for a planar area-preserving integrable homeomorphism is two-dimensional Lebesgue area on a bounded invariant sublevel set; its pushforward under the original-iterate rotation-frequency observable is a motivated exact statistical invariant. The complete mixed distribution distinguishes the six-periodic central cell from the changing-frequency exterior, and its explicit cubic edge density determines the nontrivial Pareto-two fluctuation scale as the energy/area cutoff grows. The strictly positive action derivative quantifies the twist of the invariant foliation, but does not imply nonsmooth KAM stability. These statements offer a precise, reproducible benchmark to researchers studying ultradiscrete QRT dynamics, rotation distributions and large-domain sampling. The significance is limited to this canonical normal form and area sampling; the calculation is elementary once the substantial prior return-geometry is credited, and no general class theorem or perturbation theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
