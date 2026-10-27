# Seven-level recovery and the first eight-level collapse of finite weak orders

## Finding

Write \(W(n_1,\ldots,n_h)\) for the **ordinal sum of \(h\) nonempty antichains** of respective sizes \(n_1,\ldots,n_h\). Thus \(x<y\) holds precisely when the level of \(x\) is earlier than the level of \(y\); distinct elements of one level are incomparable. The language is equality and this one strict binary order relation, with no named levels. This is the strict part of a total preorder (a finite preference ranking with ties). Let \(W\equiv_3 W'\) denote agreement on all first-order sentences of quantifier rank at most three, and let \(c_i=\min(n_i,3)\).

**Seven-level recovery.** If \(1\le h,k\le7\), then
\[
 W(n_1,\ldots,n_h)\equiv_3 W(n'_1,\ldots,n'_k)
 \quad\Longleftrightarrow\quad
 h=k\ \text{and}\ (c_1,\ldots,c_h)=(c'_1,\ldots,c'_h).
\]
Consequently there are **exactly \(3279\) rank-three theories** among all nonempty finite weak orders having at most seven levels. Every member has an equivalent representative in the same family with at most \(21\) elements; this bound is sharp within that family, attained when all seven capped sizes equal three.

**Exact eight-level collapse.** If both weak orders have exactly eight levels, they are rank-three equivalent precisely when their capped eight-tuples are equal, **or** the capped tuples agree at all positions except the fourth and fifth, at which they read \((2,3)\) and \((3,2)\), in either order, with the common sizes at positions two, three, six, and seven belonging to \(\{2,3\}\). The sizes at positions one and eight may independently be any of \(\{1,2,3\}\).

The \(3^8=6561\) capped eight-tuples therefore form **exactly \(6417\) rank-three equivalence classes**: \(6273\) singletons and \(144\) pairs. For example,
\[
W(1,2,2,2,3,2,2,1)\equiv_3 W(1,2,2,3,2,2,2,1),
\]
although these strict-order structures are nonisomorphic. Within the exactly-eight-level family, the sharp largest minimal representative has \(24\) elements. The threshold seven is optimal for recovering every capped level size: at eight levels, even the ordered size profile need not be determined.

## Assumptions and scope

Every level is finite and nonempty; there are between one and eight levels in the stated classifications. There is **no** assumption that level sizes are uniform, and the levels are *not* named by parameters or unary predicates. No claim of a complete classification for weak orders of unrestricted height, or of cross-height equivalence between an eight-level order and a shorter one, is made. The sharp representative bounds refer separately to the specified height-restricted families.

One can equally use the reflexive total-preorder relation \(\preccurlyeq\): in these structures \(x<y\) is quantifier-free definable as \(x\preccurlyeq y\wedge\neg(y\preccurlyeq x)\), while \(x\preccurlyeq y\) is quantifier-free definable as \(\neg(y<x)\). Therefore this language change preserves quantifier rank.

## Proof

**1. Uniform truncation.** For any number of levels, replacing each level of size \(n_i\) by one of size \(\min(n_i,3)\) preserves the three-round Ehrenfeucht–Fraïssé theory. Duplicator responds in the corresponding level and preserves equality of previously selected elements. At most three distinct elements are ever selected. A level of size at least three therefore always supplies a fresh answer whenever its truncated counterpart does; levels of sizes one and two are copied exactly. The partial maps preserve both incomparability within a level and strict order between levels.

**2. Exact three-round invariant.** For an ordered tuple \((x,y,z)\), its complete atomic diagram in the strict-order language is encoded by the three pair relations
\[
 d(x,y,z)=(r(x,y),r(x,z),r(y,z)),
\]
where \(r\) takes the four values equality, strict less-than, strict greater-than, and distinct incomparability. For each ordered pair \((x,y)\), define
\[
 T_1(x,y)=\big(r(x,y),\{d(x,y,z):z\in W\}\big).
\]
For each \(x\), put \(T_2(x)=\{T_1(x,y):y\in W\}\), and finally
\[
 T_3(W)=\{T_2(x):x\in W\}.
\]
All sets retain their complete nested elements, not merely cardinalities. By backward induction on the remaining moves in the Ehrenfeucht–Fraïssé game, \(T_1\) classifies the pointed two-element configurations with one further move, \(T_2\) classifies pointed configurations with two further moves, and
\[
 W\equiv_3 W'\quad\Longleftrightarrow\quad T_3(W)=T_3(W').
\]
The argument is two-sided: matching extension-type sets supplies a Duplicator response to *every* Spoiler move in *either* structure. At the end the atomic diagrams coincide, and if an extension type is absent Spoiler can force a mismatch. Equality is included explicitly, so repeated selections and multiple distinct vertices from one tied level are handled.

