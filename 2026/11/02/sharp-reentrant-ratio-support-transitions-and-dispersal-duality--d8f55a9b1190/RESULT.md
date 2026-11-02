# Sharp reentrant ratio-support transitions and dispersal duality in two-habitat stochastic growth

## Finding

Consider a two-habitat, independently repeated, perfectly anticorrelated two-state environmental growth model, in which the two possible annual growth vectors are \((m_+,m_-)\) and \((m_-,m_+)\), each with probability \(1/2\). Here \(a=m_+/m_->1\), the dispersal fraction is \(0<q<1\), and survival during dispersal is \(0<s\le1\). Let \(\nu_q\) be the unique limiting law of the positive population ratio \(r=x_2/x_1\).

Set
\[
Q_-=\frac{a}{a+s(a^2+a+1)},\qquad
Q_0=\frac1{1+s},\qquad
Q_+=\frac{a^2+a+1}{a^2+a+1+as}.
\]
These satisfy \(0<Q_-<Q_0<Q_+<1\). The following is a complete classification of the topological support of \(\nu_q\):

- For \(0<q\le Q_-\) or \(Q_+\le q<1\), it is a nondegenerate **closed interval**.
- For \(Q_-<q<Q_0\) or \(Q_0<q<Q_+\), it is a **Cantor set** with an explicit open gap around ratio one.
- For \(q=Q_0\), it is precisely the singleton \(\{1\}\).

More explicitly, put \(\theta=qs/(1-q)\), \(\tau=\min(\theta,1/\theta)\) and
\[
R=\frac{a-1+\sqrt{(a-1)^2+4a\tau^2}}{2a\tau},\qquad
X=\frac{R/a+\tau}{1+\tau R/a}.
\]
The support has endpoints \(1/R\) and \(R\) in every regime. When \(Q_-<q<Q_0\) or \(Q_0<q<Q_+\), \(0<X<1\), and the entire interval \((X,1/X)\) is absent from the support. At the two transition values, \(X=1\) and the support is an interval. At \(Q_0\), \(R=X=1\).

There is also an exact **stationary-law dispersal duality**. For
\[
q^\dagger=\frac{1-q}{1-q+s^2q},
\]
we have \(\nu_{q^\dagger}=\nu_q\) as probability measures, not merely equal supports. With lossless movement \(s=1\), this becomes \(\nu_{1-q}=\nu_q\).

## Assumptions and scope

For each integer generation \(t\ge0\), let \(x(t)=(x_1(t),x_2(t))^\mathsf T\) have strictly positive entries and satisfy
\[
x(t+1)=DM(t)x(t),\qquad D=\begin{pmatrix}1-q&qs\\qs&1-q\end{pmatrix}.
\]
Independently from generation to generation, \(M(t)\) is either \(\operatorname{diag}(m_+,m_-)\) or \(\operatorname{diag}(m_-,m_+)\), with equal probability; \(0<m_-<m_+\), \(0<s\le1\), and \(0<q<1\). These assumptions give positive population ratios at every finite time. Here \(\nu_q\) denotes the unique invariant distribution of the one-dimensional ratio chain and also its weak limit from any positive starting ratio. No assertion is made for \(q=0\), \(q=1\), or for non-antiphase environmental switching.

The support means the smallest closed subset of \((0,\infty)\) with \(\nu_q\)-probability one. "Cantor set" means a nonempty compact perfect totally disconnected subset of the real line; no assertion of an exact Hausdorff dimension or density is needed.

## Proof

**1. Ratio recursion and a uniform contraction.** Divide the second component of \(DM(t)x(t)\) by the first. With a fresh equally likely sign \(\epsilon\in\{-1,+1\}\), the ratio obeys
\[
r'=F_{\theta,\epsilon}(r)=\frac{a^\epsilon r+\theta}{1+\theta a^\epsilon r},\qquad \theta=\frac{qs}{1-q}>0.
\]
Write \(u=\log r\), \(L=\log a>0\), and \(\delta=(1-\theta)/(1+\theta)\). The recursion becomes
\[
u'=H_\delta(u+\epsilon L),\qquad H_\delta(z)=2\operatorname{artanh}\!\bigl(\delta\tanh(z/2)\bigr).
\]
Its derivative obeys
\[
\left|H_\delta'(z)\right|=
|\delta|\frac{1-\tanh^2(z/2)}{1-\delta^2\tanh^2(z/2)}
\le |\delta|<1.
\]
Both branches therefore contract globally in log-ratio distance. Standard contraction coupling gives a unique invariant probability and convergence from every positive initial ratio. The associated set operator on nonempty compact subsets is also a strict Hausdorff contraction, so it has a unique nonempty compact attractor, equal to the stationary measure's support since both branch probabilities are positive.

