# The exact power-moment frontier for Rademacher domination of vector martingales

## Finding

For a positive real exponent \(p\), let \(\mathcal D_p\) assert the following universal moment comparison: for every integer \(n\ge1\), every finite-dimensional real Euclidean space, every martingale \((M_j)_{j=0}^n\) starting at zero, and every deterministic choice of nonnegative bounds \(a_1,\ldots,a_n\) satisfying \(\|M_j-M_{j-1}\|\le a_j\) almost surely,
\[
\mathbb E\|M_n\|^p\le
\mathbb E\left|\sum_{j=1}^n a_j\varepsilon_j\right|^p,
\]
where the \(\varepsilon_j\) are independent fair signs.

**The exact exponent classification is**
\[
\boxed{\mathcal D_p\ \text{holds if and only if}\ p=2\ \text{or}\ p\ge3.}
\]
For every \(0<p<2\), a two-step martingale with independent, orthogonal, unit-length increments violates the comparison. For every \(2<p<3\), a three-step, planar, conditionally symmetric martingale with deterministic increment lengths violates it. Conversely, for every \(p\ge2\), **every martingale with at most two steps** obeys the comparison. Thus three is the first possible failure horizon in the subcubic regime.

In particular, the convex-second-derivative sufficient condition of Juškevičius and Šileikis (2026) is sharp in its power exponent for *all adapted Euclidean martingales*, but not merely by a limiting or large-dimensional obstruction.

## Assumptions and scope

The probability space and filtration are arbitrary; only conditional mean zero and the deterministic almost-sure Euclidean increment bounds are required. All moments exist because the number of steps and the increment bounds are finite. The assertion is about ordinary nonnegative real powers \(p>0\) and the **same** individual bounds on both sides. Degenerate zero bounds are permitted. The failure witness uses dimension two and three conditionally symmetric increments. No independence of martingale differences is assumed or needed in the positive direction.

## Proof

**1. The universal positive regimes.** For \(p=2\), martingale orthogonality yields
\[
\mathbb E\|M_n\|^2=\sum_{j=1}^n\mathbb E\|M_j-M_{j-1}\|^2
\le\sum_{j=1}^n a_j^2
=\mathbb E\left|\sum_{j=1}^n a_j\varepsilon_j\right|^2.
\]
For \(p\ge3\), the even function \(f(t)=|t|^p\) is convex and twice continuously differentiable, and \(f''(t)=p(p-1)|t|^{p-2}\) is convex on the real line. Theorem 3 of Juškevičius–Šileikis (arXiv:2610.31449v1) applies in dimension two; the norm-preserving finite-dimensional martingale reduction in their Section 4 extends the same inequality to every Euclidean dimension. This step uses the previously established comparison, not a new proof of it.

**2. A two-step lemma at every exponent \(p\ge2\).** Given a deterministic \(v\) in a Euclidean space and a mean-zero random vector \(X\) with \(\|X\|\le r\) almost surely, define
\[
F_r(s)=\frac{(s+r)^p+|s-r|^p}{2},\qquad s\ge0.
\]
We claim \(\mathbb E\|v+X\|^p\le F_r(\|v\|)\). When \(r=0\) this is immediate; when \(v=0\) it follows from \(\|X\|\le r\). Otherwise let \(e=v/\|v\|\), and choose the affine function \(x\mapsto B+A\langle x,e\rangle\) whose values at \(x=\pm re\) agree with \(\|v+x\|^p\). Here \(B=F_r(\|v\|)\) and
\[
A=\frac{(\|v\|+r)^p-|\|v\|-r|^p}{2r}.
\]
For \(\|x\|=r\), write \(t=\langle x,e\rangle/r\in[-1,1]\). The function
\[
t\longmapsto(\|v\|^2+r^2+2r\|v\|t)^{p/2}
\]
is convex because \(p/2\ge1\); hence it lies below its endpoint chord, precisely the affine majorant. The difference between the convex function \(x\mapsto\|v+x\|^p\) and this affine majorant is convex. Every interior point of the ball is a convex combination of boundary points, so the majorization extends throughout \(\|x\|\le r\). Taking expectations and \(\mathbb E X=0\) proves the claim.

The function \(F_r(s)\) is nondecreasing in \(s\ge0\) for \(p\ge1\), as is immediate by differentiation on \([0,r]\) and \([r,\infty)\). For a two-step martingale, apply the lemma conditionally at step two and note \(\|M_1\|\le a_1\):
\[
\mathbb E\|M_2\|^p\le\mathbb E F_{a_2}(\|M_1\|)
\le F_{a_2}(a_1)
=\mathbb E|a_1\varepsilon_1+a_2\varepsilon_2|^p.
\]
The one-step case is immediate. This proves the stated first-failure horizon.

