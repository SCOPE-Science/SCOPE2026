# Arbitrarily many leaf moments conceal a recursive-tree subtree split

## Finding
Let \(T_n\), \(n\ge3\), be a uniform random recursive tree with vertex \(j\) choosing its parent uniformly from \(\{1,\ldots,j-1\}\). Let \(S_n\) be the number of descendants of vertex \(2\), **including vertex 2**, and let \(L_n\) be the total number of leaves (vertices of outdegree zero) of the **whole** tree. Write \(X_m\) for the leaf count of an independent uniform recursive tree with \(m\) vertices; set \(X_1=1\).

**Exact conditional decomposition.** \(S_n\) is uniform on \(\{1,\ldots,n-1\}\). For each \(1\le s\le n-1\), with mutually independent copies of \(X_s\) and \(X_{n-s}\),
\[
 \mathcal L(L_n\mid S_n=s)
 =\mathcal L\bigl(X_s+X_{n-s}-\mathbf 1_{\{n-s=1\}}\bigr).
\]

**Moment camouflage, with a strict distributional difference.** If \(2\le s\le n-2\), then, for every integer \(0\le r<\min(s,n-s)\),
\[
 \mathbb E[L_n^r\mid S_n=s]=\mathbb E[L_n^r],
\]
yet \(\mathcal L(L_n\mid S_n=s)\ne\mathcal L(L_n)\). Consequently, for each prescribed positive moment order \(r\), sufficiently large trees admit an interior conditioned subtree size for which the first \(r\) moments match the unconditional law exactly although the laws differ.

**Boundary-controlled covariance.** For every \(n\ge3\),
\[
 \mathbb E[L_n\mid S_n=s]=
 \begin{cases}
 (n+1)/2,&s=1,\\
 n/2,&2\le s\le n-2,\\
 (n-1)/2,&s=n-1,
 \end{cases}
 \qquad
 \operatorname{Cov}(S_n,L_n)=-\frac{n-2}{2(n-1)}.
\]
The middle case is empty when \(n=3\).

## Assumptions and scope
The parent choices for all vertices \(2,\ldots,n\) are mutually independent and uniform over preceding labels. All leaves are counted, including vertex \(1\) if it has no children. The descendant subtree at vertex \(2\) includes that vertex. The statement concerns unconditional and conditional **finite** distributions for every indicated integer size; there is no asymptotic approximation. The moment order is any nonnegative integer strictly smaller than both component sizes.

## Proof
**1. The split and independence.** Every vertex \(j\ge3\) joins either the descendants of vertex \(2\) (red) or the complement containing vertex \(1\) (blue). Initially both classes have size one. Given the past, its parent is uniformly selected, so the next colour is red with probability \(R/(R+B)\) and blue otherwise. This is the balanced two-colour Pólya urn; its red count after \(n-2\) draws is uniform on \(\{1,\ldots,n-1\}\). Explicitly, any prescribed red/blue word containing \(s-1\) reds has probability \((s-1)!(n-s-1)!/(n-1)!\), and there are \(\binom{n-2}{s-1}\) such words, giving probability \(1/(n-1)\).

Conditional on any colour word, the parent chosen inside the selected colour is independent and uniform over preceding members of that colour. Hence the induced red and blue parent systems are independent uniform recursive trees on their respective arrival ranks, with leaf counts \(X_s\) and \(X_{n-s}\). The red root \(2\) attaches to blue root \(1\). This extra edge changes a leaf of the induced blue tree precisely when the blue tree consists only of root \(1\). Therefore the total number of leaves is the claimed independent sum minus the boundary indicator. This conditional distribution is independent of the specific colour word, so conditioning on its red count gives the same formula.

**2. Eulerian and cyclic-descent representation.** When a recursive tree of size \(m\) has \(k\) leaves, its \((m+1)\)th vertex attaches to a leaf with probability \(k/m\), preserving \(k\) leaves; otherwise the leaf count becomes \(k+1\). This is the Eulerian insertion recurrence, showing \(X_m\overset d=1+D_{m-1}\) for \(m\ge2\), where \(D_{m-1}\) is the number of descents in a uniform permutation of length \(m-1\).

Take \(m\) independent continuous random variables \(U_1,\ldots,U_m\) and count **cyclic** descents,
\[
 C_m=\sum_{i=1}^{m}\mathbf1_{\{U_i>U_{i+1}\}},\qquad U_{m+1}=U_1.
\]
Rotating the cyclic list so its unique maximum appears at the end exhibits one guaranteed descent from that maximum to the first term and a uniformly random ordinary permutation of the other \(m-1\) ranks. Thus \(X_m\overset d=C_m\) for every \(m\ge2\).

