# The fourfold of lines on two quadrics in \(\mathbf P^6\) is not weakly \(2\)-Fano
## Finding
Let
\[
X\subset\mathbf P^6_{\mathbf C}
\]
be a smooth complete intersection of two quadrics, and let
\[
F=F_1(X)
\]
be its Fano scheme of lines. Write \(\mathcal S\) for the universal rank-\(2\) subbundle on
\[
G=\operatorname{Gr}(2,7),
\]
and put
\[
H=c_1(\mathcal S^\vee)|_F.
\]
Then
\[
-K_F=H,
\]
so \(F\) is Fano. Its second Chern character is
\[
\operatorname{ch}_2(T_F)
=
-\frac52(\sigma_2-\sigma_{1,1})|_F.
\]
For the natural effective surface class
\[
S=H^2\cap[F],
\]
obtained by intersecting \(F\) with two general Plücker hyperplanes,
\[
\operatorname{ch}_2(T_F)\cdot S=-40.
\]
Consequently \(F\) is not weakly \(2\)-Fano, and hence is not \(2\)-Fano.

For scale, the same computation gives
\[
H^4=80,
\]
so the normalized value on this Plücker complete-intersection surface is
\[
\frac{\operatorname{ch}_2(T_F)\cdot H^2}{H^4}=-\frac12.
\]

## Assumptions and scope
The base field is \(\mathbf C\). The fourfold \(F\) is the scheme of projective lines contained in \(X\).

The recent work of Ji--Suzuki treats smooth intersections of two quadrics and their Fano schemes of linear spaces. In the present case their source confirms that \(F\) is smooth and projective; their \(g=3\) formula gives
\[
[F]=\mathbb L^4+8\mathbb L^3+30\mathbb L^2+8\mathbb L+1
\]
in the Grothendieck ring.

Weakly \(2\)-Fano means that \(F\) is Fano and
\[
\operatorname{ch}_2(T_F)\cdot\alpha\ge0
\]
for every nonzero effective surface class \(\alpha\). Thus a single effective surface with negative pairing disproves the property.

## Proof
Each defining quadric of \(X\) restricts to a quadratic form on the line represented by a point of \(G\). Therefore \(F\) is the zero locus of a regular section of
\[
E=\bigl(\operatorname{Sym}^2\mathcal S^\vee\bigr)^{\oplus2}
\]
on \(G\). Since \(\dim G=10\) and \(\operatorname{rk}E=6\), the zero locus has dimension \(4\), as expected.

Let \(x,y\) be the Chern roots of \(\mathcal S^\vee\), and put
\[
H=x+y.
\]
In \(K\)-theory,
\[
[T_G]=[\mathcal S^\vee\otimes\mathcal Q]
=7[\mathcal S^\vee]-[\mathcal S^\vee\otimes\mathcal S].
\]
Hence
\[
c_1(T_G)=7H.
\]
The Chern roots of \(\operatorname{Sym}^2\mathcal S^\vee\) are
\[
2x,\quad x+y,\quad 2y,
\]
so one copy has first Chern class \(3H\), and
\[
c_1(E)=6H.
\]
Adjunction gives
\[
c_1(T_F)=H,
\]
equivalently
\[
-K_F=H.
\]
Since the Plücker class is ample, \(F\) is Fano.

For the second Chern character,
\[
\operatorname{ch}_2(T_G)
=
\frac72(x^2+y^2)-(x-y)^2
=
\frac52(x^2+y^2)+2xy.
\]
For one symmetric-square summand,
\[
\operatorname{ch}_2(\operatorname{Sym}^2\mathcal S^\vee)
=
\frac12\bigl((2x)^2+(x+y)^2+(2y)^2\bigr)
=
\frac52(x^2+y^2)+xy.
\]
Thus
\[
\operatorname{ch}_2(E)
=
5(x^2+y^2)+2xy.
\]
The tangent-normal exact sequence
\[
0\longrightarrow T_F
\longrightarrow T_G|_F
\longrightarrow E|_F
\longrightarrow0
\]
therefore yields
\[
\operatorname{ch}_2(T_F)
=
-\frac52(x^2+y^2).
\]
Using
\[
x^2+y^2=\sigma_2-\sigma_{1,1},
\]
this is the claimed Schubert-class formula.

