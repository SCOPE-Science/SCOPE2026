# Correction and complete rank spectrum of the \(\mathbb F_{7^4}\) \(M\)-cyclic benchmark
## Finding

Berhuy and Molina's Example 4.25 describes
\[
K=\mathbb F_7,
\qquad
L=\mathbb F_{7^4},
\]
and asks for an element \(\omega\in L\) that simultaneously generates the multiplicative group
\[
L^\times
\]
and satisfies
\[
\omega^4=\omega^2+1.
\]
These two requirements are incompatible.

Indeed, the displayed relation implies
\[
\omega^8=2\omega^2+1,
\]
\[
\omega^{16}=-1,
\]
and therefore
\[
\omega^{32}=1.
\]
Moreover,
\[
\omega^{16}\ne1,
\]
so \(\omega\) has multiplicative order \(32\), whereas
\[
|L^\times|=7^4-1=2400.
\]

The intended example is repaired without changing its code-theoretic conclusions by taking \(\omega\) to be any root of
\[
X^4-X^2-1
\]
over \(\mathbb F_7\). This polynomial is irreducible, so
\[
L=\mathbb F_7(\omega)
\]
and
\[
(1,\omega,\omega^2,\omega^3)
\]
is still an \(\mathbb F_7\)-basis.

Set
\[
\alpha=4\omega^2-2.
\]
Then
\[
\alpha^2=-1.
\]
Hence
\[
g=(x-1)(x-\alpha)
\]
still divides
\[
x^4-1=(x-1)(x+1)(x^2+1),
\]
and the printed \([4,2]\) cyclic code is well defined after this minimal field-specification correction.

For that corrected benchmark, the projective rank spectrum is exact. Among the
\[
\frac{7^8-1}{7^4-1}=7^4+1=2402
\]
one-dimensional \(L\)-subcodes, exactly
\[
1
\]
has rank weight \(1\),
\[
49
\]
have rank weight \(2\), and
\[
2352
\]
have rank weight \(3\).

Because every one-dimensional \(L\)-subcode contains
\[
7^4-1=2400
\]
nonzero codewords and rank weight is invariant under nonzero \(L\)-scaling, the complete ordinary rank-weight enumerator is
\[
W_C(z)
=
1+2400z+117600z^2+5644800z^3.
\]

The generalized rank-weight hierarchy remains
\[
(M_1(C),M_2(C))=(1,3),
\]
as intended in the source.

## Assumptions and scope

Work in
\[
L=\mathbb F_7[\omega]/(\omega^4-\omega^2-1).
\]
The defining quartic is irreducible over \(\mathbb F_7\), so \(L\) is a field of order \(7^4\).

The code is the \(L\)-linear span of the source generator polynomial
\[
g=(x-1)(x-\alpha),
\qquad
\alpha=4\omega^2-2,
\]
inside
\[
L[x]/(x^4-1).
\]

Every codeword has the source form
\[
c(a,b)=
\bigl(
a\alpha+b,\,
-a(\alpha+1)+b\alpha,\,
a-b\alpha,\,
b
\bigr),
\qquad
a,b\in L.
\]

The correction concerns only the phrase asserting that \(\omega\) is a multiplicative generator. No change is made to the basis relation, to \(\alpha\), to the generator polynomial, or to the code.

## Proof

First, from
\[
\omega^4=\omega^2+1
\]
we obtain
\[
\omega^8=(\omega^2+1)^2
=\omega^4+2\omega^2+1
=3\omega^2+2.
\]
Squaring again in characteristic \(7\),
\[
\omega^{16}
=
(3\omega^2+2)^2
=
9\omega^4+12\omega^2+4
=
2(\omega^2+1)+5\omega^2+4
=
6
=
-1.
\]
Thus
\[
\omega^{32}=1
\]
and
\[
\omega^{16}\ne1.
\]
Therefore \(\omega\) has order \(32\), not \(2400\).

The polynomial
\[
X^4-X^2-1
\]
has no linear factor over \(\mathbb F_7\). It also has no monic quadratic factor: direct division by every monic quadratic over \(\mathbb F_7\) leaves a nonzero remainder. Hence it is irreducible.

Now
\[
\alpha^2
=
(4\omega^2-2)^2
=
16\omega^4-16\omega^2+4
=
2(\omega^2+1)-2\omega^2+4
=
6
=
-1.
\]
Thus \(\alpha\) is a root of
\[
x^2+1,
\]
so
\[
g=(x-1)(x-\alpha)
\]
divides \(x^4-1\).

It remains to count projective rank weights. Since the code has \(L\)-dimension \(2\), its one-dimensional \(L\)-subcodes are parametrized by
\[
\mathbb P^1(L).
\]