**2. Exact extremal interval and overlap criterion.** Put \(\kappa=|\delta|\), and let \(U>0\) solve \(U=H_\kappa(U+L)\). It exists and is unique when \(\kappa>0\) because the right side is bounded and has derivative bounded by \(\kappa<1\). Inversion of the ratio corresponds to reflection of \(u\), making the extremal interval \([-U,U]\) symmetric. With \(\tau=(1-\kappa)/(1+\kappa)=\min(\theta,1/\theta)\), its upper ratio endpoint \(R=e^U\) satisfies
\[
a\tau R^2+(1-a)R-\tau=0.
\]
The displayed formula for \(R\) is the unique positive root. The two branch images of \([1/R,R]\), in either orientation of the original ratio maps, are exactly
\[
[1/R,X]\quad\text{and}\quad[1/X,R],\qquad
X=\frac{R/a+\tau}{1+\tau R/a}.
\]
They touch or overlap if and only if \(X\ge1\). Because \(z\mapsto(z+\tau)/(1+\tau z)\) is increasing and fixes one for \(0<\tau<1\), this is equivalent to \(R\ge a\). The defining quadratic has one positive root and evaluates at \(a\) to
\[
(a-1)\left[\tau(a^2+a+1)-a\right].
\]
It follows that \(R\ge a\) precisely when \(\tau\le a/(a^2+a+1)\). In the overlap regime, the union of the two images is the entire extremal interval, which by the uniqueness of the compact invariant set must equal the support. In the separated regime, the first images have the strict central gap \((X,1/X)\), and subsequent branch images form a nested binary hierarchy of disjoint intervals of shrinking diameter. The address map from infinite binary sequences is a continuous bijection from the compact binary sequence space to the support, hence a homeomorphism: the support is a Cantor set.

For \(\tau=1\), the two maps are identically one, so the invariant support is \(\{1\}\).

**3. Translate to dispersal thresholds.** Since \(\theta=qs/(1-q)\) increases strictly with \(q\), the overlap inequality \(\min(\theta,1/\theta)\le a/(a^2+a+1)\) is equivalent to \(q\le Q_-\) or \(q\ge Q_+\), while \(\theta=1\) is exactly \(q=Q_0\). This proves all three regimes including equality boundaries.

**4. Equality of the full stationary laws under duality.** Write \(I(r)=1/r\). Direct rational identities give
\[
I\circ F_{\theta,\epsilon}=F_{\theta,-\epsilon}\circ I,
\qquad F_{1/\theta,\epsilon}=I\circ F_{\theta,\epsilon}.
\]
Because the signs have equal probabilities, reflecting any invariant law produces another invariant law at the same \(\theta\). Uniqueness forces \(I_*\nu_\theta=\nu_\theta\). The second identity therefore makes \(\nu_\theta\) invariant also under the system with parameter \(1/\theta\); uniqueness there gives \(\nu_{1/\theta}=\nu_\theta\). Solving \(q^\dagger s/(1-q^\dagger)=1/\theta\) yields exactly \(q^\dagger=(1-q)/(1-q+s^2q)\).

## Verification

The included standalone Python checker uses exact rational fractions to verify branch inversion, dispersal-duality identities, the three threshold equations, the quadratic critical identity, and endpoint orderings across six rational growth contrasts, four movement-survival values, and seven migration fractions per pair. Only consistency checks involving square roots use floating arithmetic. The executed checker reported **2,383 successful assertions**.

As an exact example, \(a=2\) and \(s=1\) give \(Q_-=2/9\), \(Q_0=1/2\), \(Q_+=7/9\). At \(q=1/6\) or \(5/6\) the support is an interval with \(R=(5+\sqrt{33})/4>2\). At \(q=1/3\) or \(2/3\) it is a Cantor set with \(R=(1+\sqrt3)/2<2\). The two paired migration rates in each case yield the **same entire invariant probability law**. These finite checks illustrate, but do not replace, the preceding all-parameter proof.

## Relationship to prior work

Morita and Yoshimura (2012) introduced this two-patch stochastic matrix model and its exact one-dimensional Möbius ratio recursion, and reported a complicated self-similar stationary ratio distribution. Those ingredients are prior work, not claimed as new. The present result applies an explicit contraction and interval-image analysis to give a complete sharp **support topology phase diagram** for the perfectly anticorrelated, equally likely environmental submodel, together with an exact full-distribution dispersal duality.

Barnsley and Vince (2013) cover general contractive and Möbius iterated function systems; the generic compact-attractor theorem and the coding principle are standard ingredients. Their general treatment does not by itself state the derived ecological migration thresholds or the paired stationary-law identity. Morita and Yoshimura (2013) study a different many-patch, globally coupled approximation and its growth statistics. The accessible full texts of these closest papers did not exhibit the present threshold formulas. This is a comparison of the inspected material, not proof that no broader or earlier result exists.

## Limitations

The result concerns the invariant distribution of **relative abundances**, not absolute population survival, the long-run growth exponent, finite-time uncertainty, or the statistical power of field surveys. It requires perfectly anticorrelated binary growth states that are independent across time and equally probable; changing the joint environmental law can change the available ratio maps and the support topology. Degenerate zero or unit migration fractions are excluded. In interval regimes the theorem asserts support, not an absolutely continuous density; in Cantor regimes it does not determine Hausdorff dimension. Historical priority beyond the inspected literature remains open, and no independent scientific audit has been performed.

## References

1. S. Morita and J. Yoshimura, "Analytical Solution of Metapopulation Dynamics in Stochastic Environment," initial public preprint 19 July 2012, arXiv:1207.4618v1; *Physical Review E* **86**, 045102 (2012), doi:10.1103/PhysRevE.86.045102. Model, ratio recursion, stationary-distribution discussion.
2. M. Barnsley and A. Vince, "Developments in fractal geometry," *Bulletin of Mathematical Sciences* **3**, 299–348 (2013), doi:10.1007/s13373-013-0041-3. General IFS contraction, attractor and Möbius theory.
3. S. Morita and J. Yoshimura, "Analytical solution of stochastic model of risk-spreading with global coupling," initial public preprint 30 July 2013, arXiv:1307.7903v1. Many-habitat model and growth statistics.
