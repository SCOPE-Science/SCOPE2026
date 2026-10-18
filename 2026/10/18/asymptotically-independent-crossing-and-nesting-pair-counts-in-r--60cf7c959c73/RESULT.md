# Asymptotically independent crossing and nesting pair counts in random matchings

## Finding

Consider the uniformly distributed perfect matching of \(2n\) fixed points in circular order. Write \(X_n\) for the number of unordered chord pairs with alternating endpoints, and \(Y_n\) for the number of unordered chord pairs with properly nested endpoints (using the linear order obtained by cutting the circle before point \(1\)). For every integer \(n\ge2\),

\[
\mathbb E X_n=\mathbb E Y_n=\frac{n(n-1)}6,\qquad
\operatorname{Var}(X_n)=\operatorname{Var}(Y_n)=\frac{n(n-1)(n+3)}{45},
\]
\[
\operatorname{Cov}(X_n,Y_n)=-\frac{n(n-1)}{18},\qquad
\operatorname{Corr}(X_n,Y_n)=-\frac5{2(n+3)}.
\]

More strongly, as \(n\to\infty\),

\[
n^{-3/2}\bigl(X_n-\mathbb E X_n,\,Y_n-\mathbb E Y_n\bigr)
\xrightarrow{d}\bigl(Z_1,Z_2\bigr),\qquad
Z_1,Z_2\text{ independent }N(0,1/45).
\]

Thus negative finite-sample dependence disappears at the natural joint Gaussian fluctuation scale.

## Assumptions and scope

The matching is uniform over the \((2n-1)!!\) perfect matchings of labeled points in a fixed circular order. The endpoints of one chord are represented by \(0<a<b<1\). A pair of chords crosses when its four endpoints alternate. A pair nests when one interval between its endpoints strictly contains the other. The third possible relation is separation. In contrast to the cyclic crossing relation, nesting uses the displayed cut and linear order. The claims concern the **number of two-chord crossings/nestings**, not the maximal size of a collection of pairwise crossing or nesting chords.

## Proof

**Uniform independent-chord construction.** Take \(n\) independently sampled pairs \((U_i,V_i)\) of independent uniform points of \((0,1)\), and put \(A_i=\min(U_i,V_i)\), \(B_i=\max(U_i,V_i)\). Sort all \(2n\) endpoints and forget the chord labels. Every perfect matching of the sorted positions is then equally likely: the ordering of the \(2n\) original endpoint labels is uniform and each unlabeled matching is represented by the same number of permutations. Hence this construction has the required finite matching law.

For \(i<j\), let \(C_{ij}\) indicate that chords \(i,j\) cross and \(N_{ij}\) indicate that they nest. Then \(X_n=\sum_{i<j}C_{ij}\), \(Y_n=\sum_{i<j}N_{ij}\). Three pairwise relative endpoint arrangements occur with probability \(1/3\) each: crossing, nesting, separation. In particular, \(\mathbb EC_{ij}=\mathbb EN_{ij}=1/3\) and \(C_{ij}N_{ij}=0\).

**Orthogonality of shared-chord influences.** Conditional on chord \(i\) having endpoints \(a<b\), put \(\ell=b-a\). Independent chord \(j\) crosses chord \(i\) with probability

\[
g_C(a,b)=2\ell(1-\ell),
\]

and nests with it (either of the two nesting orientations) with probability

\[
g_N(a,b)=\ell^2+2a(1-b).
\]

The joint density of \((A_i,B_i)\) is \(2\) on \(0<a<b<1\). Direct polynomial integration yields

\[
\mathbb Eg_C=\mathbb Eg_N=\frac13,\quad
\mathbb Eg_C^2=\mathbb Eg_N^2=\frac{2}{15},\quad
\mathbb E(g_Cg_N)=\frac19.
\]

Consequently \(\operatorname{Var}(g_C)=\operatorname{Var}(g_N)=1/45\) and \(\operatorname{Cov}(g_C,g_N)=0\). If two distinct unordered chord pairs share one chord, their indicator events are independent conditional on that common chord. Their cross-type covariance therefore equals the covariance of the corresponding conditional probabilities, namely **zero**. Indicators on disjoint chord pairs are independent outright. For the same unordered pair the cross-type covariance is \(-1/9\). Summing over all unordered pairs gives

