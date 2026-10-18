# Fixed-composition binary runs: exact Poisson–binomial boundary and variance gap

## Finding
Let \(a,b\) be nonnegative integers with \(N=a+b\ge1\). Choose uniformly among the \(\binom{N}{a}\) binary words containing exactly \(a\) copies of the first symbol and \(b\) of the second. Define the transition count
\[
T=\sum_{j=1}^{N-1}\mathbf{1}\{X_j\ne X_{j+1}\}.
\]
A *Poisson–binomial* law is the law of a finite sum of independent Bernoulli random variables, allowing probabilities \(0\) and \(1\) and allowing an empty sum. Then
\[
\boxed{T\text{ has a Poisson–binomial law}\ \Longleftrightarrow\ \min(a,b)\le1.}
\]
When \(a,b\ge2\), let \(m=\min(a,b)\), \(h=\max(a,b)\), \(M=2m-\mathbf{1}\{h=m\}\), and \(\mu=2ab/N\). Every Poisson–binomial law supported on exactly the same endpoint range \(\{1,\ldots,M\}\) and having mean \(\mu\) must have variance at most
\[
U=\frac{(\mu-1)(M-\mu)}{M-1}.
\]
The actual variance exceeds this limit by the following **exact, strictly positive gap**:
\[
\boxed{\operatorname{Var}(T)-U=
\begin{cases}
\dfrac{2m(m-1)(h-m)(2mh-m-h)}{(m+h)^2(2m-1)(m+h-1)},& h>m,\\[6pt]
\dfrac{m-1}{2(2m-1)},&h=m.
\end{cases}}
\]
The two arms of the statement cover every integer composition, not only asymptotic or balanced compositions.

## Assumptions and scope
The word has a fixed deterministic number of each symbol and is uniformly randomly ordered; this is the usual conditional two-class randomization null underlying the Wald–Wolfowitz runs test. The statistic \(T\) counts *changes* (one fewer than the number of constant runs). Probability parameters in a putative Poisson–binomial representation are arbitrary and need not match the marginal probabilities of individual transition indicators. No independence of the transition indicators is assumed. For \(a=0\) or \(b=0\), \(T=0\). If \(m=1<h\), \(T=1+Y\) with \(Y\sim\operatorname{Bernoulli}((h-1)/(h+1))\). If \(a=b=1\), \(T=1\) identically.

## Proof
**Endpoints and range.** Suppose \(a,b\ge1\) and write \(m=\min(a,b)\), \(h=\max(a,b)\). The smallest possible number of transitions is \(1\), attained by either word with a single block of each letter. The largest is \(M=2m\) if \(h>m\), attained by alternating all minority letters between majority letters, and \(M=2m-1\) if \(h=m\), attained by alternating letters throughout. Both endpoints have positive probability.

**Mean and variance.** Set \(I_j=\mathbf{1}\{X_j\ne X_{j+1}\}\). Sampling positions without replacement gives
\[
\Pr(I_j=1)=\frac{2ab}{N(N-1)},\quad
\Pr(I_j=I_{j+1}=1)=\frac{ab}{N(N-1)}.
\]
For \(|j-k|\ge2\) and \(N\ge4\),
\[
\Pr(I_j=I_k=1)=\frac{4a(a-1)b(b-1)}{N(N-1)(N-2)(N-3)}.
\]
There are \(N-2\) adjacent indicator pairs and \((N-2)(N-3)/2\) disjoint indicator pairs. Summing variances and twice the pair covariances, and cancelling algebraically, yields
\[
\mu=\mathbb ET=\frac{2ab}{N},\qquad
V=\operatorname{Var}(T)=\frac{2ab(2ab-N)}{N^2(N-1)}.
\]
The formula also holds for \(N=2,3\), directly by enumeration; the disjoint-pair term is absent there.

