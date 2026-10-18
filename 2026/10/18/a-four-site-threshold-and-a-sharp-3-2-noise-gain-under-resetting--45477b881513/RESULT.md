# A four-site threshold and a sharp \(3/2\) noise gain under resetting on cycles

## Finding
Consider a continuous-time nearest-neighbor random walk on the cycle \(C_n\) with \(n\geq3\), rate one in each direction, and independent Poisson resets to vertex \(0\) at rate \(r>0\). From its unique stationary distribution let \(A_T=\int_0^T\mathbf1_{\{X_s=0\}}\,ds\), and define \(V_n(r)=\lim_{T\to\infty}T^{-1}\operatorname{Var}(A_T)\). All reset moves are instantaneous; attempted resets while already at vertex zero leave the state unchanged.

Put \(t(r)=\tfrac12\operatorname{arcosh}(1+r/2)\), and let \(p_n(r)\) be the stationary probability of vertex zero. Then
\[
 p_n(r)=\tanh(t(r))\coth(nt(r)),\qquad
 V_n(r)=\frac{d}{dr}p_n(r)^2
 =\frac{2p_n(r)}n\sum_{k=1}^{n-1}\frac{4\sin^2(\pi k/n)}{\big(r+4\sin^2(\pi k/n)\big)^2}.
\]
The boundary values and derivative at zero resetting are
\[
 V_n(0)=\frac{n^2-1}{6n^2},\qquad
 V_n'(0+)=\frac{(n^2-1)(n^2-9)}{120n^2}.
\]
For the triangle, \(V_3(r)=4(r+1)/(r+3)^3\) is strictly decreasing on \((0,\infty)\). For **each** \(n\geq4\), however, every sufficiently small positive reset rate increases the asymptotic variance above its no-reset value, and \(V_n\) attains a maximum at some finite positive reset rate. These assertions do not claim uniqueness of the maximizing rate.

There is a sharp global envelope, independent of cycle size:
\[
 0<V_n(r)<\frac4{(r+4)^2}<\frac14\qquad(n\geq3,\ r>0).
\]
Writing \(M_n=\sup_{r\geq0}V_n(r)\), the constant \(1/4\) is optimal across finite cycles:
\[
 \lim_{n\to\infty}M_n=\frac14,
 \qquad\lim_{n\to\infty}\frac{M_n}{V_n(0)}=\frac32.
\]
Indeed the explicit mesoscopic choice \(r=1/n\) approaches the upper envelope, so optimization of the origin occupation's long-time variance can yield an asymptotic **fifty-percent** enhancement over the reset-free cycle. The stationary mean occupancy, by contrast, increases strictly with resetting for all \(n\).

## Assumptions and scope
Vertices are \(\{0,\ldots,n-1\}\) with indices modulo \(n\). The no-reset generator is \((L_0f)(i)=f(i-1)+f(i+1)-2f(i)\), and the reset generator is \((L_rf)(i)=(L_0f)(i)+r[f(0)-f(i)]\). The cycle has \(n\geq3\), both edge clocks have rate exactly one, and the initial state is stationary at each \(r>0\). The limit \(r=0\) refers to the irreducible no-reset chain with uniform stationary distribution. The long-time variance limit is taken **before** the limits in \(r\) or \(n\). Variance means the ordinary variance of the time integral, not counting variance of reset or jump events.

## Proof
**1. Stationary renewal resolvent.** Let \(P_s^0\) denote the no-reset transition matrix and put \(q(s)=P_s^0(0,0)\). The last-reset decomposition gives, for all initial states \(x\),
\[
 P_t^r(x,0)=e^{-rt}P_t^0(x,0)+r\int_0^t e^{-rs}q(s)\,ds.
\]
Hence \(p_n(r)=r\int_0^\infty e^{-rs}q(s)\,ds\). Discrete Fourier diagonalization of \(-L_0\) gives eigenvalues \(\lambda_k=4\sin^2(\pi k/n)\), so
\[
 p_n(r)=\frac r n\sum_{k=0}^{n-1}\frac1{r+\lambda_k}.
\]
For a periodic second-order difference equation, the diagonal Green function is
\[
 \frac1n\sum_{k=0}^{n-1}\frac1{r+\lambda_k}
 =\frac{\coth(nt)}{\sqrt{r(r+4)}},\quad
 t=\tfrac12\operatorname{arcosh}(1+r/2).
\]
This follows, for example, by summing the exponentially decaying infinite-line Green kernel \(e^{-2t|j|}/\sqrt{r(r+4)}\) over all integer translates \(j+\ell n\). Since \(r=4\sinh^2t\), the stated hyperbolic expression follows.

