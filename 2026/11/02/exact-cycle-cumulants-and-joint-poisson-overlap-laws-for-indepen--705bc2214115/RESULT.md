# Exact cycle cumulants and joint Poisson overlap laws for independent Cayley trees

## Finding

Let \(n\ge3\) and \(q\ge3\) be integers. Draw independent, uniformly distributed labeled spanning trees \(T_1,\ldots,T_q\) of the complete graph \(K_n\). For each unordered pair \(\{a,b\}\) of distinct tree indices, put
\[
X_{ab}=|E(T_a)\cap E(T_b)|,\qquad \mu_n=\mathbb E X_{ab}=\frac{2(n-1)}n.
\]
The following are assertions about one joint overlap network, not three unrelated models.

**Forest factorization.** If \(F\) is a simple forest on a subset of the tree indices, then
\[
\mathbb E\prod_{\{a,b\}\in E(F)}X_{ab}=\mu_n^{|E(F)|}.
\]
In particular, every joint cumulant of distinct overlap variables indexed by a nonempty forest with at least two edges vanishes. All *distinct* pair-overlap counts are exactly uncorrelated, including when their index pairs share a tree; finite-sample independence is not asserted.

**Exact cycle cumulants.** If \(a_1,\ldots,a_\ell\) are distinct tree indices, \(3\le\ell\le q\), and \(a_{\ell+1}=a_1\), then
\[
\boxed{\begin{aligned}
&\operatorname{cum}(X_{a_1a_2},X_{a_2a_3},\ldots,X_{a_\ell a_1})\\
&=\mathbb E\prod_{j=1}^{\ell}(X_{a_ja_{j+1}}-\mu_n)\\
&=\frac{n-1}{n^\ell}+\frac{n(n-3)}2\left(\frac{2(n-1)}{n^2}\right)^\ell>0.
\end{aligned}}
\]
For fixed \(\ell\ge3\), this is asymptotic to \(2^{\ell-1}n^{2-\ell}\). For a triangle, the exact third centered mixed moment is
\[
\frac{n-1}{n^3}+\frac{4(n-3)(n-1)^3}{n^5}\sim\frac4n.
\]
This gives a complete family of first detectable cyclic dependencies despite zero pair covariances.

**Joint Poisson limit.** For each fixed number \(q\) of trees, as \(n\to\infty\),
\[
\boxed{(X_{ab})_{1\le a<b\le q}\ \Rightarrow\ (Z_{ab})_{1\le a<b\le q},\qquad Z_{ab}\text{ mutually independent }\operatorname{Poisson}(2).}
\]
More precisely, for every fixed collection of nonnegative integers \((r_{ab})\), with \(R=\sum_{a<b}r_{ab}\),
\[
\mathbb E\prod_{a<b}(X_{ab})_{r_{ab}}=2^R+O_{q,(r_{ab})}(n^{-1}),
\]
where \((x)_r=x(x-1)\cdots(x-r+1)\) and \((x)_0=1\).

## Assumptions and scope

All host vertices are labeled, all \(n^{n-2}\) Cayley trees have equal probability, and different trees are sampled independently. Exact moment formulas apply to every \(n\ge3\) and every fixed finite index forest/cycle for which the named trees exist. The joint limit keeps \(q\) fixed as \(n\to\infty\); no growing-\(q\) theorem is claimed. Cumulants here concern *distinct* index-pair variables, not repeated powers of a single variable.

## Proof

**1. Forest containment bound.** A standard Cayley-forest extension count says that if \(H\) is an acyclic set of \(s\) prescribed host edges, and \(C\) ranges over the components of \(([n],H)\), then
\[
\Pr(H\subseteq E(T))=n^{-s}\prod_C |C|\le\left(\frac2n\right)^s.
\]
The inequality follows from \(c\le2^{c-1}\) for every positive integer \(c\), since \(\sum_C(|C|-1)=s\). A cyclic prescribed set has inclusion probability zero. For one host edge the inclusion probability is exactly \(2/n\); for two distinct host edges it equals \(3/n^2\) when they share a vertex and \(4/n^2\) otherwise.

