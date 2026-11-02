# Exact generalized roundness and critical Hilbert dimension of balanced double-star trees

## Finding

For each integer \(q\geq1\), form the unit-edge **balanced double star** \(T_q\) by joining two hubs with one edge and attaching \(q\) leaves to each hub. Let \(d_q\) be its shortest-path metric, with \(2q+2\) vertices. For \(p\geq0\), write \(D_p=(d_q(v,w)^p)_{v,w}\), with diagonal entries zero, and let \(\wp_q\) be the supremum of exponents for which \(D_p\) is conditionally negative semidefinite.

**Theorem.** For every integer \(q\geq1\), the exact exponent \(\wp_q\) is the unique solution in \((1,2]\) of
\[
q\,3^{\wp_q}=(q+1)2^{\wp_q}+q.
\]
In particular, \(\wp_1=2\), while \(1<\wp_q<2\) for every \(q\geq2\). The tree has strict \(p\)-negative type for \(0\leq p<\wp_q\), non-strict negative type at \(p=\wp_q\), and fails \(p\)-negative type for every \(p>\wp_q\).

For \(q\geq2\), the complete zero-sum equality space at \(p=\wp_q\) is one-dimensional: coefficients equal \(+1\) on all \(2q\) leaves and \(-q\) on both hubs, up to a scalar. Consequently the least Euclidean embedding dimension of the snowflaked distance \(d_q^{p/2}\) equals \(2q+1\) for \(0<p<\wp_q\), and is exactly \(2q\) at \(p=\wp_q\). For \(q=1\), the tree is a four-vertex path and its endpoint Euclidean dimension is \(1\).

The exponents decrease strictly as \(q\) increases, with the quantitative limit
\[
\wp_q=1+\frac{2}{(3\log 3-2\log2)q}+O(q^{-2})
=1+\frac{1.047371291754\ldots}{q}+O(q^{-2}).
\]
For \(q\ge2\) this exponent is **strictly smaller** than the known exponent of either induced \((q+1)\)-leaf star:
\[
\wp_q<1+\log_2(1+1/q).
\]
Thus joining two branching stars along their central edge introduces a stronger negative-type obstruction than is present in either individual star.

## Assumptions and scope

All graphs are finite, simple, unweighted, and endowed with the ordinary shortest-path distance on the **vertex set**. The parameter \(q\) is an integer at least one. The \(p\)-negative-type condition means
\[
Q_p(c)=\sum_{v,w\in V(T_q)} c_vc_w d_q(v,w)^p\leq0
\quad\text{for every real }c\text{ with }\sum_vc_v=0.
\]
Strict negative type means \(Q_p(c)<0\) for every nonzero such \(c\). The condition at \(p=0\) uses the standard convention that every off-diagonal powered distance is one and diagonal entries are zero. A finite squared-Euclidean distance matrix has conditionally negative semidefinite entries; its centered Gram matrix is \(-JD_pJ/2\), where \(J\) is projection onto the zero-sum subspace.

## Proof

**1. A complete orthogonal decomposition.** Name the hubs \(h_A,h_B\) and their leaf sets \(A,B\), both of size \(q\). The distance shells are: between distinct leaves on the same side, \(2\); between leaves on opposite sides, \(3\); between a hub and its own leaf, \(1\); between a hub and a leaf across the central edge, \(2\); and between the hubs, \(1\).