**2. Exact asymptotic variance.** The chain is finite irreducible for \(r>0\), and its stationary covariance for the origin indicator equals
\[
 \operatorname{Cov}(\mathbf1_{\{X_0=0\}},\mathbf1_{\{X_t=0\}})
 =p_n(r)\,[P_t^r(0,0)-p_n(r)].
\]
The Green--Kubo formula, valid by exponential mixing, yields \(V_n(r)=2p_n(r)\int_0^\infty[P_t^r(0,0)-p_n(r)]dt\). Substitute the last-reset identity and interchange absolutely convergent integrals to obtain
\[
 \int_0^\infty[P_t^r(0,0)-p_n(r)]dt
 =\int_0^\infty e^{-rs}(1-rs)q(s)ds
 =p_n'(r).
\]
Consequently \(V_n(r)=2p_n(r)p_n'(r)=(p_n(r)^2)'\). The spectral expression follows by differentiating the finite Fourier sum. Every nonzero eigenvalue is positive, so \(p_n'(r)>0\) and \(V_n(r)>0\).

**3. The sharp four-site transition.** Set
\[
 S_1=\sum_{k=1}^{n-1}\lambda_k^{-1}=\frac{n^2-1}{12},\qquad
 S_2=\sum_{k=1}^{n-1}\lambda_k^{-2}=\frac{n^4+10n^2-11}{720}.
\]
For completeness, start from the identity \(\sum_{j=0}^{n-1}\csc^2(x+j\pi/n)=n^2\csc^2(nx)\), obtained by logarithmically differentiating the sine product. Compare the constant terms at \(x=0\) to get \(\sum_{k=1}^{n-1}\csc^2(\pi k/n)=(n^2-1)/3\); compare the coefficients of \(x^2\), using \((\csc^2x)''=6\csc^4x-4\csc^2x\), to obtain the displayed \(S_2\). Then
\[
 p_n(r)=\frac{1+rS_1-r^2S_2+O(r^3)}n,
 \quad V_n(0)=\frac{2S_1}{n^2},\quad
 V_n'(0+)=\frac{2(S_1^2-2S_2)}{n^2}.
\]
Substitution gives the stated formulas. In the triangle \(p_3(r)=(r+1)/(r+3)\), hence \(V_3'(r)=-8r/(r+3)^4<0\) for \(r>0\). For \(n\ge4\) the first derivative at zero is positive, while \(V_n(r)\to0\) as \(r\to\infty\); continuity yields a positive interior maximizer.

**4. Global envelope and optimal constant.** Put \(\phi(r)=r/(r+4)=\tanh^2t\). As \(p_n(r)^2=\phi(r)\coth^2(nt)\), direct differentiation (using \(dr/dt=4\sinh(2t)\)) gives
\[
 \phi'(r)-V_n(r)
 =\frac{\phi(r)}{\sinh^2(2t)\sinh^2(nt)}
 \left[\frac{n\sinh(2t)}{2\tanh(nt)}-1\right]>0.
\]
The bracket is positive because \(n\sinh(2t)>2nt>2\tanh(nt)\). As \(\phi'(r)=4/(r+4)^2\), the universal bound follows. For \(r_n=1/n\), one has \(t(r_n)\to0\) and \(nt(r_n)\to\infty\). Thus \(\coth(nt)\to1\), and differentiation of its correction shows \(V_n(r_n)-\phi'(r_n)\to0\) (the correction is exponentially small in \(nt\)). Therefore \(V_n(r_n)\to1/4\), proving the claimed global sharpness. Finally \(V_n(0)\to1/6\), giving the gain factor \(3/2\).

## Verification
The included standalone `verify.py` requires only the Python standard library. Run `python verify.py` alongside this document. It solves stationary and Poisson equations of the **full resetting-chain generator** using exact rational Gaussian elimination and compares their long-time variance with an independently constructed exact resolvent derivative. The package verifies 30 cases (cycle sizes 3--12; three rational reset rates), checks independently evaluated spectral and hyperbolic formulas, 68 trigonometric-sum cases, the global upper bound, and a large-cycle mesoscopic witness. This is corroboration of, not a replacement for, the all-size proof above.

## Relationship to prior work
Evans and Majumdar (2011) introduced Poissonian stochastic resetting and its renewal stationary-state methodology. Bressloff (2020) studied occupation times under resetting for run-and-tumble particles; Méndez, Flaquer-Galmés, and Pal (2024) developed Feynman--Kac and renewal occupation-time formulas for normal/anomalous walks on intervals and half-lines; Méndez and Flaquer-Galmés (2025) treated general resetting functionals. Such general renewal and moment techniques are antecedents, not new contributions here. Grange (2021) investigated winding of a Brownian walker under resetting on a ring. Zatloukal (2020) developed local-time resolvents for nonreset random walks on graphs.

The claim here is confined to the **sharp discrete-cycle classification of the sign of the initial fluctuation response, the all-size strict envelope, and the optimal asymptotic fifty-percent gain**. The renewal-resolvent identity is a tool and is not asserted to be a new general stochastic-resetting method. These concrete cycle extremal statements were not identified in the inspected material; an equivalent older calculation or a non-obvious reduction from broader resetting theory remains possible.

## Limitations
This concerns a single continuous-time nearest-neighbor walker, homogeneous symmetric edge clocks, reset to the observed vertex, finite simple cycles, and the second asymptotic cumulant of its origin occupation time. For \(n\ge4\), the existence of a positive maximizer is proved, but neither uniqueness nor a closed-form optimal rate is claimed. The fifty-percent enhancement is a limit across growing cycles, not an exact finite-cycle equality. No results on hitting-time optimization, higher cumulants, independent reset counting, random reset destinations, higher-dimensional lattices, or interacting particles follow from this theorem. No independent audit has been performed.

## References
1. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704 (initial public version 2011-02-14), https://arxiv.org/abs/1102.2704.
2. P. C. Bressloff, *Occupation time of a run-and-tumble particle with resetting*, arXiv:2009.01968 (2020), https://arxiv.org/abs/2009.01968.
3. V. Méndez, R. Flaquer-Galmés and A. Pal, *Occupation time statistics for non-Markovian random walks*, arXiv:2412.05247 (2024), https://arxiv.org/abs/2412.05247.
4. V. Méndez and R. Flaquer-Galmés, *Statistical properties of stochastic functionals under general resetting*, arXiv:2507.05955 (2025), https://arxiv.org/abs/2507.05955.
5. P. Grange, *Winding number of a Brownian particle on a ring under stochastic resetting*, arXiv:2111.15241 (2021), https://arxiv.org/abs/2111.15241.
6. V. Zatloukal, *Local time of random walks on graphs*, arXiv:2012.15399 (2020), https://arxiv.org/abs/2012.15399.
