# A degree-twelve Galois orbit of nodes on a rational septic

## Finding
Let \(C/\mathbb Q\subset\mathbb P^2\) be the rational septic parametrized by
\[
\nu([u:v])=[uv^6-u^7:u^5(u^2+v^2):v^5(u^2+v^2)].
\]
Write \(x=X/Z\) and \(y=Y/Z\) on the affine chart \(Z\ne0\). Define
\[
D(T)=T^{12}+15T^{10}+71T^8+84T^6+9T^4-3T^2-1,
\]
\[
r(T)=\frac{T}{40}\left(17T^{10}+254T^8+1193T^6+1371T^4+134T^2-1\right).
\]
The twelve ordinary nodes other than \(P=[1:0:0]\) are **exactly** the points
\[
\{[r(\alpha):\alpha:1]:D(\alpha)=0\}.
\]
The polynomial \(D\) is irreducible over \(\mathbb Q\). Hence these twelve nodes form one Galois orbit, and their reduced zero-dimensional scheme is \(\operatorname{Spec}\mathbb Q[T]/(D(T))\), embedded by the displayed graph. Each has residue degree twelve; none is rational over \(\mathbb Q\).

Moreover, for every prime \(p\notin\{2,5,821\}\), the reduction has precisely thirteen ordinary geometric nodes and one unibranch cusp of local branch orders \((2,5)\). Its numbers of \(\mathbb F_p\)-rational **nodes** and of all rational singular points are, respectively,
\[
1+\#\{a\in\mathbb F_p:D(a)=0\},\qquad
2+\#\{a\in\mathbb F_p:D(a)=0\}.
\]
Thus at \(p=7\) there is just one rational node and one rational cusp, while at \(p=11\) there are three rational nodes and one rational cusp. The exceptional primes are excluded, not classified.

## Assumptions and scope
The characteristic-zero statement concerns the plane curve over \(\mathbb Q\) with the displayed parametrization, not the arithmetic of every Galois-point curve. Its distinguished inner Galois point \(P\) and the point \(Q=[-1:1:0]\) at infinity are rational. The reduction statement is for all prime fields of characteristics distinct from \(2\), \(5\), and \(821\); the word "node" refers to an ordinary double point over an algebraic closure. No claim is made about splitting of its two local branches over the prime field.

## Proof
**1. Elimination and birationality.** For \(v=1\), the parametrization has
\[
y=t^5,\qquad x=\frac{t-t^7}{1+t^2}.
\]
Its implicit affine equation is the irreducible polynomial
\[
\begin{aligned}
E(x,y)={}&x^5(y^2+1)+5x^4(y^3-y)+10x^3(y^4-y^2)\\
&+5x^2(2y^5-y^3+y)+5x(y^6+y^2)+y^7-y=0.
\end{aligned}
\]
Indeed \(E\) is the negative of \(\operatorname{Res}_t(t^5-y,\,x(1+t^2)-t+t^7)\). In every characteristic different from \(5\), the degree-five extension \(k(t)/k(t^5)\) has prime degree, while \(x(t)\) has valuation one at \(t=0\) and thus is not in \(k(t^5)\). Consequently \(k(t^5,x(t))=k(t)\), proving that \(\nu\) is birational onto the irreducible degree-seven curve \(C\).

**2. The affine singular scheme.** Direct resultant computation gives the exact identity
\[
\operatorname{disc}_{x}(E)=3125\,y^4D(y)^2.
\]
The two further identities
\[
\operatorname{disc}(D)=-2^{36}5^{18}821^2,\qquad
D(T)\bmod(T^2+1)=-16
\]
show that \(D\) is separable over \(\mathbb Q\) and over all the asserted residue characteristics, its roots are nonzero, and none lies on the leading-coefficient locus \(y^2+1=0\). In the quotient ring \(\mathbb Z[1/40,T]/(D(T))\), the three polynomial congruences
\[
E(r(T),T)=E_x(r(T),T)=E_y(r(T),T)=0
\]
hold. They may be checked by polynomial remainder, with no numerical approximation. Thus every root of \(D\) produces a singular point, and the \(y\)-values of these points are pairwise distinct.

