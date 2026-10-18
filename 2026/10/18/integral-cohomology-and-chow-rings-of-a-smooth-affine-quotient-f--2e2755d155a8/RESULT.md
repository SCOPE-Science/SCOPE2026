# Integral cohomology and Chow rings of a smooth affine quotient family

## Finding
Let \(n\ge 1\). Over \(\mathbb C\), let
\[
X_n=\{x^2y+z^3w^2u_1^2\cdots u_n^2=1\}\subset\mathbb A^{n+4}
\]
with the \(\mathbb G_m\)-weights \(\operatorname{wt}(x,y,z,w,u_1,u_2,\ldots,u_n)=(1,-2,2,-2,-1,0,\ldots,0)\), and let \(Y_n=X_n/\! /\mathbb G_m\). Denote by \(D_n\) the quotient of the invariant hypersurface \(x=0\). Then \(Y_n\) is a smooth affine variety of dimension \(n+2\), and there is an algebraic two-stratum decomposition
\[
Y_n\setminus D_n\simeq\mathbb A^{n+2},\qquad
D_n\simeq\mathbb A^1\times(\mathbb G_m)^n.
\]
The divisor \(D_n\) has trivial normal line bundle. In particular, \(Y_n(\mathbb C)\) is simply connected and its **complete integral cohomology ring** is
\[
H^k(Y_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
0,&k=1,\\
\mathbb Z^{\binom n{k-2}},&2\le k\le n+2,\\
0,&k>n+2,
\end{cases}
\]
with **every product of two positive-degree classes equal to zero**. In the rational mixed Hodge structure,
\[
H^{j+2}(Y_n;\mathbb Q)\cong\mathbb Q(-(j+1))^{\binom nj}\quad(0\le j\le n).
\]
The integral Chow ring is \(\operatorname{CH}^*(Y_n)\cong\mathbb Z[h]/(h^2)\), where \(h=[D_n]\) has codimension one. Writing \(\mathbb L=[\mathbb A^1]\) in the Grothendieck ring, the class is
\[
[Y_n]=\mathbb L^{n+2}+\mathbb L(\mathbb L-1)^n,
\]
and its compactly supported Hodge--Deligne polynomial equals \((uv)^{n+2}+uv(uv-1)^n\). Consequently its Euler characteristic is \(1\) and its Poincaré polynomial is \(1+t^2(1+t)^n\). The same algebraic stratification exists for the corresponding quotient over every field, and for each finite field \(\mathbb F_q\) gives
\[
\#Y_n(\mathbb F_q)=q^{n+2}+q(q-1)^n.
\]

## Assumptions and scope
All cohomology is singular cohomology of the associated complex manifold, with integral coefficients unless otherwise indicated. Cohomology ring means graded cup-product ring, including the unit in degree zero. \(\operatorname{CH}^*(Y_n)\) is the Chow ring of the smooth affine variety. The quotient is the affine categorical quotient of a diagonalizable-group action; the explicit charts below show it is geometric and smooth over every field. Mixed Hodge structures refer to the complex model only. Point counts refer to the same integral equations reduced over finite fields; no comparison between different characteristics is assumed for the topology.

## Proof
**1. A free two-chart quotient.** Put \(P=\prod_{i=2}^n u_i^2\), with the empty product equal to \(1\). On \(x\ne0\), set
\[
Z=z/x^2,\quad W=x^2w,\quad V=xu_1,\quad U_i=u_i\ (i\ge2).
\]
These are invariant, and the equation determines \(y=x^{-2}(1-Z^3W^2V^2P)\). Thus the localized coordinate ring is \(\mathbb C[x,x^{-1},Z,W,V,U_2,\ldots,U_n]\), with \(\mathbb G_m\) acting only on \(x\). The quotient of this open set is exactly \(\mathbb A^{n+2}\).

The complement \(x=0\) forces \(z,w,u_1,\ldots,u_n\ne0\), so \(u_1\ne0\) together with \(x\ne0\) covers \(X_n\). On \(u_1\ne0\), the invariant coordinates
\[
T=xu_1,\quad Y'=y/u_1^2,\quad E=zu_1^2,\quad W'=w/u_1^2,\quad U_i=u_i
\]
realize the quotient as the hypersurface
\[
T^2Y'+E^3(W')^2P=1
\]
in affine \((n+3)\)-space. Here \(u_1\) is the free orbit coordinate. These two affine quotients glue along \(T=V\ne0\), with \(Z=E/T^2\) and \(W=T^2W'\). On the second chart the quotient is smooth: if \(T\ne0\), the derivative with respect to \(Y'\) is \(T^2\ne0\); if \(T=0\), both \(E\) and \(W'\) are nonzero, so at least one of the derivatives of \(E^3(W')^2\) with respect to \(E,W'\) is nonzero in every characteristic (since \(2\) and \(3\) are relatively prime). Thus the geometric quotient is smooth, and the chart construction works over any field.

**2. The divisor and its normal bundle.** On the second chart \(D_n\) has equation \(T=0\) and hence \(E^3(W')^2P=1\). Put \(B=EW'\). Then \(E=B^{-2}P^{-1}\), \(W'=B^3P\), and \(Y'\) is free. This gives the claimed global isomorphism \(D_n\simeq\mathbb A^1_{Y'}\times(\mathbb G_m)^n_{B,U_2,\ldots,U_n}\). Since \(D_n\) is wholly contained in the \(u_1\ne0\) quotient chart and is there the principal divisor \(T=0\), its normal line bundle is trivial. It is a smooth closed effective Cartier divisor.

**3. Integral Gysin sequence and multiplication.** Set \(U=Y_n\setminus D_n\). The integral Gysin long exact sequence for the smooth divisor \(D_n\hookrightarrow Y_n\) has segment
\[
H^{k-2}(D_n;\mathbb Z)\xrightarrow{i_*} H^k(Y_n;\mathbb Z)
\longrightarrow H^k(U;\mathbb Z)\longrightarrow H^{k-1}(D_n;\mathbb Z).
\]
Since \(U\simeq\mathbb A^{n+2}\) is contractible, \(i_*\) is an isomorphism for every \(k\ge2\), while \(H^0(Y_n;\mathbb Z)=\mathbb Z\) and \(H^1(Y_n;\mathbb Z)=0\). The torus has exterior-algebra cohomology on \(n\) integral degree-one classes, so \(H^j(D_n;\mathbb Z)\cong\mathbb Z^{\binom nj}\), with no torsion. For \(a,b\in H^*(D_n;\mathbb Z)\), the integral self-intersection and projection formulas give
\[
i_*(a)\smile i_*(b)=i_*\bigl(a\smile b\smile c_1(N_{D_n/Y_n})\bigr)=0,
\]
using the trivial normal bundle. Every positive-degree class is in the image of \(i_*\), hence the positive-degree ideal is square-zero. Hodge compatibility of the algebraic Gysin map provides one Tate twist, and \(H^j((\mathbb C^*)^n;\mathbb Q)=\mathbb Q(-j)^{\binom nj}\), giving the asserted mixed Hodge structures. The inclusion \(U\hookrightarrow Y_n\) induces a surjection on fundamental groups because a loop may be moved off the smooth real-codimension-two divisor. Since \(U\) is simply connected, so is \(Y_n\).

**4. Chow ring and counting.** The localization sequence of Chow groups, \(\operatorname{CH}^{r-1}(D_n)\to\operatorname{CH}^{r}(Y_n)\to\operatorname{CH}^{r}(U)\to0\), applies to this smooth divisor. Positive-codimension Chow groups of an affine torus times an affine line, and those of affine space, vanish. Thus \(\operatorname{CH}^r(Y_n)=0\) for \(r\ge2\), and \(\operatorname{CH}^1(Y_n)\) is generated by \([D_n]\). Its first Chern class is the generator of \(H^2(Y_n;\mathbb Z)\) under the Gysin isomorphism, so the divisor has infinite order and \(\operatorname{CH}^1(Y_n)\simeq\mathbb Z\). The scissor relation gives \([Y_n]=[U]+[D_n]\). The Hodge--Deligne and Euler formulas follow by additivity. Both quotient charts and their overlap are defined over the integers and remain valid after base change. Counting their disjoint strata over \(\mathbb F_q\) gives the displayed point-count polynomial.

## Verification
The standalone standard-library program `verify.py` checks the invariant defining equations over small finite fields, counts the two strata for \(n=1,2,3\) over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), verifies their predicted quotient counts, and checks the binomial Betti-rank and Euler formulas. Run `python3 verify.py`. The infinite-range claims are established by the algebraic chart and Gysin arguments above, not by this finite enumeration.

## Relationship to prior work
The originating construction and its generic-flexibility/nonflexibility result are due to Nikitina [1], who proves smoothness and constructs an invariant divisor using Cox-ring and locally nilpotent derivation methods. The present finding determines a full affine-space/torus-divisor decomposition and computes its **integral ring-level topology**, integral Chow ring, Hodge data, and polynomial point counts. This is a topological and arithmetic description, not a new proof of generic flexibility. Kaliman and Zaidenberg [2] develop topology of certain affine modifications in a different setting; no statement for this precise quotient or these complete invariant formulas was identified in accessible material. The Gysin and intersection formulas used here are standard, as are the affine and toric Chow calculations.

## Limitations
This result does not determine the full homotopy type or higher homotopy groups, the automorphism group, or the integral motive of \(Y_n\). Equality of classes in the Grothendieck ring is not a claimed motivic isomorphism. The finite-field count uses an integral model; the cohomology statements concern the complex variety. Literature equivalence risk remains because not all historical affine-modification papers could be fully inspected, and the final pages of the originating PDF were unavailable for full-text inspection.

## References
[1] Alina Nikitina, *Generically Flexible Varieties with an Invariant Divisor*, arXiv:2610.05344, first submitted 2026-10-04, https://arxiv.org/abs/2610.05344.

[2] Shulim Kaliman and Mikhail Zaidenberg, *Affine modifications and affine hypersurfaces with a very transitive automorphism group*, arXiv:math/9801076, first submitted 1998-01-16, https://arxiv.org/abs/math/9801076.
