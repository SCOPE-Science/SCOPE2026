# Sharp ED-degree range for complete-intersection surfaces at fixed adjunction level
## Finding
Fix integers \(c\ge2\) and \(S\ge2c\). Let
\[
X_{\mathbf d}\subset\mathbb P^{c+2}_{\mathbb C}
\]
be a general smooth complete-intersection surface of codimension \(c\) and multidegree
\[
\mathbf d=(d_1,\ldots,d_c),\qquad d_i\ge2,\qquad \sum_{i=1}^c d_i=S.
\]
Write
\[
x_i=d_i-1,\qquad T=S-c=\sum_i x_i,\qquad Q=\sum_i x_i^2.
\]
Then its generic Euclidean distance degree is
\[
\operatorname{EDdeg}(X_{\mathbf d})
=
\left(\prod_i d_i\right)
\left(1+T+\frac{T^2+Q}{2}\right).
\]

Among all such multidegrees with fixed \(c\) and \(S\), this quantity has a unique maximum and a unique minimum up to permutation.

Write
\[
S=ck+r,\qquad 0\le r<c.
\]
The maximum occurs exactly at the balanced multidegree
\[
\underbrace{(k,\ldots,k)}_{c-r\text{ entries}},
\underbrace{(k+1,\ldots,k+1)}_{r\text{ entries}},
\]
and the minimum occurs exactly at
\[
(2,\ldots,2,S-2c+2).
\]

Thus, for fixed codimension and fixed adjunction level, balancing the defining degrees strictly increases the generic nearest-point algebraic complexity until the degrees differ by at most one, while concentrating all excess degree in a single equation strictly decreases it.

For example, among codimension-three complete-intersection surfaces with total defining degree \(12\),
\[
\operatorname{EDdeg}(2,2,8)=2432
<
\operatorname{EDdeg}(3,4,5)=3900
<
\operatorname{EDdeg}(4,4,4)=4096.
\]

## Assumptions and scope
The statement concerns general smooth complex projective complete intersections in \(\mathbb P^{c+2}\). The Euclidean distance degree is taken with respect to general projective coordinates, equivalently in the transverse-to-the-isotropic-quadric regime of the standard theory.

Fixing \(S\) is geometrically natural. Adjunction gives
\[
K_X\cong\mathcal O_X(S-c-3),
\]
so at fixed codimension the comparison is among complete-intersection surfaces with the same canonical polarization exponent.

The theorem is restricted to surfaces. The balancing behavior is dimension-sensitive: the same monotonicity need not persist unchanged for higher-dimensional complete intersections.

## Proof
Draisma, Horobeţ, Ottaviani, Sturmfels, and Thomas prove that a general codimension-\(c\) complete intersection in projective space has Euclidean distance degree
\[
\left(\prod_i d_i\right)
\sum_{i_1+\cdots+i_c\le m}
\prod_{j=1}^c(d_j-1)^{i_j},
\]
where \(m\) is the projective dimension. For a surface, \(m=2\). Therefore, with \(x_i=d_i-1\),
\[
\operatorname{EDdeg}(X_{\mathbf d})
=
\left(\prod_i(x_i+1)\right)(1+h_1(x)+h_2(x)).
\]
Since
\[
h_1(x)=T
\]
and
\[
h_2(x)=\frac{T^2+Q}{2},
\]
the displayed formula follows.

It remains to optimize at fixed \(T\). Suppose two entries satisfy
\[
1\le x<y-1.
\]
Replace the pair \((x,y)\) by the more balanced pair \((x+1,y-1)\). Put
\[
\delta=y-x-1>0.
\]
Let
\[
A=1+T+h_2(x_1,\ldots,x_c)
\]
and let
\[
B=(x+1)(y+1)
\]
be the contribution of this pair to the degree product before balancing. The squared-sum term changes by
\[
Q' - Q=-2\delta,
\]
so
\[
A'=A-\delta.
\]
Meanwhile the pair product changes by the exact amount
\[
(x+2)y-(x+1)(y+1)=\delta,
\]
so \(B'=B+\delta\).

All other degree factors are unchanged. Hence the change in Euclidean distance degree has the sign of
\[
(B+\delta)(A-\delta)-BA
=
\delta(A-B-\delta).
\]
Now
\[
B+\delta=(x+2)y.
\]
Also \(h_2\) contains the three nonnegative terms \(x^2+xy+y^2\), and \(T\ge x+y\). Thus
\[
A-(x+2)y
\ge
1+x+y+x^2+xy+y^2-(x+2)y
=
1+x^2+x+y^2-y>0.
\]
Therefore every nontrivial balancing move strictly increases the Euclidean distance degree.

Repeated balancing terminates exactly when all entries \(x_i\) differ by at most one. This proves the unique maximum, namely the balanced multidegree.

For the minimum, if at least two entries exceed \(1\), move one unit from a smaller positive entry to a larger one. This is the inverse of a strict balancing move and therefore strictly decreases the Euclidean distance degree. Repeating leaves exactly \(c-1\) entries equal to \(1\), hence exactly \(c-1\) defining degrees equal to \(2\), with the remaining degree forced to be \(S-2c+2\). This proves the unique minimum.

## Verification
A standalone exact-integer checker independently evaluates the complete-intersection ED-degree formula and exhaustively verifies the sharp extrema for every
\[
2\le c\le7,
\qquad
2c\le S\le 6c.
\]
It also verifies the strict increase under every admissible elementary balancing move encountered in that range.

The bounded enumeration is regression evidence only. The infinite statement is proved by the exact pair-balancing identity above.

## Relationship to prior work
Draisma, Horobeţ, Ottaviani, Sturmfels, and Thomas introduce and develop Euclidean distance degree as the number of critical points of squared distance to a generic data point. Their Corollary 2.10 gives the complete-intersection formula, and their Chern-class derivation explicitly evaluates the generating series for a general complete intersection.

The inspected primary paper does not formulate an extremal problem at fixed total defining degree or fixed canonical polarization. A 2024 paper on Euclidean distance degree of complete intersections via Newton polytopes develops mixed-volume formulas for sparse affine complete intersections, but searches within that paper for balancing, extremal, and fixed-degree statements found no covering result.

Claim-specific searches for balanced multidegrees, fixed total degree, fixed canonical class, and extremal Euclidean distance degree did not locate the sharp maximum/minimum theorem above. The nearest indexed results concern ED-degree formulas themselves or unrelated complete-intersection invariants.

## Limitations
The theorem concerns generic ED degree, so special coordinates can lower the Euclidean distance degree through nontransversality with the isotropic quadric. It does not claim that every individual complete intersection of a given multidegree attains the generic value.

The fixed-sum hypothesis is essential to the extremal statement. Other normalizations, such as fixed product of degrees or fixed topological Euler characteristic, define different optimization problems.

The proof is specific to projective dimension two. Higher-dimensional complete intersections involve higher complete homogeneous symmetric polynomials, and the same balancing direction can change.

A residual literature risk remains that an unindexed optimization-oriented source may have observed the same balancing theorem, although no such statement was found in the inspected or searched literature.

## References
Jan Draisma, Emil Horobeţ, Giorgio Ottaviani, Bernd Sturmfels, Rekha R. Thomas, *The Euclidean Distance Degree of an Algebraic Variety*, arXiv:1309.0049, first submitted 31 August 2013; Foundations of Computational Mathematics 16 (2016), 99--149.

Nguyen Tat Thang, Pham Thu Thuy, *Euclidean distance degree of complete intersections via Newton polytopes*, arXiv:2404.17237, submitted 26 April 2024.
