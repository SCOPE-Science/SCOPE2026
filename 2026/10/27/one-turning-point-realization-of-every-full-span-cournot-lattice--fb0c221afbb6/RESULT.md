# One-turning-point realization of every full-span Cournot lattice

## Finding
Let \(I=[0,1]\). For every integer \(m\geq 1\) and every pair of sets \(P,Q\subset (0,1)\) with \(|P|=|Q|=m\), there are continuous surjective piecewise-linear maps \(f_1,f_2:I\to I\), each strictly increasing before a single interior maximum and strictly decreasing afterward, for which the anti-triangular map \(F(x,y)=(f_2(y),f_1(x))\) has a point \(z\in I^2\) satisfying
\[
\omega_F(z)=(P\times I)\cup (I\times Q).
\]
Moreover, both \(f_2\circ f_1\) and \(f_1\circ f_2\) are topologically exact. Both reaction maps send both endpoints to zero and attain the value one precisely at their unique maxima.

## Assumptions and scope
The sets \(P\) and \(Q\) consist of \(m\) **distinct** points strictly between zero and one; their locations are otherwise arbitrary and independent. A map is *strictly unimodal* if it is strictly increasing on the left of one interior turning point and strictly decreasing on the right. *Topologically exact* means that for every nonempty relatively open interval \(U\subset I\), some iterate maps \(U\) onto all of \(I\). The \(\omega\)-limit set of a point consists of all accumulation points of its forward orbit. We assert realization of **full-span** horizontal and vertical lattices; arbitrary smaller supporting intervals and logistic-polynomial reaction functions are not covered.

## Proof
**1. An explicit alternating tent cycle.** Let \(T(t)=2\min(t,1-t)\), \(d=2^{2m}+1\), and define
\[
 a_j=\frac{2^{j+1}}{d},\qquad 0\le j<2m.
\]
All \(a_j\) lie strictly between zero and one and are strictly increasing in \(j\). For \(j<2m-1\), one has \(a_j<1/2\) and hence \(T(a_j)=a_{j+1}\); while \(a_{2m-1}=1-1/d\) and \(T(a_{2m-1})=a_0\). Thus the \(a_j\) form an orbit of **least** period \(2m\). This last identity also holds for \(m=1\).

**2. Two independent changes of coordinates.** Write \(P=\{p_0<\cdots<p_{m-1}\}\) and \(Q=\{q_0<\cdots<q_{m-1}\}\). There are unique increasing piecewise-linear homeomorphisms \(h,k:I\to I\), linear between consecutive prescribed nodes, such that
\[
 h(0)=k(0)=0,\quad h(1)=k(1)=1,\quad
 h(a_{2i})=p_i,\quad k(a_{2i+1})=q_i\quad(0\le i<m).
\]
Set
\[
 f_1=k\circ T\circ h^{-1},\qquad
 f_2=h\circ T\circ k^{-1}.
\]
Every piece is linear and continuous. Since both \(h\) and \(k\) are strictly increasing, \(f_1\) and \(f_2\) have exactly the single turning points \(h(1/2)\) and \(k(1/2)\), respectively; they have no constant pieces. They are onto, with endpoints zero and unique maximum one. They satisfy
\[
 f_1(p_i)=q_i,\qquad f_2(q_i)=p_{i+1\ (\mathrm{mod}\ m)}.
\]
Their two-step compositions reduce exactly to
\[
 \phi=f_2\circ f_1=h\circ T^2\circ h^{-1},\qquad
 \chi=f_1\circ f_2=k\circ T^2\circ k^{-1}.
\]
Because every nonempty interval contains a sufficiently small dyadic tent branch that some iterate of \(T\) maps onto \(I\), the map \(T\), and therefore every positive power \(T^r\), is topologically exact. Conjugacy proves exactness of \(\phi\) and \(\chi\).

**3. A dense independent coordinate on every phase.** Topological exactness of \(\chi^m\) implies topological transitivity, hence the existence of a point \(y\in I\) whose forward orbit under \(\chi^m\) is dense in \(I\) (for example by the Baire-category transitive-point theorem). Take \(z=(p_0,y)\). Iterating the defining map twice gives
\[
 F^{2n}(z)=(p_{n\ (\mathrm{mod}\ m)},\chi^n(y)).
\]
For each fixed residue \(i\in\{0,\ldots,m-1\}\), the subsequence with \(n=jm+i\) has full closure \(\{p_i\}\times I\): the orbit of \(\chi^m\) is dense and \(\chi^i\) is onto. Consequently
\[
 \omega_{F^2}(z)=P\times I.
\]
Continuity and surjectivity give
\[
 \omega_{F^2}(F(z))=F(P\times I)=I\times Q,
\]
using the identities for \(f_1(p_i)\) and that \(f_2(I)=I\). The even and odd iterates exhaust the orbit, so
\[
 \omega_F(z)=\omega_{F^2}(z)\cup\omega_{F^2}(F(z))
 =(P\times I)\cup(I\times Q).
\]
All equalities concern the full infinite orbit, with no approximation. This proves the claim.

## Verification
The accompanying exact-rational checker tests \(180\) explicitly prescribed pairs of finite sets for \(1\le m\le6\), the alternating cycle and two maps at the prescribed points, their endpoint and peak properties, and \(5580\) exact composition identities at rational test arguments. It returned `CHECKS_PASS`. These finite tests are *supporting diagnostics* only. The proof of universal realization and infinite orbit density is analytic, relying on conjugacy and exactness of the tent map, not on enumeration.

## Relationship to prior work
Kalies and Wehbe (2026) study compositional dynamics and show that direct **product maps** may carry asymptotic structure not captured by factor attractor-lattice coproducts (their Example 4.6). This motivates examining coherent phase classes when a Cournot map squares to a product map. Linero Bas and Muñoz Guillermo (2021) analyze the topology of Cournot \(\omega\)-limit sets, including connected sets with empty interior, but do not supply an arbitrary prescribed full-span cross-lattice construction with both reactions strictly unimodal. García Guirao (2026) constructs general Cournot lattices with piecewise-linear reactions and explicitly asks about unimodal realizations; that general realization does not enforce the present one-critical-point restriction. Here the resolved case is specifically the full-span lattice with independently arbitrary interior point locations and exactly one turning point in each reaction. Neither the general piecewise-linear realization nor the product-attractor results imply that turning-point bound.

## Limitations
The construction does not cover lattices with proper subintervals \(P\times J\) or \(K\times Q\), finite sets touching the boundary, a prescribed physical parametric family, or prescribed regularity beyond piecewise linearity. It does not assert that every lattice is realizable by unimodal reactions or any uniqueness of the reactions. The designated limit set is nowhere dense, not an attractor asserted to be robust under perturbation. An independently identified equivalent result under alternate terminology could supersede the priority claim.

## References
1. William D. Kalies and Tony Wehbe, *Compositionality of Global Dynamics in Product and Skew-Product Systems*, arXiv:2606.30925v1, first posted June 29, 2026, especially §4 and Example 4.6. https://arxiv.org/abs/2606.30925
2. Antonio Linero Bas and Juan Muñoz Guillermo, *A Full Description of \(\omega\)-Limit Sets of Cournot Maps Having Non-Empty Interior and Some Economic Applications*, Mathematics **9** (2021), article 452; especially §5. https://doi.org/10.3390/math9040452
3. Juan Luis García Guirao, *Connected \(\omega\)-limit sets of Cournot maps: periodic orbits, realization and almost every point*, arXiv:2610.27229v1, posted October 19, 2026, especially its general lattice realization and the unimodal-reaction question. https://arxiv.org/abs/2610.27229
