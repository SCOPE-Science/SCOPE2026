# Exact affine positional laws for consecutive triples in Ewens permutations

## Finding
Let \(n\ge3\) and \(\theta>0\). Under the Ewens law on permutations, the complete six-pattern distribution of each consecutive triple is an explicit rational function whose numerator is a polynomial in \(\theta\) with *affine coefficients in the triple's starting position*. The monotone patterns are stationary in position, while the four nonmonotone patterns exhibit exact linear slopes that change direction at the uniform measure \(\theta=1\).

Write \(B=\binom{n-1}{3}\), \(T=\binom{n-2}{2}\), \(h=n-3\), \(g=n-i-2\) and \(j=i-1\). Set \(W=(\theta+n-3)(\theta+n-2)(\theta+n-1)\). The probability of pattern \(\tau\) at positions \(i,i+1,i+2\) is \(F_\tau/W\), where:

| \(\tau\) | \(F_\tau\) |
|:--|:--|
| 123 | \(B+T\theta+h\theta^2+\theta^3\) |
| 132 | \(B-g+(T+h)\theta+(g+1)\theta^2\) |
| 213 | \(B-j+(T+h)\theta+(j+1)\theta^2\) |
| 231 | \(B+g+(T+1)\theta+j\theta^2\) |
| 312 | \(B+j+(T+1)\theta+g\theta^2\) |
| 321 | \(B+(T+h)\theta+\theta^2\) |

For \(n\ge4\), adjacent starting positions both exist. Their exact probability differences are
\[
P(132\text{ at }i+1)-P(132\text{ at }i)
=P(312\text{ at }i+1)-P(312\text{ at }i)
=\frac{1-\theta^2}{W},
\]
\[
P(213\text{ at }i+1)-P(213\text{ at }i)
=P(231\text{ at }i+1)-P(231\text{ at }i)
=\frac{\theta^2-1}{W}.
\]
Thus for \(0<\theta<1\) the 132/312 probabilities rise from left to right and 213/231 fall, and for \(\theta>1\) every orientation reverses. The probabilities of 123 and 321 are exactly position-independent. At \(\theta=1\) all six probabilities equal \(1/6\) at every position. No asymptotic or independence assumption is used.

## Assumptions and scope
A permutation \(\pi\in S_n\) has \(C(\pi)\) disjoint cycles. Its probability under Ewens parameter \(\theta>0\) is \(\theta^{C(\pi)}/\theta^{\overline n}\), with \(\theta^{\overline n}=\prod_{r=0}^{n-1}(\theta+r)\). Pattern 132 means that the first entry is smallest, the second largest and the third middle, with the analogous ranking convention for all six types. We take every integer \(n\ge3\) and every \(1\le i\le n-2\). Binomial coefficients with upper argument below the lower argument are zero.

## Proof
**1. Completing specified permutation arrows.** Fix three distinct domain vertices \(I=\{i,i+1,i+2\}\) and three distinct images \(a,b,c\), with the image order fixed by a given pattern \(\tau\). The prescribed arrows form disjoint directed paths and possibly directed cycles. Let \(\kappa\) be the number of cycles fully closed by these three arrows. Removing these closed cycles and contracting each prescribed open path produces a permutation on \(n-3\) free units, and conversely every permutation of those units lifts uniquely. The Ewens cycle-count weight over all completions therefore is
\[
\sum_{\pi:\,\pi|_I=(a,b,c)}\theta^{C(\pi)}
=\theta^\kappa\theta^{\overline{n-3}}.
\]
Consequently, the pattern probability equals \(F_\tau/W\), with
\[
F_\tau=\sum_{1\le a<b<c\le n}\theta^{\kappa(\tau;a,b,c,i)},
\qquad W=(\theta+n-3)(\theta+n-2)(\theta+n-1).
\]

**2. A degree-three polynomiality lemma.** Set \(u=i-1\ge0\) and \(v=n-i-2\ge0\), so \(n=u+v+3\). Let \(\mathcal C\) denote the eight directed simple cycles entirely inside \(I\): three loops, three unoriented two-cycles (each forces both arrows), and the two orientations of a three-cycle. In each partial-arrow diagram, its closed cycles are vertex-disjoint. For every diagram, expand
\[
\theta^{\kappa}=
\sum_{\Gamma\text{ a subset of its closed cycles}}(\theta-1)^{|\Gamma|}.
\]
Reverse the sums. For each fixed vertex-disjoint collection \(\Gamma\subseteq\mathcal C\), the requirement that these arrows occur in a type-\(\tau\) increasing selection \(a<b<c\) forces a subset of the three ranks to have prescribed values among \(i,i+1,i+2\). If incompatible with the rank order, the contribution is zero. Otherwise, write the prescribed increasing ranks as \(r_1<\cdots<r_s\), with corresponding prescribed image values \(y_1<\cdots<y_s\); use artificial boundaries \(r_0=0,r_{s+1}=4,y_0=0,y_{s+1}=n+1\). The exact number of compatible increasing triples is
\[
B_{\Gamma,\tau}(u,v)=
\prod_{m=0}^{s}\binom{y_{m+1}-y_m-1}{r_{m+1}-r_m-1}.
\]
Each factor has an affine nonnegative upper argument in \(u,v\), while the total of its fixed lower arguments is \(3-s\le3\). Hence \(B_{\Gamma,\tau}\) is a polynomial in \(u,v\) of total degree at most three. It follows that each coefficient of \(\theta\) in \(F_\tau\) is a polynomial in \((u,v)\) of total degree at most three, valid at every integer \(u,v\ge0\). This reasoning also applies at \(n=3\), since no negative gap sizes arise for compatible arrows.

