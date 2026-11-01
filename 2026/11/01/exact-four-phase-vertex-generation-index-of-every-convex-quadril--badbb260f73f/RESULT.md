# Exact four-phase vertex-generation index of every convex quadrilateral

## Finding
For a full-dimensional convex polygon \(P\) with vertex set \(V(P)\), define its **vertex-generation parameter** by
\[
\lambda(P)=\sup\{t\in[0,1]:P=tV(P)+(1-t)P\}.
\]
The right side is a Minkowski sum of a finite set and a convex polygon, not the convex hull of the sum. For every strictly convex quadrilateral \(Q\), choose an affine normalization
\[
Q=\operatorname{conv}\{(0,0),(1,0),(p,q),(0,1)\},\qquad p,q>0,\quad p+q>1.
\]
Write \(a=\min\{p,q\}\), \(b=\max\{p,q\}\), and \(k=p+q-1\). Then the exact, affine-invariant value is
\[
\boxed{\lambda(Q)=\begin{cases}
(3-a)^{-1},&b\le1,\\
\dfrac{b}{2b+1-a},&a\le1\le b,\quad a+b\le2,\\
\dfrac{b}{3b-1},&a\le1\le b,\quad a+b\ge2,\\
\dfrac{k}{2(a+b)-3+b},&a\ge1.
\end{cases}}
\]
The formulas coincide at all shared boundaries. In Schneider's normalization the corresponding sharp convexification threshold is
\[
\boxed{c(V(Q))=\lambda(Q)^{-1}-1},
\]
where \(c(V(Q))\) is the least \(s\ge0\) such that the nonconvex vertex set \(V(Q)+sQ\) becomes convex. Every genuine quadrilateral satisfies \(1/3<\lambda(Q)\le1/2\); the upper equality holds exactly for parallelograms. For the affine-symmetric kite family \(p=q=s>1/2\), the complete profile is \(\lambda=(3-s)^{-1}\) for \(s\le1\), and \(\lambda=(2s-1)/(5s-3)\) for \(s\ge1\).

## Assumptions and scope
A **strictly convex quadrilateral** here means four distinct vertices in cyclic order, with each interior angle strictly below \(\pi\) and no three collinear. The stated normalization follows by mapping three vertices \(A,B,D\), where \(B,D\) are both adjacent to \(A\), to \((0,0),(1,0),(0,1)\), and taking the remaining vertex \(C=(p,q)\); strict convexity gives the displayed parameter domain. The formulas are invariant under nonsingular affine maps and under the remaining choice of orientation or vertex labeling, although the pair \((p,q)\) itself depends on labeling.

All supremums are attained. For each point \(X\in Q\), a representation \(X=tv+(1-t)Y\), \(v\in V(Q)\), \(Y\in Q\), exists precisely when some convex barycentric representation of \(X\) over the four vertices has a coefficient at least \(t\). Thus \(\lambda(Q)\) is the minimum over \(X\in Q\) of the maximum achievable vertex coefficient. This is not a distributional or asymptotic statement.

## Proof
**1. Barycentric reduction.** Write \(X=(x,y)\) and order the vertices \(A=(0,0),B=(1,0),C=(p,q),D=(0,1)\). The affine representations over the four vertex triples are as follows; each ordered triple lists coefficients of its vertices:
\[
\begin{array}{ll}
ABC:&(1-x+(p-1)y/q,\ x-py/q,\ y/q),\\
ABD:&(1-x-y,\ x,\ y),\\
ACD:&(1-y+(q-1)x/p,\ x/p,\ y-qx/p),\\
BCD:&((p+(q-1)x-py)/k,\ (x+y-1)/k,\ (q-qx+(p-1)y)/k).
\end{array}
\]
For fixed \(X\), all nonnegative four-vertex barycentric representations form a closed segment because the affine dependence among the four vertices has a one-dimensional kernel. An affine coefficient achieves its maximum at an endpoint of that segment, and every such endpoint has a zero coordinate and hence is a triangle representation. Consequently the maximum possible vertex coefficient is the maximum of the six available coefficients in the two triangle representations containing \(X\).

