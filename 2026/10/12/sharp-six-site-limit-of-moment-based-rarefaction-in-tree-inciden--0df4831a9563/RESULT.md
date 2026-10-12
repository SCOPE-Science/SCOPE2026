# Sharp six-site limit of moment-based rarefaction in tree-incidence communities

## Finding

**Theorem (tree-incidence rarefaction and its first moment-indistinguishable networks).** Fix an integer \(n\ge4\). Consider \(n\) habitat sites and \(n-1\) distinct species such that each species occupies exactly two distinct sites, no pair of sites supports more than one species, and the graph joining sites that share a species is a tree \(T\). Choose a uniformly random subset of exactly \(k\) sites without replacement, for any \(0\le k\le n\). Let \(R_k(T)\) be the number of species recorded at least once. Put \(h=n-k\), \(m=n-1\), and

\[
 p_j=\begin{cases}\displaystyle\frac{\binom{n-j}{h-j}}{\binom n h},&h\ge j,\\[3pt]0,&h<j,\end{cases}\qquad j\in\{2,3,4\},
\]

and write \(W(T)=\sum_{v\in V(T)}\binom{d_T(v)}{2}\), the number of unordered adjacent pairs of tree edges. Then

\[
 \mathbb E[R_k(T)]=m(1-p_2),
 \quad
 \operatorname{Var}(R_k(T))
 =mp_2+m(m-1)p_4+2W(T)(p_3-p_4)-m^2p_2^2.
\]

Consequently, two \(n\)-site tree-incidence communities have **identical mean and variance curves for every sample size** if and only if their values of \(W\) agree. For each \(1\le k\le n-3\), the path uniquely minimizes and the star uniquely maximizes rarefaction variance among \(n\)-site trees, up to site relabeling. The maximal-minus-minimal variance is exactly

\[
 (n-2)(n-3)(p_3-p_4)>0.
\]

The order \(n=6\) is the **smallest** at which two nonisomorphic tree-incidence communities have identical mean and variance curves at every sample size but different full richness distributions. Such a pair exists at **every** \(n\ge6\).

## Assumptions and scope

The incidence object is a finite, unweighted, binary species-by-site matrix. Every row has exactly two ones, all rows are distinct, all columns are nonempty, and its site-projection graph is a simple connected acyclic graph; there are exactly \(n-1\) species. Sampling is uniform among all \(\binom nk\) site subsets, conditional on the observed incidence matrix; sites are not sampled independently, and no stochastic model for the incidence matrix itself is assumed. \(R_k\) counts species occurring in at least one of the selected sites. Variances in the theorem are **conditional sample-order variances**, not sampling variances of a fitted richness estimator.

The graph isomorphism convention allows relabeling habitat sites and hence the incident species. The two equality claims are unique under this convention. Primary application and classification: mathematical ecology, MSC2020 92D40; graph identities are used as proof techniques.

## Proof

**1. Indicator reduction and moment identities.** Let \(U\) denote the set of unselected sites, of size \(h\). A species corresponding to edge \(e=uv\) is missing precisely when \(u,v\in U\). Let \(I_e\) be this event's indicator and \(X=\sum_{e\in E(T)}I_e\). Then \(R_k=m-X\). Every \(I_e\) has mean \(p_2\). For two distinct edges \(e,f\), the two indicators have joint mean \(p_3\) if the edges share a site and \(p_4\) otherwise. There are precisely \(W(T)\) adjacent unordered pairs of edges and \(\binom m2-W(T)\) disjoint pairs. Thus

\[
 \mathbb E[X^2]=mp_2+2W(T)p_3+2\bigl(\binom m2-W(T)\bigr)p_4,
\]

and subtracting \((mp_2)^2\) proves both formulas. The identity is valid also for the degenerate sample sizes because the convention \(p_j=0\) when \(h<j\) makes every indicator probability correct.

**2. Which sample sizes detect the wedge count.** For \(n\ge4\), the difference \(p_3-p_4\) is the probability that three specified sites are unselected while a fourth specified site is selected. It is strictly positive if and only if \(1\le k\le n-3\). For other \(k\), the variance is independent of \(W\). In particular, \(k=1\) alone determines \(W\), as

\[
 \operatorname{Var}(R_1)=\frac{2m+2W}{n}-\left(\frac{2m}{n}\right)^2,
\]

because \(R_1\) is the degree of the uniformly selected site. Together with the first formula this proves the if-and-only-if statement about all first-two-moment curves.

**3. Sharp simultaneous variance extremizers.** For a tree define \(t_v=d_T(v)-1\ge0\). Since \(\sum_vd_T(v)=2(n-1)\), we have \(\sum_vt_v=n-2\). Furthermore,

\[
 W(T)=\sum_v\frac{t_v(t_v+1)}{2}.
\]

This is at least \(\sum_vt_v=n-2\), with equality exactly when every \(t_v\le1\), equivalently every vertex has degree at most two, so the tree is a path. By convexity, combining any two positive \(t\)'s increases the sum; the maximum is attained only when one \(t_v=n-2\), yielding \(W=\binom{n-1}{2}\) and the star. Multiplying their difference by \(2(p_3-p_4)>0\) gives the asserted exact variance gap, and uniqueness for every sample size in the stated range.

**4. Sharp onset of indistinguishability.** Up to isomorphism there is only one tree on two or three vertices. On four vertices the path and star have \(W\)-values \(2,3\); on five vertices the path, the \((3,2,1,1,1)\)-degree tree, and the star have \(W\)-values \(3,4,6\). These lists exhaust the types because the positive degree sequence of a tree sums to twice the number of edges, and the indicated small-degree sequences have unique tree realizations. By part 2, first-two-moment curves therefore distinguish trees through five sites.