**2. Index-forest product moments.** An overlap \(X_{ab}\) has mean \(\binom n2(2/n)^2=\mu_n\). For a nonempty simple forest \(F\) of tree indices, choose a leaf index \(a\) adjacent only to \(b\). Conditional on all the other trees, the only factor involving \(T_a\) is \(X_{ab}\), whose conditional mean is \(\sum_{e\in E(T_b)}2/n=\mu_n\), independent of the realized tree \(T_b\). Integrating out \(T_a\) removes the leaf edge and multiplies the moment by \(\mu_n\). Induction gives the displayed forest product identity. Its validity for every subset of the forest implies vanishing of all its mixed cumulants with at least two distinct variables by the partition formula for cumulants.

**3. The two-edge inclusion spectrum.** Index host edges by \(e\in E(K_n)\) and set \(K_{ef}=\Pr(e,f\in E(T))\). Let \(J\) denote the all-ones matrix and \(A\) the adjacency matrix of the line graph \(L(K_n)\), where distinct host edges are adjacent exactly when they share an endpoint. The inclusion probabilities in step 1 yield
\[
K=\frac4{n^2}J-\frac1{n^2}A+\frac{2(n-2)}{n^2}I.
\]
To check the spectrum without an unstated spectral lemma, let \(B\) be the \(n\)-by-\(\binom n2\) unsigned vertex-edge incidence matrix. Then \(B^\top B=2I+A\), while \(BB^\top=(n-2)I+J_n\). Hence \(A\) has eigenvalues \(2(n-2)\) with multiplicity one, \(n-4\) with multiplicity \(n-1\), and \(-2\) with multiplicity \(n(n-3)/2\). (For \(n=3\), the last multiplicity is zero.) Thus the eigenvalues of \(K\) are
\[
\mu_n\quad(1),\qquad \frac1n\quad(n-1),\qquad \frac{2(n-1)}{n^2}\quad\left(\frac{n(n-3)}2\right),
\]
with multiplicities in parentheses.

**4. Exact cyclic cumulants.** In the expansion of \(\prod_{j=1}^\ell X_{a_ja_{j+1}}\), assign a host edge \(e_j\) to each overlap. Independence of the trees gives a factor \(K_{e_{j-1}e_j}\) for each vertex of the index cycle. Summing all assigned host edges therefore gives exactly
\[
\mathbb E\prod_{j=1}^\ell X_{a_ja_{j+1}}
=\operatorname{tr}(K^\ell)
=\mu_n^\ell+\frac{n-1}{n^\ell}
+\frac{n(n-3)}2\left(\frac{2(n-1)}{n^2}\right)^\ell.
\]
Every proper subset of the edges of a *simple* index cycle is a forest, so its product moment equals the appropriate power of \(\mu_n\). Expanding the product of centered variables leaves exactly \(\operatorname{tr}(K^\ell)-\mu_n^\ell\). The same proper-subset factorization in the general moment-cumulant partition formula shows that the joint cumulant equals this centered product. Both remaining spectral terms are nonnegative, with the first strictly positive. For fixed \(\ell\), the second term is \(2^{\ell-1}n^{2-\ell}(1+O(n^{-1}))\), and the first is smaller by one order.

**5. Mixed factorial moments and asymptotic independence.** Fix \((r_{ab})\) and \(R=\sum r_{ab}\). Expanding \(\prod_{a<b}(X_{ab})_{r_{ab}}\) assigns one host edge to each of the \(R\) labeled occurrences; within a fixed index pair the assigned host edges must be distinct. If all \(R\) host edges are vertex-disjoint, there are \((n)_{2R}/2^R\) such assignments. Each of these host edges belongs to precisely two prescribed trees, and the forest formula makes the total inclusion probability \((2/n)^{2R}\). Their contribution is exactly \(2^R(n)_{2R}/n^{2R}=2^R+O_R(n^{-1})\).

If all host edges are distinct but some share a vertex, there are \(O_R(n^{2R-1})\) assignments, each of probability at most \((2/n)^{2R}\); their total is \(O_R(n^{-1})\). Otherwise suppose there are only \(d<R\) distinct host edges. The number of assignments is \(O_R(n^{2d})\). If \(s_a\) is the number of different prescribed host edges required in tree \(T_a\), the containment bound and tree independence give probability at most \((2/n)^{\sum_a s_a}\). Every host edge is associated with at least one index pair and therefore contributes at least two to \(\sum_a s_a\); a repeated host edge occurs in *different* index-pair groups (the falling factorial forbids repetition within a group) and consequently must occur in at least three different trees. Thus \(\sum_a s_a\ge2d+1\), and the total contribution of all such assignments is \(O_R(n^{-1})\). This establishes the asserted mixed factorial-moment asymptotic.

