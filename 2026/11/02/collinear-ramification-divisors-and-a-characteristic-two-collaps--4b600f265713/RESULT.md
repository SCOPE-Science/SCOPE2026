# Collinear ramification divisors and a characteristic-two collapse of normal-bundle splitting

## Finding

Let \(k\) be an algebraically closed field of arbitrary characteristic, let
\(X=(\mathbb P^1_k)^3\), and let \(U\) be the open scheme of **unramified**
fixed-source morphisms \(f=(f_1,f_2,f_3):\mathbb P^1_k\to X\) for which each
\(f_i\) has degree two. Here unramified means that the differential
\(T_{\mathbb P^1}\to f^*T_X\) is everywhere injective; no embedded-image
hypothesis is imposed.

Represent \(f_i\) by a basepoint-free pair of binary quadratics
\[
P_i=a_i s^2+b_i st+c_i t^2,\qquad
Q_i=d_i s^2+e_i st+h_i t^2.
\]
Set the binary ramification quadratic
\[
W_i=(a_i e_i-b_i d_i)s^2
       +2(a_i h_i-c_i d_i)st
       +(b_i h_i-c_i e_i)t^2,
\]
and define \(M_f\) to be the \(3\times3\) matrix of their coefficient rows
in the basis \((s^2,st,t^2)\).

**Theorem.** For every \(f\in U\), exactly the following normal-bundle
splittings occur:
\[
N_f\cong
\begin{cases}
\mathcal O_{\mathbb P^1}(5)\oplus\mathcal O_{\mathbb P^1}(5),
 &\operatorname{rank}M_f=3,\\
\mathcal O_{\mathbb P^1}(4)\oplus\mathcal O_{\mathbb P^1}(6),
 &\operatorname{rank}M_f=2.
\end{cases}
\]
If \(\operatorname{char}k\ne2\), the balanced locus is nonempty, and the
unbalanced locus
\[
D=\{f\in U:\det M_f=0\}
\]
is a **nonempty, smooth, geometrically irreducible effective Cartier
divisor**. Its defining section is the restriction to \(U\) of a section of
\(\mathcal O_{(\mathbb P^5)^3}(2,2,2)\). Geometrically, \(D\) is exactly the
locus where the three unordered ramification divisors of the maps \(f_i\),
viewed as points of the projective plane of binary quadratics, are
collinear. If \(\operatorname{char}k=2\), every \(f\in U\) has the unbalanced
splitting \(\mathcal O(4)\oplus\mathcal O(6)\); no balanced member exists.

## Assumptions and scope

The parameter space of degree-two maps \(\mathbb P^1\to\mathbb P^1\) is
the resultant-nonzero open \(H_2\subset\mathbb P^5\) of ordered pairs
\([P:Q]\) of binary quadratics, modulo simultaneous nonzero scalar. Thus
\(U\subset H_2^3\) is an open subscheme. The source \(\mathbb P^1\) has a
fixed parametrization; the theorem does not quotient by source or target
automorphisms. An individual component map is permitted to be purely
inseparable in characteristic two, provided the combined triple map is
unramified. All claims are scheme-theoretic over an algebraically closed
field, in any positive characteristic and characteristic zero. The line
bundle class \((2,2,2)\) refers to the three coefficient projective-space
factors \((\mathbb P^5)^3\), rather than a divisor class on the target \(X\).

## Proof

**1. The differential and the unramified condition.** For a basepoint-free
pair \((P_i,Q_i)\) of binary quadratics, the component differential is a
map \(\mathcal O(2)\to\mathcal O(4)\), hence a section of
\(\mathcal O(2)\). In the affine coordinate \(z=s/t\), its numerator is
\(P_i'(z)Q_i(z)-P_i(z)Q_i'(z)\), with the homogeneous expression \(W_i\)
above. Therefore \(f\) is unramified exactly when the three quadratics
\(W_i\) have **no simultaneous projective zero**. In particular,
\(\operatorname{rank}M_f\ge2\): if the row span has dimension at most one,
all three sections are multiples of one nonzero quadratic (or all zero),
and this quadratic has a zero over the algebraically closed field.

