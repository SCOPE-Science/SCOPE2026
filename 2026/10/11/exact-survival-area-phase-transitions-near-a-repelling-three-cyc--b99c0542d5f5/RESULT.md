# Exact survival-area phase transitions near a repelling three-cycle

## Finding
For the absolute-value map
\[
F_b(x,y)=(|x|-y-1,\ x-|y|+b),\qquad \frac34<b<2,
\]
write \(Q_4=\{x>0,y<0\}\) and \(Q_2=\{x<0,y>0\}\). For each integer \(n\geq1\), let \(E_n(b)\) consist of points whose first \(3n\) iterates, numbered \(0,\ldots,3n-1\), have the consecutive strict quadrant pattern \((Q_4,Q_2,Q_2)^n\). The boundary-excluded definition is used for the dynamics, and closure is used for polygon calculations. All area identities are unchanged by this distinction.

Let \(r_b=((2-b)/5,-(2b+1)/5)\). This is the repelling period-three orbit's \(Q_4\) point, already identified in the cited 2024 work. The new quantitative assertion has two parts. First, **every** \(3/4<b<2\) obeys, for integers \(n\geq8\),
\[
\overline{E_{n+8}(b)}-r_b=4096^{-1}(\overline{E_n(b)}-r_b),
\qquad |E_{n+8}(b)|=8^{-8}|E_n(b)|.
\]
Here \(|\cdot|\) denotes ordinary two-dimensional Lebesgue area and an overline denotes closure.

Second, for every \(1\leq b<2\) and every integer \(n\geq3\), the **exact** area, not only an asymptotic equivalent, is
\[
|E_n(b)|=8^{-n}C(b),\quad
C(b)=\begin{cases}
1,&1\leq b\leq3/2,\\
4(b-1)(2-b),&3/2\leq b\leq7/4,\\
12(2-b)^2,&7/4\leq b<2.
\end{cases}
\]
The overlapping endpoint formulas coincide. In particular \(C(b)\sim12(2-b)^2\) as \(b\uparrow2\). These values quantify the planar sizes of finite transient neighborhoods that imitate the repelling orbit through the prescribed itinerary.

## Assumptions and scope
All parameters and coordinates are real. Let \(c=(2-b)/5\), \(d=(2b+1)/5\), and \(e=(4b-3)/10\), so \(c,d,e>0\) on \(3/4<b<2\). Define \(M=\begin{pmatrix}2&2\\-2&2\end{pmatrix}\) and \(N=M^{-1}=\frac14\begin{pmatrix}1&-1\\1&1\end{pmatrix}\). For the first three iterates, the itinerary's closed displacement set is the convex polygon
\[
D_b=\{(u,v):u\geq-c,\quad v\leq e,\quad v-u\geq-c,\quad v+u\geq-d\}.
\]
It is bounded and contains the origin in its interior throughout the stated open parameter range. For \(b\geq1\), it is the triangle with counterclockwise vertices
\[
(-c,-2c),\qquad(c+e,e),\qquad(-c,e).
\]
The result does not determine unconditional global orbit escape, invariant-graph hitting times, or the measure of a full basin. An initial point is counted only while it follows this specific repeating quadrant pattern.

## Proof
**Step 1: Exact itinerary geometry.** On \(Q_4\), the linear part of \(F_b\) is \(A_4=\begin{pmatrix}1&-1\\1&1\end{pmatrix}\); on \(Q_2\) it is \(A_2=\begin{pmatrix}-1&-1\\1&-1\end{pmatrix}\). Direct substitution gives
\[
r_b\longmapsto ((b-2)/5,(2b+1)/5)
\longmapsto (-(3b+4)/5,(4b-3)/5)
\longmapsto r_b.
\]
The three-step linear part is \(A_2^2A_4=M\), whose eigenvalues are \(2\pm2i\), and whose determinant is \(8\). Put \((x,y)=r_b+(u,v)\). The six quadrant sign constraints on the first three images simplify, using \(3/4<b<2\), to the four defining halfspaces of \(D_b\). Specifically, the constraints \(v\leq d\) and \(u\geq-(3b+4)/10\) are redundant because \(v\leq e<d\) and \(u\geq-c>-(3b+4)/10\).

Within the prescribed itinerary, the displacement after a block of three steps is \(M(u,v)\). Thus the closures of the survivor cylinders have the exact identity
\[
S_n:=\overline{E_n(b)}-r_b
=\bigcap_{k=0}^{n-1}N^kD_b.
\tag{1}
\]
The sets are convex polygons with positive area for finite \(n\); their boundaries are finite unions of line segments.

**Step 2: Universal eight-block identity.** The matrix \(N\) is rotation by \(\pi/4\) composed with contraction by \(8^{-1/2}\). Consequently \(N^8=4096^{-1}I\). Convexity and \(0\in D_b\) imply that for each residue \(j\) modulo \(8\), the sets \(N^{j+8m}D_b=4096^{-m}N^jD_b\) are nested as \(m\) increases. When \(n\geq8\), all eight residues occur in (1); for \(n+8\), each residue's most restrictive set is precisely \(4096^{-1}\) times the corresponding one for \(n\). Taking intersections proves \(S_{n+8}=4096^{-1}S_n\). Area scaling by the determinant \(4096^{-2}=8^{-8}\) proves the first law. This argument works for the full open interval \(3/4<b<2\), including the quadrilateral \(D_b\) for \(b<1\).