**3. Failure below quadratic order.** In dimension two take independent fair signs and increments \(\varepsilon_1e_1\), \(\varepsilon_2e_2\), with orthonormal vectors \(e_1,e_2\). Their norm after two steps is identically \(\sqrt2\), so the vector moment equals \(2^{p/2}\), whereas the scalar Rademacher moment equals \(2^{p-1}\). The former is strictly larger exactly when \(0<p<2\).

**4. Strict three-step failure throughout the subcubic gap.** Fix \(0<\delta<1/2\) and independent fair signs \(\xi_1,\xi_2,\xi_3\). Use the predictable increments
\[
D_1=\delta\xi_1e_1,\qquad D_2=\delta\xi_2e_2,\qquad
D_3=\xi_3\frac{D_1+D_2}{\|D_1+D_2\|}.
\]
Each conditional mean is zero; the increment norms are deterministically \(\delta,\delta,1\). Since \(\|D_1+D_2\|=\sqrt2\delta\), the vector moment is
\[
L_p(\delta)=\frac{(1+\sqrt2\delta)^p+(1-\sqrt2\delta)^p}{2}.
\]
The comparison scalar moment is
\[
R_p(\delta)=\frac12+\frac{(1+2\delta)^p+(1-2\delta)^p}{4}.
\]
The real generalized-binomial series converge absolutely for \(2\delta<1\), and subtracting gives the identity
\[
L_p(\delta)-R_p(\delta)
=\sum_{k=2}^{\infty}
\left(2^k-2^{2k-1}\right){p\choose 2k}\delta^{2k}.
\]
For every \(2<p<3\) and every integer \(k\ge2\), the generalized-binomial coefficient \({p\choose2k}\) is strictly negative: there are exactly \(2k-3\) negative factors in its numerator, an odd number. The parenthesized factor is also strictly negative. Thus **each summand is positive**, and \(L_p(\delta)>R_p(\delta)\) for every \(0<\delta<1/2\). More precisely,
\[
L_p(\delta)-R_p(\delta)
=\frac{p(p-1)(p-2)(3-p)}6\,\delta^4+O_p(\delta^6).
\]
This is a strictly positive fourth-order obstruction across the entire open interval \(2<p<3\). Together with the preceding parts it proves the classification and its minimal-horizon assertion. \(\square\)

## Verification

Run the accompanying standalone `verify_power_threshold.py` with Python 3. It uses only the standard library and checks the exact rational generalized-binomial coefficient signs at multiple subcubic exponents and finitely many orders, the quartic coefficient, high-precision evaluations of both comparison moments over a parameter grid, endpoint identities and representative two-step directional cases. The program reports 1191 successful deterministic assertions. These checks corroborate the formulas; **the infinite coefficient signs and universal quantifiers are established analytically above**, not by finite experiments.

## Relationship to prior work

Juškevičius and Šileikis, *Concentration inequalities for vector-valued martingales* (arXiv:2610.31449v1, first public October 22, 2026), Theorem 3 and Section 4, already prove the positive result for the convex-second-derivative class, including all powers \(p\ge3\); this is explicitly reused. Their manuscript does not establish the sharp subcubic obstruction or the two-step minimality result shown here. Pinelis, *Spherically symmetric functions with a convex second derivative and applications to extremal probabilistic problems* (2002), treats the older convex-second-derivative framework and independent/vector-valued generalized-moment comparisons. Neither its relevant applications section nor the newer paper's comparison statement supplies the adapted three-step failure characterization. Earlier comparisons for deterministic Rademacher-weighted vectors are a different problem: the final direction here is random and selected using past signs, so the construction does not settle that independent-vector problem.

## Limitations

This result is confined to finite-dimensional Euclidean martingales with deterministic increment bounds and positive power moments. It does not classify non-power convex test functions, replace moment comparisons by exact tail domination, or extend the threshold to arbitrary Banach norms. The positive \(p\ge3\) half rests on a cited theorem; the additional sharpness and minimality arguments are elementary and self-contained. Historical priority is not certified: a sufficiently general earlier martingale moment-comparison result could conceivably subsume the sharpness statement.

## References

1. T. Juškevičius and M. Šileikis, *Concentration inequalities for vector-valued martingales*, arXiv:2610.31449v1 (2026-10-22), https://arxiv.org/html/2610.31449v1, Theorem 3 and Section 4.
2. I. Pinelis, *Spherically symmetric functions with a convex second derivative and applications to extremal probabilistic problems*, Mathematical Inequalities & Applications 5 (2002), 7–26, https://files.ele-math.com/articles/mia-05-02.pdf, especially Section 4.
3. I. Pinelis, *Rosenthal-type inequalities for martingales in 2-smooth Banach spaces*, Theory of Probability and Its Applications 59 (2015), 699–706, DOI:10.1137/S0040585X97T987417 (context; only the abstract was accessible in this review).
