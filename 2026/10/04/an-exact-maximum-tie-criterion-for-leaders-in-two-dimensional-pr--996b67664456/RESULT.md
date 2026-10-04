# An exact maximum-tie criterion for leaders in two-dimensional product samples
## Finding
Let \( (X_i,Y_i)_{1\le i\le n} \) be i.i.d. from an arbitrary product probability law \(F_X\otimes F_Y\) on \(\mathbb R^2\). Define the marginal maximizing-index sets
\[
I_{X,n}=\{i:X_i=\max_{1\le j\le n}X_j\},\qquad
I_{Y,n}=\{i:Y_i=\max_{1\le j\le n}Y_j\}.
\]
and their sizes \(K_{X,n}=|I_{X,n}|\) and \(K_{Y,n}=|I_{Y,n}|\). Let \(a_n\) be the probability that the sample contains a leader, meaning an observed vector that is coordinatewise at least every other observed vector.

Then for every integer \(n\ge1\),
\[
a_n=\mathbb E\left[1-\frac{\binom{n-K_{X,n}}{K_{Y,n}}}{\binom n{K_{Y,n}}}\right],
\]
where \(\binom{n-k}l=0\) when \(l>n-k\). If
\[
R_n=\frac{K_{X,n}K_{Y,n}}n,
\]
then
\[
\mathbb E\left[1-e^{-R_n}\right]\le a_n\le \mathbb E[\min(1,R_n)].
\]
In particular,
\[
a_n\longrightarrow0\quad\Longleftrightarrow\quad R_n\longrightarrow0\text{ in probability}.
\]
The leader property \(\liminf_{n\to\infty}a_n>0\) is therefore equivalent to the existence of \(\varepsilon,\delta>0\) and \(N\) such that
\[
\Pr\!\left(K_{X,n}K_{Y,n}\ge\varepsilon n\right)\ge\delta
\]
for every \(n\ge N\).

## Assumptions and scope
No continuity, discreteness, moment, support, or tail assumption is imposed on either marginal. The only structural assumption is independence of the two coordinates, so that the whole \(X\)-sample is independent of the whole \(Y\)-sample. Ties are allowed and are exactly what the variables \(K_{X,n}\) and \(K_{Y,n}\) measure.

The statement is two-dimensional. It characterizes the product-law leader event through one-dimensional sample-maximum multiplicities; it does not resolve whether two infinite-support marginals must always satisfy \(a_n\to0\).

## Proof
A sampled vector is a leader exactly when its index belongs to both marginal maximizing-index sets. Hence
\[
\{\text{a leader exists}\}=\{I_{X,n}\cap I_{Y,n}\ne\varnothing\}.
\]
Because the observations within each marginal sample are exchangeable, conditional on \(K_{X,n}=k\), the set \(I_{X,n}\) is uniform over the \(k\)-subsets of \(\{1,\ldots,n\}\). Likewise, conditional on \(K_{Y,n}=l\), the set \(I_{Y,n}\) is uniform over the \(l\)-subsets. Independence of the coordinate samples makes these two random subsets conditionally independent. Therefore
\[
\Pr(I_{X,n}\cap I_{Y,n}=\varnothing\mid K_{X,n}=k,K_{Y,n}=l)
=\frac{\binom{n-k}l}{\binom nl},
\]
with the ratio equal to zero when \(l>n-k\). Averaging proves the exact formula.

For fixed \(k,l\), let \(H_{n}(k,l)\) be the conditional probability that the two maximizing-index sets intersect. The expected size of their intersection is \(kl/n\), so Markov's inequality for the nonnegative integer intersection size gives
\[
H_n(k,l)\le\min\left(1,\frac{kl}n\right).
\]
For the lower bound, when \(l\le n-k\),
\[
1-H_n(k,l)
=\prod_{j=0}^{l-1}\left(1-\frac{k}{n-j}\right)
\le\left(1-\frac kn\right)^l
\le e^{-kl/n}.
\]
If \(l>n-k\), then \(H_n(k,l)=1\), so the same lower bound remains valid. Averaging the two pointwise bounds gives the displayed expectation inequalities.

