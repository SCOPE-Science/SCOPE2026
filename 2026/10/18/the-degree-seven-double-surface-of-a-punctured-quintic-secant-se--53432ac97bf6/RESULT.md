# The degree-seven double surface of a punctured quintic secant sextic

## Finding
Let \(k\) be an algebraically closed field of characteristic zero, and let
\[
C=\overline{\{[1:t:t^3:t^4:t^5]:t\in k\}}\subset\mathbb P^4_k.
\]
Its first secant variety \(X=\operatorname{Sec}(C)\) is an integral sextic hypersurface. In coordinates \([a:b:c:d:e]\), its homogeneous defining polynomial is
\[
\begin{aligned}
F={}&a^2ce^3-a^2d^2e^2+2abcde^2-2abd^3e-4ac^3de+4ac^2d^3\\
&-b^3e^3-b^2c^2e^2+5b^2cd^2e-b^2d^4+bc^4e-4bc^3d^2+c^6.
\end{aligned}
\]
Define three homogeneous cubics
\[
G_1=be^2+c^2e-2cd^2,\quad
G_2=ae^2+bde-2c^2d,\quad
G_3=d(ae+bd)-c(be+c^2).
\]
**The entire reduced singular locus** is the integral rational surface
\[
\operatorname{Sing}(X)_{\mathrm{red}}=D=V(G_1,G_2,G_3)_{\mathrm{red}},\qquad \deg D=7.
\]
It is the projective closure of the polynomial graph
\[
(a,b,c,d,e)=\big(cd(3c-2d^2),\ c(2d^2-c),\ c,\ d,\ 1\big).
\]
The complement \(D\setminus\{e\ne0\}\) consists of exactly two projective lines, \(V(e,c,b)\) and \(V(e,c,d)\), meeting in one point. At a general point of \(D\), the transverse singularity of \(X\) is an ordinary node with two branches. Thus \(X\) is nonnormal along a divisor.

## Assumptions and scope
Everything is over an algebraically closed field \(k\) of characteristic zero. The curve is the smooth rational monomial quintic obtained by omitting the quadratic coordinate from the complete degree-five rational normal embedding of \(\mathbb P^1\). A secant variety means the Zariski closure of the union of chords through distinct points. Singular loci and projective degrees are interpreted with reduced structure unless a scheme structure is explicitly mentioned. The degree and support assertions do not claim a computation of the nonreduced Jacobian scheme.

## Proof
**1. The sextic.** Introduce the missing coordinate \(y\) in the Hankel matrix
\[
H=\begin{pmatrix}a&b&y&c\\ b&y&c&d\\ y&c&d&e\end{pmatrix}.
\]
Every secant point of \(C\) has a lift for which \(\operatorname{rank}H\le2\), since the columns arise from sums of two geometric moment sequences. Let \(f_{012},f_{013},f_{023},f_{123}\) be the four \(3\times3\) maximal minors, indexed by their column triples. Direct expansion yields
\[
\operatorname{Res}_y(f_{013},f_{023})=(ad-bc)F.
\]
Consequently \(F\) vanishes on the secant variety (first on the dense subset \(ad\ne bc\), then everywhere). This secant image is irreducible of dimension three: the three-parameter affine secant map has Jacobian rank three, for example its projectively normalized coordinates \((b/a,c/a,d/a)\) have Jacobian determinant \(-1/16\) in parameters \((t,u,\mu)\) at \((0,1,1)\) with the other weight normalized to one. It remains to show that \(F\) is irreducible.

On \(e=1\), put
\[
z=b+c^2-2cd^2,\qquad w=a+bd-2c^2d,\qquad h=c-d^2.
\]
These are triangular polynomial coordinates \((c,d,z,w)\). Direct expansion gives the key identity
\[
F\big|_{e=1}=h\big(w^2+2cz^2\big)-z^3. \tag{1}
\]
As a polynomial in \(w\) over \(k(c,d,z)\), (1) is irreducible: a root would force \(z^2(z-2ch)/h\) to be a square, but it has a simple zero at the prime \(z-2ch\). The coefficients are relatively prime in \(k[c,d,z]\), so Gauss's lemma applies. Moreover \(F\) is not divisible by \(e\) (its \(c^6\) term survives when \(e=0\)); hence the homogeneous polynomial is irreducible. Since \(\operatorname{Sec}(C)\) is an irreducible threefold contained in the irreducible hypersurface \(V(F)\), they are equal.

**2. All singular points on \(e\ne0\).** Equation (1) has partials
\[
F_w=2hw,\qquad F_z=4chz-3z^2,\qquad
F_c=w^2+2(c+h)z^2,\qquad
F_d=-2d(w^2+2cz^2).
\]
If \(h=0\), (1) forces \(z=0\), and \(F_c=0\) then forces \(w=0\). If \(h\ne0\), the equation \(F_w=0\) forces \(w=0\). A nonzero \(z\) would simultaneously satisfy \(z=4ch/3\) from \(F_z=0\) and \(z=2ch\) from \(F=0\), a contradiction. Conversely \(z=w=0\) makes every first partial zero. Thus the affine singular locus is exactly \(z=w=0\), a smooth \(\mathbb A^2\) with parameters \((c,d)\), and its displayed graph follows by solving for \(a,b\).

