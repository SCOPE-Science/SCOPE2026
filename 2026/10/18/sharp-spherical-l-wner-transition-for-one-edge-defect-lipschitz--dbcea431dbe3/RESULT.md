# Sharp spherical Löwner transition for one-edge-defect Lipschitz dual balls

## Finding
For every integer \(p\ge2\), let \(G_p=K_{p+2}\setminus\{bc\}\), the unit-edge complete graph with exactly one edge removed. Its shortest-path metric has distance \(2\) between \(b,c\) and distance \(1\) between all other distinct vertices. Let
\[
H=\{x\in\mathbb R^{p+2}:\sum_{v}x_v=0\},\qquad Q_p=\{x\in H:|x_u-x_v|\le1\text{ for all }uv\in E(G_p)\}.
\]
Write \(A\) for the \(p\) vertices other than \(b,c\), and \(B=\{b,c\}\). Let \(P_A\) be the orthogonal projection in \(H\) onto the zero-sum variations supported on \(A\), \(P_B\) the projection onto the span of \(e_b-e_c\), and \(P_C=I_H-P_A-P_B\). Their ranks are \(p-1,1,1\).

**Theorem.** The unique least-intrinsic-volume Euclidean ellipsoid containing \(Q_p\) is
\[
E_p=\{x\in H:u_p\|P_Ax\|_2^2+v_p\|P_Bx\|_2^2+w_p\|P_Cx\|_2^2\le1\},
\]
where \((u_p,v_p,w_p)\), the inverse squared semiaxes, are exactly
\[
\begin{array}{c|ccc}
p&u_p&v_p&w_p\\\hline
2&3/2&1/2&1\\
3&1&1/2&5/8\\
4&3/4&1/2&7/12\\
5&13/21&1/2&1/2\\
p\ge6&R_p^{-2}&R_p^{-2}&R_p^{-2}
\end{array},\qquad R_p^2=\frac{\lfloor(p+2)^2/4\rfloor}{p+2}.
\]
In particular, **the optimal ellipsoid is spherical if and only if \(p\ge6\)**. Precisely from that threshold onward, it equals the Löwner ellipsoid of the unmodified equilateral \((p+2)\)-point Lipschitz dual ball, although \(Q_p\) is strictly larger than that equilateral ball. At \(p=6\), some additional vertices created by the missing edge remain tangent; for every \(p\ge7\), all additional vertices are strictly interior. Its intrinsic Euclidean volume, for \(d=p+1\), is
\[
\operatorname{vol}_d(E_p)=\frac{\pi^{d/2}}{\Gamma(1+d/2)}\,u_p^{-(p-1)/2}v_p^{-1/2}w_p^{-1/2}.
\]

## Assumptions and scope
All potentials are real. The ellipsoid and the measure are taken in the specified canonical Euclidean hyperplane, not arbitrary anchored coordinates. Every \(p\ge2\) is covered, with the graph metric fixed as above; this is not a classification of weighted missing edges or of all graphs. The John ellipsoid (largest ellipsoid *inside* \(Q_p\)) is not being computed. The result concerns the **Löwner ellipsoid outside** \(Q_p\), equivalently under polarity the John ellipsoid of the primal Lipschitz-free ball.

## Proof
**1. Symmetry reduction and objective.** The finite symmetry group \(S_p\times S_2\) acts orthogonally on \(H\); central inversion also preserves \(Q_p\). Uniqueness of the minimal enclosing ellipsoid first forces its center to be zero. The three subspaces \(P_AH,P_BH,P_CH\) are mutually inequivalent irreducible real representations, so its inverse shape operator must have the form \(D=uP_A+vP_B+wP_C\), with \(u,v,w>0\). Minimizing its volume is equivalent to maximizing the strictly concave function
\[
f(u,v,w)=(p-1)\log u+\log v+\log w
\]
subject to the linear inequalities \(u\|P_Ax\|^2+v\|P_Bx\|^2+w\|P_Cx\|^2\le1\) for each vertex \(x\) of \(Q_p\). Since \(p\ge2\), strict concavity gives uniqueness among invariant ellipsoids and the original uniqueness gives global optimality.

