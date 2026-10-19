# Four equidimensional square-zero components of the seventh-truncated two-cycle algebra

## Finding

Let \(k\) be any field of characteristic different from \(2\), let \(Q\) be the oriented quiver with two vertices and one arrow in each direction, and let \(A=kQ/J^7\), where \(J\) is the arrow ideal. Thus \(A\) has dimension \(14\). Denote by \(X\) the **reduced** algebraic variety \(\{v\in A:v^2=0\}_{\mathrm{red}}\). Then \(X\) has exactly **four geometrically irreducible components**, all of dimension \(7\), and
\[
[X]=\mathbb L^6(4\mathbb L-3)\quad\text{in }K_0(\operatorname{Var}_k),\qquad \mathbb L=[\mathbb A^1_k].
\]
In particular, for each finite field \(\mathbb F_q\) of odd characteristic,
\[
\#\{v\in A(\mathbb F_q):v^2=0\}=q^6(4q-3).
\]
When \(k\) has characteristic \(7\), this algebra is isomorphic to the modular group algebra \(k[D_{14}]\), where \(D_{14}\) is the dihedral group of order \(14\). Thus the same geometric classification and the count \(q^6(4q-3)\), in particular \(2{,}941{,}225\) for \(q=7\), hold for that group algebra.

## Assumptions and scope

All varieties are reduced. The component statements are geometric: they remain true after passing to an algebraic closure. There is **no** assumption that the field is algebraically closed or finite, except in the respective conclusions. Characteristic \(2\) is excluded; no scheme-theoretic reducedness is asserted for the equation scheme \(v^2=0\).

One can represent an element of \(A\) uniquely by four polynomials
\[
\begin{pmatrix} a(z)&z b(z)\\ c(z)&d(z)\end{pmatrix},
\]
where \(a,d\in k[z]/(z^4)\) and \(b,c\in k[z]/(z^3)\). Multiplication is the path-algebra product: diagonal entries are reduced modulo \(z^4\), and each off-diagonal coefficient polynomial is reduced modulo \(z^3\). The matrix notation is a *truncated multiplication convention*, not an embedding in an ordinary full matrix ring over \(k[z]/(z^4)\).

Square-zero elements must have zero image in \(A/J\cong k\times k\), and hence have
\[
\begin{aligned}
a(z)&=a_1z+a_2z^2+a_3z^3,\quad d(z)=d_1z+d_2z^2+d_3z^3,\\
b(z)&=b_0+b_1z+b_2z^2,\quad c(z)=c_0+c_1z+c_2z^2.
\end{aligned}
\]
All twelve coefficients range independently over \(k\) before imposing the square-zero equations.

## Proof

**1. Exact equations.** Truncated multiplication yields the necessary and sufficient system
\[
\begin{aligned}
b_0c_0&=0,\\
b_0c_1+b_1c_0&=-a_1^2=-d_1^2,\\
b_0c_2+b_1c_1+b_2c_0&=-2a_1a_2=-2d_1d_2,\\
b_0(a_1+d_1)&=c_0(a_1+d_1)=0,\\
b_0(a_2+d_2)+b_1(a_1+d_1)&=0,\\
c_0(a_2+d_2)+c_1(a_1+d_1)&=0.
\end{aligned}
\]
The coordinates \(a_3,d_3\) are free. In particular, this is an actual equation-by-equation reduction rather than an inference from point counts.

**2. Four explicit component loci.** Define \(C_1\) by
\[
\begin{gathered}
d_1=-a_1,\quad d_2=-a_2,\quad c_0=0,\\
b_0c_1+a_1^2=0,\quad b_0c_2+b_1c_1+2a_1a_2=0.
\end{gathered}
\]
Define \(C_2\) by exchanging \(b_i\) and \(c_i\) in these equations. Define the two affine linear loci
\[
C_3=\{a_1=d_1=b_0=c_0=b_1=0\},\qquad
C_4=\{a_1=d_1=b_0=c_0=c_1=0\}.
\]
Every displayed \(C_i\) is a closed subvariety of \(X\). The last two are each affine \(7\)-space.

