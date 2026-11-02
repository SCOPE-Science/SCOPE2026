# The degree-two boundary for loop–parallel-edge dependence in random configurations

## Finding

Let a configuration multigraph be formed by uniformly pairing \(M\) distinguishable half-edges, distributed among finitely many vertices with nonnegative integer degrees \(d_1,\dots,d_v\). Suppose \(M=\sum_i d_i\) is even and \(M\ge 6\). Let \(L\) be the number of self-loops, and let
\[
P=\sum_{1\le i<j\le v}\binom{X_{ij}}2,
\]
where \(X_{ij}\) counts edges between distinct vertices \(i,j\). Set
\[
a_i=\binom{d_i}2,\quad A=\sum_i a_i,\quad
B=\sum_{i<j}a_i a_j,\quad
F=\sum_i a_i(2d_i-3)(A-a_i).
\]
Then the finite-size covariance is exactly
\[
\boxed{\operatorname{Cov}(L,P)=
\frac{2\bigl(4AB-(M-1)F\bigr)}{(M-1)^2(M-3)(M-5)}.}
\]
The sign has the following **complete classification**, without regularity assumptions:

- If \(B=0\), then \(P=0\) almost surely and the covariance is zero.
- If \(B>0\) and every positive degree is two, the covariance is **strictly positive**.
- If \(B>0\) and at least one positive degree differs from two, the covariance is **strictly negative**.

In particular, zero covariance is impossible when at least two vertices have degree at least two. Adding any vertex of degree one or increasing any positive degree above two reverses the positive association of pure two-regular configurations (when the total degree remains even).

## Assumptions and scope

All pairings of the \(M\) distinguishable half-edges have equal probability. Vertices of degree zero are allowed and do not affect the distribution. Self-loops use two half-edges at one vertex; \(P\) counts unordered *pairs of edges* with the same two distinct endpoints, so a triple edge contributes three, not two. Parallel self-loops are not included in \(P\). The theorem covers every finite degree sequence of even total degree at least six; it makes no simplicity, connectivity, bounded-degree, or asymptotic assumptions. The boundary \(M=4\) is not asserted.

## Proof

**1. Exact moments by conditioning.** There are \(a_i\) possible labeled loop-pairs at vertex \(i\); each occurs with probability \(1/(M-1)\). For distinct vertices \(i<j\), each chosen pair of half-edges at each vertex has two possible cross pairings, each with probability \(1/((M-1)(M-3))\). Consequently
\[
\mathbb E L=\frac{A}{M-1},\qquad
\mathbb E P=\frac{2B}{(M-1)(M-3)}.
\]
Fix one potential loop at \(i\). Conditional on its occurrence, all remaining \(M-2\) half-edges form a uniform pairing, and the degree at \(i\) decreases by two. The loop-pair count at \(i\) therefore decreases by
\[
\binom{d_i}2-\binom{d_i-2}2=2d_i-3.
\]
The new cross-vertex pair total is \(B-(2d_i-3)(A-a_i)\). As \(M\ge6\), the remaining pairing has at least four half-edges and
\[
\mathbb E[P\mid\text{this loop at }i]
=\frac{2[B-(2d_i-3)(A-a_i)]}{(M-3)(M-5)}.
\]
Sum over the \(a_i\) potential loops to obtain
\[
\mathbb E(LP)=\frac{2(AB-F)}{(M-1)(M-3)(M-5)}.
\]
Subtracting the product of the expectations gives the announced covariance formula.