The diagonals \(AC\) and \(BD\) partition \(Q\) into four closed triangular sectors, with respective available triangle pairs \((ABC,ABD)\) in the \(A\)-sector, \((ABC,BCD)\) in the \(B\)-sector, \((ACD,BCD)\) in the \(C\)-sector, and \((ACD,ABD)\) in the \(D\)-sector. Denote the minima of the respective six-coordinate maxima by \(m_A,m_B,m_C,m_D\). The common objective is continuous and all sector domains are compact, so
\[
\lambda(Q)=\min\{m_A,m_B,m_C,m_D\}.
\]

**2. First sector.** The \(A\)-sector is characterized by \(x+y\le1\), \(qx\ge py\), \(y\ge0\). The six coefficients are those of \(ABC\) and \(ABD\). One finds
\[
m_A=\begin{cases}
1/2,&p\ge1,\\
1/(3-p),&p\le1,\ q\le1,\\
q/(2q+1-p),&p\le1,\ q\ge1.
\end{cases}
\]
Indeed, for \(p\ge1\), the coefficients \(1-x+(p-1)y/q\) and \(x\) have maximum at least \(1/2\), with equality at the midpoint of \(AB\). For \(p,q\le1\), bounding every coefficient by \(z\) forces \(x\le z\), \(y/q\le z\), and hence
\[
z\ge1-x+(p-1)y/q\ge1-(2-p)z.
\]
Equality is attained at \((x,y)=(z,qz)\), \(z=1/(3-p)\). The witness belongs to the sector, since \(p+q>1\), and all remaining coefficients are at most \(z\). For \(p\le1\le q\), the coefficients \(x,y\) and \(1-x+(p-1)y/q\) force
\[
z\ge1-z+(p-1)z/q,
\]
so \(z\ge q/(2q+1-p)\). The witness \((x,y)=(z,z)\) is in the sector, and its six coefficients do not exceed \(z\).

**3. Second sector.** The \(B\)-sector is characterized by \(x+y\ge1\), \(qx\ge py\), and \(qx+(1-p)y\le q\). Its six coefficients come from \(ABC\) and \(BCD\). A direct, sharp calculation yields
\[
m_B=\begin{cases}
1/2,&q\le1,\\
q/(3q-1),&p\le1\le q,\\
k/(2p+3q-3),&p,q\ge1.
\end{cases}
\]
For \(q\le1\), the midpoint of \(BC\) gives \(1/2\). Conversely, if every coefficient were below \(1/2\), the \(ABC\) coordinates would give \(y<q/2\), \(x<1/2+py/q\); inserting these bounds into the \(BCD\) coefficient \((p+(q-1)x-py)/k\) gives a value greater than \(1/2\), a contradiction.

For \(p\le1\le q\), the identity
\[
q\frac{p+(q-1)x-py}{k}+(q-1)\frac{q-qx+(p-1)y}{k}=q-y
\]
and \(y/q\le z\) show \(q\le(3q-1)z\). Equality is attained at
\[
z=\frac{q}{3q-1},\quad y=qz,\quad x=\frac{q(1+p)-p}{3q-1}.
\]
These coordinates satisfy all three sector inequalities; the six barycentric coefficients are bounded above by \(z\). For \(p,q\ge1\), let the largest coefficient be at most \(z\). From the \(ABC\) coefficients \(1-x+(p-1)y/q\) and \(y/q\), obtain \(x\ge1+(p-1)y/q-z\), \(y\le qz\). Substituting in the \(BCD\) coefficient \((p+(q-1)x-py)/k\), using \(q-1\ge0\), gives
\[
kz\ge k-(p+2q-2)z,
\quad\text{hence}\quad z\ge\frac{k}{2p+3q-3}.
\]
For this last \(z\), the point \((x,y)=(1+(p-2)z,qz)\) belongs to the \(B\)-sector and all six coefficients are at most \(z\), proving equality. The point and coefficient inequalities include the equality cases \(p=1\) or \(q=1\).

