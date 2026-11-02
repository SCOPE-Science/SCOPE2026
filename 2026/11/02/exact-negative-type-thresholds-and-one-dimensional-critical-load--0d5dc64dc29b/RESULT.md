# Exact negative-type thresholds and one-dimensional critical loads on two-level trees

## Finding
For integers \(k\ge2\) and \(m\ge1\), let \(T_{k,m}\) be the unit-edge rooted tree whose root has \(k\) children, each with exactly \(m\) leaves. Write \(\wp_{k,m}\) for the supremal exponent of negative type of its path metric, and define
\[
 a_p=2^p,\quad b_p=3^p,\quad c_p=4^p,\quad h_k=1+\log_2\frac{k}{k-1},
\]
\[
 U_p=k-\frac{k-1}{2}a_p,\qquad
 V_p=\frac{\sqrt m}{2}\left((k-1)+ka_p-(k-1)b_p\right),
\]
\[
 W_p=\frac{m+1}{2}a_p+(k-1)m\left(a_p-\frac{c_p}{2}\right),
 \qquad F_{k,m}(p)=U_pW_p-V_p^2.
\]
**Theorem.** Except for \((k,m)=(2,1)\), there is exactly one root \(\rho_{k,m}\) of \(F_{k,m}(p)=0\) in the open interval \((1,h_k)\), and
\[
 \boxed{\wp_{k,m}=\rho_{k,m}.}
\]
The metric has strict negative type for every \(0\le p<\rho_{k,m}\), non-strict negative type at \(p=\rho_{k,m}\), and fails negative type for every \(p>\rho_{k,m}\). At the critical exponent, the vector space of zero-sum equality loads has dimension exactly one; all its non-root coordinates are constant within the \(k\) intermediate vertices and, separately, within the \(km\) leaves. The minimal affine dimension of a Hilbert realization of the snowflaked metric \(d^{\rho_{k,m}/2}\) is \(k(m+1)-1\), one smaller than its value below the threshold. For the exceptional path \(T_{2,1}\), \(\wp_{2,1}=2\) and the critical Hilbert realization is one-dimensional.

At fixed \(k\) and increasing leaf number \(m\), the sharp rate is
\[
 \boxed{\rho_{k,m}=1+\frac{1}{m\,c_k}+O_k(m^{-2}),\qquad
 c_k=(5k-4)\log 2-3(k-1)\log 3
 =k\log(32/27)+\log(27/16)>0.}
\]
In particular, the endpoint has an explicit, nontrivial, dimension-dependent approach to one. The same exact root is the first exponent admitting a nontrivial polygonal equality on this finite tree.

## Assumptions and scope
All graph edges have length one; distance is the unique-path metric, not squared distance. A finite metric space \((X,d)\) has \(p\)-negative type when for every real vector \(\lambda\) with \(\sum_{x\in X}\lambda_x=0\),
\[
 \sum_{x,y\in X}\lambda_x\lambda_y d(x,y)^p\le0.
\]
It has strict negative type when equality is possible only for the zero vector. The snowflake \(d^{p/2}\) is the metric whose squared distances appear in Schoenberg's positive-semidefinite criterion. The Hilbert dimension is **affine** dimension (the dimension of the span of translated embedding points), not a claim about a prescribed ambient space.

The number of vertices is \(N=1+k(m+1)\). The theorem encompasses every pair of integer branching degrees in the stated range, including the one-leaf subdivision case, and does not assert a result for weighted or deeper trees.

## Proof
**1. Anchored Gram matrix.** Fix the root \(o\). For non-root vertices \(x,y\), form
\[
 K_p(x,y)=\tfrac12\big(d(o,x)^p+d(o,y)^p-d(x,y)^p\big).
\]
For every zero-sum load, writing \(\lambda_o=-\sum_{x\ne o}\lambda_x\) gives \(\sum\lambda_x\lambda_y d(x,y)^p=-2\lambda_{\ne o}^{\mathsf T}K_p\lambda_{\ne o}\). Thus negative type is equivalent to \(K_p\succeq0\). The distance values are among \(1,2,3,4\), so the following block calculation is exact, not numerical.

