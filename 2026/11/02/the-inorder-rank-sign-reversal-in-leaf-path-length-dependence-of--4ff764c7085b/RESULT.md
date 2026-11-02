# The inorder-rank sign reversal in leaf–path-length dependence of random binary search trees

## Finding
For a random binary search tree on \(n\ge2\) ordered keys, let \(I_{n,r}\) be the indicator that the key at inorder rank \(r\) is a leaf (no children), and let \(P_n\) be total internal path length, meaning the sum of all root-to-key edge distances. The exact finite-size covariance profile is
\[
\operatorname{Cov}(I_{n,r},P_n)=
\begin{cases}
-\dfrac{n-2}{2n},&r\in\{1,n\},\\[5pt]
-\dfrac19+\dfrac{2}{3r(r+1)}+\dfrac{2}{3(n-r+1)(n-r+2)},&2\le r\le n-1.
\end{cases}
\]
For every \(n\ge6\), it is **positive only for the two near-endpoint ranks** \(r=2,n-1\), and **negative** for the endpoints and all deeper interior ranks. The central rank at \((n,r)=(5,3)\) has zero covariance. At \(n=3\) the middle rank is positive; at \(n=4\) both middle ranks are positive. Summing over all ranks, with \(L_n=\sum_{r=1}^n I_{n,r}\), yields
\[
\operatorname{Cov}(L_n,P_n)=-\frac{(n-2)(n+3)}{9n}.
\]

## Assumptions and scope
Take every one of the \(n!\) insertion orders of distinct ordered keys \(1,\ldots,n\) with equal probability, and construct the usual unbalanced binary search tree. A key is a leaf if neither its left nor its right child exists. The root has depth zero; there is no edge weight or depth offset. The formulas hold for every integer \(n\ge2\) and every rank \(1\le r\le n\), not merely asymptotically. The only randomness is the insertion permutation. No assertion is made for duplicate keys or other tree laws.

## Proof
Attach independent uniform priorities \(U_1,\ldots,U_n\) to the keys; their increasing order is a uniform insertion order. The resulting BST is the Cartesian tree on those priorities. A key \(r\) has a left child exactly when it precedes its immediate left neighbor \(r-1\) in insertion, and similarly on the right; equivalently, it is a leaf precisely when \(U_r\) exceeds each existing immediate neighboring priority. This standard Cartesian-tree characterization also follows from the nearest-smaller-priority ancestor description. For \(2\le r\le n-1\), write \(a=r-1\), \(b=r+1\), and \(E_r=\{U_r>U_a,U_b\}\); then \(\Pr(E_r)=1/3\). At either endpoint, the analogous event has probability \(1/2\).

For \(1\le i<j\le n\), let \(A_{ij}\) indicate that the two keys become ancestor and descendant. The Cartesian-tree minimum property gives
\[
A_{ij}=\mathbf1\!\left\{\mathop{\rm argmin}_{i\le k\le j}U_k\in\{i,j\}\right\},\qquad
\mathbb E A_{ij}=\frac{2}{j-i+1},\qquad
P_n=\sum_{i<j}A_{ij}.
\]
Indeed, the first priority in a rank interval separates the two keys unless it belongs to an endpoint; every ancestor–descendant pair contributes one unit to internal path length.

Fix an interior rank \(r\) and set \(k=j-i+1\). Conditioned on \(E_r\), each neighboring priority \(U_a,U_b\) has density \(3(1-u^2)/2\), and the smaller of the two neighbors has density \(3(1-u)^2\). Integrating the probability that an interval endpoint is the minimum against these beta-polynomial densities gives the following complete list of nonzero conditional shifts \(\delta_{ij}=\mathbb P(A_{ij}\mid E_r)-2/k\):

* If the interval contains exactly one of \(a,b\) but not \(r\), that neighbor must be the interval endpoint; the shift is \(d_a(k)=(k-2)(k+4)/(2k(k+1)(k+2))\), with \(k\ge2\).
* If it contains exactly \(a,r\) or exactly \(r,b\), the endpoint at \(r\) gives \(d_b(k)=-(2k+1)/(2k(k+1))\), with \(k\ge3\); for \(k=2\) the shift is zero.
* If it contains all three \(a,r,b\), has length at least four, and exactly one interval endpoint is \(a\) or \(b\), its shift is \(1/(2k)\). The minimal interval \([a,b]\), of length three, has shift \(1/3\).
* Every other interval has zero shift: it is either disjoint from the influenced priorities or has two endpoints outside the triple.