**3. Exact algebraic identity certificate, valid for all lengths.** For each of the six patterns, the right side in the displayed table also has total \((u,v)\)-degree at most three coefficientwise in \(\theta\). Two such bivariate polynomials coincide identically if they agree on the ten triangular lattice points \(u,v\ge0\), \(u+v\le3\). To prove this interpolation fact, use the basis \(\binom ua\binom vb\), for \(a+b\le3\), whose evaluation on these ten points is triangular with diagonal ones (ordered by total degree). These ten points correspond precisely to all triple starts for \(3\le n\le6\). Direct exact enumeration of the \(\binom n3\) increasing image triples, counting their closed directed cycles, confirms all six rows at each of the ten positions; `verify.py` performs precisely these coefficient-by-coefficient integer checks, independently of the completion recurrence. Because of the established degree bound and the triangular interpolation theorem, these finitely many exact checks prove the displayed formulas **for every** \(n\ge3\), rather than extrapolating from small cases.

Subtracting successive rows at \(i\) and \(i+1\) yields the four stated differences. The two remaining numerators have no \(i\)-dependence. Setting \(\theta=1\) gives \(F_\tau=\binom n3\) for all six patterns and \(W=n(n-1)(n-2)\), hence the common probability \(1/6\).

## Verification
The standalone standard-library program `verify.py` checks all six coefficient identities directly by the specified-three-arrow closure method at all positions for \(3\le n\le11\), including all ten degree-determining nodes. It separately exhausts full permutations for \(3\le n\le7\), four positive rational choices of \(\theta\), and all positions, verifying the rational probabilities against Ewens-weighted exact fractions. All assertions passed. The formal all-length argument uses the explicit degree-three lemma and polynomial unisolvence, not numerical evidence alone.

## Relationship to prior work
Féray (2013) establishes asymptotic results for dashed-pattern counts under Ewens sampling. Kammoun (arXiv:2012.05845, publicly posted 2020-12-10, especially Proposition 31 and the descent-process results) establishes central-limit and local-limit universality for vincular patterns under conjugacy-invariant laws, not the exact finite-length, starting-position-resolved six-pattern probabilities here. Pinsky and Schickentanz (arXiv:2510.20654, first posted 2025-10-23, Theorem 1) determine the Ewens one-pair inversion probabilities and their parameter dependence. Those two-point marginals do not determine the joint order distribution of three entries; the present position-dependent triple probabilities are a genuine higher-order question. The position-invariant individual adjacent descent marginal consequently coexists with a position-varying joint law for two adjacent comparisons. The result is not a claim of a novel method of marking cycles; it is a specific complete finite-size six-pattern classification and its sharp \(\theta=1\) gradient reversal.

## Limitations
The six-pattern formulas describe only length-three **consecutive** windows for the standard Ewens distribution, not arbitrary lengths or gaps, nor whole-process covariance matrices or asymptotic central limit theorems. The cyclic-completion lemma and low-degree interpolation are elementary; older literature on cycle-weighted Eulerian or joint pattern statistics might contain an implicit equivalent formula. No historical-priority guarantee or independent audit is claimed. Outside \(\theta>0\) the formulas have standard limits for most \(n\), but the theorem is stated only on the positive parameter domain to avoid boundary normalization conventions.

## References
1. M. S. Kammoun, *Universality for random permutations and some other groups*, arXiv:2012.05845 (version 1, 2020-12-10), subsequently *Stochastic Processes and their Applications* 147 (2022), 76–106. https://arxiv.org/pdf/2012.05845
2. V. Féray, *Asymptotic behavior of some statistics in Ewens random permutations*, *Electronic Journal of Probability* 18 (2013), article 76. https://arxiv.org/abs/1201.2157
3. R. G. Pinsky and D. T. Schickentanz, *Inversions in Random Permutations Under the Ewens Sampling Distribution With and Without a Prescribed Number of Fixed Points*, arXiv:2510.20654 (first posted 2025-10-23). https://arxiv.org/pdf/2510.20654
