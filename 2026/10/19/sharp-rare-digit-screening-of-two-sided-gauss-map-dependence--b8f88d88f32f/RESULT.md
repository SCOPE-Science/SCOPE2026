# Sharp rare-digit screening of two-sided Gauss-map dependence

## Finding

Let \(G(x)=\{1/x\}\) be the Gauss map on \((0,1)\), with its stationary two-sided continued-fraction digit process \((A_j)_{j\in\mathbb Z}\). Write \(E_N=\{A_0\ge N\}\) for an integer \(N\ge1\). Let \(U=[0;A_1,A_2,\ldots]\) and \(V=[0;A_{-1},A_{-2},\ldots]\) be the forward and backward continued-fraction tails adjacent to the central digit. All logarithms below are natural.

Set \(L_N=\log(1+1/N)\). Conditional on \(E_N\), the joint density of \((U,V)\) on \((0,1)^2\) and its two identical marginal densities are **exactly**
\[
q_N(u,v)=\frac1{L_N}\sum_{k=N}^{\infty}\frac1{(k+u+v)^2},\qquad
m_N(u)=\frac1{L_N(N+u)}.
\]
Uniformly for \(u,v\in[0,1]\), the conditional dependence ratio satisfies
\[
\frac{q_N(u,v)}{m_N(u)m_N(v)}
=1+\frac{(u-1/2)(v-1/2)}{N^2}+O(N^{-3}).
\]
Consequently, in total variation and mutual information (measured in nats),
\[
N^2\,\left\|\mathcal L(U,V\mid E_N)-\mathcal L(U\mid E_N)\otimes\mathcal L(V\mid E_N)\right\|_{\rm TV}\longrightarrow\frac1{32},
\]
\[
N^4 I(U;V\mid E_N)\longrightarrow\frac1{288}.
\]
The **same sharp total-variation constant survives digit quantization**: with \(B_-=A_{-1}=\lfloor1/V\rfloor\) and \(B_+=A_1=\lfloor1/U\rfloor\),
\[
\boxed{\lim_{N\to\infty}N^2\left\|\mathcal L(B_-,B_+\mid E_N)-\mathcal L(B_-\mid E_N)\otimes\mathcal L(B_+\mid E_N)\right\|_{\rm TV}=\frac1{32}.}
\]
The exact information-theoretic leading constant after quantization is different:
\[
\boxed{\lim_{N\to\infty}N^4 I(B_-;B_+\mid E_N)
=\frac12\left(\frac{\pi^2}{12}-\frac34\right)^2.}
\]
In particular, conditioning on a very large continued-fraction digit leaves its two immediate neighbors asymptotically independent with the **Lebesgue-digit** marginal probabilities \(\Pr(B_\pm=k)\to 1/[k(k+1)]\), while their residual statistical dependence has the sharp powers two in total variation and four in mutual information.

## Assumptions and scope

The underlying probability space is the standard natural extension of the invariant Gauss probability measure. Up to null endpoint sets, its coordinates \((x,y)\in(0,1)^2\) have density \(1/[\log2\,(1+xy)^2]\). The central digit is \(A_0=\lfloor1/x\rfloor\), its forward tail is \(U=G(x)\), and its backward tail is \(V=y\). The two neighboring digits are \(A_1=\lfloor1/U\rfloor\) and \(A_{-1}=\lfloor1/V\rfloor\). The threshold \(N\) ranges over positive integers and tends to infinity. Total variation means one half the integral or sum of the absolute density/probability difference. Mutual information is Kullback--Leibler divergence from the product of the two *conditional marginals*; it is not divergence from the unconditional Gauss marginals. Statements involving digit distributions concern the countably infinite alphabet \(\{1,2,\ldots\}\).

The main dynamical classification is MSC2020 37A50, concerning a measure-preserving map and its induced stochastic digit process; the invariant extension's number-theoretic interpretation is supporting context.

## Proof

**1. An exact two-sided cusp law.** On the branch \(A_0=k\), write \(x=1/(k+u)\), where \(u=G(x)\in(0,1)\). Since \(|dx/du|=(k+u)^{-2}\), the invariant density transforms to \([\log2\,(k+u+y)^2]^{-1}\,du\,dy\). The event \(E_N\) comprises precisely the branches \(k\ge N\), and has probability \(\log(1+1/N)/\log2\). Division by this probability yields the displayed exact \(q_N\). Integrating it over the second coordinate telescopes:
\[
\int_0^1\sum_{k=N}^{\infty}(k+u+v)^{-2}\,dv
=\sum_{k=N}^{\infty}\left[\frac1{k+u}-\frac1{k+u+1}\right]=\frac1{N+u}.
\]
This proves the marginal identity. Symmetry proves the other marginal.

**2. The rank-one cancellation.** Euler--Maclaurin summation, uniformly for \(s\in[0,2]\), gives
\[
\sum_{k=N}^{\infty}(k+s)^{-2}
=\frac1{N+s}+\frac1{2(N+s)^2}+\frac1{6(N+s)^3}+O(N^{-5}).
\]
Insert this and \(L_N=N^{-1}-\tfrac12N^{-2}+\tfrac13N^{-3}+O(N^{-4})\) into
\[
\frac{q_N(u,v)}{m_N(u)m_N(v)}
=L_N(N+u)(N+v)\sum_{k=N}^{\infty}(k+u+v)^{-2}.
\]
Polynomial multiplication shows that the constant term is one, the \(N^{-1}\) term cancels, and the \(N^{-2}\) term equals \((u-\tfrac12)(v-\tfrac12)\). The error is uniform. This second-order interaction, rather than merely the product limit, is the critical step.

