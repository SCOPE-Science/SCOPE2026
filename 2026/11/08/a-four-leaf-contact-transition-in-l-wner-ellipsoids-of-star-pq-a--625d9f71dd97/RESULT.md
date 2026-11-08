# A four-leaf contact transition in Löwner ellipsoids of star PQ-adjacency polytopes

## Finding
For every integer \(m\ge1\), let \(G=K_{1,m}\) have hub \(0\) and leaves \(1,\ldots,m\), and let its PQ-type adjacency polytope, in the *canonical ambient Euclidean embedding*, be
\[
 P_m=\operatorname{conv}\{(e_i,e_j):i=j\text{ or }\{i,j\}\in E(G)\}\subset\mathbb R^{m+1}\oplus\mathbb R^{m+1}.
\]
Put \(d=2m\) and
\[
 w_m=\begin{cases}\displaystyle\frac{3}{4(2m+1)},&1\le m\le4,\\[2mm]
 \displaystyle\frac1{3m},&m\ge4,\end{cases}\qquad
 \alpha_m=2w_m,\quad B_m=3w_m,\quad g_m=3w_m-8mw_m^2.
\]
The two definitions agree at \(m=4\), and \(g_m>0\). The **unique minimum-volume enclosing (Löwner) ellipsoid** has center \(c=(\bar x,\bar x)\), where every leaf coordinate of \(\bar x\) equals \(\alpha_m\) and its hub coordinate is \(1-m\alpha_m\).

Write \(a_i=x_i\) and \(b_i=y_i\) for the leaf coordinates of a point \((x,y)\) of the affine hull. Define
\[
 u_i=\frac{(a_i-\alpha_m)+(b_i-\alpha_m)}{\sqrt2},\qquad
 v_i=\frac{(a_i-\alpha_m)-(b_i-\alpha_m)}{\sqrt2},\quad
 u_\parallel=\frac{\sum_i u_i}{m}\mathbf1,\quad u_\perp=u-u_\parallel.
\]
Then the exact ellipsoid is
\[
 \boxed{\mathcal E_m=\left\{(x,y):
 \frac{\|u_\parallel\|_2^2}{g_m}+
 \frac{\|u_\perp\|_2^2}{B_m}+
 \frac{\|v\|_2^2}{w_m}\le 2m\right\}.}
\]
For \(1\le m\le4\), **all \(3m+1\) vertices of \(P_m\)** contact the boundary of \(\mathcal E_m\). For \(m\ge5\), **exactly \(3m\) vertices** contact: the hub-diagonal vertex \((e_0,e_0)\) lies strictly inside, while every other vertex remains on the boundary. No nonvertex point of \(P_m\) contacts the ellipsoid.

The squared intrinsic-Euclidean semiaxes of \(\mathcal E_m\), with multiplicities, are
\[
 \boxed{2m(m+1)g_m\ (1),\qquad 2m B_m\ (m-1),\qquad
 2m(m+1)w_m\ (1),\qquad 2m w_m\ (m-1).}
\]
In particular, for \(m\ge4\) they become \(2(m+1)/9\), \(2\), \(2(m+1)/3\), and \(2/3\), respectively. With \(\kappa_{2m}=\pi^m/m!\), the **intrinsic Euclidean volume** is
\[
 \boxed{\operatorname{vol}_{2m}(\mathcal E_m)=\kappa_{2m}(m+1)
 \begin{cases}
 \displaystyle\frac{m^m3^{3m/2}}{2^m(2m+1)^{m+1/2}},&1\le m\le4,\\[2mm]
 \displaystyle\frac{2^m}{3^{m/2+1}},&m\ge4.
 \end{cases}}
\]
The formulas agree at the transition.

