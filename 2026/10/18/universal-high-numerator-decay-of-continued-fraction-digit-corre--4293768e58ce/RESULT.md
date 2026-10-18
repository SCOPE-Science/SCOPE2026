# Universal high-numerator decay of continued-fraction digit correlations

## Finding
For every integer \(N\ge1\), consider the continued-fraction map \(T_N(x)=N/x-\lfloor N/x\rfloor\) on \((0,1]\), with its invariant probability \(d\mu_N(x)=dx/[L_N(N+x)]\), where \(L_N=\log(1+1/N)\). Let \(a_j=\lfloor N/T_N^{j-1}(x)\rfloor\). Given two integer thresholds \(m_N,n_N\ge N+1\), suppose \(N/m_N\to u\in(0,1)\) and \(N/n_N\to v\in(0,1)\). For **every fixed integer lag \(k\ge1\)**,

\[
\boxed{\lim_{N\to\infty}N^k\operatorname{Cov}_{\mu_N}\bigl(\mathbf1_{\{a_1\ge m_N\}},\mathbf1_{\{a_{k+1}\ge n_N\}}\bigr)
=\frac{(-1)^k}{2^k}u(1-u)v(1-v).}
\]

More precisely, putting \(u_N=N/m_N\), \(v_N=N/n_N\), the covariance equals
\[
\frac{(-1)^k}{2^kN^k}u_N(1-u_N)v_N(1-v_N)+O_k(N^{-k-1}),
\]
with the implied constant uniform when \(u_N,v_N\) range in a fixed compact subset of \((0,1)\). Thus every successive temporal separation incurs asymptotically another factor \(-1/(2N)\), including its sign, with a nonzero universal coefficient. This is a **large-numerator limit with fixed lag**, not a large-lag spectral asymptotic for fixed \(N\).

## Assumptions and scope
All probabilities are taken with the stationary invariant measure \(\mu_N\). The thresholds may be any integer sequences satisfying the displayed ratio hypotheses; no rounding convention is required. Covariances are for indicator events, not the unbounded digit values themselves. The formula holds for fixed lag \(k\); no uniformity is asserted when \(k\) grows with \(N\). Endpoint ambiguities on rational or eventually terminating expansions occur on sets of \(\mu_N\)-measure zero.

## Proof
**1. Transfer operator and exact threshold image.** The normalized Perron–Frobenius operator of this map is
\[
(P_Nf)(x)=\sum_{a=N}^{\infty}\frac{N+x}{(a+x)(a+x+1)}f\left(\frac{N}{a+x}\right).
\]
For \(g_m(x)=\mathbf1_{\{x\le N/m\}}\) and \(m\ge N+1\), the geometric inverse branches imply, for \(0<x<1\),
\[
(P_Ng_m)(x)=\sum_{a=m}^{\infty}\frac{N+x}{(a+x)(a+x+1)}=\frac{N+x}{m+x}.
\]
Only the \(\mu_N\)-equivalence class matters; the right-hand continuous representative is used. Its derivative is \((m-N)/(m+x)^2\). Uniformly for \(u_N=N/m\) in a compact subinterval of \((0,1)\),
\[
P_Ng_m(x)=c_{1,N}+\frac{u_N(1-u_N)}{N}x+e_{1,N}(x),\qquad\operatorname{Lip}(e_{1,N})=O(N^{-2}),
\]
where a constant is absorbed into \(c_{1,N}\) and \(e_{1,N}(0)=0\).

**2. An exact mean identity.** Let \(\iota(x)=x\). A telescoping partial fraction identity yields
\[
(P_N\iota)(x)=N(N+x)\sum_{a=N}^{\infty}\frac{1}{(a+x)^2(a+x+1)}
=N\bigl[(N+x)\psi_1(N+x)-1\bigr],
\]
where \(\psi_1\) denotes the trigamma function. Euler–Maclaurin summation (or the classical trigamma expansion and its differentiated remainder) gives, uniformly for \(0\le x\le1\),
\[
\frac{d}{dx}(P_N\iota)(x)=-\frac1{2N}+O(N^{-2}).
\]
The transfer kernel reverses stochastic order. Indeed, if \(A_x\) is the sampled inverse-branch index at state \(x\), then \(\Pr(A_x\ge a)=(N+x)/(a+x)\), nondecreasing in \(x\) for \(a\ge N\). With a quantile coupling, \(A_x\le A_y\) when \(x<y\), and therefore \(N/(A_x+x)>N/(A_y+y)\). Consequently the associated probability kernels are stochastically ordered. Their one-dimensional Wasserstein-1 distance is the difference in means, so for every Lipschitz function \(f\),
\[
\operatorname{Lip}(P_N f)
\le \operatorname{Lip}(f)\operatorname{Lip}(P_N\iota)
\le\bigl(1/(2N)+O(N^{-2})\bigr)\operatorname{Lip}(f).
\]
Here the coupling is used only to establish a rigorous Lipschitz bound, not as a claim that this basic order-reversal property is novel.