The uniformly bounded first moments give tightness of the fixed-dimensional nonnegative vector. Higher factorial-moment bounds give uniform integrability of each polynomial, so all subsequential limits retain factorial moments \(2^R\). For a subsequential limit \((Y_{ab})\), Tonelli's theorem and the nonnegative factorial expansion yield, for any \(u_{ab}\ge0\),
\[
\mathbb E\prod_{a<b}(1+u_{ab})^{Y_{ab}}
=\sum_{(r_{ab})}\prod_{a<b}\frac{(2u_{ab})^{r_{ab}}}{r_{ab}!}
=\exp\left(2\sum_{a<b}u_{ab}\right).
\]
This uniquely specifies the product of independent \(\operatorname{Poisson}(2)\) laws, proving joint convergence.

## Verification

The standalone standard-library script `verify.py` checks the exact host-edge inclusion matrix against its eigenvalue trace formula for \(n=3,\ldots,8\) and powers \(2,\ldots,5\). It enumerates every Prüfer-encoded labeled tree at \(n=3,4\), independently computes triangle and square index-cycle centered moments, and checks forest product moments. It also checks positivity and the polynomial form of the triangle expression for several further orders. Execute `python3 verify.py`; the supplied file reports `VERIFY_OK 82 exact assertions`. These finite tests support but do not establish the all-size statements, which are proved above.

## Relationship to prior work

Bóna, Burghart and Wagner, arXiv:2501.18570 (first posted January 30, 2025, updated version 4), prove the scalar pair-overlap Poisson law and the needed Cayley-forest probabilities. Their Section 2 treats two trees; Remark 2 treats the rare event that *all* \(k\ge3\) trees share a common host edge. Neither is the simultaneous joint distribution of all \(\binom q2\) pair overlaps or an index-cycle cumulant formula. The fact that three fixed trees seldom share a host edge is an existing result and is not claimed as a new contribution.

James, Larson, Montealegre and Salmon, arXiv:1701.06208v3, prove the Poisson limit in total variation for the **aggregate union-edge deficit** of many trees (citing Janson's 1986 fixed-size theorem). This scalar quantity asymptotically equals the sum of all pair overlaps but does not determine their labeled joint law, and its theorem does not give exact finite-sample cyclic cumulants. The stronger prior scalar limit is expressly credited, not reproved as novel.

Janson, *Random trees in a graph and trees in a random graph* (1986), is highly relevant: the accessible abstract covers scalar intersections and unions among multiple trees. Its full 1986 text was not accessible in this investigation, so no assertion is made that the uninspected full text excludes the present formulas. This remains the most important historical-priority risk. The new statements are thus assessed against accessible detailed prior assertions rather than claimed as definitively unprecedented.

## Limitations

The underlying host graph is complete and all trees are uniformly sampled independently. The exact mixed-cumulant formula is for a *simple cycle* of distinct tree indices, not an arbitrary repeated-index cumulant or general index graph. The joint Poisson theorem requires a fixed number of trees and asserts weak convergence with \(O(n^{-1})\) estimates for each fixed mixed factorial moment; it does not supply a joint total-variation rate or an exact finite-dimensional joint mass function. Broader unindexed or inaccessible literature could contain equivalent general statements.

## References

1. M. Bóna, F. Burghart and S. Wagner, *On the intersection of pairs of trees*, arXiv:2501.18570, first posted 2025-01-30; current preprint v4 (2026-09-09). https://arxiv.org/abs/2501.18570
2. A. James, M. Larson, D. Montealegre and A. Salmon, *Unions of random trees and applications*, arXiv:1701.06208v3 (2020). https://arxiv.org/abs/1701.06208
3. S. Janson, *Random trees in a graph and trees in a random graph*, Math. Proc. Cambridge Philos. Soc. **100** (1986), 319–330. https://doi.org/10.1017/S0305004100066111
