# Universal cross-part leaf-count repulsion in random complete multipartite spanning trees

## Finding
Let \(G=K_{a_1,\ldots,a_r}\) be a complete multipartite graph with \(r\ge2\) nonempty classes of sizes \(a_1,\ldots,a_r\), and let \(T\) be a uniformly chosen spanning tree. Let \(L_i\) count the leaves (degree-one vertices) of \(T\) in class \(i\). For any distinct classes \(i\ne j\), write \(n=\sum_k a_k\) and define
\[
p_i=\left(\frac{n-1}{n}\right)^{r-2}\prod_{k\ne i}\left(1-\frac1{n-a_k}\right)^{a_k-1},
\qquad
Q_{ij}=\left(1-\frac1{(n-1)^2}\right)^{r-2}
\prod_{k\notin\{i,j\}}\left(1-\frac1{(n-a_k-1)^2}\right)^{a_k-1}.
\]
**Theorem.** For every allowed finite choice of class sizes,
\[
\mathbb E L_i=a_i p_i,\qquad
\operatorname{Cov}(L_i,L_j)=a_i a_j p_i p_j(Q_{ij}-1).
\]
This covariance vanishes identically for \(r=2\) and is strictly negative for every \(r\ge3\), regardless of the class sizes.

For fixed \(r\ge3\), suppose each \(a_k/n\to\alpha_k>0\), with \(\sum_k\alpha_k=1\). Put \(S_i=\sum_{k\ne i}\alpha_k/(1-\alpha_k)\). Then
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(L_i,L_j)}{n}
=-\alpha_i\alpha_j e^{-S_i-S_j}
\sum_{k\notin\{i,j\}}\frac{\alpha_k}{(1-\alpha_k)^2}.
\]
As a concrete consequence, for equal class sizes \(a_k=m\), \(m\to\infty\),
\[
\lim_{m\to\infty}\frac{\operatorname{Cov}(L_i,L_j)}{m}
=-e^{-2}\frac{r-2}{(r-1)^2}.
\]

## Assumptions and scope
Every class is nonempty, the graph is labeled, and all spanning trees receive equal probability. Leaves have degree exactly one. The theorem covers any \(n\ge2\); products with exponent zero equal one, and an empty product equals one. At \(r=2\), the product defining \(Q_{ij}\) is empty and its first exponent vanishes, so \(Q_{ij}=1\) even for a two-vertex graph. A zero-base, zero-exponent factor is defined as one. For \(r\ge3\), every displayed denominator is strictly positive. The large-order limit fixes \(r\) and requires each limiting class proportion to be positive.

## Proof
For nonempty parts \(b_1,\ldots,b_s\) of total size \(N\), the complete-multipartite spanning-tree enumerator from the matrix-tree theorem is
\[
\tau(K_{b_1,\ldots,b_s})=N^{s-2}\prod_{h=1}^s (N-b_h)^{b_h-1}.
\]
The same product is valid when zero-size parts resulting from deletion are formally retained: a zero part contributes \(N^{-1}\) and reduces the prefactor's exponent by one. A disconnected remaining graph has \(\tau=0\); a single isolated remaining vertex has one spanning tree.

Fix a vertex \(u\) in class \(i\). To make it a leaf, choose its unique neighbor among the \(n-a_i\) vertices outside its own class and then choose a spanning tree on \(G-u\). Hence
\[
\Pr(u\text{ is a leaf})=(n-a_i)\frac{\tau(G-u)}{\tau(G)}=p_i.
\]
The displayed formula for \(p_i\) follows by substituting the tree enumerator and canceling factors. This remains valid for singleton classes; in a complete bipartite star, a center may have leaf probability zero.

