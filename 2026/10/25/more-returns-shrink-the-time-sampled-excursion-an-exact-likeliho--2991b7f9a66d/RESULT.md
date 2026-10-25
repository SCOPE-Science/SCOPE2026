# More returns shrink the time-sampled excursion: an exact likelihood-ratio law

## Finding

Let \(S\) be a simple symmetric random-walk bridge of \(2n\) steps, with \(n\ge2\). Let \(K\) be the number of excursions between consecutive visits to zero (including the return at time \(2n\)). Write \(L_1,\ldots,L_K\) for the **semilengths** of these excursions, so that each actual excursion has \(2L_i\) steps and \(\sum_iL_i=n\). Choose one of the \(n\) consecutive two-step time cells uniformly; let \(L^\star\) be the semilength of the excursion containing it. Conditioning on \(K=k\), define \(q_{n,k}(\ell)=\Pr(L^\star=\ell\mid K=k)\).

**Theorem.** For every \(n\ge2\), the conditional laws \(q_{n,k}\) are *strictly decreasing in likelihood-ratio order* as \(k\) runs from \(1\) to \(n\): for \(1\le k<n\) and \(1\le\ell<n\),
\[
q_{n,k+1}(\ell+1)q_{n,k}(\ell)\le q_{n,k+1}(\ell)q_{n,k}(\ell+1),
\]
with distinct distributions at every adjacent pair. The inequality is strict on common support when \(k\ge3\) and both lengths have positive probability under \(q_{n,k+1}\). In particular, the conditional expectation of any strictly increasing real function of \(L^\star\) decreases strictly with \(k\).

Define the *positive-excursion semiduration* by \(A=\sum_{i:\,\text{excursion }i\text{ positive}}L_i\). This is half the number of physical steps contained in positive excursions, *not* the count of clock times at which the walk is above zero. Then
\[
\mathbb E[A\mid K=k]=\frac n2,\qquad
\operatorname{Var}(A\mid K=k)=\frac n4\mathbb E[L^\star\mid K=k].
\]
Consequently, the conditional variance decreases **strictly** with every increment of \(k\), from \(n^2/4\) at \(k=1\) to \(n/4\) at \(k=n\). More generally, \(\mathbb E[\sum_iL_i^r\mid K=k]\) strictly decreases with \(k\) for every real \(r>1\).

If \(k_n/n\to\rho\in(0,1)\), then for each positive integer \(\ell\),
\[
q_{n,k_n}(\ell)\to q_\rho(\ell)=
\frac{\rho\ell C_{\ell-1}(1-\rho)^{\ell-1}}{(2-\rho)^{2\ell-1}},
\]
where \(C_j=(j+1)^{-1}\binom{2j}{j}\) is the Catalan number. Convergence holds with first moments, and therefore
\[
\lim_{n\to\infty}\frac{\operatorname{Var}(A\mid K=k_n)}n
=\frac{\rho^2-2\rho+2}{4\rho^2}.
\]

## Assumptions and scope

All steps are independent and equiprobable signs before conditioning on \(S_{2n}=0\); \(1\le k\le n\) is feasible. A return to zero after time zero terminates precisely one excursion. The random cell used to define \(L^\star\) is sampled *after* conditioning, uniformly and independently. Because every return occurs at an even time, the cell partition into consecutive pairs of steps respects the excursion boundaries. Likelihood-ratio order uses the zero-extension of the finite probability masses, and the displayed cross-product form avoids undefined ratios at support boundaries. The large-sample limit assumes \(k_n/n\to\rho\in(0,1)\); no assertion at \(\rho=0\) is made by that limit.

## Proof

**Excursion enumeration.** A fixed-sign primitive excursion of semilength \(\ell\ge1\) has \(C_{\ell-1}\) shapes. Its sign may be chosen independently, so for a bridge conditioned to have \(k\) excursions the ordered semilength vector has probability proportional to \(\prod_i C_{L_i-1}\). Introduce
\[
E(z)=\sum_{\ell\ge1}C_{\ell-1}z^\ell=\frac{1-\sqrt{1-4z}}2,
\qquad Z(m,j)=[z^m]E(z)^j.
\]
For \(1\le j\le m\), Lagrange inversion applied to \(E=z/(1-E)\) gives
\[
Z(m,j)=\frac jm\binom{2m-j-1}{m-j}
=\frac j{2m-j}\binom{2m-j}{m-j}.
\]
Set \(Z(0,0)=1\), and \(Z(m,j)=0\) whenever \(m<j\). Conditioning on \(K=k\) and size-biasing by the semilength of a uniformly chosen cell yields the exact finite law
\[
q_{n,k}(\ell)=\frac{k\ell C_{\ell-1}Z(n-\ell,k-1)}{nZ(n,k)},
\quad 1\le\ell\le n-k+1.
\tag{1}
\]
In particular, for \(n\ge2\) and \(k\ge2\), \(q_{n,k}(1)=(k-1)/(2n-k-1)\).

**Strict likelihood-ratio ordering.** For \(2\le k<n\), divide formula (1) at \(k+1\) by formula (1) at \(k\). Apart from a positive factor independent of \(\ell\), the ratio is
\[
\frac{Z(m,k)}{Z(m,k-1)}
=\frac{k}{k-1}\frac{m-k+1}{2m-k},\qquad m=n-\ell\ge k.
\tag{2}
\]
As \(m\) increases, this ratio is constant for \(k=2\) and strictly increasing for \(k\ge3\), because the numerator of its derivative has sign \(k-2\). Thus the ratio of the two probability masses is nonincreasing in \(\ell\); for \(\ell=n-k+1\), the newer mass is zero while the older mass is positive. For \(k=1\), the older distribution is concentrated at \(\ell=n\), and the newer one is supported below it. This proves the asserted strict likelihood-ratio and stochastic ordering, including all boundary cases. Strict expectation inequalities follow by the standard single-crossing sum argument: write an increasing test function as a nonnegative combination of upper-tail indicators and use strict stochastic order.

