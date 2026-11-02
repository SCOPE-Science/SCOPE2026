# Exact priced spectral-abscissa design on a one-way three-state cycle

## Finding
For the three-state unidirectional continuous-time Markov generator
\[
Q(x,y,z)=\begin{pmatrix}-x&x&0\\0&-y&y\\z&0&-z\end{pmatrix},\qquad x,y,z>0,
\]
with fixed positive per-unit rate prices \(p_1,p_2,p_3\) and budget \(p_1x+p_2y+p_3z\le B\), the largest achievable asymptotic exponential convergence exponent is
\[
\boxed{\Gamma_* =\frac{3B}{2\bigl(P-\delta\bigr)}},\quad
P=p_1+p_2+p_3,\quad
\delta=\sqrt{p_1^2+p_2^2+p_3^2-p_1p_2-p_2p_3-p_3p_1}.
\]
The expression is a maximum when the least price is unique or all prices coincide; it is only a supremum if exactly two prices tie for the least value.

More precisely, relabel the rates and prices together so that \(a=p_1\le b=p_2\le c=p_3\). If \(a<b\), set
\[
\Lambda=\frac{3}{a+b+c-\delta},\qquad
\rho=\frac{\Lambda(a+b)-2}{1-\Lambda a},\qquad
s^2=\frac{B}{a(1+\rho)^2+b+c\rho^2}.
\]
Then \(\rho>0\), and the **unique** optimal rates are
\[
\boxed{(x,y,z)=\bigl((1+\rho)^2s^2,s^2,\rho^2s^2\bigr)}.
\]
The two nonzero eigenvalues of the optimal generator coincide, and the generator has a nontrivial Jordan block (an exceptional point). When \(a=b<c\), no strictly positive rate triple attains \(\Gamma_* =B/(2a)\): the only maximizer in the nonnegative-rate closure is \((B/(2a),B/(2a),0)\). If \(a=b=c\), every strictly positive budget-saturating triple for which \(\sqrt{x},\sqrt{y},\sqrt{z}\) obey the three (nonstrict) triangle inequalities is optimal; conversely every optimum has these properties. Thus equal prices admit a continuum of optima, generally without eigenvalue coalescence.

## Assumptions and scope
The generator is row-conservative and has only forward cyclic jumps \(1\to2\to3\to1\). Rates are strictly positive throughout the irreducible-chain optimization and prices and budget are fixed positive reals. The quantity optimized is the **asymptotic exponential decay exponent**, \(\Gamma(Q)=-\max\{\operatorname{Re}\lambda:\lambda\in\sigma(Q),\lambda\ne0\}\), not a finite-time total-variation mixing time. At a defective optimum the leading decay may include a polynomial factor \(t\), which does not change the exponent. Closure statements for a zero rate concern limits of the spectral expression, not an irreducible Markov chain.

## Proof
The characteristic polynomial follows by direct expansion:
\[
\det(\lambda I-Q)=\lambda\bigl(\lambda^2+S\lambda+T\bigr),\qquad
S=x+y+z,\quad T=xy+yz+zx.
\]
Consequently, writing \(\Delta=S^2-4T\),
\[
\Gamma(Q)=\begin{cases}S/2,&\Delta\le0,\\(S-\sqrt\Delta)/2,&\Delta>0.\end{cases}
\]
Set \(u=\sqrt{x}\), \(v=\sqrt{y}\), \(w=\sqrt{z}\). Heron's factorization gives
\[
\Delta=-(u+v+w)(-u+v+w)(u-v+w)(u+v-w).
\]
Thus \(\Delta\le0\) exactly when the three square-root rates obey the triangle inequalities. If \(\Delta>0\), let \(u>v+w\) denote the unique largest square-root rate after cyclic relabeling. Holding the other rates fixed and decreasing \(x=u^2\) to \((v+w)^2\) strictly reduces cost, and strictly increases the decay exponent: in the region \(x>(v+w)^2\),
\[
\frac{d\Gamma}{dx}=\frac12\left(1-\frac{x-y-z}{\sqrt{(x-y-z)^2-4yz}}\right)<0.
\]
Afterwards scaling all rates up to exhaust the budget strictly improves the exponent. Therefore no positive optimum is outside the triangle region, and every candidate may be dominated by one within it.

Inside that region \(\Gamma=S/2\). By positive homogeneity and budget saturation, maximizing \(\Gamma\) is equivalent to maximizing the square-root Rayleigh quotient
\[
\mathcal R(u,v,w)=\frac{u^2+v^2+w^2}{au^2+bv^2+cw^2}
\]
over positive triangle triples, giving \(\Gamma=(B/2)\sup\mathcal R\). If all prices equal \(a\), the quotient is identically \(1/a\), yielding the entire family stated. Otherwise assume \(a\) is one of the least prices. For fixed positive \(v,w\), differentiation with respect to \(u^2\) has sign \((b-a)v^2+(c-a)w^2>0\). Thus moving \(u\) upward to the allowed endpoint \(u=v+w\) strictly increases the quotient. In particular any optimum with positive rates and not all prices equal is on that boundary.

