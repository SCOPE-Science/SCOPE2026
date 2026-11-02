# Six unrestricted three-variable incidence theories of finite line geometries

## Finding

A point–line structure has a disjoint union of points and lines, unary predicates for the two sorts, and one point–line incidence relation. Equality is available. Neither line intersection, parallelism, adjacency of lines, nor counting is a named relation.

Consider the union \(\mathscr C\) of the following three natural types of finite structures:

1. all finite projective planes and affine planes of order at least two, whether Desarguesian or not;
2. the point–line structures of all finite Desarguesian affine and projective spaces \(\operatorname{AG}(d,q)\) and \(\operatorname{PG}(d,q)\), with \(d\ge3\) and \(q\) an arbitrary prime power;
3. the incidence structures \(\mathcal E_n\), \(n\ge3\), whose points are the vertices of the complete graph \(K_n\), whose lines are its two-element subsets, and whose incidence is membership.

Exactly six equivalence classes occur under ordinary, noncounting, *unrestricted-depth* three-variable first-order equivalence \(\equiv_{\mathrm{FO}^3}\). They are:

| Class | Precisely the members | Smallest member in \(\mathscr C\) |
|---|---|---|
| A | \(\mathcal E_3\) | 6 elements |
| B | All projective planes of order \(q\ge2\) | \(\operatorname{PG}(2,2)\), 14 elements |
| C | \(\mathcal E_4\), equivalently the affine plane of order two | 10 elements |
| D | \(\mathcal E_5\) | 15 elements |
| E | All affine planes of order \(q\ge3\) | \(\operatorname{AG}(2,3)\), 21 elements |
| F | Every \(\mathcal E_n\) with \(n\ge6\), and every affine or projective space of dimension \(d\ge3\) in item 2 | \(\mathcal E_6\), 21 elements |

In particular, for every \(n\ge6\), every prime power \(q\ge2\), and every \(d\ge3\),
\[
\mathcal E_n\equiv_{\mathrm{FO}^3}\operatorname{AG}(d,q)
\equiv_{\mathrm{FO}^3}\operatorname{PG}(d,q).
\]
The \(21\)-element uniform representative bound is sharp within \(\mathscr C\). All structures in \(\mathscr C\) agree through quantifier rank two. At quantifier rank three exactly four theories occur: A, B, C, and the union D–F. At quantifier rank four, all six classes are already distinguished, and no further separation becomes possible at higher depth while the number of variable symbols remains three.

## Assumptions and scope

The projective and affine planes are finite incidence planes of order \(q\ge2\), with no assumption of coordinatizability. Higher-dimensional spaces use vector-space coordinates over finite fields and contain *all* points and one-dimensional geometric lines, but not higher-dimensional flats. In the three-variable language each variable may denote a point or line, with the unary sort predicates fixing its kind. We distinguish the finite-variable fragment \(\mathrm{FO}^3\), with arbitrary quantifier rank, from quantifier-rank-three ordinary first-order logic. All universal statements quantify over exactly the stated family \(\mathscr C\); they do not extend to arbitrary linear spaces or arbitrary designs.

## Proof

**1. A finite-palette three-pebble lemma.** Color ordered pairs \((u,v)\) by nine labels: equal/distinct point pairs \(\mathrm{PP=},\mathrm{PP\ne}\); equal/meeting/disjoint line pairs \(\mathrm{LL=},\mathrm{LLM},\mathrm{LLD}\); and incident/nonincident point–line and line–point pairs \(\mathrm{PL+},\mathrm{PL-},\mathrm{LP+},\mathrm{LP-}\). In particular, meeting of two *distinct* lines means possession of a common point; it is not a basic symbol. For a colored pair \((u,v)\) define its extension signature
\[
T(u,v)=\{(c(u,w),c(v,w)): w\text{ is a point or a line}\}.
\]
Assume, for each of two structures, that \(T(u,v)\) depends only on \(c(u,v)\), that the same colors are realized in both, and that for each color the two structures have the same signature. Duplicator maintains the color of **each occupied ordered pebble pair** in a three-pebble game. Upon moving one pebble, the other two determine a colored pair and a requested pair of extension colors; equality of signatures supplies a replacement with both colors as requested. For fewer fixed pebbles, the existence of the required sorts, incidence/nonincidence, and distinct elements follows from the same tables. Pair colors refine all atomic relations, so this is an arbitrarily long winning strategy. Consequently the structures have identical \(\mathrm{FO}^3\) theories. This argument is a sufficient criterion, not an assertion that every conceivable structure with the same informal geometry is equivalent.

