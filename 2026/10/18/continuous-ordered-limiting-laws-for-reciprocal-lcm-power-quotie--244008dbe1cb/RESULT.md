# Continuous ordered limiting laws for reciprocal LCM-power quotients

## Finding
For real \(1<\kappa<\infty\), let
\[
\sigma_{-1}(n)=\sum_{d\mid n}\frac1d,\qquad
F_\kappa(n)=\sum_{d\mid n}\mu(d)\sigma_{-1}(n/d)^\kappa,\qquad
R_\kappa(n)=\left(\frac{nF_\kappa(n)}{\kappa^{\omega(n)}}\right)^{1/(\kappa-1)}
\]
for positive integers \(n\), where \(\omega(n)\) counts distinct prime factors. Set \(R_\kappa(1)=1\). Then the empirical measures \(X^{-1}\sum_{1\le n\le X}\delta_{R_\kappa(n)}\) converge weakly as \(X\to\infty\) to a probability law \(\nu_\kappa\). Every \(\nu_\kappa\) is non-atomic and has support exactly \([1,\infty)\). Its complex Mellin transform is the locally uniformly convergent Euler product given below; all its real moments exist.

There are canonical endpoint laws \(\nu_1\) and \(\nu_\infty\), also non-atomic and supported on \([1,\infty)\), such that \(\nu_\kappa\) depends weakly continuously on \(\kappa\in[1,\infty]\). The upper endpoint \(\nu_\infty\) is the classical limiting law of \(\sigma_{-1}(n)\). On one common probability space the corresponding random variables satisfy \(W_\kappa<W_\lambda\) almost surely for every fixed \(1\le\kappa<\lambda\le\infty\).

At \(\kappa=2\), the limiting mean has the explicit Euler product
\[
\lim_{X\to\infty}\frac1X\sum_{n\le X}R_2(n)
=\prod_p\left(1+\frac1{2p(p-1)}\right),
\]
whereas the upper-endpoint mean is \(\zeta(2)\).

## Assumptions and scope
All primes \(p\) are rational primes. Write \(S_{p,a}=\sum_{j=0}^a p^{-j}\) for \(a\ge0\). For \(a\ge1\) and \(1<\kappa<\infty\), define
\[
U_{\kappa,p}(a)=\left[\int_0^1\left(S_{p,a-1}+t p^{-a}\right)^{\kappa-1}\,dt\right]^{1/(\kappa-1)}.
\]
Set \(U_{\kappa,p}(0)=1\), and define the endpoints
\[
U_{1,p}(a)=\exp\left(\int_0^1\log(S_{p,a-1}+t p^{-a})\,dt\right),\qquad
U_{\infty,p}(a)=S_{p,a}\quad(a\ge1).
\]
The formula for \(U_{\kappa,p}(a)\) is exactly \(\left[p^a\{S_{p,a}^\kappa-S_{p,a-1}^\kappa\}/\kappa\right]^{1/(\kappa-1)}\). These definitions are not claims about absolute continuity of the limiting laws; continuity here means **absence of atoms**. Realization is by independent integer-valued variables \(V_p\) with \(\Pr(V_p=a)=(1-p^{-1})p^{-a}\) for \(a\ge0\).

## Proof
**Local identity and uniform bound.** Möbius inversion and multiplicativity yield \(F_\kappa(p^a)=S_{p,a}^\kappa-S_{p,a-1}^\kappa\) for \(a\ge1\). The fundamental theorem of calculus therefore gives the displayed integral for \(R_\kappa(p^a)=U_{\kappa,p}(a)\). All power means, including their logarithmic-mean and maximum endpoints, satisfy
\[
1<U_{\kappa,p}(a)\le S_{p,a}\le(1-p^{-1})^{-1}\qquad(a\ge1),
\]
with strict monotonicity in \(\kappa\) for each fixed \(p,a\ge1\). The same bounds hold for the endpoint definitions.

