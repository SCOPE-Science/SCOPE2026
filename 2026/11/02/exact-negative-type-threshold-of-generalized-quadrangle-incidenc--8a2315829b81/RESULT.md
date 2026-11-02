# Exact negative-type threshold of generalized-quadrangle incidence metrics

## Finding

Let \(q\ge2\) be an integer for which a finite generalized quadrangle of order \((q,q)\) exists. Let \(X_q\) be its point-line incidence graph with each edge assigned length one and with shortest-path metric \(d\). Define its supremal negative-type exponent
\[
\wp_q=\sup\left\{p\ge0:\ \sum_{u,v\in X_q}a_ua_vd(u,v)^p\le0\ \text{for every real }(a_u)\text{ with }\sum_u a_u=0\right\}.
\]
For \(p=0\), use the usual zero-diagonal, unit-off-diagonal convention. Define
\[
F_q(p)=-(q+1)+q(q+1)2^p-q^2(q+1)3^p+q^3 4^p.
\]
**The exact exponent \(\wp_q\) is the unique positive zero of \(F_q\)**, and it lies in
\[
0<\wp_q<\log_2(1+1/q)<1.
\]
The metric has strict \(p\)-negative type for \(0\le p<\wp_q\), nonstrict \(\wp_q\)-negative type at the endpoint, and fails \(p\)-negative type for every \(p>\wp_q\). The only zero-sum equality direction at the endpoint is the vector taking \(+1\) on points and \(-1\) on lines.

The exponent has the quantitative large-order expansion
\[
\boxed{\displaystyle
\wp_q=\frac{1}{q^3\log(4/3)}+
\frac{\log(3/2)}{q^4\log^2(4/3)}+O(q^{-5}).}
\]
In particular \(q^3\wp_q\to1/\log(4/3)\). The assertion holds along every unbounded sequence of existing orders; symplectic generalized quadrangles supply all prime-power orders.

Equivalently, Schoenberg's criterion gives isometric embedding of \((X_q,d^{p/2})\) in real Hilbert space exactly for \(0\le p\le\wp_q\). Writing \(N_q=2(q+1)(q^2+1)\), the least affine Hilbert embedding dimension is \(N_q-1\) below the endpoint, and exactly \(N_q-2\) at the endpoint.

## Assumptions and scope

A generalized quadrangle of order \((q,q)\) is a finite incidence structure in which every point is incident with \(q+1\) lines, every line contains \(q+1\) points, distinct points lie on at most one common line, and for each point not on a line there is exactly one point of the line collinear with the given point. Both the point and line sets have cardinality \((q+1)(q^2+1)\). The graph has one vertex for each point and each line, with incidence edges only. No assumption of automorphism transitivity, self-duality, or a particular classical construction is made.

For \(p>0\), the powered distance matrix is \(D_p=(d(u,v)^p)_{u,v\in X_q}\), with diagonal zero. A metric has \(p\)-negative type precisely when the symmetric form defined by \(D_p\) is nonpositive on the codimension-one space of real coefficients of total sum zero. Strictness means negative definiteness on that space. This is a finite-vertex metric statement, not a statement about the continuum obtained by filling graph edges with intervals.

## Proof

**1. Distance shells and spectral polynomial.** Let \(A=A_1\) denote the graph adjacency matrix, and let \(A_j\) be the zero-one matrix for graph distance \(j\), with \(A_0=I\). The defining incidence axioms give the distance shells, from either sort of vertex, of sizes
\[
(k_0,k_1,k_2,k_3,k_4)=
(1,q+1,q(q+1),q^2(q+1),q^3).
\]
A vertex at distance \(j\in\{1,2,3\}\) has one neighbor at distance \(j-1\) and \(q\) at distance \(j+1\); at distance four it has \(q+1\) neighbors at distance three. Thus the intersection array is
\[
\{q+1,q,q,q;\ 1,1,1,q+1\}.
\]
The matrix identities \(AA_1=(q+1)A_0+A_2\), \(AA_2=qA_1+A_3\), and \(AA_3=qA_2+(q+1)A_4\) imply
\[
\begin{aligned}
A_2&=A^2-(q+1)I,\\
A_3&=A^3-(2q+1)A,\\
A_4&=\frac{A^4-(3q+1)A^2+q(q+1)I}{q+1}.
\end{aligned}
\]
Let \(B\) be the square point-line incidence matrix. The point-collinearity matrix is \(BB^{\mathsf T}-(q+1)I\), a strongly regular adjacency matrix with parameters
\[
\big((q+1)(q^2+1),\ q(q+1),\ q-1,\ q+1\big).
\]
Indeed, two collinear points have \(q-1\) common collinear points, and two noncollinear points have \(q+1\) common collinear points, by the quadrangle axiom. Its nontrivial eigenvalues are \(q-1\) and \(-(q+1)\). Therefore \(BB^{\mathsf T}\) has eigenvalues \((q+1)^2,2q,0\), while the bipartite adjacency matrix \(A\) has spectral values
\[
q+1,\quad -(q+1),\quad \sqrt{2q},\quad -\sqrt{2q},\quad 0.
\]
All are realized for \(q\ge2\). The constant vector corresponds to \(q+1\), and the point-minus-line vector to \(-(q+1)\); all other eigenspaces are orthogonal to constants.

