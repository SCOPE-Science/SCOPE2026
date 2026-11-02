# Degree quantization and complete phase-ambiguity normal form on intersecting circles

## Finding

Let \(C_1,C_2\) be two distinct Euclidean circles in the complex plane, let \(d\geq 1\) be an integer, and let \(P,Q\) be nonzero complex polynomials of degree at most \(d\). Suppose \(|P(z)|=|Q(z)|\) on \(C_1\cup C_2\). The following classification holds.

If the circles have at most one common point, or meet at an angle \(\theta\) with \(\theta/\pi\notin\mathbb Q\), then \(P=\eta Q\) for some \(|\eta|=1\).

Suppose instead that the circles meet in exactly two points \(a\ne b\), and the smaller unoriented intersection angle satisfies \(\theta/\pi=p/q\) in lowest terms, where \(0<p/q\leq 1/2\). Choose \(\gamma\in\mathbb C\), \(|\gamma|=1\), such that
\[
 t(z)=\gamma\left(\frac{z-a}{z-b}\right)^q\in\mathbb R\cup\{\infty\}
 \quad\text{for }z\in C_1\cup C_2.
\]
Such a \(\gamma\) always exists. After cancelling the greatest common polynomial divisor of \(P,Q\), their quotient has **exactly** the following form:
\[
 \frac{P(z)}{Q(z)}=\eta\,
 \frac{U(t(z))}{U^\sharp(t(z))},\qquad
 U^\sharp(t)=\overline{U(\overline t)},\quad |\eta|=1,
\]
where \(U\) is a nonzero complex polynomial having no real zero and \(\gcd(U,U^\sharp)=1\); constants are permitted. Conversely, every rational function of this form is unimodular on both circles wherever finite, and after clearing denominators provides such a polynomial pair.

If \(k=\deg U\), then the reduced rational map has degree **exactly** \(qk\). In particular, every nonproportional equal-modulus polynomial pair has reduced quotient degree a positive multiple of \(q\), so that \(d\geq q\). This necessary threshold is sharp: choose
\[
 P_*(z)=\gamma(z-a)^q+i(z-b)^q,\qquad
 Q_*(z)=\gamma(z-a)^q-i(z-b)^q.
\]
These are nonproportional, have maximal degree \(q\), and have equal magnitudes on both circles. Thus the minimum possible maximal degree of a nonproportional ambiguous pair is **\(q\)**.

For **any** choice of \(2d+1\) distinct points on each circle, equality of the \(4d+2\) sampled magnitudes for polynomials in \(\mathcal P_d\) implies equality on both entire circles. Consequently those measurements are phase-retrieving precisely when the two circles meet at an irrational multiple of \(\pi\), do not meet transversely, or meet at rational angle \(p\pi/q\) with \(d<q\). At \(d\geq q\), every such two-circle measurement arrangement admits a nontrivial ambiguity.

## Assumptions and scope

All circles are nondegenerate Euclidean circles of positive finite radius, and are distinct. The polynomial space \(\mathcal P_d\) is the space of complex polynomials of degree at most \(d\). Phase equivalence means multiplication by a unimodular scalar. The rational-map degree of a reduced quotient is the maximum of the degrees of its coprime numerator and denominator, including its behavior at infinity. The intersection angle is taken as the smaller unoriented angle between tangents, lying in \((0,\pi/2]\). When \(d=0\), constants are trivially phase-retrievable on any nonempty sampling set; the stated result assumes \(d\geq1\) for uniformity.

The displayed quotient normal form refers to a rational identity on the Riemann sphere, not merely an equality at sampled points. Points at which a quotient formally has a pole do not invalidate the polynomial equal-modulus identity, which extends continuously.

## Proof