Put \(v=s>0\), \(w=t>0\), \(u=s+t\). The quotient becomes
\[
\frac{2s^2+2st+2t^2}{(a+b)s^2+2ast+(a+c)t^2},
\]
whose symmetric matrix pencil is
\[
H=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
M=\begin{pmatrix}a+b&a\\a&a+c\end{pmatrix}.
\]
The generalized eigenvalue equation \(\det(H-\Lambda M)=0\) reduces to
\[
3-2(a+b+c)\Lambda+(ab+bc+ca)\Lambda^2=0.
\]
Its larger root is \(\Lambda=3/(a+b+c-\delta)\). When \(a<b\le c\), the matrix \(M^{-1}H\) is strictly entrywise positive, being a positive scalar multiple of
\[
\begin{pmatrix}a+2c&c-a\\b-a&a+2b\end{pmatrix}.
\]
Perron–Frobenius theory gives one strictly positive leading eigenvector, unique up to positive scale. Its coordinate ratio is \(\rho=t/s=[\Lambda(a+b)-2]/[1-\Lambda a]>0\). The budget fixes that scale and yields the stated unique optimizer. Its triangle degeneracy forces \(\Delta=0\). A diagonalizable generator with both nonzero eigenvalues equal to \(-\Gamma_*\) would equal \(-\Gamma_*(I-\mathbf1\pi^{\mathsf T})\) for the unique positive stationary distribution \(\pi\), and thus would have all six off-diagonal entries positive, contrary to the one-way zero pattern. Hence the double eigenvalue is defective.

If \(a=b<c\), the pointwise bound \(\mathcal R\le1/a\) is strict whenever \(w>0\), and equality in the nonnegative triangle cone requires \(w=0\), \(u=v\). This gives the unique boundary rates and nonattainment by any strictly positive triple. This exhausts all price-tie cases, since \(a=b=c\) was handled separately.

## Verification
The accompanying standalone `check.py` reproduces exact generalized-eigenvalue identities, compares the closed formula with numerically computed spectra over hundreds of positive price triples, checks budget-constrained trial allocations, and tests the unique-minimum and price-tie boundaries. It reports 54,319 successful assertion checks on the supplied machine. Its finite checks corroborate the algebra but are not used to infer the all-parameter theorem. All infinite and real-parameter quantifiers are proved above.

## Relationship to prior work
Boyd–Diaconis–Xiao (2004) formulate fastest mixing on an undirected graph using symmetric discrete-time transition matrices, with semidefinite methods and a reversible prescribed-stationarity extension. Their model does not contain this nonreversible one-way generator with three independent jump-rate prices. Gerencsér (2014, first preprint) studies mixing-time growth for long cycles with random shortcut connections; the full available version treats large graph asymptotics rather than an exact three-state price-constrained spectral-abscissa design. Gerencsér–Hendrickx–Van Dooren (2015) study spectral gap on a discrete-time cycle, with doubly stochastic transition constraints. None of these inspected formulations implies the radical price threshold, optimizer-tie classification, and repeated-root design stated here without a separate nonlinear analysis. This comparison does not establish absolute priority over all unlocated specialist literature.

## Limitations
The exact objective is the spectral exponential exponent, not a uniform finite-time convergence constant. The theorem applies to exactly three states on a pure one-way cycle, with freely chosen positive rates, linear positive prices and one budget. Changing the topology, using general reversible generators, imposing a fixed stationary distribution, or including a transient-amplification penalty changes the problem. The irreducible optimum does not exist for two equal cheapest prices, although its spectral supremum does. External independent scientific audit has not been performed.

## References
- S. Boyd, P. Diaconis, and L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* 46 (2004), 667–689. Published electronically 2004-10-29. DOI: 10.1137/S0036144503423264. https://stanford.edu/~boyd/papers/pdf/fmmc.pdf
- B. Gerencsér, “Mixing times of Markov chains on a cycle with additional long range connections,” arXiv:1401.1692v1, first posted 2014-01-08. https://arxiv.org/abs/1401.1692
- B. Gerencsér, J. Hendrickx, and P. Van Dooren, “Spectral gap of Markov chains on a cycle,” *European Control Conference* (2015), DOI: 10.1109/ECC.2015.7330635. https://real.mtak.hu/173919/1/cycle_spectral_gap.pdf
