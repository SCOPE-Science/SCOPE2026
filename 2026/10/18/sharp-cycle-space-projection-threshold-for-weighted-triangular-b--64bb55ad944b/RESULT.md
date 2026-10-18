# Sharp cycle-space projection threshold for weighted triangular books

## Finding

For integers \(m\ge 2\) and real \(0<t\le 2\), let \(G_{m,t}\) be the weighted graph with hubs \(a,b\), leaves \(v_1,\ldots,v_m\), hub edge of length \(t\), and two unit-length spokes from each leaf to the hubs. Orient its edges as \(c:a\to b\), \(x_i:a\to v_i\), and \(y_i:v_i\to b\). Let \(X_{m,t}=\mathbb R^{E(G_{m,t})}\), equipped with the edge-cost norm
\[
\|f\|_{1,t}=t|f_c|+\sum_{i=1}^m (|f_{x_i}|+|f_{y_i}|).
\]
Write \(Z_{m,t}=\ker\partial\subset X_{m,t}\) for the real cycle-flow space, where \(\partial\) is the usual oriented incidence map, and let
\[
\lambda(m,t)=\inf\{\|P\|_{X_{m,t}\to X_{m,t}}:P^2=P,\ \operatorname{ran}P=Z_{m,t}\}.
\]
Then the infimum is attained and its exact value is
\[
\boxed{\lambda(m,t)=
\begin{cases}
1+\dfrac t2, &m(2-t)\ge 4,\\[5pt]
\dfrac{m(t+2)^2}{m(t^2+4)+4t}, &m(2-t)\le 4.
\end{cases}}
\]
The formulas coincide when \(m(2-t)=4\). In the regime \(m(2-t)\ge4\), there is an optimal projection annihilating the common hub-edge coordinate. When \(m(2-t)<4\), every optimal projection that is invariant under permutations of leaves and interchange of hubs has nonzero image on that coordinate.

In particular, for the unweighted triangular book \(t=1\), the exact constants are
\[
\lambda(2,1)=\frac97,\qquad \lambda(3,1)=\frac{27}{19},\qquad
\lambda(m,1)=\frac32\quad(m\ge4).
\]
Thus a sharp four-page saturation occurs, while at a fixed \(m\ge3\) the switching length is \(t_c=2-4/m\).

## Assumptions and scope

The scalar field and all projections are real. The edge-cost norm is determined by the stated **weighted graph presentation**, not just an abstract isometry class of the quotient space. At \(t=2\) the hub edge is metrically redundant; it is nonetheless retained as an edge-space coordinate, as specified. The graph-metric interpretation is valid for \(0<t\le2\). The claim concerns the minimum operator norm of a projection **onto** the cycle space inside the weighted edge \(\ell_1\)-space; it does not identify the norm of the complementary projection or a Banach--Mazur distance.

## Proof

**1. Cycle coordinates.** The vectors
\[
 z_i=e_{x_i}+e_{y_i}-e_c\qquad(1\le i\le m)
\]
lie in \(\ker\partial\) and are linearly independent because their \(x_i\)-coordinates are distinct. The connected graph has \(2m+1\) edges and \(m+2\) vertices, hence its cycle rank is \(m\); therefore \(Z_{m,t}=\operatorname{span}\{z_1,\ldots,z_m\}\). For arbitrary scalars \(\beta_i\), the norm has the particularly simple form
\[
\left\|\sum_{i=1}^m\beta_i z_i\right\|_{1,t}
=2\sum_{i=1}^m|\beta_i|+t\left|\sum_{i=1}^m\beta_i\right|.
\]

**2. Symmetrization without loss.** Every permutation of the leaves and the interchange of the two hubs induce signed coordinate-permutation isometries of \(X_{m,t}\) preserving \(Z_{m,t}\). Averaging any projection onto \(Z_{m,t}\) over this finite group gives a projection onto the same space of no larger norm. Therefore it suffices to minimize over such invariant projections. Hub interchange sends \(e_c\) to \(-e_c\), \(e_{x_i}\) to \(-e_{y_i}\), and \(z_i\) to \(-z_i\). Permutation invariance and hub interchange force any invariant projection to have, for a single real parameter \(u\),
\[
P_u e_c=u\sum_{j=1}^m z_j,\qquad
P_u e_{x_i}=P_u e_{y_i}=
\frac{1+u}{2}z_i+\frac{u}{2}\sum_{j\ne i}z_j.
\]
Indeed, before imposing the projection identity the two coefficients in the spoke image are arbitrary, while the cycle identity \(P_uz_i=z_i\) forces their values to be \((1+u)/2\) and \(u/2\). Conversely the displayed prescriptions define a projection for every \(u\in\mathbb R\), because \(P_uz_i=z_i\) and every image lies in \(Z_{m,t}\).