The top Chern class of one symmetric-square summand is
\[
c_3(\operatorname{Sym}^2\mathcal S^\vee)
=
(2x)(x+y)(2y)=4xyH,
\]
hence the class of \(F\) in \(G\) is
\[
[F]=c_6(E)=16x^2y^2H^2.
\]

For a symmetric polynomial \(f(x,y)\) of total degree \(10\), integration on \(G=\operatorname{Gr}(2,7)\) is
\[
\int_G f
=
[x^6y^5]\,(x-y)f.
\]
Applying this to the surface intersection gives
\[
\begin{aligned}
\operatorname{ch}_2(T_F)\cdot H^2
&=
\int_G
\left(-\frac52(x^2+y^2)\right)
H^2\cdot16x^2y^2H^2\\
&=-40.
\end{aligned}
\]
The same coefficient extraction gives
\[
H^4
=
\int_G H^4\cdot16x^2y^2H^2
=
80.
\]
In particular \(H^2\cap[F]\) is a nonzero effective surface class. Since \(\operatorname{ch}_2(T_F)\) is negative on that class, \(F\) cannot be weakly \(2\)-Fano.

## Verification
The source geometry was checked in the full text of Ji--Suzuki. They state that the Fano schemes of linear spaces on a smooth intersection of two quadrics are smooth projective varieties, and their \(g=3\) computation gives the explicit motivic class of this fourfold.

The weak-\(2\)-Fano criterion was checked against Araujo--Castravet: weakly \(2\)-Fano requires nonnegative \(\operatorname{ch}_2\) on every nonzero effective surface class.

The zero-locus description and Schubert-calculus coefficient method were checked against the full text of Ciliberto--Zaidenberg, which develops the symmetric-power tautological bundle construction and the Vandermonde coefficient extraction on Grassmannians.

The arithmetic in the displayed intersection calculation was independently replayed by `verify_ch2.py`; it returns
\[
\operatorname{ch}_2(T_F)\cdot H^2=-40
\qquad\text{and}\qquad
H^4=80.
\]
The script is only an arithmetic check: the proof itself is the symbolic Chern-root calculation above.

## Relationship to prior work
Ji--Suzuki compute motivic classes and consequences for cohomology of Fano schemes of lines on intersections of two quadrics. Their paper contains no statement about \(2\)-Fano or weakly \(2\)-Fano positivity and no second-Chern-character calculation.

Araujo--Castravet classify \(2\)-Fano manifolds under a high-index hypothesis. Their main classification range does not cover this fourfold, whose anticanonical class is the single Plücker class.

Ciliberto--Zaidenberg provide general enumerative and Chern-class machinery for Fano schemes of complete intersections, including the Grassmannian coefficient method used here, but they do not state the weak-\(2\)-Fano status or the negative value above for this fourfold.

Searches using the exact variety, the aliases “Fano scheme of lines on two quadrics” and “intersection of two quadrics in \(\mathbf P^6\),” the property “weakly \(2\)-Fano,” and the numerical witness \(-40\) found no published statement implying this conclusion.

## Limitations
The finding concerns the fourfold \(F_1(X)\) for a smooth intersection of two quadrics in \(\mathbf P^6\). It does not classify \(2\)-Fano behavior for all Fano schemes \(F_r(X)\) in other dimensions.

The calculation supplies one explicit negative effective surface class. It does not determine the full cone of effective surfaces, nor the complete numerical behavior of \(\operatorname{ch}_2(T_F)\) on that cone.

## References
L. Ji and F. Suzuki, “Motivic classes of Fano schemes of lines on intersections of two quadrics,” arXiv:2609.36233v1, first public 2026-09-28; especially the introduction and the \(g=3\) case of the proof of Theorem 1.2.

C. Araujo and A.-M. Castravet, “Classification of \(2\)-Fano manifolds with high index,” arXiv:1206.1357v1; especially the definition of weakly \(2\)-Fano manifolds.

C. Ciliberto and M. Zaidenberg, “On Fano schemes of complete intersections,” arXiv:1903.11294v2; especially Sections 1--3 on tautological symmetric powers, Schubert calculus, and numerical invariants.
