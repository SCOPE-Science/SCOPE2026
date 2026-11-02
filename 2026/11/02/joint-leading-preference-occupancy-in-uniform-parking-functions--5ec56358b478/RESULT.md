# Joint leading-preference occupancy in uniform parking functions

## Finding
For each integer \(n\ge2\), choose uniformly a classical parking function \(\pi=(a_1,\ldots,a_n)\), and write \(N_j=\#\{i:a_i=j\}\). Its exact bivariate enumerator is
\[
\sum_{\pi\in\mathrm{PF}_n} u^{N_1(\pi)}v^{N_2(\pi)}
=u^n+\sum_{k=1}^{n-1}\binom nk u^k(k-1+v)(n-1+v)^{n-k-1}.
\]
For \(1\le k\le n-1\), the complete conditional law is
\[
\boxed{\quad N_2\mid(N_1=k)\ \stackrel{d}{=}\ 
\operatorname{Bernoulli}(1/k)+\operatorname{Binomial}(n-k-1,1/n),\quad}
\]
with the two summands independent; when \(k=n\), \(N_2=0\) deterministically. The conditional laws are strictly decreasing in first-order stochastic order as \(k\) increases. In particular, for every strictly increasing real function \(h\) on \(\{0,\ldots,n\}\),
\[\operatorname{Cov}(N_1,h(N_2))<0.\]
The ordinary covariance is exactly
\[
\operatorname{Cov}(N_1,N_2)=2\left(\frac{n}{n+1}\right)^n-1-\frac{n-1}{(n+1)^2}<0,
\]
and tends to \(2/e-1\), a strictly negative constant. The joint weak limit is \((1+P,\ P'+B)\), where \(P,P'\) are independent \(\operatorname{Poisson}(1)\) variables and, conditional on \(P\), \(B\) is \(\operatorname{Bernoulli}(1/(1+P))\), independent of \(P'\).

## Assumptions and scope
A classical parking function is a word of \(n\) preferences from \(\{1,\ldots,n\}\) whose increasing rearrangement \(b_1\le\cdots\le b_n\) satisfies \(b_i\le i\) for all \(i\). Equivalently, all cars park by advancing to the first available spot at or beyond their preferred spot. The probability measure is uniform on the \((n+1)^{n-1}\) words satisfying this condition. We use the conventional definitions of binomial and Bernoulli variables, and stochastic comparison refers to all increasing test functions on their finite support. The case \(n=1\) is excluded because a preference for spot 2 is not defined.

## Proof
**1. The known one-preference enumerator.** For any integer \(m\ge1\), the established parking-function identity is
\[
A_m(t):=\sum_{q\in\mathrm{PF}_m}t^{\#\{i:q_i=1\}}=t(t+m)^{m-1};\qquad A_0(t)=1.
\]
This is the classical root-degree/number-of-ones formula, given, for example, in the sources listed below. We do not claim this identity as new. Its specialization at \(t=1\) counts \(\mathrm{PF}_m\).

**2. A weight-preserving decomposition.** Fix \(1\le k\le n\) and prescribe the \(k\) car indices that prefer spot 1. Parking validity is invariant under permuting car indices, so put those \(k\) cars first without changing admissibility or the two multiplicities. They occupy spots \(1,\ldots,k\). The remaining \(m=n-k\) preferences \(a_i\) all lie in \(\{2,\ldots,n\}\). Define \(q_i=\max\{1,a_i-k\}\). The remaining cars park in spots \(k+1,\ldots,n\) if and only if \(q\in\mathrm{PF}_m\): an original preference at most \(k+1\) enters at the first remaining spot, and a larger original preference shifts by \(k\) without altering the parking rule.

For any coordinate with \(q_i=1\), there are exactly \(k\) admissible original preferences \(2,3,\ldots,k+1\): the first option carries weight \(v\) for preference 2, and the other \(k-1\) options carry weight 1. A coordinate with \(q_i\ge2\) has exactly one preimage, \(a_i=q_i+k\), which does not contribute to \(N_2\). Thus the total weight with these \(k\) designated ones is \(A_m(k-1+v)\). Choosing the \(k\) designated positions multiplies by \(\binom nk\). When \(k=n\), the sole word is all ones. Summing over \(k\) gives the asserted bivariate polynomial, including all boundary values.

**3. Conditional factorization and ordering.** Set \(v=1\). For \(k<n\), the number of words with \(N_1=k\) is \(\binom nk k n^{n-k-1}\). Consequently the conditional generating polynomial for \(N_2\) is
\[
\mathbb E[v^{N_2}\mid N_1=k]
=\frac{k-1+v}{k}\left(\frac{n-1+v}{n}\right)^{n-k-1},
\]
which proves the independent Bernoulli-plus-binomial representation. Couple these variables for increasing \(k\) using one common uniform random variable for the Bernoulli term and a nested sequence of independent Bernoulli trials with parameter \(1/n\). Both the Bernoulli success probability and the number of binomial trials decrease. The coupled count cannot increase; with positive probability it strictly decreases for every adjacent pair of conditioning values, including the last step to \(k=n\). Thus the conditional expectations of every strictly increasing \(h\) strictly decrease. Since \(N_1\) has more than one possible value with positive probability, the independent-copy identity
\[
2\operatorname{Cov}(N_1,g(N_1))=\mathbb E[(N_1-N_1')(g(N_1)-g(N_1'))]
\]
with \(g(k)=\mathbb E[h(N_2)\mid N_1=k]\) proves strictly negative covariance.

**4. Exact covariance.** The first marginal enumerator from step 2 is \(u(u+n)^{n-1}\). Thus
\[
N_1\stackrel d=1+\operatorname{Binomial}(n-1,1/(n+1)),\quad
\mathbb E N_1=\frac{2n}{n+1},\quad
\operatorname{Var}N_1=\frac{n(n-1)}{(n+1)^2}.
\]
The conditional mean from step 3 is \(\mathbb E[N_2\mid N_1=k]=1/k+(n-k-1)/n\) for \(k<n\); this expression also equals zero at \(k=n\), so holds throughout the support as a numerical identity. For \(K=1+\operatorname{Binomial}(n-1,p)\), the elementary integral \(1/k=\int_0^1t^{k-1}\,dt\) gives
\[
\mathbb E[1/K]=\frac{1-(1-p)^n}{np},\quad p=\frac1{n+1}.
\]
Therefore
\[
\operatorname{Cov}(N_1,N_2)=\operatorname{Cov}(N_1,1/N_1)-\frac1n\operatorname{Var}(N_1)
=2\left(\frac n{n+1}\right)^n-1-\frac{n-1}{(n+1)^2}.
\]
For \(n\ge2\), the binomial expansion gives \((1+1/n)^n>2\), hence the covariance is strictly negative. Taking the limit yields \(2/e-1\).

**5. Joint limit.** The binomial representation of \(N_1\) tends to \(1+\operatorname{Poisson}(1)\). For each fixed \(k\), the conditional binomial part of \(N_2\) tends to an independent \(\operatorname{Poisson}(1)\), while its Bernoulli term retains parameter \(1/k\). Tightness of \(N_1\), together with convergence on each fixed conditioning class, proves the joint weak limit stated in the finding. The uniform boundedness of the first two moments in the representations justifies the covariance limit independently of weak convergence.

## Verification
The standalone standard-library Python script \(\texttt{verify.py}\) enumerates all preference sequences for sizes \(2\) through \(6\), independently enumerates admissible multiplicity vectors through size \(9\), compares the exact bivariate polynomial, and checks rational covariance and conditional means. It also tests the strict regression inequalities at sizes through \(100\). The extracted script completed 5,026 assertions. These finite tests corroborate but do not replace the all-size argument above.

## Relationship to prior work
The classical enumeration and root-degree/ones identity \(A_m(t)=t(t+m)^{m-1}\) are previously established (Yan; Diaconis–Hicks; Stanley–Yin). Gessel–Seo give another foundational parking-function interpretation and the corresponding lucky-car enumerator. Stanley–Yin's joint polynomial concerns the number of ones, leading-element multiplicity, and unlucky cars; the number of preferences equal to **2** is a different statistic and cannot be recovered merely by replacing their unlucky count. Kenyon–Yin study single-coordinate preferences and covariance between coordinate positions rather than the joint numbers occupying the two specified preference values. The present finding is the explicit two-value multiplicity distribution, its conditional stochastic ordering, and its persistent covariance, not the established one-value marginal or general parking-function enumeration.

## Limitations
The finding concerns the two boundary preference values \(1,2\), not all consecutive preference pairs or arbitrary parking protocols. General multivariate parking-function enumerators might yield an alternative derivation, so historical priority is not independently certified. The all-size claims are established symbolically; finite checks are not proofs by exhaustion. No independent audit has been performed.

## References
- I. M. Gessel and S. Seo, *A refinement of Cayley's formula for trees*, arXiv:math/0507497 (first posted 2005-07-24), especially Section 10.
- C. H. Yan, *Parking functions*, in *Handbook of Enumerative Combinatorics* (2015), Corollary 1.16 as cited in the next source.
- P. Diaconis and A. Hicks, *Probabilizing parking functions*, arXiv:1611.09821 (2016), especially Section 3 on the number of ones.
- R. Kenyon and M. Yin, *Parking functions: from combinatorics to probability*, arXiv:2103.17180 (2021), especially Section 3 on coordinate distributions.
- R. P. Stanley and M. Yin, *Some enumerative properties of parking functions*, arXiv:2306.08681 (2023), especially Theorem 4.2 and Corollary 4.3.
