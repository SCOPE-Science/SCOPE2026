# An exact cutoff crossing and two macroscopic regimes for finite Charlier--Hermite spectra

## Finding

Let \(N\geq1\) and \(t>0\). Define the real symmetric \(N\)-by-\(N\) Jacobi matrix \(J_N(t)\), with rows and columns indexed by \(0,\ldots,N-1\), by
\[
 (J_N(t))_{jj}=j+t,\qquad
 (J_N(t))_{j,j+1}=(J_N(t))_{j+1,j}=\sqrt{t(j+1)}.
\]
Write its eigenvalues in increasing order as
\(0<\lambda_{0,N}(t)<\cdots<\lambda_{N-1,N}(t)\), and put \(\mu_N(t)=\lambda_{0,N}(t)\). The following statements hold.

**Exact crossing.** For every \(N\geq1\) and \(t>0\),
\[
 \mu_N(t)<1\iff t<N,\qquad
 \mu_N(N)=1,\qquad
 \mu_N(t)>1\iff t>N.
\]
The polynomial identity behind the crossing is
\[
 \det(J_N(t)-I)=t^{N-1}(t-N).
\]

**Exact reciprocal spectral trace.** For all \(N\geq1\) and \(t>0\),
\[
 \sum_{j=0}^{N-1}\frac1{\lambda_{j,N}(t)}
 =\frac{N!}{t^N}\sum_{k=0}^{N-1}\frac{t^k}{k!(N-k)}.
\]

**Macroscopic subcritical regime.** For every fixed \(\rho\in(0,1)\), as \(N\to\infty\),
\[
 \mu_N(\rho N)
 =(1-\rho)\frac{(\rho N)^Ne^{-\rho N}}{(N-1)!}
 \bigl(1+O_\rho(N^{-1})\bigr)
 =(1-\rho)\sqrt{\frac N{2\pi}}
 \bigl(\rho e^{1-\rho}\bigr)^N
 \bigl(1+O_\rho(N^{-1})\bigr).
\]

**Macroscopic supercritical regime.** For every fixed \(\rho>1\),
\[
 \lim_{N\to\infty}\frac{\mu_N(\rho N)}N
 =(\sqrt\rho-1)^2.
\]

Thus the spectral floor is exponentially small when the displacement parameter is a fixed fraction below the Hermite cutoff, equals exactly one at the cutoff, and has a positive order-\(N\) limit above it. This constitutes a single sharp three-regime description, with exact finite-cutoff crossing and the leading coefficient in the small-eigenvalue regime.

## Assumptions and scope