The first bullet follows, for example, from the marginal neighbor density by integrating against the minimum of the other \(k-1\) uniforms. For the second, the forced rank \(r\) cannot be the minimum; conditioning on the neighbors' order gives the displayed beta integral. For the third, when all three affected priorities are present, the minimum belongs to \(a\) and \(b\) with total probability \(3/k\), equally between them, while an unaffected endpoint is minimum with probability \(1/k\). These statements are exact probability identities, not asymptotic approximations.

Collect the one-sided shifts at a side of length \(\ell\ge1\):
\[
 B(\ell)=\sum_{k=2}^{\ell}d_a(k)+\sum_{k=3}^{\ell+1}d_b(k)+\sum_{k=4}^{\ell+2}\frac{1}{2k}
 =-\frac13+\frac{2}{(\ell+1)(\ell+2)}.
\]
Empty sums are zero. The equality follows directly by partial fractions, or by subtracting the two expressions at consecutive integers and checking \(B(1)=0\). Taking left length \(r-1\), right length \(n-r\), and accounting for \([a,b]\) once, gives
\[
\sum_{i<j}\delta_{ij}=\frac13+B(r-1)+B(n-r).
\]
Multiplication by \(\Pr(E_r)=1/3\) proves the displayed interior covariance formula.

For the endpoint rank \(r=1\), the leaf event is \(U_1>U_2\), of probability \(1/2\). The only nonzero shifts occur on intervals \([1,j]\) with \(j\ge3\), shift \(-1/j\), and \([2,j]\) with \(j\ge3\), shift \((j-3)/((j-1)j)\). These are immediate beta integrals for \(U_2\mid U_1>U_2\), whose density is \(2(1-u)\). Their sum telescopes to \(-1+2/n\), so \(\operatorname{Cov}(I_{n,1},P_n)=-(n-2)/(2n)\). Reflection handles \(r=n\).

For the sign claim with \(n\ge6\), rank two gives \(-1/9+1/9+2/(3n(n-1))>0\), and reflection gives rank \(n-1\). At every other nonendpoint rank the two positive fractions are each at most \(1/18\), so the covariance is nonpositive; equality would require both denominators to be twelve, which forces \(n=5,r=3\), excluded here. Endpoints are strictly negative. Finally, summation over ranks (using telescoping reciprocal products) gives \(\operatorname{Cov}(L_n,P_n)=-(n-2)(n+3)/(9n)\). This completes the all-size proof.

## Verification
The accompanying `verify.py` enumerates **all insertion permutations** through eight keys, constructs BSTs directly, and compares the rank-specific covariances as exact rational numbers. An independent bivariate BST root-split recurrence checks the total covariance through 120 keys. Further exact arithmetic checks the partial-fraction identity for 99 one-sided lengths and the phase statement for all valid ranks below 200 keys. It reports 20,159 successful assertions. The proof above is the basis for the infinite claim: finite enumeration alone cannot establish it.

Run with Python 3 using `python verify.py`; no third-party packages or data files are needed.

## Relationship to prior work
Bóna and Pittel's *On a random search tree: asymptotic enumeration of vertices by distance from leaves* (arXiv:1412.2796, first publicly posted 2014-12-08) treats random-BST leaf geometry, but their use of “rank” refers to distance from a leaf rather than the numerical inorder key. Chern, Fuchs, Hwang and Neininger's *Dependence and phase changes in random m-ary search trees* analyzes joint subtree counts and path length, notably asymptotic global dependence for binary search trees; it does not supply the present finite-sample **inorder-rank-resolved** local covariance or its sign reversal in the inspected theorem and discussions. Neininger and Straub's article studies joint statistics of specified node types, not this path-length/rank-resolved pair. No claim of absolute historical uniqueness is made.

## Limitations
The identity covers independent continuous insertion priorities (equivalently uniform permutations), without balancing or ties. A fixed key's leaf event is a local property; the result is a covariance, not a statement of stochastic monotonicity or causal influence. The global covariance is an algebraic corollary of the local profile and should not be confused with independence. Earlier full papers and specialized literature may contain equivalent statements that remain unidentified. There has been no independent audit or independent validation.

## References
1. M. Bóna and B. Pittel, *On a random search tree: asymptotic enumeration of vertices by distance from leaves*, arXiv:1412.2796 (first posted 2014-12-08), https://arxiv.org/abs/1412.2796 .
2. H.-H. Chern, M. Fuchs, H.-K. Hwang, and R. Neininger, *Dependence and phase changes in random m-ary search trees*, preprint dated 2016-01-30. https://arxiv.org/search/?query=Dependence+and+phase+changes+in+random+m-ary+search+trees&searchtype=all .
3. R. Neininger and J. Straub, *Convergence Rates in the Probabilistic Analysis of Algorithms*, published 2020. Relevant node-type joint covariance discussion, Section 4.4.
