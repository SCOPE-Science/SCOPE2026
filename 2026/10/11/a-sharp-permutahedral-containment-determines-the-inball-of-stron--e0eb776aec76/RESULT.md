# A sharp permutahedral containment determines the inball of strong rectangulotopes
## Finding
For every integer
\[
n\ge3,
\]
let
\[
\mathrm{SR}(n)\subset\mathbf1^\perp\subset\mathbb R^n
\]
be the strong rectangulotope in the explicit realization of Cardinal and Pilaud.

For each nonempty proper subset
\[
X\subset[n],
\]
write \(f_n(X)\) for the right-hand side of its facet inequality
\[
x(X)\le f_n(X).
\]
The source gives
\[
f_n(X)
=
\#\{(I,J):I\not\subseteq[n]\setminus X,\ J\not\subseteq X\}
+
\#\{(I,J):I\not\subseteq X,\ J\not\subseteq[n]\setminus X\},
\tag{1}
\]
where \(I,J\) range over nonempty consecutive intervals with
\[
\max I=\min J-1.
\]

Then
\[
\boxed{
f_n(X)\ge
\frac n2\,|X|\bigl(n-|X|\bigr).
}
\tag{2}
\]
Equality in (2) holds if and only if \(X\) is a nonempty proper prefix or suffix of \([n]\).

Let
\[
\mathrm{Perm}_0(n)
\]
denote the classical permutahedron translated to \(\mathbf1^\perp\). Its upper subset facets are
\[
x(X)\le\frac12|X|\bigl(n-|X|\bigr).
\]
Thus (2) is exactly the sharp containment
\[
\boxed{
n\,\mathrm{Perm}_0(n)\subseteq\mathrm{SR}(n).
}
\tag{3}
\]

The exact intrinsic Euclidean inradius is
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathrm{SR}(n)\bigr)
=
\frac n2\sqrt{n(n-1)}.
}
\tag{4}
\]
The origin is an incenter. Its radius-\(r_{\mathrm{in}}\) ball is tangent exactly to the four facets indexed by
\[
\boxed{
\{1\},\quad
\{n\},\quad
[n-1],\quad
\{2,\ldots,n\}.
}
\tag{5}
\]

The complete incenter set has affine dimension
\[
\boxed{
\dim\mathcal I(\mathrm{SR}(n))=n-3.
}
\tag{6}
\]
Hence the incenter is unique for \(n=3\), while every \(n\ge4\) has a positive-dimensional family of optimal centers.

## Assumptions and scope
The strong rectangulotope is the realization from *Rectangulotopes*, not an arbitrary affine realization of the same normal fan or face lattice.

The ambient Euclidean structure is the standard one on \(\mathbb R^n\), restricted to the affine span
\[
\mathbf1^\perp=
\left\{
x:\sum_i x_i=0
\right\}.
\]

The theorem is stated for \(n\ge3\). It determines the inradius, the contact facets of the centered optimal ball, and the affine dimension of the entire incenter set. It does not determine the full vertex-distance spectrum, circumradius, or John ellipsoid.

## Proof
The source proves that every nonempty proper \(X\subset[n]\) defines an irredundant facet of \(\mathrm{SR}(n)\), with the height in (1).

We first prove the sharp lower bound (2).

Encode \(X\) by its binary word on \([n]\), and let
\[
\ell_1,\ldots,\ell_r
\]
be the lengths of its maximal monochromatic runs. Put
\[
T_n=\sum_{a=1}^{n-1}a(n-a)
=
\frac{n(n^2-1)}6
\]
and
\[
\Phi_n(t)
=
\frac{t(t+1)(3n-t-2)}6.
\tag{7}
\]

For a fixed cut between \(a\) and \(a+1\), there are \(a(n-a)\) adjacent interval pairs \((I,J)\). Applying inclusion--exclusion to the two conditions in (1), and then summing over all cuts, gives
\[
\boxed{
f_n(X)
=
2T_n
-
\sum_{j=1}^r\Phi_n(\ell_j)
+
\sum_{j=1}^{r-1}\ell_j\ell_{j+1}.
}
\tag{8}
\]
For completeness, the contribution of one monochromatic run of length \(\ell\), beginning after \(s\) coordinates, to the two exclusion sums is
\[
\sum_{t=1}^{\ell}
\left[
t(n-s-t)
+
(s+t-1)(\ell-t+1)
\right]
=
\Phi_n(\ell),
\]
so its position disappears. At each boundary between two runs, inclusion--exclusion restores the product of the two adjacent run lengths, giving the last term in (8).

Let the \(X\)-runs have lengths
\[
a_1,\ldots,a_p
\]
and the complementary runs have lengths
\[
b_1,\ldots,b_q.
\]
Set
\[
k=\sum_i a_i=|X|,
\qquad
\ell=\sum_j b_j=n-k,
\]
and let \(A\) be the sum of products of adjacent opposite-color run lengths in the binary word.

For a two-run word of lengths \(k,\ell\), equation (8) gives
\[
2T_n-\Phi_n(k)-\Phi_n(\ell)+k\ell
=
\frac n2k\ell.
\tag{9}
\]
The elementary merge identity
\[
\Phi_n(u+v)-\Phi_n(u)-\Phi_n(v)
=
\frac{uv(2n-2-u-v)}2
\tag{10}
\]
shows that splitting a color class into several runs can only increase the first two terms of the difference from (9).

More precisely, if \(p\ge2\), sequentially merging the \(a_i\) gives
\[
\Phi_n(k)-\sum_i\Phi_n(a_i)
\ge
\ell\sum_{i<j}a_i a_j,
\tag{11}
\]
because every intermediate merged total is at most \(k\), so the coefficient in (10) is at least \(\ell\). Similarly,
\[
\Phi_n(\ell)-\sum_j\Phi_n(b_j)
\ge
k\sum_{i<j}b_i b_j.
\tag{12}
\]

