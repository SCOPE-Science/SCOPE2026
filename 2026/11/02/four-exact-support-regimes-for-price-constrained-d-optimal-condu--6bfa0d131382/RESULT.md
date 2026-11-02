# Four exact support regimes for price-constrained D-optimal conductance on book networks

## Finding

Let \(m\ge3\) be an integer, and let the book network \(G_m=K_2\vee\overline{K_m}\) have two hubs \(u,v\), a direct hub edge, and \(m\) independent page vertices, each adjacent to both hubs. Let independently variable nonnegative conductances on page \(i\) be \(x_i\) on \(u i\) and \(y_i\) on \(v i\); denote the hub conductance by \(z\). Per-unit conductance prices are \(P>0\) for the first spoke class, \(Q>0\) for the second class, and \(R>0\) for the hub edge. Under the budget \(P\sum_i x_i+Q\sum_i y_i+Rz=B>0\), maximize the weighted spanning-tree enumerator \(\tau=\det L^{(v)}\), where \(L^{(v)}\) is the weighted Laplacian grounded at \(v\).

**Theorem.** There is a unique optimizer among **all** independently adjustable edge conductances. It has \(x_i=x\) and \(y_i=y\) for every page. Its four exhaustive, nonoverlapping regimes (including the stated boundary conventions) are as follows.

**First spoke class deleted.** If \(P\ge Q+R\), then
\[
x=0,\qquad y=\frac{B}{(m+1)Q},\qquad z=\frac{B}{(m+1)R}.
\]

**Second spoke class deleted.** If \(Q\ge P+R\), then
\[
x=\frac{B}{(m+1)P},\qquad y=0,\qquad z=\frac{B}{(m+1)R}.
\]

**Hub edge deleted.** Otherwise, let \(r\) be the unique positive root
\[
Pr^2-m(Q-P)r-Q=0,
\quad
r=\frac{m(Q-P)+\sqrt{m^2(Q-P)^2+4PQ}}{2P},
\]
and set
\[
R_c=\frac{(Pr+Q)(r+1)}{(m+1)r}.
\]
If \(R\ge R_c\), then
\[
x=\frac{rB}{m(Pr+Q)},\qquad y=\frac{B}{m(Pr+Q)},\qquad z=0.
\]

**All edge classes retained.** In the remaining region, equivalently \(\lvert P-Q\rvert<R<R_c\), set
\[
s=\frac12\left(1+\frac{Q-P}{R}\right),\quad
 t=\frac{B}{(m+1)[P-R(1-s)^2]}.
\]
Then
\[
x=st,\qquad y=(1-s)t,\qquad
z=\frac{B}{(m+1)R}-m s(1-s)t.
\]
All three conductances are strictly positive in this region. The cutoff satisfies \(R_c>\lvert P-Q\rvert\).

In the equal-spoke-price case \(P=Q=S>0\), the hub is deleted exactly when \(R\ge4S/(m+1)\). In particular, for equal prices on **all** edges, every \(m\ge3\) has \(z=0\). This is a size-dependent support transition, not an assertion that all edge conductances are equal at the unrestricted optimum.

## Assumptions and scope

Graphs are finite, simple, undirected, and connected before allocation. The objective includes all spanning trees, weighted by the product of their edge conductances; it is zero if the positive-weight support disconnects the graph. All prices and the budget are strictly positive and real, with \(m\ge3\). No equal-weight or symmetry restriction is imposed on feasible designs. Zero conductances are allowed, and exact equality at a cutoff belongs to the corresponding edge-deletion regime.

## Proof

**1. Unrestricted uniqueness and symmetry.** Ground the weighted Laplacian at \(v\). For any connected positive-weight support, the grounded matrix is positive definite and \(\log\tau=\log\det L^{(v)}\) is strictly concave in its matrix argument. The linear map from distinct edge conductances to this grounded Laplacian is injective: off-diagonal entries identify edges between ungrounded vertices, and the remaining grounded-edge weights are recovered from diagonal entries. Thus \(\log\tau\) is strictly concave on the connected feasible set. A connected feasible point with positive determinant exists. The closed price simplex is compact, so a maximizer exists, and every maximum must be connected. Strict concavity yields exactly one maximizer. Permuting the \(m\) page vertices preserves prices, budget, and determinant, so uniqueness forces constant \(x_i=x\) and \(y_i=y\).

**2. Exact determinant.** With \(t=x+y>0\), grounding \(v\) gives a diagonal page block \(tI_m\), a hub diagonal entry \(mx+z\), and \(-x\) on each hub-to-page entry. Its Schur complement yields
\[
\tau=t^m\left(mx+z-\frac{mx^2}{t}\right)
=t^{m-1}\bigl(mxy+zt\bigr).
\]
Write \(D=mxy+zt>0\). Connectedness within the symmetric family requires \(t>0,D>0\).

