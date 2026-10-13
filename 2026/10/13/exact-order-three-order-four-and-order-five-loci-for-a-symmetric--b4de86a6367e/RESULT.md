# Exact order-three, order-four and order-five loci for a symmetric QRT elliptic family

## Finding
Consider the smooth projective completion \(C_{B,G}\subset\mathbf P^1_{\mathbf C}\times\mathbf P^1_{\mathbf C}\) of
\[
 x^2y^2-x^2-y^2+Bxy+G=0.
\]
Let
\[
 \Delta(B,G)=G\bigl((B+2)^2-4G\bigr)\bigl((B-2)^2-4G\bigr).
\]
Whenever \(\Delta(B,G)\ne0\), the birational recurrence
\[
 H(x,y)=\left(-y-\frac{Bx}{x^2-1},\,x\right)
\]
extends to a translation automorphism of the genus-one curve. Its *exact* global finite orders \(3,4,5\) occur at precisely the following parameters:
\[
\begin{aligned}
\operatorname{ord}(H)=3&\iff B\ne0\text{ and }G=1+B,\\
\operatorname{ord}(H)=4&\iff B=0\text{ or }G=1,\\
\operatorname{ord}(H)=5&\iff (G-1-B)(G-1+B)^2-B^3(G-1)=0.
\end{aligned}
\]
All statements are understood inside the smooth locus \(\Delta\ne0\). The order-five locus is an irreducible rational curve with parametrization
\[
 B=\frac{(t-1)(t+1)^2}{t},\qquad G=t(t^2+t-1),
\]
where \(t\) avoids \(0,1,-1\) and the roots of \(t^2+t-1\) and \(t^2-4t-1\). Its smooth elliptic fibers are nonisotrivial. Thus this rational parameter family consists of globally order-five, not merely pointwise period-five, QRT dynamics.

## Assumptions and scope
All curves and groups are over \(\mathbf C\). The assumed discriminant \(\Delta\ne0\) is the specialization of Wu's smoothness condition for his symmetric QRT bidegree-\((2,2)\) family, with \(\alpha=-1\) and \(\beta=B\), \(\gamma=G\). By adjunction a smooth \((2,2)\) curve in \(\mathbf P^1\times\mathbf P^1\) has genus one. The rational expression for \(H\) is interpreted as its unique regular extension to the smooth complete curve. “Order” denotes order in \(\operatorname{Aut}(C_{B,G})\), and is not an isolated-orbit period.

## Proof
**(1) Translation structure.** At fixed first coordinate \(x\), the equation is quadratic in \(y\), with Vieta exchange
\[
 \sigma_y(x,y)=\left(x,-y-\frac{Bx}{x^2-1}\right).
\]
The factor swap \(s(x,y)=(y,x)\) is another involution, and \(H=s\circ\sigma_y\). Both extend regularly to the smooth curve. The degree-two projection to the first factor is ramified at four geometric points; hence \(\sigma_y\) has fixed points. The diagonal intersects the smooth \((2,2)\) curve at four points counting multiplicity, and the smoothness inequalities imply these fixed points of \(s\) are distinct. An involution of an elliptic curve with fixed points is a reflection \(P\mapsto A-P\); consequently the product \(s\circ\sigma_y\) is a translation. In particular, \(H^m=\mathrm{id}\) if and only if \(H^m(O)=O\) at any chosen origin \(O\).

**(2) Boundary orbit.** Put \(O=(\infty,1)\), a smooth point on every member. If \(B=0\), then \(H(x,y)=(-y,x)\), so \(H\) has order exactly \(4\) (its square is the fixed-point-free simultaneous sign involution). Suppose henceforth \(B\ne0\), and let \(t=(G-1)/B\). The recurrence and the curve equation along its boundary show
\[
 H(O)=(-1,\infty),\qquad H^2(O)=(t,-1),\qquad H^{-1}(O)=(1,-t).
\]
For instance, \(H^2(O)\) has second coordinate \(-1\); substituting this into the equation leaves \(G-1-Bx=0\), proving its first coordinate is \(t\). The inverse formula is symmetric. For \(t\ne\pm1\), the next iterate is
\[
 H^3(O)=\left(1-\frac{Bt}{t^2-1},t\right).
\]
At \(t=1\), one has \(H^3(O)=O\); at \(t=-1\), one has \(H^3(O)=(\infty,-1)\ne O\). These boundary expressions are evaluated on the projective curve rather than by illegal affine division at a pole.

**(3) Exact orders three and four.** Since \(H(O)\ne O\) and \(H^2(O)\ne O\), there is no order one or two. For \(B\ne0\), \(H^3(O)=O\) exactly when \(H^2(O)=H^{-1}(O)\), namely \((t,-1)=(1,-t)\), which occurs exactly at \(t=1\). This gives \(G=1+B\). Similarly \(H^4(O)=O\) exactly when \(H^3(O)=H^{-1}(O)\). If \(t\ne\pm1\), comparison of the second coordinates gives \(t=-t\), hence \(t=0\), and the first coordinates then agree. The explicit boundary iterates at \(t=\pm1\) rule out order four. Thus \(G=1\) is the remaining order-four condition when \(B\ne0\). Together with \(B=0\), this proves the order-three and order-four statements.