**3. Rank-one iteration.** Inductively, for each fixed \(j\ge1\), the previous estimates imply
\[
P_N^j g_m(x)=c_{j,N}+d_{j,N}x+e_{j,N}(x),\quad
 d_{j,N}=\frac{(-1)^{j-1}u_N(1-u_N)}{2^{j-1}N^j},\quad
\operatorname{Lip}(e_{j,N})=O_j(N^{-j-1}),
\]
with \(e_{j,N}(0)=0\). The base case is Step 1. For the step, apply \(P_N\) and use \(P_N\mathbf1=\mathbf1\); the affine slope \(d_{j,N}\) is multiplied by \(-1/(2N)\), with an \(O(N^{-j-2})\) Lipschitz remainder coming both from the differentiated trigamma asymptotic and from the Lipschitz contraction acting on \(e_{j,N}\). This proves the stated expansion at \(j+1\). Every error estimate is uniform for thresholds in the specified compact range.

**4. Stationary correlation and its coefficient.** The transfer duality gives
\[
\operatorname{Cov}_{\mu_N}(g_m,g_n\circ T_N^k)
=\operatorname{Cov}_{\mu_N}(P_N^kg_m,g_n).
\]
Because \(d\mu_N(x)=[1+O(N^{-1})]dx\) uniformly and \(g_n=\mathbf1_{\{x\le v_N\}}\), direct integration shows
\[
\operatorname{Cov}_{\mu_N}(\iota,g_n)
=-\frac{v_N(1-v_N)}2+O(N^{-1}).
\]
Substitute the expansion of Step 3. The Lipschitz remainder, normalized by \(e_{k,N}(0)=0\), has uniformly bounded sup-norm \(O_k(N^{-k-1})\). Its covariance therefore has that same order. The claimed coefficient and error follow.

**5. Exact checks at the first two lags.** The first-lag joint tail is
\[
\mu_N(a_1\ge m,a_2\ge n)=\frac{\log(1+N/(mn))}{\log(1+1/N)}.
\]
At lag two, a separate exact identity follows by partial fractions:
\[
(P_N^2g_m)(x)=(N+x)\left[\psi\left(N+x+\frac Nm\right)-\psi(N+x)\right],
\]
where \(\psi\) is the digamma function. These formulas independently expose the signs and the first two asymptotic constants, without finite truncation of the infinite branch sum.

## Verification
The accompanying `verify.py` checks exact telescoped inverse-branch tail identities and the exact trigamma mean identity at multiple parameters. It independently evaluates the first-lag logarithmic and second-lag digamma formulas at high precision for \(N=10,40,160\), with thresholds \(m=2N\), \(n=3N\), confirming the predicted signs and convergence to \(-1/36\) and \(1/72\) after multiplication by \(N\) and \(N^2\), respectively. These finite evaluations are not used to infer any unrestricted-lag or infinite-parameter assertion; those follow from Steps 1–4.

## Relationship to prior work
Dan Lascu's *Metric properties of N-continued fractions* (arXiv:1510.02052, first publicly posted 2015-10-07), especially Propositions 4.1 and 4.2, already establishes the invariant measure and transfer kernel, reversal of monotonicity, and a \(1/(N+1)\) variation contraction. These are **prior results** used here, not claimed as new. In particular, sign alternation of monotone digit correlations by itself follows from that monotonicity and the elementary covariance inequality; it is **not** the asserted novelty. Lascu's *Dependence with complete connections and the Gauss–Kuzmin theorem for N-continued fractions* (arXiv:1510.03606, first posted 2015-10-13) develops convergence through random systems with complete connections. Sebe and Lascu's *A two-dimensional Gauss–Kuzmin theorem for N-continued fraction expansions* (arXiv:1707.08393) gives quantitative convergence estimates for the natural extension. Those source results concern fixed-parameter decay or qualitative monotonicity and do not themselves supply the **fixed-lag, high-numerator covariance limit with its exact nonzero coefficient at every lag**. The new argument isolates a \(-1/(2N)\) affine mode and propagates the threshold amplitude through it.

## Limitations
No claim is made about growing lags, unbounded digit covariances, optimal finite-\(N\) mixing rates, or arbitrary nonstationary initial laws. Previously published transfer-operator bounds, exact Gauss–Kuzmin formulas, and stochastic ordering are acknowledged as input. Although the cited primary texts were compared at theorem/proof level, an unindexed large-parameter spectral expansion or equivalent analysis could establish the same coefficient; historical priority has not been independently certified. The program verifies only specified finite and two-lag calculations.

## References
1. D. Lascu, *Metric properties of N-continued fractions*, arXiv:1510.02052v1 (2015-10-07), especially Sections 2.5 and 4, Propositions 4.1 and 4.2. https://arxiv.org/abs/1510.02052
2. D. Lascu, *Dependence with complete connections and the Gauss–Kuzmin theorem for N-continued fractions*, arXiv:1510.03606v1 (2015-10-13). https://arxiv.org/abs/1510.03606
3. G. I. Sebe and D. Lascu, *A two-dimensional Gauss–Kuzmin theorem for N-continued fraction expansions*, arXiv:1707.08393v1 (2017-07-26). https://arxiv.org/abs/1707.08393