**3. Exact finite-order cumulant linearity.** Fix a positive integer \(r\). For \(m>r\), the \(r\)th joint-cumulant expansion of the cyclic sum \(C_m\) is a sum over ordered \(r\)-tuples of edge indicators. A joint cumulant vanishes whenever its indicators can be partitioned into nonempty independent groups. Indicators depend only on their two endpoint \(U\)'s; thus nonzero terms must be supported on a connected set of at most \(r\) edges in the cycle of \(m\) vertices. Since \(r<m\), that support is a **proper path**, whose joint comparison distribution equals that of the corresponding consecutive edges on the infinite line. Translation around the cycle gives exactly \(m\) translates of every anchored connected pattern, with pattern cumulant independent of \(m\). Consequently there is a constant \(c_r\), depending only on \(r\), such that
\[
 \kappa_r(X_m)=\kappa_r(C_m)=m c_r \quad\text{for every }m>r.
\]
The argument also covers repeated indices in the joint-cumulant tuple; they do not enlarge its edge support. By independence, for \(r<\min(s,n-s)\), the cumulants of \(X_s+X_{n-s}\) add and give \(s c_r+(n-s)c_r=n c_r=\kappa_r(X_n)\). Equality for orders \(1,\ldots,r\) implies equality of all raw moments up to order \(r\). The order-zero identity is normalization. The boundary correction vanishes for interior \(s\), proving the claim.

**4. The distributions are nevertheless different.** For interior \(s\), both independent component trees have at least one leaf, so \(\Pr(L_n=1\mid S_n=s)=0\). A recursive tree has just one leaf precisely if it is the unique directed chain \(1\to2\to\cdots\to n\). It therefore has positive probability \(\Pr(L_n=1)=1/(n-1)!\). This proves the strict distributional difference for every interior split.

**5. Covariance.** The leaf recursion gives \(\mathbb EX_m=m/2\) for \(m\ge2\), while \(X_1=1\). Apply these means to the conditional decomposition to get the displayed piecewise conditional expectation. Uniformity of \(S_n\) and the deviations \(+1/2\) at \(s=1\) and \(-1/2\) at \(s=n-1\) give
\[
 \operatorname{Cov}(S_n,L_n)=\frac1{n-1}\left[\frac12\left(1-\frac n2\right)-\frac12\left(n-1-\frac n2\right)\right]
 =-\frac{n-2}{2(n-1)}.
\]

## Verification
The attached standalone program `verification/check.py` exhaustively constructs all \(46{,}232\) recursive trees of sizes \(3\) through \(9\) from independent parent choices, computes each subtree size and whole-tree leaf count directly, and checks the exact conditional convolutions, support separation, moment equalities, uniform subtree-size laws, unconditional leaf laws, and covariance formulas. It passed \(202\) exact-rational assertions. This finite enumeration checks representative instances; the preceding combinatorial and cumulant arguments prove the unrestricted statements.

## Relationship to prior work
The recursive-tree construction, Pólya urn subtree-size description, Eulerian leaf distribution, and split-tree representation are established methods, not proposed as new. Janson (2017/2018) identifies recursive trees as random split trees and analyzes tree shape and ancestry. Mahmoud and Smythe (1991) derive distributions for **leaves within** fixed-label rooted subtrees jointly with subtree size; this differs from **whole-tree** leaf counts conditioned on the subtree size. The proposed claim is the complete global-leaf conditional decomposition together with arbitrary-order but strictly non-distributional moment matching. Earlier subtree/leaf generating functions may yield implicit equivalences; the original 1991 full text was not accessible for exhaustive comparison.

## Limitations
The exact statement is confined to uniform random recursive trees and the subtree rooted at vertex \(2\). The moment-matching range is strictly below both component sizes; no claim of identical conditional and marginal distributions is made. The root boundary correction is essential. The observed equality of finite moments does not imply full independence of subtree size and leaf count; indeed their covariance is nonzero. Independent validation and a complete historical-priority assessment have not been performed.

## References
1. S. Janson, *Random recursive trees and preferential attachment trees are random split trees*, arXiv:1706.05487, first posted 2017-06-17; *Combinatorics, Probability and Computing* 28 (2019), 81–99. https://arxiv.org/abs/1706.05487 .
2. H. M. Mahmoud and R. T. Smythe, *On the Distribution of Leaves in Rooted Subtrees of Recursive Trees*, *Annals of Applied Probability* 1 (1991), 406–418. https://doi.org/10.1214/aoap/1177005874 .
