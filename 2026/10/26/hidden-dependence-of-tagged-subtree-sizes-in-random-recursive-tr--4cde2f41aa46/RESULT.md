# Hidden dependence of tagged subtree sizes in random recursive trees

## Finding
Let \(T_n\) be a uniform random recursive tree on vertices \(1,\ldots,n\), where every new vertex independently chooses its parent uniformly from the earlier vertices. For \(1\le i<j\le n\), let \(S_i,S_j\) be the sizes, including their roots, of the descendant subtrees of vertices \(i,j\). Then
\[
\operatorname{Cov}(S_i,S_j)=0.
\]
For the nondegenerate range \(2\le i<j<n\), the variables are nevertheless dependent. Write \(A_{ij}\) for the event that \(j\) is a descendant of \(i\). Then \(\Pr(A_{ij})=1/i\), and the exact conditional covariances are
\[
\begin{aligned}
\operatorname{Cov}(S_i,S_j\mid A_{ij})
 &=\frac{n(n-j)(i-1)}{(i+1)j(j+1)}>0,\\
\operatorname{Cov}(S_i,S_j\mid A_{ij}^{\mathrm c})
 &=-\frac{n(n-j)}{(i+1)j(j+1)}<0.
\end{aligned}
\]
Their strict opposite signs cancel upon averaging with the ancestry probabilities; each event has the same conditional mean \(\mathbb E[S_j\mid A_{ij}]=\mathbb E[S_j\mid A_{ij}^{\mathrm c}]=n/j\). The only independent pairs occur when \(i=1\) or \(j=n\), for which one subtree size is deterministic.

## Assumptions and scope
An *increasing-parent recursive tree* is generated from root \(1\) by independent choices \(P_t\in\{1,\ldots,t-1\}\), each uniform, at arrivals \(t=2,\ldots,n\). Descendant subtrees include the marked vertex. Covariance is with respect to this uniform law. The strict conditional statements assume integers \(n\ge4\) and \(2\le i<j<n\); the unconditional zero statement applies to all \(n\ge2\) and \(i<j\). No assertion is made for differently weighted attachment trees.

## Proof
Set \(W=S_i(j-1)\), the size of the subtree rooted at \(i\) just before vertex \(j\) arrives. Since each new vertex enters that subtree with probability equal to its current size divided by the current total, \(W\) evolves as a two-color classical Pólya urn starting at time \(i\) with one member inside and \(i-1\) outside. Its first two rising-factorial moments are
\[
\mathbb E W=\frac{j-1}{i},\qquad
\mathbb E[W(W+1)]=\frac{2(j-1)j}{i(i+1)}.
\]
Vertex \(j\) attaches inside the \(i\)-subtree exactly on \(A_{ij}\), with conditional probability \(W/(j-1)\). Thus \(\Pr(A_{ij})=\mathbb EW/(j-1)=1/i\). Write \(Z=S_i(j)\), the size immediately after this arrival. Size biasing by \(W\) on \(A_{ij}\) gives
\[
\mathbb E[Z\mid A_{ij}]=\frac{2j}{i+1}.
\]
Since \(\mathbb E Z=j/i\), its complementary mean is
\[
\mathbb E[Z\mid A_{ij}^{\mathrm c}]=\frac{j}{i+1},\qquad i>1.
\]
After vertex \(j\) appears, partition the existing vertices into the \(j\)-subtree (size one), the other vertices in the \(i\)-subtree (size \(Z-1\) when \(A_{ij}\) occurs), and the remaining vertices (size \(j-Z\)). The \(n-j\) subsequent independent parent choices reinforce exactly these existing color classes. The resulting color counts have a Dirichlet-multinomial law. Given initial size vector of total \(j\) and \(m=n-j\) added vertices, its covariance formula for two distinct classes of initial sizes \(a,b\) is
\[
-\frac{nmab}{j^2(j+1)},
\]
while the variance of one class of initial size \(a\) is \(nma(j-a)/(j^2(j+1))\). Both follow directly from the two-draw urn probabilities or the Dirichlet mixture.