**2. Decompose its sign.** Put \(D=(M-1)F-4AB\). The denominator of the covariance is strictly positive, so its sign is the opposite of \(D\). Let \(I=\{i:d_i\ge2\}\), let \(\ell=\#\{i:d_i=1\}\), and for \(i,j\in I\) define
\[
Q_{ij}=2d_id_j-3(d_i+d_j)+3.
\]
For three distinct indices in \(I\), write
\[
\begin{split}
T_{ijk}={}&a_ia_jd_k(d_i+d_j-d_k-2)\\
&+a_ia_kd_j(d_i+d_k-d_j-2)\\
&+a_ja_kd_i(d_j+d_k-d_i-2).
\end{split}
\]
An exact expansion, grouping terms by the number of distinct vertex indices, gives
\[
\boxed{\frac D2=
\sum_{\{i,j\}\subset I}a_ia_jQ_{ij}
+\sum_{\{i,j,k\}\subset I}T_{ijk}
+\ell\sum_{\{i,j\}\subset I}a_ia_j(d_i+d_j-3).}
\tag{1}
\]
This identity includes all zero- and one-degree vertices and is valid for arbitrary degree heterogeneity.

**3. All triple terms are nonnegative.** In any triple, set \(u=d_i-1\), \(v=d_j-1\), \(w=d_k-1\), so \(u,v,w\ge1\). Algebra gives
\[
\frac{4T_{ijk}}{d_id_jd_k}=
(u^2v+uv^2+u^2w+uw^2+v^2w+vw^2)
-3uvw-(uv+uw+vw).
\]
The arithmetic–geometric mean inequality bounds the six-term parenthesis below by \(6uvw\). Hence
\[
\frac{4T_{ijk}}{d_id_jd_k}
\ge uvw\left(3-\frac1u-\frac1v-\frac1w\right)\ge0.
\]
Equality holds exactly when all three degrees equal two. In particular, for degrees \((2,2,d)\),
\[
T_{ijk}=d(d-2)(2d-3)\ge9\quad(d\ge3).
\]

**4. Classify the pair terms and finish.** Writing \(u=d_i-1\ge1\) and \(v=d_j-1\ge1\),
\[
Q_{ij}=2uv-u-v-1.
\]
It equals \(-1\) for degrees \((2,2)\), equals zero for \((2,3)\), and is strictly positive for every other unordered pair of degrees at least two. The last sum in (1) is nonnegative, and it is strictly positive when \(\ell>0\) and \(B>0\).

If every active degree equals two, let \(k=|I|\ge2\). All triple terms vanish and (1) becomes
\[
D/2=(\ell-1)\binom{k}2.
\]
Parity of \(M=2k+\ell\) forces \(\ell\) even. If \(\ell=0\), then \(D<0\); otherwise \(\ell\ge2\) and \(D>0\).

Now suppose some active vertex has degree at least three and \(B>0\). Fix such a vertex \(h\). Each negative pair term corresponds to two degree-two vertices \(i,j\), and the distinct triple \(\{i,j,h\}\) contributes at least nine, compensating that pair's \(-1\) contribution. Distinct negative pairs use distinct triples, while all other pair and triple contributions are nonnegative. Thus \(D>0\) if there is any degree-two pair. If there is no such pair, at least one pair exists because \(B>0\). Its \(Q\) is positive except possibly a unique active pair of degrees \((2,3)\). In that sole exception, \(M=5+\ell\) is even, so \(\ell\ge1\), and the last term in (1) is strictly positive. Hence \(D>0\) in every remaining case. Finally \(B=0\) means fewer than two vertices have degree at least two, so every \(X_{ij}\le1\) and \(P=0\) identically. This proves all cases.

**Regular-degree corollary.** For \(v=n\) vertices each of common degree \(d\ge2\), where \(nd\ge6\) is even,
\[
\operatorname{Cov}(L,P)
=\frac{n(n-1)d^2(d-1)^2\,[nd(2-d)+2d-3]}
{2(nd-1)^2(nd-3)(nd-5)}.
\]
It is positive at \(d=2\), asymptotic to \(1/(8n^2)\); it is negative for every \(d\ge3\), asymptotic for fixed \(d\) to \(-(d-1)^2(d-2)/(2dn)\).

## Verification

The companion `verify.py` independently enumerates every labeled half-edge pairing for 63 distinct nondecreasing positive degree profiles of total degree six, eight, or ten. It reconstructs \(L\) and \(P\) from each pairing, computes rational covariances, and compares them with the formula. It also checks the signed decomposition and classifications for 4,023 finite degree profiles and the regular corollary for 344 admissible parameter pairs. These finite checks test implementation and small boundaries; the symbolic conditioning and inequalities above, not enumeration, establish the unrestricted theorem. Run with Python 3 using `python verify.py`.

## Relationship to prior work

The configuration model, loop count, and unordered parallel-edge-pair count are standard. Janson (2006), particularly Section 7, studies simplicity and Poisson approximations to the combined defects. Angel, van der Hofstad and Holmgren (2016), equations (1.2) and (1.6), study **these same two random variables**, give their separate expectations, and prove asymptotic independent-Poisson behavior. Their Section 3, including equation (3.9), develops exact indicator-level overlap calculations for Poisson approximation. These preexisting formulas must not be confused with the asserted new contribution. The claim here is the **uniform finite-size covariance sign classification for every degree sequence**, especially its singular positive two-regular class and absence of any other zero or positive case. Its proof requires an explicit nonnegative degree-triple decomposition and a complete treatment of degree-one parity, beyond independent-Poisson asymptotics. The full texts inspected did not state this classification. Historical priority is not independently certified.

## Limitations

This result concerns uniform half-edge pairings, not uniformly sampled simple graphs, and the count \(P\) is the binomial pair count rather than \(\sum_{i<j}(X_{ij}-1)_+\). No statement is made for \(M=4\) or about covariances with the latter alternate statistic. Earlier factorial-moment methods or sources not available in full could imply the exact formula; the novelty assessment is limited to the specific complete sign classification and supporting structural inequality. An independent expert review has not yet been performed.

## References

- S. Janson, *The Probability That a Random Multigraph is Simple*, arXiv:math/0609802, first submitted 2006-09-28, especially Sections 1 and 7. https://arxiv.org/abs/math/0609802
- O. Angel, R. van der Hofstad, C. Holmgren, *Limit laws for self-loops and multiple edges in the configuration model*, arXiv:1603.07172, first submitted 2016-03-23, especially equations (1.2), (1.6), (3.9) and Section 4. https://arxiv.org/abs/1603.07172
- N. C. Wormald, *Models of Random Regular Graphs*, in *Surveys in Combinatorics, 1999*, 239–298 (1999). The available bibliographic abstract was checked but full text was not inspected. https://doi.org/10.1017/CBO9780511721335.010
