# Two primitive three-cycle geometries in mixed-sign two-saddle border-collision maps

## Finding

For the standard continuous border-collision normal form with two saddle fixed points and oppositely signed branch determinants, every **strict** primitive period-three orbit belongs to one of two explicit types. A strict orbit is one whose points all avoid the switching line. The all-parameter census and stability conclusions below apply throughout the domain in the next section.

Define
\[
\begin{aligned}
K&=ac+ad+bd-b+c+1,\\
J&=ac+a+bc+bd-d+1,\\
Q_L&=a^2+ab+a+b^2-b+1,\\
Q_R&=c^2+cd+c+d^2-d+1,\\
D_L&=1-a^2c+ab+ad+b^2d+bc,\\
D_R&=1-ac^2+ad+bc+bd^2+cd.
\end{aligned}
\]
There is exactly one strict primitive \(LLR\)-cycle if and only if \(K<0\), \(J<0\), and \(D_L>0\), and there is exactly one strict primitive \(LRR\)-cycle if and only if \(K<0\), \(J<0\), and \(D_R<0\). There are no other strict primitive three-cycles. In particular, the count is at most two.

Every admissible strict \(LRR\)-cycle is a hyperbolic saddle. Every admissible strict \(LLR\)-cycle has a positive multiplier in \((0,1)\) and a negative multiplier; writing
\[
S_L=1+a^2c-ab-ad-bc+b^2d,
\]
its classification is precisely: attracting if \(S_L>0\), a saddle if \(S_L<0\), and a simple multiplier \(-1\) with the other multiplier in \((0,1)\) if \(S_L=0\).

These alternatives coexist on a nonempty open four-parameter region. For the explicit line
\[
(a,b,c)=\left(\frac54,\frac15,-5\right),\qquad -6<d<0,
\]
both strict cycles exist throughout, the \(LRR\)-cycle is always a saddle, and the \(LLR\)-cycle is attracting exactly when
\[
-6<d<-\frac{2425}{484},
\]
with an exact \(-1\) multiplier at the intervening endpoint. No generic smooth flip bifurcation is asserted there.

## Assumptions and scope

Let \(F:\mathbb R^2\to\mathbb R^2\) be
\[
F(x,y)=\begin{cases}(ax+y+1,-bx),&x\le 0,\\(cx+y+1,-dx),&x\ge 0.\end{cases}
\]
The two rules agree at \(x=0\). Assume the **open** four-parameter region
\[
a>1+b,\quad b>0,\quad c<0,\quad d<0,\quad 1+c+d<0,\quad 1-c+d>0.
\]
Both fixed points are hyperbolic saddles; the left one is in \(x<0\), and the right one is in \(x>0\). Symbols \(L\) and \(R\) label the signs \(x<0\) and \(x>0\). A strict primitive three-cycle has three nonzero \(x\)-coordinates and least period exactly three. Cyclic rotations of an itinerary describe one geometric orbit, not three.

## Proof

The branch matrices and common offset are
\[
A_L=\begin{pmatrix}a&1\\-b&0\end{pmatrix},\qquad
A_R=\begin{pmatrix}c&1\\-d&0\end{pmatrix},\qquad e=(1,0)^T.
\]
The characteristic polynomial of \(A_L\) is \(\lambda^2-a\lambda+b\), and \(1-a+b<0\). It therefore has one eigenvalue greater than one and another in \((0,1)\). The polynomial of \(A_R\) is \(\lambda^2-c\lambda+d\); the two strict inequalities \(1+c+d<0\) and \(1-c+d>0\) imply eigenvalues respectively below \(-1\) and in \((0,1)\). Thus neither affine branch supports a primitive period-three orbit by itself: its third iterate has exactly the original fixed point. A strict three-cycle must use both symbols, so, up to cyclic rotation, its only possible itineraries are \(LLR\) and \(LRR\).

For \(LLR\), solve the linear affine return equation
\[
z_0=A_R(A_L(A_Lz_0+e)+e)+e.
\]
Its characteristic denominator is \(D_L=\det(I-A_RA_L^2)\). When nonzero, the three successive first coordinates are exactly
\[
(x_0,x_1,x_2)=\frac1{D_L}(K,J,Q_L).
\]
The second coordinates follow uniquely as \((y_0,y_1,y_2)=(-dx_2,-bx_0,-bx_1)\). Similarly, solving the \(LRR\) affine return gives
\[
(x_0,x_1,x_2)=\frac1{D_R}(Q_R,J,K),\qquad
(y_0,y_1,y_2)=(-dx_2,-bx_0,-dx_1),
\]
where \(D_R=\det(I-A_R^2A_L)\).