**2. Universal extension patterns in three-space.** For every finite field order \(q\ge2\), both \(\operatorname{AG}(3,q)\) and \(\operatorname{PG}(3,q)\) realize all nine colors, and their signatures are identical and constant on each color. The complete 52-row pair-color/signature certificate for six class representatives is supplied in `support_templates.json`; the class-F representative is \(\mathcal E_6\). The geometric verification of the uniform class-F table reduces to the following exhaustive cases (reverse point–line orientation is symmetric).

For two distinct points, there are lines through both, through exactly either one, and through neither. There are also points equal to either selected point or distinct from both. For two distinct lines, a third point can lie on both precisely when the lines meet, on either one alone, or on neither. For every selected pair of lines, whether meeting or disjoint, a third *distinct line* can be chosen in **each** of the four patterns: meets both, meets the first only, meets the second only, or meets neither. To meet both skew lines, join one point on each; to meet one while avoiding the other, take an appropriate line through a point of the first outside the plane spanned by that point and the second; to avoid both, choose an auxiliary plane that does not contain either selected line, and a line within it missing the at most two intersection points. A projective plane of order \(q\ge2\) has \(q(q-1)>0\) lines avoiding two distinct points. An affine plane of order \(q\ge2\) has at least one line avoiding any two points. These constructions also work when the selected lines meet, with the auxiliary plane chosen away from their intersection.

For a point \(p\) and line \(\ell\), if \(p\in\ell\), every other line through \(p\) meets \(\ell\), and lines through a different point of \(\ell\) or skew to \(\ell\) realize the other admissible patterns. If \(p\notin\ell\), lines through \(p\) can meet or miss \(\ell\), and lines avoiding \(p\) can likewise meet or miss \(\ell\). Third points equal to \(p\), on \(\ell\), or off \(\ell\) realize exactly the admissible equality/incidence patterns. There are always sufficiently many points and lines to avoid an occupied element.

The existence assertions are uniform at \(q=2\), not asymptotic: through a point of three-dimensional affine or projective space pass \(q^2+q+1\) lines, while at most \(q+1\) lie in a prescribed projective plane; in affine three-space the analogous plane has \(q+1\) directions and at least \(q^2\) other directions. The number of projective lines skew to a fixed projective line is \(q^4\); the number of affine lines disjoint from a fixed affine line is \(q^4-1\). If two selected points are distinct, there are lines avoiding both (at \(q=2\), at least 22 in projective three-space and 15 in affine three-space). A third line avoiding a selected point and line exists even in the smallest case. In higher dimension, any two points/lines involved in one extension lie in a three-dimensional affine or projective subspace; each required witness can therefore be chosen there, while the formally impossible patterns remain impossible in the larger space. This proves the class-F high-dimensional assertions for every \(d\ge3\).

**3. The thin complete-graph bridge.** In \(\mathcal E_n\), two lines are distinct two-element sets. A third line disjoint from each of two disjoint lines exists precisely when \(n\ge6\) (six vertices are required for three pairwise disjoint edges). All other class-F extension patterns occur already for \(n\ge5\), and the remaining one occurs at six. In particular the class-F table applies to \(\mathcal E_n\) for every \(n\ge6\). For \(n=5\), the absent triple-disjoint-line extension yields class D. At \(n=4\), all lines are the two-subsets of four points, giving exactly the affine plane of order two, class C. At \(n=3\), all lines meet and the two selected lines exhaust all three points, giving class A.

**4. Plane cases.** In every finite projective plane, all distinct lines meet, and lines through two distinct points meet the standard projective-plane counting identities. The number of lines avoiding two distinct points is \(q(q-1)>0\), as is the number of points outside two intersecting lines. Hence all orders \(q\ge2\) have the same class-B table. In every finite affine plane, two distinct lines meet or are parallel. For a parallel pair, a third line meets both or neither, and never just one; for intersecting lines, a third line cannot be disjoint from both. At order \(q=2\), two parallel lines partition all points and there is no third parallel line; this is class C. At every order \(q\ge3\), there is both a third parallel line and a point outside two parallel lines, yielding the order-independent class-E signature. This uses only the plane axioms and therefore includes all non-Desarguesian examples. The full class tables agree with the constructive cases above; there is no additional parameter distinction.

**5. Sharp separation and quantifier ranks.** Write \(D(x,y)\) for the formula saying that \(x,y\) are distinct lines without a common point, and \(M(x,y)\) for their having a common point. These predicates are definable with one further bound point variable. A three-variable sentence can mention three line variables and test any one of their pairwise meetings by **rebinding the third variable locally** within that test. The following existence properties thus have three-variable defining sentences of quantifier rank at most four:

- \(S\): two disjoint lines exist (rank three).
- \(C\): two distinct lines jointly cover all points (rank three).
- \(A\): three lines exist, the first disjoint from the second, while the third meets the first but misses the second (rank four).
- \(T\): three pairwise disjoint lines exist (rank four).

Their truth vectors \((S,C,A,T)\) for classes A–F respectively are
\[
(0,1,0,0),\quad (0,0,0,0),\quad (1,1,0,0),\quad
(1,0,1,0),\quad (1,0,0,1),\quad (1,0,1,1).
\]
They are distinct, proving six is the exact number. Rank-two equivalence follows because every structure realizes precisely the same one- and two-element atomic incidence patterns. For rank three, after two choices all available **atomic** third-element incidence patterns coincide for classes D, E and F, even though their derived meet/disjoint line extensions differ; a three-round back-and-forth strategy therefore merges these three classes, but separates A, B, C by \(S,C\). This proves the sharp depth-three/depth-four transition. The smallest representatives in the table have sizes 6, 14, 10, 15, 21 and 21; no member of either class E or F has fewer than 21 elements, so the uniform bound 21 is sharp within \(\mathscr C\).

## Verification

`verify_support.py` constructs incidence sets without using a graph or model-theory library and exhaustively computes the entire colored ordered-pair extension table for 17 concrete examples, including affine and projective three- and four-spaces, affine and projective planes over multiple fields, and \(\mathcal E_n\) for \(3\le n\le8\). It checks that within each structure every pair of the same color has the same extension signature, and recovers exactly six profile tables. `verify_rank3.py`, independently written using only atomic equality/sort/incidence and a recursive first-order logical-type computation, recovers exactly four rank-three classes in eleven smaller examples. Run both with standard Python from the same directory. Their output is embedded in `support_output.txt` and `rank3_output.txt`, and the six complete abstract templates in `support_templates.json` support inspection of every claimed pattern. These finite computations **corroborate** the geometric proof; they do not by themselves prove the infinite or arbitrary-field cases.

## Relationship to prior work

Venema, *Points, lines and diamonds* (1999), studies the two-sorted **modal** logic of projective planes, giving completeness and complexity results and discussing possible study of higher-dimensional geometries; it does not present this three-variable first-order classification. Hodkinson and Hussain, *The modal logic of affine planes is not finitely axiomatisable* (2008), considers a different modal language with named parallelism, proving nonfinite axiomatizability rather than a bounded-variable equivalence classification. Trotter and Wang, *Incidence Posets and Cover Graphs* (2013), define graph incidence posets and study order dimension and chromatic number, not their unrestricted three-variable theories.

Related mathematical classifications of affine planes, projective planes, complete-graph incidence graphs at fixed quantifier rank, affine resolvable designs, and thick partial geometries cover significant **pieces** of the families treated here. In particular, a stronger related result about thick partial geometries with named collinearity/concurrence implies the class-F equivalence for higher-dimensional examples with line size at least three. It does not cover the thin complete-graph geometries (line size two), nor supply the combined six-class classification and sharp depth-four separation in the pure point–line incidence signature. The precise new bridge is between \(\mathcal E_6\), with two points on each line, and arbitrarily large affine and projective three- and higher-dimensional geometries, with their different point/line counts and incidence degrees.

## Limitations

No claim is made for four-variable logic, counting extensions, languages with parallelism, line meeting or collinearity named as atomic relations, or the class of all finite linear spaces. An unrestricted-depth three-variable theorem is not an arbitrary-variable elementary-equivalence theorem. The computations use prime field arithmetic and selected finite dimensions; the all-field and non-Desarguesian claims rest on the mathematical construction and plane axioms, respectively. Independent mathematical verification and exhaustive priority research are not part of this proof; a general theorem about three-pebble invariants or coherent configurations could imply some or all of the classification. The literature comparisons identify this risk rather than treating a failed search as proof of novelty.

## References

1. Y. Venema, *Points, lines and diamonds: a two-sorted modal logic for projective planes*, Journal of Logic and Computation **9** (1999), 601–621, DOI: 10.1093/logcom/9.5.601; full text https://staff.science.uva.nl/y.venema/papers/vene-poin99.pdf (published 1999-10-01).
2. I. Hodkinson and A. Hussain, *The modal logic of affine planes is not finitely axiomatisable*, Journal of Symbolic Logic **73** (2008), 940–952, DOI: 10.2178/jsl/1230396757; full text https://www.doc.ic.ac.uk/~imh/papers/affine.pdf.
3. W. T. Trotter and R. Wang, *Incidence Posets and Cover Graphs*, arXiv:1308.2471v1 (first public 2013-08-12), https://arxiv.org/html/1308.2471v1.