Within one branch, the hub coordinate has diagonal entry \(1\), each hub-to-leaf entry is \(a_p/2\), the leaf diagonal is \(a_p\), and distinct leaves have entry \(a_p/2\). Between distinct branches, the hub-to-hub entry is \(1-a_p/2\), a hub-to-leaf entry is \((1+a_p-b_p)/2\), and a leaf-to-leaf entry is \(a_p-c_p/2\).

Leaf differences within a given branch give \(k(m-1)\) eigenvectors of eigenvalue \(a_p/2>0\). On the remaining two coordinates per branch (the hub and normalized sum of its leaves), let \(A_p\) be the diagonal branch block and \(B_p\) the common interbranch block. Explicitly,
\[
 A_p=\begin{pmatrix}1&\sqrt m\,a_p/2\\\sqrt m\,a_p/2&(m+1)a_p/2\end{pmatrix},
\quad
 B_p=\begin{pmatrix}1-a_p/2&\sqrt m(1+a_p-b_p)/2\\\sqrt m(1+a_p-b_p)/2&m(a_p-c_p/2)\end{pmatrix}.
\]
Permutation of the branches splits this operator into a symmetric \(2\)-plane, with matrix \(G_p=A_p+(k-1)B_p=\left(\begin{smallmatrix}U_p&V_p\\V_p&W_p\end{smallmatrix}\right)\), and \(k-1\) copies of the difference block \(H_p=A_p-B_p\).

**2. Cross-branch negativity.** For \(1<p<2\), if two vertices have positive root depths \(s,t\), their cross-branch Gram entry is
\[
 \frac{s^p+t^p-(s+t)^p}{2}
 =-\frac{1}{2\Gamma(-p)}\int_0^\infty
 (1-e^{-su})(1-e^{-tu})u^{-1-p}\,du.
\]
The integral converges at zero and infinity, and \(\Gamma(-p)>0\). Hence \(B_p\preceq0\), and it is **negative definite** on the two-dimensional hub/leaf-mean plane because \(1-e^{-u}\) and \(1-e^{-2u}\) are linearly independent as functions of \(u>0\). At \(p=1\), \(B_p=0\); at \(p=2\), \(B_p\preceq0\) by the elementary identity \((s+t)^2-s^2-t^2=2st\). Thus, on \([1,2]\),
\[
 H_p=G_p-kB_p\succeq G_p.
\]
Consequently, \(K_p\succeq0\) if and only if \(G_p\succeq0\). This gives a two-by-two criterion despite an arbitrarily large tree. The same dominance argument applies to any tree obtained by attaching identical rooted branches at one root, for exponents from one to two; only the final matrix size changes.

**3. Existence and uniqueness of the root.** At \(p=1\), one has \(U_1=1\), \(V_1=\sqrt m\), \(W_1=m+1\), so \(F_{k,m}(1)=1\) and \(G_1\) is positive definite. For \(1\le p<h_k\), \(U_p>0\). Therefore \(G_p\succeq0\) is equivalent to \(F_{k,m}(p)\ge0\).

If \(k\ge3\), then \(h_k<2\), and at \(p=h_k\), \(U_p=0\) while \(V_p\ne0\). Indeed put \(z=k/(k-1)\in(1,2)\) and \(s=\log_2 3\). Then \(2V_{h_k}/((k-1)\sqrt m)=1+2z^2-3z^s\), which is strictly negative: \(3z^s-1-2z^2\) is strictly concave on \([1,2]\) and vanishes at both endpoints. Hence \(F_{k,m}(h_k)<0\).

If \(k=2\) and \(m>1\), then \(h_2=2\). At \(p=2\), \(U_2=V_2=0\), whereas \(W_2=2-2m<0\). Therefore \(F_{2,m}(p)<0\) for every \(p<2\) sufficiently close to two, because there \(U_p>0\) and \(W_p<0\). The intermediate-value theorem now produces an interior root in all nonexceptional cases. At any such root, \(U_p>0\), so \(G_p\) is positive semidefinite with rank one; hence \(K_p\succeq0\), but not strictly. If two interior roots existed, strict \(p\)-negative type at every exponent below a larger admissible exponent (Li–Weston) would contradict non-strictness at the smaller root. Thus the root is unique. By the negative-type interval property, it is the exact supremum and negative type fails above it.

