# Generic degree-\(32\) node-splitting field of the Fresnel–Kummer quartic

## Finding
Let \(K=\mathbb Q(a,b,c)\), where \(a,b,c\) are algebraically independent, and let \(S\subset\mathbb P^3_K\) be the homogeneous Fresnel quartic
\[
F=(X^2+Y^2+Z^2)(aX^2+bY^2+cZ^2)
-T^2\{a(b+c)X^2+b(c+a)Y^2+c(a+b)Z^2\}+abcT^4=0.
\]
The reduced singular scheme of \(S\) consists of four closed points of degree \(4\) over \(K\), each geometrically splitting into four ordinary double points. The smallest Galois extension of \(K\) over which all sixteen singular points are rational has degree **\(32\)**, with Galois group \((\mathbb Z/2\mathbb Z)^5\). The four orbits are precisely the four coordinate-plane packets \(Y=0\), \(X=0\), \(Z=0\), and \(T=0\); each orbit is a free transitive orbit under a quotient \((\mathbb Z/2)^2\).

## Assumptions and scope
All assertions concern the generic function field \(K=\mathbb Q(a,b,c)\), not every numerical specialization. We assume \(abc(a-b)(b-c)(c-a)\ne0\), which is automatic in \(K\). The coordinates are \([X:Y:Z:T]\). A closed point of degree four means its residue field has dimension four over \(K\). The full splitting field means the compositum of the residue fields of all geometric singular points. The plane partition and ordinary-node count in the same quartic were previously established in [1]; the arithmetic splitting degree, Galois group and field-interdependence asserted here are the additional results.

Put \(p=b-a\), \(q=c-b\), and \(r=c-a=p+q\), and define eight nonzero elements of \(K\):
\[
\begin{aligned}
 A&=cp/r,&B&=aq/r,&C&=-cp/q,&D&=br/q,\\
 E&=br/p,&H_F&=-aq/p,&G&=-q/r,&H&=-p/r.
\end{aligned}
\]
The symbol \(H_F\) denotes a radicand and is not the quartic \(F\). Explicit representatives of the sixteen geometric singularities are
\[
\begin{array}{ll}
[\pm\sqrt A:0:\pm\sqrt B:1], & [0:\pm\sqrt C:\pm\sqrt D:1],\\
[\pm\sqrt E:\pm\sqrt{H_F}:0:1], & [\pm\sqrt G:1:\pm\sqrt H:0].
\end{array}
\]
Each pair of signs is independently chosen, giving four points in each plane.

## Proof
**(1) Exhaustive geometry and local reducedness.** Write \(R=X^2+Y^2+Z^2\), \(U=aX^2+bY^2+cZ^2\), and \(V=a(b+c)X^2+b(c+a)Y^2+c(a+b)Z^2\). The equation is \(RU-T^2V+abcT^4\). Its derivatives in the first three variables have factors \(2X,2Y,2Z\), with residual factors \(U+aR-a(b+c)T^2\), \(U+bR-b(c+a)T^2\), and \(U+cR-c(a+b)T^2\). The \(T\)-derivative is \(-2TV+4abcT^3\). Solving on the three affine coordinate planes with \(T=1\) yields exactly the first three displayed quartets. At \(T=0\), the singular equations require \(R=U=0\), yielding the last quartet after setting \(Y=1\). The converse exclusion of additional solutions follows by subtracting the residual factors, exactly as in the case analysis of [1, Proposition 4.3]; it is also immediate when three variables are nonzero, since the differences force \(R=aT^2=cT^2\), impossible over \(K\). Cases with two vanishing affine spatial coordinates fail by substitution. Thus the displayed sixteen points are exhaustive.

The determinants of the Hessian matrices in three affine local coordinates are, respectively,
\[
\begin{aligned}
Y=0 &: 32ac(a-b)^2(b-c)^2,\\
X=0 &: 32bc(a-b)^2(a-c)^2,\\
Z=0 &: 32ab(a-c)^2(b-c)^2,\\
T=0,\ Y=1 &: 32(a-b)^2(b-c)^2.
\end{aligned}
\]
These follow from the identity \(\partial_i\partial_j(RU)=2\delta_{ij}(U+\varepsilon_iR)+4(\varepsilon_i+\varepsilon_j)x_ix_j\), with the other quartic terms differentiated directly. All determinants are nonzero. Each displayed point is therefore a reduced ordinary double point, and the singular scheme is finite étale over \(K\).

