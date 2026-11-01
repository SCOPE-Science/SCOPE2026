# Three exact growth laws for Ritt defects of finite-range convolution walks

## Finding

A finite-support random walk produces a power-bounded convolution operator whose first-difference norm has exactly one of three asymptotic behaviors. The three possibilities are separated by a finite arithmetic invariant of its support and, on the arithmetic-neutral branch, by its drift.

**Theorem.** Let \(S\subset\mathbb Z\) be finite, with at least two distinct integers. Choose weights \(p_k>0\) for \(k\in S\), satisfying \(\sum_{k\in S}p_k=1\). Define the probability measure \(\mu=\sum_{k\in S}p_k\delta_k\) and the convolution operator \(P\) on \(\ell^2(\mathbb Z)\) by

\[
(Pf)(j)=\sum_{k\in S}p_k f(j-k),\qquad j\in\mathbb Z.
\]

For each positive integer \(n\) put \(D_n=n\|P^n-P^{n-1}\|_{\mathcal B(\ell^2)}\). The integer and moment parameters are

\[
g=\gcd\{|k-\ell|:k,\ell\in S\}>0,\quad
q=\frac{g}{\gcd(g,r)},\quad
m=\sum_{k\in S}kp_k,\quad
v=\sum_{k\in S}(k-m)^2p_k>0,
\]

where \(r\) can be **any** member of \(S\). The integer \(q\) is independent of that choice because all support points are congruent modulo \(g\). Then the following are exact limits:

\[
\begin{array}{ll}
\displaystyle\lim_{n\to\infty}\frac{D_n}{n}=c_q,
& q>1,\\[2mm]
\displaystyle\lim_{n\to\infty}\frac{D_n}{\sqrt n}=\frac{|m|}{\sqrt{e v}},
& q=1,\ m\ne0,\\[3mm]
\displaystyle\lim_{n\to\infty}D_n=e^{-1},
& q=1,\ m=0,
\end{array}
\]

where

\[
c_q=\max_{0\le j<q}|1-e^{2\pi i j/q}|=
\begin{cases}
2,&q\text{ even},\\
2\cos(\pi/(2q)),&q\text{ odd}.
\end{cases}
\]

In particular, \(\sup_{n\ge1}D_n<\infty\), which is the Ritt first-difference condition, holds **if and only if** \(q=1\) and \(m=0\). This is an exact, quantitative result for the \(\ell^2\) norm, not a claim about \(\ell^1\) or pointwise kernel norms.

## Assumptions and scope

All operators act on complex \(\ell^2(\mathbb Z)\). The support is finite, all listed probabilities are strictly positive, and at least two distinct integers have positive mass. These conditions ensure a nonzero lattice span and strictly positive variance. No symmetry of the measure is required; the support may lie in a nontrivial sublattice.

For completeness, if the measure has a single support atom, then \(P\) is an integer translation unitary. For \(\mu=\delta_0\), \(D_n=0\) for all \(n\); for \(\mu=\delta_k\) with \(k\ne0\), \(D_n=2n\) for all \(n\).

We use the standard bounded-power formulation: a power-bounded operator is Ritt when \(\sup_{n\ge1}n\|P^n-P^{n-1}\|<\infty\). Since \(P\) is an average of translations, \(\|P\|\le1\), so the power-bounded hypothesis is automatic.

## Proof

**1. Exact multiplier representation.** The unitary Fourier transform from \(\ell^2(\mathbb Z)\) to \(L^2(\mathbb T)\) turns convolution into multiplication by the trigonometric polynomial

\[
\phi(t)=\sum_{k\in S}p_k e^{ikt},\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]

A harmless sign change in the Fourier convention conjugates this expression and does not alter any modulus below. As the multiplier is continuous, its essential supremum is its maximum. Therefore the exact identity is

\[
D_n=n\max_{t\in[0,2\pi]}|\phi(t)|^{n-1}|1-\phi(t)|.\tag{1}
\]

For any \(t\), the triangle inequality gives \(|\phi(t)|\le1\), with equality if and only if all \(e^{ikt}\), \(k\in S\), are the same complex number. Since all masses are positive, equality entails \(e^{i(k-\ell)t}=1\) for all support pairs. By the integer Bézout identity this holds exactly at

\[
t_j=2\pi j/g,\qquad j=0,1,\ldots,g-1.
\]

