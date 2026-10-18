# Asymptotic independence of crossing and nesting counts despite exact negative finite-size covariance

## Finding
For a uniformly random perfect matching of the ordered set \(\{1,\ldots,2n\}\), with integer \(n\geq2\), let \(X_n\) be the number of unordered pairs of chords whose four endpoints alternate (crossings), and let \(Y_n\) be the number of unordered chord pairs for which one interval strictly contains the other (nestings). Then
\[
\mathbb E X_n=\mathbb E Y_n=\frac{n(n-1)}6,\qquad
\operatorname{Var}(X_n)=\operatorname{Var}(Y_n)=\frac{n(n-1)(n+3)}{45},
\]
\[
\operatorname{Cov}(X_n,Y_n)=-\frac{n(n-1)}{18},\qquad
\operatorname{Corr}(X_n,Y_n)=-\frac5{2(n+3)}.
\]
In particular, the covariance is strictly negative for each finite \(n\geq2\), but the standardized pair satisfies the **joint** weak limit
\[
\left(\frac{X_n-\mathbb E X_n}{\sqrt{\operatorname{Var}(X_n)}},
\frac{Y_n-\mathbb E Y_n}{\sqrt{\operatorname{Var}(Y_n)}}\right)
\ \xrightarrow{\ d\ }\ (G_1,G_2),
\]
where \(G_1,G_2\) are **independent** standard Gaussian random variables. This is asymptotic independence in the joint Gaussian limit, not exact finite-size independence or a total-variation claim.

## Assumptions and scope
Every perfect matching of \(\{1,\ldots,2n\}\) has probability \(1/(2n-1)!!\). For two chords \((a,b)\) and \((c,d)\), with \(a<b\), \(c<d\), crossing means \(a<c<b<d\) or \(c<a<d<b\); nesting means \(a<c<d<b\) or \(c<a<b<d\). Each unordered chord pair contributes at most one to either count. No independence between \(X_n\) and \(Y_n\) for finite \(n\) is assumed. The limit is as \(n\to\infty\) through positive integers.

## Proof
**Independent-chord representation.** Draw \(2n\) independent continuous uniform variables on \([0,1]\), group consecutive pairs into \(n\) labeled chords, and sort the \(2n\) values globally. The resulting unlabeled matching on ranks \(1,\ldots,2n\) is uniform: each matching has exactly \(2^n n!\) preimages among the \((2n)!\) permutations of labeled endpoints. Crossing and nesting depend only on these ranks. Thus we may use independent chord variables \(Z_i=(A_i,B_i)\), \(A_i=\min(U_i,V_i)\), \(B_i=\max(U_i,V_i)\), each with density \(2\) on \(0<a<b<1\).

Let \(h_C(Z_i,Z_j)\) and \(h_N(Z_i,Z_j)\) indicate crossing and nesting, respectively. By exchangeability of the three pairings of four uniform endpoints, \(\mathbb E h_C=\mathbb E h_N=1/3\), and hence the means follow.

