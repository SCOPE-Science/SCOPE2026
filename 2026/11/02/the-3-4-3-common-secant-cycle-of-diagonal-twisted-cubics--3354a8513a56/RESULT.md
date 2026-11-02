# The \(3+4+3\) common-secant cycle of diagonal twisted cubics

## Finding
Let \(C\subset\mathbb P^3_{\mathbb C}\) be the standard twisted cubic parametrized by
\[
[s:t]\longmapsto[s^3:s^2t:st^2:t^3].
\]
For \(a,b,c\in\mathbb C\), write \(D=\operatorname{diag}(1,a,b,c)\), and let \(C_D=D(C)\). Assume
\[
abc(a^2-b)(b^2-ac)(ab-c)\ne0.
\]
For a twisted cubic \(Y\), let \(\Sigma(Y)\subset\operatorname{Gr}(1,\mathbb P^3)\) denote its **closed** secant congruence, which includes tangent lines as limits of proper secants. Form the scheme-theoretic intersection
\[
Z_D=\Sigma(C)\times_{\operatorname{Gr}(1,\mathbb P^3)}\Sigma(C_D).
\]
**Theorem.** The finite scheme \(Z_D\) is supported at precisely three lines:
\[
\ell_0=\mathbb P\langle e_0,e_1\rangle,\quad
\ell_{0\infty}=\mathbb P\langle e_0,e_3\rangle,\quad
\ell_\infty=\mathbb P\langle e_2,e_3\rangle.
\]
Its respective completed local rings (equal to the Artinian local rings) are
\[
\mathbb C[[z]]/(z^3),\qquad
\mathbb C[[u,v]]/(u^2,v^2),\qquad
\mathbb C[[z]]/(z^3).
\]
Consequently its zero-cycle and total scheme length are
\[
[Z_D]=3[\ell_0]+4[\ell_{0\infty}]+3[\ell_\infty],
\qquad \operatorname{length}(Z_D)=10.
\]
Only \(\ell_{0\infty}\) is a proper secant of both curves: the two other support lines are their common tangent lines at the shared endpoints. Thus the theorem is about the **compactified secant intersection scheme**, not a claim of ten distinct proper secants for the diagonal pair.

## Assumptions and scope
Everything is scheme-theoretic over \(\mathbb C\). The three nonvanishing relations select a nonempty Zariski-open subset of the three-dimensional diagonal torus, modulo the chosen normalization of its first entry. The statement is uniform throughout that open subset. The Grassmannian has dimension four; each closed secant congruence is a smooth embedded \(\mathbb P^2\). The distinguished basis vectors \(e_0,\ldots,e_3\) refer to the homogeneous coordinates used in the parametrization. All multiplicities are lengths of local intersection rings in the Grassmannian, not intersection multiplicities of the two curves in \(\mathbb P^3\).

## Proof
**1. Embedded secant surfaces.** A pair of parameters of \(\mathbb P^1\), including a repeated pair, corresponds to a binary quadratic up to scale with coefficients \([A:B:C]\). The associated secant/tangent line is the common kernel of the two independent linear forms
\[
A x_2-Bx_1+Cx_0,\qquad A x_3-Bx_2+Cx_1.
\]
The dual Plücker coordinates of its annihilator two-plane, in order \((01,02,03,12,13,23)\), are
\[
P(A,B,C)=(C^2,-BC,AC,B^2-AC,-AB,A^2).
\]
These six quadratics form a basis of the degree-two forms in \(A,B,C\), proving that \(\Sigma(C)\) is a Veronese \(\mathbb P^2\) embedded in the Grassmannian. In particular the parameter is unique and the closed secant surface is smooth. The diagonal transform acts on covectors by the inverse diagonal; hence the corresponding six coordinates for \(\Sigma(C_D)\) are
\[
Q(U,V,W)=\left(\frac{W^2}{a},-\frac{VW}{b},\frac{UW}{c},
\frac{V^2-UW}{ab},-\frac{UV}{ac},\frac{U^2}{bc}\right).
\]
An intersection point is an equality \(P(A,B,C)=TQ(U,V,W)\) in projective Plücker space for some \(T\ne0\). This equation also defines the scheme-theoretic fiber product, because the two parametrizations are closed immersions.

**2. The first tangent point and the entire chart \(A\ne0\).** Since \(P_{23}=A^2\) and \(Q_{23}=U^2/(bc)\), when \(A\ne0\) also \(U\ne0\). Scale to \(A=U=1\). The last, fifth, and third coordinate equations successively give
\[
T=bc,\qquad V=\frac ab B,\qquad W=\frac1b C.
\]
Put \(\delta=1-ac/b^2\) and \(\varepsilon=c/(ab)-1\). The remaining equations reduce exactly to
\[
\delta BC=0,\qquad \delta B^2+\varepsilon C=0,
\qquad\varepsilon C^2=0.
\]
Both constants are nonzero under the hypotheses. Eliminating \(C=-(\delta/\varepsilon)B^2\), the ideal becomes \((B^3)\): the last equation contributes only a multiple of \(B^4\). Thus this whole affine chart contains exactly one intersection point \([A:B:C]=[1:0:0]\), with local ring \(\mathbb C[B]/(B^3)\). Its line is \(\ell_0\).

**3. The line joining the two shared endpoints.** If \(A=0\), then the sixth Plücker coordinate forces \(U=0\). If also \(B\ne0\), the fourth coordinate forces \(V\ne0\); normalize \(B=V=1\). The second coordinate gives \(W=C/a\), while the first gives
\[
(1-b/a^2)C^2=0.
\]
Since \(a^2\ne b\), there is just the point \([A:B:C]=[0:1:0]\) on this stratum. It is \(\ell_{0\infty}\). If instead \(A=B=0\), necessarily \([A:B:C]=[0:0:1]\), namely \(\ell_\infty\). Thus these three are the **entire** geometric support.

