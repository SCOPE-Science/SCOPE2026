# The characteristic-five Hasse divisor of the reciprocal genus-three Howe family

## Finding
Let \(k=\overline{\mathbb F}_5\). For \((u,v)\in k^2\), put
\[
f_{u,v}(x)=x^8+ux^6+vx^4+ux^2+1,
\qquad
\Delta(u,v)=(2u-v-2)(2u+v+2)(u^2-4v+8).
\]
For every \(\Delta(u,v)\ne0\), the smooth projective curve \(C_{u,v}:y^2=f_{u,v}(x)\) is hyperelliptic of genus three. Define
\[
F_+(u,v)=u^2+2v+2u,\quad
F_-(u,v)=u^2+2v-2u,\quad
F_0(u,v)=2u^2+v^2+2.
\]
Its Jacobian has \(5\)-rank equal to the number of nonzero values in \(\{F_+,F_-,F_0\}\), and \(a\)-number equal to three minus that rank. In particular, the smooth marked family has the complete stratification:

| Condition on \((u,v)\) | \(5\)-rank | \(a\)-number |
| --- | ---: | ---: |
| \(F_+F_-F_0\ne0\) | 3 | 0 |
| Exactly one of \(F_+,F_-,F_0\) vanishes | 2 | 1 |
| \((u,v)=(0,0),(2,0),(-2,0)\) | 1 | 2 |
| All three vanish | impossible on the smooth locus | — |

On \(U=\{\Delta\ne0\}\subset\mathbb A_k^2\), the scheme-theoretic nonordinary divisor \(V(F_+F_-F_0)\) is **reduced with simple normal crossings**. Its three irreducible components are two parabolas \(V(F_+)\), \(V(F_-)\) and one geometrically irreducible conic \(V(F_0)\). Each pair meets in exactly one point on \(U\), transversely, and no three components meet. The three rank-one points above are exactly these intersections. Thus **no smooth curve in this marked family has \(5\)-rank zero or \(a\)-number three**.

## Assumptions and scope
The base field is algebraically closed of characteristic five. All polynomial equalities below are taken in characteristic five. We study the displayed *marked* affine parameter space \(U\), not the coarse moduli quotient: different parameters can represent isomorphic curves. The smoothness condition \(\Delta\ne0\) excludes repeated branch roots. We make no assertion about the Newton slopes of rank-one or rank-two members beyond the stated rank and \(a\)-number.

## Proof
**Smoothness.** An exact discriminant identity, valid already over \(\mathbb Z[u,v]\), is
\[
\operatorname{Disc}_x(f_{u,v})=
256(2u-v-2)^2(2u+v+2)^2(u^2-4v+8)^4.
\]
Because \(256\ne0\) in characteristic five, \(\Delta\ne0\) is equivalent to \(f_{u,v}\) being squarefree. It has degree eight and nonzero leading coefficient; the smooth hyperelliptic projective model therefore has genus three.

**Hasse–Witt matrix.** Use the holomorphic differential basis \(\{dx/y,x\,dx/y,x^2\,dx/y\}\). Let \(c_m\) be the coefficient of \(x^m\) in \(f_{u,v}(x)^2\). For characteristic five the Hasse–Witt matrix is, up to the usual Frobenius-semilinear convention, \(H=(c_{5i-j})_{1\le i,j\le3}\). Expanding gives
\[
H=\begin{pmatrix}
u^2+2v&0&2u\\0&2u^2+v^2+2&0\\2u&0&u^2+2v\end{pmatrix}.
\]
In the constant eigenbasis \(e_1+e_3,e_1-e_3,e_2\) (defined over \(\mathbb F_5\)), this semilinear operator is diagonal, with diagonal entries \(F_+,F_-,F_0\). Because the change of basis is defined over the prime field, all its Frobenius twists are the same; iterated Frobenius has a nonzero coordinate exactly when the corresponding \(F_j\) is nonzero. Thus its stable rank is the number of nonzero \(F_j\), equal to the \(5\)-rank. The \(a\)-number equals \(3-\operatorname{rank}H\), giving the stated table. In particular \(\det H=F_+F_-F_0\).

**Divisor components and intersections.** Each of \(F_+,F_-\) is a graph of a polynomial in \(u\), hence smooth and irreducible. The projective closure of \(F_0=0\) is the nonsingular conic \(2u^2+v^2+2w^2=0\), so \(F_0\) is geometrically irreducible and smooth. Since \(F_+-F_-=4u\), the first two components meet only at \((u,v)=(0,0)\), where \(F_0=2\). For \(F_+=0\), eliminate \(v\) as \(v=2u^2+4u\). An identity in \(\mathbb F_5[u]\) yields
\[
4F_0(u,2u^2+4u)=(u-1)^3(u+2).
\]
The root \(u=1\) gives the excluded discriminant point \((1,1)\), while the simple root \(u=-2\) gives \((-2,0)\in U\). Similarly, on \(F_-=0\), use \(v=2u^2+u\) to obtain
\[
4F_0(u,2u^2+u)=(u+1)^3(u-2).
\]
The triple root \(u=-1\) lies at the excluded point \((-1,1)\); the simple root \(u=2\) gives \((2,0)\in U\). The gradients of each intersecting pair are linearly independent at all three points (the associated \(2\times2\) Jacobian determinants are nonzero modulo five). All three points satisfy \(\Delta\ne0\). Hence the reduced divisor has simple normal crossings on \(U\), exactly as claimed. No point has all three Hasse factors zero.

