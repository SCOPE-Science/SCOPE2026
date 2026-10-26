# Unique Frobenius-triangle orbit of all-smooth conic nets in even characteristic

## Finding
For every even prime power \(q=2^r\), \(r\ge1\), a three-dimensional \(\mathbf F_q\)-linear subspace \(W\subset H^0(\mathbf P^2_{\mathbf F_q},\mathcal O(2))\) has **all its nonzero rational members geometrically smooth** if and only if its scheme-theoretic base is a noncollinear Frobenius orbit \(\{P,P^q,P^{q^2}\}\) of three degree-three points. In that case, \(W\) is precisely the space of conics through those points. All such nets lie in one \(\operatorname{PGL}_3(\mathbf F_q)\)-orbit; their total number as coordinate-fixed subspaces and their stabilizer orders are, respectively,
\[
N(q)=\frac{q^3(q-1)^2(q+1)}{3},\qquad |\operatorname{Stab}(W)|=3(q^2+q+1).
\]
In particular, \(N(2)=8\) and \(N(4)=960\). Here a *net* is a projective two-dimensional linear system (not a pencil), and a geometrically smooth conic means nonsingular over an algebraic closure.

## Assumptions and scope
The ground field is exactly \(k=\mathbf F_q\) with \(q\) a power of two. Distinct nets are distinct three-dimensional \(k\)-linear subspaces in the six-dimensional space of ternary quadratic forms in fixed coordinates, without division by \(\operatorname{PGL}_3(k)\). The base scheme is the scheme-theoretic common zero locus in \(\mathbf P^2_{\bar k}\); its three points form a reduced geometric scheme and a degree-three closed point over \(k\). The word smooth quantifies only over \(k\)-rational members of the system, but tests each such member over \(\bar k\). The statement does not require every member defined over extensions of \(k\) to be smooth.

## Proof
**1. Polar-form normal form.** Write the general ternary quadratic as \(aX^2+bY^2+cZ^2+dXY+eXZ+fYZ\). Its polar alternating matrix has kernel spanned by \((f,e,d)\) when \((d,e,f)\ne(0,0,0)\). The corresponding conic is geometrically smooth precisely when the quadratic does not vanish on that radical: this follows from its three linear partial derivatives and Euler's relation in characteristic two. If \((d,e,f)=0\), the quadratic is a square over \(\bar k\) and is singular. Therefore an all-smooth three-dimensional \(W\) projects injectively, hence isomorphically, onto the three-dimensional space of cross-term coefficients.

Parametrize its forms by \(u=(u_1,u_2,u_3)\in k^3\) so the polar radical of the member is \(u\):
\[
Q_u(X,Y,Z)=u_3XY+u_2XZ+u_1YZ+\sum_{i=1}^3\left(\sum_{j=1}^3 a_{ij}u_j\right)X_i^2,
\quad (X_1,X_2,X_3)=(X,Y,Z).
\]
The member \(Q_u\), for nonzero \(u\in k^3\), is smooth if and only if its radical evaluation is nonzero, i.e. if and only if
\[
C(u)=u_1u_2u_3+\sum_{i,j=1}^3 a_{ij}u_i^2u_j\ne0.
\]
Thus \(C\) is a homogeneous ternary cubic with **no projective \(k\)-rational zero**.

