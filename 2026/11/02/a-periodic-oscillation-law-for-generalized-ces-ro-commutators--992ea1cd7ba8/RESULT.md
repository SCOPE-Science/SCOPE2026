# A periodic oscillation law for generalized Cesàro commutators

## Finding
Let \(p\ge 1\), and let \(d_0,\ldots,d_{p-1}\in\mathbb C\) be an arbitrary periodic profile. On \(\ell^2(\mathbb N_0)\), define the diagonal operator \(De_n=d_{n\bmod p}e_n\), the generalized discrete Cesàro operator
\[
 (C_t x)_n=\frac1{n+1}\sum_{j=0}^{n}t^{n-j}x_j,\qquad 0\le t\le1,
\]
and \(K_t=[D,C_t]=DC_t-C_tD\). Let
\[
 m=\frac1p\sum_{r=0}^{p-1}d_r,\qquad V=\frac1p\sum_{r=0}^{p-1}|d_r-m|^2,\qquad A=2V.
\]
For residues \(0\le r<p\) (all subscripts of \(d\) are read modulo \(p\)), put
\[
 u_r=\frac1p\sum_{k=0}^{p-1}|d_r-d_{r-k}|^2,\quad
 b_r=\sum_{k=0}^{r}|d_r-d_{r-k}|^2-(r+1)u_r,\quad a_r=\frac{r+1}{p},
\]
and define the finite, explicitly computable correction
\[
 L(d)=-\frac1p\sum_{r=0}^{p-1}(u_r-A)\psi(a_r)
 +\frac1{p^2}\sum_{r=0}^{p-1}b_r\psi_1(a_r),
\]
where \(\psi\) is the digamma function and \(\psi_1=\psi'\) is the trigamma function. Then:

**Sharp operator-ideal transition.** If the profile is constant, \(K_t=0\) for every \(t\). Otherwise, \(K_0=0\), while for each \(0<t<1\),
\[
 K_t\in\bigcap_{s>1}\mathcal S_s\setminus\mathcal S_1.
\]
At \(t=1\), \(K_1\) is bounded but not compact, with the explicit lower estimate \(\|K_1\|_{\mathrm{ess}}\ge\sqrt{V/2}\).

**Two exact renormalizations.** As \(t\uparrow1\),
\[
 \boxed{\|K_t\|_{\mathcal S_2}^2
 =A\log\!\frac1{1-t^2}+A+L(d)+o(1).}
\]
Writing \(P_N\) for the projection onto the first \(N\) coordinate vectors, as \(N\to\infty\),
\[
 \boxed{\|P_NK_1P_N\|_{\mathcal S_2}^2
 =A\log N+A\gamma+L(d)+o(1),}
\]
where \(\gamma\) is Euler's constant. The logarithmic coefficient is precisely twice the profile variance, and the difference of the finite constants is \(A(1-\gamma)\). Both formulas also hold (trivially, with zero terms) for constant profiles.

For example, with \(p=2\) and \((d_0,d_1)=(1,-1)\), one has \(A=2\) and \(L(d)=-\pi^2/4\), so the first finite term equals \(2-\pi^2/4\) and the second equals \(2\gamma-\pi^2/4\).

## Assumptions and scope
Indices begin at zero, and the Hilbert space is complex \(\ell^2(\mathbb N_0)\). The period \(p\) is any positive integer, not necessarily minimal; the profile may have repeated values and need not be real. Schatten notation \(\mathcal S_s\) is used for finite \(s\ge1\). The essential norm is distance to compact operators in the usual operator norm. We make no uniform-in-period claim and no claim about singular-value pointwise asymptotics. The limit \(t\uparrow1\) is along real parameters smaller than one.

Boundedness of \(C_1\) on \(\ell^2\) is the classical Hardy inequality (operator norm \(2\)); since \(C_t\) is entrywise dominated by \(C_1\) for \(0\le t\le1\), every \(C_t\) and hence every \(K_t\) is bounded.

## Proof
**1. Exact kernel.** Direct multiplication gives, for \(0\le j\le n\),
\[
 (K_t)_{nj}=\frac{(d_n-d_j)t^{n-j}}{n+1},
 \qquad (K_t)_{nj}=0\text{ for }j>n.
\]
It follows, writing \(q=t^2\) and \(a_{n,k}=|d_n-d_{n-k}|^2\), that whenever \(t<1\),
\[
 F(q):=\|K_t\|_{\mathcal S_2}^2
 =\sum_{n=0}^{\infty}\frac1{(n+1)^2}
       \sum_{k=0}^{n}q^k a_{n,k}.
 \tag{1}
\]
The series is finite by the geometric estimate \(\sum_{k=0}^n q^k a_{n,k}\le4\|d\|_\infty^2/(1-q)\).

**2. The exact ideal transition.** Let \(S\) denote the unilateral forward shift. For each \(k\ge1\), let \(E_k\) be diagonal with entries \((E_k)_{jj}=(d_{j+k}-d_j)/(j+k+1)\). Thus
\[
 K_t=\sum_{k=1}^{\infty}t^k S^kE_k.
\]
For any \(s>1\), \(\|S^kE_k\|_{\mathcal S_s}=\|E_k\|_{\mathcal S_s}\le2\|d\|_\infty\zeta(s)^{1/s}\). The series therefore converges in \(\mathcal S_s\) for every \(0<t<1\), proving all asserted positive ideal memberships. Since \(C_0\) is diagonal, \(K_0=0\).

For any trace-class operator \(T\) and any fixed subdiagonal, the sum of the absolute values of entries on that subdiagonal is bounded by \(\|T\|_{\mathcal S_1}\). Indeed, pair \(T\) with a norm-one partial shift whose phases match those entries, and use trace duality, first for finite truncations and then by monotone convergence. The first subdiagonal of \(K_t\) is \(t(d_{n+1}-d_n)/(n+2)\). A nonconstant periodic profile has at least one nonzero adjacent difference in each period, so
\[
 \sum_{n\ge0}|(K_t)_{n+1,n}|
 =t\sum_{n\ge0}\frac{|d_{n+1}-d_n|}{n+2}=\infty
\]
for every \(t>0\). Thus \(K_t\notin\mathcal S_1\) whenever \(t>0\) and \(d\) is not constant.

**3. Exact finite-section decomposition.** For each residue \(r\), the sequence \(a_{n,k}\), with \(n\equiv r\pmod p\), is periodic in \(k\) with mean \(u_r\). Its periodic remainder at the finite endpoint is particularly simple: if \(n=hp+r\), then
\[
 \sum_{k=0}^{n}a_{n,k}=(n+1)u_r+b_r.\tag{2}
\]
Also, using the mean \(m\) defined above,
\[
 u_r=|d_r-m|^2+V,\qquad
 \frac1p\sum_{r=0}^{p-1}u_r=A.
 \tag{3}
\]
Consequently (2) gives the *exact* identity
\[
 \|P_NK_1P_N\|_{\mathcal S_2}^2
 =\sum_{n=0}^{N-1}\frac{u_{n\bmod p}}{n+1}
  +\sum_{n=0}^{N-1}\frac{b_{n\bmod p}}{(n+1)^2}.
 \tag{4}
\]

Write \(\delta_r=u_r-A\), so \(\sum_r\delta_r=0\). The periodic zero-mean harmonic series converges by Dirichlet's test, and the partial fraction formulas for the digamma function imply
\[
 \sum_{n=0}^{\infty}\frac{\delta_{n\bmod p}}{n+1}
 =-\frac1p\sum_{r=0}^{p-1}\delta_r\psi(a_r).
 \tag{5}
\]
The trigamma identity \(\psi_1(a)=\sum_{h\ge0}(h+a)^{-2}\) gives
\[
 \sum_{n=0}^{\infty}\frac{b_{n\bmod p}}{(n+1)^2}
 =\frac1{p^2}\sum_{r=0}^{p-1}b_r\psi_1(a_r).
 \tag{6}
\]
Equations (4)--(6) and \(\sum_{j=1}^N1/j=\log N+\gamma+o(1)\) prove the second boxed formula.

**4. Damped renormalization.** Split the squared difference into its period mean and zero-mean part:
\[
 a_{n,k}=u_{n\bmod p}+v_{n,k},
 \qquad\sum_{k=0}^{p-1}v_{n,k}=0.
\]
For every \(n\), the partial sums in \(k\) of this periodic zero-mean sequence are bounded uniformly in \(n\) by a constant depending only on the profile and its period. Summation by parts with the decreasing weights \(q^k\) therefore gives
\[
 \sup_{n\ge0,\;0\le q\le1}
 \left|\sum_{k=0}^{n}q^kv_{n,k}\right|<\infty.
 \tag{7}
\]
Using (1), dominated convergence now shows that the zero-mean contribution has the limit
\[
 \sum_{n=0}^{\infty}\frac1{(n+1)^2}\sum_{k=0}^{n}v_{n,k}
 =\sum_{n=0}^{\infty}\frac{b_{n\bmod p}}{(n+1)^2},
 \tag{8}
\]
which equals the right-hand side of (6).

For the mean contribution, define
\[
 f_j(q)=\frac{1-q^j}{(1-q)j^2},\qquad j\ge1,
\]
with continuous value \(f_j(1)=1/j\). For every \(0\le q\le1\), this sequence is decreasing in \(j\), bounded by \(1/j\), and tends to zero. Because the partial sums of \(\delta_{j-1\bmod p}\) are bounded, Dirichlet's test has a tail bound uniform in \(q\). It follows that
\[
 \lim_{q\uparrow1}\sum_{j=1}^{\infty}\delta_{j-1\bmod p}f_j(q)
 =\sum_{j=1}^{\infty}\frac{\delta_{j-1\bmod p}}j,
 \tag{9}
\]
whose value is (5). Finally,
\[
 \sum_{j=1}^{\infty} f_j(q)
 =\frac{\zeta(2)-\operatorname{Li}_2(q)}{1-q}
 =\log\frac1{1-q}+1+o(1)
 \qquad(q\uparrow1),
 \tag{10}
\]
since \(\zeta(2)-\operatorname{Li}_2(1-\varepsilon)=\int_0^\varepsilon[-\log v]/(1-v)\,dv
 =\varepsilon(1-\log\varepsilon)+o(\varepsilon)\). Multiplying (10) by \(A\), and combining (5), (6), (8), and (9), proves the first boxed formula.

**5. Noncompactness at the classical endpoint.** Suppose \(V>0\), and let \(N\to\infty\) through multiples of \(p\). Define the unit vector
\[
 x^{(N)}_j=\begin{cases}
 \overline{d_j-m}/\sqrt{NV},&N\le j<2N,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Periodicity gives \(\sum_jx^{(N)}_j=0\) and \(\sum_jd_jx^{(N)}_j=\sqrt{NV}\). For every \(n\ge2N\), the kernel in Step 1 therefore yields
\[
 (K_1x^{(N)})_n=-\frac{\sqrt{NV}}{n+1}.
\]
These vectors tend weakly to zero, while
\[
 \liminf_{N\to\infty}\|K_1x^{(N)}\|_2^2
 \ge\lim_{N\to\infty}NV\sum_{n=2N}^{\infty}(n+1)^{-2}=\frac V2.
\]
Every compact operator sends this weakly null sequence to zero in norm, proving \(\|K_1\|_{\mathrm{ess}}\ge\sqrt{V/2}>0\). If \(V=0\), every profile value equals \(m\) and \(K_t=0\). This completes all claims.

## Verification
The proof is analytic and establishes statements about infinitely many coordinates. The standalone `check_periodic_cesaro.py` uses exact rational arithmetic to compare the commutator's finite Hilbert--Schmidt energy against the residue-grouped and endpoint formulas for several periods and parameters, and supplementary numerical checks of the two finite renormalization constants in the alternating period-two case. All 275 packaged checks passed. Finite computations do not prove convergence, noncompactness, or ideal nonmembership; those follow from Steps 2--5.

## Relationship to prior work
Curbera and Ricker's February 2023 preprint establishes the generalized discrete Cesàro model, compactness for \(t<1\) across Banach lattices, and spectral information; it does not state the periodic-diagonal commutator theorem above. Albanese, Bonet, and Ricker's May 2023 work treats spectra and dynamics in further sequence spaces. The broader commutator-Schatten results of Hytönen concern singular integrals on metric-measure spaces satisfying geometric and kernel assumptions, not the present one-sided discrete Cesàro matrices or their exact renormalization constants. Related quantitative work on generalized Cesàro singular values and real-variable Cesàro commutators does not imply the two period-dependent constants here. The phase-sensitive finite correction and simultaneous damping-versus-section renormalizations are the central claimed additions, not the established basic Cesàro boundedness or compactness statements.

## Limitations
This result is limited to bounded periodic diagonal symbols and real damping \(0\le t\le1\) on complex \(\ell^2\). It gives no pointwise asymptotic for the singular values of \(K_t\), no sharp essential norm at \(t=1\), and no extension to almost-periodic or statistically stationary symbols. The published-literature comparison cannot rule out every differently phrased general theorem; independent mathematical evaluation remains outstanding.

## References
1. G. P. Curbera and W. J. Ricker, *Fine spectra and compactness of generalized Cesàro operators in Banach lattices in \(\mathbb C^{\mathbb N_0}\)*, arXiv:2302.08750, first submitted 17 February 2023. https://arxiv.org/abs/2302.08750
2. A. A. Albanese, J. Bonet, and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805, first submitted 8 May 2023. https://arxiv.org/abs/2305.04805
3. T. Hytönen, *Schatten properties of commutators on metric spaces*, arXiv:2411.02613, first submitted 4 November 2024. https://arxiv.org/abs/2411.02613