**Exact conditional projections.** For a fixed \(z=(a,b)\), put \(\ell=b-a\). The other chord crosses it exactly when it has one endpoint inside and one outside the interval. It nests with it exactly when both endpoints lie inside or when it contains both \(a\) and \(b\). Therefore
\[
p_C(a,b):=\mathbb E[h_C(z,Z')]=2\ell(1-\ell),\qquad
p_N(a,b):=\mathbb E[h_N(z,Z')]=\ell^2+2a(1-b).
\]
Using density \(2\) on the triangle and integrating these explicit polynomials gives
\[
\mathbb E[p_C]=\mathbb E[p_N]=\frac13,\quad
\mathbb E[p_C^2]=\mathbb E[p_N^2]=\frac{2}{15},\quad
\mathbb E[p_Cp_N]=\frac19.
\]
For complete reproducibility each integral is \(2\int_0^1\int_a^1(\cdot)\,db\,da\). It follows that the centered projections \(g_C=p_C-1/3\), \(g_N=p_N-1/3\) each have variance \(1/45\) and have covariance exactly zero.

**Finite covariance and variance.** Two indicators indexed by disjoint unordered pairs of chord labels are independent. When two unordered chord pairs share exactly one chord, their covariance is the covariance of their one-chord conditional means. Thus crossing–nesting shared-chord covariance is \(0\), and the analogous crossing–crossing and nesting–nesting shared-chord covariance is \(1/45\). For an identical unordered chord pair, the crossing and nesting indicators are mutually exclusive, yielding covariance \(-1/9\); each indicator has variance \(2/9\). There are \(\binom n2\) individual pairs and \(3\binom n3\) unordered pairs of *distinct* indicators sharing a chord. Consequently
\[
\operatorname{Cov}(X_n,Y_n)=-\frac19\binom n2,
\quad \operatorname{Var}(X_n)=\operatorname{Var}(Y_n)=
\frac29\binom n2+\frac{6}{45}\binom n3.
\]
Simplifying yields the stated formulas and the exact correlation. The shared-chord terms of the cross-covariance vanish; all its negative contribution comes from mutual exclusion for the same chord pair.

**Joint central limit theorem.** The Hoeffding decompositions are
\[
X_n-\mathbb E X_n=(n-1)\sum_{i=1}^n g_C(Z_i)+R_{C,n},\qquad
Y_n-\mathbb E Y_n=(n-1)\sum_{i=1}^n g_N(Z_i)+R_{N,n},
\]
where each residual is the sum over \(i<j\) of \(h(Z_i,Z_j)-1/3-g(Z_i)-g(Z_j)\). Every such kernel is conditionally centered given either argument. Hence residuals from distinct pairs are uncorrelated even when their label pairs intersect. Their exact variances are
\[
\operatorname{Var}(R_{C,n})=\operatorname{Var}(R_{N,n})
=\frac8{45}\binom n2=\frac{4n(n-1)}{45}=O(n^2).
\]
Thus the residual vector divided by \(n^{3/2}\) tends to zero in \(L^2\). Since \((g_C(Z_i),g_N(Z_i))\) are iid bounded centered vectors with covariance matrix \(\frac1{45}I_2\), the classical iid bivariate central limit theorem implies
\[
\frac1{\sqrt n}\sum_{i=1}^n(g_C(Z_i),g_N(Z_i))
\xrightarrow{d}N_2\left(0,\frac1{45}I_2\right).
\]
Because \(\operatorname{Var}(X_n)=\operatorname{Var}(Y_n)\sim n^3/45\), Slutsky's theorem gives the displayed joint limit. The zero off-diagonal Gaussian covariance gives independence of its coordinates. This completes the proof.

## Verification
The standalone `verify.py` checks all five projection integrals symbolically by exact polynomial integration over the chord triangle, checks the covariance and variance algebra, and independently exhausts all \((2n-1)!!\) matchings for \(2\le n\le7\), comparing exact rational means, variances and covariances. These finite checks support, but do not replace, the iid joint-CLT and degenerate-kernel arguments for general \(n\).

## Relationship to prior work
The crossing/nesting symmetry and exact bivariate enumerating polynomial are classical: Kasraoui and Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions* (2006), prove the exchange symmetry and give a two-variable continued fraction (Proposition 3.8); Klazar's earlier work proves matching equidistribution. These general generating-function results encode every finite-size mixed moment and **must not** be mistaken for an absence of prior joint-distribution information. Differentiating them can in principle recover the finite covariance, so the covariance identity on its own is not advanced as a priority-independent novelty claim.

The principal assertion here is instead the particular **joint** Gaussian limit with independent coordinates, together with the explicit orthogonal one-chord projection mechanism and the exact vanishing of shared-chord cross terms. Paguyo (first posted 2021-04-02; Theorem 1.1 and Lemma 2.2) gives a quantitative **univariate** crossing CLT and the known crossing variance, not this joint crossing/nesting limit. Féray's weighted-dependency-graph treatment likewise proves a univariate crossing CLT (Theorem 6.5). The cited general multivariate methods do not, without an additional joint comparison, establish independence of these two limiting coordinates.

## Limitations
The limiting pair is Gaussian independent only after centering and variance normalization; the finite counts are dependent and negatively correlated. No rate of bivariate convergence, independence in total variation, or multivariate local limit theorem is claimed. General U-statistic central limit technology is classical; the claim lies in its explicit application to this natural pair, especially the zero mixed first-projection covariance. A historical-priority risk remains because older crossing/nesting generating functions might have led to an unlocated asymptotic theorem. Independent historical verification has not been performed.

## References
1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134 (first public version 2021-04-02), https://arxiv.org/abs/2104.01134 ; Theorem 1.1, Lemma 2.2, Sections 2 and 4.
2. A. Kasraoui and J. Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions*, arXiv:math/0601081 (2006), https://arxiv.org/abs/math/0601081 ; Corollary 1.5 and Proposition 3.8.
3. M. Klazar, *On identities concerning numbers of crossings and nestings of two edges in matchings*, arXiv:math/0503012 (2005), https://arxiv.org/abs/math/0503012 .
4. V. Féray, *Weighted dependency graphs*, arXiv:1605.03836 (2016), https://arxiv.org/abs/1605.03836 ; Section 6, Theorem 6.5.