To obtain the full local ring at \(\ell_{0\infty}\), use \(B=V=1\) and the invertible Plücker scale \(T\), which equals \(ab\) at the point. The second and fifth coordinate equations give
\[
W=\frac{bC}{T},\qquad U=\frac{acA}{T}.
\]
The first and last equations become
\[
(aT-b^2)C^2=0,\qquad (bT-a^2c)A^2=0.
\]
Their leading coefficients at the point are \(b(a^2-b)\ne0\) and \(a(b^2-ac)\ne0\). They therefore force \(A^2=C^2=0\) in the completed local ring. The fourth equation is
\[
T^2-ab(1-AC)T-abc\,AC=0.
\]
Its derivative with respect to \(T\) at \((A,C,T)=(0,0,ab)\) is \(ab\ne0\); hence it determines \(T\) uniquely as a formal function, reducing modulo \((A^2,C^2)\) to
\[
T=ab+(c-ab)AC.
\]
The displayed formulas reduce to \(U=(c/b)A\) and \(W=C/a\) in this quotient. Direct substitution into the remaining third-coordinate equality \(AC=T UW/c\) gives an identity because \((AC)^2=0\). Conversely every element of \(\mathbb C[[A,C]]/(A^2,C^2)\) so parametrizes a solution. Thus the completed local ring is **exactly** \(\mathbb C[[A,C]]/(A^2,C^2)\), of length four, rather than merely a ring of length at most four.

**4. The tangent at infinity.** Reverse the four ambient coordinates and exchange \(A\) with \(C\). After rescaling the first diagonal entry to one, the reversed diagonal becomes \(\operatorname{diag}(1,b/c,a/c,1/c)\). Step 2 then applies with constants
\[
\delta_\infty=1-b/a^2,\qquad
\varepsilon_\infty=c/(ab)-1.
\]
Both are nonzero. On the chart \(C=1\), the local equations reduce to
\[
\delta_\infty B^2+\varepsilon_\infty A=0,
\qquad B^3=0.
\]
The last point is \(\ell_\infty\), with local ring \(\mathbb C[B]/(B^3)\).

**5. Completion of the proof.** Steps 2–4 cover all geometric points and compute their full local schemes. As a finite \(\mathbb C\)-scheme, \(Z_D\) is a disjoint union of its three local Artin schemes. Their respective vector-space lengths are three, four, and three. Since both secant congruences are two-dimensional in the smooth four-dimensional Grassmannian and their intersection is finite, their scheme intersection represents the proper intersection product. The familiar general count of ten common secants is thereby recovered as the sum of these three contributions. \(\square\)

## Verification
The included standalone `verify.py` rebuilds the two dual Plücker parametrizations and performs exact rational Gröbner-basis elimination for three independent generic diagonal triples, in the tangent-at-zero, middle, and tangent-at-infinity charts. It checks that the respective quotient bases have lengths \(3,4,3\), that the three local ideals are as stated for the first triple, and that the Plücker vectors satisfy the Grassmannian quadratic equation. Run `python3 verify.py` using Python 3 with SymPy installed. Finite examples are checks of the algebraic calculations; the theorem for **every** admissible \((a,b,c)\) is established by the symbolic argument above.

## Relationship to prior work
Aslam, Faust, Hauenstein, Lopez Garcia, Kagy, Regan, Wampler, and Zhang (arXiv:2603.25003, first posted 2026-03-26) recall that two **general** twisted cubics have ten common secants and study monodromy and real distributions of those transverse solutions. Their parameter matrices are general; their ten-line enumeration does not describe nonreduced intersections for diagonal pairs sharing two points. In particular the two tangent support lines in the present theorem are excluded by their definition of a proper secant. The theorem here gives an exact special-fiber intersection **cycle** with support and local algebra, not a new generic ten-line count.

Ponce, Sturmfels, and Trager (arXiv:1608.05924, Sections 2 and 4) describe secant congruences, identify the twisted-cubic secant congruence with a Veronese surface, and exhibit its Plücker equations. Their presentation supplies context for Step 1, but the checked material does not compare two diagonal translates or compute the \(3+4+3\) special-fiber local rings. Classical Schubert calculus determines the total intersection number ten, not this distribution of lengths among three nonreduced points.

## Limitations
The theorem is restricted to diagonal projective transformations satisfying the three explicit nonvanishing relations. It does not classify their boundary parameter loci, arbitrary pairs of twisted cubics, or the real distribution of ten distinct generic secants. Only one of the three support lines is a proper common secant for the diagonal pair. Literature priority beyond the inspected primary sources is not independently certified; implicit coverage in classical enumerative geometry or toric intersection theory remains a possibility.

## References
1. S. Aslam, M. Faust, J. D. Hauenstein, J. Lopez Garcia, B. Kagy, M. H. Regan, C. W. Wampler, and A. Zhang, *Common Real Secants to Pairs of Real Twisted Cubic Curves*, arXiv:2603.25003v1 (2026-03-26), https://arxiv.org/abs/2603.25003.
2. J. Ponce, B. Sturmfels, and M. Trager, *Congruences and Concurrent Lines in Multi-View Geometry*, arXiv:1608.05924 (2016), https://arxiv.org/abs/1608.05924.
3. D. Eisenbud and J. Harris, *3264 and All That: A Second Course in Algebraic Geometry*, Cambridge University Press (2016), Schubert-calculus count of common secants (background; cited in Reference 1).
