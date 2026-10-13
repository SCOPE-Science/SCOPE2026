# Exact negative cherry–Wiener covariance in uniform Cayley trees

## Finding

Let \(T_n\) be uniformly distributed over all \(n^{n-2}\) unrooted trees labelled by \(\{1,\dots,n\}\). Define the cherry count \(C_n\) as the number of unordered pairs of **distinct degree-one vertices sharing a neighbor**, with no restriction on that neighbor's degree, and the Wiener index \(W_n\) as the sum of distances over unordered vertex pairs. For \(m\ge2\) put
\[
d_m=\sum_{k=1}^{m-1}\prod_{j=2}^{k}\left(1-\frac jm\right),\qquad d_1=0,
\]
where an empty product equals one. Define \(\mu_m=\binom m2 d_m\) for \(m\ge1\). Then, for every integer \(n\ge3\),
\[
\boxed{\operatorname{Cov}(C_n,W_n)=\frac{n\binom{n-1}{2}(n-2)^{n-4}}{n^{n-2}}\left[\frac{n+2}{n-2}\mu_{n-2}+2(n-1)-\mu_n\right].}
\]
In particular the covariance is zero for \(n=2,3\) and **strictly negative for every \(n\ge4\)**. Moreover,
\[
\boxed{\operatorname{Cov}(C_n,W_n)\sim-\frac{e^{-2}}4\sqrt{\frac\pi2}\,n^{5/2}}\qquad(n\to\infty).
\]
The exact finite-size statement is valid without asymptotic or distributional approximations.

## Assumptions and scope

All trees are unrooted, unweighted, simple, and **uniformly labelled**; the result does not assert the same formula for uniformly unlabelled, plane, or conditioned phylogenetic trees. A cherry is an unordered pair of leaves with a common center; multiple leaf pairs at one center each count once. In particular, a center may have more than three neighbors. For \(n=2\), \(C_2=0\). For \(n=3\), every tree is a path, \(C_3=1\), and \(W_3=4\). The power with exponent \(n-4=-1\) at \(n=3\) has base one and therefore equals one.

## Proof

**1. A distinguished cherry and its contraction.** Fix pairwise distinct labels \(a,b,c\). Let \(A_{a,b,c}\) be the event that \(a,b\) are leaves both adjacent to \(c\). Deleting the two leaves is a bijection between trees satisfying \(A_{a,b,c}\) and all labelled trees on the remaining \(r=n-2\) vertices. Cayley's count therefore gives, for \(n\ge4\),
\[
\mathbb P(A_{a,b,c})=\frac{r^{r-2}}{n^{n-2}},\qquad
\mathbb E C_n=n\binom{n-1}{2}\frac{r^{r-2}}{n^{n-2}}.
\]
The latter expectation is also one for \(n=3\), as directly checked. Conditional on \(A_{a,b,c}\), the remaining tree \(S_r\) is uniform. With \(c\) in \(S_r\), counting old pairs, pairs containing a new leaf, and the new leaf pair gives exactly
\[
W_n=W(S_r)+2\sum_{x\in V(S_r)}d_{S_r}(c,x)+2r+2.
\]
By exchangeability of the vertices of \(S_r\), the expected distance sum from a fixed center is \(2\mathbb E W(S_r)/r\). Hence
\[
\mathbb E[W_n\mid A_{a,b,c}]=\left(1+\frac4r\right)\mu_r+2(r+1).
\]
Summing the mixed moment over the \(n\binom{n-1}{2}\) labelled cherry indicators yields the boxed exact covariance.

**2. Exact mean distances.** Fix distinct vertices \(u,v\). The number of trees in which the path between \(u,v\) has length \(k\) is
\[
(n-2)_{k-1}\,(k+1)n^{n-k-2},\qquad 1\le k\le n-1,
\]
where \((z)_q\) is the falling factorial. Indeed, order its \(k-1\) interior vertices, then attach the other vertices to that prescribed path. Here the forest-extension count can be proved directly: for a fixed forest on \(n\) labelled vertices with \(c\) components of sizes \(t_1,\ldots,t_c\), the weighted Laplacian of the contracted components is \(n\operatorname{diag}(t_i)-(t_it_j)_{i,j}\). The matrix determinant lemma gives any principal cofactor as \(n^{c-2}\prod_{i=1}^c t_i\); the matrix-tree theorem therefore counts precisely this many completions. Taking a fixed path component of size \(k+1\) and \(n-k-1\) singleton components yields \((k+1)n^{n-k-2}\). Thus, with \(D_n=d_{T_n}(u,v)\),
\[
\mathbb P(D_n=k)=\frac{(k+1)(n-2)_{k-1}}{n^k},\quad
\mathbb P(D_n\ge k)=f_n(k):=\prod_{j=2}^k\left(1-\frac jn\right)
\]
for \(1\le k\le n-1\), and \(f_n(k)=0\) for \(k\ge n\). Summing these tails yields \(\mathbb ED_n=d_n\) and \(\mu_n=\binom n2d_n\).