**2. All vertex types.** Fix one potential coordinate on \(A\) to zero. The resulting edge-difference constraint matrix is a submatrix of an oriented graph incidence matrix, hence totally unimodular, with integral right-hand side. Thus all vertices have integral coordinate differences. The clique inequalities force the values on \(A\) to have range at most \(1\).

If that range equals \(1\), translate the minimum of \(A\) to \(0\). Precisely \(i\in\{1,\ldots,p-1\}\) of its vertices have value \(1\), and the other \(p-i\) have value \(0\); both \(b,c\) have values in \(\{0,1\}\), with \(j\in\{0,1,2\}\) ones. Call this type \(\mathrm I(i,j)\).

If the \(A\)-values have range zero, translate them all to zero. Because the tight-edge graph of a vertex must be connected, each of \(b,c\) must be incident to a tight edge; neither \(b\) nor \(c\) is adjacent to the other, so each must have value \(\pm1\). Call the state with exactly \(j\) positive values type \(\mathrm{II}(j)\), for \(j\in\{0,1,2\}\). Conversely the tight-edge graphs of all listed states are connected, so they are exactly the vertices, modulo permutation and simultaneous sign reversal. The integer-vertex conclusion rules out intermediate clique heights; the connected-tight-edge criterion rules out the all-zero clique with an untight \(b\) or \(c\).

For a centered representative of \(\mathrm I(i,j)\), its three squared orthogonal projection lengths are
\[
(a,b,c)_{\mathrm I(i,j)}=\left(\frac{i(p-i)}p,\frac{j(2-j)}2,\frac{(2i-pj)^2}{2p(p+2)}\right).
\]
For a centered representative of \(\mathrm{II}(j)\), they are
\[
(a,b,c)_{\mathrm{II}(j)}=\left(0,2j(2-j),\frac{2p(j-1)^2}{p+2}\right).
\]
These follow by decomposing \(x\) into its two within-class centered vectors and its between-class mean difference, whose squared projection length is \(2p/(p+2)\) times the squared difference of class means. There are no unlisted vertex constraints.

**3. Exact small-case certificates.** For \(p=2,3,4,5\), substitute the claimed \((u,v,w)\). Exhaustive rational evaluation of the displayed formulas for \(\mathrm I\) gives the following maxima over \(j=0,1,2\), listed in increasing order of \(i=1,\ldots,p-1\); evaluations at \(\mathrm{II}(0),\mathrm{II}(1),\mathrm{II}(2)\) are also given:

| \(p\) | Maxima over \(j\), for consecutive \(i\) | Three type-II values |
| --- | --- | --- |
| 2 | \(1\) | \(1,1,1\) |
| 3 | \(1,1\) | \(3/4,1,3/4\) |
| 4 | \(1,1,1\) | \(7/9,1,7/9\) |
| 5 | \(20/21,1,1,20/21\) | \(5/7,1,5/7\) |

Hence all vertices satisfy \(x^{\mathsf T}Dx\le1\). To certify *optimality*, assign positive multiplier \(\alpha\) to each active orbit representative in the following table:

| \(p\) | Active types and multipliers \(\alpha\) |
| --- | --- |
| 2 | \(\mathrm I(1,0):4/3\), \(\mathrm{II}(1):1\), \(\mathrm{II}(0):2/3\) |
| 3 | \(\mathrm I(1,2):3\), \(\mathrm{II}(1):1\) |
| 4 | \(\mathrm I(1,2):16/7\), \(\mathrm I(2,1):16/7\), \(\mathrm{II}(1):3/7\) |
| 5 | \(\mathrm I(2,1):20/13\), \(\mathrm I(3,0):50/13\), \(\mathrm{II}(1):8/13\) |

