# A sharp shell-count law for angular-momentum peaks in Gaussian Fock localization

## Finding

**Theorem (spectral shell-count, sharp at every Gaussian observation mass).** Fix an integer \(d\geq1\), an integer \(q\geq1\), and endpoints
\[
0<a_1<b_1<a_2<b_2<\cdots<a_q<b_q<\infty.
\]
Let \(E=\{z\in\mathbb C^d:|z|^2\in S\}\), where \(S=\bigcup_{j=1}^q[a_j,b_j]\), and let \(T_E\) be Gaussian Fock-space Toeplitz localization with the indicator of \(E\). Its degree-\(n\) eigenvalue, \(\lambda_n\), has **at most \(q\) strict local maxima**, counting the one-sided endpoint \(n=0\), and at most \(q-1\) strict interior local minima. The maximum bound is sharp. More strongly, for every prescribed normalized Gaussian observation mass \(0<p<1\) and every \(d,q\), there are \(q\) such annuli with \(\Pr\{|Z|^2\in S\}=p\) for standard complex Gaussian \(Z\in\mathbb C^d\) and **exactly \(q\) strict local maxima** of \((\lambda_n)_{n\geq0}\). Thus a fixed mass budget does not reduce the optimal number of spectral peaks.

The precise concentration spectrum is
\[
\lambda_n=\frac{1}{\Gamma(n+d)}\sum_{j=1}^q\int_{a_j}^{b_j}e^{-t}t^{n+d-1}\,dt,
\quad n=0,1,\ldots.
\]
Each \(\lambda_n\) has multiplicity \(\binom{n+d-1}{d-1}\); a *spectral peak* refers to successive homogeneous degrees, not to ordering eigenvalues with multiplicity.

## Assumptions and scope

The Hilbert space is the analytic Bargmann--Fock space \(\mathcal F^2(\mathbb C^d)\) with normalized Gaussian inner product
\[
\langle f,g\rangle=\pi^{-d}\int_{\mathbb C^d}f(z)\overline{g(z)}e^{-|z|^2}\,dV(z).
\]
The operator \(T_Ef=P(\mathbf1_E f)\) uses the orthogonal analytic projection \(P\). All intervals are nondegenerate, disjoint, bounded and bounded away from the origin. Local maxima are strict: \(\lambda_0>\lambda_1\) at \(n=0\), and \(\lambda_n>\lambda_{n-1},\lambda_{n+1}\) for \(n\ge1\). Strict interior minima reverse the inequalities. No assertion is made for an infinite number of shells, signed masks, general nonsymmetric observation sets, or peaks in a multiplicity-sorted singular-value list.

## Proof

**1. Exact reduction.** Rotational invariance makes each homogeneous holomorphic polynomial space an eigenspace. Polar integration of a normalized degree-\(n\) monomial shows that the variable \(|z|^2\) in its squared-norm measure has the Gamma distribution with shape \(n+d\) and unit rate. This gives the displayed eigenvalues. Integration by parts yields the *exact* first-difference identity
\[
\boxed{\Gamma(n+d+1)(\lambda_{n+1}-\lambda_n)=G(n+d)},
\qquad
G(x)=\sum_{j=1}^q\left(e^{-a_j}a_j^x-e^{-b_j}b_j^x\right).
\]
Indeed, \(\frac{d}{dt}(t^{n+d}e^{-t})=(n+d-t)t^{n+d-1}e^{-t}\).

**2. Variation bound.** The generalized Descartes rule for exponential sums says that if \(\mu_1<\cdots<\mu_m\), the number of real zeros of \(\sum_{i=1}^m c_i e^{\mu_i x}\), counted with multiplicity, is at most the number of changes of sign in the ordered nonzero coefficient list. A short proof is by induction: divide by the least exponential and differentiate. The derivative has the coefficient signs of \(c_2,\ldots,c_m\). If \(c_1,c_2\) have opposite signs, Rolle's theorem adds at most one zero; if their signs agree, the function and its derivative initially point in the same direction at negative infinity, so a first zero requires an additional derivative zero. Multiplicities follow from generalized Rolle counting.

Applied to \(G\), the ordered bases \(a_1,b_1,\ldots,a_q,b_q\) yield coefficient signs \(+,-,+,-,\ldots,+,-\). Hence \(G\) has at most \(2q-1\) real zeros. Also
\[
G(0)=\sum_j(e^{-a_j}-e^{-b_j})>0,
\]
and \(G(x)<0\) for all sufficiently large \(x\), since the largest base \(b_q\) has a negative coefficient. There can consequently be at most \(q\) positive-to-negative sign crossings and at most \(q-1\) negative-to-positive crossings. Any strict local maximum of \(\lambda_n\) forces a positive-to-negative crossing of \(G\) between consecutive sampled arguments; when \(n=0\) is a maximum, its crossing occurs between \(0\) and \(d\). Different strict maxima require different crossings. Strict interior minima similarly force distinct negative-to-positive crossings. This proves both bounds, including boundary cases and accidental zeros of \(G\) at integer samples.

