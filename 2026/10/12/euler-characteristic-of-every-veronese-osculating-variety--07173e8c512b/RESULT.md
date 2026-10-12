# Euler characteristic of every Veronese osculating variety
## Finding
Let
\[
n\ge1,\qquad d\ge1,\qquad 0\le k<d.
\]
Write
\[
X_{n,d}
=
v_d(\mathbb P^n)
\subset
\mathbb P(\operatorname{Sym}^d\mathbb C^{n+1})
\]
for the \(d\)-uple Veronese variety, and let
\[
O_{k,n,d}
\]
be its \(k\)-th osculating variety, the union of the \(k\)-th osculating spaces.

Then
\[
\boxed{
\chi_{\mathrm{top}}(O_{k,n,d})
=
\sum_{j=1}^{\min\{n+1,\lfloor d/(d-k)\rfloor\}}
(-1)^{j+1}
\binom{n+1}{j}
\binom{n+d-j(d-k)}{n}.
}
\]

Equivalently, the Euler characteristic is exactly the number of degree-\(d\) monomials
\[
x_0^{a_0}\cdots x_n^{a_n}
\]
for which
\[
\max_i a_i\ge d-k.
\]

In the stable range
\[
d>2k,
\]
the sets counted for different variables are disjoint, and the formula collapses to
\[
\boxed{
\chi_{\mathrm{top}}(O_{k,n,d})
=
(n+1)\binom{n+k}{n}.
}
\]

For the endpoint
\[
k=d,
\]
one has
\[
O_{d,n,d}
=
\mathbb P(\operatorname{Sym}^d\mathbb C^{n+1}),
\]
so
\[
\chi_{\mathrm{top}}(O_{d,n,d})
=
\binom{n+d}{n}.
\]

## Assumptions and scope
The base field is
\[
\mathbb C.
\]

The osculating convention is the one used in the archival source:
at a Veronese point
\[
[L^d]
\]
the \(k\)-th osculating space consists of the classes
\[
[L^{d-k}F],
\qquad
F\in\operatorname{Sym}^k\mathbb C^{n+1}.
\]
Hence
\[
O_{k,n,d}
=
\{[L^{d-k}F]\}.
\]

The theorem concerns the ordinary topological Euler characteristic of the underlying complex projective variety. It does not require smoothness or normality.

The endpoint
\[
k=d
\]
is separated because the exponent
\[
d-k
\]
vanishes and the osculating variety is the ambient projective space.

## Proof
Choose coordinates
\[
x_0,\ldots,x_n
\]
on
\[
\mathbb C^{n+1}.
\]
Fix an integer
\[
B>d
\]
and let
\[
\mathbb C^*
\]
act diagonally by
\[
z\cdot x_i=z^{B^i}x_i.
\]

A degree-\(d\) monomial
\[
x_0^{a_0}\cdots x_n^{a_n},
\qquad
\sum_i a_i=d,
\]
has weight
\[
\sum_i a_iB^i.
\]
Because
\[
0\le a_i\le d<B,
\]
base-\(B\) expansion is unique. Thus distinct degree-\(d\) monomials have distinct weights.

Consequently the fixed locus in the ambient projective space is the finite set of monomial coordinate points.

The diagonal action preserves the Veronese variety and every osculating variety. Indeed,
\[
[L^{d-k}F]
\longmapsto
[(z\cdot L)^{d-k}(z\cdot F)].
\]

Now let
\[
0\le k<d
\]
and let
\[
[M]
\]
be a monomial coordinate point. We claim that
\[
[M]\in O_{k,n,d}
\]
if and only if
\[
M
\]
is divisible by
\[
x_i^{d-k}
\]
for some
\[
i.
\]

The reverse implication is immediate: if
\[
M=x_i^{d-k}F
\]
with
\[
\deg F=k,
\]
then
\[
[M]\in O_{k,n,d}.
\]

Conversely, suppose
\[
M=L^{d-k}F
\]
for a nonzero linear form
\[
L.
\]
Since
\[
d-k>0,
\]
the linear polynomial
\[
L
\]
divides the monomial
\[
M.
\]
The polynomial ring is a unique factorization domain, and every irreducible linear factor of a monomial is associated to one of the coordinate variables. Hence
\[
L
\]
is proportional to some
\[
x_i,
\]
and therefore the exponent of
\[
x_i
\]
in
\[
M
\]
is at least
\[
d-k.
\]