At such a point, \(\phi(t_j)=\zeta_j=e^{2\pi i jr/g}\). Moreover, for every real \(u\),

\[
\phi(t_j+u)=\zeta_j\phi(u),\qquad |\phi(t_j+u)|=|\phi(u)|.\tag{2}
\]

The set of distinct \(\zeta_j\) is exactly the set of \(q\)-th roots of unity: the order of \(e^{2\pi i r/g}\) equals \(q=g/\gcd(g,r)\).

**2. Nontrivial peripheral phases.** Suppose \(q>1\). At \(t_j\), identity (1) gives \(D_n/n\ge|1-\zeta_j|\), uniformly in \(n\); hence \(\liminf_nD_n/n\ge c_q\). Fix any sufficiently small pairwise disjoint neighborhoods of the finitely many \(t_j\). On the closed complement, the strict inequality \(|\phi|<1\) is uniform, so the quantity \(|\phi|^{n-1}|1-\phi|\) tends uniformly to zero. On each neighborhood, it is at most \(|1-\phi|\), and uniform continuity bounds its limsup by \(|1-\zeta_j|\) plus a quantity tending to zero as the neighborhood shrinks. Thus \(\limsup_nD_n/n\le c_q\). A point on the unit circle furthest from \(1\) is \(-1\) when \(q\) is even; for odd \(q\), the two nearest \(q\)-th roots to \(-1\) give \(2\cos(\pi/(2q))\). This proves the first case.

**3. Local expansions when every peripheral phase equals one.** Suppose \(q=1\). Equation (2) makes \(\phi\) locally identical near every peripheral point. At the origin, Taylor's theorem for this finite trigonometric polynomial gives

\[
\phi(u)=1+imu-\tfrac12(v+m^2)u^2+O(|u|^3),\qquad
|\phi(u)|=1-\tfrac12vu^2+O(|u|^4).\tag{3}
\]

The even-order remainder in the modulus follows because \(|\phi(u)|^2\) is an even real-analytic function of \(u\), with quadratic coefficient \(-v\). Since \(v>0\), there are positive \(c\), \(\delta\) such that \(|\phi(u)|\le e^{-c u^2}\) whenever \(|u|\le\delta\). Taylor expansion also gives, for \(u\to0\),

\[
|1-\phi(u)|=
\begin{cases}
|m|\,|u|+O(u^2),&m\ne0,\\
\tfrac12v u^2+O(|u|^3),&m=0.
\end{cases}\tag{4}
\]

Outside fixed small neighborhoods of the \(t_j\), there is a \(\rho<1\) with \(|\phi(t)|\le\rho\), so the corresponding portion of (1) is at most \(2n\rho^{n-1}\), which is negligible even after normalization by \(\sqrt n\). Inside the neighborhoods, (2) reduces to studying the origin only.

**4. Rescaled maximization.** Put \(u=x/\sqrt n\). Uniformly for \(x\) in each compact interval, (3) implies

\[
|\phi(x/\sqrt n)|^{n-1}\longrightarrow e^{-vx^2/2}.
\]

When \(m\ne0\), (4) gives the locally uniform limit

\[
\frac{n}{\sqrt n}|\phi(x/\sqrt n)|^{n-1}|1-\phi(x/\sqrt n)|
\longrightarrow |m|\,|x|e^{-vx^2/2}.\tag{5}
\]

When \(m=0\), the locally uniform limit is instead

\[
n|\phi(x/\sqrt n)|^{n-1}|1-\phi(x/\sqrt n)|
\longrightarrow \tfrac12v x^2e^{-vx^2/2}.\tag{6}
\]

These are **global maximization limits**, not merely pointwise asymptotics. Indeed, for \(|u|\le\delta\), equations (3)--(4) provide a constant \(C\) with \(|1-\phi(u)|\le C|u|\) in the noncentered case and \(|1-\phi(u)|\le C u^2\) in the centered case. Combining these estimates with \(|\phi(u)|^{n-1}\le e^{-c(n-1)u^2}\), the normalized rescaled integrands in (5)--(6) are bounded, for \(n\ge2\), respectively by \(C|x|e^{-cx^2/2}\) and \(Cx^2e^{-cx^2/2}\). Both bounds vanish uniformly as \(|x|\to\infty\). Compact convergence plus these tails therefore allows maxima to be passed to the limit. The maximizers of \(|x|e^{-vx^2/2}\) have \(|x|=1/\sqrt v\), whereas those of \((vx^2/2)e^{-vx^2/2}\) have \(|x|=\sqrt{2/v}\). Their maxima are \(1/\sqrt{ev}\) and \(e^{-1}\), respectively. Equations (5)--(6) prove the second and third cases.

