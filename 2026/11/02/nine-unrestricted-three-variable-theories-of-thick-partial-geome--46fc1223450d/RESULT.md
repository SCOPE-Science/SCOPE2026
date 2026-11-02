# Nine unrestricted three-variable theories of thick partial geometries with named collinearity

## Finding

A finite partial geometry \(\operatorname{pg}(s,t,\alpha)\) has \(s+1\) points on every line, \(t+1\) lines on every point, at most one line on any two distinct points, and exactly \(\alpha\) points of a nonincident line collinear with each given point. Throughout, \(s,t\ge2\) and \(1\le\alpha\le\min(s+1,t+1)\). Let \(\mathfrak G\) be its structure in the binary relational signature consisting of point and line unary predicates, point–line incidence \(I\), distinct-point collinearity \(C\), and distinct-line concurrence \(M\). The last two relations mean sharing an incident line or point respectively and are irreflexive.

For \(u\in\{s,t\}\) define
\[
\sigma(u,\alpha)=\begin{cases}0,&\alpha\le u-1,\\1,&\alpha=u,\\2,&\alpha=u+1.\end{cases}
\]
**Theorem.** For any two finite partial geometries \(\mathfrak G,\mathfrak H\) with the preceding thickness assumption, the following are equivalent:

1. \(\mathfrak G\) and \(\mathfrak H\) have the same ordered pair \((\sigma(s,\alpha),\sigma(t,\alpha))\).
2. They satisfy the same first-order sentences of quantifier rank at most three in the stated signature.
3. They satisfy the same first-order sentences using at most three variable symbols, with unrestricted quantifier depth and no counting quantifiers.

All **nine** status pairs in \(\{0,1,2\}^{2}\) occur, hence this gives precisely nine theories. The bound of three variables and rank three is also sufficient to distinguish every two distinct classes. Explicit representatives of all nine classes have at most 50 elements in their point–line universes.

## Assumptions and scope

The universe is the disjoint union of finite points and lines. Each line has exactly \(s+1\) distinct points and each point lies on exactly \(t+1\) distinct lines. Every two points share at most one line, and for every point \(p\) and line \(L\) with \(p\notin L\), exactly \(\alpha\) points of \(L\) are collinear with \(p\). No flag-transitivity, Desarguesian coordinates, equal parameters, or automorphism-homogeneity assumptions are needed. The sort predicates are named; \(C\) and \(M\) are named binary relations, so the theorem is **not** a claim that every separation is expressible by three variables in the incidence-only reduct. Quantifier-rank-three and three-variable equivalence here refer to the entire displayed signature.

## Proof

**1. Point-graph counts.** Put \(v=|P|\), \(b=|L|\), and \(k=s(t+1)\). A point has \(k\) distinct collinear neighbours. Elementary double counting, or the partial-geometry parameter formulas, gives
\[
 v=\frac{(s+1)(st+\alpha)}{\alpha},\qquad
 b=\frac{(t+1)(st+\alpha)}{\alpha}.
\]
The point collinearity graph is strongly regular, with \(\lambda=s-1+t(\alpha-1)\) common neighbours of collinear distinct points and \(\mu=\alpha(t+1)\) common neighbours of noncollinear distinct points. The line concurrence graph has the dual formulas obtained by swapping \(s,t\). A noncollinear point pair exists exactly when \(v-1-k=st(s+1-\alpha)/\alpha>0\), i.e. \(\alpha\le s\); dually a disjoint line pair exists exactly when \(\alpha\le t\).

**2. Ordered-pair extension table.** We give all counts required to extend any pair by one third vertex. Each entry is the number of vertices in the stated class, with equality cases treated separately. Here \(p,q\) are distinct points unless stated otherwise, and \(L,K\) are distinct lines unless stated otherwise.

For a single point \(p\), there are one point equal to \(p\), \(k\) other points collinear with \(p\), \(v-1-k\) other points noncollinear with \(p\), \(t+1\) incident lines, and \(b-t-1\) nonincident lines. A repeated pair \((p,p)\) has exactly these extension types. The line case is dual.

For a collinear pair \(p,q\): the two equality choices each have count one. Third points collinear with both number \(\lambda\), collinear with exactly one number \(t(s+1-\alpha)\) on either specified side, and collinear with neither number
\[
\frac{t(s-\alpha)(s+1-\alpha)}{\alpha}.
\]
Third lines incident with both number one, incident with exactly one number \(t\) on each specified side, and incident with neither number \(b-2t-1\).

