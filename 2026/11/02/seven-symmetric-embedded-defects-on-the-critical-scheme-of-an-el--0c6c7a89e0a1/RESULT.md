# Seven symmetric embedded defects on the critical scheme of an elementary-symmetric quartic

## Finding

Let \(k\) be algebraically closed of characteristic \(2\). Define the elementary-symmetric quartic
\[
F=e_4(x_1,\ldots,x_6)=\sum_{1\le i<j<\ell<m\le6}x_ix_jx_\ell x_m
\]
and its homogeneous gradient ideal \(J=(F_{x_1},\ldots,F_{x_6})\) in \(R=k[x_1,\ldots,x_6]\). Set \(Y=\operatorname{Proj}(R/J)\subset\mathbb P^5_k\). Consider the projective frame
\[
P_i=[e_i]\quad(1\le i\le6),\qquad P_7=[1:1:1:1:1:1].
\]
Then the following statements hold jointly.

1. The reduced scheme \(C=Y_{\mathrm{red}}\) is the union of **exactly 21 lines** \(\overline{P_iP_j}\) for \(1\le i<j\le7\). Their only pairwise intersections are the seven frame vertices; six lines pass through each vertex.
2. The scheme \(Y\) is reduced along the complement of the seven vertices. The finite-length sheaf \(\mathcal I_{C/Y}\) (the kernel of \(\mathcal O_Y\twoheadrightarrow\mathcal O_C\)) has **length 8 at every frame vertex** and total length \(56\).
3. The full Hilbert series and Hilbert polynomial are
\[
\operatorname{Hilb}_{R/J}(t)
=\frac{1+4t+10t^2+14t^3+12t^4-11t^6-10t^7+t^8}{(1-t)^2},
\quad P_Y(d)=21d+35.
\]
For the reduced curve, \(P_C(d)=21d-21\).
4. The full **projective linear stabilizer** of \(Y\) is the symmetric group \(S_7\), acting on the seven vertices. In particular, the nontrivial linear map
\[
T_i:(x_1,\ldots,x_6)\longmapsto(x_1+x_i,\ldots,x_{i-1}+x_i,x_i,x_{i+1}+x_i,\ldots,x_6+x_i)
\]
interchanges \(P_i\) and \(P_7\), fixes the other five vertices, and satisfies \(F\circ T_i=F+x_i^4\).
5. Crucially, \(Y\) is the *gradient-critical scheme*, not the singular scheme of the quartic hypersurface \(V(F)\). Its six noncoordinate lines do not lie on \(V(F)\); the reduced singular locus of \(V(F)\) is exactly the fifteen coordinate lines.

## Assumptions and scope

All schemes are over an algebraically closed field of characteristic \(2\), and all Hilbert polynomials are with respect to the indicated projective embeddings. "Embedded correction" means the finite-length kernel of \(\mathcal O_Y\to\mathcal O_{Y_{\mathrm{red}}}\); the assertion is **not** an explicit primary decomposition or a classification of the local Artin algebras. \(Y\) is defined by the gradient ideal alone, without adjoining \(F\), a distinction necessary because the degree \(4\) vanishes in the base field.

## Proof

**A. Exact reduced support.** For any coordinate \(x_i\), the characteristic-two identity
\[
F_{x_i}=e_3+x_i e_2+x_i^2e_1+x_i^3
\]
shows that at a critical point every coordinate value is a root of a single monic cubic. Consequently there are at most three distinct coordinate values. When there are exactly two distinct values \(a,b\) appearing with multiplicities \(m,6-m\), direct substitution into the six derivatives gives, up to symmetry:
\[
\begin{array}{c|cc}
m&F_{x_i}\text{ at an }a&F_{x_j}\text{ at a }b\\\hline
1&0&0\\
2&0&b(a+b)^2\\
3&b(a+b)^2&a(a+b)^2\\
4&a(a+b)^2&0\\
5&0&0
\end{array}
\]
Thus only the \(m=1,5\) unrestricted families, and the coordinate-line specializations, survive. For three pairwise distinct values \(a,b,c\), the only multiplicity patterns, up to relabelling, are \((4,1,1)\), \((3,2,1)\), and \((2,2,2)\). Their respective derivative triples are
\[
\begin{aligned}
(4,1,1)&:\quad(a(a+b)(a+c),0,0),\\
(3,2,1)&:\quad(c(a+b)^2,a(a+b)(a+c),a(a+b)^2),\\
(2,2,2)&:\quad(a(b+c)^2,b(a+c)^2,c(a+b)^2).
\end{aligned}
\]
The last two patterns cannot vanish for distinct values; the first forces \(a=0\), leaving exactly two freely chosen nonzero coordinates. The single-value case is the point \(P_7\). Hence the critical locus is exactly the fifteen coordinate lines together with the six lines joining \(P_7\) to the coordinate vertices. These are precisely the edges of the seven-point projective frame; any four vertices are linearly independent, so disjoint edges do not meet.

**B. No generic or off-vertex thickening.** The Hessian has entries \(H_{ii}=0\) and \(H_{ij}=e_2\) in the four variables other than \(x_i,x_j\), for \(i\ne j\). On a coordinate line with two nonzero coordinates \(a,b\), the transverse four-by-four block has zero diagonal and constant off-diagonal entry \(ab\), hence rank \(4\) in characteristic \(2\). On a noncoordinate frame line, write the coordinates as \((a,b,b,b,b,b)\), with \(b(a+b)\ne0\) away from its two endpoints. The five-by-five Hessian block transverse to the distinguished coordinate is \(b(a+b)\) times the matrix with zero diagonal and all off-diagonal entries one, of rank \(4\). Thus the projective gradient equations have Jacobian rank four at every nonvertex point of their one-dimensional reduced support. The Jacobian criterion makes \(Y\) smooth, hence reduced, there. Any discrepancy from \(C\) is therefore supported at the seven vertices.

