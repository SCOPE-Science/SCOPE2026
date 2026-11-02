# Quadratically thickened jumping triangles for odd Fermat curves

## Finding
For every integer \(r\ge 2\), let \(C_r\subset\mathbf P^2_{\mathbf C}\) be the smooth Fermat curve
\[
C_r:\quad x^{2r+1}+y^{2r+1}+z^{2r+1}=0.
\]
Let \(E_r=T_{\mathbf P^2}(-\log C_r)\) be the logarithmic tangent bundle and normalize it by \(F_r=E_r(r-1)\). Then \(F_r\) is stable, with \(c_1(F_r)=0\) and \(c_2(F_r)=3r^2\). For every line \(L_{[a:b:c]}=\{ax+by+cz=0\}\), the restriction has precisely one of two splitting types:
\[
F_r|_{L_{[a:b:c]}}\cong
\begin{cases}
\mathcal O_L\oplus\mathcal O_L,&abc\ne0,\\
\mathcal O_L(r)\oplus\mathcal O_L(-r),&abc=0.
\end{cases}
\]
In particular there are no lines of intermediate jumping order. With the canonical determinant (Barth) scheme structure, the jumping divisor on the dual plane is exactly
\[
\boxed{\ J(F_r)=V\!\bigl((abc)^{r^2}\bigr)
=r^2\{a=0\}+r^2\{b=0\}+r^2\{c=0\}.\ }
\]
The scheme-theoretic multiplicity of each coordinate pencil grows quadratically with the curve degree. For the smooth Fermat quintic \(r=2\), the jumping divisor is the coordinate triangle with multiplicity four on each side, of total degree twelve.

## Assumptions and scope
The base field is \(\mathbf C\), the curve has odd degree \(2r+1\) with \(r\ge2\), and the coordinate dual plane is \((\mathbf P^2)^\vee\). The logarithmic tangent sheaf of the smooth divisor is locally free. The term *jumping divisor* refers to the degeneracy Cartier divisor of the natural square map on global sections over a varying line; this is the standard determinant scheme for normalized stable rank-two bundles with first Chern class zero. Its underlying reduced set is distinguished from its nonreduced scheme structure. The formula does not concern arbitrary smooth curves or positive characteristic.

## Proof
**(1) Gradient bundle and stability.** Write \(d=2r+1\), so the three partial derivatives of the defining equation are nonzero multiples of \(x^{2r},y^{2r},z^{2r}\). They have no common projective zero, so the usual logarithmic-gradient sequence is exact:
\[
0\longrightarrow E_r\longrightarrow\mathcal O_{\mathbf P^2}(1)^{\oplus3}
\xrightarrow{(x^{2r},y^{2r},z^{2r})}\mathcal O_{\mathbf P^2}(2r+1)\longrightarrow0.
\]
Taking Chern classes gives \(c_1(E_r)=2-2r\) and \(c_2(E_r)=4r^2-2r+1\). Twisting by \(r-1\) gives \(c_1(F_r)=0\) and \(c_2(F_r)=3r^2\). A global section of \(F_r\) would be a syzygy on \((x^{2r},y^{2r},z^{2r})\) with coefficients of degree \(r\), but the elementary Koszul syzygies have minimal coefficient degree \(2r\), and the three monomial ideals have no non-Koszul syzygies. Thus \(H^0(\mathbf P^2,F_r)=0\). Since \(F_r\) is a normalized rank-two vector bundle with trivial determinant, this implies slope-stability: a destabilizing saturated rank-one subsheaf would have nonnegative degree and produce a section after multiplying by a homogeneous form.

**(2) Square jumping matrix.** For a line \(L\), tensor the exact gradient sequence by \(\mathcal O_L(r-2)\):
\[
0\longrightarrow F_r(-1)|_L\longrightarrow
\mathcal O_L(r-1)^{\oplus3}\xrightarrow{\Phi_L}
\mathcal O_L(3r-1)\longrightarrow0.
\]
Both spaces of global sections in \(\Phi_L\) have dimension \(3r\). The line jumps if and only if the square map \(H^0(\Phi_L)\) is singular: if \(F_r|_L=\mathcal O_L(t)\oplus\mathcal O_L(-t)\), then \(H^0(F_r(-1)|_L)\ne0\) is equivalent to \(t\ge1\). Consequently the determinant of this family of square maps defines its jumping Cartier divisor.

**(3) Exact determinant on the chart \(c\ne0\).** Write \(A=a/c\) and \(B=b/c\), so \(L\) is parametrized by \(z=-Ax-By\). The map \(\Phi_L\) is multiplication by the three binary forms \(x^{2r},y^{2r},(Ax+By)^{2r}\), with coefficients in binary forms of degree \(r-1\). Use monomial bases ordered by the exponent of \(x\). The first two blocks provide unit pivots for the \(r\) lowest and \(r\) highest exponents of \(x\). Deleting their rows and columns leaves an \(r\)-by-\(r\) middle block with entries (indices \(0\le i,j\le r-1\))
\[
N_{ij}=\binom{2r}{r+i-j}A^{r+i-j}B^{r-i+j}.
\]
The determinant of the full square map equals \(\pm\det N\), and every permutation term of \(\det N\) contains exactly \(r^2\) factors of each of \(A\) and \(B\). Hence
\[
\det\Phi_L=\pm (AB)^{r^2}D_r,\qquad
D_r=\det\!\left[\binom{2r}{r+i-j}\right]_{0\le i,j<r}.
\]
The constant \(D_r\) never vanishes over \(\mathbf C\). Indeed Vandermonde's identity writes its matrix as \(PP^{\mathsf T}\), where \(P_{it}=\binom r{t-i}\) for \(0\le i<r\), \(0\le t<2r\), and out-of-range binomial coefficients vanish. The first \(r\) columns of \(P\) form a triangular matrix with diagonal entries one, so \(P\) has full row rank. Therefore \(PP^{\mathsf T}\) is positive definite over \(\mathbf R\), proving \(D_r>0\). Thus on \(c\ne0\), the determinant vanishes to order exactly \(r^2\) along each of \(a=0\) and \(b=0\), and nowhere else.