To see that they cover \(X\), first suppose \(a_1\ne0\). The equations imply \(d_1=\pm a_1\). The choice \(d_1=a_1\) forces \(b_0=c_0=0\), contradicting \(b_0c_1+b_1c_0=-a_1^2\). Hence \(d_1=-a_1\) and then \(d_2=-a_2\). Moreover exactly one of \(b_0,c_0\) is nonzero, placing the point in \(C_1\) or \(C_2\).

Suppose next \(a_1=0\); then \(d_1=0\). Set \(s=a_2+d_2\). If \(s\ne0\), the equations require \(b_0=c_0=0\) and \(b_1c_1=0\), placing the point in \(C_3\) or \(C_4\). If \(s=0\), the conditions reduce to \(bc=0\) in \(k[z]/(z^3)\). If \(b_0\ne0\), then \(c=0\) and the point belongs to \(C_1\); the symmetric case \(c_0\ne0\) belongs to \(C_2\). Finally, when \(b_0=c_0=0\), we have \(b_1c_1=0\) and lie in \(C_3\cup C_4\). This exhausts all points over every algebraically closed extension.

The open subset of \(C_1\) where \(b_0\ne0\) is isomorphic to \(\mathbb G_m\times\mathbb A^6\): \(b_0\) is nonzero, while \(a_1,a_2,a_3,d_3,b_1,b_2\) are free, and \(c_1,c_2\) are uniquely determined. Its dense subopen where also \(a_1\ne0\) is isomorphic to \((\mathbb G_m)^2\times\mathbb A^5\). To verify the entire \(C_1\) is irreducible, regard its five defining equations as elimination of \(d_1,d_2,c_0\), followed by two equations in an affine \(9\)-space. Its \(b_0=0\) complement has \(a_1=0\) and \(b_1c_1=0\), so its reduced dimension is at most \(6\). By the principal ideal theorem every component of the two-equation closed set in affine \(9\)-space has dimension at least \(7\), while the displayed dense open is irreducible of dimension \(7\). Hence \(C_1\) itself is irreducible of dimension \(7\). The same argument proves this for \(C_2\). The four components are distinct: \(C_1,C_2\) contain disjoint nonempty generic loci with \(a_1\ne0\), and \(C_3,C_4\) contain distinct generic loci with \(s\ne0\). None contains another. Thus the four are precisely the geometric components.

**3. Motivic count by disjoint strata.** Partition \(X\) into \(a_1\ne0\), \(a_1=0,s\ne0\), and \(a_1=s=0\). In the first stratum, one of \(b_0,c_0\) is a unit and the other has zero constant term; the equations uniquely determine two coefficients in the latter. Therefore its class is
\[2(\mathbb L-1)^2\mathbb L^5.\]
In the second stratum \(b_0=c_0=0\), and \(b_1c_1=0\), giving class
\[\mathbb L^5(\mathbb L-1)(2\mathbb L-1).\]
In the third, \(d_2=-a_2\), the \(a_2,a_3,d_3\) coefficients are free, and the remaining condition is \(bc=0\) in \(k[z]/(z^3)\). The zero-product pairs split by the valuation of \(b\), with motivic class
\[
(\mathbb L-1)\mathbb L^2+(\mathbb L-1)\mathbb L^2+(\mathbb L-1)\mathbb L^2+\mathbb L^3
=4\mathbb L^3-3\mathbb L^2.
\]
Thus the third stratum has class \(\mathbb L^5(4\mathbb L-3)\). Summation yields
\[
[X]=\mathbb L^5\bigl[2(\mathbb L-1)^2+(\mathbb L-1)(2\mathbb L-1)+(4\mathbb L-3)\bigr]=\mathbb L^6(4\mathbb L-3).
\]
All strata are defined over the base field, and all affine/torus decompositions are literal isomorphisms, so both the motivic identity and finite-field specialization hold over every field in the stated range.