Fix \(p>0\), and abbreviate \(t=2^p\) and \(u=3^p\). For a zero-sum vector \(c\), write its leaf coefficients as means \(a_A,a_B\) plus zero-sum residuals \(r_A,r_B\), and denote its hub coefficients by \(b_A,b_B\). Put
\[
a_s=(a_A+a_B)/2,\quad a_a=(a_A-a_B)/2,\quad
b_s=(b_A+b_B)/2,\quad b_a=(b_A-b_B)/2.
\]
The zero-sum constraint says \(b_s=-qa_s\). Expanding the powered-distance quadratic form, or applying the side-interchange symmetry, gives the **exact identity**
\[
\begin{aligned}
Q_p(c)={}&-t\bigl(\|r_A\|_2^2+\|r_B\|_2^2\bigr)
+2q\,f_q(p)a_s^2\\
&+2\left[q((q-1)t-qu)a_a^2
+2q(1-t)a_ab_a-b_a^2\right],
\end{aligned}
\]
where \(f_q(p)=qu-(q+1)t-q\). All leaf-residual modes are strictly negative. The symmetric contrast mode is controlled by \(f_q\). The antisymmetric two-dimensional block is the symmetric matrix
\[
M_q(p)=\begin{pmatrix}q((q-1)t-qu)&q(1-t)\\q(1-t)&-1\end{pmatrix},
\]
with determinant \(qg_q(p)\), where
\[
g_q(p)=qu+(q+1)t-qt^2-q.
\]
The upper-left entry of \(M_q\) is strictly negative for \(p>0\); thus the block is strictly negative definite exactly when \(g_q(p)>0\).

**2. The unique symmetric threshold.** Divide \(f_q(p)=0\) by \(q2^p\) to obtain
\[
\phi(p):=(3/2)^p-1-2^{-p}=1/q.
\]
The function \(\phi\) is strictly increasing for \(p\ge0\), and \(\phi(1)=0\), \(\phi(2)=1\). It therefore has a unique root \(\wp_q\in(1,2]\), strictly between one and two when \(q\ge2\). For \(1\le p<\wp_q\), the symmetric mode is strictly negative; at the root it vanishes; above it the concrete coefficient vector \(c=+1\) on all leaves and \(c=-q\) on both hubs gives \(Q_p(c)=2qf_q(p)>0\). This proves failure for **every** \(p>\wp_q\), not just for a sampled exponent.

