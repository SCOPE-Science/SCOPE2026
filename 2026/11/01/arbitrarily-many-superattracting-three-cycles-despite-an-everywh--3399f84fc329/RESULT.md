# Arbitrarily many superattracting three-cycles despite an everywhere nilpotent Jacobian

## Finding
For every integer \(N\ge 1\), there is a polynomial \(P_N\in\mathbb Q[t]\) of degree at most \(2N\), with \(P_N(0)=0\), for which the polynomial map
\[
F_N(x,y,z)=\bigl(U,\ z-2xU,\ U^2\bigr),\qquad U=P_N(y+x^2),
\]
has an everywhere nilpotent Jacobian and possesses at least \(N\) **different, locally superattracting orbits of least period three**. These cycles can be prescribed at the distinct squared-integer locations \(s_j=j^2\), \(1\le j\le N\), and have the explicit form
\[
(0,s_j,0)\longmapsto(j,0,s_j)\longmapsto(j,-s_j,s_j)\longmapsto(0,s_j,0).
\]
The origin remains the sole fixed point; there are no points of least period two. Thus pointwise nilpotency gives no degree-independent bound on the number of attracting three-cycles in this family. The polynomial and all cycles are constructed exactly over the rationals.

## Assumptions and scope
The ambient space is \(\mathbb R^3\); iteration is deterministic and discrete. "Superattracting" means that the differential of the three-step return map is the zero matrix at at least one phase of each cycle, so each orbit attracts a full open neighborhood and has all three return multipliers zero. No claim is made about the **total** number of three-cycles, their basins' boundaries, or the behavior of points outside the stated neighborhoods. The degree bound concerns the one-variable polynomial \(P_N\), not the total degree of \(F_N\). This map belongs to the nilpotent-Jacobian family analyzed by Chamberland and by Castañeda--Rebollo-Perdomo.