**3. Strict negative sign for every size.** Put \(r=n-2\) and \(\Delta_n=d_n-d_r\). Substituting the mean-distance identity into the conditional shift gives
\[
Q_n:=\mathbb E[W_n\mid A_{a,b,c}]-\mathbb EW_n
=2(n-1)-3d_r-\binom n2\Delta_n.
\]
For \(n\ge4\), every factor in \(f_n(k)\) dominates the corresponding factor in \(f_r(k)\), so \(\Delta_n>0\). To obtain a uniform quantitative bound, let \(K=\lfloor\sqrt r\rfloor\), and suppose \(K\ge25\). For \(2\le k\le K\), the product difference telescopes into
\[
f_n(k)-f_r(k)
=\sum_{j=2}^k\frac{2j}{nr}
\left(\prod_{i=2}^{j-1}(1-i/n)\right)
\left(\prod_{i=j+1}^{k}(1-i/r)\right)
\ge \frac{f_r(k)}{nr}[k(k+1)-2].
\]
The elementary product bound \(\prod_i(1-t_i)\ge1-\sum_i t_i\), for \(0\le t_i\le1\), gives
\[
f_r(k)\ge1-\frac{k(k+1)/2-1}{r}
\ge\frac{K-1}{2K}.
\]
Summing over \(k=2,\dots,K\) proves
\[
\Delta_n\ge\frac{(K-1)^2(K+4)}{6nr}>\frac4n.
\]
The last inequality holds because \(r<(K+1)^2\) and \((K-1)^2(K+4)>24(K+1)^2\) for every integer \(K\ge25\); the difference is \(K^3-22K^2-55K-20\), which is positive at \(K=25\) and increasing thereafter. This covers all \(n\ge627\). Accordingly,
\[
Q_n<2(n-1)-3d_r-\binom n2\frac4n=-3d_r<0.
\]
The only remaining values \(4\le n\le626\) are covered by the **finite exact integer certificate** in `verify.py`; it reconstructs each \(d_m\) as an integer numerator over \(m^{m-2}\), forms exact rational \(Q_n\), and asserts \(Q_n<0\) separately for each integer in that complete interval. It also checks \(Q_3=0\). Thus no numerical approximation or finite extrapolation is used for the unrestricted sign claim.

**4. Leading asymptotic.** Standard Gaussian-product/Riemann-sum estimates give \(d_n\sim\sqrt{\pi n/2}\). For completeness, fix \(t>0\) and \(k/\sqrt n\to t\); the product formula gives
\[
f_n(k)\to e^{-t^2/2},\qquad
n[f_n(k)-f_{n-2}(k)]\to t^2e^{-t^2/2}.
\]
For \(k\le n/2\), the same telescoping sum gives \(n[f_n(k)-f_{n-2}(k)]\le C(k^2/n)e^{-c k^2/n}\) with universal constants \(C,c>0\), while the sum over \(k>n/2\) is exponentially small. Dominated Riemann sums therefore yield
\[
\sqrt n\,(d_n-d_{n-2})\longrightarrow\int_0^\infty t^2e^{-t^2/2}\,dt=\sqrt{\pi/2}.
\]
Consequently \(Q_n\sim-\tfrac12\sqrt{\pi/2}\,n^{3/2}\), while the cherry expectation satisfies \(\mathbb EC_n\sim e^{-2}n/2\). Their product gives the stated covariance asymptotic.

## Verification

Run `python3 verify.py` from the extracted package. The checker uses only Python's standard library. It verifies the exact sign and conditional-distance expression for all \(624\) integers \(3\le n\le626\), and independently enumerates all \(18{,}247\) Prüfer sequences of labelled trees for \(n=3,4,5,6,7\). For each size it recomputes cherry counts and pairwise distances from the graph, checks their separate means, and checks their mixed covariance against the formula. The checker also evaluates a few sizes beyond the analytic threshold as a secondary spot check. The infinite sign proof for \(n\ge627\) and the asymptotic are analytic, not claimed to follow from these finite computations.

## Relationship to prior work

Erdős and Rényi (1963, Section 5, Theorem 6) use **precisely** the definition of a cherry as two leaves with a common neighbor and compute its occurrence probability in random labelled trees. That single-statistic result does not imply any cherry–Wiener mixed moment. Janson (2003, Sections 3–7) studies the Wiener index in simply generated trees, including Cayley trees as a Poisson(1) case, and joint behavior with **internal path length**, not cherry count. Wagner (2006 preprint / subsequent journal article) studies correlations of Wiener index with other graph parameters in the **rooted ordered** tree model; its parameter set and probability measure are different. The present identity explicitly combines the cherry event with the conditional distance sum in a uniform **unrooted labelled** tree. A standard expected-cherry formula or a standard expected-Wiener formula alone cannot determine the covariance.

## Limitations

No independent mathematical audit has been performed. The historical originality conclusion is relative to the compared sources and searches; an older joint tree-parameter enumerator might encode the same mixed moment. The finite certificate is exact but only spans its stated integers; the remaining infinite range depends on the stated product inequality. The theorem does not classify the full joint law of \((C_n,W_n)\), prove correlation monotonicity, or cover other tree models. It uses the broader original cherry convention and must not be silently substituted for a degree-three-centered cherry definition.

## References

1. P. Erdős and A. Rényi, “Asymmetric graphs,” *Acta Math. Acad. Sci. Hungar.* **14** (1963), 295–315, Section 5, Theorem 6. DOI: https://doi.org/10.1007/BF01895716. Public author-hosted PDF: https://www.renyi.hu/~p_erdos/1963-04.pdf.
2. Svante Janson, “The Wiener Index of Simply Generated Random Trees,” *Random Structures & Algorithms* **22** (2003), 337–358, DOI: https://doi.org/10.1002/rsa.10074. First online publication: 2003-03-03.
3. Stephan Wagner, “Calculating the correlation coefficients of graph-theoretical indices,” preprint arXiv:math/0608753 (2006), https://arxiv.org/abs/math/0608753.
4. G. O. Munsonius, “On Tail Bounds for Random Recursive Trees,” *J. Appl. Probab.* **49** (2012), 566–581, DOI: https://doi.org/10.1239/jap/1339878805 (primary MSC 60C05; classification context, not a claimed source of the new formula).
