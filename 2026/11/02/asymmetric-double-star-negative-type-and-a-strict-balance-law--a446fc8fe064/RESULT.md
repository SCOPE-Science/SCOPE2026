# Asymmetric double-star negative type and a strict balance law

## Finding

For every pair of integers \(m,n\ge2\), the unweighted double-star tree \(D_{m,n}\) has a completely determined supremal \(p\)-negative-type exponent \(\wp_{m,n}\). Put
\[
U_k(p)=2^p\left(1+\frac1k\right)-2^{2p-1},\qquad
B(p)=3^p-1-2^{2p-1},\qquad
p_*=\min\left\{\log_2\left(2+\frac2m\right),\log_2\left(2+\frac2n\right)\right\}.
\]
The exact exponent is the **unique** solution \(p\in(1,p_*)\) of
\[
\boxed{U_m(p)U_n(p)=B(p)^2.}
\]
Strict negative type holds for every \(0\le p<\wp_{m,n}\), and at the endpoint the zero-sum negative-type equality space is one-dimensional. No exponent above \(\wp_{m,n}\) has negative type.

**Strict fixed-size balance law.** For any fixed total number \(S=m+n\ge4\) of leaves, \(\wp_{m,n}\) increases strictly with the product \(mn\). Thus the largest exponent occurs exactly at the balanced or near-balanced allocation and the smallest occurs at the two extremal allocations \((2,S-2)\) and \((S-2,2)\).

**Large-branching interpolation.** Let \(L=\log2\), \(J=3\log3-4\log2\), and suppose \(m,n\to\infty\) with \(m/n\to\rho\in(0,\infty)\). Then
\[
\boxed{\lim_{n\to\infty}n(\wp_{m,n}-1)
=\frac{2/\rho}{L(1+1/\rho)+\sqrt{L^2(1-1/\rho)^2+J^2/\rho}}.}
\]
For each fixed \(m\ge2\), the extreme-imbalance law instead reads
\[
\boxed{\lim_{n\to\infty}n(\wp_{m,n}-1)=\frac1{\log2}.}
\]
For example, \(\wp_{2,4}\approx1.307286363417\), whereas \(\wp_{3,3}\approx1.346824482471\). The known balanced identity is recovered by setting \(m=n=q\), obtaining \(q3^p=(q+1)2^p+q\).

## Assumptions and scope

The graph has two distinguished adjacent vertices \(h_1,h_2\), \(m\) degree-one neighbors of \(h_1\), and \(n\) degree-one neighbors of \(h_2\), with every edge of length one and all \(m+n+2\) vertices retained. Distances between two distinct same-side leaves are two, between opposite-side leaves three, between hubs one, and between a leaf and its near or far hub one or two, respectively. We take \(m,n\ge2\) throughout.

A metric has \(p\)-negative type if, for every real vertex vector \(\alpha\) with coordinate sum zero,
\[
\mathcal Q_p(\alpha)=\sum_{i,j}\alpha_i\alpha_j d(i,j)^p\le0.
\]
It has strict \(p\)-negative type if equality forces \(\alpha=0\). Its supremal exponent is the supremum of all such \(p\ge0\). Logarithms without a subscript are natural. The powered snowflake distance for Euclidean embedding is \(d^{p/2}\).

## Proof

**1. Exact zero-sum decomposition.** Denote the coefficients on the first leaves by \(x_i\), on the second leaves by \(y_j\), and on the hubs by \(u,v\). Let \(X=\sum_i x_i\), \(Y=\sum_j y_j\), so that \(u+v+X+Y=0\); set \(\widetilde x_i=x_i-X/m\) and \(\widetilde y_j=y_j-Y/n\). Direct expansion of every pairwise distance, followed by completion of the hub square, gives the exact identity
\[
\begin{aligned}
\mathcal Q_p(\alpha)={}&-2^p\sum_i\widetilde x_i^2-2^p\sum_j\widetilde y_j^2\\
&-2\left(u+\frac{2^pX}{2}-\frac{(2^p-2)Y}{2}\right)^2\\
&-U_m(p)X^2-U_n(p)Y^2+2B(p)XY.
\end{aligned}
\]
Consequently the metric has \(p\)-negative type exactly when
\[
H_{m,n}(p)=\begin{pmatrix}U_m(p)&-B(p)\\-B(p)&U_n(p)\end{pmatrix}
\]
is positive semidefinite. When the matrix is positive definite, the metric has strict negative type.

**2. Existence, uniqueness and endpoint rank.** At \(p=1\), \(U_k(1)=2/k\) and \(B(1)=0\), hence \(H_{m,n}(1)\) is positive definite. For \(1<p<2\), \(B(p)>0\): the strictly concave function
\[
p\longmapsto\log(3^p-1)-(2p-1)\log2
\]
vanishes at both \(p=1\) and \(p=2\), so it is positive between them. Each \(U_k(p)\) is strictly positive for \(1\le p<\log_2(2+2/k)\) and vanishes at its upper endpoint. Thus \(\det H_{m,n}(1)>0\) but \(\det H_{m,n}(p_*)=-B(p_*)^2<0\). There is a root in \((1,p_*)\), with positive diagonals and nonzero off-diagonal at the first root.

Li and Weston's strict-negative-type inheritance principle says that if a metric has \(q\)-negative type for any \(q>p\), it has strict \(p\)-negative type. A first singular exponent therefore excludes a later negative-type exponent: a later exponent would force the first singular matrix to be strictly negative type, a contradiction. The same argument excludes a second root of the displayed determinant within \((1,p_*)\), since every zero there has nontrivial zero-sum equality. At the unique root \(H_{m,n}\) has rank one, and all three other squares in the decomposition are strictly negative except at zero; the negative-type equality space is exactly one-dimensional. The ordinary Schoenberg correspondence gives minimum affine Euclidean embedding dimension \(m+n+1\) for \(0<p<\wp_{m,n}\), dropping to \(m+n\) at \(p=\wp_{m,n}\).

