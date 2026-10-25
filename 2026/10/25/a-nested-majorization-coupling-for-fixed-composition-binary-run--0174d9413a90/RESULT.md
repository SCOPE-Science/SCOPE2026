# A nested majorization coupling for fixed-composition binary-run lengths

## Finding

Fix positive integers \(a,b\), and draw uniformly a binary word with exactly \(a\) ones and \(b\) zeros. Write \(R\) for its number of maximal constant runs. Let \(\Lambda^{(r)}\) be the decreasing list of all run lengths conditional on \(R=r\), padded by zeros to length \(a+b\). Every integer
\[
2\le r\le r_{\max}=2\min(a,b)+\mathbf{1}_{\{a\ne b\}}
\]
is attainable. **All these conditional laws admit one coupling satisfying**
\[
\Lambda^{(2)}\succeq\Lambda^{(3)}\succeq\cdots\succeq\Lambda^{(r_{\max})}
\quad\text{almost surely},
\]
where \(\succeq\) is vector majorization. More precisely, each step is obtained by splitting exactly one positive run length into two positive integer lengths, with all other lengths unchanged. The positive run lengths of each color can simultaneously be coupled by refinement.

Consequently, for every convex \(\phi:[0,\infty)\to\mathbb R\) with \(\phi(0)=0\),
\[
\mathbb E\left[\sum_{j=1}^{R}\phi(\ell_j)\mid R=r+1\right]
\le \mathbb E\left[\sum_{j=1}^{R}\phi(\ell_j)\mid R=r\right],
\]
and the longest run, including each color's longest run separately, decreases in first-order stochastic order as the conditioned total run count increases. For the quadratic clustering statistic \(Q=\sum_j\ell_j^2\), the coupling gives the **strict, sharp one-step bound**
\[
\mathbb E[Q\mid R=r]-\mathbb E[Q\mid R=r+1]\ge2.
\]
The constant \(2\) is attained for \((a,b)=(1,2)\).

There is also an exact closed form. Set
\[
F(x,t)=\frac{x(2x-t+1)}{t+1}.
\]
At even attainable run counts,
\[
\mathbb E[Q\mid R=2t]=F(a,t)+F(b,t).
\]
At odd attainable run counts (so \(a+b>2t\)),
\[
\mathbb E[Q\mid R=2t+1]
=\frac{(a-t)\bigl(F(a,t+1)+F(b,t)\bigr)
 +(b-t)\bigl(F(a,t)+F(b,t+1)\bigr)}{a+b-2t}.
\]
Terms with zero prefactors correspond to impossible orientations and are interpreted as absent, not as an evaluation of an invalid composition.

## Assumptions and scope

The model is the conditional uniform two-sample rank-label null: all \(\binom{a+b}{a}\) fixed-content binary words are equiprobable. No iid Bernoulli assumption without conditioning on the numbers of the two labels is asserted. Each run is a maximal consecutive block of one symbol; its length is a strictly positive integer. An increasing cut set for the \(a\) occurrences of one symbol determines an ordered positive composition of \(a\), and similarly for the \(b\) occurrences of the other symbol.

For vectors \(x,y\in[0,\infty)^{a+b}\) with equal sums, \(x\succeq y\) means that the sum of the \(k\) largest coordinates of \(x\) is at least that of \(y\) for every \(1\le k<a+b\). The coupling is a coupling of run-length multisets and two color-specific ordered compositions. It is not an embedding of the original binary words as subsequences.

## Proof

**1. Conditional composition law.** For \(R=2t\), each color has exactly \(t\) runs and either symbol may start. There are
\[
2\binom{a-1}{t-1}\binom{b-1}{t-1}
\]
such words. Each of the two orientations occurs with probability \(1/2\), and conditional on either orientation, the two ordered run-length compositions are independent and uniform among positive compositions into \(t\) parts.

For \(R=2t+1\), the first and last symbols agree. The numbers of words with \(t+1\) one-runs and \(t\) zero-runs, or conversely, are respectively
\[
A_t=\binom{a-1}{t}\binom{b-1}{t-1},\qquad
B_t=\binom{a-1}{t-1}\binom{b-1}{t}.
\]
On the feasible range, Pascal-binomial ratios give
\[
\frac{A_t}{A_t+B_t}=\frac{a-t}{a+b-2t},\qquad
\frac{B_t}{A_t+B_t}=\frac{b-t}{a+b-2t}.
\]
Conditional on either orientation, each color composition is again independently uniform for its indicated number of parts. The formulas remain valid when a numerator is zero, by omitting the corresponding impossible orientation.

**2. Simultaneous cut-growth construction.** Regard the \(a-1\) potential internal cuts of the first color and the \(b-1\) potential internal cuts of the second as two disjoint finite sets. Start with neither set cut: this yields \(R=2\), with a fresh fair choice of starting color. Suppose the current total number of runs is \(2t\), so each color has \(t\) parts. Add one cut chosen uniformly from the \((a-t)+(b-t)\) unused cuts in both sets. The extra cut is of the first color with probability \((a-t)/(a+b-2t)\), exactly the preceding odd-run orientation weight. Conditional on which color was chosen, the enlarged cut set is a uniform subset of the required size, by counting its possible deleted cuts. Thus the resulting two compositions have precisely the law conditional on \(R=2t+1\); the starting color is the one with \(t+1\) runs.

Suppose instead the current total number of runs is \(2t+1\). One color has \(t+1\) runs and the other \(t\). Whenever another attainable level exists, add a uniformly chosen unused cut **in the latter color only**. A uniform subset of size \(t-1\) augmented by an independent uniformly chosen unused element is uniform of size \(t\): each final subset has exactly \(t\) predecessors. Consequently both color cut sets become independent uniform \(t\)-subsets of their respective internal boundaries, regardless of the previous orientation. Choose the starting color fairly. This is exactly the conditional \(R=2t+2\) law. Induction constructs all attainable levels on one probability space.