**2. Only two possible normal-bundle types.** Since
\(f_i^*T_{\mathbb P^1}=\mathcal O(4)\), the everywhere-injective differential
gives a vector-bundle exact sequence
\[
0\longrightarrow\mathcal O(2)
\xrightarrow{(W_1,W_2,W_3)}\mathcal O(4)^3
\longrightarrow N_f\longrightarrow0.
\]
Thus \(E=N_f(-4)\) is globally generated, has rank two and degree two.
Grothendieck splitting and global generation leave only
\(E\cong\mathcal O(1)^2\) or
\(E\cong\mathcal O\oplus\mathcal O(2)\). To distinguish them, twist the
normal sequence by \(\mathcal O(-6)\):
\[
0\longrightarrow\mathcal O(-4)
\xrightarrow{(W_i)}\mathcal O(-2)^3
\longrightarrow N_f(-6)\longrightarrow0.
\]
The induced map \(H^1(\mathcal O(-4))\to H^1(\mathcal O(-2))^3\) has
Serre-dual transpose the linear map
\[
k^3\longrightarrow H^0(\mathbb P^1,\mathcal O(2)),\qquad
(\lambda_1,\lambda_2,\lambda_3)\longmapsto
\lambda_1 W_1+\lambda_2 W_2+\lambda_3 W_3.
\]
It consequently has rank \(\operatorname{rank}M_f\). Since the two
\(H^1\)-spaces both have dimension three and
\(H^0(\mathcal O(-4))=H^0(\mathcal O(-2))=0\), exactness gives
\[
h^0(N_f(-6))=3-\operatorname{rank}M_f.
\]
This dimension is zero for \(\mathcal O(5)^2\) and one for
\(\mathcal O(4)\oplus\mathcal O(6)\). This establishes the classification
in every characteristic, and rules out deeper jumps.

**3. The characteristic-two wall.** The middle coefficient of every
\(W_i\) equals \(2(a_i h_i-c_i d_i)\), so it vanishes in characteristic
two. Therefore \(\operatorname{rank}M_f\le2\), while unramifiedness gives
the reverse inequality. This proves universal unbalancedness. Nonemptiness
of \(U\) is witnessed by the triple of maps in affine coordinates
\[
f_1(z)=z^2+z,\qquad
f_2(z)=\frac{z^2}{z+1},\qquad
f_3(z)=z^2+z.
\]
Its ramification sections are \(1,z^2,1\), with no common zero and row
rank two. The expressions refer to the degree-two homogeneous pairs
\((s^2+st,t^2)\), \((s^2,st+t^2)\), and \((s^2+st,t^2)\).

**4. The determinant in odd characteristic.** A direct polynomial
identity gives
\[
\operatorname{disc}(W_i)=4\operatorname{Res}(P_i,Q_i).
\]
For characteristic different from two, basepoint freeness implies that
\(W_i\) is a quadratic with two distinct projective roots. The
ramification-divisor map
\[
\beta:H_2\longrightarrow V:=
\mathbb P(H^0(\mathbb P^1,\mathcal O(2)))
\setminus\{\text{double-root quadratics}\},\quad
[P:Q]\longmapsto[W(P,Q)]
\]
is smooth and surjective with geometrically irreducible fibers
isomorphic to \(\operatorname{PGL}_2\). Indeed, after an étale-local
ordering of the two distinct ramification points and a source coordinate
sending them to \(0\) and \(\infty\), every degree-two map having that
ramification divisor is uniquely of the form \(A\circ(z\mapsto z^2)\)
with \(A\in\operatorname{PGL}_2\). This also gives an étale-local
trivialization of \(\beta\).

The hypersurface of linearly dependent triples of vectors in
\((\mathbb P^2)^3\) is the irreducible determinant hypersurface. It is
smooth at rank-two triples; its singular locus consists of triples of rank
at most one. Intersect with \(V^3\), and then remove triples whose three
quadratics have a common root. Call the resulting base \(B\). It is a
smooth irreducible open subset of the determinant hypersurface. The
preimage of \(B\) under \(\beta^3\) is exactly \(D\): rank-one triples
cannot arise in \(U\), and a rank-two triple arises in \(U\) precisely
when there is no common root. The smooth, surjective, étale-locally trivial
\(\operatorname{PGL}_2^3\)-bundle \(\beta^3\) has irreducible fibers,
so its preimage of the irreducible \(B\) is smooth and irreducible. Hence
\(D\) is smooth and geometrically irreducible. The determinant is cubic
in the entries \(W_i\), but **quadratic in the coefficient variables of
each individual component**; it is therefore a section of
\(\mathcal O_{(\mathbb P^5)^3}(2,2,2)\) restricted to \(U\). Both its
zero locus and nonzero locus are nonempty by the witnesses below, so it
defines an effective Cartier divisor, and its zero scheme is reduced and
smooth.

