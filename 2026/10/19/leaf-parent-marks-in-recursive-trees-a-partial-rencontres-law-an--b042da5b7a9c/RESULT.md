# Leaf-parent marks in recursive trees: a partial-rencontres law and asymptotically independent Poisson ages

## Finding
Let \(T_n\) be a uniformly random recursive tree on ordered birth labels \(1,\ldots,n\), where \(n\ge2\). Define the **leaf-parent mark**
\[
E_{j,i}=\mathbf1\{\operatorname{parent}(i)=j,\ i\text{ is a leaf of }T_n\},\qquad 1\le j<i\le n,
\]
and \(Y_j=\sum_{i=j+1}^{n}E_{j,i}\), the number of final leaves directly attached to vertex \(j\).

**Complete cylinder law.** For any \(r\) distinct labels \(i_1,\ldots,i_r\in\{2,\ldots,n\}\), and prescribed parent labels \(1\le j_s<i_s\),
\[
\Pr\{E_{j_1,i_1}=\cdots=E_{j_r,i_r}=1\}
=\begin{cases}
\displaystyle\frac{(n-r-1)!}{(n-1)!},
&\{j_1,\ldots,j_r\}\cap\{i_1,\ldots,i_r\}=\varnothing,\\[6pt]
0,&\text{otherwise}.
\end{cases}
\]
Here \(1\le r\le n-1\); mutually incompatible demands involving a child with different prescribed parents also have probability zero.

**Partial-rencontres identity.** For each \(1\le j\le n\), the binary vector \((E_{j,i}:j<i\le n)\) has exactly the joint distribution of fixed-point indicators \((\mathbf1\{\sigma(k)=k\}:j\le k\le n-1)\), where \(\sigma\) is a uniform permutation of \(1,\ldots,n-1\). Therefore
\[
\mathbb E z^{Y_j}=\sum_{r=0}^{n-j}\binom{n-j}{r}\frac{(z-1)^r}{(n-1)_{\underline r}},
\qquad \mathbb EY_j=\frac{n-j}{n-1},
\]
with \((m)_{\underline0}=1\) and \((m)_{\underline r}=m(m-1)\cdots(m-r+1)\).

**Inter-parent dependence.** For \(n\ge3\) and \(1\le j<k\le n\),
\[
\boxed{\operatorname{Cov}(Y_j,Y_k)=-\frac{(n-k)(n+j-2)}{(n-1)^2(n-2)}.}
\]
It is strictly negative for \(k<n\); the final vertex has \(Y_n=0\). In contrast, distinct admissible marks from the same parent have positive covariance \(1/((n-1)^2(n-2))\).

**Asymptotic joint law.** For each fixed \(d\ge1\), choose distinct parent indices \(j_{1,n},\ldots,j_{d,n}\in\{1,\ldots,n\}\) with \(j_{s,n}/n\to u_s\in[0,1]\). Then
\[
(Y_{j_{1,n}},\ldots,Y_{j_{d,n}})\ \Rightarrow\ (Z_1,\ldots,Z_d),
\qquad Z_s\ \text{independent, }\ Z_s\sim\operatorname{Poisson}(1-u_s).
\]

**Age-resolved protection.** A vertex is protected when it is nonleaf and has no direct leaf child. For every \(1\le j\le n\), its probability is exactly
\[
\boxed{p_{n,j}=\sum_{r=0}^{n-j}(-1)^r\binom{n-j}{r}\frac1{(n-1)_{\underline r}}-\frac{j-1}{n-1}.}
\]
If \(j/n\to u\in[0,1]\), then \(p_{n,j}\to e^{u-1}-u\). For \(n\ge3\), \(p_{n,1}>\cdots>p_{n,n-1}=p_{n,n}=0\). The root-only and aggregate protected-node formulas are established in earlier literature and are not claimed as new.

## Assumptions and scope
The model is the standard increasing-label recursive tree: for each \(i=2,\ldots,n\), its parent is independently uniform in \(\{1,\ldots,i-1\}\). Thus all \((n-1)!\) such trees are equally likely. A leaf has no children; the root is not a leaf for \(n\ge2\). Every limit holds along arbitrary sequences satisfying the stated index-ratio hypotheses. The new finite-size cylinder law applies to all admissible parent-child assignments, not only a fixed number of marks; Poisson convergence holds for fixed vector dimension only.

## Proof
**1. Exact leaf-parent cylinders.** Take a set \(S=\{i_1,\ldots,i_r\}\) of prescribed marked leaves and parent map \(i_s\mapsto j_s\). If some \(j_s\in S\), the mark conditions are impossible, as a leaf cannot be a parent. Otherwise delete the vertices in \(S\) and their incident edges. Precisely because they are leaves, the remaining tree is a recursive tree on the remaining \(n-r\) ordered labels. Conversely any such recursive tree extends uniquely by reattaching each \(i_s\) to its prescribed earlier surviving vertex \(j_s\); all the marked vertices remain leaves. The remaining labels need not be consecutive, but their increasing-tree count is \((n-r-1)!\). Dividing by the full count \((n-1)!\) proves the formula, including \(r=n-1\).

**2. Fixed-point identity and moments.** For a fixed parent \(j\), every subset of \(r\) distinct potential child indices \(i>j\) is compatible because the designated parent is not among them. Its mark-intersection probability is \(1/(n-1)_{\underline r}\). A uniform permutation of size \(n-1\) fixes any prescribed \(r\) indices with precisely the same probability. Inclusion-exclusion recovers the entire binary vector distribution from its intersection probabilities. Expanding \(\prod_{i>j}(1+(z-1)E_{j,i})\) gives the polynomial probability-generating function. Also, for \(n\ge3\), \(\mathbb E(Y_j)_{\underline 2}=(n-j)(n-j-1)/((n-1)(n-2))\).