**3. Finite exhaustive classification.** By Step 1, the inputs with at most seven levels reduce to exactly
\[
 3+3^2+\cdots+3^7=3279
\]
ordered vectors over \(\{1,2,3\}\). The provided standalone program computes the exact nested finite sets in Step 2 for each vector; all \(3279\) sets differ, including across different permitted heights. This proves the first assertion and the sharp internal \(21\)-vertex bound: each component marked three needs at least three vertices, and the seven-tripleton vector is distinguished from all other seven-or-fewer-level vectors.

At exactly eight levels there are \(6561\) capped vectors. Exhaustive comparison of the same exact invariants gives \(6417\) different sets. Every fiber has size one or two. The fibers of size two are exactly those obtained by exchanging the central \((2,3)\) with \((3,2)\), subject to four surrounding positions in \(\{2,3\}\). There are precisely
\[
 3\cdot2\cdot2\cdot2\cdot2\cdot3=144
\]
such unordered pairs, with independently variable outermost entries. The program *constructs all predicted pairs and tests equality of their complete list with the actual fibers*, in addition to checking the counts; neither number alone is used to infer the stated classification. Finally, the all-three eight-vector is not in any exceptional pair, and its smallest eight-level representative has \(24\) vertices.

These finite checks are exhaustive over all reduced structures. Together with Step 1 they prove the universally quantified assertions for **all** positive original level sizes; numerical samples are not used as a substitute for an infinite argument.

## Verification

The accompanying `verify.py` requires only Python 3 and the standard library. From the directory containing the file, run `python3 verify.py low`, `python3 verify.py eight`, and `python3 verify.py game`. Their recorded outputs appear in `VERIFY_OUTPUT.txt`.

`low` checks all \(3279\) vectors and compares the full-vertex calculation with a separate stabilizer-orbit enumeration. `eight` checks all \(6561\) vectors and the exact \(144\)-pair relation, not just its cardinality. `game` independently plays the two-sided three-move game on selected positive and negative boundary pairs and checks uncapped sizes. The formal proof is the finite reduction plus the exact Hintikka recursion; samples are auxiliary checks.

## Relationship to prior work

Mwesigye and Truss (2011) develop finite-coloured-linear-order Ehrenfeucht–Fraïssé characters and explicit optimal bounds for one and two rounds in a language with **unary colour predicates**. Their general reduction methods are relevant, but the inspected paper does not state the present classification for the **pure strict-order language on ordinal sums of antichains**, in which a level's size is *not* provided as a colour predicate. Mwesigye and Truss (2019) analyze three-move coloured-word equivalence and long optimal words, again in the named-colour language. Their inspected full text gives neither the seven-level recovery assertion nor the exact eight-level \(144\)-pair phenomenon. The difference in languages is material: a colour visible in one move is not an automatically named size class in the weak-order game.

## Limitations

The eight-level census is **within exactly eight levels**, not a classification of all cross-height comparisons. The exact results depend on pure first-order logic without counting quantifiers or named levels. The verifier assumes ordinary integer arithmetic and exact finite set operations; independent external mathematical validation has not been performed. Completeness of historical-literature retrieval is not claimed, and an equivalent formulation outside the inspected sources remains possible.

## References

1. F. Mwesigye and J. K. Truss, “Classification of Finite Coloured Linear Orderings,” *Order* 28 (2011), 387–397; first published online 7 September 2010; DOI: 10.1007/s11083-010-9178-9.
2. F. Mwesigye and J. K. Truss, “On Optimal Representatives of Finite Coloured Linear Orders,” *Order* 36 (2019), 107–117; online 2 May 2018; DOI: 10.1007/s11083-018-9458-3.