**Infinite products and finite-integer limit.** Define \(W_\kappa=\prod_pU_{\kappa,p}(V_p)\) for \(\kappa\in[1,\infty]\). Since
\[
\sum_p\mathbb E\log U_{\kappa,p}(V_p)
\le\sum_p\frac{\log(1-p^{-1})^{-1}}p<\infty,
\]
this product converges to a finite positive random variable almost surely. Uniformly for \(\kappa\in[1,\infty]\), for any cutoff \(P\) and every \(X\ge1\),
\[
\frac1X\sum_{n\le X}\sum_{\substack{p>P\\p\mid n}}\log U_{\kappa,p}(v_p(n))
\le\sum_{p>P}\frac{\log(1-p^{-1})^{-1}}p=O(P^{-1}).
\]
For finitely many primes the valuations of a uniformly sampled integer \(1\le n\le X\) converge jointly to the independent geometric valuations \(V_p\), by the Chinese remainder theorem and the elementary densities of exact prime powers. The tail estimate then proves weak convergence of \(R_\kappa(n)\) to \(W_\kappa\), via bounded-Lipschitz test functions applied to their logarithms.

**Exact Mellin transform and moments.** The law of independence gives
\[
\mathbb E W_\kappa^z=\prod_p\left[(1-p^{-1})\sum_{a=0}^\infty\frac{U_{\kappa,p}(a)^z}{p^a}\right]\qquad(z\in\mathbb C).
\]
For \(z\) in any compact set, each Euler factor equals \(1+O_z(p^{-2})\), uniformly in \(\kappa\), because \(\log U_{\kappa,p}(a)=O(p^{-1})\). Hence the product converges locally uniformly and every real moment is finite. Moment convergence along the integers follows by uniform integrability: for each \(q>0\), the averages of \(\sigma_{-1}(n)^q\) are uniformly bounded. Indeed \(\sigma_{-1}(n)^q\le\prod_{p\mid n}(1+u_p)\) with \(u_p=(1-p^{-1})^{-q}-1=O_q(p^{-1})\); expansion over squarefree divisors gives the bound \(\prod_p(1+u_p/p)<\infty\). Since \(1\le R_\kappa(n)\le\sigma_{-1}(n)\), Hölder's inequality yields uniform integrability of each desired power.

**Absence of atoms.** Partition the primes \(p\ge3\) into successive, disjoint, finite blocks \(B_j\) by stopping a block when \(\prod_{p\in B_j}(1-p^{-1})\le1/2\). Divergence of \(\sum_p1/p\) ensures infinitely many blocks. Because each factor for \(p\ge3\) is at least \(2/3\), the probability \(q_j\) that no prime in \(B_j\) occurs satisfies \(1/3\le q_j\le1/2\). Its logarithmic block contribution is zero with probability \(q_j\), and positive otherwise. Write this independent block variable as \(B_j^*Y_j\), where \(Y_j>0\), independent of the Bernoulli variable \(B_j^*\) of success probability \(1-q_j\in[1/2,2/3]\). A biased Bernoulli of parameter in this range can be represented as a fair coin with probability at least \(2/3\), and a forced \(1\) otherwise. Among the first \(m\) blocks, with exponentially high probability at least \(m/2\) coin choices are free. Conditional on all positive weights \(Y_j\) and forced choices, subsets of free coins yielding a fixed sum form an antichain: a proper inclusion strictly increases a sum of positive weights. The elementary Sperner bound limits its fair-coin probability to \({\binom{k}{\lfloor k/2\rfloor}}/{2^k}=O(k^{-1/2})\). Thus the maximum atom of the sum of the first \(m\) block contributions is \(O(m^{-1/2})\). Convolution with independent remaining blocks cannot increase maximum atom. Letting \(m\to\infty\) proves that \(\log W_\kappa\), and hence \(W_\kappa\), has no atoms. (The Sperner bound follows from double-counting a uniformly random maximal chain: an antichain meets each chain at most once.)

