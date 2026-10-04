# The minimal-volume equality surface has basket \(A_3\sqcup A_1\sqcup A_2\sqcup \frac1{21}(1,8)\)
## Finding
Let
\[
X_{18}=\left\{z^2+y^2(y-x^3)+x^2t^2=0\right\}\subset\mathbf P(2_x,6_y,7_t,9_z)
\]
be the unique equality surface of Liu--Shao. The coarse surface \(X_{18}\) has exactly four singular points, with complete analytic basket
\[
A_3\ \sqcup\ A_1\ \sqcup\ A_2\ \sqcup\ \frac1{21}(1,8).
\]
More explicitly:
\[
P_x=[1:0:0:0]\quad\text{has type}\quad \frac14(1,3)=A_3,
\]
\[
Q_2:\ t=z=0,\ y=x^3\quad\text{has type}\quad \frac12(1,1)=A_1,
\]
\[
Q_3:\ x=t=0,\ z^2+y^3=0\quad\text{has type}\quad \frac13(1,2)=A_2,
\]
and
\[
P_t=[0:0:1:0]\quad\text{has type}\quad \frac1{21}(1,8).
\]
The point \(Q_3\) is unique in the weighted line \(\mathbf P(6,9)\): after dividing the common weight by \(3\), the two affine square-root representatives of \(z^2+y^3=0\) in \(\mathbf P(2,3)\) are identified by the residual weighted scaling.

At \(P_t\), the local canonical index is \(7\). Its minimal resolution is the Hirzebruch--Jung chain
\[
[-3,-3,-3],
\]
and, with
\[
K_{\widetilde X}=\pi^*K_X+\sum_{i=1}^3a_iE_i,
\]
the discrepancy vector is
\[
(a_1,a_2,a_3)=\left(-\frac47,-\frac57,-\frac47\right).
\]
Hence the minimal resolution of \(X_{18}\) has exceptional configuration
\[
A_3\ \sqcup\ A_1\ \sqcup\ A_2\ \sqcup\ [-3,-3,-3],
\]
with \(3+1+2+3=9\) irreducible exceptional curves.

## Assumptions and scope
The base field is \(\mathbf C\), and \(X_{18}\) is the weighted hypersurface appearing in Liu--Shao, arXiv:2609.27259v1. The claim concerns the analytic singularities of the coarse projective surface, not the ambient weighted-projective stack. Quotient notation \(\frac1r(1,a)\) is understood up to the usual change of generator and interchange of the two coordinates.

The calculation does not describe the boundary divisor \(B_{18}\) through these quotient charts beyond what is needed to locate the surface singularities. It does not compute \(\mathbf Q\)-Gorenstein deformation spaces or global deformation obstructions.

## Proof
Write
\[
F=z^2+y^2(y-x^3)+x^2t^2.
\]
Liu--Shao compute the singular locus of the affine cone \(F=0\subset\mathbf A^4\) as the union of the \(x\)-axis and the \(t\)-axis. Thus, away from their projectivizations \(P_x\) and \(P_t\), the weighted-projective stack cut out by \(F\) is smooth.

It remains to intersect \(X_{18}\) with the positive-dimensional orbifold strata of \(\mathbf P(2,6,7,9)\). The only pairs of weights having nontrivial gcd are
\[
\gcd(2,6)=2,\qquad \gcd(6,9)=3.
\]
On the \((x,y)\)-line, where \(t=z=0\),
\[
F=y^2(y-x^3).
\]
The reduced intersection consists of \(P_x\) and one further point \(Q_2\) with \(y=x^3\). On the \((y,z)\)-line, where \(x=t=0\),
\[
F=z^2+y^3,
\]
which gives one projective point \(Q_3\). Among the coordinate points, \(P_x\) and \(P_t\) lie on \(X_{18}\), while the \(y\)- and \(z\)-coordinate points do not. Therefore these four points exhaust the coarse singular locus.

At \(Q_2\), use the \(x\neq0\) orbifold chart. The residual stabilizer is \(\mu_2\), and after setting \(x=1\) the equation is
\[
z^2+y^2(y-1)+t^2=0.
\]
At \(y=1,t=z=0\), the derivative with respect to \(y\) is nonzero, so the stack surface is smooth. Its tangent coordinates \(t,z\) both have odd \(\mu_2\)-weight. Hence the coarse germ is
\[
\frac12(1,1)=A_1.
\]

At \(Q_3\), the stabilizer of a point with \(y,z\neq0\) is \(\mu_3\). The stack surface is smooth because the derivative with respect to \(z\) is nonzero. The two tangent coordinates can be taken to be \(x,t\), of weights
\[
2,\ 7\equiv 2,\ 1\pmod 3.
\]
Thus
\[
(Q_3\in X_{18})\simeq \frac13(1,2)=A_2.
\]