## Assumptions and scope
All norms, volumes, and semiaxis lengths use the **intrinsic Euclidean metric induced from \(\mathbb R^{2(m+1)}\)**, not the lattice-normalized metric of a unitarily inequivalent coordinate chart. A Löwner ellipsoid means the ellipsoid of least \(2m\)-dimensional intrinsic volume that contains the complete polytope. The affine hull has equations \(\sum_i x_i=\sum_i y_i=1\) and dimension \(2m\). The hub-deleted coordinates \((a,b)\) are used only to write a convenient equation; the ambient intrinsic metric is restored explicitly for the axis and volume formulas.

## Proof
**1. An exact vertex chart.** Delete the hub coordinate from each of the two vectors; the deleted coordinate is uniquely recovered as one minus the sum of the leaf coordinates. The PQ vertex list becomes precisely
\[
 0,\qquad (e_i,0),\quad(0,e_i),\quad(e_i,e_i)\quad(1\le i\le m)
\]
in \(\mathbb R^m\oplus\mathbb R^m\). Each is a vertex: the origin uniquely minimizes the sum of all nonnegative coordinates, and for each leaf, the three nonzero patterns are vertices of the corresponding two-coordinate square face. The \(2m\) coordinate-unit vertices give full affine dimension.

**2. An explicit contact probability measure.** Give weight \(w_m\) to each of the \(3m\) nonzero vertices and weight
\[
 p_{0,m}=1-3mw_m=\begin{cases}\displaystyle\frac{4-m}{4(2m+1)},&m\le4,\\0,&m\ge4\end{cases}
\]
to the origin. These weights are nonnegative and total one. Their mean, in the leaf chart, has every coordinate \(\alpha_m=2w_m\).

The covariance \(C_m\) of this measure is positive definite. In the orthogonal leaf-coordinate transform \((a,b)\mapsto((a+b)/\sqrt2,(a-b)/\sqrt2)\), write the centered coordinates as \((u,v)\). Each nonzero pair block contributes an uncentered covariance of \(3w_m\) in its sum coordinate and \(w_m\) in its difference coordinate. The mean is \(\sqrt2\alpha_m\mathbf1\) in the sum coordinates and zero in the differences. Therefore
\[
 C_m|_{u}=3w_m I_m-2\alpha_m^2\mathbf1\mathbf1^{\mathsf T},
 \qquad C_m|_{v}=w_m I_m.
\]
Consequently the eigenvalues are \(g_m=3w_m-2m\alpha_m^2\) on the all-ones sum line, \(B_m=3w_m\) on its orthogonal complement, and \(w_m\) on the entire difference space. Substitution yields
\[
 g_m=\begin{cases}\displaystyle\frac9{4(2m+1)^2},&m\le4,\\\displaystyle\frac1{9m},&m\ge4,\end{cases}
\]
which is strictly positive. Thus the displayed ellipsoid is exactly the covariance ellipsoid \(\{z:(z-c)^\mathsf TC_m^{-1}(z-c)\le d\}\) in the affine chart.

**3. All boundary checks, exactly.** The squared Mahalanobis distances of the three orbit types (origin, coordinate-unit, paired-unit) are
\[
 Q_0=\frac{2m\alpha_m^2}{g_m},
\]
\[
 Q_a=\frac{(1-2m\alpha_m)^2}{2m g_m}
 +\frac{m-1}{2m B_m}+\frac1{2w_m},
\]
\[
 Q_p=\frac{2(1-m\alpha_m)^2}{m g_m}
 +\frac{2(m-1)}{m B_m}.
\]
Substituting the explicit parameters and simplifying gives \(Q_a=Q_p=2m\) for **every** \(m\ge1\). Moreover, \(Q_0=2m\) when \(m\le4\), and \(Q_0=8\) when \(m\ge4\). Therefore each vertex belongs to the displayed ellipsoid, with precisely the claimed contacts. Its interior is strictly convex, so every nontrivial convex combination of distinct vertices has strict inequality.

