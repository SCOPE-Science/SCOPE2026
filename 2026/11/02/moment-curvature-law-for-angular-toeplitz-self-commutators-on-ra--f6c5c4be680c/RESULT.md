# Moment-curvature law for angular Toeplitz self-commutators on radial analytic Hilbert spaces

## Finding
Let \(m\geq1\) be an integer and let \(\nu\) be a nondegenerate probability measure on \((0,\infty)\) with every nonnegative real moment finite. Put
\[
M(x)=\int_0^\infty t^x\,d\nu(t),\qquad g(x)=\log M(x),\quad x\geq0.
\]
Suppose \(g\in C^3([0,\infty))\), \(g''>0\), \(g'''<0\), and, for positive constants \(c,\gamma\),
\[
g''(x)\sim c x^{-\gamma},\qquad
 g'''(x)\sim-\gamma c x^{-\gamma-1}\quad(x\to\infty).
\]
Form the rotationally invariant analytic Hilbert space \(\mathcal H_\nu\), the closure of analytic polynomials under the probability measure with radial variable \(t=|z|^2\) distributed as \(\nu\) and uniform argument. Let \(T_m\) be compression to \(\mathcal H_\nu\) of multiplication by the unit-modulus angular symbol \(u_m(z)=e^{im\arg z}\) (with arbitrary value at the origin), and set
\[
Q_m=T_m^*T_m-T_mT_m^*.
\]
Then \(Q_m\) is positive and injective (every diagonal eigenvalue is strictly positive) and trace class, with \(\operatorname{Tr}Q_m=m\). Its ordered singular values satisfy the **sharp moment-curvature law**
\[
\boxed{\lim_{j\to\infty}j^{\gamma+1}s_j(Q_m)=\frac{\gamma c m^3}{4}.}
\]
Consequently, for every \(p>0\),
\[
Q_m\in\mathcal S_p\quad\Longleftrightarrow\quad p>\frac1{\gamma+1},
\]
and, at the critical exponent \(p_*=1/(\gamma+1)\),
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{j=1}^N s_j(Q_m)^{p_*}
=\left(\frac{\gamma c m^3}{4}\right)^{p_*}.
\]
The sharp decay exponents and constants specialize to
\[
\lim_{j\to\infty}j^3s_j(Q_m)=\frac{m^3(\alpha+1)}2
\quad\text{on weighted disk Bergman space }\alpha>-1,
\]
and
\[
\lim_{j\to\infty}j^2s_j(Q_m)=\frac{m^3}{4a}
\quad\text{on power-Fock space of weight }e^{-|z|^{2a}},\ a>0.
\]
These are two distinct sharp Schatten boundaries, respectively \(p>1/3\) and \(p>1/2\), for the same angular-winding symbol.

## Assumptions and scope
All inner products use the same normalized radial probability measure. The symbol is bounded and measurable even when its value at the origin is chosen arbitrarily. The analytic space is *defined* as the closure of polynomials; it need not be identified with any larger holomorphic \(L^2\) class. The normalized orthogonal monomials are \(e_n(z)=z^n/\sqrt{M(n)}\), \(n\geq0\). The conditions on \(g\) are assumed globally for strict positivity and asymptotically for decay; a finite set of exceptional moments is not covered by this theorem. The index \(j\) enumerates singular values with multiplicity, starting at one.

For the disk, \(d\nu_\alpha(t)=(\alpha+1)(1-t)^\alpha\,dt\) on \((0,1)\), and
\[
M_\alpha(x)=\frac{\Gamma(\alpha+2)\Gamma(x+1)}{\Gamma(x+\alpha+2)}.
\]
For power Fock, \(d\nu_a(t)=a\Gamma(1/a)^{-1}e^{-t^a}\,dt\) on \((0,\infty)\), with
\[
M_a(x)=\frac{\Gamma((x+1)/a)}{\Gamma(1/a)}.
\]
The customary Gaussian Bargmann--Fock space corresponds to \(a=1\).

## Proof
**1. Exact weighted-shift reduction.** Angular orthogonality and the definition of \(M\) give
\[
T_m e_n=w_ne_{n+m},\qquad
w_n=\frac{M(n+m/2)}{\sqrt{M(n)M(n+m)}}.
\]
Strict log-convexity of \(M\), equivalently \(g''>0\), implies \(0<w_n<1\). For \(n\geq0\), set \(w_n=0\) when \(n<0\) and \(q_n=w_n^2-w_{n-m}^2\). The operator \(Q_m\) is diagonal in the monomial basis, with eigenvalues \(q_n\).

**2. Strict increase and quantitative limit.** Put \(h=m/2\) and extend the weight formula to real \(x\geq0\). By the integrated central-difference identity,
\[
B(x):=g(x)+g(x+m)-2g(x+h)
 =\int_{-h}^h(h-|v|)g''(x+h+v)\,dv.
\]
The right side is positive and \(\log w(x)^2=-B(x)\). Differentiating under the integral gives
\[
B'(x)=\int_{-h}^h(h-|v|)g'''(x+h+v)\,dv<0.
\]
Thus \(w(x)^2\) increases strictly. As \(x\to\infty\), the assumed asymptotics are uniform on the bounded integration interval, and \(\int_{-h}^h(h-|v|)dv=h^2\); therefore
\[
B(x)\sim ch^2x^{-\gamma},\qquad
B'(x)\sim-\gamma ch^2x^{-\gamma-1}.
\]
Consequently \(w(x)^2\to1\) and
\[
\frac{d}{dx}w(x)^2=-B'(x)e^{-B(x)}
\sim \gamma ch^2x^{-\gamma-1}.
\]
For \(n\geq m\), integrate this derivative between \(n-m\) and \(n\). The uniform fixed-width asymptotic yields
\[
q_n=w_n^2-w_{n-m}^2
\sim m\gamma ch^2 n^{-\gamma-1}
=\frac{\gamma cm^3}{4}n^{-\gamma-1}.
\]
All \(q_n>0\), including the initial \(m\) terms.

