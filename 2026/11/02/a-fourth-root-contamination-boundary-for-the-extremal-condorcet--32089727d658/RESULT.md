# A fourth-root contamination boundary for the extremal Condorcet culture

## Finding

For every integer \(n\ge3\), let \(R_n\) be the uniform law on the \(n\) cyclic rotations of the ranking \((0,1,\ldots,n-1)\), and let \(U_n\) be the uniform law on all \(n!\) strict rankings. Three voters independently sample from the same mixture \(M_{n,\varepsilon}=(1-\varepsilon)R_n+\varepsilon U_n\), where \(0\le\varepsilon\le1\). Write \(P_n(\varepsilon)\) for the probability that the resulting pairwise-majority relation has a Condorcet winner, and \(H_n=\sum_{j=1}^{n}1/j\).

Define
\[
 A_n=\frac{3n-2}{n^2},\qquad
 B_n=\frac{2H_n-1}{n},\qquad
 Q_n=\Pr(\text{a Condorcet winner for three independent }U_n\text{ rankings}).
\]
Then the following is an **exact finite-size law**:
\[
 \boxed{P_n(\varepsilon)=(1-\varepsilon)^3 A_n
 +3\varepsilon(1-\varepsilon)^2 B_n
 +\varepsilon^2(3-2\varepsilon)Q_n.}
\tag{1}
\]
The impartial-culture term is itself an exact finite combinatorial sum. With \(N=n-1\),
\[
 Q_n=\frac1{n^2}\!\sum_{\substack{r,s,t\ge0\\r+s+t\le N}}
 \frac{\binom{N-r}{s}}{\binom Ns}
 \frac{\binom{N-r-s}{t}}{\binom Nt}.
\tag{2}
\]
In particular, \(P_n'(0)=3(2H_n-4+2/n)/n>0\) for every \(n\ge3\). The law \(M_{n,\varepsilon}\) has full support on all rankings whenever \(\varepsilon>0\).

Writing \(c=\pi^{3/2}/2\), the known impartial-culture asymptotic \(Q_n\sim c/\sqrt n\) implies a **sharp contamination crossover**: for every fixed \(t\ge0\),
\[
 \boxed{\lim_{n\to\infty}nP_n(tn^{-1/4})=3+3ct^2
 =3+\frac{3\pi^{3/2}}2t^2.}
\tag{3}
\]
For arbitrary \(\varepsilon_n\to0\), the two regimes are
\[
 \varepsilon_n n^{1/4}\to0\implies nP_n(\varepsilon_n)\to3,
 \qquad
 \varepsilon_n n^{1/4}\to\infty\implies
 P_n(\varepsilon_n)\sim\frac{3c\varepsilon_n^2}{\sqrt n}.
\tag{4}
\]
The new conditional ingredient is the harmonic identity \(B_n=(2H_n-1)/n\): one completely impartial voter restores a Condorcet winner with probability of order \((\log n)/n\) when the other two voters use independently selected cyclic rankings, whereas two impartial voters give the much larger \(n^{-1/2}\) scale.

## Assumptions and scope

There are exactly three voters and \(n\ge3\) labeled alternatives. Rankings are strict, independently sampled across voters, and every voter has the **same** stated law. A Condorcet winner beats each other alternative by at least two of the three pairwise votes. There can be at most one winner. The contamination parameter \(\varepsilon\) is a probability of replacing an entire cyclic ranking by an independent uniform ranking, not of independently flipping pairwise comparisons. Limits in (3) and (4) concern the number of alternatives growing while the voter count stays three. In (3), \(tn^{-1/4}\le1\) for all sufficiently large \(n\).

## Proof

**1. The all-cyclic stratum.** A triple of cyclic rankings has a Condorcet winner exactly when at least two rotations coincide. To see necessity, compare each alternative with its immediate predecessor around the cycle: that alternative is preferred to its predecessor only by the rotation that starts at it. Thus a winner requires at least two voters to choose that rotation. Conversely, two voters with the same top alternative make it the Condorcet winner. The collision probability is
\[
 A_n=3\frac1n\left(1-\frac1n\right)+\frac1{n^2}
 =\frac{3n-2}{n^2}.
\]
This is also the three-voter special case of Sauermann's extremal-culture formula.

**2. Exactly one impartial voter.** By cyclic relabeling, fix the first cyclic ballot to be \((0,1,\ldots,n-1)\). The second cyclic ballot is its rotation by a uniform offset \(j\in\{0,\ldots,n-1\}\). For \(j=0\), the two ballots coincide and a Condorcet winner exists regardless of the third ballot. If \(1\le j\le n-1\), the two ballots agree on the rankings *within* blocks \(A=(0,\ldots,j-1)\) and \(B=(j,\ldots,n-1)\), but disagree on every comparison *between* blocks. The only possible winners are the respective block leaders \(0\) and \(j\): any other alternative is unanimously beaten by an earlier alternative in its own block.

The candidate \(0\) wins precisely when the impartial ballot places \(0\) ahead of all \(n-j\) members of \(B\); this has probability \(1/(n-j+1)\). Likewise \(j\) wins with probability \(1/(j+1)\). These events are disjoint because they impose opposite ordering of \(0\) and \(j\). Averaging the offset gives
\[
 B_n=\frac1n\left[1+\sum_{j=1}^{n-1}
 \left(\frac1{n-j+1}+\frac1{j+1}\right)\right]
 =\frac{2H_n-1}{n}.
\tag{5}
\]
This count is exact for every integer \(n\ge2\).

**3. At least two impartial voters.** Conditional on a fixed third ranking, two iid uniform rankings have a distribution invariant under any relabeling of alternatives. Every fixed ranking is the relabeling of the identity, so the conditional winner probability is the same as when all three rankings are uniform, namely \(Q_n\). Hence both the two-impartial and three-impartial strata contribute \(Q_n\).

To establish (2) directly, fix one alternative and let \(r,s,t\) be the numbers of alternatives ranked above it by the three independent impartial voters. Each of these counts is independently uniform on \(\{0,\ldots,N\}\). Given their sizes, the sets of higher-ranked alternatives are independent uniform subsets of an \(N\)-element set. The fixed candidate wins if and only if those three subsets are pairwise disjoint. This requires \(r+s+t\le N\), and its conditional probability is
\[
 \frac{\binom{N-r}s}{\binom Ns}
 \frac{\binom{N-r-s}t}{\binom Nt}.
\]
Summing over sizes, multiplying by \(n\) candidates, and using their mutually exclusive winner events proves (2).

**4. Conditioning on contamination.** The number of impartial ballots is binomial with parameters \((3,\varepsilon)\). Its probabilities for zero, one, two, and three impartial ballots are respectively \((1-\varepsilon)^3\), \(3\varepsilon(1-\varepsilon)^2\), \(3\varepsilon^2(1-\varepsilon)\), and \(\varepsilon^3\). Substituting the exact conditional probabilities from steps 1–3 and combining the last two terms gives (1).

The directional derivative at zero is \(3(B_n-A_n)\). It is positive because \(2H_n-4+2/n=1/3\) at \(n=3\) and its increment from \(n\) to \(n+1\) equals \(2(n-1)/(n(n+1))>0\).

**5. The fourth-root boundary.** The three-voter impartial-culture theorem of May (1971), also in Sauermann (2022, Theorem 1), states \(Q_n=(c+o(1))n^{-1/2}\) with \(c=\pi^{3/2}/2\). Independently, (5) gives \(B_n=(2\log n+O(1))/n\), while \(A_n=3/n+O(n^{-2})\). Substituting \(\varepsilon_n=tn^{-1/4}\) in (1) yields (3): the one-impartial term is only \(O(n^{-5/4}\log n)\), while the two-impartial term contributes \(3ct^2/n+o(n^{-1})\). The same estimates prove both implications in (4), including the negligibility of the one-impartial term in the second regime.

## Verification

The standalone Python 3 standard-library script `verify.py` calculates the exact three conditional strata by independently enumerating rankings for every \(2\le n\le6\); it compares these counts to (2) and (5) as exact rational numbers. It additionally enumerates **all** ordered three-voter profiles with mixture weights for \(n=2,3,4\) at \(\varepsilon\in\{0,1/4,1/2,1\}\), checking (1) directly rather than only by conditioning. It checks the derivative-sign inequality for all \(3\le n\le100\). Its output reports 125 exact identity/inequality checks passing. These finite computations are sanity checks; the proof for arbitrary \(n\) and the asymptotic limit are the arguments above.

For reference, the exact triple of conditional probabilities \((A_n,B_n,Q_n)\) at \(n=3,4,5,6\) is respectively \((7/9,8/9,17/18)\), \((5/8,19/24,8/9)\), \((13/25,107/150,21/25)\), and \((4/9,13/20,359/450)\).

## Relationship to prior work

Sauermann (2022, arXiv:2203.13713, Theorems 1 and 2 and Proposition 9) proves the impartial-culture asymptotic and exact minimum attained by the cyclic-rotation culture. The constant \(c\) at three voters was earlier derived by May (1971). Those endpoint results are **prior**, not new claims here. The present result computes the previously unaccounted conditional two-cyclic/one-impartial stratum (5), the complete interpolation (1), and the asymptotically sharp contamination boundary (3)–(4).

Pittel (2025, arXiv:2506.20613) analyzes impartial cultures with a number of voters tending to infinity and considerably larger than the number of candidates; it does not address three fixed voters or mixtures with the cyclic extremizer. Classical general-culture enumeration by Garman and Kamien (1968) permits brute-force probabilities for fixed finite systems, but its documented general framework does not state the harmonic simplification or the growing-number-of-alternatives contamination boundary. Such broad summation frameworks do not alone supply uniform asymptotics. Other finite-voter/candidate tables may imply particular entries of the verification table without covering the variable-\(n\) theorem. No historical-priority guarantee is asserted.

## Limitations

The result concerns exactly three voters, iid identical mixtures of the particular extremal cyclic culture with full impartial rankings, and no ties. It does not characterize all near-minimizing cultures, prove universal stability, or treat more voters or other perturbation mechanisms. The \(n^{-1/4}\) scale is specific to this mixture and these asymptotic regimes. The impartial-culture asymptotic uses a published theorem; it is not independently reproved here. Historical-priority comparison is based on accessible material, and some older publisher full texts were not available for complete examination. Independent validation has not been performed.

## References

1. L. Sauermann, *On the probability of a Condorcet winner among a large number of alternatives*, arXiv:2203.13713, first publicly submitted 2022-03-25. https://arxiv.org/abs/2203.13713
2. R. M. May, *Some mathematical remarks on the paradox of voting*, Behavioral Science 16 (1971), 143–151. https://doi.org/10.1002/bs.3830160204
3. M. B. Garman and M. I. Kamien, *The paradox of voting: Probability calculations*, Behavioral Science 13 (1968), 306–316. https://doi.org/10.1002/bs.3830130405
4. B. Pittel, *On likelihood of a Condorcet winner for uniformly random and independent voter preferences*, arXiv:2506.20613, 2025. https://arxiv.org/abs/2506.20613
