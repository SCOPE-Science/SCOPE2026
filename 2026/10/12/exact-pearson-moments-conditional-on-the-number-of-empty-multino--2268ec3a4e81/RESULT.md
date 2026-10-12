# Exact Pearson moments conditional on the number of empty multinomial cells
## Finding
Let
\[
(C_1,\ldots,C_m)\sim\operatorname{Multinomial}(N;1/m,\ldots,1/m),
\qquad m\ge2,\quad N\ge2.
\]
Write
\[
E=\#\{j:C_j=0\},\qquad K=m-E,
\]
and let Pearson's goodness-of-fit statistic for equiprobability be
\[
X^2=\sum_{j=1}^m\frac{(C_j-N/m)^2}{N/m}.
\]
For every feasible
\[
1\le k\le\min(m,N),
\]
write \(S(r,k)\) for a Stirling number of the second kind and define
\[
a_{N,k}=\frac{S(N-1,k)}{S(N,k)},
\qquad
b_{N,k}=\frac{S(N-2,k)}{S(N,k)}.
\]
Then
\[
\boxed{
\mathbb E[X^2\mid K=k]
=
m-N+m(N-1)a_{N,k}
}
\]
and
\[
\boxed{
\operatorname{Var}(X^2\mid K=k)
=
\frac{4m^2}{N^2}
\left[
\binom N2 a_{N,k}(1-a_{N,k})
+
\binom N2\left(\binom N2-1\right)
\left(b_{N,k}-a_{N,k}^2\right)
\right].
}
\]
Since \(E=m-K\), the same formulas are the exact first two Pearson moments conditional on the observed number of empty cells.

## Assumptions and scope
The null distribution is the equiprobable \(m\)-cell multinomial with a fixed sample size \(N\). The empty cells are sampling zeros, not structural zeros. The conditioning event is feasible exactly when \(1\le k\le\min(m,N)\).

The result is finite-sample and exact. It does not claim the same formulas for unequal null probabilities, estimated cell probabilities, contingency tables with fixed margins, or structural zeros.

## Proof
Condition on \(K=k\). First choose the \(k\) occupied cells. Conditional on that chosen set and on every chosen cell being nonempty, the \(N\) labeled observations are uniformly distributed over all surjections onto the \(k\) occupied labels. Their number is
\[
k!\,S(N,k).
\]

Let
\[
U=\sum_{1\le r<s\le N}
\mathbf 1\{\text{observations }r\text{ and }s\text{ fall in the same cell}\}.
\]
Because
\[
\sum_{j=1}^m C_j^2=N+2U,
\]
Pearson's statistic satisfies
\[
X^2=m-N+\frac{2m}{N}U.
\]

For one fixed unordered pair of observations, requiring the pair to occupy the same cell is equivalent to merging the pair into one super-observation. Surjections of the resulting \(N-1\) labeled units onto the same \(k\) labels are counted by
\[
k!\,S(N-1,k).
\]
Therefore
\[
\Pr(\text{a fixed pair collides}\mid K=k)
=
a_{N,k}.
\]
With \(M=\binom N2\),
\[
\mathbb E[U\mid K=k]=M a_{N,k}.
\]
Substituting into the affine representation of \(X^2\) gives
\[
\mathbb E[X^2\mid K=k]
=
m-N+m(N-1)a_{N,k}.
\]

For two distinct unordered pairs, imposing both collision events always creates exactly two identifications. If the pairs overlap, three observations are merged into one unit; if they are disjoint, each pair is merged separately. In either case the number of resulting labeled units is \(N-2\), and the number of compatible surjections is
\[
k!\,S(N-2,k).
\]
Thus for any two distinct pair indicators,
\[
\Pr(\text{both collide}\mid K=k)=b_{N,k}.
\]
Consequently
\[
\operatorname{Var}(U\mid K=k)
=
M a_{N,k}(1-a_{N,k})
+
M(M-1)(b_{N,k}-a_{N,k}^2).
\]
Multiplication by the squared affine coefficient
\[
\left(\frac{2m}{N}\right)^2
\]
proves the conditional variance formula.

## Verification
The accompanying `checker.py` performs exact rational verification over every count vector for all \(2\le m\le6\) and \(2\le N\le7\). For each feasible value of \(K\), it computes the exact multinomial conditional mean and variance of \(X^2\) and compares them with the two Stirling-number formulas.

The checker also verifies the pair-collision derivation directly through the same exact conditional distributions. These finite checks are supplementary; the proof above establishes the formulas for every admissible \(m,N,k\).

## Relationship to prior work
Finkler's work on sparse contingency tables explicitly introduces the random number of zero cells and proposes corrections to Pearson's statistic based on that observed number. The complete inspected preprint does not state conditional first or second moments of Pearson's statistic given the zero-cell count.

Filina and Zubkov give an exact finite algorithm for the unconditional distribution of Pearson's statistic in multinomial schemes, including the equiprobable case. Their complete inspected article does not condition on empty or occupied cell counts.

Earlier exact-distribution work of Good, Gover, and Mitchell is a plausible historical source for stronger coverage of the equiprobable Pearson statistic, but only bibliographic and title-level material was available in the searches used here. This remains a literature risk.

A previously checked occupancy result gives unconditional covariances between the total number of occupied cells and individual occupancy-count classes. Those unconditional covariances do not determine the conditional first two moments of Pearson's statistic given the total number of occupied cells.

## Limitations
The identity relies on equal cell probabilities. The corresponding unequal-probability conditioning law is weighted rather than uniform over surjections and does not reduce to the same Stirling ratios.

The literature comparison cannot exclude an unindexed historical statement of the same conditional moments. In particular, the complete text of the 1970 exact-distribution paper by Good, Gover, and Mitchell was not available for direct inspection.

## References
1. A. Finkler, “Goodness of fit statistics for sparse contingency tables,” arXiv:1006.2287, first submitted 11 June 2010.
2. M. V. Filina and A. M. Zubkov, “Exact Computation of Pearson Statistics Distribution and Some Experimental Results,” *Austrian Journal of Statistics* 37 (2008), 129–135. DOI: 10.17713/ajs.v37i1.294.
3. I. J. Good, T. N. Gover, and G. J. Mitchell, “Exact Distributions for \(\chi^2\) and for the Likelihood-Ratio Statistic for the Equiprobable Multinomial Distribution,” *Journal of the American Statistical Association* 65 (1970), 267–283. DOI: 10.1080/01621459.1970.10481078.