**4. Symmetry and minimization.** Interchanging the two coordinate axes interchanges \(p,q\), the \(A,D\) sectors, and the \(B,C\) sectors. Consequently \(m_D(p,q)=m_A(q,p)\) and \(m_C(p,q)=m_B(q,p)\). Comparing these four explicit expressions and sorting \(a=\min(p,q)\), \(b=\max(p,q)\) produces exactly the four regimes stated above. If \(b\le1\), the controlling sector has minimum \((3-a)^{-1}\). If \(a\le1\le b\) and \(a+b\le2\), it is \(b/(2b+1-a)\); when \(a+b\ge2\), it is \(b/(3b-1)\). For \(a\ge1\), the smaller of the two \(B,C\) minima is \(k/[2(a+b)-3+b]\). These comparisons remain valid on all boundaries by continuity.

**5. Sharp convexification threshold and rigidity.** For \(0<t<1\), multiplying \(Q=tV(Q)+(1-t)Q\) by \(1/t\) gives \(V(Q)+[(1-t)/t]Q=Q/t\). The threshold is therefore \(c(V(Q))=(1-\lambda(Q))/\lambda(Q)\); monotonicity follows because the sum at a larger scale is a Minkowski sum of a convex set and a positive multiple of \(Q\). The explicit formulas show \(\lambda(Q)>1/3\) and \(\lambda(Q)\le1/2\), with \(\lambda=1/2\) iff \(p=q=1\), equivalently iff \(Q\) is a parallelogram. Substituting \(p=q=s\) gives the stated kite profile.

## Verification
Run `python3 verify_quadrilateral_vertex_index.py` using Python's standard library. The independent verifier solves the four small linear programs directly by enumerating all triples of active affine inequalities using exact rational arithmetic, independently of the final closed formula. It compares the minimum over the four sectors to the formula for 101 nondegenerate rational quadrilaterals across all four regimes and transition boundaries. It returned `VERIFY_OK: 101 exact rational quadrilateral systems; four-sector LP vertex enumeration`. This is finite corroboration; the universal proof consists of the sharp sector inequalities and explicit attaining witnesses above.

## Relationship to prior work
Artstein-Avidan, Falah and Slomka introduced the vertex-generation parameter and related it to Schneider's nonconvexity index; they established the general simplex and zonotope bounds but did not evaluate its full two-parameter quadrilateral profile. Meyer's work on finite convexification by Minkowski summation develops general criteria and treats the planar situation, but no evaluated four-chamber formula for arbitrary quadrilateral vertex sets occurs in the inspected primary text. In contrast, this result supplies a closed all-shape classification with equality witnesses. The determination of a known index from a new class-specific optimization is the claimed contribution, not the definition of the index itself.

## Limitations
The classification is for proper convex quadrilaterals, not degenerate three-vertex limits or higher-dimensional polytopes. The two-parameter affine coordinate normalization depends on the labeling, though the result is invariant. No independent expert audit or absolute historical priority guarantee is claimed; an equivalent older formulation in nonconvexity or covering literature remains possible.

## References
1. Shiri Artstein-Avidan, Tomer Falah, and Boaz A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604 (first posted 2024-07-30), especially Definition 1.1, Sections 2, 3, 4.1, and Proposition 7.5.
2. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744 (first posted 2026-10-19), especially the introduction, Theorems 1.1–1.3 and the planar-case discussion.
3. Rolf Schneider, *A measure of convexity for compact sets*, Pacific Journal of Mathematics **58** (1975), 617–626, DOI:10.2140/PJM.1975.58.617; original source examined through its publicly accessible full-text journal PDF.