**(4) Global scheme structure.** Over the dual plane let \(\mathcal U\) denote the rank-two tautological subbundle of the constant three-dimensional vector space, whose fiber is the vector space defining the corresponding line. Then the global square map has domain \((\operatorname{Sym}^{r-1}\mathcal U^\vee)^{\oplus3}\) and target \(\operatorname{Sym}^{3r-1}\mathcal U^\vee\). The determinant is a section of
\[
\mathcal O_{(\mathbf P^2)^\vee}\!\left(
\frac{(3r-1)(3r)}2-3\frac{(r-1)r}2\right)
=\mathcal O_{(\mathbf P^2)^\vee}(3r^2).
\]
Permuting coordinates makes the three coordinate pencils symmetric. By step (3), the divisor has no other components and has exact multiplicity \(r^2\) along two of them. Symmetry gives the same multiplicity along the third. Its defining homogeneous equation is therefore a nonzero scalar multiple of \((abc)^{r^2}\); this proves equality as Cartier divisors, not merely of reduced sets.

**(5) Exact splitting on the coordinate pencils.** If one of \(a,b,c\) vanishes, the restrictions of the three monomials \(x^{2r},y^{2r},z^{2r}\) to \(L\) have a constant syzygy: either one vanishes or two are proportional. The remaining two independent forms are powers of distinct linear coordinates on \(L\) and have no common zero, so their syzygy bundle splits as \(\mathcal O_L\oplus\mathcal O_L(-2r)\). Reinstating the \(\mathcal O_L(1)\) gradient twist and then twisting by \(r-1\) yields \(F_r|_L\cong\mathcal O_L(r)\oplus\mathcal O_L(-r)\). If \(abc\ne0\), step (3) says \(H^0(F_r(-1)|_L)=0\). Since the restricted bundle has degree zero, this forces its splitting to be \(\mathcal O_L^{\oplus2}\), completing the classification.

## Verification
Run `python3 artifacts/verify_jumping.py` with Python 3 and no additional packages. The supplied script uses exact integer Bareiss elimination, binomial convolution and Gram factorizations; it checks \(D_r>0\) and the Chern formula for \(1\le r\le8\), and checks the full \(3r\)-by-\(3r\) multiplication determinant at three nontrivial coefficient pairs for \(1\le r\le5\), totaling 23 test sets. Its expected terminal line is `VERIFY_OK: 23 exact determinant/Gram/Chern test sets`. The proof for all \(r\ge2\) rests on the symbolic Vandermonde/Gram argument, not on these finite experiments.

## Relationship to prior work
Dimca and Sticlaru (2018) study jumping lines of logarithmic bundles of plane curves and explicitly describe the Fermat cubic jumping triangle and a Fermat-quartic example of jumping lines of the second kind. These cases, the general jumping-line criterion and the expected degree of the Barth divisor are not claimed as new. Brenner and Kaid (2010) connect syzygy bundles of powers to weak Lefschetz properties and generic splitting; their generic balanced-splitting framework does not state the all-odd-degree scheme equation. Guardo, Keiper and Malara (2026) give determinant constructions and examples of jumping divisors with fixed components for bundles from finite point configurations and line arrangements. Their subject differs from the smooth Fermat curve's logarithmic tangent bundle. The result here is the uniform **exact Cartier divisor** and the **complete splitting classification** for every odd smooth Fermat degree. Related general theories can make this specialization computationally accessible; no claim is made that the underlying determinant techniques are new.

## Limitations
The result is restricted to smooth odd-degree Fermat plane curves over \(\mathbf C\). The determinant scheme is specifically the standard first jumping divisor defined by \(H^0(F_r(-1)|_L)\), not a claim about every possible higher degeneracy/Fitting convention. The result does not address even Fermat degrees, deforming away from Fermat curves, or characteristic-dependent cancellations in positive characteristic. Literature coverage is extensive but cannot certify absolute historical priority; independent mathematical review has not been performed.

## References
1. E. Guardo, G. Keiper, G. Malara, *Interpolation matrices and jumping lines of logarithmic bundles*, arXiv:2601.11114 (first posted January 16, 2026); https://arxiv.org/html/2601.11114v1.
2. A. Dimca, G. Sticlaru, *On the jumping lines of bundles of logarithmic vector fields along plane curves*, arXiv:1804.06349 (2018); https://arxiv.org/abs/1804.06349.
3. H. Brenner, A. Kaid, *A note on the weak Lefschetz property of monomial complete intersections in positive characteristic*, arXiv:1003.0824 (2010); https://arxiv.org/abs/1003.0824.