**4. Critical equality and embedding dimension.** For an interior root \(1<p<2\), the cross-branch block is strictly negative definite, whence \(H_p=G_p-kB_p\) is strictly positive definite. Leaf-difference eigenvalues are also strictly positive. The sole kernel is therefore the one-dimensional kernel of \(G_p\), represented in symmetric normalized branch coordinates by \((V_p,-U_p)\). Its non-root load is constant on all intermediate vertices and separately constant on all leaves, and the root coefficient is determined by zero sum. Since the Gram rank is \(N-2\), the minimum affine Hilbert embedding dimension is \(N-2=k(m+1)-1\). Below the critical exponent, strict negative type gives Gram rank \(N-1\). The exceptional \(T_{2,1}\) is a five-vertex path, whose graph distance itself is Euclidean distance on an interval, giving critical exponent two and a one-dimensional realization.

**5. Sharp large-leaf asymptotic.** Direct differentiation of the displayed two-by-two determinant gives
\[
 F_{k,m}(1)=1,\qquad
 F'_{k,m}(1)=-m\big[(5k-4)\log2-3(k-1)\log3\big]-(k-2)\log2.
\]
For fixed \(k\), the determinant is affine in \(m\), and its coefficient has a simple zero at \(p=1\) with negative derivative \(-c_k\). Since \(c_k=k\log(32/27)+\log(27/16)>0\), the implicit-function theorem applied with \(1/m\) as parameter yields the stated expansion. Uniqueness identifies that local root with the global threshold.

## Verification
The analytical proof is self-contained modulo the standard finite negative-type interval and strictness theorems. A standalone supplementary checker is provided as `artifacts/check_numeric.py`; it independently constructs each tree's shortest-path distance matrix using breadth-first search and compares the full anchored Gram eigenvalues against the branch decomposition. It also checks critical kernel multiplicities and the leading asymptotic on a finite parameter grid. To replay, from the package root run `python artifacts/check_numeric.py` with Python 3, NumPy and SciPy installed. Its passing message is not an infinite proof.

For illustration, the critical exponent is approximately \(1.5271730883\) for \((k,m)=(2,2)\), \(1.4190934700\) for \((3,2)\), and \(1.3137003486\) for \((4,2)\). The first of these was already numerically reported in earlier tree-roundness literature; it is not separately claimed as new.

## Relationship to prior work
Doust and Weston (2024) prove a general theorem characterizing exponents admitting nontrivial polygonal equality for an arbitrary finite metric. The present result locates the first such exponent and its unique equality direction for a specific but infinite, naturally parameterized family. Caffarelli, Doust and Weston (2010/2011) study spherically symmetric trees, provide general bounds whose principal finite-tree theorem requires radius at least three, and tabulate a numerical approximation for the binary depth-two tree; their tables and general estimates are acknowledged prior coverage. Sánchez (2011) provides a general determinant/inverse-matrix criterion, not a reduced all-parameter formula, critical eigenvector classification or the sharp fixed-depth large-branching law. Li and Weston provide the strictness theorem used to establish uniqueness. None of the generic finite-metric criteria or already tabulated special values is claimed as new here.

## Limitations
This is an exact two-level, unweighted, finite-tree result, not a result for arbitrary edge lengths, irregular branch sizes, or greater depth. The expression for the threshold is an implicit, uniquely specified scalar root, not a claimed elementary closed form. Numeric checks cover only finite parameter samples and are supplementary. The comparison with published literature is subject to a residual historical-priority risk: an equivalent symmetry reduction may have been recorded under alternate terminology or in older literature not located by the checked searches. Independent mathematical validation has not been performed.

## References
- I. Doust and A. Weston, *Polygonal equalities and \(p\)-negative type*, arXiv:2404.06658v1 (first public 9 April 2024), sections 1–3. https://arxiv.org/abs/2404.06658
- E. Caffarelli, I. Doust, and A. Weston, *Metric trees of generalized roundness one*, arXiv:1008.3418, sections 1, 2 and 5. https://arxiv.org/abs/1008.3418
- S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451, section 2. https://arxiv.org/abs/1108.0451
- H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695, main strictness theorem. https://arxiv.org/abs/0901.0695
- L. Levy-Moore, M. Nichols, and A. Weston, *Comparing the generalised roundness of metric spaces*, arXiv:1608.03699 (first public 12 August 2016), comparison of generalized roundness and metric-tree embeddings. https://arxiv.org/abs/1608.03699
