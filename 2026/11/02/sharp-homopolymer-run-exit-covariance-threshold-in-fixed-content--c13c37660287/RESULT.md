# Sharp homopolymer–run-exit covariance threshold in fixed-content binary words

## Finding

Let \(n\ge4\), let \(a\ge3\) and \(b\ge1\) be integers with \(a+b=n\), and choose a binary word \(W=W_1\cdots W_n\) uniformly from the \(\binom{n}{a}\) words with exactly \(a\) zeros and \(b\) ones. Define the overlapping length-three word counts
\[
X=\sum_{i=1}^{n-2}\mathbf 1\{W_iW_{i+1}W_{i+2}=000\},\qquad
Y=\sum_{i=1}^{n-2}\mathbf 1\{W_iW_{i+1}W_{i+2}=001\}.
\]
Thus \(X\) counts three-zero homopolymer windows, while \(Y\) counts windows where two zeros are followed by a one (a zero-run exit).

**Theorem.** For every such \((n,a,b)\),
\[
\boxed{\operatorname{Cov}(X,Y)=
\frac{a b^2(a-1)(a-2)\bigl[(n+6)(n-1)-(4n-6)a\bigr]}
{n^2(n-3)(n-2)(n-1)^2}.}
\tag{1}
\]
Consequently, with
\[
\tau_n=\frac{(n+6)(n-1)}{4n-6}
=\frac n4+\frac{13}{8}+\frac{15}{8(2n-3)},
\tag{2}
\]
the covariance is positive precisely when \(a<\tau_n\), zero when \(a=\tau_n\), and negative precisely when \(a>\tau_n\). The **only nondegenerate zero-covariance compositions** in the entire domain are
\[
(n,a,b)=(4,3,1)\quad\text{and}\quad(9,4,5).
\tag{3}
\]
For \(a\le2\), \(X\) vanishes identically, giving an additional trivial zero-covariance case outside the displayed theorem's nondegenerate domain.

If \(a/n\to p\in(0,1)\) as \(n\to\infty\), then
\[
\frac1n\operatorname{Cov}(X,Y)\longrightarrow
p^3(1-p)^2(1-4p).
\tag{4}
\]
Thus the limiting sign threshold is the zero proportion \(1/4\), and the exact finite-size crossover is confined to an additive \(O(1)\) window around \(n/4\).

## Assumptions and scope

The sampling is **without replacement**: the total numbers of zero and one symbols are fixed. The word is linear, not circular, and windows overlap and are counted at all starting positions \(1,\ldots,n-2\). There is no independence assumption between different windows. The theorem concerns covariance, not independence; zero covariance in (3) is not asserted to imply independence.

The fixed-composition model is the exact conditional random-arrangement null for binary sequence-pattern statistics. If the maximal zero runs have lengths \(L_j\), and \(E_j\) indicates that run \(j\) is followed by a one, then \(X=\sum_j (L_j-2)_+\) and \(Y=\sum_j E_j\mathbf 1\{L_j\ge2\}\). Thus \(X\) measures excess lengths of long zero runs, while \(Y\) counts how many such runs exit into a one. Their joint covariance enters calibration of contrasts formed from these two natural run-profile observables.

## Proof

Write \((x)_k=x(x-1)\cdots(x-k+1)\) for falling factorials, with \((x)_0=1\). For a prescribed collection of \(r\) distinct positions containing \(u\) zeros and \(r-u\) ones, exchangeability under fixed composition gives probability
\[
\frac{(a)_u(b)_{r-u}}{(n)_r}.
\tag{5}
\]
Hence
\[
\mathbb EX=(n-2)\frac{(a)_3}{(n)_3},\qquad
\mathbb EY=(n-2)\frac{(a)_2b}{(n)_3}.
\tag{6}
\]

For the ordered joint count \(XY\), let the \(000\) window start at \(i\) and the \(001\) window start at \(j\). If \(j=i\) or \(j<i\) with \(i-j\le2\), the prescriptions conflict; if \(j=i+1\), their union is \(0001\); if \(j=i+2\), it is \(00001\). All windows with \(|j-i|\ge3\) are disjoint and prescribe five zeros and one one. For \(n\ge6\), the corresponding numbers of ordered pairs are \(n-3\), \(n-4\), and \((n-4)(n-5)\), respectively. Thus
\[
\begin{aligned}
\mathbb E[XY]={}&(n-3)\frac{(a)_3b}{(n)_4}
 +(n-4)\frac{(a)_4b}{(n)_5}\\
&+(n-4)(n-5)\frac{(a)_5b}{(n)_6}.
\end{aligned}
\tag{7}
\]
Subtracting the product of the expectations in (6), using \(n=a+b\), and canceling common factors gives exactly (1). This is an identity of rational functions and requires no limiting argument.

