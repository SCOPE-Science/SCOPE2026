# Arithmetic splitting of the seven bitangents and fourteen contact flags of the Klein quartic in characteristic two

## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_2}\) be the smooth quartic
\[
C:\quad x^3y+y^3z+z^3x=0.
\]
All geometric bitangents, in the sense that their intersection divisor is \(2P+2Q\) for distinct geometric points \(P,Q\), are
\[
L_t:\quad z+t^3x+ty=0,\qquad t^7=1.
\]
The seven solutions are the nonzero elements of \(\mathbb F_8\). Each bitangent has the following two contact points, with \(w^2+w+1=0\):
\[
P_{t,w}=[t^5w:1:tw^2].
\]
The finite étale bitangent scheme has Frobenius cycle lengths \((1,3,3)\), and the finite étale scheme of bitangent--contact-point flags has Frobenius cycle lengths \((2,6,6)\). In particular, writing \(q=2^m\), their rational-point numbers are
\[
\#\operatorname{Bit}(C)(\mathbb F_q)=\begin{cases}1&3\nmid m,\\7&3\mid m,\end{cases}
\qquad
\#\operatorname{Flag}(C)(\mathbb F_q)=\begin{cases}0&2\nmid m,\\2&2\mid m,\ 6\nmid m,\\14&6\mid m.\end{cases}
\]
Their zeta functions, with zeta variable \(T\), are
\[
Z(\operatorname{Bit}(C)/\mathbb F_2,T)=\frac1{(1-T)(1-T^3)^2},\qquad
Z(\operatorname{Flag}(C)/\mathbb F_2,T)=\frac1{(1-T^2)(1-T^6)^2}.
\]
As an additional explicit arithmetic realization of the classical Fano arrangement, its seven triple vertices are indexed by unordered triples \(\{a,b,a+b\}\subset\mathbb F_8^\times\) and equal
\[
V_{a,b}=[1:a^2+ab+b^2:ab(a+b)].
\]
These seven points are all off the quartic.

## Assumptions and scope
The ground field and all extension fields have characteristic two. Algebraic closures are used only to define geometric lines and tangent contacts. The displayed equation specifies the arithmetic model; its Frobenius action must not be transferred from another isomorphic geometric twist without checking descent. A bitangent is required to have two **distinct** double contacts; there are no hyperflex-only exceptions in this classification. The flag scheme is the incidence scheme of a bitangent together with one of its two geometric tangency points. No assertion about different integral models or other characteristics is made.

## Proof
**Smoothness.** For \(f=x^3y+y^3z+z^3x\), the partials are \(f_x=x^2y+z^3\), \(f_y=x^3+y^2z\), \(f_z=y^3+z^2x\). If any coordinate vanishes and all partials vanish, all coordinates vanish, impossible projectively. Otherwise normalize \(z=1\); the partials imply \(x=y^3\), \(x^3=y^2\), and \(x^2y=1\). Then \(f=x^3y+y^3+x=y^3\ne0\) at every common zero of the partials. Hence \(C\) is geometrically smooth, of genus three.

**All bitangents.** If a line has nonzero \(z\)-coefficient, write \(z=ux+vy\). In characteristic two its quartic restriction equals
\[
 u^3x^4+(1+u^2v)x^3y+uv^2x^2y^2+(u+v^3)xy^3+vy^4.
\]
This is the square of a binary quadratic if and only if the two odd-exponent coefficients vanish: \(u=v^3\) and \(1+u^2v=0\). Thus \(v^7=1\), giving \(u=t^3\), \(v=t\), as asserted. No line with zero \(z\)-coefficient has square restriction: for \(ax+by=0\), direct substitution leaves an odd-exponent monomial \(z^3x\), or \(y^3z\) if \(x=0\). These cases exhaust all projective lines.

**Exact tangent-contact scheme.** Substituting \(z=t^3x+ty\), using \(t^7=1\), yields the polynomial identity
\[
 f(x,y,t^3x+ty)=t^2x^4+t^5x^2y^2+ty^4
 =(tx^2+t^6xy+t^4y^2)^2.
\]
The quadratic \(tx^2+t^6xy+t^4y^2\) is separable: after setting \(y=1\), divide by \(t\) and put \(x=t^5w\) to obtain \(w^2+w+1=0\). Its two distinct roots lie in \(\mathbb F_4\setminus\mathbb F_2\), giving \(P_{t,w}\) above. Since \(t^7-1\) and \(w^2+w+1\) are separable, the seven-line and fourteen-flag parameter schemes are finite étale of degrees seven and fourteen. The displayed equations are explicit inverse parameterizations of the corresponding geometric incidence schemes, so no additional scheme-theoretic multiplicity appears.