Subtracting (9) from (8) yields
\[
f_n(X)-\frac n2k\ell
=
\left(
\Phi_n(k)-\sum_i\Phi_n(a_i)
\right)
+
\left(
\Phi_n(\ell)-\sum_j\Phi_n(b_j)
\right)
-
(k\ell-A).
\tag{13}
\]

If one color has a single run, alternation forces the other color to have at most two runs. If it has two, every opposite-color run pair is adjacent, so \(A=k\ell\), while the corresponding split term in (11) or (12) is strictly positive.

If both colors have at least two runs, then
\[
\sum_{i<j}a_i a_j\ge k-1,
\qquad
\sum_{i<j}b_i b_j\ge \ell-1.
\]
Consequently the first two terms on the right of (13) are at least
\[
\ell(k-1)+k(\ell-1)
=
2k\ell-k-\ell
\ge
k\ell,
\]
while
\[
k\ell-A<k\ell
\]
because \(A>0\). Thus (13) is strictly positive.

Therefore equality in (2) occurs exactly when both colors have one run, meaning precisely that \(X\) is a prefix or suffix. This proves (2)--(3).

Now let
\[
|X|=k.
\]
Inside \(\mathbf1^\perp\), the projected normal of the facet \(x(X)=f_n(X)\) is
\[
\mathbf1_X-\frac kn\mathbf1,
\]
with norm
\[
\sqrt{\frac{k(n-k)}n}.
\tag{14}
\]
At the origin, (2) and (14) give the facet-distance lower bound
\[
\frac{f_n(X)}{\sqrt{k(n-k)/n}}
\ge
\frac n2\sqrt{nk(n-k)}
\ge
\frac n2\sqrt{n(n-1)}.
\tag{15}
\]
Equality in both inequalities occurs exactly for a prefix or suffix of cardinality \(1\) or \(n-1\), giving precisely the four facets in (5). Hence the centered ball of radius (4) is contained in \(\mathrm{SR}(n)\).

To prove optimality, use the two opposite endpoint facets
\[
x_1\le\frac{n(n-1)}2,
\qquad
-x_1\le\frac{n(n-1)}2.
\]
If a radius-\(\rho\) ball centered at \(c\in\mathbf1^\perp\) lies in the polytope, then
\[
\frac{n(n-1)}2-c_1
\ge
\rho\sqrt{\frac{n-1}{n}},
\]
and
\[
\frac{n(n-1)}2+c_1
\ge
\rho\sqrt{\frac{n-1}{n}}.
\]
Adding gives
\[
\rho\le
\frac n2\sqrt{n(n-1)}.
\]
Thus (4) is exact. Equality forces \(c_1=0\). The analogous endpoint pair at coordinate \(n\) forces \(c_n=0\).

At the optimal radius, all remaining facet inequalities have strict slack at the origin by (15). Therefore the full incenter set is contained in
\[
\mathbf1^\perp\cap\{c_1=0,\ c_n=0\},
\]
and contains a relative neighborhood of the origin in this subspace. Its affine dimension is therefore \(n-3\), proving (6).

## Verification
The proof is symbolic and valid for every \(n\ge3\).

The source-dependent premises were inspected directly in the full text and page image: Theorem 3 gives the affine equation and all subset-facet heights, while Lemma 19 states that the submodular description is irredundant.

The accompanying `verify.py` checks every nonempty proper subset for
\[
3\le n\le14.
\]
It independently counts the adjacent interval pairs in the source formula, verifies the run-length identity (8), the sharp lower bound (2), its equality classification, and the four centered contact facets. This finite computation is corroborative only.

## Relationship to prior work
Cardinal and Pilaud introduce the weak and strong rectangulotopes as quotientopes encoding flip graphs of rectangulations and give explicit vertex and facet descriptions. They emphasize that the strong rectangulotope ceases to be combinatorially equivalent to the permutahedron once \(n>4\). Their paper does not state an inradius, Chebyshev-center, or Euclidean facet-distance theorem.

The later literature on simple congruences of the weak order uses the strong rectangulotope as an important example and studies its combinatorial vertices and faces, not its Euclidean inball.

The new inequality (2) compares the full strong-rectangulotope facet function with the cardinality-only permutahedral facet function and is stronger than merely computing one radius: it gives the sharp containment (3), identifies every equality facet, and explains why a non-permutahedral family retains a simple permutahedral-scale inradius.

Targeted published-result and literature searches under “strong rectangulotope”, “rectangulotope”, “inradius”, “Chebyshev center”, “Euclidean facet distance”, and “inscribed ball” did not locate a theorem implying (2)--(6).

## Limitations
The theorem concerns the explicit strong-rectangulotope realization from the cited source. Other quotientopes with the same normal fan can have different metric geometry.

The incenter is not unique for \(n\ge4\); only its affine dimension and the contact set of the centered optimal ball are determined here. The exact boundary of the complete incenter polytope is not simplified beyond the shifted source inequalities.

The run-fragmentation inequality is elementary once the source facet count is rewritten in the form (8), so an equivalent observation under binary-run or submodular-function terminology remains a residual originality risk. Search nonappearance is not treated as a formal novelty certificate.

## References
1. Jean Cardinal and Vincent Pilaud, *Rectangulotopes*, arXiv:2404.17349, first public version 2024-04-26; European Journal of Combinatorics 125 (2025), 104090, DOI 10.1016/j.ejc.2024.104090.
2. Emily Barnard, Jean-Christophe Novelli, and Vincent Pilaud, *Separating trees and simple congruences of the weak order*, European Journal of Combinatorics 136 (2026), 104375.