For a noncollinear pair \(p,q\): the two equality choices each have count one. Third points collinear with both number \(\mu\), collinear with exactly one number \((s-\alpha)(t+1)\) on either specified side, and collinear with neither number \(v-2-2k+\mu\). Third lines incident with both number zero, incident with exactly one number \(t+1\) on either specified side, and incident with neither number \(b-2t-2\). This row is used only when \(\alpha\le s\).

For an incident mixed pair \(p\in L\), third points comprise \(p\) itself (one); points of \(L\setminus\{p\}\) (\(s\)); points outside \(L\) collinear with \(p\) (\(st\)); and points outside \(L\) noncollinear with \(p\) (\(v-1-k\)). Third lines comprise \(L\) itself (one); other lines through \(p\) (\(t\)); lines concurrent with \(L\) but not through \(p\) (\(st\)); and lines disjoint from \(L\) (\(b-1-t(s+1)\)).

For a nonincident mixed pair \(p\notin L\), third points comprise \(p\) itself (one); points of \(L\) collinear with \(p\) (\(\alpha\)); points of \(L\) noncollinear with \(p\) (\(s+1-\alpha\)); points outside \(L\) collinear with \(p\) (\(k-\alpha\)); and points outside \(L\) noncollinear with \(p\), other than \(p\) (\((st-\alpha)(s+1-\alpha)/\alpha\)). Third lines comprise \(L\) itself (one); lines through \(p\) meeting \(L\) (\(\alpha\)); lines through \(p\) disjoint from \(L\) (\(t+1-\alpha\)); lines not through \(p\) meeting \(L\) (\(t(s+1)-\alpha\)); and lines not through \(p\) disjoint from \(L\) (\((st-\alpha)(t+1-\alpha)/\alpha\)). The tables for two lines follow from the two-point rows by interchanging points with lines and \(s\) with \(t\). Reversing an ordered mixed pair reverses the extension coordinates.

**3. Exact positivity.** Every positive-looking constant in the preceding table is strictly positive for actual thick partial geometries unless an explicit factor \(s-\alpha\), \(s+1-\alpha\), \(t-\alpha\), or \(t+1-\alpha\) vanishes. In particular, \(st>\alpha\). For the one less obvious entry, write \(\delta=s-\alpha\ge0\) for a noncollinear point pair. Direct reduction gives
\[
 v-2-2k+\mu=(t-1)+\frac{\delta\bigl(t(\delta+1)-\alpha\bigr)}{\alpha}>0.
\]
Indeed \(t\ge2\); if \(\delta>0\), then \(t(\delta+1)\ge2t\ge t+1\ge\alpha\), and if \(\delta=0\) the second term is zero. The dual argument handles nonconcurrent line pairs. Also \(b-2t-2=(t+1)(st-\alpha)/\alpha>0\) and \(b-2t-1>0\), with dual inequalities. Therefore, **for each atomic ordered-pair type the set of attainable atomic third-vertex extensions depends only on the two statuses** \(\sigma(s,\alpha)\) and \(\sigma(t,\alpha)\), and not on the exact numerical parameters or on the incidence structure.

**4. Arbitrarily long three-pebble strategy.** Suppose the status pairs coincide. Every atomic ordered-pair type occurring in one geometry occurs in the other: this is apparent from the preceding counts and duality. Duplicator always preserves the sorts, equality, incidence, point collinearity, and line concurrence of the at most three occupied pebbles. When Spoiler moves one pebble, the other two (possibly coincident) specify an ordered pair; by the extension table and shared positivity pattern, Duplicator can place the moved pebble in the other structure with the same complete atomic relationships to those fixed pebbles. This is a legal partial isomorphism on all occupied pebbles. The move can be answered indefinitely in both directions. The ordinary infinite three-pebble game therefore gives equivalence for **all** first-order formulas with at most three variable symbols; finite quantifier-rank-three equivalence follows.

**5. Sharp distinguishability and realization.** For the point status, the two-variable sentence \(\exists x\exists y\,[P(x)\land P(y)\land x\ne y\land\neg C(x,y)]\) holds exactly when \(\sigma(s,\alpha)<2\). The rank-three sentence
\[
\exists x\exists y\exists z\,[P(x)\land P(y)\land P(z)\land C(x,y)\land\neg C(x,z)\land\neg C(y,z)]
\]
holds exactly when \(\sigma(s,\alpha)=0\), by the adjacent-pair neither-neighbour count in step 2. Taken together these sentences distinguish the three point-status values. Their line-dual versions distinguish the line-status values. Every differing status pair therefore has a rank-at-most-three separating sentence.