**2. Every potentially obstructing powered-distance eigenvalue.** Since
\[
D_p=A_1+2^pA_2+3^pA_3+4^pA_4,
\]
the eigenvalue on the point-minus-line direction is exactly \(F_q(p)\). On the other zero-sum eigenspaces, the eigenvalues are
\[
\begin{aligned}
E_0(p)&=q4^p-(q+1)2^p,\\
E_\pm(p)&=(q-1)2^p-q4^p\pm\sqrt{2q}\,(3^p-1).
\end{aligned}
\]
These identities determine the signs of the entire powered-distance quadratic form on the zero-sum subspace; no symmetry assumption is imposed on test coefficient vectors.

**3. A unique early root in the bipartition mode.** Set \(b_q=\log_2(1+1/q)\). Directly, \(F_q(0)=-1\) and
\[
F'_q(0)=q^3\log(4/3)-q^2\log(3/2)+q\log2>0.
\]
The positivity follows from \(2\log(4/3)>\log(3/2)\). Also \(F''_q(p)>0\) for every \(p\ge0\). To see this, divide the derivative formula by \(q2^p\), then use \(2^p\ge(3/2)^p\):
\[
\frac{F''_q(p)}{q2^p}\ge(q+1)(\log2)^2+
\big[q^2(\log4)^2-q(q+1)(\log3)^2\big](3/2)^p>0.
\]
The bracket is strictly positive for all \(q\ge2\), because \(4^4>3^5\) implies \(\log4/\log3>5/4>\sqrt{3/2}\), and \((q+1)/q\le3/2\).

For \(q\ge3\), \(F'_q(0)>(q+1)\log2\). In fact the difference is \(q^2[q\log(4/3)-\log(3/2)]-\log2\), which is bounded below by \(9\log(128/81)-\log2>0\). Since \(b_q\ge1/((q+1)\log2)\), strict convexity yields \(F_q(b_q)\ge-1+b_qF'_q(0)>0\). For \(q=2\) one may instead use \(b_2>1/2\) and
\[
F_2(1/2)=13+6\sqrt2-12\sqrt3>0.
\]
It follows that \(F_q\) increases strictly on \([0,\infty)\), has a unique positive zero \(\wp_q\), and \(0<\wp_q<b_q\).

**4. All competing modes remain negative.** For \(0\le p\le b_q\), put \(u=2^p-1\). Then \(0\le u\le1/q\). The first competing eigenvalue satisfies
\[
E_0(p)=2^p\big[q2^p-(q+1)\big]\le0,
\]
with strict inequality for \(p<b_q\). Since the function \(x\mapsto x^{\log_2 3}\) is convex, its graph lies below the chord joining \((1,1)\) and \((2,3)\). Therefore, for \(0\le p\le1\),
\[
3^p-1\le2(2^p-1)=2u.
\]
This gives the uniform bound
\[
\begin{aligned}
E_+(p)&\le-(1+u)(1+qu)+2\sqrt{2q}\,u\\
&=-1+[2\sqrt{2q}-q-1]u-qu^2\\
&\le-1+u-qu^2<0.
\end{aligned}
\]
The penultimate inequality follows from \(2\sqrt{2q}\le q+2\), equivalent to \((q-2)^2\ge0\); the strict final inequality uses \(u\le1/q\le1/2\). Since \(E_-(p)\le E_+(p)\), both competing modes are strictly negative throughout the relevant interval. Consequently, at \(p=\wp_q\) only the one-dimensional bipartition mode reaches zero; all other zero-sum modes are strictly negative. For larger \(p\), the strictly positive \(F_q(p)\) obstructs negative type. This proves the exact exponent and the equality-space statement.

