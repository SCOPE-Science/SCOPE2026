# Exact Mahler profile and strict equilateral maximum for equiradial finite Lipschitz-free spaces

## Finding

For every integer \(n\ge2\) and real \(s\ge\tfrac12\), let \(M_{n,s}=\{o,v_1,\ldots,v_n\}\) carry the metric
\[
d(o,v_i)=s,\qquad d(v_i,v_j)=1\quad(i\ne j).
\]
Denote by \(P_{n,s}\) the real Lipschitz-free unit ball over \(M_{n,s}\) in the hub-based coordinates \(\sum_i x_i(\delta_{v_i}-\delta_o)\), and by \(P_{n,s}^{\circ}\) its polar for the coordinate pairing. Writing \(\operatorname{Vol}_n\) for ordinary coordinate Lebesgue volume, we obtain, for **every** such dimension and radius,
\[
\operatorname{Vol}_n(P_{n,s})
=\frac{2}{n!s^n}\sum_{j=0}^{n-1}\binom{n-1+j}{j}s^j,
\qquad
\operatorname{Vol}_n(P_{n,s}^{\circ})=2ns-n+1.
\]
Their Mahler volume product is therefore
\[
\boxed{\mathcal M_n(s)=\frac{2(2ns-n+1)}{n!s^n}
\sum_{j=0}^{n-1}\binom{n-1+j}{j}s^j.}
\]
Moreover, its **complete shape** is determined by the exact positive-coefficient factorization
\[
\boxed{\mathcal M_n'(s)=\frac{2(1-s)}{n!s^{n+1}}
\sum_{j=0}^{n-2}(n-j)(n-j-1)\binom{n-1+j}{j}s^j.}
\]
Thus the product strictly increases on \([\tfrac12,1]\), strictly decreases on \([1,\infty)\), and has its **unique global maximum within this metric family** at the equilateral metric \(s=1\). The endpoint and limiting values are
\[
\mathcal M_n(\tfrac12)=\frac{4^n}{n!},\qquad
\mathcal M_n(1)=\frac{n+1}{n!}\binom{2n}{n},\qquad
\lim_{s\to\infty}\mathcal M_n(s)=\frac{4n}{n!}\binom{2n-2}{n-1}.
\]
The tree and equilateral endpoint volumes are known. The claim is the full continuous, dimension-uniform profile and its strict monotonicity, not a global maximization over unrelated finite metrics.

## Assumptions and scope

All spaces and functionals are real. The hub-leaf metric is well defined precisely for \(s\ge\tfrac12\), since the only restrictive triangle inequality is \(1\le2s\). The free space has dimension \(n\). Volumes are computed in the explicitly stated hub-based coordinate identification; their product is invariant under invertible linear coordinate changes. The polar uses the dual pairing for these same coordinates. No fixed Euclidean normalization is needed for a Mahler product.

The following norm identity is elementary and not asserted to be new:
\[
\left\|\sum_{i=1}^n x_i(\delta_{v_i}-\delta_o)\right\|
=\frac12\sum_{i=1}^n|x_i|+
\left(s-\frac12\right)\left|\sum_{i=1}^n x_i\right|.
\]
Indeed, if the total positive and negative leaf masses are \(p\) and \(q\), moving \(\min(p,q)\) directly from negative leaves to positive leaves and the imbalance \(|p-q|\) via the hub costs \(\min(p,q)+s|p-q|\). The reverse inequality follows from dual Lipschitz potentials: for \(p\ge q\), assign \(s\) to positive leaves and \(s-1\) to negative leaves, with hub value zero; these potentials are admissible exactly when \(s\ge\tfrac12\). Reverse signs when \(q>p\).

Consequently
\[
P_{n,s}=\operatorname{conv}\{\pm e_i/s,\ \pm(e_i-e_j):1\le i\ne j\le n\},
\qquad
P_{n,s}^{\circ}=\{f\in\mathbb R^n:|f_i|\le s,\ |f_i-f_j|\le1\}.
\]
The listed primal points need not all be vertices at degenerate parameters; the convex-hull description and volume calculation remain valid.

## Proof

**1. The dual volume.** The second description makes \(P_{n,s}^{\circ}\) the set of \(n\) points in an interval of length \(L=2s\ge1\) whose range is at most one. For \(n\ge2\), prescribing distinct coordinates as minimum and maximum, the volume density at range \(r\in(0,1)\) is \(n(n-1)(L-r)r^{n-2}\). Integrating and using \(L\ge1\) gives
\[
\operatorname{Vol}_n(P_{n,s}^{\circ})
=n(n-1)\int_0^1(L-r)r^{n-2}\,dr=nL-(n-1)=2ns-n+1.
\]
Boundaries with tied extrema have measure zero; the argument includes \(L=1\).