**Elliptic interpretation.** The commuting involutions on \(C_{u,v}\) are
\[
\alpha:(x,y)\mapsto(-x,y),\quad
\beta:(x,y)\mapsto(1/x,y/x^4),\quad
\alpha\beta:(x,y)\mapsto(-1/x,y/x^4).
\]
The corresponding smooth genus-one quotient curves are
\[
\begin{aligned}
E_0:&\quad Y^2=Z^4+uZ^3+vZ^2+uZ+1,\\
E_-:&\quad W^2=Z^4+(u-4)Z^2+(v-2u+2),\\
E_+:&\quad W^2=Z^4+(u+4)Z^2+(v+2u+2).
\end{aligned}
\]
The quotient coordinates are \((Z,Y)=(x^2,y)\), \((Z,W)=(x+1/x,y/x^2)\), and \((Z,W)=(x-1/x,y/x^2)\), respectively. The standard elliptic Hasse coefficient \([Z^4](\text{quartic})^2\) equals \(F_0,F_-,F_+\), respectively. The classical prime-to-five decomposition of the Jacobian under the Klein four action gives an isogeny \(\operatorname{Jac}(C_{u,v})\to E_0\times E_-\times E_+\) of \(2\)-power degree. Consequently their \(5\)-divisible groups agree up to isomorphism, independently confirming the rank and \(a\)-number description. The elliptic quotient construction itself is prior work, not claimed as new here.

## Verification
The companion executable `verify.py` uses exact modular-polynomial arithmetic with Python and SymPy. It checks the degree-eight discriminant identity, all nine Hasse–Witt entries, its three-factor determinant, three elliptic quotient substitutions and Hasse coefficients, the two elimination factorizations, the smoothness and transversality of the three intersections, and all \(\mathbb F_5\)-rational parameter cases. It returns `VERIFY_OK`. The finite-field enumeration is corroborative; the symbolic factorizations and geometric arguments prove the assertions over the algebraic closure.

## Relationship to prior work
Glass–Pries (2004) develop general \(p\)-torsion strata and commuting-involution constructions, including existence of hyperelliptic genus-three curves with rank one and \(a\)-number two. Gutierrez–Sevilla–Shaska (2012) and Shaska–Shor (2013) describe hyperelliptic genus-three families with additional involutions. Ohashi (2021), especially Section 3, uses **the same reciprocal octavic and parameters**, records its smoothness factors, gives the three elliptic quotient equations, and studies superspecial hyperelliptic Howe curves. These classical structures are not new contributions here. The new, narrower statement is the exact characteristic-five **marked Hasse-divisor decomposition, complete rank/\(a\)-number stratification, three transverse rank-one intersections and absence of rank-zero members**; none is asserted by those inspected theorems. Elkin–Pries treat characteristic-five strata for general genus-three hyperelliptic curves, not this three-factor divisor on the reciprocal Howe locus. Historical priority of an equivalent calculation in unindexed elliptic-quotient or finite-field tables remains uncertain.

## Limitations
The classification concerns marked parameters \((u,v)\) and not isomorphism classes; the components can become identified in a moduli quotient. It determines rank and \(a\)-number, not full Newton polygons. The elliptic quotient identities and isogeny splitting were known; the contribution is the characteristic-five arithmetic stratification and its intersection geometry. No claim of independent external verification or global historical priority is made.

## References
- D. Glass and R. Pries, *Hyperelliptic Curves with Prescribed \(p\)-Torsion*, arXiv:math/0401008 (first public 2004-01-02), especially Sections 2 and 5.
- J. Gutierrez, D. Sevilla and T. Shaska, *Hyperelliptic Curves of Genus 3 with Prescribed Automorphism Group*, arXiv:1209.2938 (2012).
- T. Shaska and C. Shor, *The 2-Weierstrass Points of Genus 3 Hyperelliptic Curves with Extra Automorphisms*, arXiv:1307.8177 (2013), especially Section 3.
- A. Elkin and R. Pries, *Hyperelliptic Curves with \(a\)-Number 1 in Small Characteristic*, especially Sections 2 and 3.3, open text: https://www.math.colostate.edu/~pries/Preprints/00DecPreprints/07g3smallphyper907.pdf.
- R. Ohashi, *On the Maximality of Hyperelliptic Howe Curves of Genus 3*, arXiv:2112.11152 (2021), especially Section 3 and Theorem 1.1.
