# The complete line scheme and rank-26 line lattice of an explicit sextic branch surface

## Finding

For every integer \(d\ge4\), define the smooth degree-\(d\) surface over \(\mathbb Q\)
\[
S_d=\bigl\{x_1^d+x_1x_2^{d-1}+x_3^d-x_4^d=0\bigr\}\subset\mathbb P^3.
\]
The **entire Hilbert (Fano) scheme of lines** is the finite étale scheme
\[
F_1(S_d)\cong\operatorname{Spec}\mathbb Q[a,b]/(a^d+a,\ b^d-1),
\]
where the point \((a,b)\) corresponds to the line
\[
L_{a,b}:\quad x_1=a x_2,\qquad x_3=b x_4.
\]
There are exactly \(d^2\) geometric lines. Exactly four are defined over \(\mathbb Q\) if \(d\) is even, and exactly one if \(d\) is odd.

Two distinct lines meet if and only if they share their first or second parameter. On the smooth surface their intersection pairing is
\[
L_{a,b}\cdot L_{a',b'}=\begin{cases}
2-d,&(a,b)=(a',b'),\\
1,&a=a'\ \text{or}\ b=b'\text{ (but not both)},\\
0,&a\ne a',\ b\ne b'.
\end{cases}
\]
The \(d^2\)-by-\(d^2\) intersection matrix has eigenvalues \(d\) with multiplicity \(1\), zero with multiplicity \(2(d-1)\), and \(-d\) with multiplicity \((d-1)^2\). Hence the rational vector space spanned by these line divisor classes in \(\operatorname{NS}(S_d\otimes\overline{\mathbb Q})\otimes\mathbb Q\) has dimension exactly \((d-1)^2+1\).

For the specific sextic branch surface in Cheltsov--Tschinkel's example, \(d=6\): the full line scheme has **36 reduced geometric points, four rational points**, and the line divisor classes span a rank-\(26\) subspace of the geometric Néron--Severi group. In particular its geometric Picard number is at least \(26\).

## Assumptions and scope

The base field is \(\mathbb Q\) and geometric assertions are over \(\mathbb C\). The integer \(d\) ranges over every \(d\ge4\). The source's smooth sextic double solid is \(x_5^2=x_1^6+x_1x_2^5+x_3^6-x_4^6\); its branch divisor in \(\mathbb P^3\) is precisely \(S_6\). The claim concerns all projective lines in the branch **surface**, not lines in the double solid or arbitrary higher-degree curves. The Néron--Severi assertion computes the rank of the **span of the line classes**, not the full Picard number.

## Proof

**1. Smoothness.** The four partial derivatives of the defining form are
\[
 d x_1^{d-1}+x_2^{d-1},\quad (d-1)x_1x_2^{d-2},\quad d x_3^{d-1},\quad -d x_4^{d-1}.
\]
Their common zero over characteristic zero requires \(x_3=x_4=0\), and the first two derivatives then force \(x_1=x_2=0\). This is not a projective point, so \(S_d\) is smooth.

**2. Every line is one of the displayed lines.** Parametrize a projective line by four binary linear forms \(A(s,t),B(s,t),C(s,t),D(s,t)\). Their associated linear map has rank two. Let the ranks of the two pairs \((A,B)\) and \((C,D)\) be \(r_1,r_2\), each at most two. Neither rank can be zero, since the opposite pair would then have to yield an identically vanishing degree-\(d\) binary form, impossible for a rank-two pair, while a rank-one opposite pair yields a constant projective point rather than a line. If one rank is one and the other two, substituting the rank-two pair into its squarefree binary degree-\(d\) form produces \(d\) distinct roots, whereas the rank-one pair gives either zero or a scalar \(d\)-th power of a linear form. They cannot be negatives of each other.

If both pair ranks were two, the line equation would give a projective linear equivalence between the degree-\(d\) binary forms \(u^d+uv^{d-1}\) and \(z^d-w^d\), hence a Möbius equivalence between their two sets of roots. The second set is the \(d\)-th roots of unity on a generalized circle. The first set consists of \(0\) and the \((d-1)\)-st roots of \(-1\). Since \(d-1\ge3\), the latter roots uniquely determine the unit circle while \(0\) does not lie on it. These \(d\) points are not cocircular. Möbius transformations preserve generalized circles, so the root sets are not equivalent. Thus both pair ranks are one.

Consequently the four coordinates are \((a\ell_1,\ell_1,b\ell_2,\ell_2)\) for independent linear forms \(\ell_1,\ell_2\). The defining equation restricts to
\[
(a^d+a)\ell_1^d+(b^d-1)\ell_2^d=0.
\]
Independence of \(\ell_1\) and \(\ell_2\) forces \(a^d+a=b^d-1=0\), giving precisely the \(d^2\) lines stated. Both root polynomials are separable in characteristic zero.

