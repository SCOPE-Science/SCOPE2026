# Exact opposite-side Ptolemy branch for rectangles
## Finding
Let \(L,H>0\) and let
\[
R=[0,L]\times[0,H].
\]
For cyclically ordered boundary points with
\[
A,B\in[0,L]\times\{0\},\qquad C,D\in[0,L]\times\{H\},
\]
where \(A\) precedes \(B\) from left to right and \(C\) precedes \(D\) when the top side is traversed right to left, define
\[
p(A,B,C,D)=\frac{|AB|\,|CD|+|AD|\,|BC|}{|AC|\,|BD|}.
\]
Then
\[
\max p(A,B,C,D)=\frac{L^2+2H^2}{2H\sqrt{L^2+H^2}}.
\]
Equality holds exactly, up to reflection in the vertical midline and interchange of the two horizontal sides, at
\[
A=(L/2,0),\quad B=(L,0),\quad C=(L/2,H),\quad D=(0,H).
\]
Thus the full class having two points on each member of a fixed pair of opposite sides is solved exactly.

If the displayed sides are the long sides of a rectangle and \(t=L/H\ge1\), write
\[
Q(t)=\frac{t^2+2}{2\sqrt{t^2+1}}.
\]
The Harmaala--Klén lower bound for the full rectangle contains
\[
M(t)=\max\left\{\sqrt2,\sqrt{1+\frac{t^2}{4}}\right\}.
\]
For \(1\le t\le2\), \(Q(t)<\sqrt2\); for \(t\ge2\),
\[
1+\frac{t^2}{4}-Q(t)^2=\frac{t^2}{4(t^2+1)}>0.
\]
Hence this opposite-side branch never supplies the full rectangle extremum. If instead the two occupied sides are the short sides, the corresponding aspect ratio is at most \(1\), and the branch maximum is at most \(3/(2\sqrt2)<\sqrt2\).

## Assumptions and scope
The theorem concerns Euclidean distance and four boundary points constrained to lie two on each of two opposite sides of one rectangle. Coincident endpoint limits may be included by continuity, but the stated equality configuration is nondegenerate for \(L,H>0\). No assertion is made here about the remaining side-occupancy patterns, so this does not by itself prove the conjectured exact Ptolemy constant of an arbitrary rectangle.

## Proof
Write the two occupied horizontal intervals as
\[
A=(m_0-a,0),\quad B=(m_0+a,0),\quad
C=(m_1+b,H),\quad D=(m_1-b,H),
\]
with \(a,b\ge0\). Reflecting horizontally if necessary, put \(h=m_0-m_1\ge0\). Since both intervals lie in \([0,L]\),
\[
h+a+b\le L.
\]
Set
\[
p_0=a+b,\qquad q=a-b.
\]
A direct distance calculation gives
\[
p(A,B,C,D)=
\frac{p_0^2-q^2+\Phi_h(q)}{\Phi_h(p_0)},
\]
where
\[
\Phi_h(z)=\sqrt{((h-z)^2+H^2)((h+z)^2+H^2)}.
\]
Put \(X=q^2\). Then
\[
\Phi_h(q)^2=X^2+2(H^2-h^2)X+(h^2+H^2)^2
\]
and
\[
\Phi_h(q)^2-(X+H^2-h^2)^2=4H^2h^2.
\]
Consequently
\[
\frac{d}{dX}\left(p_0^2-X+\Phi_h(q)\right)
=-1+\frac{X+H^2-h^2}{\Phi_h(q)}\le0.
\]
Thus, for fixed \(p_0,h\), the ratio is maximal when \(q=0\), equivalently \(a=b\).

With \(q=0\), put
\[
u=h+p_0,\qquad v=|h-p_0|.
\]
Then \(0\le v\le u\le L\) and
\[
p(A,B,C,D)\le
F(u,v):=\frac{u^2+v^2+2H^2}{2\sqrt{(u^2+H^2)(v^2+H^2)}}.
\]
For fixed \(u\), if \(Y=v^2\), differentiation gives
\[
\frac{\partial F}{\partial Y}=
\frac{Y-u^2}{4\sqrt{u^2+H^2}(Y+H^2)^{3/2}}\le0.
\]
Hence \(F(u,v)\le F(u,0)\). Finally
\[
F(u,0)=\frac{u^2+2H^2}{2H\sqrt{u^2+H^2}},
\]
and
\[
\frac{d}{du}F(u,0)=\frac{u^3}{2H(u^2+H^2)^{3/2}}\ge0.
\]
Since \(u\le L\), the desired upper bound follows. Equality forces \(q=0\), \(v=0\), and \(u=L\), hence \(a=b=L/4\) and \(h=L/2\), which gives exactly the displayed configurations after the stated symmetries.

The comparison with the full-rectangle lower candidates follows from the two explicit identities in the Finding section and the monotonicity of \(Q(t)\) for \(t>0\).

## Verification
The proof is analytic. The bundled checker verifies the algebraic identity controlling the first monotonicity step, the exact derivative formulas for the second and third steps, the equality value, and the comparison identity with the long-rectangle lower candidate. These computations are diagnostic support; the inequalities above supply the infinite-family proof.

## Relationship to prior work
Harmaala and Klén proved general lower and upper bounds for parallelograms and, for rectangles, obtained
\[
\max\left\{\sqrt2,\sqrt{1+\frac{\max\{r,s\}^2}{4\min\{r,s\}^2}}\right\}
\le P(R)\le
\sqrt{1+\frac{\max\{r,s\}^2}{\min\{r,s\}^2}}.
\]
Their parallelogram lower-bound construction contains the same numerical quantity
\[
\frac{L^2+2H^2}{2H\sqrt{L^2+H^2}}
\]
for one special opposite-side quadruple, but they do not prove that it is the exact maximum over the complete two-on-each-opposite-side class. Their rectangle proof treats opposite-vertex configurations only through a coarser angle estimate. The present theorem supplies the missing sharp branch upper bound and equality classification.

Finch subsequently proposed the Harmaala--Klén rectangle lower bound as the likely global formula, explicitly describing the argument as nonrigorous and noting that many vertex configurations still had to be ruled out. The theorem here rigorously eliminates one entire natural occupancy branch but does not settle Finch's global formula.

## Limitations
The theorem does not cover configurations using adjacent sides, three sides, or all four sides. It therefore does not establish the exact full Ptolemy constant of a rectangle. The historical 1996 unpublished licentiate thesis by P. Seittenranta cited by Harmaala--Klén was not materially available for comparison; an unindexed equivalent branch computation there remains a residual originality risk.

## References
E. Harmaala and R. Klén, *Ptolemy constant and uniformity*, arXiv:1604.05367, first public version 2016-04-18. In particular, Proposition 4.1, Theorems 4.4--4.5, and Corollary 4.8.

S. R. Finch, *Ptolemy Constants as Described by Eccentricity*, arXiv:1608.04299, first public version 2016-08-12.
