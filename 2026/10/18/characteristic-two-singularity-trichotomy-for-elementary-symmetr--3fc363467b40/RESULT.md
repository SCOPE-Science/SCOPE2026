# Characteristic-two singularity trichotomy for elementary symmetric cubic hypersurfaces

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), let \(n\ge4\), and put \(F=e_3(x_1,\ldots,x_n)=\sum_{i<j<\ell}x_i x_jx_\ell\). The projective hypersurface \(X_n=V(F)\subset\mathbb P_k^{n-1}\) is geometrically integral, normal, Cohen--Macaulay, and Gorenstein. Its complete **reduced** singular locus has the following all-rank classification.

If \(n\not\equiv2\pmod4\), the singular locus consists of the distinct isolated points \([\mathbf1_I]\), where \(I\subseteq\{1,\ldots,n\}\) and \(|I|\equiv1\pmod4\). Here \(\mathbf1_I\) has coordinates \(1\) on \(I\) and \(0\) elsewhere. There are exactly \(\sum_{\substack{1\le r\le n\\r\equiv1\ (4)}}\binom nr\) such points, and every point is an ordinary quadratic double point (its projectivized quadratic tangent cone is smooth over \(k\)).

If \(n\equiv2\pmod4\), the reduced singular locus is a union of projective lines \(L_{I\mid I^c}\), indexed by unordered two-block partitions \(I\mid I^c\) with both block cardinalities congruent to \(1\) modulo \(4\). The line is the set of points whose coordinates are constant on each block. The number of distinct lines is
\[
\frac12\sum_{\substack{1\le r<n\\r\equiv1\ (4)}}\binom nr.
\]
Every pair of distinct lines meets only at the diagonal point \(\Delta=[1:\cdots:1]\). Away from \(\Delta\), each line is a smooth singular stratum with nondegenerate transverse quadratic tangent cone. At \(\Delta\), the hypersurface has multiplicity exactly \(3\), and its affine chart germ is the homogeneous cubic cone given by \(e_3(y_1,\ldots,y_{n-1})=0\). In particular the singular locus jumps from a finite set to a highly reducible one-dimensional arrangement precisely when \(n\equiv2\pmod4\).

## Assumptions and scope

All singular loci refer to geometric points over an algebraically closed field of characteristic \(2\), and the asserted union is a statement about the underlying reduced algebraic subset, not equality with the possibly nonreduced Jacobian scheme. The statement holds for every integer \(n\ge4\), with no restriction on whether \(k\) is the algebraic closure of a finite field. An ordinary quadratic double point means that the leading quadratic form defines a smooth quadric in the projectivized tangent space, including the odd-dimensional characteristic-two convention.

## Proof

Write \(S=e_1(x_1,\ldots,x_n)\) and \(E=e_2(x_1,\ldots,x_n)\). In characteristic \(2\), direct differentiation gives
\[
D_i=\frac{\partial F}{\partial x_i}=E+Sx_i+x_i^2.
\]
The singularity equations \(D_1=\cdots=D_n=0\) force all coordinates to be roots of the single monic quadratic \(T^2+ST+E\), hence at most two distinct values. Conversely Euler's identity \(3F=\sum_i x_iD_i\), with \(3=1\) in characteristic \(2\), shows every common nonzero projective zero of all derivatives lies on \(X_n\).

Suppose first the coordinates take distinct values \(a,b\), occurring \(r,s=n-r\) times. Subtracting two derivative equations gives \((a+b)(S+a+b)=0\); hence \(S=a+b\). But \(S=ra+sb\) modulo \(2\), so
\[
(r+1)a+(s+1)b=0.
\]
If \(n\) is odd, exactly one of \(r,s\) is odd; the other value is forced to vanish. Writing \(r\) for the number of nonzero coordinates then gives \(D_i=\binom{r-1}{2}a^2\) at nonzero coordinates and \(D_j=\binom r2 a^2\) at zeros. Both vanish exactly when \(r\equiv1\pmod4\). If \(n\) is even, \(r,s\) must be odd (the case both even forces \(a=b\)). For odd \(r,s\), the common derivative equation is
\[
0=\epsilon_r a^2+\epsilon_s b^2,\qquad \epsilon_t=\begin{cases}0&t\equiv1\pmod4,\\1&t\equiv3\pmod4.\end{cases}
\]
When \(n\equiv0\pmod4\), the two residues are \(1\) and \(3\), forcing the value belonging to the \(3\)-block to be zero and leaving precisely the indicated binary projective points. When \(n\equiv2\pmod4\), the residues agree: both \(3\) forces \(a=b\), whereas both \(1\) imposes no further restriction, yielding the stated projective lines.

For the one-value case, every nonzero projective vector is \(\Delta\). Its derivatives vanish exactly when \(\binom{n-1}{2}\) is even, equivalently \(n\equiv1,2\pmod4\). In the first case \(\Delta=[\mathbf1_{\{1,\ldots,n\}}]\) is already in the finite list. In the second case it belongs to every listed line. Distinct unordered bipartitions give distinct lines, because their defining two-dimensional vector subspaces are equal only when the indicator vectors differ by addition of the all-ones vector. Every two different such subspaces meet in the all-ones direction. This gives the exact component counts and intersections.