**3. Scheme structure and arithmetic.** Adjunction gives \(K_{S_d}=(d-4)H\). For any displayed line \(L\), \(H\cdot L=1\), so \(-2=(K_{S_d}+L)\cdot L=(d-4)+L^2\), yielding \(L^2=2-d\). As a Cartier curve in a smooth surface, \(N_{L/S_d}\cong\mathcal O_{\mathbb P^1}(2-d)\), with no global sections. The Zariski tangent space of the Hilbert scheme of lines at \([L]\) is \(H^0(L,N_{L/S_d})=0\). Thus all its finitely many geometric points are reduced. The obvious morphism from the product of the two separable root schemes to the Hilbert scheme is a geometric bijection between finite étale \(\mathbb Q\)-schemes; hence it is the claimed isomorphism. Rational roots of \(a^d+a\) are \(0,-1\) for even \(d\), and only \(0\) for odd \(d\). Rational roots of \(b^d-1\) are \(\pm1\) for even \(d\), and only \(1\) for odd \(d\), giving the stated rational-point counts.

**4. Intersections and lattice.** Lines in the same \(a\)-row meet at \([a:1:0:0]\); lines in the same \(b\)-column meet at \([0:0:b:1]\); if neither parameter agrees, their spanning two-dimensional linear subspaces of \(\mathbb Q^{4}\otimes\overline{\mathbb Q}\) are disjoint. Different lines on smooth \(S_d\) intersect transversely when they meet, so their intersection number is one. The diagonal entry is \(2-d\) by adjunction.

Order the lines as a \(d\)-by-\(d\) grid. Writing \(J_d\) for the all-ones matrix, its intersection matrix is
\[
G_d=(2-d)I_{d^2}+(J_d-I_d)\otimes I_d+I_d\otimes(J_d-I_d).
\]
The decomposition of \(\mathbb Q^d\) into the all-ones line and its sum-zero complement gives precisely the eigenvalues and multiplicities displayed above. For each fixed \(a\), the section \(x_1=a x_2\) of \(S_d\) is the union of the \(d\) row lines, with multiplicity one. Likewise \(x_3=b x_4\) cuts the \(d\) column lines. Hence every row sum and every column sum equals the ample hyperplane class \(H\). The space spanned by the line classes contains \(H\); by the Hodge index theorem the intersection form restricted to that space is nondegenerate (it is negative definite on the complement perpendicular to \(H\)). The dimension of the span therefore equals the matrix rank, namely \((d-1)^2+1\). Its \(2(d-1)\) rational relations are exactly the independent differences between row sums and between column sums.

## Verification

Execute `python check_lines.py` with Python 3 and SymPy. The exact-arithmetic checks for \(d=4,5,6\) verify the restriction identity, separability of both root forms, an explicit complete tensor eigenbasis for the intersection matrix, the rational-root counts, and the predicted dimensions. They return `VERIFY_OK`. The exhaustive classification for all \(d\ge4\), scheme-theoretic reducedness, and Néron--Severi rank follow from the preceding proofs, not from those finite checks.

## Relationship to prior work

Cheltsov and Tschinkel (arXiv:2610.07479v1, Example 3 and §2) introduce the specific sextic double solid and use rational curves of its branch surface to establish potential density. Their result does not state the complete line Hilbert scheme, the incidence matrix, or the rank of its line-class span. Poonen (arXiv:0902.3961v2, §§1--2) studies arithmetic of a related, but different, surface defined by equating two copies of a single binary form; his distinguished lines do not classify lines on this mixed-form branch surface. Page, Ryan and Smith (arXiv:2406.15868v2) prove general maximal line bounds for smooth degree-\(d\) surfaces; the bound does not determine the exact line scheme of this family. Searches using the defining equation, Fano-scheme aliases, separated-binary-form equivalence, and grid-intersection invariants did not locate an equivalent precise result. This search is not a proof of absolute priority.

## Limitations

The theorem is over characteristic zero and addresses linear curves only. It does not compute the full Néron--Severi group, possible additional divisor classes from nonlinear curves, or any birational invariant of the double solid beyond the branch-line geometry. Broad structural results on special split hypersurfaces could conceivably imply parts of this exact calculation; no absolute novelty claim is made.

## References

- I. Cheltsov and Y. Tschinkel, *Potential density of rational points on sextic double solids*, arXiv:2610.07479v1, first public 2026-10-05; especially Example 3 and §2.
- B. Poonen, *Multivariable polynomial injections on rational numbers*, arXiv:0902.3961v2, especially §§1--2.
- J. Page, T. Ryan, and K. E. Smith, *Smooth Surfaces with Maximal Lines*, arXiv:2406.15868v2.
