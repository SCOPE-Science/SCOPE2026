# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

For a reduced flat torus
\[
T_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z),\qquad
\tau=x+iy\in F,
\]
the shortest lattice vector has length \(1\), so \(\operatorname{SR}(T_\tau)=1/y\). Normalization by the Loewner optimum gives \(q=\sqrt3/(2y)\).

The quotient-distance reduction was checked against the standard \((2,3,\infty)\) modular tessellation. After the reflection symmetry \(x\mapsto-x\), the half-domain
\[
F_+=\{0\le x\le1/2,\ x^2+y^2\ge1\}
\]
is a Coxeter chamber whose type-three vertex is \(\rho=1/2+i\sqrt3/2\). It lies in the Voronoi cell of that lift of the order-three point, so the orbifold distance to the hexagonal class is the ordinary hyperbolic distance to \(\rho\) inside this chamber.

The hyperbolic radius-\(d\) circle about \(\rho\) was derived directly from the upper-half-plane distance formula:
\[
(x-\tfrac12)^2+(y-\tfrac{\sqrt3}{2}\cosh d)^2=\tfrac34\sinh^2d.
\]
The maximum feasible \(y\) is always the upper point on \(x=1/2\), giving \(q_{\min}=e^{-d}\).

For the minimum feasible \(y\), the circle first meets the unit-circle boundary. The switch occurs exactly at the square point \(i\), at distance \(\log\sqrt3\). Parameterizing the unit-circle geodesic by \(e^{i\theta}\) gives
\[
d=\log(\sqrt3\tan(\theta/2)),
\]
hence the first upper branch \((3e^{-d}+e^d)/4\). Beyond the square point the first feasible endpoint lies on \(x=0\); solving the circle equation there gives
\[
[\cosh d+\sqrt{\sinh^2d-1/3}]^{-1}.
\]
The two branches agree at the transition. The feasible circle portion is connected, so continuity gives every intermediate systolic-ratio value.

The inverse formulas were checked algebraically. The first branch is the appropriate root of \(4q=3e^{-d}+e^d\). On the rectangular branch \(\tau=iy\), substitution of \(y=\sqrt3/(2q)\) into the distance formula gives
\[
\cosh d=(3+4q^2)/(6q).
\]
No numerical approximation is used in the proof.

Potential boundary cases were checked: \(d=0\) collapses both envelopes to the hexagonal value; \(d=\log\sqrt3\) gives the square normalized ratio \(\sqrt3/2\); and both envelopes are asymptotic to \(e^{-d}\) in the cusp.

## Originality

**PASS, to the best of our knowledge.**

The novelty claim excludes Loewner's inequality itself, standard reduction theory for two-dimensional lattices, and the known formula \(\operatorname{SR}(T_\tau)=1/\operatorname{Im}\tau\) on the modular fundamental domain.

Pu's 1952 paper is the first published reference for Loewner's torus inequality. Horowitz--Katz--Katz give an isosystolic defect in terms of variance of a conformal factor; this is a different quantity from distance in flat-torus moduli. Fortier Bourque--Martínez-Granado--Vargas Pallete explicitly describe the modular fundamental domain, the formula \(1/\operatorname{Im}\tau\), and the unique strict maximum at the hexagonal torus, but do not state the fixed-distance profile derived here. Standard modular-orbifold references supply the \((2,3,\infty)\) geometry used in the distance reduction.

Searches using the phrases and synonyms “flat torus systolic stability,” “Hermite invariant stability,” “modular surface systole,” “hyperbolic distance to the hexagonal lattice,” “distance to the hexagonal torus,” and binary-quadratic-form language did not locate the displayed two-sided profile, its exact inverse, or the square-torus phase transition.

Residual risk is material because the proof is elementary in reduced coordinates. Classical geometry-of-numbers, reduction-theory, or modular surface literature may contain an equivalent statement under another normalization. No specific inaccessible source was found with concrete evidence that it contains this result.

## Value

**PASS.**

The theorem turns the equality case of the two-dimensional Hermite/Loewner bound into a complete global sharp diagram on the natural flat-torus moduli orbifold. It identifies both extremal directions at every distance, exhibits a geometric phase transition at the square torus, and can be inverted exactly to bound modular distance from a measured systolic ratio. The linear near-optimal deficit also records the nonsmooth orbifold geometry of the systolic maximum.

## Limitations

- Flat two-tori up to similarity only; no claim is made for arbitrary Riemannian torus metrics.
- Hyperbolic distance uses curvature \(-1\); alternate genus-one Teichmüller normalizations rescale it.
- Only the systolic ratio is profiled; diameter, covering radius, and other lattice-shape quantities are not controlled here.
- Originality is to the best of our knowledge, with genuine folklore risk because the derivation is short.

## Sources checked

- P. M. Pu, *Some inequalities in certain nonorientable Riemannian manifolds*, Pacific J. Math. 2 (1952), 55--71. https://doi.org/10.2140/pjm.1952.2.55
- C. Horowitz, K. Usadi Katz, M. G. Katz, *Loewner's torus inequality with isosystolic defect*, arXiv:0803.0690. https://arxiv.org/abs/0803.0690
- M. Fortier Bourque, D. Martínez-Granado, F. Vargas Pallete, *The extremal length systole of the Bolza surface*, Annales Henri Lebesgue 7 (2024), 1409--1455. https://doi.org/10.5802/ahl.223
- D. Calegari, J. Louwsma, *Immersed surfaces in the modular orbifold*, arXiv:1003.1532. https://arxiv.org/abs/1003.1532