At a binary point \([\mathbf1_I]\) with \(r=|I|\equiv1\pmod4\), choose a nonzero coordinate as affine pivot. The quadratic part of the local equation splits as \(e_2\) on the \(r-1\) remaining coordinates of \(I\) plus \(e_2\) on the \(s=n-r\) complementary coordinates. The polar form of \(e_2\) in \(m\) variables has rank \(m\) when \(m\) is even and \(m-1\) when \(m\) is odd. If \(n\) is odd, both \(r-1\) and \(s\) are even, so the polar form is nonsingular. If \(n\equiv0\pmod4\), then \(s\equiv3\pmod4\): its one-dimensional polar radical consists of equal complementary coordinates, where \(e_2\) takes value \(\binom s2=1\) in \(k\). Thus the quadratic projective tangent cone is smooth in both finite cases. When \(n\equiv2\pmod4\), \(s\equiv1\pmod4\), and the quadratic form has exactly one projective radical direction with value zero, tangent to the singular line. Its transverse polar form has full rank \(n-2\), proving the transverse quadratic assertion. Any other non-diagonal point on the same line has identical transverse rank by the displayed derivative and Hessian formula, since the two coordinate values remain distinct.

Finally, if \(n\equiv2\pmod4\), the binomial coefficients \(n-2\), \(\binom{n-1}{2}\), and \(\binom n3\) vanish modulo \(2\). The elementary-symmetric translation formula therefore gives \(F(x_1+c,\ldots,x_n+c)=F(x_1,\ldots,x_n)\) for every scalar \(c\). In the affine chart \(x_n=1\), translating the remaining coordinates by \(1\) gives the exact local equation \(e_3(y_1,\ldots,y_{n-1})=0\) at \(\Delta\). It has exact multiplicity \(3\).

The singular locus has dimension at most \(1\), while \(\dim X_n=n-2\). Since \(n\ge4\), the singular locus has codimension at least \(2\) inside the hypersurface. Moreover \(F\) has smooth points: take exactly two nonzero coordinates equal to \(1\); a derivative with respect to any third coordinate is \(1\). Any nontrivial factorization of \(F\) would yield a codimension-one singular intersection of distinct projective hypersurface factors, and any repeated factor would make every point singular. Both are impossible by the established singular dimension bounds. Hence \(F\) is geometrically irreducible and reduced. Serre's criterion (\(R_1\) and \(S_2\)) now proves normality, and the hypersurface property gives Cohen--Macaulay and Gorenstein.

## Verification

The standalone script `verify.py` exhaustively enumerates projective points over \(\mathbb F_4\) for \(4\le n\le7\), computes each derivative using native finite-field multiplication, and compares the full resulting singular set with the predicted binary points or two-block lines. It obtains respectively \(4,6,25,28\) projective singular points over \(\mathbb F_4\), all matching the classification. For \(n=6\), six lines each have five \(\mathbb F_4\)-points and one common diagonal point, so the total is \(6(5-1)+1=25\). The checker returns `VERIFY_OK`. These finite cases test but do not prove the all-rank assertion; the symbolic argument above supplies its proof.

## Relationship to prior work

Cafure, Matera and Privitelli (first public version 2011-09-10, arXiv:1109.2265v1), especially their Theorem 3.1 and derivative identity (8), establish that singular points of general symmetric hypersurfaces with a smooth polynomial in the first \(d\) elementary symmetric functions have at most \(d-1\) distinct coordinate values and give a general singular-locus dimension bound. Taking \(d=3\) and the polynomial \(e_3\) recovers the two-value constraint used here, but the cited theorem does not imply which multiplicity patterns survive in characteristic \(2\), the mod-four trichotomy, the exact component counts, or the tangent-cone types. The four-variable Cayley cubic is classical; the general classification claimed here begins with its all-rank extension, not with a claim that its four nodes are new. Published comparisons and index searches located no statement covering the full classification, but incomplete indexing and alternative formulations remain originality risks.

## Limitations

No claim is made about the nonreduced Jacobian singular scheme, full resolution graphs, or mixed-characteristic simultaneous deformations. The local tangent-cone statement at non-diagonal line points is transverse, not a claim of a globally trivial product germ. The novelty assessment is based on accessible primary literature and searches rather than an exhaustive database proof; independent mathematical review has not been performed.

## References

1. A. Cafure, G. Matera, M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed–Solomon codes*, arXiv:1109.2265v1, posted 2011-09-10, https://arxiv.org/pdf/1109.2265 . Relevant full text: Section 3, Theorem 3.1, equation (8), and Section 4.
2. A. Cayley, *A Memoir on Cubic Surfaces*, Philosophical Transactions of the Royal Society of London (1869). Classical four-variable case; used for context, not as a source for the positive-characteristic all-rank statement.