For an affine projective point write
\[
(a,b)=(t,1).
\]
The source codeword formula has the same \(\mathbb F_7\)-span as
\[
1,\qquad t\alpha,\qquad t-\alpha.
\]
Thus its rank weight is
\[
\dim_{\mathbb F_7}
\operatorname{Span}_{\mathbb F_7}
\{1,t\alpha,t-\alpha\}.
\]

Rank weight \(1\) forces both
\[
t\alpha\in\mathbb F_7
\]
and
\[
t-\alpha\in\mathbb F_7.
\]
Writing
\[
t=\alpha+s,\qquad s\in\mathbb F_7,
\]
gives
\[
t\alpha=-1+s\alpha.
\]
This lies in \(\mathbb F_7\) only for \(s=0\). Hence the unique rank-one affine point is
\[
t=\alpha.
\]

For rank at most \(2\), there must be a nonzero projective relation direction
\[
[A:B]\in\mathbb P^1(\mathbb F_7)
\]
such that
\[
At\alpha+B(t-\alpha)\in\mathbb F_7.
\]
For fixed \([A:B]\),
\[
A\alpha+B\ne0,
\]
and the solutions are exactly
\[
t=\frac{B\alpha+r}{A\alpha+B},
\qquad
r\in\mathbb F_7.
\]
Thus there are
\[
8\cdot7=56
\]
incidence pairs between affine \(t\) and relation directions.

The unique rank-one point has a two-dimensional relation space and therefore contributes all
\[
8
\]
projective relation directions. Every rank-two affine point has a one-dimensional relation space and contributes exactly one direction. Hence the number of affine rank-two points is
\[
56-8=48.
\]

The remaining projective point
\[
(a,b)=(1,0)
\]
has coordinate span
\[
\operatorname{Span}_{\mathbb F_7}\{1,\alpha\},
\]
so it has rank weight \(2\). Therefore the projective counts are
\[
N_1=1,
\qquad
N_2=49,
\qquad
N_3=2402-1-49=2352.
\]

Multiplying by \(2400\) nonzero scalar multiples per projective line gives
\[
A_1=2400,
\qquad
A_2=117600,
\qquad
A_3=5644800,
\]
which proves the rank-weight enumerator.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It first checks directly that
\[
X^4-X^2-1
\]
has no linear or quadratic factor over \(\mathbb F_7\). It then implements exact arithmetic in
\[
\mathbb F_7[\omega]/(\omega^4-\omega^2-1).
\]

The verifier checks
\[
\omega^{16}=-1,
\qquad
\omega^{32}=1,
\]
and confirms that the multiplicative order of \(\omega\) is \(32\). It checks
\[
\alpha^2=-1
\]
for
\[
\alpha=4\omega^2-2.
\]

Next it enumerates all
\[
2402
\]
projective message lines in \(\mathbb P^1(\mathbb F_{7^4})\), evaluates the source codeword formula exactly, and computes each coordinate-span rank over \(\mathbb F_7\). The resulting line counts are
\[
1,\ 49,\ 2352
\]
at rank weights \(1,2,3\).

Finally it independently evaluates the relation-direction incidence count and verifies
\[
56=8+48.
\]

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Berhuy and Molina introduce this exact \([4,2]\) benchmark in Example 4.25. The source states the field relation, the generator polynomial, and the generalized rank weights
\[
M_1=1,
\qquad
M_2=3.
\]
It does not give the complete rank-weight distribution.

The source's printed field specification simultaneously calls \(\omega\) a generator of the multiplicative group and imposes
\[
\omega^4=\omega^2+1.
\]
Those assertions cannot both hold. Replacing the multiplicative-generator claim by the weaker and sufficient statement that \(\omega\) is a root of the displayed irreducible quartic preserves the intended basis and the code.

General rank-weight enumerator and generalized-rank-weight theory does not determine the three multiplicities above without a code-specific calculation. Focused searches using the exact example number, polynomial relation, element \(\alpha\), projective rank counts, and final enumerator did not locate an earlier correction or this complete spectrum.

## Limitations

The result repairs and classifies one named finite benchmark. It does not alter the general theorems of the source.

The correction is minimal: only the assertion that \(\omega\) is a multiplicative generator is removed. Other presentations of the same field or code are equivalent.

The rank spectrum is the ordinary distribution of codeword rank weights, not a classification of codewords under the full automorphism group.

A later or unindexed erratum may independently note the field-element inconsistency, and an unindexed computation may already contain the same spectrum.

## References

1. Grégory Berhuy and Julien Molina, *On the rank weight hierarchy of \(M\)-codes*, arXiv:2507.00609, first public version 1 July 2025; Advances in Mathematics of Communications 24 (2026), 208--236, DOI 10.3934/amc.2026035.
2. Relinde Jurrius and Ruud Pellikaan, *On defining generalized rank weights*, Advances in Mathematics of Communications 11 (2017), 225--235, DOI 10.3934/amc.2017014.