For the short cases, direct enumeration under the \(\binom{n}{a}\) uniform words gives
\[
\begin{array}{c|c|c|c}
n&a&b&\operatorname{Cov}(X,Y)\\ \hline
4&3&1&0\\
5&3&2&1/50\\
5&4&1&-3/25
\end{array}
\]
which agrees with (1) and completes its proof for \(n\ge4\).

Every factor of (1) outside the square bracket is positive on the stated domain. This proves the strict sign classification from comparison of \(a\) with (2). To classify the equality cases, suppose
\[
(4n-6)a=(n+6)(n-1).
\tag{8}
\]
Then \(t=2n-3\) divides \((n+6)(n-1)\). Multiplying by four and reducing modulo \(t\) yields
\[
4(n+6)(n-1)=(2n+12)(2n-2)\equiv15\pmod t.
\]
Hence \(t\mid15\). Because \(n\ge4\), \(t\ge5\), so \(t=5\) or \(15\); these give \(n=4\) or \(9\), and (8) then forces \(a=3\) or \(4\), respectively. This proves (3).

Expanding (2) gives the stated additive crossover scale. Dividing (1) by \(n\) and taking \(a/n\to p\) gives (4).

## Verification

The accompanying standalone `verify_pattern_covariance.py` requires only the Python standard library. It independently enumerates every fixed-composition binary word for all lengths \(4\le n\le17\), compares the first mixed moments and covariance with (1), separately recomputes the ordered window-placement expectations for \(4\le n\le20\), and checks integer sign and zero cases for \(4\le n\le400\). Its completed output is:

```text
EXACT_CHECKS_PASSED 79723
NONDEGENERATE_ZERO_PAIRS [(4, 3), (9, 4)]
ALL_DONE
```

These are finite checks, not an infinite proof. Equations (5)–(8), including the divisibility argument, prove the theorem for every integer composition in its stated domain. No stochastic independence claim is inferred from a vanishing covariance.

## Relationship to prior work

Rukhin (2010) develops joint pattern-frequency generating functions and correlation matrices for stationary Markov sources and rare long patterns; its examples concern independent or Markov-generated sequences. Régnier (2000) provides a general framework for word occurrences, including exact moment calculations in Bernoulli and Markov models. Neither model is the uniform law **conditioned on fixed zero and one counts**, and the inspected portions do not state the finite-composition threshold (2) or the exceptional equality classification (3).

The previously published exact dependence phases for fixed-composition **two-position transition indicators** provide the closest fixed-count comparison. Its adjacent/disjoint local transition covariances have thresholds \((a-b)^2=n\) and \((a-b)^2=n(n-2)/(2n-3)\). Those are different observables and different thresholds from (2); no identity of statements or reduction to the two-position pair classification was identified. The present proof explicitly enumerates the three-position and six-position overlaps needed for the two motif counts.

## Limitations

The result covers this specific, motivated pair of length-three motifs in binary fixed-count words, not all patterns or larger alphabets. The exact covariance controls only second-order dependence; it does not determine the full joint law, infer independence at (3), establish a new hypothesis test, or prove an improvement in statistical power. A more general multivariate word-count generating function may encode the result implicitly, so historical priority for a formula not written in these terms remains a risk.

## References

1. A. L. Rukhin, “Joint Distribution of Pattern Frequencies and Multivariate Polya–Aeppli Law,” *Theory of Probability and Its Applications* **54** (2010), 246–260. DOI: [10.1137/S0040585X97984115](https://doi.org/10.1137/S0040585X97984115). Public record dated 2010-01-14: [NIST](https://www.nist.gov/publications/joint-distribution-pattern-frequencies-and-multivariate-polya-aeppli-law).
2. M. Régnier, “A unified approach to word occurrence probabilities,” *Discrete Applied Mathematics* **104** (2000), 259–280. DOI: [10.1016/S0166-218X(00)00195-5](https://doi.org/10.1016/S0166-218X(00)00195-5).
3. A. L. Rukhin, “Pattern correlation matrices for Markov sequences and tests of randomness,” *Theory of Probability and Its Applications* **51** (2007), 663–679; original 2006. DOI: [10.4213/tvp21](https://doi.org/10.4213/tvp21).
4. “Exact dependence phases of fixed-composition run transitions,” [published result](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-dependence-phases-of-fixed-composition-run-transitions--c6b28ad6d93d), accessed 2026-10-31 UTC.
