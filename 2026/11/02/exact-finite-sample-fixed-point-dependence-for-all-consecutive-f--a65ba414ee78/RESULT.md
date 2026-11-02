# Exact finite-sample fixed-point dependence for all consecutive four-patterns

## Finding

Let \(\pi\) be uniform on the permutations of \(\{1,\ldots,n\}\), where \(n\ge4\). Let \(F\) count fixed points, and for each permutation pattern \(\tau\) of length four let \(N_\tau\) count contiguous four-position windows whose values have relative order \(\tau\). Overlapping windows count separately. Define
\[
Q_\tau(n)=6n(n-1)(n-2)\operatorname{Cov}(F,N_\tau).
\]
Every \(Q_\tau\) is the quadratic polynomial in the following complete table. A listed second pattern denotes the reverse-complement mate of the first, and has the same polynomial. The map \(\pi(i)\mapsto n+1-\pi(n+1-i)\) preserves both the uniform law and fixed-point count, and explains these paired entries.

| Consecutive pattern(s) | \(Q_\tau(n)\) |
|:--|:--|
| `1234` | \(3(n-1)(n-2)\) |
| `1243`, `2134` | \(2(n^2-3n-1)\) |
| `1324` | \(3(n-3)(n-2)\) |
| `1342`, `3124` | \(2(n-5)(n-4)\) |
| `1423`, `2314` | \((n-4)(n+1)\) |
| `1432`, `3214` | \(n^2-9n+26\) |
| `2143` | \((n-5)(n+2)\) |
| `2341`, `4123` | \(-n^2+9n-26\) |
| `2413` | \(-n^2+9n-26\) |
| `2431`, `4213` | \(-2(n-5)(n-4)\) |
| `3142` | \(n^2-21n+62\) |
| `3241`, `4132` | \(-(n-4)(n+1)\) |
| `3412` | \(-n^2-9n+46\) |
| `3421`, `4312` | \(-2(n^2-3n-1)\) |
| `4231` | \(-3(n-6)(n-3)\) |
| `4321` | \(-3(n^2-7n+14)\) |

Precisely three patterns attain both positive and negative covariance as \(n\) ranges over integers at least four. Pattern `2143` is negative at \(n=4\), zero at \(n=5\), and positive for \(n\ge6\). Pattern `4231` is positive at \(n=4,5\), zero at \(n=6\), and negative for \(n\ge7\). Pattern `3142` is strictly negative for \(4\le n\le17\) and strictly positive for \(n\ge18\), without an integer zero. All other patterns retain one weak sign, with zeros only where their displayed factors vanish. If \(a_\tau\) is the coefficient of \(n^2\) in its displayed quadratic, then \(n\operatorname{Cov}(F,N_\tau)\to a_\tau/6\), giving the entire large-sample first-order covariance profile. This includes the delayed reversal
\[
\operatorname{Cov}(F,N_{3142})\big|_{n=17}=-\frac1{4080},\qquad
\operatorname{Cov}(F,N_{3142})\big|_{n=18}=\frac1{3672}.
\]

## Assumptions and scope

The probability law is uniform over all \(n!\) bijections from \(\{1,\ldots,n\}\) to itself; a fixed point means \(\pi(i)=i\), not a cycle record or a local extremum. In a window beginning at \(a\), the pattern is obtained by replacing its four values with their ranks among those four values. We require integer \(n\ge4\); there are \(n-3\) possible contiguous windows. Every covariance and expected value is ordinary finite-population covariance. The theorem concerns all 24 length-four patterns and all admissible sample sizes, not only the examples in the verification program.

## Proof

Write \(I_t=\mathbf1\{\pi(t)=t\}\), and \(P_{\tau,a}\) for the occurrence indicator in the window at positions \(a,a+1,a+2,a+3\). Uniform exchangeability gives \(\mathbb EF=1\) and \(\mathbb EN_\tau=(n-3)/24\). If \(t\) lies outside the given window, then conditioning on \(I_t=1\) leaves its four remaining values exchangeable, so \(\mathbb E[P_{\tau,a}\mid I_t=1]=1/24\).

For \(t=a+\ell-1\), where \(1\le\ell\le4\), let \(r=\tau_\ell\). Conditional on \(\pi(t)=t\), the other three values are sampled without replacement from \(\{1,\ldots,n\}\setminus\{t\}\). To produce the specified pattern one must choose exactly \(r-1\) of the remaining values below \(t\) and \(4-r\) above \(t\); their positions are then uniquely prescribed. Hence
\[
\mathbb P(P_{\tau,a}=1\mid I_t=1)
=\frac{\binom{t-1}{r-1}\binom{n-t}{4-r}}{(n-1)(n-2)(n-3)}.
\]
Summing the \(n\) fixed-point indicators, with the \(n-4\) off-window terms removed by covariance centering, proves the exact conditional-moment identity
\[
\operatorname{Cov}(F,N_\tau)=\frac1n\left[
\frac{\displaystyle\sum_{\ell=1}^4\sum_{t=\ell}^{n-4+\ell}
\binom{t-1}{\tau_\ell-1}\binom{n-t}{4-\tau_\ell}}{(n-1)(n-2)(n-3)}
-\frac{n-3}{6}\right]. \tag{1}
\]
For any fixed rank \(r\in\{1,2,3,4\}\), partitioning four-element subsets by their \(r\)-th smallest value yields the elementary Vandermonde identity
\[
\sum_{t=1}^{n}\binom{t-1}{r-1}\binom{n-t}{4-r}=\binom n4.
\]
Define the missing-endpoint count
\[
E_\tau(n)=\sum_{\ell=1}^4\left[
\sum_{t=1}^{\ell-1}\binom{t-1}{\tau_\ell-1}\binom{n-t}{4-\tau_\ell}
+\sum_{t=n-3+\ell}^{n}\binom{t-1}{\tau_\ell-1}\binom{n-t}{4-\tau_\ell}
\right], \tag{2}
\]
with empty sums equal to zero. Inserting the full Vandermonde sums into (1), then subtracting (2), gives the universal boundary-defect formula
\[
\boxed{\operatorname{Cov}(F,N_\tau)
=\frac1{2n}-\frac{E_\tau(n)}{n(n-1)(n-2)(n-3)}.} \tag{3}
\]
The dependence on each pattern enters only through missing rank-conditioned placements at the ends of the ordered labels.