**3. Exact norm optimization.** Since the domain is weighted \(\ell_1\), an operator's norm is the largest norm of a coordinate-column image divided by that coordinate's weight. Hence
\[
\|P_u\|=\max\left\{\frac{m(2+t)}{t}|u|,\ |1+u|+(m-1)|u|+\frac t2|1+mu|\right\}. \tag{1}
\]
For \(u\ge0\), the second expression is \((1+t/2)(1+mu)\), so no value smaller than \(1+t/2\) is possible there. Put \(u=-v\). For \(v\ge1/m\), the first expression increases strictly, and the second is also nondecreasing: on \([1/m,1]\) it equals \(1-t/2+[m(1+t/2)-2]v\), with positive slope for \(m\ge2,t>0\); on \([1,\infty)\) it again has positive slope. Thus no minimum requires \(v>1/m\).

For \(0\le v\le1/m\), formula (1) becomes
\[
 F(v)=\max\left\{\underbrace{\frac{m(2+t)}t v}_{L(v)},\;
\underbrace{1+\frac t2+\left[m\left(1-\frac t2\right)-2\right]v}_{H(v)}\right\}. \tag{2}
\]
If \(m(2-t)\ge4\), then \(H\) is nondecreasing; both functions have their smallest maximum at \(v=0\), giving \(1+t/2\). If \(m(2-t)<4\), then \(H\) is strictly decreasing and \(L\) strictly increasing. Their unique intersection is
\[
 v_*=\frac{t(t+2)}{m(t^2+4)+4t}.
\]
This point lies in \([0,1/m]\): the requisite inequality simplifies to \(2mt\le4m+4t\), which follows from \(t\le2\). The intersection gives \(\lambda(m,t)=L(v_*)=m(t+2)^2/[m(t^2+4)+4t]\). This proves the piecewise formula, attainability and the asserted symmetrized-projection behavior. At equality the branch expressions agree by (2). Substituting \(t=1\) yields the three unweighted values and the four-page threshold.

## Verification

The separate reproducibility script `verify.py` uses exact rational arithmetic to construct the projected cycle columns and verify the projection identity, the weighted-\(\ell_1\) column norm and the piecewise formula on a declared grid. Where SciPy is installed, it also independently solves the full **unsymmetrized** finite-dimensional linear program for small graphs. The latter is numerical corroboration; the group-averaging argument and the one-variable optimization above prove the result for every real \(t\) and every integer \(m\ge2\).

## Relationship to prior work

Ostrovska and Ostrovskii's work on transportation cost spaces gives the weighted-edge-space quotient by a cycle space, providing the Banach-space setting for asking how well that cycle subspace is complemented. Dilworth, Kutzarova and Ostrovskii use invariant projections to study recursive diamond and Laakso graphs, and discuss multibranching diamonds without a retained weighted spine edge. A later paper by the same authors studies invariant and minimum cycle-space projections and gives a general representation-theoretic uniqueness criterion, then analyzes discrete tori and Hamming graphs. Those structural results and graph-family computations do not state or imply the present exact two-parameter minimum for triangular books.

The result is different from geometric ellipsoid invariants of symmetric edge polytopes of book graphs, as well as coordinate suppression projections of cactus edge bases: an \(m\)-page triangular book with \(m\ge2\) is not a cactus, and the operator optimized here is a projection onto its **entire real cycle space** in the weighted \(\ell_1\) edge space. Search-based comparisons do not establish global uniqueness of this formula in the literature.

## Limitations

This theorem concerns the specified real weighted-edge presentation and is not an assertion about all \(\ell_1\)-representations of a metric's transportation cost space. At \(t=2\) the extra direct edge is redundant for shortest-path distances but remains relevant to the projection problem. No result for arbitrary unequal spoke lengths or arbitrary graphs is claimed. The bibliographic comparison covers the identified sources and records, not all possibly unindexed treatments; independent scholarly confirmation has not been performed.

## References

1. S. Ostrovska and M. I. Ostrovskii, *On relations between transportation cost spaces and \(\ell_1\)*, arXiv:1910.03625, first publicly submitted 2019-10-08; see §3 and Theorem 3.1. https://arxiv.org/abs/1910.03625
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, first publicly submitted 2018-07-10; see §§4–6 on cycle-space projections and diamond graphs. https://arxiv.org/abs/1807.03814
3. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, Proceedings of Symposia in Pure Mathematics 106 (2024), 97–131, doi:10.1090/pspum/106/01929; see §§1.4–1.6 and §2.1. https://denka.web.illinois.edu/CycleSpaces.pdf