At \(P_x\), the \(x\neq0\) orbifold cover has residual \(\mu_2\) and local equation
\[
z^2+t^2-y^2+y^3=0.
\]
After the invariant analytic change \(Y=y\sqrt{1-y}\) and the linear change
\[
u=t+iz,\qquad v=t-iz,
\]
this becomes
\[
uv-Y^2=0.
\]
The residual involution acts by
\[
(u,v,Y)\longmapsto(-u,-v,Y).
\]
Uniformize the \(A_1\) cover by
\[
u=a^2,\qquad v=b^2,\qquad Y=ab.
\]
The involution lifts to the order-four action
\[
(a,b)\longmapsto(ia,-ib),
\]
whose square is the deck involution of the \(A_1\) cover. Consequently the coarse germ is
\[
\frac14(1,3)=A_3.
\]

At \(P_t\), the \(t\neq0\) orbifold cover has residual \(\mu_7\) with weights
\[
(x,y,z)\equiv(2,6,2)\pmod7
\]
and equation
\[
z^2+x^2+y^3-x^3y^2=0.
\]
Because \(xy^2\) has weight \(0\) modulo \(7\), the equivariant analytic change
\[
X=x\sqrt{1-xy^2}
\]
is legitimate. With
\[
u=z+iX,\qquad v=z-iX,
\]
the equation becomes
\[
uv+y^3=0,
\]
an \(A_2\) singularity on the orbifold cover. Uniformize it by
\[
u=a^3,\qquad v=-b^3,\qquad y=ab.
\]
The \(A_2\) deck group is \(\mu_3(1,-1)\). The residual \(\mu_7\)-action lifts as
\[
(a,b)\longmapsto(\zeta^3a,\zeta^3b),
\]
because \(3\cdot3\equiv2\pmod7\) and \(3+3\equiv6\pmod7\). Since \(3\) and \(7\) are coprime, the combined group is cyclic of order \(21\). If \(\eta\) is a primitive \(21\)-st root, a generator acts with exponents
\[
(16,2)\pmod{21}.
\]
Changing the generator and interchanging coordinates gives
\[
\frac1{21}(16,2)\simeq\frac1{21}(1,8).
\]

The local canonical index of \(\frac1{21}(1,8)\) is
\[
\frac{21}{\gcd(21,1+8)}=7.
\]
The negative continued fraction is
\[
\frac{21}8=[3,3,3]^-,
\]
so the minimal resolution has three curves of self-intersection \(-3\). By adjunction,
\[
K_{\widetilde X}\cdot E_j=-2-E_j^2=1.
\]
Therefore the discrepancy vector solves
\[
\begin{pmatrix}
-3&1&0\\
1&-3&1\\
0&1&-3
\end{pmatrix}
\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}
=
\begin{pmatrix}1\\1\\1\end{pmatrix},
\]
whose unique solution is
\[
\left(-\frac47,-\frac57,-\frac47\right).
\]
The three Du Val points contribute respectively \(3\), \(1\), and \(2\) \((-2)\)-curves, completing the claimed nine-curve exceptional configuration.

## Verification
The accompanying `verify.py` checks, using exact integer and rational arithmetic, the ambient gcd strata, membership of the coordinate points, the residual tangent weights at \(Q_2\) and \(Q_3\), the lifted group weights at \(P_x\) and \(P_t\), the normalization of \(\frac1{21}(16,2)\) to \(\frac1{21}(1,8)\), the continued fraction \(21/8=[3,3,3]^-\), the canonical index \(7\), and the discrepancy linear system. The saved replay output ends in `VERIFY_OK`.

The analytic coordinate changes and the fact that the affine-cone singular locus is the two axes are proved mathematically in the preceding argument and in the cited source; the finite verifier is a consistency check, not a substitute for those local analytic arguments.

## Relationship to prior work
Liu--Shao construct \(X_{18}\), prove that it is normal, compute the singular locus of its affine cone, and prove that the equality pair is unique. Their general equality-pair analysis also shows that the boundary contains two cyclic quotient points with different coefficients corresponding to indices \(2\) and \(3\). In the inspected full text, however, the surface \(X_{18}\) is not assigned a complete singularity basket, the \(A_3\) type at \(P_x\) is not stated, and the off-boundary point \(P_t\) is not identified as \(\frac1{21}(1,8)\) with resolution chain \([-3,-3,-3]\).

Targeted exact-equation and exact-quotient searches located the initiating preprint and summaries of it but no source stating this complete four-point basket or the \(\frac1{21}(1,8)\) local model for \(X_{18}\).

## Limitations
The result is a local analytic classification of the singular points of one distinguished surface. It does not determine deformation theory, smoothing components, the global Picard lattice of the minimal resolution, or the interaction of the boundary with every exceptional component.

Searches can miss unindexed or differently phrased computations, so the absence of a located matching basket is not a proof of novelty. The strongest originality evidence is the inspected primary full text together with exact-equation and exact-local-type searches.

## References
1. J. Liu and W. Shao, *The Minimal Volume of Normal Stable Surface Pairs with Reduced Boundary Containing a Zero-Dimensional Non-klt Center*, arXiv:2609.27259v1, submitted 23 September 2026; primary MSC 14J29. See Theorem 6.1 and Proposition 6.2 for \(X_{18}\), and Theorem 5.1 for the boundary singularity information.