**2. The primal volume, decomposed by signs.** Fix an orthant with \(k\) strictly positive coordinates and \(\ell=n-k\) strictly negative coordinates. For \(1\le k,\ell\le n-1\), write \(p\) and \(q\) for the positive and negative mass totals. The Lebesgue density in these two totals is
\[
\frac{p^{k-1}q^{\ell-1}}{(k-1)!(\ell-1)!}\,dp\,dq.
\]
In the half-region \(p\ge q\), put \(p=a+b\), \(q=b\). The norm constraint becomes \(sa+b\le1\). By expanding \((a+b)^{k-1}\) and using
\[
\int_{a,b\ge0,\,sa+b\le1}a^j b^{n-2-j}\,da\,db
=\frac{j!(n-2-j)!}{n!s^{j+1}},
\]
the contribution of that half-region in this fixed orthant is
\[
\frac1{n!}\sum_{j=0}^{k-1}
\frac{(n-2-j)!}{(k-1-j)!(\ell-1)!\,s^{j+1}}.
\]
The other half-region interchanges \(k\) and \(\ell\). Summing over the \(\binom nk\) orthants of each type, and using the symmetry between the two half-regions, gives for all mixed-sign orthants together
\[
\frac{2}{n!}\sum_{j=0}^{n-2}\frac1{s^{j+1}}
\sum_{k=j+1}^{n-1}\binom nk\binom{n-2-j}{k-1-j}.
\]
Vandermonde's identity evaluates the inner sum to \(\binom{2n-2-j}{n-1-j}\). The two pure-sign orthants are simplices of combined volume \(2/(n!s^n)\). Consequently
\[
\operatorname{Vol}_n(P_{n,s})
=\frac2{n!s^n}\left[1+
\sum_{j=0}^{n-2}\binom{2n-2-j}{n-1-j}s^{n-1-j}\right]
=\frac2{n!s^n}\sum_{j=0}^{n-1}\binom{n-1+j}{j}s^j.
\]
The disjointness of the orthant interiors and of the two half-regions establishes this without any approximation or incomplete enumeration.

**3. Exact derivative and strictness.** Set
\[
H(s)=\sum_{j=0}^{n-1}b_js^j,\quad
b_j=\binom{n-1+j}{j},\quad
A(s)=2ns-n+1.
\]
Direct differentiation yields
\[
\mathcal M_n'(s)=\frac2{n!s^{n+1}}\left[sA'(s)H(s)+sA(s)H'(s)-nA(s)H(s)\right].
\]
Using \((j+1)b_{j+1}=(n+j)b_j\) and comparing coefficients gives the exact polynomial identity
\[
sA'H+sAH'-nAH=(1-s)\sum_{j=0}^{n-2}
(n-j)(n-j-1)b_js^j.
\]
For \(n\ge2\), all coefficients in this last sum are strictly positive and \(s\ge\tfrac12\). The derivative thus has the sign of \(1-s\), and vanishes only at \(s=1\). This proves the asserted unique maximum and strict monotonicity on the two subintervals.

**4. Endpoints.** At \(s=\tfrac12\) the metric is a tree with half-unit arms, and the unit ball is linearly a cross-polytope, hence its volume product is \(4^n/n!\). At \(s=1\) the metric is equilateral; the known type-\(A\) root-polytope endpoint has volume product \((n+1)\binom{2n}{n}/n!\), independently recovered by evaluating the finite binomial sum. The limit at infinity follows from the leading coefficient \(b_{n-1}=\binom{2n-2}{n-1}\).

## Verification

The standalone `VERIFY.py` has two independent checks. In exact rational arithmetic, it directly integrates both orthant halves without using the collapsed Vandermonde sum and compares this with the asserted primal volume for \(2\le n\le14\) at seven rational values of \(s\), including values strictly greater than one; it also checks the polynomial derivative factorization coefficient by coefficient and both endpoints. A distinct geometric computation constructs the primal convex hull and the dual half-space polytope and compares their volumes for \(2\le n\le5\) at six radii. All exact and geometric tests passed in the reviewed package. The optional geometric computation requires NumPy and SciPy; the exact tests use only the Python standard library. Finite tests are not a proof for unbounded dimension or all real parameters: the analytic proof above is responsible for those quantifiers.

Run with `python VERIFY.py` from the directory containing the script. The optional geometric tests automatically skip if NumPy or SciPy is unavailable; for an independently complete verification one should confirm that their pass line appears.

## Relationship to prior work

Aliaga [1] classifies extreme points of Lipschitz-free unit balls over proper metric spaces, supplying the structural functional-analytic setting; his theorem does not calculate this family's continuous volumes or their product. Alexander–Fradelizi–García-Lirola–Zvavitch [2] analyze Mahler products of finite Lipschitz-free unit balls and establish the relevant equilateral and tree endpoint facts; the inspected primary text does not give the one-hub deformation profile or the strict global-in-the-family maximum. Work on the exact Euclidean Banach–Mazur distance for the *same equiradial hub-and-leaf metric* computes a different Banach-space invariant and does not imply an affine volume product. Similarly, cube–cross-polytope intersection and simplex-difference-body volume formulas concern distinct convex-body families. The novelty claim is precisely the continuous one-hub formula with its factorized derivative, not the norm identity or endpoints.

## Limitations

The theorem applies to equal leaf-pair distances and a common hub distance, not arbitrary finite metrics, unequal spokes, or any infinite-dimensional limit. The maximizing statement holds only along the specified one-parameter family; it does not assert that equilateral metrics maximize volume product over all finite metrics of the same cardinality. The product is an affine invariant, whereas the two factor volumes are reported only in the explicit coordinates. Equivalent results might exist under terminology such as deformed root polytopes or hub-augmented equilateral metrics; no absolute novelty guarantee or independent validation is asserted.

## References

[1] Ramón J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219, first public version 1 February 2021, primary MSC2020 46B20. Theorem 1 and its proof.

[2] Matthew Alexander, Matthieu Fradelizi, Luis C. García-Lirola, Artem Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public version 24 November 2019, especially its volume-product section and equilateral computation.