**3. Majorization and strictness.** At every step just one unused internal boundary is inserted, so exactly one positive run length \(u+v\) is replaced by two positive run lengths \(u,v\). Sorting and zero-padding preserves the elementary majorization relation
\[
(u+v,0)\succeq(u,v).
\]
All other coordinates remain unchanged. Transitivity establishes the full nested coupling, with the corresponding refinement relation holding separately for both colors.

For convex \(\phi\) with \(\phi(0)=0\), convexity implies \(\phi(u)+\phi(v)\le\phi(u+v)\); hence the displayed expected inequality follows pathwise. Choosing a threshold indicator of the largest coordinate gives stochastic monotonicity of the longest overall run and each color's longest run. Finally, the quadratic statistic decreases at a split by
\[
(u+v)^2-u^2-v^2=2uv\ge2.
\]
For \((a,b)=(1,2)\), the only possible transition is from a run of length two to two singleton runs, and equality \(2\) holds.

**4. Quadratic expectation.** In a uniformly chosen ordered positive \(t\)-composition \((X_1,\ldots,X_t)\) of an integer \(x\ge t\), ordinary generating functions yield
\[
\sum_{\substack{X_1+\cdots+X_t=x\\X_i\ge1}}\sum_i X_i(X_i-1)
=[z^x]\frac{2t z^{t+1}}{(1-z)^{t+2}}
=2t\binom{x}{t+1}.
\]
Divide by the number \(\binom{x-1}{t-1}\) of such compositions and add \(\sum_iX_i=x\) to obtain
\[
\mathbb E\sum_i X_i^2=x+\frac{2x(x-t)}{t+1}=F(x,t).
\]
The even and odd conditional-composition laws in Step 1 now yield both exact formulas in the finding, completing the proof for every admissible pair of positive integers.

## Verification

The standalone `verify_runs.py` independently enumerates all \(\binom{a+b}{a}\) fixed-content words for each of the \(49\) pairs \(1\le a,b\le7\). For every feasible run count, it checks the exact rational conditional mean of \(Q\); for every adjacent pair of run counts and every integer longest-run threshold it checks the stochastic tail inequality and strict quadratic decrease. Separately it enumerates the entire cut-growth transition kernel using exact rational probabilities and verifies that every induced cut-set state has the required conditional distribution. Execute `python verify_runs.py` with standard Python; no libraries beyond the standard library are required.

For example, when \((a,b)=(3,5)\), the exact sequence of conditional means of \(Q\) at run counts \(2,3,4,5,6,7\) is
\[
34,\quad26,\quad20,\quad\frac{63}{4},\quad13,\quad10.
\]
These finite checks are corroboration, not substitutes for the argument of Steps 1–4.

## Relationship to prior work

Kazemi and Jafari (2014) provide the elementary distribution of the **numbers** of runs of each color in a fixed-content two-sample sequence, with positive-composition factors matching Step 1. Their paper concerns order statistics of run **counts**, not majorization of run **lengths** across conditioning levels. Lou (1996) and Kong (2006) developed exact computational or generating-function methods for runs and longest runs; their full texts were not accessible during this comparison, so no negative whole-document claim is made about them.

Wentzel-Larsen and Anhøj (2019), with its subsequent `crossrun` implementation, give exact joint finite-sample distributions of crossing counts (one less than total run count) and the longest run, including the fixed-content setting. Their tables can evaluate particular conditional longest-run tails, but an exact finite table does not itself provide a coupled, all-sample-size majorization statement for the **entire run-length vector**. Kong's article on ordered longest runs (published 2017; freely available as arXiv:2405.01747) provides broad exact distributional formulas for run-length order statistics. Its statements do not present a refinement coupling over successive conditioned total run counts. Thus the claim is a structural comparison of conditional laws, rather than a new way to tabulate one already-known marginal distribution.

## Limitations

The comparison assumes two symbols, fixed positive content, and the uniform permutation null. It concerns unordered multisets of run lengths (with optional retention of each color's ordered lengths), not prefix locations, Kolmogorov–Smirnov-type path statistics, dependent labels, or changing symbol counts. It does not claim that every statistic associated with the binary word decreases as the number of runs increases. A cut-growth coupling is constructed, but not a stationary Markov chain whose levels have independent increments. Priority remains subject to independent examination of some inaccessible earlier full texts. No independent audit has been performed.

## References

1. M. R. Kazemi and A. A. Jafari, *Characterization of Order Statistics in Two Runs Using Conditional Expectation*, arXiv:1410.8167v1 (first public arXiv posting: 2014-10-29), https://arxiv.org/abs/1410.8167.
2. W. Y. W. Lou, *On Runs and Longest Run Tests: A Method of Finite Markov Chain Imbedding*, Journal of the American Statistical Association 91 (1996), 1595–1601, https://doi.org/10.1080/01621459.1996.10476727.
3. Y. Kong, *Distribution of Runs and Longest Runs: A New Generating Function Approach*, Journal of the American Statistical Association 101 (2006), 1253–1263, https://doi.org/10.1198/016214505000001401.
4. T. Wentzel-Larsen and J. Anhøj, *Joint distribution for number of crossings and longest run in independent Bernoulli observations*, PLOS ONE 14 (2019), e0223233, https://doi.org/10.1371/journal.pone.0223233.
5. Y. Kong, *The \(m\)-th longest runs of multivariate random sequences*, Annals of the Institute of Statistical Mathematics 69 (2017), 497–512, https://doi.org/10.1007/s10463-015-0551-8; available text https://arxiv.org/abs/2405.01747.
