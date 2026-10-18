# Arithmetic classification and realization of spectral-radius discontinuities for positive weighted rotations

## Finding

Let \(g\) be any real-valued, real-analytic \(2\pi\)-periodic function. For each \(\alpha\in\mathbb R/\mathbb Z\), let the positive invertible weighted composition operator on \(C(\mathbb T;\mathbb C)\) be
\[
 (W_\alpha f)(e^{i\theta})=e^{g(\theta)}f(e^{i(\theta+2\pi\alpha)}).
\]
Write \(m=\widehat g(0)=(2\pi)^{-1}\int_0^{2\pi}g(\theta)\,d\theta\), and let
\[
 D_g=\{q\ge1:\text{there is an integer }k\ge1\text{ with }q\mid k\text{ and }\widehat g(k)\ne0\}.
\]
Then the map \(\alpha\mapsto r(W_\alpha)\) is continuous at every irrational angle and is discontinuous at a reduced rational angle \(p/q\) **if and only if** \(q\in D_g\). Thus its discontinuity denominators are closed downward under divisibility. More precisely, for every reduced \(p/q\),
\[
 \log r(W_{p/q})=\max_{\theta\in[0,2\pi]}\sum_{j\in\mathbb Z}\widehat g(jq)e^{ijq\theta},\qquad
 \log r(W_\alpha)=m\quad(\alpha\notin\mathbb Q),
\]
and \(\log r(W_{p/q})-m\ge0\). For any \(\rho>0\) for which \(g\) is bounded and holomorphic on a closed substrip \(|\operatorname{Im}z|\le\rho\), with bound \(M_\rho\),
\[
 0\le \log r(W_{p/q})-m\le \frac{2M_\rho e^{-\rho q}}{1-e^{-\rho q}}.
\]

Conversely, **every** subset \(D\subseteq\mathbb N\) closed downward under divisibility, including the empty set, occurs as precisely these discontinuity denominators for a positive weighted rotation family whose weight is arbitrarily close to the constant weight \(1\) in supremum norm. For any \(\eta>0\) set
\[
 g_{D,\eta}(\theta)=2\eta\sum_{k\in D}e^{-k^2}\cos(k\theta),\qquad w_{D,\eta}=e^{g_{D,\eta}}.
\]
The potential extends to an entire periodic function of the complex variable \(\theta\), and at a reduced rational angle
\[
 \log r(W_{p/q})=2\eta\sum_{\substack{\ell\ge1\\\ell q\in D}}e^{-(\ell q)^2}.
\]
This is positive exactly for \(q\in D\). If \(q\in D\), its value is \(2\eta e^{-q^2}(1+O(e^{-3q^2}))\), uniformly as \(q\to\infty\). Thus arbitrary divisor-ideal rational discontinuity patterns, including dense ones, are possible despite arbitrarily small entire-analytic positive weight perturbations.

## Assumptions and scope

The space is the complex Banach lattice \(C(\mathbb T;\mathbb C)\), equipped with the supremum norm and pointwise order on its real part. Here \(r(A)=\lim_{n\to\infty}\|A^n\|^{1/n}\) is the operator spectral radius; positivity is pointwise positivity. Fourier coefficients use the convention \(\widehat g(k)=(2\pi)^{-1}\int_0^{2\pi}g(\theta)e^{-ik\theta}\,d\theta\). All rational numbers are interpreted modulo \(1\), with positive reduced denominator \(q\), including \(0=0/1\). The statement concerns parameter-wise scalar spectral radii, not norm continuity of the operators.

## Proof

**1. Exact rational radius.** For \(\alpha=p/q\) reduced, the \(q\)-fold composition is the identity on the circle. Accordingly, \(W_{p/q}^{q}\) is multiplication by \(\exp(qG_q(\theta))\), where
\[
 G_q(\theta)=\frac1q\sum_{j=0}^{q-1}g(\theta+2\pi jp/q).
\]
Since multiplication by a positive continuous function has spectral radius its maximum, the spectral mapping theorem gives \(\log r(W_{p/q})=\max G_q\). Absolute convergence of the Fourier series of the analytic \(g\), together with the root-of-unity filter, gives
\[
 G_q(\theta)=\sum_{j\in\mathbb Z}\widehat g(jq)e^{ijq\theta}.
\]
Its mean is \(m\). Therefore \(\max G_q\ge m\), with equality exactly when \(G_q\) is constant. Fourier uniqueness and reality of \(g\) show that this constancy is equivalent to \(q\notin D_g\).

**2. Exact irrational radius.** If \(\alpha\) is irrational, then for any nonzero Fourier mode \(e^{ik\theta}\),
\[
 \frac1n\sum_{j=0}^{n-1}e^{ik(\theta+2\pi j\alpha)}
 =e^{ik\theta}\frac{1-e^{2\pi ink\alpha}}{n(1-e^{2\pi ik\alpha})}\longrightarrow0
\]
uniformly in \(\theta\). Approximate the continuous \(g-m\) uniformly by zero-mean trigonometric polynomials to deduce \(n^{-1}\sum_{j<n}g(\theta+2\pi j\alpha)\to m\) uniformly in \(\theta\). The explicit product formula for \(W_\alpha^n\) gives \(\log\|W_\alpha^n\|=\max_\theta\sum_{j<n}g(\theta+2\pi j\alpha)\). Gelfand's formula yields \(\log r(W_\alpha)=m\).