Both positive numerators are strictly positive throughout the domain:
\[
Q_L=a^2+ab+a+(b-1/2)^2+3/4>0,
\]
\[
Q_R=\left(c+\frac{d+1}{2}\right)^2+\frac34(d-1)^2>0.
\]
If a denominator vanishes, the corresponding affine return equation has no solution: multiplying the undivided first-coordinate equation by its denominator yields the nonzero numerator \(Q_L\) or \(Q_R\). Otherwise the required signs \((-,-,+)\) for \(LLR\) and \((-,+,+)\) for \(LRR\) are equivalent exactly to the conditions in the finding. In particular, every admitted candidate indeed follows its prescribed branch rules and has least period three. The resulting list is exhaustive.

For the \(LLR\) return matrix \(P_L=A_RA_L^2\), direct multiplication yields
\[
\mathrm{tr}(P_L)=a^2c-ab-ad-bc,\quad
\det P_L=b^2d<0,\quad
\det(I-P_L)=D_L.
\]
Under admissibility \(D_L>0\), its two real eigenvalues \(\lambda_+>0>\lambda_-\) satisfy \(0<\lambda_+<1\), since \((1-\lambda_+)(1-\lambda_-)>0\). The negative eigenvalue lies in \((-1,0)\), equals \(-1\), or lies below \(-1\) exactly according to the sign of
\[
(1+\lambda_+)(1+\lambda_-)=\det(I+P_L)=S_L.
\]
This proves the full \(LLR\) stability statement.

For the \(LRR\) return matrix \(P_R=A_R^2A_L\), one has \(\det P_R=bd^2>0\) and \(\det(I-P_R)=D_R<0\) at every admissible cycle. Its real characteristic polynomial therefore has two positive roots separated by one, so \(0<\lambda_1<1<\lambda_2\): the orbit is necessarily a hyperbolic saddle.

Finally substitute \((a,b,c)=(5/4,1/5,-5)\). Exact simplification yields
\[
D_L=\frac{129(4d+25)}{400}>0,\qquad
D_R=\frac{(d-25)(4d+25)}{20}<0,
\]
\[
K=\frac{29d-209}{20}<0,\quad
J=-\frac{4d+25}{5}<0,\quad
S_L=-\frac{484d+2425}{400}.
\]
All are strict except the designated neutral multiplier boundary. Both cycles exist throughout \(-6<d<0\), and the last formula yields the exact attracting subinterval. Since the strict signs persist under sufficiently small parameter changes, coexistence includes a nonempty open subset of the full four-parameter domain.

## Verification

The accompanying `verify.py` checks the exact affine return matrices, first-coordinate formulas, determinants, stability polynomial, the witness-line factorizations, and direct three-step substitutions at seven rational values, including the neutral boundary. It uses exact SymPy arithmetic, not floating-point orbit detection. Analytical sign arguments, rather than finitely many samples, establish the general assertions.

## Relationship to prior work

The normal form and two-saddle regime come from Ghosh–McLachlan–Simpson (2024), which principally analyzes chaotic attractors, renormalisation, and period-two/four behavior in the opposite-determinant sector. The general method of encoding periodic orbits with branch words and matrix products is classical; the source literature already contains some explicit three-cycle stability examples for other parameter regimes. The result here is the all-parameter **strict period-three census and stability dichotomy within the specified two-saddle mixed-sign regime**, notably the prohibition of any attracting \(LRR\)-cycle there and its coexistence with an attracting \(LLR\)-cycle on an explicit open set. The 2022 synopsis uses a different specialized parameter regime for an attracting \(LRR\)-cycle, so it does not imply this exclusion. An equivalent statement expressed through general symbolic-matrix inequalities could exist elsewhere.

## Limitations

No orbit with a point on the switching line is classified; consequently, the theorem does not give the complete boundary-inclusive period-three count. It gives no higher-period census, global basin statement, or chaotic-attractor theorem. At \(S_L=0\), a multiplier equals \(-1\), but the local dynamics at neutrality is not asserted to be a smooth period-doubling. The one-dimensional rational witness is an illustration of a full-dimensional open parameter phenomenon, not a classification of all parameter bifurcations.

## References

1. I. Ghosh, R. I. McLachlan, D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393v1 (8 February 2024), https://arxiv.org/html/2402.05393v1 .
2. H. O. Fatoyinbo, D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445 (2022), https://arxiv.org/abs/2210.14445 .
3. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790 (2024), https://arxiv.org/abs/2408.04790 .
4. D. J. W. Simpson, V. Avrutin, *From two-dimensional continuous maps to one-dimensional discontinuous maps*, arXiv:2512.02291 (2025), https://arxiv.org/abs/2512.02291 .