**3. Simultaneous sharpness and prescribed mass.** Fix \(d\), \(q\) and \(0<p<1\). First choose \(a>0\) so small that some finite \(b_0>a\) obeys
\[
\frac{1}{\Gamma(d)}\int_a^{b_0}e^{-t}t^{d-1}\,dt=p,
\qquad a^de^{-a}<b_0^de^{-b_0}.
\]
This is possible by taking \(a\downarrow0\) and using the positive \(p\)-quantile of the Gamma\((d,1)\) distribution. With this first interval alone, the strict first difference at degree zero is negative.

For \(q\ge2\) and a large positive integer \(M\), place \(q-1\) distant shells at
\[
R_j=M^{2j},\qquad [A_j,B_j]=[R_j-\sqrt{R_j},R_j+\sqrt{R_j}],
\quad j=1,\ldots,q-1.
\]
Their total Gamma\((d,1)\) probability tends to zero as \(M\to\infty\). By continuity and strict monotonicity of the Gamma distribution function, a unique \(b(M)\to b_0\) makes
\[
S_M=[a,b(M)]\cup\bigcup_{j=1}^{q-1}[A_j,B_j]
\]
have *exactly* mass \(p\). For all large \(M\), these are ordered disjoint positive intervals and \(\lambda_0>\lambda_1\), since the distant-shell boundary contributions at the fixed degree tend to zero.

We prove additional **strict** peaks at the explicit degrees \(n_j=R_j-d\). For a single distant shell, the boundary expression \(e^{-A_j}A_j^x-e^{-B_j}B_j^x\) is positive precisely when
\[
x<L(A_j,B_j):=\frac{B_j-A_j}{\log(B_j/A_j)},
\]
and negative above this logarithmic mean. Taylor expansion gives
\[
L(R_j-\sqrt{R_j},R_j+\sqrt{R_j})
=R_j-\frac13+O(R_j^{-1}),
\]
so its signs at \(x=R_j-1\) and \(x=R_j\) are respectively positive and negative. After division by \(\Gamma(x+1)\), their magnitudes are bounded below by a fixed positive multiple of \(R_j^{-1}\) for large \(M\), by Stirling's formula. Every other shell lies either at a bounded radius, at a radius negligible compared with \(R_j\), or at a radius much larger than \(R_j\). Stirling's formula (equivalently Gamma large-deviation bounds) makes each of their normalized boundary terms \(o(R_j^{-1})\) at these two arguments. Thus for all sufficiently large \(M\),
\[
G(R_j-1)>0>G(R_j).
\]
The first-difference identity therefore proves \(\lambda_{R_j-d}>\lambda_{R_j-d-1}\) and \(\lambda_{R_j-d}>\lambda_{R_j-d+1}\). Together with the peak at zero, this gives \(q\) strict maxima. The maximum-count bound excludes any additional strict maxima. The case \(q=1\) is the first interval alone.

## Verification

The included `check_shell_modes.py` independently recomputes Gamma interval masses, the integration-by-parts boundary identity, the exact single-shell logarithmic-mean threshold and concrete prescribed-mass multipeak examples in multiple complex dimensions. These are finite corroborative tests; the proof of the global bound and its all-parameters sharpness is the analytic argument above. To run: `python check_shell_modes.py` with Python 3, NumPy and SciPy.

## Relationship to prior work

Radial Fock Toeplitz diagonalization and the Gamma-moment form are established in Dewage--Ólafsson (arXiv:2107.01465; especially Section 2 and Corollaries 2.14--2.15), building on Grudsky--Vasilevski. Rozenblum--Vasilevski (arXiv:2203.04170, Section 3) establishes corresponding monomial spectral representations for radial Bergman operators. Generalized Descartes variation counting for exponential sums is classical. The claim here is the sharp, dimension-independent spectral peak budget for **positive finite unions of Fock annuli**, including constructive attainment **at every prescribed Gaussian observation mass**. The cited diagonalization and general exponential-sum zero bound supply ingredients, but neither source's stated results classify or construct the fixed-mass extremal annular spectra. A related harmonic Bergman circle-trace staircase concerns one sampling circle in a different Hilbert space and is not the asserted multiring theorem.

## Limitations

This is an analytic Gaussian Fock result for finite unions of strictly separated, positive-radius shells. The claim counts strict degree-indexed local extrema, not arbitrary nonstrict plateaus or sorted eigenvalues with multiplicity. Published-priority search and same mathematical model proof review cannot rule out every equivalent formulation in older total-positivity and radial localization literature; external expert review remains outstanding. No independent mathematical audit has been performed.

## References

1. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first publicly available 2021-07-03), Section 2 and Corollaries 2.14--2.15. https://arxiv.org/abs/2107.01465
2. G. Rozenblum and N. Vasilevski, *Commutative algebras of Toeplitz operators on the Bergman space revisited: Spectral theorem approach*, arXiv:2203.04170 (2022-03-08), Section 3. https://arxiv.org/html/2203.04170v1
3. S. Grudsky and N. Vasilevski, *Toeplitz operators on the Fock space: radial component effects*, Integral Equations and Operator Theory (2002), cited for the original radial Fock spectral formula in Reference 1.