**3. Dependence across parents.** For \(j<k\), a possible mark for parent \(j\) is \((j,i)\) with \(i>j\), while one for parent \(k\) is \((k,h)\) with \(h>k\). A pair is compatible precisely when \(i\ne h\) and \(i\ne k\). Thus there are \((n-k)(n-j-2)\) compatible ordered pairs. Each has probability \(1/((n-1)(n-2))\), giving
\[
\mathbb EY_jY_k=\frac{(n-k)(n-j-2)}{(n-1)(n-2)}.
\]
Subtracting \((n-j)(n-k)/(n-1)^2\) yields the displayed covariance. For two distinct children of the same parent, the joint mark probability is \(1/((n-1)(n-2))\) and both marginals are \(1/(n-1)\), proving the positive same-parent covariance. The case \(n=2\) contains no two nonconstant parent counts.

**4. Joint Poisson limit.** Fix integers \(r_1,\ldots,r_d\ge0\), put \(r=\sum r_s\), and expand \(\mathbb E\prod_s(Y_{j_{s,n}})_{\underline{r_s}}\) into ordered collections of marked child assignments. Those with any repeated child label or any selected child equal to a selected parent label contribute zero. The total number of compatible collections is
\[
\prod_{s=1}^{d}(n-j_{s,n})^{r_s}+O_{r,d}(n^{r-1}),
\]
because excluding one of finitely many collisions or parent labels eliminates at least one free choice. Every compatible collection contributes \(1/(n-1)_{\underline r}\). Consequently the mixed factorial moments converge to \(\prod_s(1-u_s)^{r_s}\), also when some \(u_s=1\). Ordinary mixed moments follow from Stirling-number conversion, and the product-Poisson distribution is moment-determinate (its joint moment generating function is finite everywhere). Hence the claimed joint weak convergence.

**5. Protected vertex law and age profile.** Under the fixed-point identity, the probability of no leaf child at \(j\) equals the alternating sum above. A vertex with no children is automatically in this event, and its leaf probability is
\[
\prod_{t=j+1}^{n}\left(1-\frac1{t-1}\right)=\frac{j-1}{n-1},
\]
including the root boundary \(j=1\). Subtracting gives \(p_{n,j}\). For fixed \(r\), \(\binom{n-j}{r}/(n-1)_{\underline r}\to(1-u)^r/r!\), and its magnitude is at most \(1/r!\); dominated convergence yields \(e^{u-1}-u\). Finally the partial-fixed-point representation shows that deleting one constrained coordinate increases the no-fixed-point probability by at most \(1/(n-1)\). The difference \(p_{n,j}-p_{n,j+1}\) equals the probability that this coordinate is fixed together with at least one other constrained coordinate, strictly positive for \(j\le n-2\), and zero for \(j=n-1\). This gives the finite-size ordering.

## Verification
The standalone script `verification/verify_leaf_parents.py` uses exact rational arithmetic and enumerates every uniform recursive tree for \(2\le n\le8\). It verifies marked-leaf cylinders through three prescribed marks, the complete same-parent indicator-field distribution against permutation fixed points, every vertex's protected probability, and every inter-parent covariance. Running it produced `TOTAL_EXACT_ASSERTIONS 6196`. Its finite enumeration checks examples and boundaries; the counting and moment arguments above prove the universal statements.

## Relationship to prior work
Devroye and Janson (2013 arXiv preprint, 2014 journal publication) derive a Poisson number of leaf children for the root of a limiting random fringe tree and determine protected-node proportions. This is a scalar asymptotic precursor, not a birth-label-resolved joint law. Mahmoud and Ward (2015) obtain an exact expectation for the total protected-node count and an exact root-protection probability. The root case of the displayed formula is the classical derangement probability \(D_{n-1}/(n-1)!\); summing the displayed protected-node probabilities reproduces Mahmoud and Ward's exact expectation \(n(1/2-\sum_{r=0}^{n}(-1)^r/r!)\). Neither root formula nor aggregate mean is new here. The contribution being assessed is the complete *labeled leaf-parent mark* law and its cross-parent dependence, joint Poisson limit, and all-label age-resolved protection probabilities. Earlier work on leaves in rooted descendant subtrees studies a different (descendant-level rather than direct-child) quantity; the full historic source is a residual comparison risk.

## Limitations
The theorem concerns only the independent-uniform recursive-tree growth model. The asymptotic joint independence is for a fixed number of parents and does not state independence of the full growing-dimensional vector. Existing root and total-protection identities are excluded from the originality claim. Although relevant primary sources were materially inspected, older incomplete-access sources or general enumerative identities could implicitly cover some consequences; independent historical priority confirmation is outstanding. The tests do not certify infinite claims independently.

## References
- L. Devroye and S. Janson, *Protected nodes and fringe subtrees in some random trees*, arXiv:1310.0665v1 (first public 2013-10-02); *Electronic Communications in Probability* **19** (2014), article 6, doi:10.1214/ECP.v19-3048. Section 7 concerns random recursive trees.
- H. M. Mahmoud and M. D. Ward, *Asymptotic properties of protected nodes in random recursive trees*, *Journal of Applied Probability* **52** (2015), 290–297, doi:10.1239/jap/1429282623. Theorem 2.1 and equation (2.4) contain the earlier total and root formulas.
- H. M. Mahmoud and R. T. Smythe, *On the distribution of leaves in rooted subtrees of recursive trees*, *Annals of Applied Probability* **1** (1991), 406–418, doi:10.1214/aoap/1177005874 (historical comparison with incomplete full-text access).