**(4) Exact order five.** When \(B\ne0\), the cases \(t=0,1\) already have exact orders four and three; when \(t=-1\), the third iterate is \((\infty,-1)\), excluding order five. Hence assume \(t\notin\{0,\pm1\}\). Set
\[
 a=1-\frac{Bt}{t^2-1},\qquad H^3(O)=(a,t).
\]
The condition \(H^5(O)=O\) is equivalent to \(H^4(O)=H^{-1}(O)=(1,-t)\). The second-coordinate equality forces \(a=-t\). Conversely, if \(a=-t\), applying the recurrence at \((-t,t)\) gives
\[
 H^4(O)=\left(-t+\frac{Bt}{t^2-1},-t\right)=(1,-t).
\]
Thus \(H\) has exact order five precisely when \(Bt=(t-1)(t+1)^2\). Substituting \(t=(G-1)/B\) gives
\[
 (G-1-B)(G-1+B)^2-B^3(G-1)=0.
\]
Indeed the displayed equation vanishes identically on the asserted parameterization. Conversely, on the smooth locus it cannot have \(B=0\), since \(B=0\) forces \(G=1\) and hence \(\Delta=0\). It follows that \(t\) is defined and the preceding equivalences apply. The resulting orbit is
\[
 (\infty,1)\to(-1,\infty)\to(t,-1)\to(-t,t)\to(1,-t)\to(\infty,1).
\]
The smaller possible orders have already been ruled out, so the order is exactly five.

**(5) Algebraic structure and nonisotriviality.** Write \(F_5\) for the left side of the displayed fifth-order equation. The parameterization has rational inverse \(t=(G-1)/B\) wherever \(B\ne0\), hence its image is birational to a rational curve. More strongly, \(B(t)=(t-1)(t+1)^2/t\) has degree three as a rational map \(\mathbf P^1_t\to\mathbf P^1_B\). Thus \([\mathbf C(t):\mathbf C(B)]=3\), and \(G=1+Bt\) has degree three over \(\mathbf C(B)\). As \(F_5\) is monic cubic in \(G\) and vanishes, it is irreducible in \(\mathbf C(B)[G]\) and then primitive and irreducible in \(\mathbf C[B,G]\).

Under the parameterization, the discriminant factors exactly as
\[
 \Delta(B(t),G(t))
 =\frac{(t-1)^5(t+1)^5(t^2-4t-1)(t^2+t-1)}{t^3},
\]
which gives precisely the forbidden parameters in the statement. Finally, completing the square in \(y\) yields the equivalent quartic double cover
\[
 z^2=x^4+c x^2+G,\qquad c=\frac{B^2}{4}-1-G,
\]
with its classical elliptic invariant
\[
 j=\frac{16(c^2+12G)^3}{G(c^2-4G)^2}.
\]
As \(t\to1\), one has \(B\to0\), \(G\to1\), \(c\to-2\); the numerator approaches a nonzero number while the denominator tends to zero. Therefore \(j\) has a pole and is nonconstant on the order-five curve. This proves nonisotriviality.

## Verification
All displayed rational identities can be reproduced with exact polynomial expansion and rational arithmetic. An accompanying Python standard-library checker evaluates both directions of the indicated sample cycles, the order-five elimination equation, and the discriminant factorization on multiple rational test parameters. Representative smooth cases are \((B,G)=(1,2)\) for order three, \((0,2)\) and \((1,1)\) for order four, and \((9/2,10)\) for order five. These finitely many checks are corroboration, not an infinite or complete parameter-space proof; the preceding algebraic argument proves the classification.

## Relationship to prior work
Wu, *Direct Group Laws on Classical Genus-One Models* (arXiv:2610.00029v1, first submitted 2026-09-02), establishes the genus-one discriminant and the Vieta-involution dynamics for the general symmetric biquadratic. It does not state the exact global order-three, order-four or order-five loci above. The general group-law and torsion-translation interpretation for QRT maps, including descriptions in Hamad–Hone–van der Kamp–Quispel and in the McMillan mapping literature, is established background. A previously described free simultaneous-sign involution and its associated degree-two isogeny for this same biquadratic family gives a different translation and does not decide the order of \(H\). The specific new statements concern the explicit parameter conditions, irreducibility and nonisotrivial fifth-order locus.

## Limitations
The theorem classifies only exact orders three, four and five; it does not assert the absence of members of other finite orders. It applies over \(\mathbf C\) and excludes singular fibers. The rational parameterization concerns the fifth-order locus, not arbitrary elliptic curves with rational five-torsion. Older general QRT torsion criteria may imply the equations by specialization; a fully exhaustive historical equivalence search is not possible, so originality should be independently assessed before external publication.

## References
1. H. Wu, *Direct Group Laws on Classical Genus-One Models*, arXiv:2610.00029v1 (first submission 2026-09-02), especially Section 10 and Proposition 10.1.
2. T. Zolkin, S. Nagaitsev, I. Morozov, S. Kladov and Y.-K. Kim, *Dynamics of McMillan mappings III. Symmetric map with mixed nonlinearity*, arXiv:2410.10380v2 (2024), Sections II–V.
3. K. Hamad, A. N. W. Hone, P. H. van der Kamp and G. R. W. Quispel, *QRT maps and related Laurent systems*, arXiv:1702.07047 (2017).
4. J. J. Duistermaat, *Discrete Integrable Systems: QRT Maps and Elliptic Surfaces*, Springer (2010), background reference; its full text has not been checked against the specific equations.