**3. Boundary and global support.** At \(e=0\), the relevant partial derivatives include
\[
F_a=4c^2d^3,\quad F_b=-2d^2(bd^2+2c^3),\quad
F_c\big|_{d=e=0}=6c^5.
\]
Hence every singular point on \(e=0\) has \(c=0\); when \(d\ne0\), also \(b=0\). Substitution into all five partial derivatives confirms that the complete boundary singular set is
\[
L_1=V(e,c,b),\qquad L_2=V(e,c,d).
\]
For the global ideal description, \(G_1=G_2=0\) on \(e=1\) is exactly the graph \(z=w=0\); then \(G_3\) follows. On \(e=0\), the three cubics reduce to \(-2cd^2,-2c^2d,bd^2-c^3\), cutting out precisely \(L_1\cup L_2\) set-theoretically. Both lines belong to the closure of the affine graph: homogenize the graph as the quartic parametrization
\[
[c:d:e]\dashrightarrow
[cd(3ce-2d^2):ce(2d^2-ce):ce^3:de^3:e^4].
\]
Approaching \([1:0:0]\) along \(d=se\) gives \([3s:-1:0:0:0]\), sweeping a dense part of \(L_2\). Approaching \([0:1:0]\) along \(c=se^3\) gives \([-2s:0:0:1:0]\), sweeping a dense part of \(L_1\). Thus the complete reduced singular set is the irreducible projective closure \(D\).

**4. Its degree.** The two cubics \(G_1,G_2\) have no common divisor and cut out a complete-intersection surface of degree nine. On \(e\ne0\), its unique component is \(D\); on \(e=0\), its only additional two-dimensional components are the distinct coordinate planes \(\{e=c=0\}\) and \(\{e=d=0\}\). Both occur with generic multiplicity one: for the first, the Jacobian of \((G_1,G_2)\) in \((c,e)\) has nonzero determinant at a generic point with \(bd\ne0\); for the second, the Jacobian in \((e,d)\) has nonzero determinant when \(c\ne0\). The graph component is generically reduced because \(G_1,G_2\) solve uniquely for \(b,a\) on \(e\ne0\). Degree additivity of the complete-intersection cycle gives \(9=\deg D+1+1\), hence \(\deg D=7\).

**5. Transverse singularities.** At a generic point of \(D\), both \(c\) and \(h=c-d^2\) are units. In the transverse coordinates \((z,w)\), the quadratic term of (1) is \(h(w^2+2cz^2)\), a nondegenerate binary quadratic form. The formal Morse lemma gives the ordinary nodal transverse germ \(uv=0\). Since \(D\) is a divisor in the integral hypersurface \(X\), the hypersurface fails Serre's condition \(R_1\) and is nonnormal.

## Verification
A standalone `verify.py` uses exact symbolic arithmetic to reconstruct the resultant factor, 13-term sextic, triangular normal form, boundary gradient identities, graph equations, and an exact generic hyperplane slice of the singular surface with seven simple intersection points. It also substitutes the independent two-point moment parametrization into \(F\), checks the generic transverse Hessian, and exhaustively compares the reduced singular equations with the gradient over \(\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), examining all projective points. The executable prints `VERIFY_OK`. Those finite-field checks are corroboration, not a characteristic-zero proof.

## Relationship to prior work
Ranestad's 2004 preprint (published in 2006) supplies general degree formulas for monomial-curve secants. Cueto and Lin construct tropical secant graphs and multidegree/Newton-polytope algorithms, treating hypersurfaces in their Section 6. Vermeire gives normality and smoothness criteria for sufficiently ample embeddings; those hypotheses do not cover this punctured linear system. The degree-six secant hypersurface itself is not the originality claim. The increment is the **complete reduced singular support of this specific projected quintic secant**, its irreducibility and degree seven, boundary-line description, and generic two-branch transverse germ. General degree, normalization criteria, or tropical implicitization alone do not imply those exact geometric conclusions.

## Limitations
The theorem is characteristic-zero only. It describes reduced singular support, not the nonreduced Jacobian ideal or full conductor scheme. It does not classify nongeneric analytic germs along the two degeneration curves inside \(D\), nor singularities at their boundary-line intersection. The possibility of an equivalent implicit calculation in earlier elimination literature remains a literature-coverage risk; no claim of uniqueness of discovery is made.

## References
- K. Ranestad, *The Degree of the Secant Variety and the Join of Monomial Curves*, preprint dated 2004-05-27, https://library.slmath.org/preprints/files/2004/2004-007/2004-007.pdf (later Collectanea Mathematica 57 (2006)).
- M. A. Cueto and S. Lin, *Tropical Secant Graphs of Monomial Curves*, arXiv:1005.3364, first posted 2010-05-19, especially Sections 1 and 6, https://arxiv.org/abs/1005.3364.
- P. Vermeire, *Singularities of the Secant Variety*, arXiv:0712.2364, first posted 2007-12-14, Theorem 2.2, https://arxiv.org/html/0712.2364v1.
