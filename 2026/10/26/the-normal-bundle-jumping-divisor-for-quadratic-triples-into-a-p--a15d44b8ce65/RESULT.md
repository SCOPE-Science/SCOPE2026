# The normal-bundle jumping divisor for quadratic triples into a product of projective lines

## Finding
Let \(k\) be an algebraically closed field of arbitrary characteristic. Let \(U\) be the open parameter space of unramified morphisms
\[
f=(f_1,f_2,f_3):\mathbb P^1_k\longrightarrow(\mathbb P^1_k)^3,
\qquad\deg(f_i)=2\quad(i=1,2,3),
\]
with fixed source. Let \(N_f\) be the locally free cokernel of the differential. Then exactly the following behavior occurs.

* If \(\operatorname{char}k\ne2\), the balanced locus is a nonempty open subset of \(U\), where \(N_f\simeq\mathcal O_{\mathbb P^1}(5)^{\oplus2}\). Its complement is a **nonempty smooth irreducible divisor** \(D\), on which \(N_f\simeq\mathcal O_{\mathbb P^1}(4)\oplus\mathcal O_{\mathbb P^1}(6)\). In the natural parameterization \(U\subset(\mathbb P^5)^3\), \(D\) is cut out by a multihomogeneous determinant of multidegree \((2,2,2)\), expressing collinearity of the three binary-quadratic ramification sections in \(\mathbb P H^0(\mathbb P^1,\mathcal O(2))\cong\mathbb P^2\).
* If \(\operatorname{char}k=2\), every \(f\in U\) satisfies \(N_f\simeq\mathcal O_{\mathbb P^1}(4)\oplus\mathcal O_{\mathbb P^1}(6)\). In particular the balanced locus is empty, although \(U\) is nonempty.

Thus this smallest all-quadratic multidegree on the toric threefold \((\mathbb P^1)^3\) has a complete two-stratum normal-bundle classification in characteristic different from two, whereas characteristic two forces the jumping splitting throughout the unramified family.

## Assumptions and scope
Throughout, the source is a fixed copy of \(\mathbb P^1_k\); no quotient by source reparametrization is taken. The three target components have **exact** degree two, so each is given by a coprime pair of binary quadratics. The term **unramified** means that the differential into the threefold has rank one at every geometric source point; it does not assert that the image map is an embedding.

Write \([s:t]\) for source coordinates and let
\[
f_i([s:t])=[A_i(s,t):B_i(s,t)],\quad
A_i=a_i s^2+b_i st+c_i t^2,\quad B_i=d_i s^2+e_i st+h_i t^2.
\]
The equation \(\operatorname{Res}(A_i,B_i)\ne0\) ensures that \(f_i\) is a degree-two morphism. Put
\[
R_i=(a_ie_i-b_id_i)s^2+2(a_ih_i-c_id_i)st+(b_ih_i-c_ie_i)t^2
\in H^0(\mathbb P^1,\mathcal O(2)).
\]
The entries of the \(3\times3\) coefficient matrix \(W\) of \((R_1,R_2,R_3)\) are the coefficients of \(s^2,st,t^2\), in that order. Its determinant \(\Delta=\det W\) is the claimed multihomogeneous equation. Vanishing of \(\Delta\) is independent of the scalar representatives of the three quadratic pairs.

## Proof
**1. The exact normal sequence.** On the affine chart \(t\ne0\), setting \(z=s/t\), direct differentiation of \(A_i(z,1)/B_i(z,1)\) gives numerator
\[
(a_ie_i-b_id_i)z^2+2(a_ih_i-c_id_i)z+(b_ih_i-c_ie_i).
\]
Since \(T_{\mathbb P^1}\simeq\mathcal O(2)\) and \(f_i^*T_{\mathbb P^1}\simeq\mathcal O(4)\), these homogeneous sections are precisely the three components of \(df\), after the canonical local identifications. Thus \(f\in U\) if and only if the \(R_i\) have no common geometric zero. For such \(f\),
\[
0\longrightarrow\mathcal O(2)
\xrightarrow{(R_1,R_2,R_3)}\mathcal O(4)^{\oplus3}
\longrightarrow N_f\longrightarrow0.
\tag{1}
\]
The bundle \(N_f\) has rank two and degree ten. As \(N_f(-4)\) is a quotient of \(\mathcal O^{\oplus3}\), it is globally generated. Birkhoff–Grothendieck then restricts its splitting type to
\[
\mathcal O(5)\oplus\mathcal O(5)
\quad\hbox{or}\quad
\mathcal O(4)\oplus\mathcal O(6).
\tag{2}
\]
Let \(r=\dim_k\langle R_1,R_2,R_3\rangle\). If \(r\le1\), the sections have a common zero, because every nonzero section of \(\mathcal O(2)\) has one over an algebraically closed field. Hence \(r\in\{2,3\}\) on \(U\).

Twist (1) by \(\mathcal O(-6)\). The resulting cohomology exact sequence identifies \(H^0(N_f(-6))\) with the kernel of
\[
H^1(\mathcal O(-4))\longrightarrow H^1(\mathcal O(-2))^{\oplus3}.
\]
By Serre duality its transpose is \(k^3\to H^0(\mathcal O(2))\), sending the \(i\)-th coordinate vector to \(R_i\). Consequently,
\[
h^0(N_f(-6))=3-r.
\tag{3}
\]
The two possibilities in (2) give respectively zero and one global section after twisting by \(-6\). Thus \(r=3\) gives \((5,5)\), while \(r=2\) gives \((4,6)\), with no omitted splitting types.

