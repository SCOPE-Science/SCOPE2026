# Three-variable metric collapse of finite thick generalized-quadrangle incidence graphs

## Finding

Let \(\mathcal Q\) range over **all** finite generalized quadrangles of order \((s,t)\), where the integers \(s,t\ge 2\); no transitivity, regularity of automorphism groups, or classical-construction hypothesis is imposed. Let \(G(\mathcal Q)\) be the undirected point–line incidence graph. Expand it to a relational structure \(G^+(\mathcal Q)\) with unary point and line predicates \(P,L\), adjacency \(E\), and five binary predicates \(D_0,\ldots,D_4\) naming exact graph distances. In ordinary first-order logic **without counting**, every two such enriched structures have the same sentences using at most three distinct variable symbols, at *arbitrary quantifier depth*:

\[
G^+(\mathcal Q)\equiv_{\mathrm{FO}^3}G^+(\mathcal Q')\qquad
\text{for all finite thick generalized quadrangles }\mathcal Q,\mathcal Q'.
\]

Thus the entire class has **one** unrestricted three-variable theory, even in the distance-enriched signature. Consequently the same holds for the simpler language with named point and line predicates and incidence alone, and for the uncoloured adjacency graph. The smallest model within the class is the \(30\)-vertex incidence graph of \(W(3,2)\), the generalized quadrangle of order \((2,2)\); hence \(30\) is the sharp smallest-representative bound for this class.

The three-variable indistinguishability bound is **sharp in the distance-enriched signature**: \(G^+(W(3,2))\) and \(G^+(W(3,3))\) are equivalent in \(\mathrm{FO}^3\), but a four-variable sentence distinguishes them. The same four-variable witness distinguishes the order-\((2,2)\) model from the Hermitian example of order \((4,2)\).

## Assumptions and scope

A generalized quadrangle is a point–line incidence system in which any two distinct points lie on at most one common line, every line contains \(s+1\) points, every point lies on \(t+1\) lines, and, for every nonincident point–line pair \((p,\ell)\), there is **exactly one** point on \(\ell\) collinear with \(p\). Its dual is obtained by exchanging points and lines and swapping \(s,t\). We assume finiteness and \(s,t\ge2\), traditionally called *thickness*. The graph has

\[
|P|=(s+1)(st+1),\qquad |L|=(t+1)(st+1),\qquad
|V|=(s+t+2)(st+1).
\]

Graph distances are \(0,2,4\) between two points or two lines, and \(1,3\) between a point and a line. Distinct points have distance two exactly when collinear; distinct lines have distance two exactly when intersecting. Point–line distance one means incidence. In the expanded structure, \(D_i(a,b)\) means exactly distance \(i\). The five relations are *named*, so the theorem is stronger than an equivalence only in graph adjacency. The symbol \(\mathrm{FO}^k\) permits reuse of any of \(k\) variable symbols and arbitrarily deep nesting, but not counting quantifiers.

## Proof

**1. Exact pair-extension table.** For an ordered pair \((a,b)\), let \(T_{AB,h}(X;i,j)\) be the number of vertices \(z\) of side \(X\in\{P,L\}\) satisfying \(d(a,z)=i\) and \(d(b,z)=j\), where \(A,B\) are the sides of \(a,b\) and \(h=d(a,b)\). The following table gives **every nonzero value**, not only those needed to establish positivity. A pair \((i,j):c\) denotes \(T_{AB,h}(X;i,j)=c\); omitted cells have count zero.

| Ordered-pair type | Side of \(z\) | All nonzero distance-pair counts \((i,j):c\) |
|---|---|---|
| \(PP,0\) | \(P\) | \((0,0):1,\ (2,2):s(t+1),\ (4,4):s^2t\) |
| \(PP,0\) | \(L\) | \((1,1):t+1,\ (3,3):st(t+1)\) |
| \(PP,2\) | \(P\) | \((0,2):1,\ (2,0):1,\ (2,2):s-1,\ (2,4):st,\ (4,2):st,\ (4,4):st(s-1)\) |
| \(PP,2\) | \(L\) | \((1,1):1,\ (1,3):t,\ (3,1):t,\ (3,3):t(s(t+1)-1)\) |
| \(PP,4\) | \(P\) | \((0,4):1,\ (4,0):1,\ (2,2):t+1,\ (2,4):(s-1)(t+1),\ (4,2):(s-1)(t+1),\ (4,4):t(s^2-s+1)-s\) |
| \(PP,4\) | \(L\) | \((1,3):t+1,\ (3,1):t+1,\ (3,3):(t+1)(st-1)\) |
| \(PL,1\) | \(P\) | \((0,1):1,\ (2,1):s,\ (2,3):st,\ (4,3):s^2t\) |
| \(PL,1\) | \(L\) | \((1,0):1,\ (1,2):t,\ (3,2):st,\ (3,4):st^2\) |
| \(PL,3\) | \(P\) | \((0,3):1,\ (2,1):1,\ (4,1):s,\ (2,3):s(t+1)-1,\ (4,3):s(st-1)\) |
| \(PL,3\) | \(L\) | \((3,0):1,\ (1,2):1,\ (1,4):t,\ (3,2):(s+1)t-1,\ (3,4):t(st-1)\) |

For \(LL,h\), take the \(PP,h\) rows, interchange the side labels \(P,L\), and interchange \(s,t\); for \(LP,h\), do the same to the \(PL,h\) rows. This is legitimate because the dual system is another generalized quadrangle of order \((t,s)\). It supplies the remaining five pair types. The table therefore treats all ten possible ordered side-and-distance types, including equality.

**Derivation.** For a fixed point \(p\), precisely \(s(t+1)\) other points are collinear with it, and precisely \(s^2t\) are not. Two distinct collinear points have exactly \(s-1\) common other collinear points (the remaining points of their line). Two noncollinear points have exactly \(t+1\) common collinear points: each line through the first point supplies, by the quadrangle axiom, precisely one such point. Thus the point-collinearity graph has the relevant common-neighbour numbers \(s-1\) and \(t+1\). For two collinear points, exactly one line contains both; for two noncollinear points, none does. All remaining row entries follow by subtracting these intersection sizes from the known degrees and totals \(|P|,|L|\).

For example, in the collinear-point row the count of lines incident with neither point is \( (t+1)(st+1)-(2t+1)=t(s(t+1)-1)\). For a noncollinear point pair, the number of points collinear with neither is \((s+1)(st+1)-2-(t+1)-2(s-1)(t+1)=t(s^2-s+1)-s\), and the number of lines incident with neither is \((t+1)(st+1)-2(t+1)=(t+1)(st-1)\). These account for the largest apparently exceptional table entries.

For a point \(p\) on a line \(\ell\), the other \(s\) points of \(\ell\) are collinear with \(p\), and \(t\) other lines through \(p\) meet \(\ell\) at \(p\). For \(p\notin\ell\), exactly one point of \(\ell\) is collinear with \(p\), and exactly one line through \(p\) meets \(\ell\); subtraction gives the two mixed rows. More explicitly, if \(p\notin\ell\), the \(s\) other points of \(\ell\) are not collinear with \(p\), and the number of points not on \(\ell\) and not collinear with \(p\) equals \(s^2t-s=s(st-1)\). Dually, among the lines disjoint from \(\ell\), exactly \(t\) pass through \(p\), leaving \(t^2s-t=t(st-1)\) disjoint from \(\ell\) and nonincident with \(p\). The row entries for each side sum respectively to \((s+1)(st+1)\) and \((t+1)(st+1)\). This verifies that the lists are exhaustive and that there are no omitted positive entries.

**2. Parameter-independent support.** Every listed term is strictly positive for integers \(s,t\ge2\). The only less-immediate expression is

\[
t(s^2-s+1)-s\ \ge\ 2s^2-3s+2\ =\ (s-1)(2s-1)+1\ >0.
\]

Every other term is either visibly positive or contains a factor of the form \(s-1\), \(t-1\), or \(st-1\), or is a positive product minus one. Therefore the Boolean support of the entire ten-type extension table is identical for all finite thick generalized quadrangles, even when their parameters differ.

**3. Infinite three-pebble strategy.** Consider the ordinary back-and-forth game with three reusable pebbles on any two expanded structures. Maintain the invariant that corresponding pebbled vertices have the same side, and that all corresponding ordered pairs have the same exact graph distance (including distance zero for coinciding vertices). If one pebble is moved, at most two pebbles remain fixed. Their side-and-distance type agrees on both boards. Spoiler's new vertex determines a side and a distance to each of the two fixed vertices. By the support equality in the table, Duplicator can choose a vertex of the same side and with precisely those two distances on the other board. When fewer pebbles have been placed, fill the missing anchor positions conceptually by repetitions of a retained vertex, or use the \(PP,0\) and \(LL,0\) rows; the same existence argument applies. The invariant consequently holds after **every** move, without a bound on the number of rounds.

The invariant preserves equality, the two unary sorts, adjacency, and all five named distance relations on pebbled elements. The three-pebble characterization of finite-variable first-order equivalence therefore proves the asserted \(\mathrm{FO}^3\) collapse in the full expanded signature.

**4. Sharpness of variable width in the expanded signature.** Define the four-variable sentence

\[
\psi_4=\exists x_1\exists x_2\exists x_3\exists x_4\,
\bigwedge_{1\le i\le4}P(x_i)\ \land\
\bigwedge_{1\le i<j\le4}D_2(x_i,x_j).
\]

The condition \(D_2\) forces distinct points. Any three pairwise collinear points of a generalized quadrangle lie on one common line: otherwise, a point off the line through the first two would have two distinct collinear points on that line, contradicting uniqueness. Hence all four pairwise-collinear points must lie on a common line. The sentence \(\psi_4\) is therefore true exactly when \(s+1\ge4\), that is, \(s\ge3\). It is false for \(W(3,2)\) and true for \(W(3,3)\), giving an exact width-three-versus-four separation in the enriched language. This does **not** claim that width four is optimal in the smaller adjacency-only language.

Finally, \((s+t+2)(st+1)\ge(2+2+2)(2\cdot2+1)=30\), with equality for the existing quadrangle \(W(3,2)\). This proves the sharp smallest-representative statement.

## Verification

The standalone standard-library program `verify_generalized_quadrangles.py` constructs three finite classical geometries from their forms: the symplectic quadrangles \(W(3,2)\) and \(W(3,3)\), and the Hermitian quadrangle \(H(3,4)\) of order \((4,2)\). It independently enumerates every graph-distance vector for **each ordered pair** and checks its full count dictionary against the displayed symbolic formula, not merely its nonzero support. The three graphs have respectively \(30,80,72\) vertices, giving \(900+6400+5184=12484\) ordered pairs. Each graph realizes exactly ten pair-side/distance types, with a shared total of \(84\) positive extension entries. The program also checks the common support and all ten side-specific row-total identities for \(3600\) symbolic integer parameter pairs \((s,t)\in\{2,\ldots,61\}^2\), and independently tests the four-point \(D_2\)-clique separating sentence on each graph. Reproduce with `python3 verify_generalized_quadrangles.py`; the recorded output is in `verification_output.txt`.

These computations corroborate the extension table. They do not prove the claims for all parameters: that follows from the complete combinatorial derivation, positivity argument, and pebble strategy above. The raw form constructions are not used as hypotheses of the theorem.

## Relationship to prior work

The generalized-quadrangle axioms and classical examples are standard in the finite-geometry literature. Thas (2002), *Automorphisms and Combinatorics of Finite Generalized Quadrangles*, develops the wider geometry and automorphism theory; its inspected historical/prefatory material concerns geometric constructions. Inoue (first arXiv posting May 7, 2012) addresses uniqueness at order \((4,16)\). Bamberg, Li, and Swartz (first arXiv posting August 14, 2015) classify antiflag-transitive generalized quadrangles, a geometric symmetry hypothesis **not** assumed here; the relevant introductory/parameter sections of their publicly available accepted manuscript were inspected. Their classification does not state the unrestricted non-counting three-variable equivalence proved here in those inspected sections.

The general use of finite-variable pebble games is classical, including the foundational literature of Ehrenfeucht and Kolaitis–Väänänen. A support test for distance-regular graphs resembles the strategy but does not directly settle this theorem for unequal-valency quadrangle incidence graphs, nor does it automatically give the named-sort, all-distance signature. In particular, \(H(3,4)\) has point degree \(3\) and line degree \(5\), so its incidence graph is **not regular**. The present ten-type exact table handles that nonregular case without any transitivity assumption.

Search and source inspection did not reveal an earlier theorem with the same all-parameter, arbitrary-depth, distance-enriched claim. This is a qualified comparison, not an exhaustive priority determination; a general result on coherent configurations or relation algebras might subsume the theorem.

## Limitations

Only **finite, thick** generalized quadrangles of order \((s,t)\), \(s,t\ge2\), are covered. The theorem concerns ordinary non-counting finite-variable first-order logic; counting quantifiers can distinguish degrees, while an unrestricted number of variables can distinguish finite cardinalities. No classification for the thin cases \(s=1\) or \(t=1\) or for higher variable widths is asserted. The four-variable separation is established in the **expanded distance signature** only. The historical originality determination is qualified, and no independent mathematical audit has been performed.

## References

1. K. Thas, *Automorphisms and Combinatorics of Finite Generalized Quadrangles*, Ghent University doctoral thesis, 2002. Open-access thesis: https://biblio.ugent.be/publication/522069 (preface and relevant geometric introduction inspected).
2. K. Inoue, *The Uniqueness of a Generalized Quadrangle of Order (4,16)*, first publicly posted 2012-05-07, arXiv:1205.1431, https://arxiv.org/abs/1205.1431 (dated abstract accessible; full text not accessed).
3. J. Bamberg, C. H. Li, and E. Swartz, *A Classification of Finite Antiflag-Transitive Generalized Quadrangles*, first posted 2015-08-14, arXiv:1508.03565; accepted manuscript https://research-repository.uwa.edu.au/files/33963664/Bamberg_et_al._2018_A_classification_of_finate_antiflag_trasitive_generalized_quadrangles.pdf (introduction and parameter section inspected).
4. P. G. Kolaitis and J. A. Väänänen, *Generalized quantifiers and pebble games on finite structures*, LICS 1992, pp. 348–359, https://lics.siglog.org/archive/1992/Vnnen-Generalizedquantifi.html (accessible abstract and bibliographic record).