\[
\operatorname{Cov}(X_n,Y_n)=\binom n2(-1/9)=-\frac{n(n-1)}{18}.
\]

For two crossing indicators on distinct chord pairs that share one chord, the covariance equals \(\operatorname{Var}(g_C)=1/45\); the same is true for two nesting indicators. Writing \(m=\binom n2\), exactly \(3\binom n3\) unordered pairs of distinct chord pairs share a chord. Therefore

\[
\operatorname{Var}(X_n)=\operatorname{Var}(Y_n)
=m\frac29+2\cdot3\binom n3\frac1{45}
=\frac{n(n-1)(n+3)}{45}.
\]

Division produces the asserted exact correlation.

**Joint Gaussian limit.** Denote the centered one-chord projections by \(h_C=g_C-1/3\), \(h_N=g_N-1/3\), and let \(W_i=(A_i,B_i)\). The order-two Hoeffding decompositions read

\[
X_n-\mathbb EX_n=(n-1)\sum_{i=1}^nh_C(W_i)+R_{n,C},\qquad
Y_n-\mathbb EY_n=(n-1)\sum_{i=1}^nh_N(W_i)+R_{n,N}.
\]

The degenerate remainder for each bounded order-two kernel has variance \(O(n^2)\): distinct unordered kernel terms have zero covariance, including terms sharing one index, by the defining conditional-mean-zero property. Hence both remainders, divided by \(n^{3/2}\), tend to zero in \(L^2\). The independent vectors \((h_C(W_i),h_N(W_i))\) have mean zero and covariance matrix \(\operatorname{diag}(1/45,1/45)\). The ordinary multivariate iid central limit theorem and Slutsky's theorem yield the displayed convergence to independent Gaussians.

## Verification

The companion Python script `verify.py` exhaustively enumerates each perfect matching through six chords using rational arithmetic. For each size it checks the exact means, variances, covariance and correlation. It also independently enumerates all \(90\) arrangements of three distinguishable chords to check the shared-chord mixed-probability cancellation. The analytic integral identities above and the Hoeffding argument—not any finite enumeration—establish the general result. Execute `python verify.py` with Python 3; no extra packages are required.

## Relationship to prior work

Flajolet and Noy (2000, INRIA RR3914, Section 2, Theorem 3) proved the marginal mean, variance and Gaussian limit for the number of chord-pair crossings. Crossing/nesting marginal symmetry and joint symmetry are studied by Klazar (2005) and by Chen, Deng, Du, Stanley and Yan (2005). Baik and Jenkins (2011) prove asymptotic independence for **maximal crossing and maximal nesting sizes**, which have Tracy–Widom rather than Gaussian fluctuation scales; those are not the present pair counts. The specific finite covariance cancellation and resulting bivariate Gaussian independence of crossing-pair and nesting-pair **counts** are not given by the inspected statements of these papers. The marginal variance and marginal Gaussianity are not claimed as new.

## Limitations

The result applies to uniform perfect matchings, not to nonuniform or restricted matching ensembles. The exact covariance does not imply finite-size independence; indeed the two counts are negatively correlated. The limiting law is weak convergence, without an asserted quantitative convergence rate. General generating functions for joint crossing/nesting counts may encode the covariance implicitly, so full historical priority remains uncertain. No independent external audit or priority certification is claimed.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA RR3914, March 2000; Section 2, Theorem 3. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
2. M. Klazar, *On identities concerning the numbers of crossings and nestings of two edges in matchings*, arXiv:math/0503012, publicly posted March 1, 2005. https://arxiv.org/abs/math/0503012
3. W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley, C. H. Yan, *Crossings and Nestings of Matchings and Partitions*, arXiv:math/0501230, publicly posted January 14, 2005. https://arxiv.org/abs/math/0501230
4. J. Baik and R. Jenkins, *Limiting distribution of maximal crossing and nesting of Poissonized random matchings*, arXiv:1111.0269, publicly posted November 1, 2011. https://arxiv.org/abs/1111.0269
5. W. Hoeffding, *A Class of Statistics with Asymptotically Normal Distribution*, Ann. Math. Statist. 19 (1948), 293–325; general decomposition used in the proof.
