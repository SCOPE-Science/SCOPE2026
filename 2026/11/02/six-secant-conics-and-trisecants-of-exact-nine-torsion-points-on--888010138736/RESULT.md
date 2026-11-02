# Six-secant conics and trisecants of exact-nine-torsion points on a plane cubic

## Finding

Let \(E\subset\mathbb P^2_{\mathbb C}\) be **any** smooth plane cubic, choose any flex \(O\) as the group identity, and set \(T=E[9]\setminus E[3]\). The set \(T\) consists of the \(72\) geometric points of exact order \(9\), also called the type-nine points. A *six-secant conic* is a projective plane conic whose intersection with \(E\) consists of six **distinct** points of \(T\). Reducible conics are counted as conics but never as smooth conics.

There are exactly \(1{,}928{,}772\) distinct six-secant conics. Exactly \(227{,}520\) are reducible (each the union of two distinct trisecant lines with disjoint triples of points of \(T\)); exactly \(1{,}701{,}252\) are smooth. The set \(T\) determines exactly \(720\) trisecant lines, with precisely \(30\) through each point of \(T\). Each point of \(T\) belongs to exactly \(160{,}731\) six-secant conics, of which \(18{,}960\) are reducible and \(141{,}771\) smooth.

All these counts are independent of the isomorphism class of the smooth complex plane cubic and of the choice of flex origin.

## Assumptions and scope

The ground field is \(\mathbb C\). A *trisecant line* here contains three distinct points of \(T\), not a tangent line counted with multiplicities. The six points of a six-secant conic are its entire scheme-theoretic intersection with \(E\); each has intersection multiplicity one. Counts refer to **unmarked distinct geometric curves**, not ordered tuples of points or equations up to different scalings. The group scheme \(E[9]\) is identified abstractly with \(G=(\mathbb Z/9\mathbb Z)^2\), and \(E[3]\) with \(H=3G\). Thus \(T=G\setminus H\) has \(81-9=72\) elements.

## Proof

### 1. Conics are equivalent to zero-sum six-subsets

Since \(O\) is a flex, \(\mathcal O_E(1)\simeq\mathcal O_E(3O)\), so \(\mathcal O_E(2)\simeq\mathcal O_E(6O)\). For six distinct points \(P_1,\ldots,P_6\in E\), put \(D=\sum_i P_i\). Abel's theorem for an elliptic curve says that \(D\sim6O\) exactly when \(\sum_iP_i=O\) in the group law. The line bundle \(\mathcal O_E(2)(-D)\) has degree zero; it has a nonzero global section exactly when it is trivial, in which case its section space is one-dimensional. The restriction map

\[
H^0(\mathbb P^2,\mathcal O(2))\longrightarrow H^0(E,\mathcal O_E(2))
\]

is an isomorphism, because the cubic ideal sequence has kernel \(H^0(\mathbb P^2,\mathcal O(-1))=0\) and cokernel controlled by \(H^1(\mathbb P^2,\mathcal O(-1))=0\). Therefore **exactly one** projective conic contains the given six points when their sum is zero, and none otherwise. Bézout's theorem forces its six intersections with \(E\) to be exactly the six chosen distinct points, all transverse. No two different six-subsets can define the same conic.

Likewise, three distinct points of \(E\) are collinear exactly when their group sum is \(O\); a line has no fourth intersection with the cubic.

### 2. Character count of all six-secant conics

Let \(N\) be the number of six-element subsets \(A\subset T\) such that \(\sum_{a\in A}a=0\). For a character \(\chi:G\to\mathbb C^\times\), define

\[
P_\chi(z)=\prod_{t\in T}(1+\chi(t)z).
\]

Character orthogonality gives the exact finite coefficient formula

\[
N=\frac1{81}\sum_{\chi\in\widehat G}[z^6]P_\chi(z).
\]

There is one trivial character, eight characters of exact order three, and seventy-two of exact order nine. Their respective polynomials are

\[
(1+z)^{72},\qquad
\frac{(1+z^3)^{27}}{(1+z)^9},\qquad
\frac{(1+z^9)^9}{(1+z^3)^3}.
\]

To justify the latter two products: an order-three character has all nine points of \(H=3G\) in its kernel, so removing \(H\) from \(G\) changes the multiplicity of its eigenvalue one from 27 to 18. An order-nine character takes each ninth root of unity nine times on \(G\), while on \(H\) each cubic root occurs three times. The coefficients of \(z^6\) in the three displayed polynomials are, respectively,

\[
\binom{72}{6}=156{,}238{,}908,\qquad
\binom{14}{6}-27\binom{11}{3}+\binom{27}{2}=-1{,}101,\qquad
\binom42=6.
\]

Consequently,

\[
N=\frac{156{,}238{,}908-8(1{,}101)+72(6)}{81}
=\boxed{1{,}928{,}772}.
\]

By Step 1, this is precisely the number of distinct six-secant conics, including reducible ones.

### 3. Complete trisecant incidence count

Fix \(x\in T\). Each triple through \(x\) has the form \(\{x,y,-x-y\}\) with all three elements distinct and in \(T\). Among the 72 possibilities for \(y\in T\), exactly nine make \(-x-y\in H\): those in the coset \(-x+H\). Three further possibilities are excluded by repeated points: \(y=x\), \(y=-2x\), or \(y=-5x\) (the last because \(2y=-x\) modulo nine). These three lie outside \(-x+H\), are distinct, and have order nine. Thus there are \(72-9-3=60\) valid **ordered** choices of \(y\), or \(30\) unordered triples through \(x\). Counting point-line incidences yields