**5. Asymptotics and Hilbert embedding ranks.** Write \(a=\log(4/3)\) and \(b=\log(3/2)\). For every fixed bounded \(c\ge0\), Taylor's formula at zero gives
\[
F_q(c/q^3)=-1+ac-\frac{bc}{q}+O_c(q^{-2}),
\]
because \(F'_q(0)=aq^3-bq^2+q\log2\) and \(F''_q(p)=O(q^3)\) uniformly for \(p=O(q^{-3})\). Root bracketing shows \(q^3\wp_q\to1/a\), and one further substitution yields
\[
\wp_q=\frac{1}{aq^3}+\frac{b}{a^2q^4}+O(q^{-5}).
\]
The Schoenberg correspondence identifies \(p\)-negative type with a Hilbert realization of the powered metric \(d^{p/2}\). The centered Gram matrix is \(-\tfrac12 JD_pJ\), with \(J\) the orthogonal projection away from constants. Its rank is \(N_q-1\) for \(p<\wp_q\) and \(N_q-2\) at \(p=\wp_q\), as exactly one zero-sum eigenvalue vanishes. These are the least possible affine embedding dimensions.

## Verification

The included standalone Python script `gq_negative_type_check.py` constructs the classical symplectic generalized quadrangles over the prime fields of orders \(2,3,5\), verifies all distance-shell counts and both nontrivial distance-matrix recurrences on all vertex pairs, and evaluates the critical spectral modes. It additionally samples root and mode inequalities for orders \(2\) through \(199\). It uses only Python's standard library and prints the exact counts of graph-recurrence comparisons. The finite checks are corroboration only; the proofs of strictness, uniqueness, universality across all existing quadrangles, and the asymptotic expansion are analytic.

Numerically, the smallest orders give \(\wp_2\approx0.345784723476\), \(\wp_3\approx0.137565128845\), and \(\wp_5\approx0.032764105998\). These numerical approximations are not used to determine the proof's sign inequalities.

## Relationship to prior work

The definitions, Hilbert correspondence, and general powered-distance framework follow classical Schoenberg theory and are discussed by Robertson (arXiv:2309.16070, first posted September 27, 2023). Robertson's examples concern complete bipartite graphs and Hamming cubes, not generalized-quadrangle incidence graphs. Robertson (arXiv:2004.10923) and Murugan (arXiv:1112.5657) give general determinant/row-regular metric criteria, but no explicit generalized-quadrangle active eigenmode, root equation, or cubic-order asymptotic law.

Bartoli, Héger, Kiss, and Takáts (arXiv:1706.06583, first posted June 20, 2017) study the same generalized-quadrangle incidence graphs and their metric dimension, a different invariant. In particular, their metric dimension is a resolving-set cardinality, not a negative-type threshold. The more recent work of Campbell, Hendrey, Lund, and Tompkins (arXiv:2501.07098) studies negative type for *continuous* metric graphs formed by retaining the entire edge intervals; it does not directly determine the finite *vertex* metric here.

A general determinant test plus the known distance-regular intersection array can in principle be used as a starting point for this calculation. What is established here is the explicit identification and exclusion of competing modes at every order, the sharp scalar root, the critical equality rank, and the two-term asymptotic expansion. Literature comparisons do not establish absolute historical priority.

## Limitations

The formula applies only to the shortest-path metric on the vertices of an existing order-\((q,q)\) generalized quadrangle with \(q\ge2\). It does not extend automatically to unbalanced orders, continuous metric graphs, weighted incidence edges, or arbitrary graphs with similar girth. Neither uniqueness of a particular coordinate realization nor any independent validation is claimed. Older terminology for negative type, generalized roundness, or finite-polar-geometry distance matrices could conceal prior equivalent work; the targeted inspection and search are not a proof of worldwide novelty.

## References

1. Bartoli, D.; Héger, T.; Kiss, G.; Takáts, M., *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, arXiv:1706.06583 (first public version June 20, 2017). https://arxiv.org/abs/1706.06583
2. Robertson, G., *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space*, arXiv:2309.16070 (first public version September 27, 2023). https://arxiv.org/abs/2309.16070
3. Robertson, G., *The Maximal Generalised Roundness of Finite Metric Spaces*, arXiv:2004.10923 (first public version April 23, 2020). https://arxiv.org/abs/2004.10923
4. Murugan, M. K., *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657 (first public version December 23, 2011). https://arxiv.org/abs/1112.5657
5. Campbell, R.; Hendrey, K.; Lund, B.; Tompkins, C., *Metric graphs of negative type*, arXiv:2501.07098 (first public version January 13, 2025). https://arxiv.org/abs/2501.07098