For six sites let \(A\) and \(B\) have the following edge sets (site labels are \(0,\ldots,5\)):

```text
A: (0,1) (1,3) (0,2) (2,4) (0,5)
B: (0,1) (1,2) (2,3) (0,4) (0,5)
```

They are trees with degree multiset \((3,2,2,1,1,1)\) and \(W(A)=W(B)=5\). They are not isomorphic: the unique degree-three site has one leaf neighbor in \(A\) but two in \(B\). By part 2 their full mean-and-variance curves coincide. Yet when two sites are sampled, the 15 equally likely site pairs yield exact richness histograms

\[
 \begin{array}{c|rrrr}
 &R_2=2&R_2=3&R_2=4&R_2=5\\\hline
 A&5&5&5&0\\
 B&4&8&2&1
 \end{array}
\]

(the counts divide by \(15\) to give probabilities). Both distributions have mean \(3\) and variance \(2/3\), but their third centered moments are respectively \(0\) and \(2/5\).

For each \(n>6\), add \(n-6\) new leaf sites, all attached to site \(0\), to both graphs. Their degree multisets remain identical: one site has degree \(n-3\), two have degree \(2\), and \(n-3\) are leaves. Both have \(W=\binom{n-3}{2}+2\) and remain nonisomorphic because the unique high-degree site's count of adjacent leaves differs by one. Among selected site pairs, richness \(2\) arises either from two nonadjacent leaves or from an adjacent degree-two/leaf pair. Both trees have the same number of leaves, but the first has two degree-two/leaf edges while the second has one. Consequently,

\[
 \mathbb P_A(R_2=2)-\mathbb P_B(R_2=2)
 =\frac1{\binom n2}>0.
\]

Thus the full laws still differ for every \(n\ge6\), proving the sharp threshold and the infinite counterfamily.

## Verification

The accompanying `verify.py` uses Python's standard library and exact integer/fraction arithmetic; run `python3 verify.py`. It enumerates **all 18,244 labeled trees** of orders four through seven by Prüfer sequences and all sample-site subsets at every sample size, comparing direct richness moments against the theorem in **144,358 tree-and-sample-size cases**, totaling **2,238,496 site-subset evaluations**. It also checks the six-site histograms and their third centered moments exactly and verifies the constructed infinite family at orders six through fifteen. The completed run printed `VERIFY_OK`. These finite computations independently stress-test the symbolic proof but are not its justification for unbounded \(n\).

## Relationship to prior work

Classical sample-based species-accumulation theory already contains unrestricted combinatorial expressions for conditional first and second moments. In particular Ugland, Gray and Ellingsen (2003) give these quantities for general incidence matrices, and Colwell, Mao and Chang (2004) distinguish this conditional sample-order variance from a different estimator variance. **The first formula above is not claimed to be new as a general rarefaction formula.** The central contribution is the tree-constrained information boundary: exact equivalence of the entire two-moment curve to a single local overlap count, a **sharp first six-site loss of distributional information**, and a persistent all-orders construction. The simultaneous variance envelopes translate classical tree-degree extremal inequalities into this rarefaction setting; they are useful corollaries, not independent claims of new tree-degree inequalities.

Tittmann, Averbouch and Makowsky (2008 preprint; 2011 journal) develop the full induced-subgraph component polynomial, which for a tree encodes the **entire** distribution of richness at every fixed site-subset size. Their Proposition 2 reports that this stronger polynomial distinguishes all nonisomorphic trees through nine vertices. There is no conflict: the two trees here share only first and second moments, not the full component polynomial. The checked work does not supply this moment-blindness threshold or simultaneous tree-incidence variance envelope. The result is not a claim that full rarefaction distributions fail to distinguish trees at six vertices.

## Limitations

The theorem assumes exactly two occupied sites per species, distinct incidence rows, a minimally connected site-projection tree, and equal-probability sampling of fixed-size site subsets. It neither concerns random underlying tree generation nor provides confidence intervals for an estimator of population richness. The numerical tests end at the stated finite orders; the unlimited theorem rests on the preceding identities and construction. Mathematical originality remains subject to possibly unindexed results about graph degree moments, vertex-induced edge-count distributions, and related polynomial specializations; unpublished work cannot be excluded by database searches. The variance extrema use standard tree-degree inequalities already treated in the literature on random crossings in dependency trees, so their significance is contextual and is not presented as a new inequality on its own.

## References

1. K. I. Ugland, J. S. Gray and K. E. Ellingsen, *The species-accumulation curve and estimation of species richness*, Journal of Animal Ecology 72 (2003), 888–897. First publicly published 2003-08-15. DOI: 10.1046/j.1365-2656.2003.00748.x.
2. R. K. Colwell, C. X. Mao and J. Chang, *Interpolating, extrapolating, and comparing incidence-based species accumulation curves*, Ecology 85 (2004), 2717–2727. DOI: 10.1890/03-0557. Author-hosted lawful full text: https://www.robertkcolwell.org/publications/7532.pdf.
3. P. Tittmann, I. Averbouch and J. A. Makowsky, *The enumeration of vertex induced subgraphs with respect to the number of components*, arXiv:0812.4147 (first posted 2008-12-22); European Journal of Combinatorics 32 (2011), 954–974.
4. R. Ferrer-i-Cancho, *Random crossings in dependency trees*, arXiv:1305.4561 (2013 preprint). In particular, the known star/path extrema of the degree second moment are relevant prior coverage of the tree-degree part of this result.