In each row, writing \(t_k=(a_k,b_k,c_k)\) for its specified type, direct rational substitution verifies
\[
\sum_k\alpha_kt_k=\left(\frac{p-1}{u},\frac1v,\frac1w\right)=\nabla f(u,v,w),
\qquad \alpha_k>0,\quad u a_k+v b_k+w c_k=1.
\]
For every feasible positive \((u',v',w')\), concavity therefore gives
\[
f(u',v',w')\le f(u,v,w)+\nabla f(u,v,w)\cdot((u',v',w')-(u,v,w))\le f(u,v,w),
\]
because the last dot product is the weighted sum of nonpositive changes in active vertex inequalities. Thus the four displayed triples are precisely the global maximizers.

**4. Universal spherical regime and sharp boundary.** Let \(Q^{\mathrm{eq}}_{p+2}\) denote the equilateral potential ball, where even the \(b,c\) difference is at most \(1\). It lies properly inside \(Q_p\). Permutation invariance under \(S_{p+2}\) and central symmetry force its unique Löwner ellipsoid to be a centered Euclidean ball. Its vertices have two \(0/1\) levels with \(k\) ones, and squared norm \(k(p+2-k)/(p+2)\). Hence its minimal enclosing ball has squared radius
\[
R_p^2=\frac{\lfloor(p+2)^2/4\rfloor}{p+2}.
\]
For every type-I vertex of \(Q_p\) the same equilateral bound holds because it also has only \(0/1\) entries. For every type-II vertex, the squared norm is at most \(2\), with equality only for \(\mathrm{II}(1)\). Exactly when \(p\ge6\) does \(R_p^2\ge2\). Therefore for \(p\ge6\) the equilateral optimal sphere contains the entire larger \(Q_p\), yet no smaller-volume ellipsoid can contain the equilateral subset. This proves equality of Löwner ellipsoids, uniqueness, and the claimed threshold. If \(p=6\), \(R_p^2=2\), giving tangency of \(\mathrm{II}(1)\); if \(p\ge7\), \(R_p^2>2\), giving strict interiority of all type-II vertices. The rational small-case table proves that no \(p\le5\) has a spherical optimal ellipsoid. The claimed intrinsic-volume expression follows by multiplying orthogonal semiaxis lengths.

## Verification
Run \(`python3 checker.py`\) in the same directory as this document. The script uses Python standard-library \(`fractions.Fraction`\), evaluates *every* type-I and type-II orbit inequality for \(p=2,3,4,5\), verifies exact positive multiplier identities, and checks the spherical inequalities and contact boundary for integers \(6\le p<500\). The independent, symbolic all-dimensional proof is in Steps 1–4; checks at finitely many values are not used to infer an infinite theorem.

## Relationship to prior work
Finite metric Lipschitz dual balls are polars of Lipschitz-free balls, as described by Alexander–Fradelizi–García-Lirola–Zvavitch (arXiv:1911.10642). Aliaga (arXiv:2102.01219) studies extremal molecules in Lipschitz-free spaces, supplying related geometry but not this enclosing-ellipsoid calculation. The general log-determinant and optimal-design equivalence is treated by Suliman–Weinstein (arXiv:2302.05966); this framework does not specify the one-edge-defect formulas or the \(p=6\) and \(p=7\) contact transitions. Calculations of **inscribed ellipsoids in the dual potential ball**, and of **circumscribed ellipsoids of the polar symmetric-edge polytope**, address the opposite extremal problem and do not imply this theorem. The known equilateral optimal-ball formula is used, not claimed as new.

## Limitations
The theorem is a self-contained all-dimensional calculation for one missing edge, not for arbitrary edge removals or weighted edges. It depends on the fixed canonical Euclidean normalization; the numerical ellipsoid is not invariant under arbitrary nonorthogonal coordinate choices. Existing general ellipsoid characterizations could imply parts of this result when specialized, and undiscovered equivalent graph-specific formulas remain a bibliographic risk. Independent external validation has not been performed.

## References
1. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public version 2019-11-24), https://arxiv.org/abs/1911.10642.
2. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first public version 2021-02-01), https://arxiv.org/abs/2102.01219.
3. A. Suliman, O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966 (first public version 2023-02-12), https://arxiv.org/abs/2302.05966.
