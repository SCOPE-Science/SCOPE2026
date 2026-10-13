# Exact common divisor of Segre Chow and Hurwitz degrees
## Finding
Let
\[
X_{a,b}=\mathbb P^a\times\mathbb P^b
\subset
\mathbb P^{(a+1)(b+1)-1}
\]
be the Segre embedding, where
\[
a,b\ge1.
\]
Let \(C_{a,b}\) denote the degree in Pluecker coordinates of the Chow form of \(X_{a,b}\), and let \(H_{a,b}\) denote the degree in Pluecker coordinates of its Hurwitz form.

Writing
\[
d=a+b,
\]
the two degrees are
\[
C_{a,b}=\binom{d}{a}
\]
and
\[
H_{a,b}
=
\frac{2ab}{d}\binom{d}{a}
=
\frac{2(d-1)!}{(a-1)!(b-1)!}.
\]

Their exact common divisor is
\[
\boxed{
\gcd(C_{a,b},H_{a,b})
=
\frac{\binom{d}{a}\,\gcd(d,2ab)}{d}
}.
\]

In particular,
\[
\boxed{
\gcd(C_{a,b},H_{a,b})=1
}
\]
if and only if, up to exchanging the two factors,
\[
a=1
\qquad\text{and}\qquad
b\ \text{is even}.
\]

Thus among non-linear Segre varieties, arithmetic primitivity of the two consecutive associated-hypersurface degrees occurs exactly for
\[
\mathbb P^1\times\mathbb P^{2m},
\qquad
m\ge1.
\]

## Assumptions and scope
The base field is \(\mathbb C\). The embedding is the standard Segre embedding associated with
\[
\mathcal O_{\mathbb P^a\times\mathbb P^b}(1,1).
\]

The Chow degree means the degree of the Chow form in Pluecker coordinates. For an irreducible projective variety this equals its projective degree.

The Hurwitz degree is the Pluecker degree of the Hurwitz form in the sense of the higher associated hypersurface one step beyond the Chow form.

Because every Segre variety is smooth, the codimension condition on the singular locus in the general Hurwitz-degree theorem is automatic.

## Proof
Let \(A\) and \(B\) denote the pullbacks of the hyperplane classes from the two factors. The Segre hyperplane class is
\[
H=A+B.
\]
The Chow degree is therefore
\[
C_{a,b}
=
\int_{X_{a,b}}H^d
=
\binom{d}{a},
\]
since only the monomial
\[
A^aB^b
\]
survives in the top intersection product.

Let \(g\) be the sectional genus. A general complete intersection of \(d-1\) Segre hyperplanes is a smooth curve with class
\[
H^{d-1}.
\]
Adjunction gives
\[
2g-2
=
\bigl(K_{X_{a,b}}+(d-1)H\bigr)\cdot H^{d-1}.
\]
The canonical class is
\[
K_{X_{a,b}}
=
-(a+1)A-(b+1)B.
\]
Using
\[
A\cdot H^{d-1}
=
\binom{d-1}{a-1},
\qquad
B\cdot H^{d-1}
=
\binom{d-1}{a},
\]
one obtains
\[
2g-2
=
-(a+1)\binom{d-1}{a-1}
-(b+1)\binom{d-1}{a}
+(d-1)\binom{d}{a}.
\]

The general Hurwitz-degree theorem states
\[
H_{a,b}=2C_{a,b}+2g-2.
\]
Substitution and the identities
\[
\binom{d-1}{a-1}=\frac{a}{d}\binom{d}{a},
\qquad
\binom{d-1}{a}=\frac{b}{d}\binom{d}{a}
\]
give
\[
H_{a,b}
=
\frac{2ab}{d}\binom{d}{a}.
\]
Equivalently,
\[
H_{a,b}
=
\frac{2(d-1)!}{(a-1)!(b-1)!},
\]
so its integrality is manifest.

Now put
\[
C=C_{a,b},
\qquad
r=\frac{2ab}{d}.
\]
Write the rational number \(r\) in lowest terms as
\[
r=\frac{u}{q},
\qquad
q=\frac{d}{\gcd(d,2ab)}.
\]
Since
\[
H=C\frac{u}{q}
\]
is an integer and \(\gcd(u,q)=1\), one has
\[
q\mid C.
\]
Therefore
\[
\gcd(C,H)
=
\gcd\!\left(C,C\frac{u}{q}\right)
=
\frac{C}{q}
=
\frac{C\,\gcd(d,2ab)}{d}.
\]
This proves the exact gcd formula.

For the coprimality classification, suppose first that
\[
\min(a,b)=1.
\]
By symmetry take \(a=1\), so \(d=b+1\). Then
\[
C_{1,b}=b+1,
\qquad
H_{1,b}=2b,
\]
and hence
\[
\gcd(C_{1,b},H_{1,b})
=
\gcd(b+1,2).
\]
This is \(1\) exactly when \(b\) is even.

Now suppose
\[
a,b\ge2.
\]
Then \(d\ge4\). Since
\[
q=\frac{d}{\gcd(d,2ab)}\le d
\]
and
\[
C=\binom{d}{a}\ge\binom{d}{2}=\frac{d(d-1)}2>d,
\]
we get
\[
\gcd(C,H)=\frac{C}{q}>1.
\]
Thus no Segre variety with both factors of dimension at least \(2\) has coprime Chow and Hurwitz degrees.

## Verification
The bundled checker evaluates the intersection-theoretic closed forms and the gcd identity for every pair
\[
1\le a,b\le200.
\]
It also checks the coprimality classification over the same range.

For selected small pairs it evaluates the sectional-genus formula directly and verifies
\[
H_{a,b}=2C_{a,b}+2g-2.
\]

These finite computations are regression evidence only. The theorem for all positive \(a,b\) is proved symbolically above.

## Relationship to prior work
The general theory of the Hurwitz form identifies it as the higher associated hypersurface immediately adjacent to the Chow form and proves that, for a smooth projective variety of degree \(p\) and sectional genus \(g\), its Pluecker degree is
\[
2p+2g-2.
\]
That theorem supplies the geometric input used here.

For a Segre product, the Chow degree and sectional genus can be computed explicitly in its two-generator intersection ring. Combining those calculations yields the closed Hurwitz-degree formula above.

The inspected general Hurwitz-form source discusses Chow and Hurwitz forms, includes the quadric Segre surface as an example, and gives the general degree theorem, but it does not state the exact gcd formula or the coprimality classification for the full family
\[
\mathbb P^a\times\mathbb P^b.
\]
Targeted searches for the same statement in gcd, common-divisor, coprimality, and associated-hypersurface language did not locate an equivalent result.

## Limitations
The theorem concerns only the first two associated hypersurfaces, namely the Chow and Hurwitz forms. It does not classify common divisors across the entire coisotropic or polar-degree sequence.

The result is for the standard Segre embedding. Segre-Veronese embeddings have different projective and sectional-genus formulas and are not covered.

The arithmetic statement is a short consequence once the general Hurwitz-degree theorem and the Segre intersection ring are juxtaposed. An unindexed source on associated hypersurfaces or Segre intersection theory could contain the same consequence.

## References
Bernd Sturmfels, *The Hurwitz Form of a Projective Variety*, arXiv:1410.6703, first submitted 24 October 2014; *Journal of Symbolic Computation* 79 (2017), 186--196, DOI 10.1016/j.jsc.2016.08.012.

I. M. Gel'fand, M. M. Kapranov, and A. V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants*, Birkhauser, 1994.
