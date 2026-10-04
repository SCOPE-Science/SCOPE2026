# Sharp automorphism-dimension bounds in the two-heavy weighted-projective family
## Finding
For every integer \(r\ge2\), let \(X_{r,a,b}=\mathbb P(1^r,a,b)\) with \(1\le a\le b\). Among the canonical members, \(\dim\operatorname{Aut}(X_{r,a,b})\) is maximized uniquely at \((a,b)=(2r,3r)\), with value \(r^2+\binom{3r-1}{r-1}+\binom{4r-1}{r-1}+\binom{2r-1}{r-1}+1\). Among the terminal members, for \(r=2\) the maximum is \(15\), attained exactly at \((1,1)\) and \((1,2)\); for every \(r\ge3\) it is attained uniquely at \((2r-2,3r-3)\), with value \(r^2+\binom{3r-3}{r-1}+\binom{4r-4}{r-1}+\binom{2r-2}{r-1}+1\).

Thus the most symmetric canonical member in this family is always the outer corner of the canonical parameter triangle. Except in dimension three of the weighted projective space itself (the case \(r=2\)), the terminal maximum is likewise the outer corner of the terminal triangle.

## Assumptions and scope
The base field is \(\mathbb C\), \(r\ge2\), and \(1\le a\le b\). The automorphism group is the algebraic automorphism group of the underlying weighted projective variety, and \(\dim\operatorname{Aut}(X)\) means its algebraic-group dimension; finite components do not affect this dimension. The result concerns ordinary weighted projective spaces, not fake weighted projective spaces.

## Proof
Put
\[
B_r(m)=\binom{r+m-1}{r-1}\qquad(m\ge0).
\]
Let \(S=\mathbb C[x_1,\ldots,x_r,y,z]\) be the Cox ring, with weights \(1,\ldots,1,a,b\). Cox's automorphism theorem for complete simplicial toric varieties says that the covering automorphism group has dimension equal to the sum, over Cox variables, of the dimensions of the homogeneous pieces having the corresponding variable degrees. For weighted projective space the grading group has one-dimensional torus \(G\cong\mathbb C^\times\), so
\[
\dim\operatorname{Aut}X
 =r\dim S_1+\dim S_a+\dim S_b-1. \tag{1}
\]
This also follows directly by counting the possible homogeneous images of each Cox variable and then quotienting by the grading torus.

Assume first that \(1<a<b\), and put \(d=b-a\). Since \(S_a\) consists of the \(B_r(a)\) unit-variable monomials together with \(y\), while \(S_b\) consists of \(z\) and the monomials \(y^j\) times a unit-variable monomial of residual degree \(b-ja\), equation (1) gives
\[
\dim\operatorname{Aut}X
=r^2+B_r(a)+B_r(a+d)+
\sum_{k=0}^{\lfloor d/a\rfloor} B_r(d-ka)+1. \tag{2}
\]
For the equal-heavy-weight and unit-heavy-weight cases one similarly gets
\[
\dim\operatorname{Aut}\mathbb P(1^r,a,a)=r^2+2B_r(a)+3\quad(a>1), \tag{3}
\]
\[
\dim\operatorname{Aut}\mathbb P(1^r,1,b)=(r+1)^2+\binom{r+b}{r}\quad(b>1), \tag{4}
\]
and \(\dim\operatorname{Aut}\mathbb P(1^{r+2})=(r+2)^2-1\).

For this two-heavy family, the Reid--Tai age inequalities reduce to
\[
0\le d\le r,\qquad 1\le a\le r+d \tag{5}
\]
for canonicity, and
\[
0\le d<r,\qquad 1\le a<r+d \tag{6}
\]
for terminality. These are obtained by applying the age test on the two heavy affine charts \(\frac1a(1^r,b)\) and \(\frac1b(1^r,a)\); the verification script independently checks the age sums against (5)--(6).

We maximize (2) over the canonical triangle. If \(a>d\), then \(\lfloor d/a\rfloor=0\), so
\[
\dim\operatorname{Aut}X=r^2+B_r(a)+B_r(a+d)+B_r(d)+1.
\]
By (5),
\[
a\le2r,\qquad a+d\le3r,\qquad d\le r.
\]
Since \(B_r\) is strictly increasing, this is at most
\[
r^2+B_r(2r)+B_r(3r)+B_r(r)+1,
\]
with equality only when \(d=r\) and \(a=2r\), hence only at \((a,b)=(2r,3r)\).