**4. Modular dihedral realization.** In characteristic \(7\), write \(D_{14}=\langle r,s\mid r^7=s^2=1,\ srs=r^{-1}\rangle\). In \(k[\langle r\rangle]\), the element \(r+r^{-1}\) has constant augmentation \(2\), hence is invertible. Define
\[y=(r-r^{-1})(r+r^{-1})^{-1}.\]
Writing \(t=r-1\) gives \(k[\langle r\rangle]\cong k[t]/(t^7)\) and \(y=t+O(t^2)\), so \(y\) generates the truncated polynomial algebra and \(y^7=0\). Conjugation by \(s\) sends \(y\) to \(-y\). With \(e_\pm=(1\pm s)/2\), the two elements \(e_+ye_-\) and \(e_-ye_+\) are opposite arrows and products of length seven vanish. Their alternating paths, together with \(e_\pm\), give all fourteen basis elements. This constructs the claimed algebra isomorphism and transfers the square-zero classification.

## Verification

Run `python verify.py` under Python 3. The program derives squares by direct truncated polynomial multiplication, exhaustively checks the reduced ten-coordinate system over \(\mathbb F_3\) (the remaining two coordinates are free), independently checks the explicit four-component union on every enumerated point, and tests the dihedral change of generators over \(\mathbb F_7\). The output must end with `VERIFY_OK`. In \(\mathbb F_3\), the checked total is \(6561\), agreeing with \(3^6(4\cdot3-3)\). Finite checks are not used as proofs of the arbitrary-field claims.

## Relationship to prior work

Cyclic-quiver algebras and their module categories are standard: Wolf's work on the cyclic-quiver Hall algebra (arXiv:0709.4348) and Adachi's classification of \(\tau\)-tilting Nakayama modules (arXiv:1309.2216) provide context, but study representation categories rather than the internal square-zero-element locus. Huisgen-Zimmermann (arXiv:1410.3166) classifies components of **module representation varieties** for local truncated path algebras, also a different functor. Karagueuzian–Oliver–Ventura, DOI 10.1201/9781420028324.ch11, analyzes components of certain **upper-triangular matrix** square-zero rank subvarieties, not the truncated two-cycle multiplication locus. Jeyakumar, DOI 10.1112/jlms/s2-2.2.297 (1970), is an older source on modular dihedral group algebras; its full text was inaccessible during this comparison, and it remains a material literature risk. The exact four-component and motivic statements above were not identified in the inspected material; this is not a proof of absolute novelty.

## Limitations

This theorem is specific to Loewy length seven and a two-vertex cyclic quiver. It does not classify all truncation lengths, arbitrary quivers, or characteristic two. It concerns reduced loci, not the original equation scheme or its infinitesimal nilpotents. The modular dihedral application requires characteristic seven, not any odd characteristic. An inaccessible historical source may still contain overlapping special results, so literature originality remains subject to external review.

## References

1. S. Wolf, *The Hall algebra of a cyclic quiver at \(q=0\)*, arXiv:0709.4348 (initial public submission 2007-09-27).
2. T. Adachi, *The classification of tau-tilting modules over Nakayama algebras*, arXiv:1309.2216 (initial public submission 2013-09-09).
3. B. Huisgen-Zimmermann, *Irreducible components of varieties of representations I. The local case*, arXiv:1410.3166 (initial public submission 2014-10-12).
4. D. Karagueuzian, B. Oliver, J. Ventura, *The components of a variety of matrices with square zero and submaximal rank*, DOI:10.1201/9781420028324.ch11 (2005).
5. A. V. Jeyakumar, *Group algebras of dihedral and dicyclic groups over modular fields*, J. London Math. Soc. s2-2 (1970), 297–304, DOI:10.1112/jlms/s2-2.2.297.