**2. Characteristic two.** If \(2=0\) in \(k\), the mixed coefficient of every \(R_i\) vanishes, so \(R_i\in\langle s^2,t^2\rangle\). Hence \(r\le2\) for every triple, and unramifiedness forces \(r=2\). Equation (3) proves the asserted constant unbalanced splitting. Nonemptiness is witnessed by
\[
[f_1,f_2,f_3]
=\bigl([s^2:t^2],\,[s^2+st:t^2],\,[st+t^2:s^2]\bigr),
\]
whose derivative sections are \((0,t^2,s^2)\). They have no common zero; the first component is allowed to be inseparable.

**3. The divisor in odd or zero characteristic.** When \(2\) is invertible, the degree-two maps themselves form the open subset \(M_2\subset\mathbb P^5\) of coprime ordered quadratic pairs, modulo simultaneous scalar. Send a pair to the two-plane it spans in \(H^0(\mathbb P^1,\mathcal O(2))\). This gives a smooth \(\operatorname{PGL}_2\)-torsor
\[
M_2\longrightarrow G\subset\operatorname{Gr}(2,3)\simeq\mathbb P^2,
\]
where \(G\) is the open locus of basepoint-free quadratic pencils. In Plücker coordinates \((a e-b d,\,a h-c d,\,b h-c e)\), the projective ramification quadratic is obtained by the linear change \((u,v,w)\mapsto(u,2v,w)\). This is a projective automorphism precisely when \(2\) is invertible. Thus the map from \(M_2\) to its projective ramification quadratic is itself a smooth torsor over a nonempty open subset of \(\mathbb P^2\).

The ordered triples of collinear points in \((\mathbb P^2)^3\) form an irreducible determinantal hypersurface: it is dominated by the incidence family of one projective line and three marked points on it. Its singular locus lies among triples of coefficient-matrix rank at most one; at rank two the determinant has nonzero differential. Taking the inverse image under the three smooth torsors preserves smoothness at rank two and irreducibility. Intersecting with the open unramified locus removes every rank-one triple, so \(D=\{\Delta=0\}\cap U\) is smooth and, provided it is nonempty, irreducible. Each row of \(W\) is quadratic in the coefficients of its corresponding pair, hence \(\Delta\) has multidegree \((2,2,2)\).

Finally, both strata are nonempty. For \(\operatorname{char}k\ne2\), take
\[
F_{\mathrm{bal}}=
\bigl([s^2:t^2],\,[s^2+t^2:st],\,[s^2-t^2:st]\bigr).
\]
Its derivative sections are \((2st,s^2-t^2,s^2+t^2)\), a basis of \(H^0(\mathcal O(2))\). For the jumping example take
\[
F_{\mathrm{jump}}=
\bigl([s^2:t^2],\,[s^2:t^2],\,[s^2+t^2:st]\bigr),
\]
with rank-two sections \((2st,2st,s^2-t^2)\) having no common zero. Both triples are honest degree-two maps. This completes the proof.

## Verification
The accompanying standalone `verify.py` checks the universal Wronskian expansion symbolically, the independent and dependent rank-three/rank-two examples in characteristics zero, three, five and seven, and the characteristic-two witness. It also exhausts the \(24\) degree-two maps over \(\mathbb F_2\), checking all \(24^3=13824\) ordered triples: exactly \(9072\) have unramified derivative, each of rank two. This finite enumeration corroborates the universal proof; it does **not** prove the classification over all algebraically closed fields.

Run with Python 3 and SymPy: `python verify.py`.

## Relationship to prior work
Iwasaki, *Normal Bundle Splitting Strata of Rational Curves in Toric Varieties*, arXiv:2609.39309v1 (2026), develops relative cohomology morphisms and determinantal techniques for unramified rational curves in arbitrary smooth projective toric varieties. Its explicit applications focus on blowups of projective space along linear subspaces, not this complete degree-\((2,2,2)\) product classification or its characteristic-two collapse. The present proof specializes the normal sequence to a product of three projective lines and additionally exploits the Plücker linearity of quadratic ramification and the failure of that linear map to be invertible in characteristic two.

Coskun–Smith, *Very free rational curves in Fano varieties*, arXiv:2106.01991 (2021), study normal bundles in products via deformations under factorwise immersion hypotheses. Those hypotheses do not apply to degree-two maps \(\mathbb P^1\to\mathbb P^1\), which necessarily ramify in characteristic different from two; moreover that result does not classify the exact fixed-source jumping locus here. Established Birkhoff–Grothendieck splitting, Serre duality and the normal exact sequence are used without originality claims.

## Limitations
The theorem concerns unramified morphisms with fixed source, not every image curve or its Hilbert-scheme structure, and does not identify the scheme-theoretic closure of \(D\) across the ramification or resultant boundary. In characteristic two it asserts no reduced divisor of jumping points: the balanced splitting disappears entirely. The algebraic novelty comparison is best knowledge from the cited published works and targeted searches, not proof that no unindexed earlier treatment exists. No independent validation has been carried out.

## References
1. H. Iwasaki, *Normal Bundle Splitting Strata of Rational Curves in Toric Varieties*, arXiv:2609.39309v1, initially public 2026-09-30, especially Sections 1, 3, 5 and 6.
2. I. Coskun and G. Smith, *Very free rational curves in Fano varieties*, arXiv:2106.01991, 2021, introduction and product theorem.
3. I. Coskun, E. Larson and I. Vogt, *Normal bundles of rational curves in Grassmannians*, arXiv:2404.08102, 2024, for contextual contrast with Grassmannian targets.
4. Standard results: Grothendieck's splitting theorem on \(\mathbb P^1\), Serre duality on \(\mathbb P^1\), and the Euler sequence for \(T_{\mathbb P^1}\).