**3. Continuous total variation and information.** Denote the last ratio by \(1+z_N(u,v)\). Its expansion is uniform, with \(\|z_N\|_\infty=O(N^{-2})\). Both conditional marginals converge uniformly to the constant density one. Hence dominated convergence gives
\[
\lim N^2\frac12\int m_N(u)m_N(v)|z_N(u,v)|\,du\,dv
=\frac12\left(\int_0^1|u-\tfrac12|\,du\right)^2=\frac1{32}.
\]
Also \(\int m_N(u)m_N(v)z_N(u,v)\,du\,dv=0\) exactly. Taylor's formula \((1+z)\log(1+z)=z+z^2/2+O(|z|^3)\), uniformly on the relevant range, now yields
\[
\lim N^4 I(U;V\mid E_N)
=\frac12\left(\int_0^1(u-\tfrac12)^2du\right)^2=\frac1{288}.
\]

**4. Projection to integer digits.** Let \(J_k=(1/(k+1),1/k)\), \(p_k=|J_k|=1/[k(k+1)]\), and \(\mu_k=p_k^{-1}\int_{J_k}(u-1/2)\,du\). Then
\[
\mu_k=\frac12\left(\frac1k+\frac1{k+1}-1\right).
\]
The uniform ratio expansion integrates over every \(J_k\times J_l\) to give, uniformly in \(k,l\ge1\),
\[
\frac{\Pr(B_+=k,B_-=l\mid E_N)}{\Pr(B_+=k\mid E_N)\Pr(B_-=l\mid E_N)}
=1+N^{-2}\mu_k\mu_l+O(N^{-3}).
\]
Uniformity holds even for large digits, since the remainder is bounded pointwise *relative to the conditional product density* before integration, and the discrepancy of conditional bin means from \(\mu_k\) is uniformly \(O(N^{-1})\).

As \(\mu_1=1/4\), all \(\mu_k<0\) for \(k\ge2\), and \(\sum_kp_k\mu_k=0\), one has \(\sum_kp_k|\mu_k|=1/4\). Dominated convergence for the countable product gives the displayed digit total-variation constant \(\tfrac12(1/4)^2=1/32\). The same uniform Taylor expansion used above gives
\[
\lim N^4I(B_-;B_+\mid E_N)
=\frac12\left(\sum_{k=1}^{\infty}p_k\mu_k^2\right)^2.
\]
The series evaluates exactly by partial fractions:
\[
\frac{(k^2-k-1)^2}{4k^3(k+1)^3}
=\frac1{4(k+1)}+\frac3{4(k+1)^2}-\frac1{4(k+1)^3}
-\frac1{4k}-\frac1{4k^2}+\frac1{4k^3},
\]
whose sum is \(\zeta(2)/2-3/4=\pi^2/12-3/4\). This proves the discrete constant and the theorem.

## Verification

The companion `verify.py` uses exact symbolic algebra to check the uniform-asymptotic polynomial coefficient and the partial-fraction identity, and high-precision special functions to check the independent four-quadrant evaluation of the leading digit total-variation constant. Invoke `python verify.py` with SymPy and mpmath installed. The successful local run prints `VERIFY_OK`. The exact invariant density and Euler--Maclaurin remainder, together with the analytic summability arguments above, establish the infinite statements; finite calculations serve only as independent checks.

## Relationship to prior work

Sinai and Ulcigrai (2007), especially their Section 2.2, give the Gauss natural-extension density used as the starting point; their result concerns a different continued-fraction renewal time and does not calculate sharp two-sided dependence conditioned on an extreme central digit. Kesseböhmer and Schindler (2016) investigate large-digit counting laws and mixing coefficients, including conditional natural-extension kernels, but do not give the displayed two-sided rare-digit total-variation or mutual-information asymptotics. Jin, Singh, Zhang and Hildebrand (2024) provide explicit frequencies for single-digit classes and repeated-digit strings rather than this conditional two-sided information law. The present calculations use the established exact invariant density and standard analytic expansions; neither the density itself nor the existence of mixing is claimed as new.

## Limitations

The results concern the stationary natural extension of the *ordinary* Gauss map, with one conditioned central digit and its two immediate neighbors. They do not assert the same constants for other continued-fraction algorithms, nonstationary initial laws, longer windows or simultaneous rare digit clusters. The proof does not establish independent historical priority or a general theorem for arbitrary dynamical systems. An equivalent sharp information law could have appeared under a different terminology; the literature comparison cannot exclude that possibility exhaustively.

## References

1. Y. G. Sinai and C. Ulcigrai, *Renewal-type Limit Theorem for the Gauss Map and Continued Fractions*, arXiv:0710.1283v1 (first submitted 2007-10-05), §2.2.
2. M. Kesseböhmer and T. Schindler, *Limit theorems for counting large continued fraction digits*, arXiv:1604.06612 (first submitted 2016-04-22), especially §§1 and 4.
3. A. Jin, S. Singh, Z. Zhang and A. J. Hildebrand, *On the Continued Fraction Expansion of Almost All Real Numbers*, arXiv:2403.16761v1 (first submitted 2024-03-25), Theorem 3 and §4.