**5. The Ritt criterion and one-atom boundaries.** In the first two regimes \(D_n\) diverges, because \(c_q>0\) and \(v>0,\ m\ne0\). In the centered \(q=1\) regime, \(D_n\to e^{-1}\), so \(\sup_nD_n<\infty\). Since \(\|P^n\|\le1\), this is exactly the Ritt criterion. For a single atom \(\delta_k\), the multiplier is \(e^{ikt}\), giving \(D_n=n\max_t|1-e^{ikt}|\): the asserted two degenerate cases follow. This completes the proof.

## Verification

The accompanying standalone `checker.py` checks exact rational support, span, moment and parity identities, and compares finite sampled multiplier maxima with the predicted asymptotic constants across centered, drifting, and resonant walks. It also includes non-strictly-aperiodic examples supported on proper sublattices, where the integer \(q\) remains decisive. The calculations are supportive finite tests only; the preceding analytical argument supplies all infinite-dimensional and asymptotic conclusions.

To reproduce: run `python3 checker.py` with a standard Python 3 interpreter. No third-party packages or network are required. The code reports `CHECK_OK` after completing the listed checks. The tested Fourier-frequency grid is finite and does **not** certify a continuum maximum or a limit.

## Relationship to prior work

Borichev, Gomilko and Tomilov (2026) establish abstract functional-calculus and Beurling--Kato characterizations of Ritt operators, along with examples and permanence results. Their Sections 6 and 8 do not state this finite-range convolution multiplier trichotomy or its exact leading constants.

Cuny (2016) proves the Ritt property for centered, strictly aperiodic probabilities with a second moment in the stronger \(\ell^1\) setting (Theorem 1.6), and presents the bounded angular ratio characterization in \(\ell^p\) for \(p>1\) (Theorem 1.3). Accordingly, the centered qualitative criterion on the strictly aperiodic subclass is **not** new. The theorem here concerns the exact \(\ell^2\) defect limits for **all finite supports**, including nontrivial peripheral root phases, nonzero drift, and support in a proper sublattice; those constants and the three-way joint classification are not contained in the statements just cited.

Diaconis and Saloff-Coste (2012 preprint) investigate convolution-power local limit behavior. Their Theorem 3.5 gives pointwise local-limit bounds for multiple peripheral maxima, and Section 3.1 gives local Fourier expansions; neither states the exact global \(\ell^2\) power-difference maximum or the q-dependent root constants. Nevertheless, the Gaussian localization method is classical and a broader historical theorem could indirectly imply parts of the present statement.

## Limitations

This theorem is specific to finite-support nonnegative probability laws on \(\mathbb Z\) and the operator norm on \(\ell^2(\mathbb Z)\). It does not imply matching \(\ell^1\) norm asymptotics, sharp finite-\(n\) maxima, estimates for infinite-support laws, or arbitrary signed/complex convolution kernels. None of the finite grid checks substitutes for the analytic proof. Novelty is based on accessible published sources and comparisons, not a proof that no equivalent theorem exists in all literature. Independent validation has not been performed.

## References

1. A. Borichev, A. Gomilko and Yu. Tomilov, *Beurling--Kato theory, Hardy--Sobolev calculus and Ritt operators*, arXiv:2607.10507 (first public July 11, 2026), especially Sections 6 and 8. https://arxiv.org/abs/2607.10507
2. C. Cuny, *On the Ritt property and weak type maximal inequalities for convolution powers on* \(\ell^1(\mathbb Z)\), *Studia Mathematica* 235 (2016), 47–85, Theorems 1.3 and 1.6, DOI:10.4064/sm8516-8-2016. https://www.impan.pl/shop/en/publication/transaction/download/product/91807
3. P. Diaconis and L. Saloff-Coste, *Convolution powers of complex functions on* \(\mathbb Z\), arXiv:1205.6490 (2012). https://arxiv.org/abs/1205.6490