## Proof
**Construction.** Fix \(N\ge1\) and write \(s_j=j^2\) for \(1\le j\le N\). Impose the \(2N+1\) rational Hermite conditions
\[
P_N(0)=0,\quad P_N(s_j)=j,\quad P_N'(s_j)=0\quad(1\le j\le N).
\]
They have a unique polynomial solution of degree at most \(2N\): the homogeneous interpolation problem would require a nonzero polynomial of degree at most \(2N\) to vanish at zero and have double zeros at all \(N\) distinct positive nodes, impossible by the root-multiplicity bound. Existence follows by nonsingularity of the square interpolation matrix. Explicitly, set
\[
\ell_j(t)=\prod_{\substack{1\le m\le N\\m\ne j}}\frac{t-s_m}{s_j-s_m},\qquad
R(t)=\sum_{j=1}^N j\,[1-2(t-s_j)\ell_j'(s_j)]\ell_j(t)^2,
\]
and \(W(t)=\prod_{j=1}^N(t-s_j)^2\). Then \(P_N(t)=R(t)-R(0)W(t)/W(0)\) satisfies the conditions and has rational coefficients and degree at most \(2N\). In particular \(P_1(t)=2t-t^2\).

**Pointwise nilpotency.** For any differentiable \(P\), write \(u=P(y+x^2)\), \(v=P'(y+x^2)\). Direct differentiation gives
\[
DF=\begin{pmatrix}
2xv&v&0\\
-2u-4x^2v&-2xv&1\\
4xuv&2uv&0
\end{pmatrix}.
\]
Direct matrix multiplication, as an identity in the free real variables \(x,u,v\), yields \((DF)^3=0\). Thus at every input all Jacobian eigenvalues vanish. This calculation is independent of the interpolation data.

**Exact cycles.** At \(A_j=(0,s_j,0)\) and \(B_j=(j,0,s_j)\), the argument \(y+x^2\) equals \(s_j\); therefore \(u=j\) and \(v=0\). At \(C_j=(j,-s_j,s_j)\) that argument is zero and \(u=P_N(0)=0\). Substitution into the map gives \(F_N(A_j)=B_j\), \(F_N(B_j)=C_j\), and \(F_N(C_j)=A_j\). Since \(j>0\), the three points are distinct. A cycle contains exactly one point whose first coordinate is zero, namely \(A_j\), so different indices produce different cycles.

**Superattraction.** At both \(A_j\) and \(B_j\) the displayed Jacobian becomes the identical matrix
\[
J_j=\begin{pmatrix}0&0&0\\-2j&0&1\\0&0&0\end{pmatrix},\qquad J_j^2=0.
\]
Consequently \(D(F_N^2)(A_j)=J_j^2=0\), and therefore \(D(F_N^3)(A_j)=0\). Since the return map is polynomial and fixes \(A_j\), Taylor's theorem gives \(\|F_N^3(A_j+h)-A_j\|\le C_j\|h\|^2\) in a sufficiently small ball. That ball contains a smaller positively invariant ball for the three-step map; its points converge to \(A_j\), and continuity of the first two steps gives attraction to the whole period-three orbit. All return multipliers are zero.

**Shorter cycles.** Any fixed point satisfies \(x=u\), \(z=x^2\), \(y=-x^2\), and hence \(x=P_N(0)=0\); the origin is the only fixed point. For two-cycles, use the invertible polynomial coordinate change
\[
(X,Y,Z)=\bigl(x-P(Y),\ Y,\ z-2xP(Y)+P(Y)^2\bigr),\qquad Y=y+x^2,
\]
which conjugates \(F_N\) to \(G(X,Y,Z)=(P(Y)-P(Z),Z,(P(Y)-P(Z))^2)\). At a point fixed by \(G^2\), the first coordinates of its two phases are opposites; the third coordinates are their squares, hence equal. The second coordinates are swapped third coordinates, hence equal too. Therefore the differences of \(P\) vanish and both first coordinates are zero; all coordinates then vanish. There is no nontrivial two-cycle.

## Verification
`CHECK.py` is a standalone exact-rational Python program using only the standard library. It constructs \(P_N\) by rational Gaussian elimination for \(N=1,\ldots,6\), verifies every interpolation condition and each displayed three-step orbit, computes the two consecutive Jacobians and checks their product is zero, and tests the universal matrix-cube identity at 27 rational points for each size. The program reports 267 successful exact checks. The proof above establishes the result for **all** positive integers \(N\); a finite checker does not certify the universal quantifier.

## Relationship to prior work
Chamberland (2005 manuscript, published 2006) studied the sign-conjugate form of this family and established an existence criterion for one nonconstant three-cycle, with examples of attracting and saddle behavior. Castañeda and Rebollo-Perdomo (first posted 15 September 2022) develop a larger nilpotent-Jacobian class, give a general three-cycle equation and its nonzero multiplier, and explicitly ask whether the three-cycle could be unique and attracting. Those one-cycle criteria and the known coordinate reductions are **not claimed as new**. The present simultaneous rational Hermite construction resolves uniqueness negatively in the stronger form of arbitrarily many *coexisting superattracting* cycles, with an explicit degree bound and a directly verified zero return differential. A separately indexed finding on the same nilpotent family establishes a sharp degree threshold for **four**-cycles, rather than three-cycle multiplicity; its coordinate-conjugacy calculation is consistent with the reduction above. Full-text priority beyond the inspected materials has not been established.

## Limitations
This is an existence construction, not a classification of all periodic orbits. The source papers' one-cycle existence criteria, combined with classical Hermite interpolation, are close antecedents: the possibility of a concise derivation from them is an important publication-priority risk, even though neither inspected paper states the arbitrarily-many-superattractors assertion. The polynomial degree grows with the desired count, and optimal degree is not determined. The local attraction statement does not imply global attraction. No independent audit was performed.

## References
1. Á. Castañeda and S. Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1, first public 15 September 2022. https://arxiv.org/pdf/2209.06986 (especially Theorem 1.1, Section 3, and Section 5).
2. M. Chamberland, *Dynamics of Maps with Nilpotent Jacobians*, author manuscript dated 17 May 2005, subsequently *Journal of Difference Equations and Applications* 12 (2006), 49–56. https://chamberland.math.grinnell.edu/papers/nilpotent.pdf (especially Theorem 3.1 and Section 4).
3. *A sharp degree threshold for four-cycles in a three-dimensional nilpotent-Jacobian family*, published-finding corpus indexed finding `2026/10/11/SCOPE-a-sharp-degree-threshold-for-four-cycles-in-a-three-dimensional--7541997decfd`, accessed 27 October 2026. This is a separate four-cycle result, not prior coverage of the present three-cycle multiplicity.