**3. Trace and singular-value rearrangement.** Exact telescoping gives, for every integer \(N\geq m-1\),
\[
\sum_{n=0}^{N}q_n=\sum_{n=N-m+1}^{N}w_n^2\longrightarrow m.
\]
The positive diagonal operator is therefore trace class and has trace \(m\). Since \(q_n\sim C n^{-\beta}\), with \(C=\gamma c m^3/4>0\) and \(\beta=\gamma+1>1\), counting eigenvalues above \(t\) shows
\[
\#\{n:q_n>t\}\sim(C/t)^{1/\beta}\quad(t\downarrow0).
\]
Indeed, for any fixed \(\varepsilon>0\), all sufficiently large \(n\) obey \((1-\varepsilon)Cn^{-\beta}<q_n<(1+\varepsilon)Cn^{-\beta}\), which squeezes the count; finitely many initial terms do not affect the limit. Inverting the count gives \(s_j(Q_m)\sim Cj^{-\beta}\), without assuming the \(q_n\) themselves are monotonically ordered. The series \(\sum s_j^p\) converges exactly for \(\beta p>1\). At \(p=1/\beta\), termwise comparison with \(C^p/j\) and Cesàro convergence against the harmonic series prove the claimed logarithmic coefficient.

**4. The two model moment laws.** For disk moments, the digamma expansions give
\[
g''(x)=\psi_1(x+1)-\psi_1(x+\alpha+2)
\sim(\alpha+1)x^{-2},
\]
\[
g'''(x)=\psi_2(x+1)-\psi_2(x+\alpha+2)
\sim-2(\alpha+1)x^{-3}.
\]
For power Fock moments, \(g''(x)=a^{-2}\psi_1((x+1)/a)\sim a^{-1}x^{-1}\) and \(g'''(x)=a^{-3}\psi_2((x+1)/a)\sim-a^{-1}x^{-2}\). The integral representations of polygamma functions show \(\psi_1>0\), \(\psi_2<0\), and, for every \(\alpha>-1\), \(\psi_1(x+1)>\psi_1(x+\alpha+2)\) and \(\psi_2(x+1)<\psi_2(x+\alpha+2)\). Both cases satisfy all global strict-sign hypotheses. Substitution gives the two announced coefficients and thresholds. This completes the proof.

## Verification
The standalone script `checks/moment_curvature_check.py` evaluates exact gamma-moment formulas at 65-digit precision for three disk weights, three power-Fock weights, and winding orders \(m=1,2,4\). It checks strict weight growth, positivity of the self-commutator diagonals, telescoping finite traces, and convergence toward the exact spectral coefficients at three large indices. Running `python checks/moment_curvature_check.py` with `mpmath` available gives 3294 finite assertions passed. The rigorous statements about all indices, strict positivity, and sharp infinite-dimensional asymptotics follow from the proof above, not the numerical checks.

## Relationship to prior work
Dewage and Ólafsson derive quasi-radial Toeplitz spectral/moment formulas on Fock spaces; their diagonal quasi-radial symbols differ from the angular phase symbols here. Rodríguez Rodríguez develops quasi-homogeneous Toeplitz operator algebras on Bergman spaces. Dong and Zhou classify finite-rank commutators of quasihomogeneous symbols, but their finite-rank statements do not determine the positive infinite-rank spectral decay or the radial moment-curvature coefficient. Al-Qabani and Virtanen's Fock Toeplitz Fredholm theory concerns the topological index, not the asymptotic singular values of the self-commutator. The weighted-shift representation and Fredholm index \(-m\), as well as the trace identity \(\operatorname{Tr}Q_m=m\), should be regarded as familiar consequences; the claimed contribution is the general curvature-to-singular-value theorem together with its sharp constants and distinct disk/Fock Schatten boundaries.

## Limitations
The curvature assumptions include differentiability and a precise regular-variation law for both second and third logarithmic moment derivatives. Oscillatory moment curvature or sign-changing curvature may produce different behavior. The result treats nonnegative winding numbers and one complex variable; the negative winding case follows by adjunction but has the opposite self-commutator sign. There is no assertion about arbitrary nonsymmetric or matrix-valued symbols, and no complete classification of measures satisfying the curvature conditions. Earlier or unindexed results on angular Toeplitz commutators could affect historical priority; this paper does not claim novelty of the weighted-shift mechanism or topological index.

## References
1. A. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first public 2021-07-03).
2. J. C. Rodríguez Rodríguez, *Commutative Banach Algebras Generated by Toeplitz Operators on the Bergman Space*, arXiv:2206.11557 (2022).
3. X.-T. Dong and Z.-H. Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213 (2014).
4. M. Al-Qabani and J. A. Virtanen, *Fredholm theory of Toeplitz operators on standard weighted Fock spaces*, Ann. Acad. Sci. Fenn. Math. 43 (2018), DOI:10.5186/aasfm.2018.4344.
5. R. Quiroga-Barranco, *Toeplitz operators, T^m-invariance and quasi-homogeneous symbols*, arXiv:2106.01980 (2021).