**(2) Five squareclass generators.** The eight radicands satisfy three identities **up to rational squares**:
\[
\begin{aligned}
G&=AC\bigl(q/(cp)\bigr)^2,\\
H&=ACDE\bigl(q/(bcr)\bigr)^2,\\
H_F&=ABCDE\bigl(q/(bcp)\bigr)^2.
\end{aligned}
\]
Consequently, all sixteen points are rational over
\[
L=K(\sqrt A,\sqrt B,\sqrt C,\sqrt D,\sqrt E).
\]
To prove that this compositum has degree \(2^5\), use the UFD \(\mathbb Q[a,b,c]\): the distinct irreducible factors \(a,b,c,p,q,r\) give independent valuation vectors modulo two. The squareclasses of \(A,B,C,D,E\), in the order \((a,b,c,p,q,r)\), are
\[
\begin{array}{c|cccccc}
 &a&b&c&p&q&r\\\hline
A&0&0&1&1&0&1\\
B&1&0&0&0&1&1\\
C&0&0&1&1&1&0\\
D&0&1&0&0&1&1\\
E&0&1&0&1&0&1
\end{array}.
\]
They have rank five over \(\mathbb F_2\): in a dependence, the \(a\)-coordinate first forces the coefficient of \(B\) to vanish; the \(c\)- and \(p\)-coordinates force the coefficients of \(A,C,E\) to satisfy \(\alpha_A=\alpha_C\) and \(\alpha_E=0\); the \(q\)-coordinate and then the \(b\)-coordinate force \(\alpha_D=\alpha_C\) and \(\alpha_D=0\), hence every coefficient vanishes. Equivalently, row reduction of the displayed matrix has rank five. Kummer theory in characteristic zero gives \([L:K]=32\) and \(\operatorname{Gal}(L/K)\cong(\mathbb Z/2)^5\).

**(3) Degree-four closed points and minimality.** Each of the pairs \((A,B)\), \((C,D)\), \((E,H_F)\), \((G,H)\) consists of independent squareclasses. This follows by restricting the six-factor parity vectors; equivalently, each pair gives a matrix of rank two. Hence each displayed sign packet is one degree-four closed point. Conversely, rationalizing all sixteen singular points requires the square roots of \(A,B,C,D,E\) from the first three packets; therefore every splitting field contains \(L\). Combined with (2), \(L\) is the minimal splitting field. The action on each packet is the independent sign-change action of its two-dimensional quotient, proving the claimed orbit structure.

## Verification
The standalone \(verify_nodes.py\) uses exact rational arithmetic to replay the quartic and gradient identities at five nondegenerate numerical triples, verify the four local Hessian-determinant formulas, verify three radical relations, and perform binary row reduction on the independent valuation vectors. Run `python3 verify_nodes.py`; it prints `VERIFY_OK`. The rank-five proof concerns the independent formal irreducible divisors of \(\mathbb Q[a,b,c]\); finite numerical examples by themselves are not used to prove generic independence.

## Relationship to prior work
Shaska [1, Proposition 4.3] establishes the sixteen-node geometry and places the nodes in the four coordinate planes, and [1, Theorem 4.5] identifies the complex Kummer model and the distinction between its real form and the physical Fresnel form. Those are premises, not claimed novelties. The present finding determines the **generic arithmetic residue fields, common splitting extension and five-dimensional elementary abelian Galois action** of the explicit quartic over \(\mathbb Q(a,b,c)\). This is a field-of-definition invariant not implied numerically by the sixteen-node count or the real-node count. Earlier classical work on tetrahedroids and Kummer surfaces [2,3] covers the geometric configuration in broader families; no previously identified statement gives this specific generic degree-\(32\) extension and four degree-\(4\) orbits.

## Limitations
The degree \(32\) is a generic result; specializing \(a,b,c\) can make radical classes dependent, lowering the splitting degree, although the geometric singularities remain ordinary nodes whenever \(abc(a-b)(b-c)(c-a)\ne0\). The Galois action is on the nodes of the **Fresnel quartic over the formal parameter field**, not the distinct real form given by the Jacobian Kummer model. The result does not compute Picard groups, fields of moduli, or arithmetic of arbitrary tetrahedroids. Classical or unindexed arithmetic accounts may contain an equivalent computation; the checked literature is not an exhaustive originality proof.

## References
[1] Tanush Shaska, *Exact Quotients of Fresnel-Kummer Surfaces and Certified Biaxial Refraction*, arXiv:2609.23249, first submitted 2026-09-19, especially §§4.1–4.4, Proposition 4.3 and Theorem 4.5. https://arxiv.org/abs/2609.23249.

[2] S. J. Patterson, *On a question of H. A. Schwarz*, arXiv:1912.06807 (2019), on tetrahedroids and Kummer geometry. https://arxiv.org/abs/1912.06807.

[3] J. W. S. Cassels and E. V. Flynn, *Prolegomena to a Middlebrow Arithmetic of Curves of Genus 2*, London Mathematical Society Lecture Note Series 230, Cambridge University Press, 1996 (background on Kummer models; not independently inspected in full).