**Step 3: The three finite stabilization regimes.** For \(1\leq b\leq3/2\), the displayed triangle \(D_b\) has area \(1/8\), and direct substitution of its vertices in the four inequalities defining \(D_b\) proves \(ND_b\subseteq D_b\). Hence \(S_n=N^{n-1}D_b\) for all \(n\geq1\), and its area is \(8^{-n}\).

For \(3/2\leq b\leq7/4\), define the convex polygon \(P_b\) by the counterclockwise vertex sequence
\[
(c/4,-3c/4),\quad
(c/4,c/4+e/2),\quad
(-c,-c+e/2),\quad
(-c,c/2).
\]
At the first endpoint two vertices coincide, so the polygon is triangular. Computing the defining halfplanes gives \(S_2=P_b\), and checking those halfplanes at the four vertices of \(NP_b\) gives \(NP_b\subseteq P_b\). Thus \(S_n=N^{n-2}P_b\) for \(n\geq2\). Direct polygon integration or the shoelace formula gives
\[
|P_b|=\frac{(b-1)(2-b)}{16},
\]
so \(|S_n|=4(b-1)(2-b)8^{-n}\).

For \(7/4\leq b<2\), put \(\eta=2-b\) and let \(Q\) be the fixed quadrilateral with counterclockwise vertices
\[
(1/20,-1/40),\quad(-1/5,9/40),\quad
(-1/5,1/10),\quad(-3/40,-1/40).
\]
The twelve halfplanes defining \(D_b\cap ND_b\cap N^2D_b\) reduce exactly to \(S_3=\eta Q\). Moreover \(NQ\subseteq Q\), and \(|Q|=3/128\). Hence for all \(n\geq3\), \(S_n=\eta N^{n-3}Q\), with
\[
|S_n|=(2-b)^2\frac3{128}\,8^{-(n-3)}
=12(2-b)^2 8^{-n}.
\]
The boundary values at \(b=3/2\) and \(b=7/4\) agree by continuity (and the explicitly given polygons). Combining the three expressions establishes the claim.

**Step 4: Uniform verification of all parameter values.** The algebra in Step 3 can be checked without sampling continuous parameters. For \(j=1,2,3\), the halfplanes of \(\bigcap_{k=0}^{j-1}N^kD_b\) have fixed normal vectors and offsets affine in \(b\). In each of the three closed parameter subintervals, every proposed vertex of \(D_b\), \(P_b\), or \((2-b)Q\) is affine in \(b\). Therefore vertex feasibility, supporting-edge equality, and invariance \(N\mathcal P_b\subseteq\mathcal P_b\) are each *affine endpoint checks*. For each polygon edge, the same fixed normal is supporting at both interval endpoints; this proves equality of the candidate polygon and the whole halfplane intersection, not merely inclusion. The exact-rational executable included with this result performs these endpoint tests and the area and matrix identities. Positivity of polygon area in each open interval follows from the displayed formulas; \((2-b)Q\) is a positive homothety for \(b<2\). All arguments therefore hold for every real parameter in the claimed ranges, not just tested rational values.

## Verification
Run the self-contained exact arithmetic script \(\texttt{python3 verify.py}\) from the extracted package directory. It uses only the Python standard library and prints \(\texttt{EXACT\_AFFINE\_FACET\_CERTIFICATE\_OK}\) after checking the three parameter intervals, all moving supporting edges, inclusion of their inverse images, exact polygon areas, and \(N^8=4096^{-1}I\). No numerical integration or finite-difference approximations are used. The separate reasoning in Step 2 proves the infinite-index recurrence beyond the finite certificate.

## Relationship to prior work
Cima, Gasull, Mañosa, and Mañosas determine the map's invariant graphs and its period-three \((4,2,2)\) orbit, including its expanding return matrix, in their 2024 preprint, especially Section 4.1, equation (8), and the analysis of \(1<b<2\) in Section 5.6. That existence/classification is **not new here**. The new assertion concerns Lebesgue areas of sets of arbitrary planar initial conditions that keep the same transient itinerary, their sharp \(b=3/2\) and \(b=7/4\) phase changes, and the exact eight-block rescaling. Their subsequent study concentrates on topological entropy and invariant-graph \(\omega\)-limits, a different measure and dynamical question. The expansion determinant alone suggests geometric scaling but does not determine the parameter-dependent constants or exact finite stabilization thresholds.

## Limitations
No claim is made that points leaving the \((4,2,2)\) itinerary necessarily escape to infinity; many trajectories enter an attracting invariant graph. The exponent and coefficients concern **conditional transient itinerary cylinders in planar Lebesgue area**, not the invariant measure on that graph. The simple three-piece coefficient \(C(b)\) is established only for \(1\leq b<2\); on \(3/4<b<1\) the universal eight-block renormalization holds, but no universal closed coefficient is asserted. Strict quadrant-boundary trajectories are excluded; their zero area does not alter any area formula. This is a deterministic, exact result and has not undergone independent mathematical review. Unrecognized equivalent deductions in earlier work remain a priority risk.

## References
1. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052 (first public version, 2024-10-01), especially Sections 4.1 and 5.6. https://arxiv.org/html/2410.01052v2
2. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Entropy and omega-limit sets on invariant graphs for a class of planar piecewise linear maps*, arXiv:2503.02411 (2025), especially introductory statements and invariant-graph measure results. https://arxiv.org/html/2503.02411v4