The exclusions in (2) have at most three terms per end per pattern position. Each is a polynomial of degree at most three in \(n\), because either \(t\) or \(n-t\) is one of the fixed integers from zero to three. Consequently
\[
R_\tau(n)=3(n-1)(n-2)(n-3)-6E_\tau(n)
\]
is a polynomial of degree at most three, and \(R_\tau(n)=(n-3)Q_\tau(n)\) by (3). For each of the 24 patterns, substituting \(n=4,5,6,7\) into the finite binomial sums (2) gives \(R_\tau(n)=(n-3)Q_\tau(n)\) for the listed polynomial. Both sides have degree at most three, so equality at these four distinct inputs is a polynomial identity for all \(n\); thus the table is proved for every integer \(n\ge4\). The four-input integer certificates for all patterns are recomputed independently by the supplied standalone verifier.

For the three sign-changing patterns, the endpoint sums additionally simplify directly to
\[
E_{2143}(n)=\frac{(n-3)(n^2-3n+8)}3,\quad
E_{3142}(n)=\frac{(n-3)(n^2+6n-28)}3,\quad
E_{4231}(n)=(n-3)(n^2-6n+10).
\]
Substitution into (3) gives their displayed quadratics without interpolation. Every denominator in the definition of \(Q_\tau\) is strictly positive for \(n\ge4\). The factorizations in the table establish all signs: the only nontrivial changing quadratic, \(n^2-21n+62\), is negative at integer arguments from four through seventeen and positive from eighteen onward, since its larger real root lies strictly between seventeen and eighteen. The remaining nonfactored quadratics are either positive for all admissible integers or have an explicitly constant sign there. This completes the classification.

## Verification

The accompanying `checker.py` uses exact integers and rational numbers, with no third-party dependencies. It verifies the four-input polynomial certificates for every pattern, directly tests formula (3) for additional integer sizes through 100, and independently exhausts all 46,224 permutations of orders four through eight to compare the true joint moments with the proposed covariances. It checks the three sign changes and the conservation identity \(\sum_\tau \operatorname{Cov}(F,N_\tau)=0\), which follows independently from \(\sum_\tau N_\tau=n-3\). The program completed 954 exact assertions successfully. The general theorem follows from the degree bound and polynomial-identity argument, not empirical extrapolation.

## Relationship to prior work

Paguyo (2021, arXiv:2112.07728, initial version) analyzes fixed points, descents and inversions in the probabilistic setting of permutation double cosets, but not joint moments of fixed points and each consecutive four-pattern. Borga (2020, arXiv:2003.08426) studies central limits for consecutive-pattern counts in permutation families; the stated results do not give this exact uniform-permutation mixed covariance classification. Fulman, Kim and Lee (2019, arXiv:1902.00978) study peaks conditional on cycle structure, which concerns aggregated length-three peaks rather than the present individual four-pattern tensor. Allen and collaborators (2020, arXiv:2011.12179) study expected distinct consecutive patterns rather than their joint fixed-point moments. Previously reported exact dependence for descents or records does not imply the 24 length-four formulas without additional analysis. Full historical priority is not asserted.

## Limitations

The result requires the uniform permutation law and four consecutive positions. It makes no claim about nonconsecutive patterns, Mallows-weighted permutations, higher joint cumulants or independence. The covariance is generally of order \(n^{-1}\), so a finite sign diagram does not by itself establish a strong asymptotic dependence effect. Generalizations to patterns longer than four, and proof of historical priority, remain open here. Independent mathematical review has not been performed.

## References

1. J. E. Paguyo, *Fixed points, descents, and inversions in parabolic double cosets of the symmetric group*, arXiv:2112.07728, first submitted 2021-12-14. https://arxiv.org/abs/2112.07728
2. J. Borga, *Asymptotic normality of consecutive patterns in permutations encoded by generating trees with one-dimensional labels*, arXiv:2003.08426, first submitted 2020-03-18. https://arxiv.org/abs/2003.08426
3. J. Fulman, G. B. Kim and S. Lee, *Central limit theorem for peaks of a random permutation in a fixed conjugacy class*, arXiv:1902.00978, first submitted 2019-02-03. https://arxiv.org/abs/1902.00978
4. A. Allen and collaborators, *The Expected Number of Distinct Consecutive Patterns in a Random Permutation*, arXiv:2011.12179, first submitted 2020-11-24. https://arxiv.org/abs/2011.12179
