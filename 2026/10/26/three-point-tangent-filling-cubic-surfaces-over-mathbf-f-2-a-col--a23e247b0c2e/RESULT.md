# Three-point tangent-filling cubic surfaces over \(\mathbf F_2\): a collinearity criterion and two orbits

## Finding
For a geometrically smooth cubic surface \(S\subset\mathbf P^3_{\mathbf F_2}\), call \(S\) *tangent-filling* when the union of the tangent planes \(T_PS\) at all \(P\in S(\mathbf F_2)\) contains all \(15\) rational points of the ambient projective space. The sharp minimum of \(\#S(\mathbf F_2)\) among tangent-filling smooth cubics is \(3\). For **every** smooth cubic surface with exactly three rational points, tangent-filling is equivalent to collinearity of those three points.

There are exactly \(1{,}540\) scalar-normalized equations defining tangent-filling smooth cubic surfaces attaining this minimum in fixed projective coordinates. They form exactly two \(\operatorname{PGL}_4(\mathbf F_2)\)-orbits, of sizes \(420\) and \(1{,}120\), with respective projective stabilizer orders \(48\) and \(18\). In the size-\(420\) orbit, the unique rational line through the three points is **contained** in the cubic surface as a geometric line; in the size-\(1{,}120\) orbit, it is **not** contained. Thus the two types have the same rational point set and the same three tangent-plane pencil, but different scheme-theoretic line incidence.

With homogeneous coordinates \([w:x:y:z]\), representatives for the two types are
\[
 F_{\mathrm{in}}=w^3+w^2x+w^2z+wz^2+x^3+x^2y+xy^2,
\qquad
 F_{\mathrm{out}}=w^3+wx^2+x^3+y^2z+yz^2.
\]
Both have precisely the three rational points of \(L=\{w=x=0\}\), and their tangent planes at those points are the three distinct planes through one rational line.

## Assumptions and scope
The base field is exactly \(k=\mathbf F_2\). "Surface" means the projective zero scheme of a nonzero homogeneous polynomial of total degree three in four variables; smoothness means geometric smoothness after algebraic closure. Over this field scalar normalization is unique. The two orbits are under projective **linear** coordinate change of the fixed embedding; they are not claimed to classify abstract isomorphism types over other fields. The tangent-filling condition uses only tangent planes at \(k\)-rational smooth surface points and covering of \(\mathbf P^3(k)\), not tangent planes at every geometric point.

## Proof
**1. A parity obstruction and the covering minimum.** For any homogeneous ternary-degree cubic \(F\) in four binary variables, \(\sum_{v\in k^4}F(v)=0\) in \(k\), since each degree-three monomial is independent of at least one coordinate. Thus the number of zero vectors of \(F\) is even; removing the zero vector shows that \(\#V(F)(k)\) is odd. Every rational hyperplane of \(\mathbf P^3(k)\) has seven points. Consequently a tangent-filling surface cannot have one rational point. Three distinct rational planes cover all fifteen rational points if and only if they are the three planes through one rational line: pairwise intersections have three points, and their triple intersection has three points in the pencil case and one otherwise, yielding union sizes \(15\) and \(13\), respectively.

**2. The equivalence for exactly three rational surface points.** For every homogeneous cubic in characteristic two and vectors \(a,b\), direct polarization gives
\[
 F(a+b)=F(a)+F(b)+\nabla F(a)\mathbin{\cdot}b+\nabla F(b)\mathbin{\cdot}a.
\]
Euler's identity gives \(\nabla F(a)\mathbin{\cdot}a=F(a)\). Suppose the only nonzero zero vectors are three linearly independent vectors \(a,b,c\). Their pairwise sums are nonzero points not on the surface, so
\[
 F(a+b)+F(a+c)+F(b+c)=1.
\]
By the polarization identity the left side equals \((\nabla F(a)+\nabla F(b)+\nabla F(c))\mathbin{\cdot}(a+b+c)\), because all three Euler diagonal terms vanish. Thus the three gradients cannot sum to zero. For three tangent planes to cover, however, their nonzero normals would necessarily be the three elements of a two-dimensional subspace and hence sum to zero. Therefore a tangent-filling three-point smooth cubic has collinear rational points.

Conversely suppose the rational zero set consists of the three nonzero vectors of a two-dimensional linear subspace \(U\). A projective linear change takes \(U\) to \(\{w=x=0\}\). The cubic
\[
 F_0=w^3+x^3+w^2x
\]
has rational value \(0\) on \(U\) and \(1\) at every vector outside \(U\). The vector space of homogeneous cubic forms vanishing at every vector in \(k^4\) has dimension six, with basis
\[
 K_{ij}=X_i^2X_j+X_iX_j^2\quad(0\le i<j\le3),
 \quad (X_0,X_1,X_2,X_3)=(w,x,y,z).
\]
Indeed the Boolean evaluation of the twenty cubic monomials spans the fourteen squarefree nonconstant monomials of degrees one, two and three; the six displayed independent relations span its kernel. Hence every cubic with rational zero set \(U\setminus\{0\}\) is uniquely \(F_0+\sum b_{ij}K_{ij}\). On \(U\), \(\nabla F_0=0\) and \(\nabla K_{ij}(v)\) depends linearly on \(v\): it is the \(i,j\) alternating-matrix contribution. The three gradients at the nonzero vectors of \(U\) consequently sum to zero. Geometric smoothness makes them nonzero; linearity and nonvanishing make them distinct. Their tangent planes therefore form the complete three-plane pencil and cover the rational projective space.

**3. Exact count for a prescribed rational line.** Write \(\lambda=b_{23}\) and let \(a=b_{02},b=b_{12},c=b_{03},d=b_{13}\). At the rational points of \(U\), the two gradient columns for \(y\) and \(z\) are
\[
  (a,b,0,\lambda)^\top,\qquad(c,d,\lambda,0)^\top.
\]
All three rational points are regular exactly when these columns are independent over \(k\). If \(\lambda=1\), independence is automatic, giving \(2^4\cdot2=32\) forms, with the last factor the unrestricted \(b_{01}\). If \(\lambda=0\), the matrix \(\left(\begin{smallmatrix}a&c\\b&d\end{smallmatrix}\right)\) must be invertible, giving \(\#\mathrm{GL}_2(k)\cdot2=6\cdot2=12\) forms. Exactly \(44\) of the \(64\) cubics having this rational zero set are regular at their rational points. Also \(F|_L=\lambda(y^2z+yz^2)\), so precisely the twelve with \(\lambda=0\) contain the line scheme-theoretically.

**4. Geometric smoothness and projective-orbit completeness.** The two displayed representatives are within the 12- and 32-element collections. Their respective gradient systems, with partials ordered \((w,x,y,z)\), are
\[
 \nabla F_{\mathrm{in}}=(w^2+z^2,\ w^2+x^2+y^2,\ x^2,\ w^2),
 \qquad
 \nabla F_{\mathrm{out}}=(w^2+x^2,\ x^2,\ z^2,\ y^2).
\]
Each four-equation system vanishes only at the origin over an algebraic closure, so each representative is geometrically smooth. The stabilizer of \(L\) in \(\mathrm{GL}_4(k)\) has order \(576\): the two columns spanning \(U\) have \(6\) choices, the quotient has \(6\) choices, and the two lifted quotient basis vectors have \(4^2=16\) choices. Exact substitution of all these \(576\) invertible matrices gives orbits of \(12\) and \(32\) cubics from the two representatives, respectively (complete executable enumeration: `check_normal_forms.py`). Since these exhaust all \(44\) rationally regular forms and line containment distinguishes the two collections, all 44 are geometrically smooth and constitute exactly two stabilizer orbits. There are \(35\) rational projective lines in \(\mathbf P^3(k)\), and the rational zero line of each three-point extremizer is unique. The global orbit sizes are \(35\cdot12=420\) and \(35\cdot32=1{,}120\); their sum is \(1{,}540\). Finally \(\#\operatorname{PGL}_4(k)=20{,}160\) gives stabilizer orders \(48\) and \(18\).

## Verification
`check_normal_forms.py` is a dependency-free executable certificate that constructs the exact cubic monomial basis, all six evaluation-kernel generators, all 64 line-filling cubic forms, and all 576 matrices stabilizing \(L\). It checks the full 12- and 32-element orbits under actual polynomial substitution, confirms the 44 regular-at-rational-point forms, and checks rank four of the square-coordinate Jacobian matrices of the two representatives, which proves their geometric smoothness. Run `python3 check_normal_forms.py`; it prints a final `PASS` statement.

An independent full-space computational crosscheck is provided in `crosscheck_full_scan.cpp`. It enumerates every one of the \(2^{20}-1\) nonzero quaternary cubic forms, computes rational points and tangent-plane coverage from bitwise exact evaluations, and confirms that exactly 1,540 three-point cubics are rationally regular and tangent-filling, with none having only one rational point. Compile and run using `g++ -O3 -std=c++17 crosscheck_full_scan.cpp -o crosscheck_full_scan && ./crosscheck_full_scan`. This second program does **not** substitute for the geometric smoothness proof; the proof uses the representative Jacobian and projective-orbit reduction above.

## Relationship to prior work
Asgarli–Ghioca (first public version 2023-02-26) introduced and studied tangent-filling **plane curves**, defined using tangent lines in \(\mathbf P^2\); their theorems and proof do not furnish the three-dimensional cubic-surface collinearity criterion or the \(1{,}540\)-surface stratification. The natural higher-dimensional dual-incidence analogue motivates the present question.

The complete older projective classifications of binary cubic surfaces (especially Dickson 1915) and literature on their rational lines (including McKean, first preprint 2021-01-20), together with modern automorphism results (Vikulova, first preprint 2023-12-28), are relevant: they cover broader **surface types**, rational lines or automorphisms. In particular, the orbit counts by themselves should not be presented as new classifications of cubic surfaces. The specific equivalence between three-point tangent-plane covering and collinearity, the automatic geometric smoothness of the 44 rationally regular fixed-line forms, and the split by scheme-theoretic containment of the point line are the claimed new incidence statements. A prior complete surface classification might make the numerical orbit stratification recoverable after additional tangent calculations; this is a residual priority risk.

## Limitations
The criterion applies to geometrically smooth **cubic surfaces over exactly \(\mathbf F_2\)** having precisely three rational points. It does not assert a classification of tangent-filling cubics with five or more rational points, general fields, higher-degree surfaces, or geometric tangent hyperplanes. The 1915 Dickson full text and one 2021 small-field surface paper were not available for full comparison in the performed source access; they remain publication-priority risks. No independent external audit has been performed.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, v1 dated 2023-02-26; published 2024. https://arxiv.org/abs/2302.13420
2. S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217, first posted 2021-01-20. https://arxiv.org/abs/2101.08217
3. A. V. Vikulova, *The most symmetric smooth cubic surface over a finite field of characteristic 2*, arXiv:2312.17032, first posted 2023-12-28. https://arxiv.org/abs/2312.17032
4. L. E. Dickson, *Projective Classification of Cubic Surfaces Modulo 2*, Ann. of Math. 16 (1914–15), 139–157. https://doi.org/10.2307/1968056
5. F. Karaoğlu, *Non-Singular Cubic Surfaces over \(\mathbf F_{2^k}\)*, Turkish J. Math. 45 (2021), 2492–2510. https://doi.org/10.3906/mat-2102-10