**Full support.** The quantities \(\log U_{\kappa,p}(1)\) are positive, tend to zero, and have divergent sum over primes: for every fixed finite \(\kappa\in[1,\infty)\) they equal \(1/(2p)+O_\kappa(p^{-2})\), while at \(\kappa=\infty\) they equal \(1/p+O(p^{-2})\). Given any \(t\ge0\) and \(\epsilon>0\), take sufficiently large primes and choose a finite subset with the sum of these terms within \(\epsilon/2\) of \(t\), using divergence and vanishing increments. Requiring exactly these primes to occur to exponent one and all other primes below a large cutoff to be absent has positive probability. The remaining tail is below \(\epsilon/2\) with positive probability, by the expectation bound. Thus every neighborhood of \(e^t\) has positive probability, while \(W_\kappa\ge1\). The support is precisely \([1,\infty)\).

**Parameter interpolation and mean.** Generalized power-mean monotonicity applied to the nonconstant positive function \(S_{p,a-1}+tp^{-a}\) proves \(U_{\kappa,p}(a)<U_{\lambda,p}(a)\) whenever \(1\le\kappa<\lambda\le\infty\) and \(a\ge1\). Since with probability one some (in fact infinitely many) \(V_p\) are positive, the coupled random products satisfy \(W_\kappa<W_\lambda\) almost surely. The uniform logarithmic majorant permits dominated convergence in \(\kappa\) along every sample path, proving weak continuity and the stated endpoint laws. For \(\kappa=2\), \(U_{2,p}(a)=S_{p,a-1}+1/(2p^a)\); direct geometric summation yields
\[
(1-p^{-1})\sum_{a\ge0}\frac{U_{2,p}(a)}{p^a}=1+\frac1{2p(p-1)}.
\]
Moment convergence proves the claimed average. At the upper endpoint \(\mathbb E W_\infty=\prod_p(1-p^{-2})^{-1}=\zeta(2)\).

## Verification
The accompanying standalone verifier checks exact prime-power identities and the rational \(\kappa=2\) Euler factor for multiple primes, enumerates \(R_2(n)\) independently by two formulas, and compares empirical means against truncated Euler products. These finite checks do not prove weak convergence or atomlessness; the preceding arguments do.

## Relationship to prior work
Molnar, *Reciprocal LCM powers and Robin's criterion* (arXiv:2610.12816v1, October 8, 2026), supplies the multiplicative function, the parameter-monotone normalization and its pointwise large-parameter limit, together with average and extremal orders. The present result concerns an additional, **integer-sampling probability law**: explicit all-parameter Mellin products, atomlessness, full unbounded support, stochastic coupling including the logarithmic-mean endpoint, and the exact \(\kappa=2\) limiting average. Its parameter monotonicity and prime-power identities are credited to the source, not independently new. The classical Davenport distribution of \(\sigma(n)/n\) supplies the upper endpoint; general additive-function limit theory anticipates the existence mechanism but does not provide this stated complete parameter family and the local Euler mean computation.

## Limitations
The laws are shown to be continuous (non-atomic), not necessarily absolutely continuous with respect to Lebesgue measure. No convergence rate in \(X\) is asserted. The formulas are Euler products, not elementary closed-form distribution functions. No new claim about the Riemann hypothesis follows. The analysis is restricted to \(n\) sampled by natural density and \(\kappa\ge1\), with \(\kappa=1\) understood as an endpoint of the normalization rather than the original Möbius convolution.

## References
1. G. Molnar, *Reciprocal LCM powers and Robin's criterion*, arXiv:2610.12816v1 (first public release 2026-10-08), https://arxiv.org/html/2610.12816v1.
2. E. Jennings, P. Pollack, L. Thompson, *Variations on a theorem of Davenport concerning abundant numbers*, arXiv:1306.0537 (2013), https://arxiv.org/abs/1306.0537.
3. H. Davenport, classical continuity theorem for the distribution of \(n/\sigma(n)\) (1933), as surveyed in reference 2.
4. P. Erdős and A. Wintner, classical theory of limiting distributions of additive arithmetic functions (1939), used here only as contextual precedent; the proof above is direct.
