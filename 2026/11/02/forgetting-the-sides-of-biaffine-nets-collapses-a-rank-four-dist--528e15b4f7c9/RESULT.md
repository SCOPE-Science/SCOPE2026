# Forgetting the sides of biaffine nets collapses a rank-four distinction

## Finding

Let \(\mathcal N\) be a finite affine plane of order \(q\ge2\), with one entire parallel class of lines removed. Let \(B(\mathcal N)\) be its undirected point–remaining-line incidence graph. Write \(\equiv_4\) for elementary equivalence through first-order quantifier rank four. When unary predicates \(P\) and \(L\) name the two sides of the incidence graph, write \(\equiv_4^{P,L}\).

For any two such structures of orders \(q\) and \(r\), including structures obtained from non-Desarguesian affine planes,
\[
B(\mathcal N_q)\equiv_4 B(\mathcal N_r)
\quad\Longleftrightarrow\quad
(q=2\Leftrightarrow r=2),
\]
whereas
\[
B(\mathcal N_q)\equiv_4^{P,L}B(\mathcal N_r)
\quad\Longleftrightarrow\quad
\min(q,4)=\min(r,4).
\]
Thus the uncolored family has exactly two rank-four classes, while naming its point and line sides produces exactly three. Within the family, the sharp largest smallest representative has \(18\) vertices without the names and \(32\) vertices with them.

The proof requires only the net incidence axioms in the next section. It therefore also holds for any finite incidence structure satisfying those axioms, whether or not a completion to an affine plane is supplied.

## Assumptions and scope

The graph is simple, undirected and loopless. Its two vertex sides \(P,L\) each contain \(q^2\) elements. Each side is partitioned into \(q\) groups of size \(q\). Each vertex has exactly one neighbor in each opposite-side group. Distinct vertices in the same group have no common neighbor; vertices in different groups on the same side have exactly one common neighbor. These axioms hold when an affine plane has one parallel class removed: the groups on \(P\) are the deleted-line fibers, and the groups on \(L\) are the remaining parallel classes. The parameters \(q,r\) are integers at least two for which such structures exist. The language is either \(\{E,=\}\) or \(\{E,=,P,L\}\), with \(P,L\) interpreted as unary side predicates; there are no constants, counting quantifiers, or built-in group operations.

## Proof

**Four-move reduction.** For an ordered triple \(\bar a=(a,b,c)\), define its one-step extension profile as its complete atomic diagram together with the set of complete atomic diagrams of \((a,b,c,w)\), for all choices of \(w\) in the same structure. Equality choices \(w=a,b,c\) are already forced by the atomic triple diagram. For a fresh \(w\), an extension diagram is determined by its three adjacency bits and, in the language with named sides, by the side of \(w\). Identical one-step profiles are exactly what Duplicator needs at the fourth move.

**Neighborhood calculation.** Two distinct same-side vertices have either zero or one common neighbor, according as their groups coincide or differ. Opposite-side vertices have no common neighbor. Consequently an extension adjacent to two specified distinct members of a triple is controlled by the unique common neighbor of that pair, including whether that neighbor is the third selected vertex or is also adjacent to it. An extension adjacent to all three exists precisely when the distinct selected vertices are on one side, from suitable different groups, and have a common incident vertex; repetitions reduce to the smaller distinct tuple. A fresh vertex adjacent to exactly one selected vertex exists whenever the resulting adjacency pattern is consistent with repetitions and the side predicates: each of the other two selected vertices forbids at most one of its \(q\) neighbors, leaving at least \(q-2\ge1\) choices when \(q\ge3\).

For the zero-adjacency pattern with side forgotten, at most \(3q\) vertices are adjacent to a chosen triple, and at most three vertices are already selected. Since \(2q^2-3q-3>0\) for every \(q\ge3\), a fresh vertex adjacent to none always exists. With the side of the fourth vertex prescribed, such a vertex also always exists when \(q\ge4\). Indeed, at most three opposite-side vertices exclude at most \(3q<q^2\) candidates; if fewer than three are opposite-side, the corresponding bound is strictly stronger even after excluding selected vertices.

There is exactly one exceptional side-sensitive situation for \(q=3\): when the selected triple consists of all three vertices of a single group on one side, every vertex of the opposite side is adjacent to one of them, so the zero-adjacency pattern on the opposite side is absent. If the triple does not exhaust such a group, three same-side neighborhoods cannot cover all \(q^2\) opposite-side vertices: when \(q=3\), any selected pair from different groups has a common neighbor, so their neighborhoods overlap. The uncolored zero-adjacency pattern remains available on the triple's own side. Thus all relevant one-step profile tests depend solely on the elementary incidence configuration of the selected triple, with precisely this side-sensitive exceptional case.

**Complete third-move availability.** After the first move, match its side. After the second, distinguish exactly five ordered-pair positions: equal; distinct same-side/same-group; distinct same-side/different-group; incident opposite-side; and nonincident opposite-side. Every category occurs relative to each initial vertex. For each category the possibilities for the third vertex are exhaustively as follows, with the point/line dual cases understood:

| Pair position | Exhaustive relative positions of the third vertex | Raw cases | Uncolored one-step profiles, \(q\ge3\) | Named-side one-step profiles, \(q\ge4\) |
| --- | --- | ---: | ---: | ---: |
| Equal | equal; same-side/same-group; same-side/other-group; opposite incident; opposite nonincident | 5 | 4 | 5 |
| Parallel same-side | equal to first or second; third in same group; third in another group; opposite incident only with first, only with second, or with neither | 7 | 6 | 7 |
| Intersecting same-side | equal to first or second; third in either old group; third in another group and concurrent or nonconcurrent; opposite common neighbor, incident only with first, only with second, or with neither | 10 | 10 | 10 |
| Incident opposite-side | equal to point or line; another point on line; off-line point in old or another group; another line through point; parallel line; line meeting old line away from point | 8 | 7 | 8 |
| Nonincident opposite-side | equal to point or line; point on old line in old or another group; off-line point in old or another group; line through point parallel or nonparallel to old line; line not through point parallel or nonparallel to old line | 10 | 9 | 10 |

Every row is obtained just by the group and unique-common-neighbor axioms. For example, for two same-side vertices in different groups, there are \(q-2\) choices for a concurrent third vertex in other groups (one in each unused group) and \((q-2)(q-1)\) nonconcurrent choices. For a nonincident point–line pair, an off-line point in the point's group exists in \(q-2\) ways, and a parallel line incident with neither given vertex exists in \(q-2\) ways. These minimum counts are positive for every \(q\ge3\); all other nontrivial categories use factors \(q-1\), \((q-1)^2\), or \(q(q-2)\), also positive. In the four rows whose uncolored profile count is one less than their raw-case count, two cases have the same atomic diagram and one-step adjacency support; this follows from the preceding neighborhood calculation. No further incidence information from an affine coordinate system occurs.

It follows that, for \(q,r\ge3\), corresponding ordered pairs have identical sets of achievable *uncolored* one-step triple profiles. For \(q,r\ge4\), they also have identical sets of achievable *side-named* profiles. Duplicator matches the pair positions in round two, the corresponding triple profile in round three, and the final atomic extension in round four. This proves the two claimed stable equivalences for all nets, without assuming transitive automorphism groups or a finite-field coordinatization.

**Sharp separations.** The rank-four sentence saying that some vertex has at least three distinct neighbors distinguishes \(q=2\), when every degree is two, from every \(q\ge3\). In the named-side language, the rank-four sentence
\[
\exists p_1\exists p_2\exists p_3\bigl(P(p_1)\land P(p_2)\land P(p_3)\land
\operatorname{Distinct}(p_1,p_2,p_3)\land
\forall \ell\,(L(\ell)\to\bigvee_{i=1}^3 E(p_i,\ell))\bigr)
\]
holds at \(q=3\): take the three points in one deleted-line group, so every remaining line meets one of them. It fails for \(q\ge4\), since three points lie on at most \(3q<q^2\) remaining lines. The \(q=2\) case was already separated by degree. This proves exactly two and three classes respectively. The elementary Desarguesian nets of orders \(2,3,4\) have \(8,18,32\) vertices; no smaller-order net represents the last uncolored or named-side class, yielding the sharp bounds stated.

## Verification

The self-contained `verify_biaffine.py` computes rank-four types from complete one-point extension signatures using five ordered-pair orbit representatives in the Desarguesian examples. It checks orders \(2,3,4,5,7,8,9,11,13,16\), including nonprime field orders via explicit finite-field arithmetic. The independent `independent_direct.py` enumerates every ordered vertex pair and continuation without symmetry reductions for prime orders \(2,3,5\). Both checks passed; see `verification_output.txt`. These tests verify the small-field boundary and implementations, not the general-net theorem, whose infinite quantification follows from the preceding structural proof.

## Relationship to prior work

Abreu, Araujo-Pardo, Balbuena and Labbate (arXiv:1111.3277v1, November 14, 2011), Sections 1–2, give the biaffine/elliptic-semiplane incidence graph and its block structure; their subsequent results concern reductions, amalgams and girth-five regular graph constructions. Pikhurko and Verbitsky (arXiv:1003.4865v1, March 25, 2010), Section 3, present Ehrenfeucht games and the general logical-depth framework, not this net-specific calculation. The new result concerns exact rank-four *equivalence across orders and coordinatizations*, together with the separation created by naming the bipartition. It is not implied by vertex-transitivity, graph degree, girth, or the existence of those previous construction methods.

## Limitations

This statement concerns quantifier rank four only, not higher ranks, counting logic, variable-restricted pebble games, or net isomorphism. The independent checker is not an independent mathematical audit. The named-side quantifier-rank distinction is not a claim that the bipartition is first-order undefinable at arbitrary rank; it is specifically a comparison of rank-four expressive power. No exhaustive historical-priority claim is made: uncatalogued finite-geometry/model-theory literature could contain equivalent statements.

## References

1. M. Abreu, G. Araujo-Pardo, C. Balbuena, D. Labbate, *Families of Small Regular Graphs of Girth 5*, arXiv:1111.3277v1 (2011-11-14), https://arxiv.org/abs/1111.3277.
2. O. Pikhurko, O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865v1 (2010-03-25), https://arxiv.org/abs/1003.4865.