**1. From equal magnitudes to two reflections.** For a circle \(C=\{z:|z-c|=r\}\) define its anti-Möbius reflection
\[
 \sigma_C(z)=c+\frac{r^2}{\overline z-\overline c}.
\]
It fixes \(C\) pointwise. Let \(F=P/Q\) be the reduced rational quotient. Equality of magnitudes on \(C\) gives \(|F|=1\) away from finitely many removable zeros of the initial pair. Since \(z\mapsto \overline{F(\sigma_C(z))}\) is rational in \(z\), equality on infinitely many points of \(C\) implies the rational identity
\[
 F(z)\,\overline{F(\sigma_C(z))}=1.
\]
Thus \(F\circ (\sigma_{C_2}\circ\sigma_{C_1})=F\).

**2. Infinite-order rigidity.** A nonconstant rational function has finite generic fibres. If a Möbius map \(M\) has infinite order, it has an infinite orbit outside at most two exceptional fixed points. Therefore \(F\circ M=F\) would put an infinite orbit in one finite fibre, a contradiction. Standard elementary circle-reflection geometry (or conjugating the two circles to disjoint circles, tangent lines, or intersecting lines) shows that \(M=\sigma_{C_2}\circ\sigma_{C_1}\) has infinite order for circles having at most one common point, and for transverse intersections with irrational \(\theta/\pi\). Hence \(F\) is constant in those cases. Its circle modulus is one, so \(P=\eta Q\) for \(|\eta|=1\).

**3. Finite reflection group and quotient degree.** Let the two transverse intersection points be \(a,b\), and set \(w=(z-a)/(z-b)\). Both circles become straight lines through the origin in the \(w\)-plane. Reflection in these lines composes to the rotation \(w\mapsto\zeta w\), where \(\zeta=e^{\pm 2i\theta}\) and hence is a primitive \(q\)-th root of unity when \(\theta/\pi=p/q\) in lowest terms. The invariant rational functions for this cyclic rotation are exactly \(\mathbb C(w^q)\): to see this, the extension \(\mathbb C(w)/\mathbb C(w^q)\) has degree \(q\), and its \(q\) distinct rotation automorphisms exhaust the group of automorphisms of this extension. Thus
\[
 F(z)=S(w(z)^q)
\]
for a unique rational function \(S\). The degree of a composition of nonconstant rational maps on the Riemann sphere is the product of their degrees. Therefore \(\deg F=q\deg S\). In particular, nonconstant \(F\) forces \(q\leq\deg F\leq d\).

**4. Exact unimodular normal form.** Write the two image lines as \(e^{i\phi_j}\mathbb R\), where \(\phi_2-\phi_1\equiv\pm\theta\pmod\pi\). Set \(\gamma=e^{-iq\phi_1}\). Since \(q\theta=p\pi\), \(t=\gamma w^q\) takes both lines to the extended real line. The condition \(|F|=1\) on either source circle is equivalent to \(|S_0(t)|=1\) for all real \(t\) where \(S_0\) is finite, with \(F=S_0(t)\). If \(S_0=A/B\) in coprime polynomial form, the rational reflection identity \(S_0(t)\overline{S_0(\overline t)}=1\) shows that every finite zero is paired, with multiplicity, to the conjugate pole and conversely. There are no real zeros or poles. Also \(S_0(\infty)\) is finite and unimodular, so numerator and denominator have the same degree. Consequently there exist \(\eta\) of modulus one and a polynomial \(U\) with no real roots and with \(\gcd(U,U^\sharp)=1\) such that \(S_0=\eta U/U^\sharp\). Conversely that expression is unimodular on the real axis. Composition with \(t\) completes the necessary-and-sufficient classification and proves \(\deg F=q\deg U\), including the constant case \(\deg U=0\).

**5. Attainment of the minimal ambiguity degree.** Taking \(U(t)=t+i\) and \(U^\sharp(t)=t-i\), then clearing the denominator of \(t(z)\), produces the stated \(P_*,Q_*\). The two polynomials are coprime: a common root would also annihilate their sum \(2\gamma(z-a)^q\) and difference \(2i(z-b)^q\), which is impossible since \(a\ne b\). Their quotient is not constant and has rational-map degree \(q\). The equality of magnitudes on both circles follows because \(t(z)\) is real or infinite there. This sharpens the necessary bound \(d\geq q\).