**C. Hilbert polynomial of the reduced curve.** Its normalization is the disjoint union of \(21\) projective lines. At each vertex six branches meet, with tangent directions projectively equivalent to the five coordinate axes and their sum in the affine tangent space of dimension five. In the normalization-to-curve local ring comparison, constants on the six branches have codimension \(5\), first-order coefficients have codimension \(1\), and higher-degree coefficients are unrestricted. For the last assertion, five coordinate squares and one cross-product distinguish all six tangent directions at degree two; multiplying by a linear form nonzero on all six directions propagates surjectivity to higher orders. Hence the local normalization quotient has length \(5+1=6\) at each vertex. Since the curve has \(21\) rational irreducible components, the normalization exact sequence gives
\[
P_C(d)=21(d+1)-7\cdot6=21d-21.
\]

**D. Exact Hilbert series of the gradient ideal.** Computing a Gröbner basis of the six cubics over \(\mathbb F_2\) in graded reverse lexicographic order produces \(49\) basis elements, with minimal initial monomials of degree distribution \(6,7,13,12,9,2\) in degrees \(3,4,5,6,7,8\). The monomial-ideal deletion/colon recursion computes the numerator of \(\operatorname{Hilb}_{R/J}(t)\), over denominator \((1-t)^6\), as
\[
1-6t^3+t^4+15t^6-13t^8-20t^9+35t^{10}-14t^{11}+t^{12}.
\]
This factors as \((1-t)^4(1+4t+10t^2+14t^3+12t^4-11t^6-10t^7+t^8)\), proving the stated series and \(P_Y(d)=21d+35\). A complete exact-arithmetic reproduction is supplied as `verify.py`; it recomputes the basis, leading monomials and Hilbert recursion from the defining polynomial rather than trusting a printed list. The same program independently evaluates the first nine graded pieces of the reduced line union via restriction matrices.

Since the two schemes agree outside the seven vertices, the Hilbert-polynomial difference is the length of their zero-dimensional discrepancy:
\[
\operatorname{length}(\mathcal I_{C/Y})=(21d+35)-(21d-21)=56.
\]

**E. Symmetry and equal local lengths.** For each \(i\), direct expansion modulo two yields \(F\circ T_i=F+x_i^4\); differentiating and using invertibility of \(T_i\) shows that \(T_i\) preserves \(J\). The maps \(T_i\) interchange \(P_i\) and \(P_7\), while coordinate permutations generate permutations of the first six points. Together they realize all of \(S_7\), transitively on the vertices. Therefore the seven local correction lengths are equal, and each is \(56/7=8\). Conversely, any projective linear automorphism of \(Y\) preserves its reduced line arrangement and so permutes its seven uniquely six-valent points. A projective transformation fixing all seven points of a projective frame is the identity. This embeds the stabilizer into \(S_7\), proving equality.

Finally, \(F\) restricts to zero on every coordinate line and to \(b^4\) on \((a,b,b,b,b,b)\). Hence the only critical lines lying on the quartic hypersurface are the fifteen coordinate lines. This is a statement about the reduced hypersurface singular locus, not its full singular subscheme.

## Verification

Run `python verify.py` with SymPy installed. The script works entirely over exact finite-field and integer arithmetic: it checks the six Frobenius identities, computes the \(49\)-polynomial Gröbner basis, derives the Hilbert numerator recursively, and calculates the graded restriction ranks for the \(21\)-line union through degree eight. A successful run prints `VERIFY_OK`. The line-count classification, local smoothness and vertex normalization length also have the analytic proofs above; the program verifies critical algebraic identities without pretending finite-dimensional computations alone prove unrelated generalizations.

## Relationship to prior work

Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic* (arXiv:2610.00259, first submitted 2026-09-24) proves general dimension formulas and analyzes extremal components and generic coordinate-component multiplicities; the current exact smaller-dimension support, seven-vertex embedded correction and projective symmetry are additional scheme-specific statements, not asserted as prior general theorems. Orzel (arXiv:2509.05009) studies vanishing loci and dimensions of derivatives of elementary symmetric polynomials. Cafure, Matera and Privitelli (arXiv:1109.2265) provide general coordinate-value bounds for singularities of symmetric hypersurfaces. The present proof uses and refines those kinds of methods in one characteristic-two quartic case; no claim of exclusive historical priority is made.

## Limitations

The assertion is about \(e_4\) in precisely six variables over characteristic \(2\). It does not determine a full primary decomposition or classify local embedded Artin algebras, and does not generalize the Hilbert series to arbitrary degrees, characteristics or numbers of variables. Computational Hilbert claims rely on reproducible exact Gröbner calculations, not on a separate formal verification. An independent mathematical audit has not been performed, and a literature comparison cannot exclude every unpublished or differently formulated result.

## References

1. Y. Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259, version 1, publicly submitted 2026-09-24, https://arxiv.org/abs/2610.00259 .
2. J. Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009, publicly submitted 2025-09-05, https://arxiv.org/abs/2509.05009 .
3. A. Cafure, G. Matera, and M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed-Solomon codes*, arXiv:1109.2265, https://arxiv.org/abs/1109.2265 .
