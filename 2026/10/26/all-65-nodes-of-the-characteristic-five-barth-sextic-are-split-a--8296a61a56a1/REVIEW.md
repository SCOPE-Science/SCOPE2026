# Scientific review: the characteristic-five Barth sextic

## Correctness — PASS

The reduction uses the ramified specialization \(\tau\equiv3\), yielding exactly the displayed symmetric sextic. Over an algebraic closure, the affine Jacobian equations reduce to \(2x(T-a^2)=2y(T-b^2)=2z(T-c^2)=0\), and a complete split by zero/nonzero coordinates yields four squared-coordinate patterns with \(6+12+8+24=50\) points. All have invertible affine Hessians (determinants \(1,4,4,1\) on representatives). The six lines at infinity have fifteen distinct pairwise intersections, with nonzero transverse-square coefficients, giving exactly fifteen further nodes. All geometric singularities are accounted for; the Jacobian scheme is reduced. The executable checker independently reproduces finite computations. Its enumeration is supplementary, not a substitute for the complete algebraic case split.

## Originality — PASS, qualified

The characteristic-zero \(65\)-node sextic and its equation originate with Barth and are not claimed as new. Jaffe's 1994 preprint records the known complex construction, the full Bauer–Hulek–Rams–Sarti–Szemberg exposition presents its classical one-parameter geometry, and the Labs board and MathWorld describe the same characteristic-zero equation. An Orbiter manual search excerpt concerns a characteristic-eleven finite-field calculation, not the ramified characteristic-five fiber. Specific searches for the split \(65\)-node reduction and exact Jacobian singular scheme found no coverage. The complex count does not automatically imply that the nodes remain distinct and nondegenerate at the ramified prime. Nevertheless, the original Barth article was not completely accessible and may contain explicit node coordinates that imply some of the conclusion after reduction; this is a substantive residual risk.

## Mathematical value — PASS

The prime \(5\) is genuinely special: the golden-ratio ring ramifies there and the icosahedral representation changes, so preserving every one of the classical \(65\) nodes is not a generic-good-reduction tautology. The result resolves the precise exceptional-prime behavior of a distinguished extremal sextic, including complete scheme structure and the field of definition of all singularities. It is not merely a point count: a complete argument establishes no hidden geometric singularities and nondegenerate tangent cones.

## Closest sources and limits

Barth (1996), Jaffe (1994), and the Bauer–Hulek–Rams–Sarti–Szemberg 2017 article account for the characteristic-zero construction. Labs' display and MathWorld state the classical equation and the \(50+15\) distribution. The Orbiter documentation excerpt concerns characteristic \(11\). The complete Barth original and complete Orbiter manual were not inspected; no global characteristic-five node bound is claimed.

Self-review: passed. Independent audit: not yet performed.