**2. Pointless cubic lemma.** A homogeneous plane cubic over any finite field with no rational projective point must be the product, over an algebraic closure, of three distinct Galois-conjugate nonconcurrent lines. Indeed, a geometrically integral smooth cubic has a rational point by the genus-one Hasse–Weil bound \(\#E(k)\ge q+1-2\sqrt q>0\). A geometrically integral singular plane cubic has exactly one singular geometric point by the arithmetic genus formula, which is necessarily Galois-fixed and rational. A geometrically reducible cubic with a proper rational component has a rational line and hence rational points. In the remaining case the three geometric degree-one components form one Galois orbit of length three. If concurrent, their unique common point is Frobenius-fixed, contradicting the absence of rational points. Thus they form a triangle. This also rules out repeated components.

**3. Gradient and base locus.** In characteristic two, differentiate \(C\) with respect to the net parameters. Direct calculation yields
\[
\frac{\partial C}{\partial u_j}(X,Y,Z)=Q_{e_j}(X,Y,Z),\qquad j=1,2,3,
\]
where \(e_j\) is the \(j\)-th standard basis vector and the point coordinates replace the parameter coordinates. The three basis conics therefore cut out the gradient-zero scheme of \(C\). Because \(C\) is the product of three distinct nonconcurrent conjugate lines, its gradient scheme is **exactly the three reduced vertices** of the triangle. Frobenius permutes them transitively. Since three noncollinear geometric points impose three independent linear conditions on the six-dimensional quadratic-form space, the conics through those vertices constitute exactly the three-dimensional net \(W\).

**4. Converse.** Conversely, let \(P,P^q,P^{q^2}\) be a noncollinear Frobenius triple. The linear system of conics through it descends to \(k\) and has vector-space dimension three. After a coordinate change over \(\bar k\) sending the three points to the coordinate vertices, it is spanned by \(XY,XZ,YZ\). A form \(dXY+eXZ+fYZ\) is nonsingular exactly when \(def\ne0\). Frobenius permutes the three vertices cyclically and hence cyclically permutes the three monomial coefficients up to nonzero factors. For any nonzero descended \(k\)-rational member, if one coefficient vanished, all three would vanish, contradiction. Thus every nonzero rational member is smooth.

**5. Count and orbit.** The closed points of degree three in \(\mathbf P^2_k\) number
\[
\frac{|\mathbf P^2(\mathbf F_{q^3})|-|\mathbf P^2(k)|}{3}=\frac{q^6+q^3-q^2-q}{3}.
\]
A collinear Frobenius triple lies on its unique Frobenius-stable (hence rational) line. Each of the \(q^2+q+1\) rational lines contributes \((q^3-q)/3\) such triples, so subtracting gives
\[
N(q)=\frac{q^6+q^3-q^2-q-(q^2+q+1)(q^3-q)}{3}=\frac{q^3(q-1)^2(q+1)}3.
\]
Given two such ordered Frobenius triples, the projective coordinate transformation carrying one to the other is Frobenius invariant; hence \(\operatorname{PGL}_3(k)\) acts transitively. Dividing \(|\operatorname{PGL}_3(k)|=q^3(q^3-1)(q^2-1)\) by \(N(q)\) gives the stated stabilizer order. This completes both directions and the exact census.

## Verification
Two standalone exact-arithmetic scripts are included. Running `python verify_nets.py` enumerates all \(q^9\) square-coefficient maps for \(q=2,4\) and tests the cubic nonvanishing on all \(q^2+q+1\) projective rational points; for \(q=2\) it independently enumerates every three-dimensional subspace of the 64 conic coefficient vectors. Running `python verify_frobenius.py` separately enumerates all Frobenius degree-three closed points over \(\mathbf F_{q^3}\) and tests the determinant of each conjugate triple. The two methods return \(8\) and \(960\) in both cases; see `verification_output.txt`. These are finite cross-checks of the preceding general proof, not a replacement for it.

## Relationship to prior work
Asgarli–Ghioca–Reichstein (arXiv:2207.00918, 2022) proved that projective dimension two is the maximum for all-smooth plane conic linear systems and constructed such systems over finite fields: existence and maximal dimension are **prior results**, not claimed here. Alnajjarine–Lavrauw (arXiv:2209.08354, 2022) classified planes meeting the rank-one Veronese locus and explicitly described the complementary plane classification as open; it cites Zanella's earlier construction of maximal nonsingular conic nets. The result here concerns a specific distinguished *all-geometrically-smooth* subclass of nets, classifies all of them via their base triangles, and supplies one orbit and an exact census. The classification is not a claim to solve the general plane-disjoint-Veronese classification.

## Limitations
Publication priority remains qualified: Zanella's 2012 *On finite Steiner surfaces* was checked at the abstract and secondary-citation level, not throughout its full text, and may contain an equivalent uniqueness or counting statement; Campbell's 1928 incomplete treatment may also encode a similar family. No universal originality certification or independent review is claimed. The geometric correspondence holds in even characteristic over finite fields as stated; the finite verification only covers \(q=2,4\).

## References
1. S. Asgarli, D. Ghioca, Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918 (first posted 2022-07-02), https://arxiv.org/html/2207.00918v2.
2. N. Alnajjarine, M. Lavrauw, *A classification of planes intersecting the Veronese surface over finite fields of even order*, arXiv:2209.08354 (2022), https://arxiv.org/html/2209.08354v1.
3. C. Zanella, *On finite Steiner surfaces*, Discrete Mathematics 312 (2012), 652–656, DOI:10.1016/j.disc.2011.05.035 (abstract accessible; full text not inspected).
4. A. Campbell, *Nets of conics in the Galois field of order \(2^n\)*, Bulletin of the American Mathematical Society 34 (1928), 481–489 (cited in reference 2; full text not inspected).