**6. Sampling reduction.** Parametrize any circle by \(z=c+re^{i\varphi}\). For polynomials of degree at most \(d\), the restriction \(|P(z)|^2-|Q(z)|^2\) is a real trigonometric polynomial with frequencies in \([-d,d]\). Multiplication by \(e^{id\varphi}\) turns it into an ordinary polynomial in \(e^{i\varphi}\) of degree at most \(2d\). Hence \(2d+1\) distinct zeros force it to vanish identically. Applying this separately to the two circles reduces the finite measurements to the already-classified continuous equality, without any equispacing assumption. The explicit pair from step 5 proves failure for all sample choices when \(d\geq q\), while step 2 and the degree obstruction in step 3 prove injectivity in every other stated case. \(\square\)

## Verification

The proof is algebraic and covers all complex coefficient vectors, not just generic polynomials. A standalone standard-library checker, `CHECK.py`, constructs explicit equal-modulus degree-\(q\) pairs for intersection denominators \(q=2,\ldots,9\) and checks 11,544 floating-point assertions on the two circles (observed maximum relative squared-intensity discrepancy approximately \(2.05\cdot10^{-15}\)). These finite checks illustrate the construction; the all-degree classification and sharp threshold follow from the six analytical proof steps, not finite sampling.

Reproduce the finite illustration by running `python3 CHECK.py` in the same directory as this document. The checker uses no network access or nonstandard Python packages.

## Relationship to prior work

Chalendar and Partington, *Phase retrieval on circles and lines* (first posted 24 March 2024), Theorem 2.16, prove qualitative two-circle phase retrieval for nontransverse/irrational configurations and construct rational-angle counterexamples. Their Theorem 2.1 proof also establishes an integer-divisibility condition for the first nonzero local Taylor term near an intersection. The present statement does **not** claim that qualitative dichotomy as new. It supplies the stronger global rational-quotient normal form, proves that the **entire reduced rational-map degree** is a multiple of the angle denominator, and deduces the exact finite-polynomial-degree threshold and location-independent \(2d+1\)-per-circle measurement rule. Local Taylor-order divisibility alone does not assert global degree divisibility or give all rational quotients.

Perez's 2020 paper proves uniqueness for irrational-angle segments and two concentric circles, but does not state the rational-angle quotient classification. Hammen's 2015 thesis examines finite polynomial phase retrieval via circles at irrational angles and finite frames; the examined section does not contain this rational-angle cyclic-invariant classification. Earlier concentric-circle phaseless sampling results treat a different geometry: intersecting rational-angle circles admit nonconstant unimodular rational quotients, whereas concentric circles do not.

## Limitations

The results apply to two **complete** Euclidean circles and complex univariate polynomials. The sampling statement gives a sufficient uniform count per circle but does not assert that \(4d+2\) is a globally minimal number of measurements. The normal form is a classification of quotients, not a quantitative noise-stability estimate. The classification is not claimed for partial arcs with arbitrary finite samples or for multivariate polynomials. The local rational-angle constraint is already implicit in the 2024 source; the additional global degree classification and finite-degree implication are the asserted contribution. Possible earlier appearances of the cyclic quotient description remain a historical-priority risk. No independent mathematical validation is claimed.

## References

1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255, initially submitted 24 March 2024, especially Theorems 2.1 and 2.16 and Examples 2.2 and 2.17. https://arxiv.org/abs/2403.16255
2. R. Perez III, *A Note on the Phase Retrieval of Holomorphic Functions*, arXiv:2009.02061, initially submitted 4 September 2020. https://arxiv.org/abs/2009.02061
3. N. Hammen, *Stable Phase Retrieval Using Low-Redundancy Frames of Polynomials*, doctoral thesis, University of Houston, 2015, Section 2.2 (irrational-angle polynomial measurements). https://www.uh.edu/nsm/_docs/math/phd_thesis/2015_2016/nhammenthesisfinal.pdf