**3. Continuity and the optimal arithmetic restriction.** Every sequence of **distinct** reduced rational angles approaching any fixed angle has denominators tending to infinity: there are only finitely many reduced fractions of bounded denominator on the circle. Analyticity gives \(|\widehat g(k)|\le M_\rho e^{-\rho|k|}\) for any admissible strip width \(\rho\). Consequently \(\sup_\theta|G_q(\theta)-m|\le2M_\rho e^{-\rho q}/(1-e^{-\rho q})\to0\). Irrational angles all have logarithmic radius \(m\), so the radius is continuous at each irrational. At a rational \(p/q\), it is continuous precisely if its own radius equals this common limiting value \(e^m\); otherwise irrational approximants show discontinuity. By step 1 this occurs precisely when \(q\notin D_g\). If \(d\mid q\) and \(q\in D_g\), then \(d\in D_g\), proving downward closure.

**4. Simultaneous inverse realization.** Fix any divisor-downward-closed \(D\). The displayed Fourier series for \(g_{D,\eta}\) converges absolutely and uniformly on every horizontal strip: the Gaussian coefficient \(e^{-k^2}\) dominates \(e^{Ak}\) for any finite \(A\). Thus \(g_{D,\eta}\) is entire, real on the real line and periodic. Its nonzero positive Fourier support is exactly \(D\). In particular \(D_{g_{D,\eta}}=D\), using downward closure. For rational \(p/q\), the root-of-unity filter yields a cosine series with all nonnegative coefficients; its maximum occurs at \(\theta=0\), proving the exact spike formula. If \(q\notin D\), no positive multiple of \(q\) belongs to \(D\), and the spike is zero. If \(q\in D\), the \(\ell=1\) term is positive. Finally \(\|g_{D,\eta}\|_\infty\le2\eta\sum_{k\ge1}e^{-k^2}\) gives
\[
 \|w_{D,\eta}-1\|_\infty\le \exp\!\left(2\eta\sum_{k\ge1}e^{-k^2}\right)-1\longrightarrow0
\]
as \(\eta\downarrow0\). For \(q\in D\), the tail after the first positive term obeys \(\sum_{\ell\ge2}e^{-(\ell q)^2}\le e^{-4q^2}/(1-e^{-5q^2})\), proving the uniform relative error \(O(e^{-3q^2})\). This completes all directions.

## Verification

Each critical assertion reduces to an explicit operator-power identity, a finite geometric series followed by uniform trigonometric approximation, a Fourier projection identity, or a positive-coefficient maximization. None relies on a finite search or numerical conjecture. As an exact illustrative instance, taking \(D\) to be the positive divisors of \(6\) produces discontinuities exactly at rationals whose reduced denominators belong to \(\{1,2,3,6\}\), while all irrationals and other rationals are continuity points. This follows without numerical approximation from the formula in the finding.

## Relationship to prior work

Fixed-operator spectral-radius variational formulas for positive weighted composition operators were known well before this result, including results summarized and extended by Zajkowski (2010). Thus the fixed-angle spectral-radius calculation is **not** claimed as new. Macdonald (1996) studied norms of powers, ergodic averages and decomposability for weighted irrational rotations; Dobrick (2026) gives a general peripheral spectral-cyclicity theorem and an unweighted irrational-rotation example. The additional object classified here is the **set of points at which the spectral radius changes discontinuously as the rotation angle varies for one fixed analytic weight**, together with simultaneous realization of every arithmetically admissible pattern. The Fourier-support obstruction and constructive inverse realization are not assertions of those cited results.

## Limitations

The classification concerns positive, everywhere nonzero analytic weights on \(C(\mathbb T)\); it does not claim an identical structure for sign-changing weights, other base dynamics, or the entire operator spectrum. Earlier equivalent continuity-locus results under ergodic-optimization terminology are a possible publication-priority risk. Finite tests cannot certify novelty; independent mathematical and publication-priority assessment have not been performed.

## References

1. Alexander Dobrick, *On the Cyclicity Conjecture*, arXiv:2610.10093v1 (public 7 October 2026), especially Theorem 1.2 and Example 3.2. https://arxiv.org/html/2610.10093v1
2. Krzysztof Zajkowski, *Spectral radius of weighted composition operators in Lp-spaces*, Studia Mathematica **198** (2010), 301–307. DOI:10.4064/sm198-3-8. https://www.impan.pl/shop/en/publication/transaction/download/product/90271
3. Gordon W. Macdonald, *Decomposable weighted rotations on the unit circle*, Journal of Operator Theory **35** (1996), 205–221. https://www.theta.ro/jot/archive/1996-035-002/1996-035-002-001.pdf