On \(A_{ij}\) the \(j\)-subtree sits inside the \(i\)-subtree. Since its initial size is one, the conditional covariance of their final sizes, given the tree through time \(j\), is
\[
\frac{n(n-j)(j-Z)}{j^2(j+1)}.
\]
On \(A_{ij}^{\mathrm c}\) the two subtrees are disjoint and the analogous conditional covariance is
\[
-\frac{n(n-j)Z}{j^2(j+1)}.
\]
In both cases \(\mathbb E[S_j\mid T_j]=n/j\) is deterministic. Consequently the covariance of conditional means contributes zero even after restricting to either ancestry event. Averaging the preceding expressions using the two conditional means of \(Z\) proves both conditional covariance identities.

The law of total covariance over \(A_{ij}\), together with the identical conditional means \(n/j\) of \(S_j\), now gives
\[
\operatorname{Cov}(S_i,S_j)=\frac1i\frac{n(n-j)(i-1)}{(i+1)j(j+1)}
+\frac{i-1}{i}\left(-\frac{n(n-j)}{(i+1)j(j+1)}\right)=0.
\]
The trivial boundary cases \(i=1\) or \(j=n\) also have zero covariance because \(S_1=n\) and \(S_n=1\).

To show genuine dependence in the interior, consider \(H_i=\{S_i=n-i+1\}\), which has positive probability and means that every vertex arriving after \(i\) joins the \(i\)-subtree. Conditional on this event, the successive parent choices within labels \(i,\ldots,n\) form a uniform recursive tree on that interval. Therefore
\[
\mathbb E[S_j\mid H_i]=\frac{n-i+1}{j-i+1}
=\frac nj+\frac{(i-1)(n-j)}{j(j-i+1)}>\frac nj
\]
for \(2\le i<j<n\), whereas \(\mathbb ES_j=n/j\). This disproves independence. The boundary cases are independent because one variable is constant.

## Verification
The accompanying standard-library Python program exhaustively enumerates all \((n-1)!\) increasing-parent recursive trees for each \(3\le n\le9\), and checks ancestry probabilities, conditional covariance formulas, unconditional orthogonality, strict signs, and the conditional expectation witnessing dependence for every admissible labeled pair. Its run completed 1,022 exact rational assertions. These finite tests are independent checks, not a proof of the universal statements.

## Relationship to prior work
The independent-parent construction and urn method are classical. Janson (2004) treats recursive-tree degree statistics with generalized Pólya urns, not joint sizes of two fixed descendant subtrees. Kuba (2006, Chapter 5.3.3) supplies a general formal multivariate generating-function framework for parameters at several fixed nodes, and Chapter 5.4 establishes individual tagged-subtree size distributions. The inspected sections do not evaluate the present ancestry-conditioned pair covariance formulas or classify their cancellation and dependence. The multivariate framework is a substantive broader-method prior: possible implicit derivability and unlocated earlier explicit formulas remain originality risks. The claim here is the evaluated sign and independence classification, not the underlying urn identities or the general multivariate generating-function setup.

## Limitations
This concerns a fixed pair of labels under uniform recursive attachment. It does not establish independence for distinct nontrivial subtree sizes—indeed it disproves it. Pairwise zero covariance does not imply joint independence or describe the complete joint distribution. The historical priority of the explicit evaluated identities is not independently certified; in particular, an equivalent expression could be extracted from older multivariate recursion work. No external independent audit has been performed.

## References
1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83; first public online date November 16, 2004. DOI: 10.1002/rsa.20046.
2. M. Kuba, *Analysis of node isolation procedures and label-based parameters in tree structures*, doctoral thesis, Vienna University of Technology (2006), Chapter 5, especially §§5.3.3–5.4. Stable repository identifier: https://repositum.tuwien.at/handle/20.500.12708/10168.
