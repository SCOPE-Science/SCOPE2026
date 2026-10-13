# Sharp RK4 positivity intervals on every unweighted path and cycle

## Finding

For the unit-rate heat equation \(u'(t)=-L_Gu(t)\) on a finite connected simple graph \(G\) of maximum degree at most two, one classical fourth-order explicit Runge–Kutta end step is \(T_G(h)=R(-hL_G)\), where
\[
R(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}.
\]
For every real timestep \(h\ge0\), \(T_G(h)\) is entrywise nonnegative **if and only if** \(0\le h\le H_G\). The following table gives the complete sharp classification; \(P_n\) denotes the path on \(n\) vertices and \(C_n\) the simple cycle on \(n\) vertices.

| Graph | Sharp endpoint \(H_G\) |
| --- | --- |
| \(P_1\) | \(+\infty\) |
| \(P_2\) | \(a\) |
| \(P_3\) | \(b\) |
| \(P_4\) | \(2/3\) |
| \(P_5\) | \(4/7\) |
| \(P_n\), \(n\ge6\) | \(1/2\) |
| \(C_3\) | \(b\) |
| \(C_4\) | \(c\) |
| \(C_5\) | \(d\) |
| \(C_6\) | \(1/2\) |
| \(C_7\) | \(4/7\) |
| \(C_n\), \(n\ge8\) | \(1/2\) |

Here \(a,b,c,d\) are the respective **unique positive** roots of
\[
\begin{aligned}
3-3a+2a^2-a^3&=0,\\
8-12b+12b^2-9b^3&=0,\\
3-6c+8c^2-8c^3&=0,\\
24-48d+60d^2-55d^3&=0,
\end{aligned}
\]
with approximate values \(a=1.3926467817\), \(b=0.9284311878\), \(c=0.6963233909\), and \(d=0.7203257332\). In particular, positivity cutoffs are **not monotone in cycle size**: \(H_{C_5}>H_{C_4}\) and \(H_{C_7}>H_{C_6}\). For a possibly disconnected simple graph of maximum degree at most two, the cutoff is the minimum among its connected-component cutoffs (with isolated vertices imposing no restriction).

## Assumptions and scope

Each edge has diffusion rate one. The Laplacian has \((L_G)_{vv}=\deg(v)\), \((L_G)_{vw}=-1\) on an edge, and zero elsewhere. Graphs are undirected and simple. Positivity means preservation of the nonnegative orthant by the **completed RK4 step**, for every nonnegative input; no assertion is made about intermediate stage vectors. This is an exact-arithmetic statement for every real \(h\ge0\). The cycle convention starts at \(n=3\); a path with one vertex has zero Laplacian.

## Proof

Write \(Q=-L_G\), and \(T(h)=\sum_{k=0}^4h^kQ^k/k!\). Because \(Q\mathbf1=0\), every row of \(T(h)\) sums to one. Since the graph is undirected, \(Q\) is symmetric nonpositive definite. For every \(x\ge0\), Taylor's integral remainder gives
\[
R(-x)=e^{-x}+\frac{x^5}{24}\int_0^1(1-t)^4e^{-tx}\,dt>0.
\]
By the spectral theorem every diagonal entry of \(T(h)\) is positive. An off-diagonal entry at graph distance greater than four vanishes, while one at distance exactly four equals \(h^4\) times a positive integer divided by \(24\).

**Short-distance lemma.** For every \(P_n\) and \(C_n\), the entries at graph distance one or two are positive whenever \(0<h\le2/3\). Indeed a distance-one entry, divided by \(h\), is one of these seven cubic polynomials:
\[
\begin{gathered}
1-h+\frac23h^2-\frac13h^3,\qquad
1-\frac32h+\frac32h^2-\frac98h^3,\\
1-\frac32h+\frac32h^2-\frac76h^3,\qquad
1-2h+\frac52h^2-\frac94h^3,\\
1-2h+\frac52h^2-\frac{55}{24}h^3,\qquad
1-2h+\frac52h^2-\frac73h^3,\\
1-2h+\frac83h^2-\frac83h^3.
\end{gathered}
\]
A distance-two entry, divided by \(h^2\), is one of five quadratics:
\[
\begin{gathered}
\frac12-\frac23h+\frac{13}{24}h^2,\qquad
\frac12-\frac56h+\frac56h^2,\qquad
\frac12-h+\frac76h^2,\\
1-2h+\frac73h^2,\qquad
\frac12-h+\frac{29}{24}h^2.
\end{gathered}
\]
This list follows by multiplying \(Q\) at most four times: a contributing walk has length at most four, so each vertex pair sees only its four-step neighborhood; the connected geometry is a truncated path or a short cycle. For paths with at least ten vertices and cycles with at least nine vertices no new local walk pattern can occur, since the opposite boundary or the alternative cyclic arc is beyond four steps. The finitely many shorter path and cycle configurations together with these stable local neighborhoods give precisely the seven and five polynomials displayed. The respective possible boundary patterns produce precisely the seven and five polynomials displayed. In Bernstein form after \(h=2t/3\), \(0\le t\le1\), the coefficientwise lower bounds across all seven cubics are \((1,5/9,13/27,5/81)\), and those across all five quadratics are \((1/2,1/6,8/27)\). Every Bernstein basis function is nonnegative on this interval and the coefficients are strictly positive. This proves the lemma; the standalone checker independently reconstructs every polynomial from graph-walk products.

At graph distance three, the only contributions are a positive \(h^3\) term from length-three shortest paths and a fourth-degree term from one diagonal stay on such paths and possibly an extra length-four path around a short cycle. Directly counting those walks gives the decisive entries:
\[
\begin{array}{c|c|c}
G&\text{vertices}&T(h)_{uv}\\ \hline
P_4&1,4&h^3(4-6h)/24\\
P_5&1,4&h^3(4-7h)/24\\
P_n\ (n\ge6)&2,5&h^3(4-8h)/24\\
C_6&0,3&h^3(8-16h)/24\\
C_7&0,3&h^3(4-7h)/24\\
C_n\ (n\ge8)&0,3&h^3(4-8h)/24.
\end{array}
\]
For each row, all shorter-distance entries remain positive up to the listed first zero (which never exceeds \(2/3\)), by the short-distance lemma, and all farther-distance entries are nonnegative. Above the first zero the indicated distance-three entry is strictly negative. This proves all path cases from \(P_4\) upward and cycle cases from \(C_6\) upward.

For \(P_2,P_3,C_3,C_4,C_5\), direct expansion gives the unique potentially sign-changing off-diagonal entry \(h g(h)/m\), with \((g,m)\) respectively
\[
\begin{array}{c|c|c}
P_2&(3-3h+2h^2-h^3)&3\\
P_3,C_3&(8-12h+12h^2-9h^3)&8\\
C_4&(3-6h+8h^2-8h^3)&3\\
C_5&(24-48h+60h^2-55h^3)&24.
\end{array}
\]
The derivative of each displayed cubic is strictly negative on \([0,\infty)\), because each derivative is a downward-opening quadratic with negative discriminant. Thus each cubic has exactly one positive zero, and changes sign there. Every other off-diagonal polynomial on these graphs is nonnegative for all \(h\ge0\): for \(P_3\), the distance-two coefficient is \(h^2(13h^2-16h+12)/24\); for \(C_4\), it is \(h^2(7h^2-6h+3)/3\); and for \(C_5\), it is \(h^2(5h^2-5h+3)/6\). Each quadratic has a positive leading coefficient and negative discriminant. Together with positive diagonals, this establishes all remaining cases and excludes any reentrant positivity interval. Finally, Laplacians and their RK4 steps of disjoint unions are block diagonal, proving the componentwise assertion.

## Verification

Run `python3 verify.py` with the Python standard library. The program computes \(Q^k\) with exact integer graph-walk recurrences, divides coefficients by \(k!\) using rational arithmetic, checks all seven nearest-neighbor and five distance-two polynomial types, and certifies their positive Bernstein coefficients over \([0,2/3]\). It also checks entrywise positivity equivalences for 57 individual path/cycle sizes and 13 exact-rational timesteps per size, totalling 245752 exact matrix-entry tests. The infinite family follows from the finite-radius walk argument, not from sampling a finite list of graph sizes.

## Relationship to prior work

Fekete, Ketcheson and Lóczi (arXiv:1610.00228, initially submitted 2016-10-02) investigate positivity of explicit Runge–Kutta schemes, including a periodic second-order heat stencil. Their Section 6.2 develops general step-size criteria for two-stage schemes under potentially spatially varying diffusion; it does not give the present fourth-order, unweighted-path-and-cycle all-size classification. Khalsaraei (2015, DOI below) studies classical RK4 positivity on more general semidiscrete and flux-limited models with advection test cases, without these exact graph-size-dependent thresholds. Horváth (1998, DOI below) establishes general Runge–Kutta positivity radii, rather than the individual sharp endpoints here. Horváth (2005, DOI below) analyzes positivity thresholds and positive invariant cones, including finite-difference Dirichlet heat systems tested with a theta method, two-stage Lobatto IIIC, and two-stage Radau IIA; it does not address sharp classical RK4 end-step entrywise thresholds on every path and periodic cycle. The full 1998 and 2005 primary texts were inspected for this comparison. The well-known linear stability and positivity polynomial techniques remain foundational; this finding is the specialized complete graph-topological cutoff classification, not a claim to have invented RK positivity theory.

## Limitations

The results classify end-step **entrywise nonnegativity** on unit-weight unweighted paths and cycles, not intermediate-stage positivity, asymptotic accuracy, or positivity for arbitrary weighted or directed graphs. Graph sizes are unrestricted but graph degree is at most two. The short-distance classification is a finite walk calculation; code checks help detect errors but are not themselves a proof for infinitely many sizes. Historical priority is not conclusively established, and an overlooked specialization in older numerical-PDE literature remains possible.

## References

1. I. Fekete, D. I. Ketcheson, L. Lóczi, *Positivity for convective semi-discretizations*, arXiv:1610.00228 (first submitted 2016-10-02), especially Section 6.2. https://arxiv.org/abs/1610.00228
2. M. Mehdizadeh Khalsaraei, *Positivity of an explicit Runge–Kutta method*, Ain Shams Engineering Journal (2015), DOI:10.1016/j.asej.2015.05.018.
3. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, DOI:10.1016/S0168-9274(98)00050-6.
4. S. Gottlieb, C.-W. Shu, E. Tadmor, *Strong stability-preserving high-order time discretization methods*, SIAM Review 43 (2001), 89–112, DOI:10.1137/S003614450036757X.
5. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, DOI:10.1016/j.apnum.2004.08.026.