**5. Nonempty strata with exact witnesses.** For any odd characteristic
consider
\[
f_1(z)=z^2,\qquad f_2(z)=\frac{z^2+1}{z}.
\]
Their ramification quadratics are \(2st\) and \(s^2-t^2\). For
\(f_3(z)=(z^2+1)/(z+1)\), the third ramification quadratic is
\(s^2+2st-t^2\), the sum of the first two. The maps all have degree
two, their derivatives have no common zero, and the rank is two: this
is a member of \(D\). Instead set \(f_3(z)=(z^2+2)/z\); its ramification
quadratic is \(s^2-2t^2\), independent of the first two in every odd
characteristic. This gives a member of \(U\setminus D\). The proof of
both existence claims is uniform, including characteristic three. This
finishes the theorem.

## Verification

The standalone Python 3 program `verify.py` contains only standard-library
imports. It checks the exact Wronskian coefficient rule, basepoint-free
conditions via homogeneous quadratic resultants, and the absence of common
ramification points using Euclidean gcd over the finite prime fields
\(p=3,5,7,11,13,17,19\). It checks row rank two for the jump witness
and rank three for the balanced witness in each odd characteristic. In
characteristic two, it checks the unramified rank-two witness and
exhaustively verifies the vanishing middle Wronskian coefficient for all
\(2^6\) coefficient choices. It also checks the quadratic scaling rule
for the determinant line bundle. The observed output is exactly
`VERIFY_OK: exact witness, characteristic-two, rank and homogeneity checks`.
The infinite theorem, smoothness and irreducibility are established by the
preceding mathematical arguments, **not** by extrapolation from these
finite tests.

To reproduce: run `python3 verify.py` from the directory containing this
file and `verify.py`; no third-party packages or data files are needed.

## Relationship to prior work

Iwasaki, *Normal Bundle Splitting Strata of Rational Curves in Toric
Varieties*, arXiv:2609.39309 (first public September 30, 2026), develops
general two-term resolutions and cohomological jumping-locus schemes over
arbitrary characteristic (Sections 3 and 5). Its explicit worked
application (Section 6) concerns blowups of projective space along linear
subspaces. The exact splitting dichotomy, branch-divisor collinearity,
proved irreducibility and smoothness of the first jump divisor, and
characteristic-two collapse for tridegree \((2,2,2)\) maps to
\((\mathbb P^1)^3\) are not stated there. The normal-sequence cohomology
criterion is standard and is not claimed as a new general technique.
The characteristic-two behavior of projective-space normal bundles, also
recalled by Iwasaki, provides context but does not imply this particular
toric-product classification. Searches of titles and statements under
normal-bundle splitting, triple products, tridegree, ramification
quadratics, and determinantal jumping loci did not locate an explicit
preexisting equivalent classification. A coordinate-equivalent earlier
computation cannot be categorically excluded.

## Limitations

The theorem concerns maps of **exactly** tridegree \((2,2,2)\) with
fixed parameterized source and unramified differential. It says nothing
about ramified triples, embeddings as a separate moduli problem, other
tridegrees, or target toric varieties in general. The odd-characteristic
smoothness statement concerns \(D\) within the unramified-map open
\(U\), not the closure of \(D\) in the ambient product of projective
spaces, whose rank-one locus is singular. The theorem gives splitting
types and the divisor's line-bundle class but not an enumerative
intersection number against arbitrary incidence conditions. No
independent audit or external priority certification has been performed.

## References

1. H. Iwasaki, *Normal Bundle Splitting Strata of Rational Curves in Toric Varieties*, arXiv:2609.39309, first public September 30, 2026. Sections 1, 3, 5, and 6.
2. A. Grothendieck, *Sur la classification des fibrés holomorphes sur la sphère de Riemann*, Amer. J. Math. 79 (1957), 121–138. (Vector bundles on the projective line.)
3. R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics 52, Springer, 1977. (Serre duality, tangent sequences and Cartier divisors.)