The Jacobi matrix is the finite-section representation of a displaced one-dimensional harmonic oscillator. With \(Xf(x)=xf(x)\), \(Pf(x)=-if'(x)\), and normalized Hermite functions \((h_j)_{j\geq0}\) for \(X^2+P^2\), let \(\Pi_N\) project onto \(\operatorname{span}\{h_0,\ldots,h_{N-1}\}\). For \(a,b\in\mathbb R\) not both zero, set \(t=(a^2+b^2)/2\). A diagonal unitary gauge makes
\[
 \left.\Pi_N\bigl((X-a)^2+(P-b)^2\bigr)\Pi_N\right|_{\operatorname{ran}\Pi_N}
 \quad\text{unitarily equivalent to}\quad I+2J_N(t).
\]
Consequently, the optimal finite-Hermite **additive** uncertainty energy equals \(1+2\mu_N(t)\). The theorem makes no claim about minimizing the **product** of the two individual variances, and the oscillator is understood in the standard self-adjoint realization with \([X,P]=iI\).

The asymptotic statements keep \(\rho\) fixed separately in \((0,1)\) or \((1,\infty)\). No uniformity as \(\rho\to1\) is asserted, and no critical-window asymptotic is claimed. The first two identities are exact for every finite \(N\) and positive \(t\).

## Proof

**1. Oscillator and Charlier Jacobi representation.** Let \(\mathfrak a=(X+iP)/\sqrt2\) and \(\mathfrak a^*=(X-iP)/\sqrt2\). Then \(X^2+P^2=2\mathfrak a^*\mathfrak a+I\), and \(\mathfrak a h_j=\sqrt j\,h_{j-1}\). The linear term in the displacement has a complex coefficient with absolute value \(2\sqrt t\). Removing its phase by a diagonal unitary produces \(I+2J_N(t)\). Write \(A_N\) for the strict upper shift with entries \((A_N)_{j,j+1}=\sqrt{j+1}\). The upper bidiagonal matrix \(B_N(t)=\sqrt t I+A_N\) satisfies
\[
 J_N(t)=B_N(t)^*B_N(t).
\]
Since \(B_N(t)\) is invertible for \(t>0\), all eigenvalues are positive. Irreducibility gives distinct eigenvalues. The Jacobi recurrence is the usual normalized Charlier recurrence; no identification of its degree-dependent parameter with a fixed-parameter asymptotic is made.

**2. Exact crossing.** Put \(D_j(x;t)=\det(J_j(t)-xI)\), with \(D_0=1\), \(D_1=t-x\). Expansion along the final row gives
\[
 D_j(x;t)=(j-1+t-x)D_{j-1}(x;t)-t(j-1)D_{j-2}(x;t).
\]
At \(x=1\), induction yields \(D_j(1;t)=t^{j-1}(t-j)\): substituting the expressions for \(j-1\) and \(j-2\) reduces the bracket to \(t(t-j)\).

Let \(J_\infty(t)\) be the infinite Jacobi operator formed with the same coefficients. It is unitarily equivalent by the Weyl displacement operator to the nonnegative number operator, hence has eigenvalues \(0,1,2,\ldots\). The Rayleigh--Ritz min--max principle for its \(N\)-dimensional compression gives \(\lambda_{j,N}(t)\geq j\) for every \(j\), in particular \(\lambda_{j,N}(t)\geq1\) for \(j\geq1\). The interlacing with the leading \(N\)-by-\(N\) principal section of \(J_{N+1}(t)\) is strict, since the Jacobi off-diagonal entries are nonzero and the two characteristic polynomials have no common zero. Therefore \(\lambda_{j,N}(t)>\lambda_{j,N+1}(t)\geq j\) for \(1\leq j<N\), with the last inequality supplied by infinite-operator min--max. Thus every eigenvalue other than the lowest is strictly greater than one. It follows that the sign of \(D_N(1;t)\) equals the sign of \(\mu_N(t)-1\). Because \(t^{N-1}>0\), the crossing follows, including equality at \(t=N\).

An independent explicit witness at \(t=N\) is the eigenvector with components
\[
 v_j=(-1)^j\frac{N^{j/2}}{\sqrt{j!}}\left(1-\frac jN\right),
 \qquad0\leq j<N.
\]
The Jacobi recurrence verifies \(J_N(N)v=v\); after alternating signs, its components are strictly positive, confirming that it represents the bottom eigenvalue. The crossing statement also covers \(N=1\), where \(J_1(t)=(t)\).

**3. Reciprocal trace.** Inverting the triangular factor explicitly gives, for \(0\leq i\leq j<N\),
\[
 (B_N(t)^{-1})_{ij}=(-1)^{j-i}
 \sqrt{\frac{j!}{i!}}\,t^{-(j-i+1)/2},
\]
and zero below the diagonal. Hence
\[
 \operatorname{tr}J_N(t)^{-1}
 =\lVert B_N(t)^{-1}\rVert_{\mathrm{HS}}^2
 =\sum_{j=0}^{N-1}\sum_{i=0}^j
 \frac{j!}{i!t^{j-i+1}}.
\]
Grouping terms by \(p=j-i+1\), and using the hockey-stick binomial identity, the coefficient of \(t^{-p}\) is
\[
 \sum_{i=0}^{N-p}\frac{(i+p-1)!}{i!}
 =(p-1)!\binom Np=\frac{N!}{p(N-p)!}.
\]
Replacing \(p\) by \(N-k\) gives the asserted exact formula.

**4. Subcritical asymptotics.** For \(t=\rho N\), let \(K\) be Poisson with mean \(\rho N\). The reciprocal trace formula becomes exactly
\[
 S_N(\rho N):=\operatorname{tr}J_N(\rho N)^{-1}
 =\frac{(N-1)!e^{\rho N}}{(\rho N)^N}
 \mathbb E\!\left[\frac{N}{N-K}\mathbf 1_{\{K<N\}}\right].
\]
Fix \(0<\rho<1\). On the event
\(\lvert K-\rho N\rvert\leq\frac12(1-\rho)N\), Taylor expansion of \(N/(N-K)\) around \(K=\rho N\), together with \(\mathbb E(K-\rho N)=0\) and \(\mathbb E(K-\rho N)^2=\rho N\), yields \((1-\rho)^{-1}+O_\rho(N^{-1})\). Outside the event the Poisson Chernoff bound is exponentially small; the truncated integrand is at most \(N\), so the tail is negligible. Consequently
\[
 S_N(\rho N)
 =\frac{(N-1)!e^{\rho N}}{(\rho N)^N}
 \left(\frac1{1-\rho}+O_\rho(N^{-1})\right).
\]
The base \(\rho e^{1-\rho}\) lies strictly between zero and one. Stirling's formula implies \(S_N(\rho N)\) grows exponentially. The min--max bound from Step 2 gives
\[
 0\leq S_N(\rho N)-\frac1{\mu_N(\rho N)}
 =\sum_{j=1}^{N-1}\frac1{\lambda_{j,N}(\rho N)}
 \leq\sum_{j=1}^{N-1}\frac1j=O(\log N).
\]
Thus \(\mu_N(\rho N)=S_N(\rho N)^{-1}(1+o(N^{-m}))\) for each fixed positive integer \(m\). Inverting the expectation expansion and applying Stirling gives the two asserted subcritical formulas, including the relative \(O_\rho(N^{-1})\) remainder.

**5. Supercritical asymptotics.** Let \(t=\rho N\) with fixed \(\rho>1\). The strict upper shift has \(\lVert A_N\rVert=\sqrt{N-1}\). Therefore, for every vector \(w\),
\[
 \lVert B_N(\rho N)w\rVert
 \geq(\sqrt{\rho N}-\sqrt{N-1})\lVert w\rVert,
\]
which proves
\[
 \liminf_{N\to\infty}\frac{\mu_N(\rho N)}N
 \geq(\sqrt\rho-1)^2.
\]
For the reverse bound, let \(L=\lfloor\sqrt N\rfloor\), and choose a unit vector supported on indices \(N-L,\ldots,N-1\) with coordinates \(w_j=(-1)^jf_j\), where \(f_j\geq0\) is a normalized discrete sine arch that vanishes immediately outside that index interval. The shift difference satisfies \(\lVert f-\operatorname{shift} f\rVert=O(L^{-1})\), and the varying coefficients obey \(\sqrt{j+1}=\sqrt N+O(L/\sqrt N)\) on the support. Thus
\[
 \frac{\lVert B_N(\rho N)w\rVert}{\sqrt N}
 \leq\sqrt\rho-1+O(L^{-1}+L/N).
\]
The Rayleigh quotient of \(B_N^*B_N\) on \(w\) yields the matching upper limit. This proves the supercritical formula.

## Verification

The standalone `verify.py` checks, using exact fractions, the determinant identity and both expressions for the reciprocal trace for twenty matrix sizes and five rational parameters; it also checks the explicit critical eigenvector numerically for thirty sizes and the Poisson expectation prefactor in four subcritical parameter regimes. Its last successful run reported `PASS 250 checks`. These checks reproduce finite identities and asymptotic trends only; the uniform quantifiers and infinite limits follow from the proof above. Reproduction requires Python 3 standard library only; run `python3 verify.py` from the containing directory.

## Relationship to prior work

Williams, Ortelli and Silva (arXiv:2609.17970, first public September 16, 2026) develop the displaced oscillator's **infinite** tridiagonal Hermite representation and its exact infinite spectrum. Their results motivate the finite-section problem, but do not state the unit crossing or the degree-and-displacement-scaled lowest-eigenvalue asymptotics above. Dominici (arXiv:1406.6193) develops fixed-parameter Charlier Mehler--Heine asymptotics; his 2018 higher-order sequel likewise treats fixed degree-independent Charlier parameters. Those statements do not cover \(t=\rho N\). Soria-Lorente and Michel (arXiv:2608.27495) study Mehler--Heine limits for modified discrete orthogonal polynomials rather than this joint scaling. Nilsson (arXiv:1202.2557) establishes the Charlier-to-Hermite transition near the degree-parameter matching scale, not the two fixed-ratio outer regimes. Kuijlaars and Van Assche (1999) address global discrete polynomial zero distributions and largest zeros, rather than the exact first-zero cutoff crossing and the exponentially small first zero. Krasikov and Zarkh (2008) develop bounds for extreme discrete-polynomial zeros; an exact comparable joint-scaling statement was not established from accessible material. Knessl and van Leeuwaarden (2015) give exact transforms for first-passage laws in immigration--death and related queues, so their denominator polynomials overlap the spectral object, but their inspected asymptotic treatment concentrates on Halfin--Whitt critical scaling rather than the sharp fixed-ratio outer laws and finite unit crossing here. The general Charlier recurrence and standard spectral min--max theory are classical inputs and are not asserted to be new.

The mathematical contribution claimed here is the conjunction of the **exact finite critical crossing**, an **exact inverse-trace identity yielding a sharp subcritical prefactor**, and the **supercritical scaled least-eigenvalue law** for this same natural finite-section problem. Existing literature may contain equivalent statements under birth--death or queueing terminology; that is a residual originality risk, not an assumption of uniqueness.

## Limitations

These statements concern the bottom eigenvalue of the one-dimensional displaced oscillator compressed to the consecutive lowest \(N\) Hermite modes. They do not establish a critical-window distribution at \(t=N+O(\sqrt N)\), higher-eigenvalue asymptotics, arbitrary nonconsecutive Hermite masks, or higher-dimensional oscillators. No independent external mathematical audit has been performed. The Poisson argument proves relative errors for each fixed \(\rho<1\), not errors uniform at the phase boundary.

## References

1. C. L. Williams, L. C. Ortelli, and G. Silva, *The Fourier Uncertainty Principle Through the Lens of Infinite Banded Matrices*, arXiv:2609.17970 (first submitted 2026-09-16), https://arxiv.org/abs/2609.17970.
2. D. Dominici, *Mehler--Heine type formulas for Charlier and Meixner polynomials*, arXiv:1406.6193 (2014), https://arxiv.org/abs/1406.6193.
3. D. Dominici, *Mehler--Heine type formulas for Charlier and Meixner polynomials II. Higher order terms*, Journal of Classical Analysis 12 (2018), DOI:10.7153/jca-2018-12-02.
4. J. Soria-Lorente and L. Michel, *Mehler--Heine asymptotics for finite differences of mass-modified Charlier and Meixner polynomials*, arXiv:2608.27495 (2026), https://arxiv.org/abs/2608.27495.
5. M. Nilsson, *On the transition of Charlier polynomials to the Hermite function*, arXiv:1202.2557 (2012), https://arxiv.org/abs/1202.2557.
6. A. B. J. Kuijlaars and W. Van Assche, *Extremal Polynomials on Discrete Sets*, Proceedings of the London Mathematical Society 79 (1999), 191--221, DOI:10.1112/S0024611599011867.
7. I. Krasikov and A. Zarkh, *On zeros of discrete orthogonal polynomials*, Journal of Approximation Theory 156 (2009), 121--141, DOI:10.1016/j.jat.2008.04.015.
8. C. Knessl and J. S. H. van Leeuwaarden, *Transient analysis of the Erlang A model*, Mathematical Methods of Operations Research 82 (2015), 143--173, DOI:10.1007/s00186-015-0498-9.