Fix vertices \(u\) in class \(i\) and \(v\) in a different class \(j\). For \(n\ge3\), if both are leaves then they cannot be adjacent: their connecting edge would form a separate two-vertex component. Deleting both leaves therefore leaves a spanning tree on \(G-\{u,v\}\); each leaf must choose one neighbor in the remaining core. Those choice counts are \(n-a_i-1\) and \(n-a_j-1\), respectively. Thus
\[
\Pr(u,v\text{ are both leaves})
=(n-a_i-1)(n-a_j-1)\frac{\tau(G-\{u,v\})}{\tau(G)}=p_i p_j Q_{ij}.
\]
The identity remains correct if the core is disconnected (both sides zero). The \(n=2\) case is the deterministic single-edge tree, giving leaf probabilities one and covariance zero. Cancellation of the spanning-tree products yields the displayed \(Q_{ij}\). By exchangeability within each class and bilinearity, summing the covariances of individual leaf indicators gives \(\operatorname{Cov}(L_i,L_j)=a_i a_j p_i p_j(Q_{ij}-1)\).

For \(r=2\), \(Q_{ij}=1\). For \(r\ge3\), all \(p_i>0\) and the factor \((1-1/(n-1)^2)^{r-2}\) lies strictly between zero and one. Every remaining factor lies in \([0,1]\), so \(Q_{ij}<1\). This proves the exact sign classification.

For fixed \(r\) and positive limiting proportions, taking logarithms gives \(\log p_i\to-S_i\) and
\[
\log Q_{ij}=-\frac1n\sum_{k\notin\{i,j\}}\frac{\alpha_k}{(1-\alpha_k)^2}+o(n^{-1}).
\]
Consequently \(n(Q_{ij}-1)\) tends to minus the displayed sum, while \(a_i a_j/n^2\to\alpha_i\alpha_j\). Combining these proves the asymptotic formula. Substituting \(\alpha_k=1/r\) and \(n=rm\) yields the balanced-class corollary.

## Verification
The accompanying `verify.py` enumerates all admissible Prüfer-code trees for twenty small multipartite class-size configurations, computes one-vertex leaf probabilities, two-vertex joint leaf probabilities, and cross-class leaf-count covariance using exact rational arithmetic. It separately evaluates the formula and its sign on several thousand positive integer part-size configurations. Running `python3 verify.py` on the embedded file prints `VERIFY_OK trees=348528 assertions=22795 cases=20`. These finite checks are supplementary; the all-size assertions follow from the preceding deletion argument and matrix-tree identity.

## Relationship to prior work
Eğecioğlu and Remmel (1994) prove the complete-multipartite tree count, a weight-preserving bijection, and a single-vertex asymptotic leaf proportion (especially their Section 6 and Lemma 1). Remmel and Williamson (2002) develop more general multivariate degree-sensitive generating functions for these spanning trees (their Theorem 2.4 and Example 3.2). Their generating functions encode much finite degree information, making the present exact covariance recoverable in principle by specialization and coefficient extraction. The distinct-class zero-versus-strict-negative sign theorem and its limiting covariance coefficient are the explicit dependence conclusions assessed here; they are not stated in the inspected papers. Accordingly, the result does not assert a new spanning-tree counting method or novelty of the original enumerator.

## Limitations
The result concerns pairwise covariance of leaf counts across *different* classes. In the bipartite case, zero covariance does not by itself imply independence. No within-class leaf covariance, higher-order negative dependence, multivariate central limit theorem, or uniformity when the number of classes increases is claimed. General vertex-degree generating functions may imply the finite identities indirectly; independent historical-priority assessment has not been performed. The numerical checks cover only finite cases.

## References
Eğecioğlu, Ö., and Remmel, J. B., “A Bijection for Spanning Trees of Complete Multipartite Graphs,” *Congressus Numerantium* **100** (1994), 225–243. Full text: https://sites.cs.ucsb.edu/~omer/DOWNLOADABLE/multipartite94.pdf.

Remmel, J. B., and Williamson, S. G., “Spanning Trees and Function Classes,” *Electronic Journal of Combinatorics* **9** (2002), R34, publicly dated 2002-08-12. https://doi.org/10.37236/1650.
