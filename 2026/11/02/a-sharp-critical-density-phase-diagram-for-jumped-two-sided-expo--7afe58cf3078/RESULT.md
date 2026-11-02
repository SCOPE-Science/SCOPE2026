# A sharp critical-density phase diagram for jumped two-sided exponential Gabor windows

## Finding
Fix \(\lambda>0\) and \(c>0\), and consider the **jumped two-sided exponential**
\[
g_{\lambda,c}(t)=
\begin{cases}
e^{-\lambda t},&t\ge0,\\
c e^{\lambda t},&t<0.
\end{cases}
\]
Write \(r=e^{-\lambda}\in(0,1)\). For the critical-density Gabor system
\[
\mathcal G_{\lambda,c}=\{M_mT_ng_{\lambda,c}:m,n\in\mathbb Z\},\qquad
(M_mT_ng)(t)=e^{2\pi i mt}g(t-n),
\]
the *optimal squared frame bounds* (allowing zero as the optimal lower Bessel inequality constant in the nonframe cases) are
\[
\boxed{A_{\lambda,c}=\left(\frac{\max\{r-c,cr-1,0\}}{1+r}\right)^2},\qquad
\boxed{B_{\lambda,c}=\left(\frac{\max\{1+cr,c+r\}}{1-r}\right)^2}.
\]
In particular, the system is a frame, equivalently a Riesz basis at this density, **if and only if**
\[
\boxed{0<c<e^{-\lambda}\quad\text{or}\quad c>e^{\lambda}}.
\]
Every \(e^{-\lambda}\le c\le e^{\lambda}\) is a nonframe, even though all but the single value \(c=1\) give a genuinely discontinuous window at the origin.

The frame/Bessel operator \(S_{\lambda,c}\) has spectrum exactly
\[
\sigma(S_{\lambda,c})=[A_{\lambda,c},B_{\lambda,c}],
\]
and has no eigenvalues, including throughout the nonframe region.

At the left transition the exact formula is \(A_{\lambda,c}=(r-c)^2/(1+r)^2\) for \(0<c<r\); at the right it is \(A_{\lambda,c}=r^2(c-r^{-1})^2/(1+r)^2\) for \(c>r^{-1}\). Thus both onsets are exactly quadratic. Every finite positive \(c\) belonging to either frame phase satisfies the **strict conditioning barrier**
\[
\boxed{\frac{B_{\lambda,c}}{A_{\lambda,c}}>
\left(\frac{1+r}{r(1-r)}\right)^2}.
\]
The right-hand value is the sharp infimum, reached only in the limiting one-sided regimes \(c\to0^+\) or, after normalization by \(c\), \(c\to\infty\). In particular, adding a positive opposite-side exponential tail never improves critical-density frame conditioning.

## Assumptions and scope
The ambient Hilbert space is \(L^2(\mathbb R)\), with the standard unnormalized inner product and counting measure on the integer Gabor lattice. Every claim is for each real \(\lambda>0\) and \(c>0\), without a compactness assumption on these parameters. The frame inequality is
\[
A\|f\|_2^2\le \sum_{m,n\in\mathbb Z}|\langle f,M_mT_ng_{\lambda,c}\rangle|^2\le B\|f\|_2^2
\quad(f\in L^2(\mathbb R)).
\]
The value at the single jump point \(t=0\) does not change the assertions. All endpoints in the formulas denote essential lower/upper bounds, not necessarily attained on a set of positive Zak measure. The spectrum assertion concerns the bounded positive frame operator even when its lower bound is zero.

## Proof
**1. Zak reduction with explicit normalization.** On \(0<x<1\), set \(\theta=2\pi\omega\), \(z=e^{i\theta}\), \(r=e^{-\lambda}\), \(P_x=e^{-\lambda x}\), and \(Q_x=cr e^{\lambda x}\). With the unitary Zak convention
\[
Zg(x,\omega)=\sum_{n\in\mathbb Z}g(x+n)e^{2\pi i n\omega},
\]
absolute convergence follows from the exponential tails, and the two geometric series give
\[
\boxed{Zg_{\lambda,c}(x,\omega)=\frac{P_x}{1-rz}+\frac{Q_x}{z-r}.}\tag{1}
\]
The unitary Zak transform sends \(M_mT_ng\) to a character times \(Zg\). By Fourier Parseval on the unit square, the analysis frame inequality is therefore equivalent to
\[
A\le |Zg_{\lambda,c}(x,\omega)|^2\le B\quad\text{a.e. on }(0,1)^2.
\]
Thus the best constants are precisely the essential infimum and supremum of the squared multiplier; no further normalization factor occurs at unit lattice parameters.

**2. Exact frequency extrema.** Since \(|z-r|=|1-rz|\) for \(|z|=1\) and \(1-r\le |1-rz|\le1+r\), the triangle and reverse-triangle inequalities applied to (1) give
\[
\frac{|P_x-Q_x|}{1+r}\le|Zg_{\lambda,c}(x,\omega)|
\le\frac{P_x+Q_x}{1-r}.
\]
Both bounds are **equalities at explicit frequencies**: at \(z=-1\), the expression equals \((P_x-Q_x)/(1+r)\), and at \(z=1\) it equals \((P_x+Q_x)/(1-r)\). Hence for every \(0<x<1\) these are the exact minimum and maximum over frequency. Continuity ensures that the essential extrema over \(x\) have the same endpoint limits as the ordinary extrema.