It follows that the fixed locus of
\[
O_{k,n,d}
\]
is indexed by the weak compositions
\[
(a_0,\ldots,a_n)
\]
of
\[
d
\]
for which at least one coordinate satisfies
\[
a_i\ge d-k.
\]

For a chosen set of
\[
j
\]
coordinates required to satisfy this inequality, subtract
\[
d-k
\]
from each of those coordinates. The remaining sum is
\[
d-j(d-k),
\]
so the number of weak compositions is
\[
\binom{n+d-j(d-k)}{n},
\]
provided this remaining degree is nonnegative.

Inclusion-exclusion over the
\[
n+1
\]
coordinates gives
\[
\#(O_{k,n,d})^{\mathbb C^*}
=
\sum_{j=1}^{\min\{n+1,\lfloor d/(d-k)\rfloor\}}
(-1)^{j+1}
\binom{n+1}{j}
\binom{n+d-j(d-k)}{n}.
\]

For any complex algebraic variety
\[
Y
\]
with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One proof removes the fixed locus and refines a Rosenlicht stratification by stabilizer type; every nonfixed stratum fibers with fiber a finite quotient of
\[
\mathbb C^*,
\]
whose compactly supported Euler characteristic is zero.

Since
\[
O_{k,n,d}
\]
is projective,
\[
\chi_{\mathrm{top}}(O_{k,n,d})
=
\chi_c(O_{k,n,d})
=
\#(O_{k,n,d})^{\mathbb C^*},
\]
which proves the formula.

If
\[
d>2k,
\]
then
\[
2(d-k)>d.
\]
Therefore no degree-\(d\) monomial can have two distinct exponents both at least
\[
d-k.
\]
Only the
\[
j=1
\]
term survives, giving
\[
(n+1)\binom{n+k}{n}.
\]

## Verification
The bundled checker enumerates all degree-\(d\) monomials for
\[
1\le n\le5,
\qquad
1\le d\le10,
\qquad
0\le k<d.
\]

For every triple it independently:
- counts monomials satisfying
  \[
  \max_i a_i\ge d-k;
  \]
- evaluates the inclusion-exclusion formula;
- verifies equality with the stable closed form whenever
  \[
  d>2k;
  \]
- verifies that the base-\((d+1)\) monomial weights are pairwise distinct.

The finite computation is regression evidence only. The all-parameter theorem is proved symbolically above.

## Relationship to prior work
Bernardi, Catalisano, Gimigliano, and Idà define exactly the varieties
\[
O_{k,n,d}
\]
used here and prove that
\[
O_{k,n,d}
=
\{[L^{d-k}F]\}.
\]
Their paper studies dimensions and higher secant defectivity through inverse systems and Hilbert functions.

The inspected full text contains no occurrence of “Euler,” “Poincaré,” or “topolog.” Its use of “fixed” is unrelated to torus-fixed-point topology.

The case
\[
k=1,\qquad d\ge3,
\]
specializes to the tangential Veronese formula
\[
\chi_{\mathrm{top}}=(n+1)^2.
\]
The present theorem is not merely that specialization: it gives an exact formula for every osculating order, including the overlap regimes
\[
d\le2k
\]
where multiple coordinate divisibility conditions interact and inclusion-exclusion is genuinely necessary.

Targeted searches for Euler characteristic, Poincaré polynomial, motivic formulas, monomial fixed points, and equivalent osculating-Veronese formulations did not locate this all-parameter formula.

## Limitations
Ordinary Euler characteristic is coarse. The theorem does not determine Betti numbers, mixed Hodge structure, singularities, degree, defining equations, or the defectivity of higher secant varieties.

The argument uses only diagonal torus symmetry and unique factorization, so an older unindexed or folklore observation remains a residual originality risk.

The formula concerns the osculating variety itself. It does not compute Euler characteristics of its higher secant varieties.

## References
A. Bernardi, M. V. Catalisano, A. Gimigliano, and M. Idà, *Osculating Varieties of Veronesean and their higher secant varieties*, arXiv:math/0403132, first submitted 8 March 2004; published as *Osculating Varieties of Veronese Varieties and Their Higher Secant Varieties*, *Canadian Journal of Mathematics* 59 (2007), 488--502, DOI 10.4153/CJM-2007-021-6.

E. Ballico and C. Fontanari, *On the secant varieties to the osculating variety of a Veronese surface*, *Central European Journal of Mathematics* 1 (2003), 315--326, DOI 10.2478/BF02475212.