**Excursion signs and variance.** Conditional on the semilengths, the \(k\) excursion signs are independent fair signs. Therefore \(A=\sum_iL_iB_i\) for independent \(B_i\sim\mathrm{Bernoulli}(1/2)\). Hence \(\mathbb E[A\mid L_1,\dots,L_k]=n/2\) and \(\operatorname{Var}(A\mid L_1,\dots,L_k)=\frac14\sum_iL_i^2\). Uniform cell sampling gives \(\mathbb E[L^\star\mid L_1,\dots,L_k]=\sum_iL_i^2/n\). Conditional total variance now proves the variance identity and strict monotonicity. Likewise, \(\mathbb E[\sum_iL_i^r\mid K=k]=n\mathbb E[(L^\star)^{r-1}\mid K=k]\) for \(r>1\). At \(k=1\), \(A\) equals either \(0\) or \(n\) with probability \(1/2\); at \(k=n\), all semilengths are one and \(A\) is binomial with parameters \(n\) and \(1/2\).

**Linear-density limit.** Equation (1) gives \(q_{n,k}(1)=(k-1)/(2n-k-1)\). For \(\ell\) below the upper support boundary, the ratio of consecutive masses is
\[
\frac{q_{n,k}(\ell+1)}{q_{n,k}(\ell)}
=\frac{2(2\ell-1)}\ell\cdot
\frac{m(m-k+1)}{(2m-k-1)(2m-k)},\qquad m=n-\ell.
\tag{3}
\]
For \(k/n\to\rho\in(0,1)\) and fixed \(\ell\), the second factor tends to \(z_\rho=(1-\rho)/(2-\rho)^2\). Recursion (3) and the limit of \(q(1)\) give the displayed distribution. For moment convergence, uniformly over \(m\in[k,n]\) when \(k/n\to\rho\), the second factor in (3) is at most \(z_\rho+o(1)\): its continuous leading term \((1-u)/(2-u)^2\), with \(u=k/m\ge\rho+o(1)\), decreases in \(u\in(0,1]\), and the finite-size correction is uniformly \(o(1)\) because \(m\ge\rho n/2\) eventually. Since \(4z_\rho<1\), equation (3) supplies a uniform geometric tail bound. Thus the first moments converge. The limit mass has generating function
\[
\sum_{\ell\ge1}q_\rho(\ell)t^\ell
=\frac{\rho t}{(2-\rho)\sqrt{1-4z_\rho t}},
\]
whose derivative at \(t=1\) is \(1+2(1-\rho)/\rho^2\). Substitution into the variance identity gives the last formula.

## Verification

The accompanying standalone `verify.py` independently enumerates every balanced sign sequence through \(2n=18\), constructs its actual return-excursion decomposition, and checks exact conditional probabilities and conditional second moments. It also checks the exact formula and pairwise likelihood-ratio cross-product inequality for every \(2\le n\le50\). The checker reports 43,394 successful exact assertions. The analytic argument, rather than the finite tests, proves the all-size and limit statements.

## Relationship to prior work

Csáki and Hu (2003) analyze ranked lengths and heights of random-walk excursions, while Lindell and Holst (2007) derive generating functions and distributions for the longest excursions in tied-down walks. Serlet (2014) provides the particularly close exact Catalan-product enumeration for bridges conditioned on their return count, as well as an invariance principle when that count grows more slowly than the square root of the duration. The enumeration step above is classical and is not asserted to be new. The claimed contribution is the exact *cross-return-count likelihood-ratio order for a time-sampled excursion*, together with the strict hierarchy for positive-excursion semiduration variance and the linear-return-density moment limit. The inspected sources did not explicitly give this ordering or variance hierarchy; the ordering must be deduced by comparing normalization ratios across conditional laws. Related general work on simply generated trees and random allocations may imply the linear-density limit.

## Limitations

The likelihood-ratio statement is limited to equiprobable nearest-neighbor bridges. It need not hold for general step distributions, general renewal laws, or Brownian bridges conditioned on a noninteger local time. The occupation variable uses a complete-excursion convention; it is not the number of discrete clock instants above zero. Earlier renewal-ordering theorems could subsume this particular Catalan case, and some broad allocation literature was not completely inspected. The result has only self-review, not independent audit or external certification.

## References

1. E. Csáki and Y. Hu, *Lengths and heights of random walk excursions*, Discrete Mathematics and Theoretical Computer Science, Proceedings AC (2003), 45–52; DOI: 10.46298/dmtcs.3337; https://dmtcs.episciences.org/en/articles/3337.
2. A. Lindell and L. Holst, *Distributions of the longest excursions in a tied down simple random walk and in a Brownian bridge*, Journal of Applied Probability 44 (2007), 1056–1067; DOI: 10.1239/jap/1197908824.
3. L. Serlet, *Invariance Principle for the Random Walk Conditioned to Have Few Zeros*, Séminaire de Probabilités XLVI (2014), 461–472; DOI: 10.1007/978-3-319-11970-0_19; https://lmbp.uca.fr/~serlet/rwfew.pdf.
4. S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), 103–252; DOI: 10.1214/11-PS188.