**4. A global uniqueness certificate.** This step does not assume a symmetric competitor. Let \(S\) be any positive-definite shape matrix and \(z\) any center of a containing ellipsoid \(\{x:(x-z)^\mathsf TS^{-1}(x-z)\le1\}\) in the \(d\)-dimensional leaf chart. Averaging the vertex containment inequalities using the measure in Step 2 gives
\[
 \operatorname{tr}(S^{-1}C_m)+(c-z)^\mathsf TS^{-1}(c-z)\le1.
\]
Applying the arithmetic--geometric mean inequality to the eigenvalues of \(C_m^{1/2}S^{-1}C_m^{1/2}\) yields
\[
 d\left(\frac{\det C_m}{\det S}\right)^{1/d}
 \le\operatorname{tr}(S^{-1}C_m)\le1.
\]
Hence \(\det S\ge d^d\det C_m\). Equality requires \(z=c\) and \(S=dC_m\), proving uniqueness of the proposed smallest-volume enclosing ellipsoid. The affine embedding from chart to canonical Euclidean space changes every competing ellipsoid volume by the same positive Jacobian, so the same ellipsoid is optimal in the intrinsic ambient Euclidean metric.

**5. Intrinsic semiaxes and volume.** A leaf-coordinate displacement reconstructs the hub displacement as the negative sum of the leaf displacements. Thus the induced squared norm of an \(m\)-coordinate leaf displacement is \(\|h\|_2^2+(\sum_i h_i)^2\). In the \((u,v)\) decomposition this multiplies each constant-leaf mode squared norm by \(m+1\) and leaves each mean-zero mode unchanged. This gives the stated four intrinsic eigenvalues of \(dC_m\). The chart-to-intrinsic volume Jacobian is \(m+1\); multiplying it by \(\kappa_d\sqrt{\det(dC_m)}\) and simplifying proves both volume branches.

## Verification
The file `verification/check_pq_star.py` is a Python-standard-library exact-rational checker. It independently constructs all \(3m+1\) vertices, recomputes the discrete contact measure and the full \(2m\)-by-\(2m\) covariance entry by entry, checks the three inverse-covariance quadratic forms, positivity, and the transition for \(1\le m\le9\). Execute `python verification/check_pq_star.py` from the package directory. The all-\(m\) assertion follows from the symbolic identities in Steps 2--4; a finite check cannot replace that proof.

## Relationship to prior work
Ohsugi and Tsuchiya [1], Sections 1 and 4, define exactly the PQ-type graph-adjacency polytope in the present affine embedding and establish Ehrhart \(h^*\)-polynomial and normalized-volume formulas for join graphs, including complete multipartite graphs. Since a star is \(K_{1,m}\), their results apply to its lattice invariants but do not furnish the least-volume Euclidean enclosing ellipsoid or the new contact transition. An available published result [2] gives the Löwner ellipsoid for **balanced** PQ-type complete-bipartite graphs \(K_{r,r}\) with \(r\ge2\). The present family \(K_{1,m}\), \(m\ge2\), is disjoint from that hypothesis; in particular neither its ellipsoid nor the four-leaf contact transition follows from the balanced formula. The proof does not rely on balanced-case calculations. The general covariance-moment optimality criterion is classical; its explicit and phase-sharp specialization is the contribution here.

## Limitations
The result is specific to stars, not arbitrary unbalanced complete-bipartite graphs or joins, and it concerns the canonical affine embedding with the induced Euclidean metric. A general affine change of coordinates changes its semiaxes and volume, though it transports the Löwner ellipsoid itself. Historical originality is provisional, particularly against equivalent formulations for convex joins or free sums of squares under other names. No independent mathematical audit has been performed.

## References
[1] H. Ohsugi and A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, first publicly posted 2021-03-28, arXiv:2103.15045v1, published in *Discrete & Computational Geometry* 70 (2023), 214--235. https://arxiv.org/abs/2103.15045 ; https://doi.org/10.1007/s00454-022-00447-z

[2] *The exact Löwner ellipsoid of balanced complete-bipartite PQ-type adjacency polytopes*, research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-exact-l-wner-ellipsoid-of-balanced-complete-bipartite-pq-typ--eed12b121d5b