Conversely an affine singular point satisfies \(E=E_x=0\), hence its \(y\)-coordinate is zero or a root of \(D\). The only point above \(y=0\) is \((0,0)\), which is smooth because \(E_y(0,0)=-1\). At a simple root \(a\) of \(D\), the discriminant vanishes to precisely order two. The map \(t\mapsto t^5\) is unramified at each preimage, because \(a\ne0\) and the characteristic is not \(5\). Therefore an order-two discriminant zero can only arise from one transverse collision of two smooth local branches: it is exactly one ordinary node. Two distinct double collisions over the same ordinate, a tangent collision, or a higher-order collision would force discriminant order at least four. The displayed graph gives its unique \(x\)-coordinate.

**3. Points at infinity.** The preimages of \(Z=0\) are \(v=0\) and the two points \(u/v=\pm i\), with \(i^2=-1\). The latter both map to \(P\); in the chart \(X=1\) their tangent slopes \(Y/Z\) are \(\pm i\), giving an ordinary node for odd characteristic. The former maps to \(Q\). With \(w=v/u\), its local coordinates in the chart \(Y=1\) satisfy
\[
X/Y+1=\frac{w^2(1+w^4)}{1+w^2},\qquad Z/Y=w^5.
\]
For characteristics different from \(2,5\), these give a unique unibranch cusp with characteristic pair \((2,5)\). Since every point in the image of the projective normalization has been accounted for, no additional singularities occur.

**4. Irreducibility and arithmetic.** Reduce \(D\) modulo \(7\). Modular repeated squaring yields
\[
T^{7^6}\equiv-T,\qquad T^{7^{12}}\equiv T\pmod{D(T)},
\]
and
\[
\gcd(D,T^{7^4}-T)=\gcd(D,T^{7^6}-T)=1
\quad\text{in }\mathbb F_7[T].
\]
The finite-field irreducibility criterion for degree twelve (the prime divisors of twelve are two and three) proves \(D\) irreducible modulo seven, hence over \(\mathbb Q\). Since the node's \(y\)-coordinate generates its residue field and \(x=r(y)\), the twelve geometric points comprise one degree-twelve Galois orbit. Reduction outside \(2,5,821\) preserves the graph and all simple roots; exactly those with \(y\in\mathbb F_p\) are rational. Adding \(P\) gives the node formula and adding the rational cusp \(Q\) gives the singular-point formula.

## Verification
The accompanying `verify.py` reconstructs the resultant polynomial, verifies both discriminants and the graph's three Jacobian congruences, checks the two modular greatest-common-divisor identities needed for irreducibility, and checks example root counts in six prime fields. It uses only exact integer/rational arithmetic and finite-field polynomial calculations with SymPy. The geometric transversality argument, birationality, and uniform quantification over all permitted primes are proven above rather than inferred from sampling.

## Relationship to prior work
Abouelsaad's paper *Galois Points and Cremona Transformations*, Theorem C and Lemma 5.2, supplies precisely the displayed degree-seven parametrization and its nonextendable inner order-five Galois action. That paper studies Cremona extendability and a bound on singular multiplicities, not a degree-twelve arithmetic singular-point scheme or its prime-field rationality. General work on extendable transformations (for example Miura's 2023 paper) addresses different Galois-point extension questions. The geometric count and analytic types of singularities are not presented here as the original contribution; the new content is the rational node-coordinate algebra, Galois transitivity, and exact uniform good-prime descent rule.

## Limitations
The theorem does not determine the full splitting Galois group of \(D\), the densities of every possible number of rational nodes, or the geometry in characteristics \(2\), \(5\), and \(821\). It counts rational singular **points**, not all rational points on \(C\); it does not claim that rational nodes have individually rational branches. The assessment of originality rests on inspected texts and targeted searches and cannot exclude every unindexed calculation. Independent validation has not been performed.

## References
- A. Abouelsaad, *Galois Points and Cremona Transformations*, arXiv:2302.00324v1 (public February 1, 2023), especially Theorem C and Lemma 5.2. https://arxiv.org/html/2302.00324v1
- K. Miura, *Extendable birational transformations belonging to Galois points*, arXiv:2302.00870v1 (public February 2, 2023), Sections 1–5. https://arxiv.org/html/2302.00870v1