**Poisson–binomial variance ceiling.** Let a random variable \(Y\) supported between \(1\) and \(M\), with both endpoints of positive mass, be representable as a sum of independent Bernoulli variables. Remove all identically zero Bernoullis. Because its minimum is \(1\), exactly one summand is identically \(1\); because its maximum is \(M\), the other \(M-1\) summands are nondegenerate Bernoullis. Write their parameters as \(u_1,\ldots,u_{M-1}\in(0,1)\). With \(\mathbb EY=\mu\), they sum to \(\mu-1\), and Cauchy–Schwarz yields
\[
\operatorname{Var}(Y)=\sum_{i=1}^{M-1}u_i(1-u_i)
=\mu-1-\sum_{i=1}^{M-1}u_i^2
\le (\mu-1)\left(1-\frac{\mu-1}{M-1}\right)=U.
\]
This is a necessary condition, regardless of the original dependence among the \(I_j\).

**Sharp positive violation.** For \(h>m\ge2\), substitute \(a=m,b=h,M=2m\) and the displayed \(\mu,V\); a common denominator gives
\[
V-U=\frac{2m(m-1)(h-m)(2mh-m-h)}{(m+h)^2(2m-1)(m+h-1)}>0.
\]
Every factor is positive: in particular \(2mh-m-h=(m-1)(h-1)+mh-1>0\). If \(h=m\ge2\), substitute \(M=2m-1\) to obtain \(V-U=(m-1)/(2(2m-1))>0\). These contradictions exclude all independent-Bernoulli representations whenever both symbol counts are at least two.

**Attainability in the remaining cases.** If \(m=0\), the transition count is zero. If \(m=1<h\), the exceptional letter lies at an endpoint with probability \(2/(h+1)\), yielding one transition; otherwise it lies inside and yields two. Hence \(T=1+\operatorname{Bernoulli}((h-1)/(h+1))\) in distribution. If \(a=b=1\), \(T=1\). This proves both directions.

## Verification
The independent standard-library checker `verify.py` evaluates the exact finite-composition run enumerator
\[
\#\{T=2k-1\}=2\binom{a-1}{k-1}\binom{b-1}{k-1},
\]
\[
\#\{T=2k\}=\binom{a-1}{k}\binom{b-1}{k-1}
+\binom{a-1}{k-1}\binom{b-1}{k}
\]
(with out-of-range binomial coefficients interpreted as zero) and compares it with direct enumeration for all positive integer \(a,b\le6\). It checks the exact mean, variance, support endpoint, and variance gap across an additional rectangular range of integer parameters. The infinite-parameter statement is proved symbolically above; finite checks are not a substitute for the proof. Execute `python verify.py` with Python 3.

## Relationship to prior work
The classical Wald–Wolfowitz conditional runs distribution gives the fixed-margin randomization context and known moments. Kong, *Joint distribution of rises, falls, and number of runs in random sequences* (published online January 5, 2018; accessible author full text, arXiv:2405.01748), derives joint counting generating functions for arbitrary multiset specifications; its formulas encompass binary runs counts. It does not establish the independence-representation boundary or the exact variance gap. Oh and Jang, *On Success runs of a fixed length defined on a q-sequence of binary trials* (arXiv:2210.04521, October 10, 2022), derive distributions for fixed-length runs under a varying-probability binary process, a different sampling and counting scheme. The present result is not the known elementary fact that the individual transition indicators are dependent: dependence of one representation does not rule out an independent-summand **distributional** representation. The proof instead rules out every alternative Poisson–binomial factorization.

## Limitations
The theorem concerns two symbols with their multiplicities conditioned exactly. It does not characterize unconditioned Bernoulli runs, multicolor fixed-composition words, weighted word-order distributions, or optimal approximations outside the Poisson–binomial class. The historical priority assessment is necessarily limited by incomplete access to some classical runs and randomization literature. Independent external mathematical validation has not been performed.

## References
1. Y. Kong, "Joint distribution of rises, falls, and number of runs in random sequences," *Communications in Statistics—Theory and Methods* 48 (2019), 493–499. DOI: 10.1080/03610926.2017.1414261. Public online date January 5, 2018. Lawful full text: https://arxiv.org/abs/2405.01748.
2. J. Oh and D.-G. Jang, "On Success runs of a fixed length defined on a q-sequence of binary trials," arXiv:2210.04521 (first posted October 10, 2022), https://arxiv.org/abs/2210.04521.
3. A. Wald and J. Wolfowitz, "On a test whether two samples are from the same population," *Annals of Mathematical Statistics* 11 (1940), 147–162. Classical conditional runs test.