\[
\#\{\text{trisecant lines}\}=\frac{72\cdot30}{3}=\boxed{720}.
\]

Two distinct trisecant lines share at most one point of \(T\). For each fixed trisecant, the other lines meeting its triple comprise exactly \(3(30-1)=87\) lines, with no overlap between these three lists. Hence precisely

\[
720-1-87=632
\]

other trisecants have **disjoint** triples of points in \(T\).

### 4. Reducible conics and their uniqueness

A reducible conic over \(\mathbb C\) is a union of two lines, possibly coincident. A double line cannot contain six distinct points of \(E\), as a line meets the cubic in only three points. Each component of a reducible six-secant conic must therefore contain three distinct points of \(T\) by Bézout, with disjoint triples. Conversely the union of any two trisecants with disjoint triples gives a six-secant conic. Uniqueness of the conic determined by its six points (Step 1), alternatively uniqueness of factorization into lines, ensures that no two such line pairs produce the same conic. Their exact number is

\[
\frac{720\cdot632}{2}=\boxed{227{,}520}.
\]

Every irreducible plane conic over \(\mathbb C\) is smooth, so the smooth count is

\[
\boxed{1{,}928{,}772-227{,}520=1{,}701{,}252}.
\]

The group \(\mathrm{GL}_2(\mathbb Z/9\mathbb Z)\) acts transitively on \(T\) and preserves both distinctness and zero-sum subsets. This is an **abstract group-combinatorial symmetry**, not a claim of additional projective automorphisms of \(E\). It makes the total six-subset incidence uniform, so each point lies on \(6N/72=160{,}731\) conics. The reducible incidence is also directly \(30\cdot632=18{,}960\), leaving \(141{,}771\) smooth six-secant conics through each point.

Finally, if the flex origin is changed by \(h\in E[3]\), the set \(T\) is translated by \(-h\) and is unchanged, while sums of six points change by \(-6h=0\). All counts are thus independent of the chosen flex.

## Verification

The accompanying Python 3 program `verify_sixsecants.py` uses only the standard library. It independently performs a six-subset dynamic program on \((\mathbb Z/9)^2\), checks the three character coefficients, exhausts all \(720\) distinct zero-sum triples, and enumerates all disjoint pairs of such triples, checking that all \(227{,}520\) six-point supports occur once. It also checks the complete point-incidence statistics. Its terminal success line is `TYPE9_SIXSECANTS_GROUP_CHARACTER_AND_REDUCIBLE_COUNTS_OK`. The proof above establishes the identification of finite group configurations with actual plane curves; the script is a reproducibility check of the exact finite arithmetic, not a replacement for the geometric argument.

## Relationship to prior work

Gattazzo (1979) first characterized the \(72\) type-nine points and proved that the third intersection of a line through two type-nine points may be a flex or another type-nine point; his work does not enumerate all distinct-point six-secant conics. Szemberg and Szpond, arXiv:2211.00494 (first made public November 1, 2022), count \(8{,}244\) conics through six distinct **sextactic**, i.e. \(E[6]\setminus E[3]\), points of the Fermat cubic and distinguish \(5{,}976\) smooth conics. Their introduction explicitly proposes studying curves through higher-order division points. Merta and Zięba, arXiv:2406.13802 (first made public June 19, 2024), determine the \(72\) **type-nine** points and count \(324\) conics with contact multiplicity three at each of two type-nine points. Merta’s 2026 dissertation, Chapter 2, additionally exhibits three special 24-line pencils through the type-nine points of the Fermat cubic, but these are selected trisecant subarrangements rather than the complete 720-line collection, and its conic section treats contact at two points. None of these described results gives the conics through **six distinct** type-nine points: the prescribed intersection divisors and, in the sextactic case, the torsion sets differ. The present counting theorem also applies to every smooth complex plane cubic, not just the Fermat member.

## Limitations

This result does not classify projective equivalence classes of the conics, their mutual intersection arrangement, or the scheme structure of their parameter locus. The six-secant conics in this note are reduced geometric curves; multiplicities of points in a Hilbert scheme are not claimed. The proof is in characteristic zero. A literature-priority risk remains for earlier unindexed or incompletely accessible calculations of the same six-secant count.

## References

1. T. Szemberg and J. Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics*, arXiv:2211.00494, first posted 2022-11-01. https://arxiv.org/abs/2211.00494
2. Ł. Merta and M. Zięba, *Sextactic and type-9 points on the Fermat cubic and associated objects*, arXiv:2406.13802, first posted 2024-06-19. https://arxiv.org/abs/2406.13802
3. Ł. Merta, *Geometric properties of arrangements of low-degree curves*, PhD thesis, Kraków, 2026, Chapter 2 (publicly deposited 2026-07-13). https://rep.up.krakow.pl/xmlui/handle/11716/14216
4. R. Gattazzo, *Punti di tipo 9 di una cubica ellittica*, Rend. Sem. Mat. Univ. Padova 61 (1979), 285–301. https://www.numdam.org/item/RSMUP_1979__61__285_0/
5. Classical Abel theorem for divisors on a complex elliptic curve, applied to the degree-three flex embedding; the requisite form is also recalled in Merta–Zięba, Theorem 2.1.