**3. Rigidity under balancing.** Fix \(S=m+n\), put \(t(p)=1-2^{p-1}\), and denote the determinant by \(\Delta_{m,n}(p)\). An exact rearrangement gives
\[
\boxed{\Delta_{m,n}(p)=2^{2p}\left[t(p)^2+\frac{1+St(p)}{mn}\right]-B(p)^2.}
\]
Let \(p_S=\log_2(2+2/S)\), so \(t(p_S)=-1/S\), and therefore
\[
\Delta_{m,n}(p_S)=\frac{2^{2p_S}}{S^2}-B(p_S)^2
\]
independently of the allocation. This is strictly positive. To see it without a numerical assumption, \(B\) is concave for \(p\ge1\), since
\[
B''(p)=3^p(\log3)^2-2\cdot4^p(\log2)^2<0.
\]
The last inequality follows already at \(p=1\) from \(3^5<2^8\) and becomes stronger as \(p\) increases. Writing \(J=B'(1)=3\log3-4\log2>0\), concavity gives
\[
0<B(p_S)\le J(p_S-1)\le\frac{J}{S\log2}<\frac2S<\frac{2^{p_S}}S.
\]
Hence \(\wp_{m,n}>p_S\) for every allocation with the same leaf budget. Whenever \(p>p_S\), \(1+St(p)<0\), so the determinant in the boxed identity is **strictly increasing** as the product \(mn\) increases. At the smaller-product allocation's critical root, the larger-product determinant is positive; its own critical root must therefore be larger. This proves the fixed-budget balance law and its strictness.

**4. Branching limits.** When \(m/n\to\rho\in(0,\infty)\), the root lies between \(1\) and \(p_*\), so \(\varepsilon=\wp_{m,n}-1=O(1/n)\). Taylor expansion uniformly along the parameter sequence gives
\[
U_m(1+\varepsilon)=\frac2m-2L\varepsilon+O(n^{-2}),\quad
U_n(1+\varepsilon)=\frac2n-2L\varepsilon+O(n^{-2}),\quad
B(1+\varepsilon)=J\varepsilon+O(n^{-2}).
\]
Every subsequential limit \(c\) of \(n\varepsilon\) solves
\[
\left(\frac2\rho-2Lc\right)(2-2Lc)=J^2c^2.
\]
The nonnegative root compatible with \(\varepsilon<\min\{\log_2(1+1/m),\log_2(1+1/n)\}\) is unique, and the quadratic formula yields the claimed \(c(\rho)\). If \(m\) is fixed while \(n\to\infty\), \(U_m(\wp_{m,n})\to2/m>0\), the determinant equation yields \(U_n(\wp_{m,n})=O(n^{-2})\), and the expansion of \(U_n\) gives \(n(\wp_{m,n}-1)\to1/L\).

## Verification

A standalone Python 3.10+ checker, `verify_bistar.py`, uses only the standard library. Run it with `python verify_bistar.py`. It has been executed successfully and reports:

```
EXACT_ZERO_SUM_QUADRATIC_IDENTITY_OK 1550
CRITICAL_ROOT_INTERVAL_AND_RANK_OK 576
FIXED_LEAF_BUDGET_BALANCE_DIAGNOSTICS_OK 1521
ASYMMETRIC_LARGE_BRANCHING_LIMIT_DIAGNOSTICS_OK
ALL_UNBALANCED_DOUBLE_STAR_NEGATIVE_TYPE_CHECKS_OK
```

The 1,550 exact-rational checks test the completed-square distance identity at integral powers against independently enumerated graph distances. The remaining finite root and limit checks are diagnostics, not substitutes for the analytical existence/uniqueness, balance, and asymptotic arguments. For instance, the balanced special-case equality reduces exactly to the previously known balanced double-star formula.

## Relationship to prior work

Doust and Weston, *Enhanced negative type for finite metric trees* (arXiv:0705.0411, first public 2007-05-03), prove general tree negative-type bounds and an exact formula for a **single-hub equiradial star** in their Section 5. Their inequalities concern finite trees more generally but do not directly evaluate the asymmetric double-star determinant or its balancing law. Li and Weston, *Strict p-negative type of a metric space* (arXiv:0901.0695, first public 2009-01-06), supply the general inheritance theorem and nonstrict endpoint framework used above; those results do not give the explicit double-star calculation. A balanced two-hub calculation yields the specialization \(q3^p=(q+1)2^p+q\), so the symmetric subfamily alone is not presented as a discovery. The new content is the **asymmetric two-parameter exact classification**, its **strict fixed-leaf-budget rearrangement order**, and its **branching-ratio interpolation**.

## Limitations

The result assumes an unweighted diameter-three tree with two hubs and at least two leaves at each hub, with all vertices included. It does not classify unequal positive edge lengths, three or more hubs, arbitrary trees, or the optimal finite-order quantitative stability gap under balancing. The proof establishes exact root characterization rather than a closed elementary expression for the root. Complete literature priority cannot be certified from accessible sources alone; equivalent unpublished or unindexed results remain a possible originality risk.

## References

- I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411 (first publicly posted 2007-05-03), https://arxiv.org/abs/0705.0411.
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first publicly posted 2009-01-06), https://arxiv.org/abs/0901.0695.