**3. Global Karush–Kuhn–Tucker conditions.** Set \(F=\log\tau\). The reduced cost is \(m(Px+Qy)+Rz=B\). By homogeneity degree \(m+1\), the optimum's budget multiplier is \(\lambda=(m+1)/B\). Its marginal derivatives are
\[
F_x=\frac{m-1}{t}+\frac{my+z}{D},\qquad
F_y=\frac{m-1}{t}+\frac{mx+z}{D},\qquad
F_z=\frac{t}{D}.
\]
For each variable, its derivative is at most its cost times \(\lambda\); equality holds when that variable is positive. Thus \(F_x\le\lambda mP\), \(F_y\le\lambda mQ\), and \(F_z\le\lambda R\). These conditions are sufficient as well as necessary by concavity.

If \(x=0\), connectivity requires \(y,z>0\), and the active equations give \(y=B/[(m+1)Q]\) and \(z=B/[(m+1)R]\). The missing class inequality reduces *exactly* to \(P\ge Q+R\). Exchanging the hub labels yields the second deleted-spoke regime. These two price conditions cannot both hold.

If \(z=0\) and neither spoke class vanishes, connectivity requires \(x,y>0\). Put \(r=x/y\). Subtracting the two active spoke equations, together with the budget, gives \(Pr^2-m(Q-P)r-Q=0\). Its constant term is negative, so it has exactly one positive root. Solving the budget gives the stated \(x,y\). The absent-hub derivative inequality \(F_z\le\lambda R\) is equivalent to \(R\ge R_c\).

If \(x,y,z>0\), all marginal inequalities are equalities. From \(D=t/(\lambda R)\) and the spoke difference equation, \(y-x=(P-Q)t/R\); hence \(x=st\), \(y=(1-s)t\) with the stated \(s\). The first spoke equality can be rewritten as \(1/t=\lambda[P-R(1-s)^2]\), giving \(t\). Finally \(D=mxy+zt\) yields the formula for \(z\).

For completeness, \(R_c>\lvert P-Q\rvert\): when \(P\ge Q\), put \(d=P-Q\) and use the defining positive-root equation \(Pr^2+mdr=Q\). Then \((Pr+Q)(r+1)-(m+1)rd=r[P(1+r)^2+d(mr-1)]>0\), since \(P\ge d\) and \((1+r)^2+mr-1>0\). The other case follows by exchanging hub labels (equivalently replacing \(r\) with \(1/r\)). If the spoke deletion conditions fail, the hub-deletion condition either holds, giving that unique KKT optimum, or fails, forcing all classes strictly positive at the unique optimum. Thus the four regimes exhaust the positive price domain, and no additional support pattern can optimize. This completes the proof.

## Verification

For \(m=3\), \((P,Q,R,B)=(2,1,3/2,92)\) lies in the all-positive region and the optimum is \((x,y,z)=(4,20,16/3)\), with \(\tau=211968\). For \((P,Q,R,B)=(1,1,1/2,8)\), the optimum is \((8/7,8/7,16/7)\), with \(\tau=16384/343\). Both statements are exact rational identities.

The included standalone \(\texttt{verify.py}\) can be run with Python, NumPy, and SciPy. It independently recomputes grounded-Laplacian determinants; checks 28 exact rational determinant examples, 320 randomized budget/KKT cases, 160 direct numerical determinants, 44 successful unrestricted numerical optimizations, and 2,560 asymmetric feasible designs. These finite experiments corroborate, but do not replace, the proof for all real prices and integers \(m\ge3\).

## Relationship to prior work

Weighted Matrix–Tree and grounded-Laplacian log-determinant optimality are classical; the general formulation and applications to network D-optimality are discussed by Khosoussi et al. (arXiv:1604.01116), and graph formulations of experimental D-optimality by Bailey and Cameron (arXiv:1111.3768). Chestnut and Fishkind (arXiv:1208.4125) provide unweighted spanning-tree enumeration for threshold graphs, a family containing \(K_2\vee\overline{K_m}\). These sources establish the determinant framework or non-optimized counts but, in the examined material, do not state this independently priced, unrestricted book-network optimizer and its four exact support regimes. The theorem concerns a continuous edge-budget design, rather than a discrete edge-selection problem.

## Limitations

The allocation model assumes one shared price per spoke class and one hub-edge price, with an arbitrary positive real budget; it does not cover page-specific prices, additional leaf-to-leaf edges, directed networks, or nonlinear conductance costs. The optimal design may delete edges, but remains connected. The novelty comparison is bounded by the primary and mathematical-index sources examined and does not establish publication priority; specialized older sources could conceivably cover a mathematically equivalent classification.

## References

1. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116 (first posted 2016-04-05), https://arxiv.org/abs/1604.01116.
2. R. A. Bailey and P. J. Cameron, *Using graphs to find the best block designs*, arXiv:1111.3768 (first posted 2011-11-16), https://arxiv.org/abs/1111.3768.
3. S. R. Chestnut and D. E. Fishkind, *Counting Spanning Trees of Threshold Graphs*, arXiv:1208.4125 (first posted 2012-08-20), https://arxiv.org/abs/1208.4125.