All nine pairs occur. Concrete examples, recorded as status pair \(\mapsto\) geometry, with point count plus line count, are:

| Status | Representative | Total elements |
|---|---|---:|
| \((0,0)\) | symplectic generalized quadrangle \(W(3,2)\) | 30 |
| \((1,1)\) | three parallel classes of the affine plane of order three | 18 |
| \((1,0)\) | transversal design \(\mathrm{TD}(3,4)\) from the additive Latin square of order four | 28 |
| \((0,1)\) | dual of the preceding transversal design | 28 |
| \((2,1)\) | affine plane of order three | 21 |
| \((1,2)\) | dual of the preceding affine plane | 21 |
| \((2,0)\) | point–line geometry of \(\mathrm{PG}(3,2)\), a Steiner triple system on 15 points | 50 |
| \((0,2)\) | dual of the preceding Steiner triple system | 50 |
| \((2,2)\) | Fano projective plane | 14 |

Each example satisfies the partial-geometry axioms directly. Consequently nine classes, and not merely at most nine, are realized. This completes all implications.

## Verification

Two standalone Python 3 scripts accompany the finding. `check_profiles.py` directly constructs the nine incidence structures, verifies each partial-geometry axiom, and enumerates all atomic one-point extensions for every ordered vertex pair; it finds nine distinct support profiles, each internally uniform. `symbolic_profiles.py` independently implements the extension-count formulas, agrees entry-for-entry with the direct enumeration, and checks the status-profile constancy on **54,944 arithmetically admissible parameter triples** with \(2\le s,t\le80\). Its finite scan is only a consistency check: the infinite theorem is established by the formulas and positivity proof in steps 1–4. Both scripts use only the Python standard library and can be run from the same directory.

## Relationship to prior work

Bose's 1963 paper introduced partial geometries and derived their strongly regular point graphs and intersection parameters; the original paper's axioms, formulas, and examples provide the direct geometric starting point. Brouwer and van Lint survey strongly regular graphs and partial geometries. Grohe and Otto describe plain non-counting finite-variable equivalence and its pebble-game/Boolean algebraic interpretation for binary relational signatures. None of the inspected pertinent sections states the **nine-class all-parameter classification in the jointly enriched incidence, collinearity, and concurrence signature**, nor its rank-three separation and unrestricted-depth collapse. The result uses these established tools but also requires the mixed point–line extension calculations and exact sharp status analysis. A residual priority possibility is that a broad coherent-configuration statement and known partial-geometry intersection tables together imply the classification; this remains a literature-comparison risk, not a claim of exhaustive uniqueness.

## Limitations

The theorem assumes the two unary sorts and all three named binary relations; it does not assert the same exact nine-way classification in the incidence-only reduct. It excludes thin geometries with \(s=1\) or \(t=1\), and does not cover arbitrary semipartial geometries. Counting quantifiers can read parameter-dependent multiplicities, so the theorem is strictly about non-counting logic. No claims are made about larger variable widths or logical isomorphism. The verification examples and finite parameter scan are checks of the identities, not independent infinite certificates; independent mathematical audit and a complete historical priority determination have not been performed.

## References

- R. C. Bose, “Strongly Regular Graphs, Partial Geometries and Partially Balanced Designs,” *Pacific Journal of Mathematics* **13** (1963), 389–419. DOI: 10.2140/pjm.1963.13.389. Open original: https://msp.org/pjm/1963/13-2/pjm-v13-n2-p04-p.pdf.
- A. E. Brouwer and J. H. van Lint, “Strongly Regular Graphs and Partial Geometries,” in *Enumeration and Design* (1984), 85–122. Public record: https://ir.cwi.nl/pub/1817/.
- L. M. Batten, “Partial Geometries,” in *Combinatorics of Finite Geometries*, chapter 7, Cambridge University Press, originally 1997, online 2010-03-26. DOI: 10.1017/CBO9780511665608.009.
- M. Grohe and M. Otto, “Pebble Games and Linear Equations,” *CSL 2012*, LIPIcs **16** (2012), 289–304. DOI: 10.4230/LIPIcs.CSL.2012.289. Open article: https://drops.dagstuhl.de/storage/00lipics/lipics-vol016-csl2012/LIPIcs.CSL.2012.289/LIPIcs.CSL.2012.289.pdf.