Now suppose \(R_n\to0\) in probability. Since \(0\le\min(1,R_n)\le1\), bounded convergence in probability implies \(\mathbb E[\min(1,R_n)]\to0\), hence \(a_n\to0\). Conversely, if \(a_n\to0\), then the lower bound yields \(\mathbb E[1-e^{-R_n}]\to0\). For each \(\varepsilon>0\),
\[
\Pr(R_n\ge\varepsilon)
\le\frac{\mathbb E[1-e^{-R_n}]}{1-e^{-\varepsilon}}
\longrightarrow0,
\]
so \(R_n\to0\) in probability.

For the leader-property equivalence, one direction follows immediately from the lower bound: if \(\Pr(R_n\ge\varepsilon)\ge\delta\) eventually, then \(a_n\ge\delta(1-e^{-\varepsilon})\) eventually. Conversely, if \(c=\liminf_n a_n>0\), then for all sufficiently large \(n\), \(\mathbb E[\min(1,R_n)]\ge c/2\). Taking \(\varepsilon=c/4\) and using \(\min(1,R_n)\le\varepsilon+\mathbf 1_{\{R_n>\varepsilon\}}\) gives \(\Pr(R_n>\varepsilon)\ge c/4\) eventually.

## Verification
The proof is analytic. A standalone checker exhausts all subset-size pairs for small \(n\), verifies the hypergeometric intersection formula by direct subset enumeration, and verifies the exact rational inequalities
\[
1-\frac{\binom{n-k}l}{\binom nl}
\le\min\left(1,\frac{kl}n\right)
\]
and
\[
1-\frac{\binom{n-k}l}{\binom nl}
\ge1-\left(1-\frac kn\right)^l
\]
over a larger finite range. These computations are stress tests only; the proof above establishes the result for every \(n\).

Two consistency checks are immediate. If both marginals are continuous, then \(K_{X,n}=K_{Y,n}=1\) almost surely and the formula gives \(a_n=1/n\), agreeing with the known continuous-product case. If one conditional multiplicity is \(l=1\), then the conditional leader probability is exactly \(k/n\).

## Relationship to prior work
Răducan, Rădulescu, Rădulescu, and Zbăganu introduced the leader probability \(a_n\), established several sufficient conditions for product distributions, proved \(a_n=1/n\) for two continuous independent coordinates, and asked for a computable criterion for the leader property. Their discrete product analysis bounds the leader event through distribution-function and maximum comparisons; the inspected full text does not state the maximizing-index-set intersection formula, the two-sided multiplicity bounds, or the resulting necessary-and-sufficient criterion above.

A later paper by Răducan and Zbăganu studies quasi-unidimensional vectors of the form \(f(X)\). Its inspected introduction and conclusions continue the leader-property program in that dependent-coordinate setting and do not cover the independent-coordinate product criterion proved here.

The present result does not settle the 2022 conjecture that two independent infinite-support marginals cannot have the leader property. Instead it identifies exactly what that conjecture requires at the sample level: the normalized product \(K_{X,n}K_{Y,n}/n\) must converge to zero in probability.

## Limitations
The theorem is restricted to two independent coordinates. It gives a complete reduction to the random multiplicities \(K_{X,n}\) and \(K_{Y,n}\), but it does not itself classify which one-dimensional distributions make their product sublinear in probability. Thus the infinite-support conjecture remains open unless one separately controls those multiplicities.

A terminology-based literature risk remains: an equivalent common-maximizer or random-subset-intersection criterion could exist outside the small leader-property literature under different language. Targeted searches for leader probability, maximizing-index intersections, maximum multiplicity, and hypergeometric formulations did not locate such a statement.

## References
1. A. M. Răducan, C. Z. Rădulescu, M. Rădulescu, and G. Zbăganu, “On the Probability of Finding Extremes in a Random Set,” *Mathematics* 10 (2022), 1623. DOI: 10.3390/math10101623. Published 10 May 2022.
2. A. M. Răducan and G. Zbăganu, “The Leader Property in Quasi Unidimensional Cases,” *Mathematics* 10 (2022), 4199. DOI: 10.3390/math10224199. Published 9 November 2022.