If instead \(a\le d\), then \(a\le r\), \(a+d\le2r\), and
\[
\sum_{k=0}^{\lfloor d/a\rfloor}B_r(d-ka)
\le\sum_{m=0}^d B_r(m)
=\binom{r+d}{r}
\le\binom{2r}{r}.
\]
Therefore
\[
\dim\operatorname{Aut}X
\le r^2+B_r(r)+B_r(2r)+\binom{2r}{r}+1.
\]
For every \(r\ge2\),
\[
\binom{2r}{r}<B_r(3r)=\binom{4r-1}{r-1}.
\]
Indeed, writing both binomial coefficients as products, the ratio of the latter to the former is
\[
\frac12\prod_{i=1}^{r-1}\frac{3r+i}{r+i}>1,
\]
because every displayed factor is greater than \(2\). Hence this case is strictly below the claimed canonical maximum. The cases \(a=b\) follow from (3), and \(a=1\) from (4); their canonical bounds \(a\le r\) and \(b\le r+1\) give strictly smaller values. For (4), \(r=2\) is checked directly, while for \(r\ge3\) one uses \(\binom{4r-1}{r-1}\ge\binom{2r+1}{r}\) together with \(B_r(2r)+B_r(r)>2r\). This proves the canonical statement.

The terminal argument is the same with the strict triangle (6). For \(r\ge3\), if \(a>d\), then
\[
a\le2r-2,\qquad a+d\le3r-3,\qquad d\le r-1,
\]
so (2) is maximized uniquely at \(d=r-1\), \(a=2r-2\), i.e. \((a,b)=(2r-2,3r-3)\). If \(a\le d\), then
\[
\sum_{k=0}^{\lfloor d/a\rfloor}B_r(d-ka)
\le\binom{2r-1}{r}
<\binom{4r-4}{r-1}=B_r(3r-3),
\]
where the strict inequality follows because \(\binom{2r-1}{r}=\binom{2r-1}{r-1}\) and the upper argument on the right is larger. The cases \(a=b\) are again smaller by (3). For \(a=1\), formula (4) and \(b\le r\) give an upper bound \((r+1)^2+\binom{2r}{r}\); for \(r\ge3\),
\[
\binom{4r-4}{r-1}>\binom{2r}{r},
\]
as follows from
\[
\frac12\prod_{i=1}^{r-1}\frac{3r-3+i}{r+i}>1,
\]
since each factor exceeds \(3/2\). The remaining positive terms in the candidate formula dominate the difference \((r+1)^2-r^2\), so the inequality is strict.

Finally, when \(r=2\), the terminal triangle contains only \((1,1),(1,2),(2,3)\). Their automorphism-group dimensions are respectively \(15,15,14\), proving the stated exceptional equality case.

Substituting \(a=2r,b=3r\) and \(a=2r-2,b=3r-3\) into (2) gives exactly the two displayed closed formulas.

## Verification
The standalone script `verify_aut_dimension_bounds.py` recomputes homogeneous-piece dimensions directly from weighted monomial counts, compares the triangle criteria with the full Reid--Tai age inequalities, and exhaustively checks the stated maxima and equality cases for \(2\le r\le80\). It also checks the closed formulas. The script prints `VERIFY_OK`. This finite calculation is a regression check only; the all-dimensional result rests on the inequalities above.

## Relationship to prior work
Cox's homogeneous-coordinate-ring theorem gives the general toric automorphism-group formula used in (1), and explicitly identifies the Cox ring of weighted projective space with its weighted polynomial ring. Kasprzyk gives general canonical and terminal criteria and classifications for weighted projective spaces. The result here combines those general ingredients with the special two-heavy parameter triangle to obtain sharp, all-dimensional automorphism-dimension bounds and exact equality cases. Targeted searches for automorphism dimension together with canonical or terminal weighted projective spaces, and for the candidate weight patterns \(2r,3r\) and \(2r-2,3r-3\), did not locate an equivalent theorem. The closest indexed weighted-projective published-finding corpus item concerns reflexive weighted-projective four-simplices and \(h^*\)-vectors, not automorphism groups.

## Limitations
The theorem is specialized to ordinary weighted projective spaces with exactly two possibly non-unit weights. It does not optimize automorphism dimension over all canonical or terminal weighted projective spaces, over fake weighted projective spaces, or in positive characteristic. Originality is supported by the documented searches and source comparisons rather than by an exhaustive proof that no equivalent statement exists under different notation.

## References
1. D. A. Cox, *The Homogeneous Coordinate Ring of a Toric Variety*, arXiv:alg-geom/9210008, first submitted 1992-10-22; J. Algebraic Geom. 4 (1995), 17--50. Section 4, especially Theorem 4.2.
2. A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029, first posted 2013-04-10.