**3. The antisymmetric block cannot obstruct earlier when \(q\ge2\).** Let \(\alpha=\log_2 3\), so \(1<\alpha<5/3\). Direct differentiation gives
\[
\frac{g_q'(p)}{q(\log2)2^p}
=\alpha(3/2)^p+1+1/q-2^{p+1}.
\]
For \(q\ge2\), the right side is negative at \(p=1\), since \(3\alpha/2-3+1/q<0\). It strictly decreases on \([1,\infty)\): its derivative is \(\alpha\log(3/2)(3/2)^p-2\log2\,2^p<0\). Hence \(g_q\) strictly decreases for \(p\ge1\).

It remains to show \(g_q(\wp_q)>0\). Set \(s=1+1/q\in(1,2)\), and let \(p_0=\log_2(2s)\). Then
\[
\frac{f_q(p_0)}q=3s^\alpha-2s^2-1.
\]
This expression is zero at \(s=1\) and \(s=2\), and strictly positive between them: its second derivative is \(3\alpha(\alpha-1)s^{\alpha-2}-4<0\), since \(\alpha<5/3\) and \(s\ge1\). The monotonicity of \(\phi\) implies \(\wp_q<p_0\), so \(t=2^{\wp_q}<2+2/q\). Substituting \(qu=(q+1)t+q\) into \(g_q\) at the root now yields
\[
g_q(\wp_q)=t\bigl(2(q+1)-qt\bigr)>0.
\]
As \(g_q\) decreases for \(p\ge1\), it is positive throughout \([1,\wp_q]\). The antisymmetric block is therefore strictly negative definite throughout this interval.

**4. All exponents and equality spaces.** At \(p=1\), any finite tree has strict negative type. One direct proof writes the tree metric as the sum of its edge-cut semimetrics; for any zero-sum \(c\),
\[
Q_1(c)=-2\sum_{e\in E(T_q)}\left(\sum_{v\in U_e}c_v\right)^2,
\]
where \(U_e\) is either component after deleting edge \(e\). All cut sums vanish only when \(c=0\), by removing leaves inductively. Standard negative-type monotonicity then gives strict \(p\)-negative type below \(1\) (or use the Li--Weston strictness theorem).

For \(q\ge2\), Steps 1--3 prove strict negative type on \([1,\wp_q)\) and exactly one zero-sum null direction at \(p=\wp_q\), namely the symmetric vector described in the finding. The centered Gram rank is therefore \(2q+1\) below the critical exponent and \(2q\) at it. Schoenberg's finite metric criterion converts these ranks into the stated least Hilbert dimensions. When \(q=1\), \(T_1\) is a path on four consecutive integer points, so its metric has \(2\)-negative type and an endpoint rank-one squared-Euclidean Gram matrix. For \(p>2\), the coefficients \((1,-2,1)\) on three consecutive path vertices give \(Q_p=2(2^p-4)>0\); strictness below \(2\) follows again by monotonicity.

**5. Asymptotics and the one-hub comparison.** The defining equation \(\phi(\wp_q)=1/q\) and \(\phi'(1)=(3\log3-2\log2)/2>0\) yield the displayed expansion by Taylor inversion, with error \(O(q^{-2})\). Since \(\phi\) increases, \(\wp_q\) strictly decreases with \(q\). The strict comparison with a \((q+1)\)-leaf star follows from \(\wp_q<p_0=1+\log_2(1+1/q)\) in Step 3 and the exact star exponent obtained by Doust and Weston.

## Verification

The accompanying standalone `verify_bistar_roundness.py` uses only the Python standard library. It constructs the shortest-path distance matrices independently by breadth-first search for all \(1\le q\le12\), checks the full invariant-block quadratic identity using exact rational arithmetic at exponents \(1,2,3\), and evaluates the critical exponents and their null vectors. It also checks the first asymptotic coefficient at several larger sizes. Run `python3 verify_bistar_roundness.py` from this directory. The expected terminal marker is `ALL_BALANCED_BISTAR_ROUNDNESS_CHECKS_OK`.

These are finite reproducibility checks only. The universal quantifiers, uniqueness, full real-exponent sign assertions, and asymptotic remainder follow from the analytic arguments in the proof.

## Relationship to prior work

Doust and Weston [1] establish strict \(1\)-negative type and enhanced-gap bounds for all finite trees, and **exactly evaluate the one-hub star** in their Theorem 38; their exact star formula is used in the comparison. Li and Weston [2] establish strictness properties for finite negative-type metrics. Caffarelli, Doust and Weston [3] study the approach of finite-tree generalized roundness toward one and give bounds for spherically symmetric trees; their work motivates the asymptotic question but does not evaluate this two-hub family. Sánchez [4] supplies a general distance-matrix approach and evaluates complete-bipartite shortest-path metrics, not this tree family.

The contribution here is the **all-parameter evaluated formula for the balanced double star**, its complete first-loss equality space, the critical Hilbert-rank drop, and the strict separation from one-hub stars. These statements are not asserted to be consequences of the generic finite-metric determinant characterization alone. An equivalent calculation in unindexed or otherwise unlocated literature remains a possibility.

## Limitations

The exact theorem treats balanced, unweighted double-star **vertex** metrics. It does not classify unequal numbers of leaves, nonunit edge lengths, continuous metric realizations of the edges, arbitrary diameter-three trees, or arbitrary weighted trees. The Euclidean embedding assertion concerns the snowflake \(d_q^{p/2}\), **not** the unsnowflaked tree distance unless \(p=2\). The proof is analytic; finite checks have no bearing on missing infinite cases. Independent scientific validation has not been performed.

## References

1. Ian Doust and Anthony Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411 (first posted May 3, 2007), especially Theorem 38 and the preceding general negative-type gap results. https://arxiv.org/abs/0705.0411
2. Hanfeng Li and Anthony Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695 (first posted January 6, 2009), especially the interval and strictness results. https://arxiv.org/abs/0901.0695
3. Elena Caffarelli, Ian Doust and Anthony Weston, *Metric trees of generalized roundness one*, arXiv:1008.3418 (first posted August 20, 2010), Sections 2 and 5. https://arxiv.org/abs/1008.3418
4. Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first posted August 2, 2011), Sections 2--3. https://arxiv.org/abs/1108.0451