**Frobenius descent.** Arithmetic Frobenius squares \(t\) and \(w\). On \(\mathbb F_8^\times\), squaring has one fixed element \(t=1\) and two length-three orbits. The roots of \(w^2+w+1\) are exchanged by squaring. Thus the corresponding flag orbits have lengths \(2\) for \(t=1\) and \(6,6\) for the six other parameters. Standard zeta-factorization for a finite étale scheme with Frobenius orbit lengths \(d_j\) yields \(\prod_j(1-T^{d_j})^{-1}\), proving both point-count and zeta formulas for every \(m\ge1\).

**Explicit Fano incidence.** For distinct \(a,b\in\mathbb F_8^\times\), solve \(L_a=L_b=0\) with \(x=1\). This gives \(y=a^2+ab+b^2\) and \(z=ab(a+b)\). The same point lies on \(L_{a+b}\); \(a+b\ne0\) is again a seventh root. The 21 unordered pairs partition into seven triples, hence exactly seven triple vertices. Each vertex is \(\mathbb F_8\)-rational, whereas each line's geometric contact points have a nontrivial \(\mathbb F_4\) factor: their \(x/y=t^5w\) is not in \(\mathbb F_8\), because \(\mathbb F_4\cap\mathbb F_8=\mathbb F_2\). Hence no vertex lies on \(C\), and there are no higher-multiplicity concurrency points.

## Verification
A standalone dependency-free verifier, `klein_char2_verify.py`, implements \(\mathbb F_{64}=\mathbb F_2[W]/(W^6+W+1)\), enumerates every seventh root and both cubic-root parameters, verifies the restriction-square identities across all binary inputs, checks all fourteen contact points and the seven off-curve triple vertices, and computes the exact Frobenius orbit lengths. Command: `python3 klein_char2_verify.py`. Expected final line: `VERIFY_OK`. These are finite corroborating computations; the preceding symbolic argument proves the geometric and all-extension claims.

## Relationship to prior work
The geometric seven-bitangent Fano arrangement is **not new**: Wall's classification of characteristic-two plane quartics, reproduced in Dolgachev--Kondō Proposition 5.8, covers it over an algebraic closure. Van Lint's algebraic-geometric coding lecture, Example 3.12, already treats this **same** equation and its \(\mathbb F_2\)-rational line \(x+y+z=0\), the two \(\mathbb F_4\)-rational contacts, and the absence of contacts over \(\mathbb F_8\). None of those facts is claimed as new. The contribution isolated here is the **complete explicit Frobenius descent of the seven-line scheme and all fourteen contact flags**, including the degree-six contact cycles and both finite-scheme zeta functions. Elkies' discussion of characteristic-two Klein models emphasizes that different twists have different arithmetic Frobenius actions, so geometric line counts alone do not imply this descended configuration. Plaumann--Sturmfels--Vinzant's 2010 discussion concerns classical complex bitangents, not these characteristic-two arithmetic cycles.

## Limitations
Novelty is a best-knowledge assessment, not an exhaustive historical priority certificate; a complete older computation of these same Frobenius cycles could supersede this result. The Fano incidence type itself and the first two contact points are prior knowledge. The first-public date in the accompanying metadata is the first precise day verified for one archival source examined; older historical works exist but their first-public **day** was not established. The result is self-contained for the stated model and its contact configuration, and does not address theta characteristics with additional marking, Galois cohomology of twists, or arbitrary genus-three quartics.

## References
1. J. H. van Lint, *Introduction to Coding Theory and Algebraic Geometry*, lecture notes, §§3.12--3.13. [Accessible PDF](https://theswissbay.ch/pdf/Gentoomen%20Library/Information%20Theory/Coding%20Theory/Introduction%20To%20Coding%20Theory%20And%20Algebraic%20Geometry%20-%20Jacobus%20Van%20Lint.pdf).
2. C. T. C. Wall, *Quartic curves in characteristic 2*, Math. Proc. Camb. Phil. Soc. 117 (1995), 393--414.
3. I. Dolgachev and S. Kondō, *Bitangent surfaces and involutions of quartic surfaces*, Proposition 5.8 (reproduces Wall's classification). [Accessible PDF](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1467/2026/02/EPiGA-1.pdf).
4. N. D. Elkies, *The Klein Quartic in Number Theory*, MSRI Publications 35 (1998), §3, characteristic-two models. [Accessible PDF](https://library.slmath.org/books/Book35/files/elkies.pdf).
5. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104, first posted 2010-08-24; characteristic-zero background. [https://arxiv.org/abs/1008.4104](https://arxiv.org/abs/1008.4104).