**3. Exact position extrema.** The function \(D(x)=P_x-Q_x=e^{-\lambda x}-cr e^{\lambda x}\) is strictly decreasing, with \(D(0)=1-cr\) and \(D(1)=r-c\). Its minimum absolute value on the closed interval is therefore
\[
\min_{0\le x\le1}|D(x)|=\max\{r-c,cr-1,0\}.
\]
The sum \(E(x)=P_x+Q_x\) is strictly convex, so its maximum occurs at an endpoint; those values are \(E(0)=1+cr\) and \(E(1)=r+c\). Substitution yields exactly the announced optimal constants. Positivity of the lower one is equivalent to \(c<r\) or \(c>r^{-1}\), and a critical-density Gabor frame is automatically a Riesz basis by Zak diagonalization.

**4. Spectrum and absence of eigenvalues.** Under the same unitary map the positive frame operator is multiplication by the nonnegative function \(|Zg|^2\). Formula (1) is real-analytic in \((x,\theta)\) on the connected open cylinder \((0,1)\times\mathbb T\), and not constant there (at fixed \(x\), its frequency maximum and minimum differ unless a degenerate identity held for every \(x\), which the strictly decreasing \(D\) excludes). Its continuous image on this connected domain is an interval. The essential-range closure is therefore precisely the full interval from the extrema computed above. A level set of a nonconstant real-analytic function has two-dimensional Lebesgue measure zero, so the multiplication operator has no nonzero-measure eigenlevel set and hence no eigenvalues.

**5. Sharp onsets and conditioning.** The lower-bound expressions in the two frame regions are exact squares, proving the asserted quadratic transition coefficients. For \(0<c<r\), the ratio of upper to lower bounds is
\[
\frac{B}{A}=
\left(\frac{1+r}{1-r}\frac{1+cr}{r-c}\right)^2;
\]
for \(c>r^{-1}\), it is
\[
\frac{B}{A}=
\left(\frac{1+r}{1-r}\frac{c+r}{cr-1}\right)^2.
\]
In the first range \((1+cr)/(r-c)>1/r\) because \(c(1+r^2)>0\). In the second range \((c+r)/(cr-1)>1/r\) because \(1+r^2>0\). Both ratios approach \(1/r\) as \(c\to0^+\) and \(c\to\infty\), respectively. This proves the strict inequality and the sharp unattained infimum.

## Verification
The bundled `verify.py` uses only the Python standard library. It independently checks the two-sided geometric series against truncated Zak sums, tests both frequency extremizers, scans all four critical/noncritical amplitude regimes and both thresholds, verifies that computed interior zeros occur precisely within the predicted nonframe interval, and tests the condition-number inequality. A completed execution passed **81,136 supplementary assertions** across four decay rates and multiple jump amplitudes. This finite test is not an infinite proof; the five analytical steps above establish the results for all \(\lambda,c>0\).

To reproduce: run `python verify.py` using Python 3. No external data, libraries, paper downloads or network access are required.

## Relationship to prior work
Gröchenig (arXiv:2301.00857, 2023-01-02) proves the critical-density nonframe conclusion for integrable totally positive continuous two-sided exponentials and their more general class on rational lattices. The present \(c\ne1\) windows have a jump and fall outside the continuous two-sided family; the cited theorem does not determine either of their two surviving frame regions or their sharp frame bounds. Kloos and Stöckler (arXiv:1311.7359, especially Section 5) study continuous even two-sided exponentials and noncritical density parameters, not this jump-amplitude phase diagram. Faulhuber and Shafkulovska (arXiv:2204.02917, Sections 2.3, 2.4, 7 and 8) obtain lattice and conditioning optimization for separate **one-sided** and **continuous two-sided** windows, rather than a positive bilateral jumped family at critical density. Janssen's 2003 analysis of critical-density tight-frame generation addresses smooth even two-sided exponentials with a single Zak zero.

The present calculation uses classical Zak diagonalization as an established method; its claim is the full sharp classification and exact quantitative spectral/conditioning behavior of the explicitly defined jumped family, not the method itself.

## Limitations
Only equal positive exponential decay rates on the two half-lines and the integer time-frequency lattice are treated; independently chosen left/right decay exponents or noncritical lattice geometries are not classified. The no-eigenvalues statement does not by itself assert a particular formula for spectral density. The precise numerical conditioning constants refer to this unnormalized window definition. Historical novelty has been checked against the specified close sources and published mathematical search results, but an older equivalent piecewise-exponential special case remains possible without an exhaustive literature search. Independent mathematical validation has not been performed.

## References
1. K. Gröchenig, *Totally Positive Functions and Gabor Frames over Rational Lattices*, arXiv:2301.00857v1 (2023-01-02), https://arxiv.org/abs/2301.00857.
2. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917v1 (2022-04-06), https://arxiv.org/html/2204.02917v2.
3. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1 (2013-11-28), https://arxiv.org/abs/1311.7359.
4. A. J. E. M. Janssen, *On generating tight Gabor frames at critical density*, Journal of Fourier Analysis and Applications 9 (2003), 175–214, DOI:10.1007/s00041-003-0011-3.
