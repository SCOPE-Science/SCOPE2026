# Four rank-four theories of Paley tournaments over prime-power fields, with an existential-fragment gap

## Finding

For every odd prime power \(q\equiv3\pmod4\), define the quadratic-residue tournament \(T_q\) on \(\mathbf F_q\) by \(a\to b\) when \(b-a\) is a nonzero square. Write \(\equiv_4\) for agreement on every first-order sentence of quantifier rank at most four in the signature consisting only of the arc relation and equality. Then

\[
T_q\equiv_4 T_r\quad\Longleftrightarrow\quad \min(q,19)=\min(r,19).
\]

The family has exactly two theories at rank three: \(T_3\) and one common theory for all \(q\ge7\). The family has precisely four theories at rank four, with least representatives \(T_3,T_7,T_{11},T_{19}\). Every family member has a rank-four-equivalent representative with at most 19 vertices, and 19 is best possible.

There is a strict quantifier-alternation distinction at this threshold. Among existential-prenex sentences of rank at most four (at most four existential quantifiers followed by a quantifier-free formula), only three theories occur, represented by \(T_3,T_7,T_{11}\). Specifically, \(T_{11}\) and \(T_{19}\) agree on this entire existential fragment, yet a sentence with prefix \(\forall x\forall y\forall z\exists w\) and total rank four separates them.

## Assumptions and scope

Let \(q=p^e\) with \(p\) an odd prime and \(q\equiv3\pmod4\). Denote by \(\chi\) the quadratic multiplicative character of \(\mathbf F_q\), extended by \(\chi(0)=0\). Since \(\chi(-1)=-1\), for unequal elements exactly one of \(x\to y\) and \(y\to x\) holds. We name neither addition nor multiplication, the field, the constants, nor any orientation reversal in the first-order signature. Repeated variables are allowed; the quantifier rank of a nested quantifier sequence is its length.

A tournament is *three-existentially closed* (3-e.c.) when, for every set \(\{a,b,c\}\) of three distinct vertices and every prescribed direction on the three arcs linking a new vertex to these vertices, a distinct witness realizes all three directions. Three-e.c. entails one- and two-e.c. by extending a smaller prescribed set to a three-set and arbitrarily prescribing the additional directions.

## Proof

**1. All admissible orders at least 19 are three-e.c.** Fix distinct \(a,b,c\in\mathbf F_q\) and signs \(\epsilon_a,\epsilon_b,\epsilon_c\in\{1,-1\}\). The number \(N_\epsilon\) of vertices \(z\notin\{a,b,c\}\) with \(\chi(z-v)=\epsilon_v\) for \(v=a,b,c\) is

\[
8N_\epsilon=\sum_{z\notin\{a,b,c\}}\prod_{v\in\{a,b,c\}}\bigl(1+\epsilon_v\chi(z-v)\bigr).
\]

Over the full field, the three linear character sums vanish, the three two-factor character sums are each \(-1\), and the remaining cubic character sum \(S=\sum_z\chi((z-a)(z-b)(z-c))\) satisfies \(|S|\le2\sqrt q\) by the classical Hasse–Weil bound for the nonsingular elliptic curve \(y^2=(z-a)(z-b)(z-c)\). The full sum is

\[
q-\epsilon_a\epsilon_b-\epsilon_a\epsilon_c-\epsilon_b\epsilon_c+\epsilon_a\epsilon_b\epsilon_c S\;\ge\;q-3-2\sqrt q.
\]

For \(z\in\{a,b,c\}\) the omitted summand lies between zero and four: one factor is one, and the others lie in \(\{0,2\}\). Therefore

\[
8N_\epsilon\ge q-15-2\sqrt q>0\qquad(q\ge27).
\]

The last inequality is true at 27 and its left side increases with \(q\ge27\). Thus all admissible prime powers \(q\ge27\), including proper field extensions, are 3-e.c. The two remaining admissible orders between 19 and 27 are 19 and 23. Exact finite-field checks, using all unordered triples and all eight patterns for each, find eight patterns for each of the \(\binom{19}{3}=969\) triples of \(T_{19}\) and for each of the \(\binom{23}{3}=1771\) triples of \(T_{23}\). The attached self-contained program reproduces both exhaustive verifications using two different representations of the condition. This proves three-existential closure for every admissible order \(q\ge19\).

**2. Three-e.c. tournaments agree through rank four.** Play a four-move Ehrenfeucht–Fraïssé game between any two 3-e.c. tournaments. Duplicator preserves the induced arc diagram on the chosen vertices. If Spoiler repeats an already chosen vertex, Duplicator repeats its mate. If Spoiler chooses a new vertex when at most three distinct vertices have previously been selected, Duplicator uses the corresponding one-, two-, or three-extension property to realize exactly the required arc directions. Consequently Duplicator survives four moves; all three-e.c. tournaments are \(\equiv_4\)-equivalent. Applying step 1 gives one common class for all \(q\ge19\). At rank three only the two-extension property is needed. Direct exhaustive four-pattern checks for every unordered pair in \(T_7\) and \(T_{11}\) establish two-existential closure there; higher admissible orders are two-e.c. because they are three-e.c. The same game argument for three moves shows that every \(T_q\) with \(q\ge7\) has the same rank-three theory. The transitive-triangle formula below separates \(T_3\) from the others, proving exactly two rank-three classes.

**3. The three smaller admissible orders are distinct.** There are no other prime powers \(q\equiv3\pmod4\) below 19 besides 3, 7, and 11. Three existential rank-at-most-four properties give a sharp chain of witnesses. First, \(T_3\) is a directed three-cycle and contains no transitive directed triangle, whereas \(T_7\) contains such a triangle, represented by \((0,1,2)\). Second, \(T_7\) has no transitive induced four-vertex tournament, whereas \(T_{11}\) has the transitive four-element set \(\{0,1,3,4\}\), whose topological order is \((0,3,1,4)\). Third, the rank-four sentence

\[
\forall x\,\forall y\,\forall z\,\bigl[(x\ne y\land y\ne z\land x\ne z)\longrightarrow
\exists w\,(w\to x\land w\to y\land w\to z)\bigr]
\]

fails for \(T_{11}\): the triple \(\{0,1,3\}\) has no common in-neighbor. It holds in \(T_{19}\), and all higher admissible orders, by 3-e.c. These rank-four sentences distinguish the four classes. Since the three smallest class representatives have respectively 3, 7, and 11 vertices, and the final one begins at 19, the bound 19 is sharp *within the Paley-tournament family*.

**4. The existential-prenex fragment stabilizes earlier.** Any existential-prenex sentence with at most four quantified variables and a quantifier-free matrix says that at least one induced diagram on at most four distinct vertices occurs, possibly with identifications. There are exactly four tournament isomorphism types on four vertices. Direct enumeration shows that \(T_{11}\) contains all four, with multiplicities \(55,55,55,165\) among the 330 four-subsets; \(T_7\) contains only three, with multiplicities \(7,7,21\). Every \(T_q\) with \(q\ge19\) contains all four: such a tournament contains both the cyclic and the transitive triple (regularity guarantees a cyclic triple, and every tournament on four vertices contains a transitive triple), and 3-e.c. extends any triple by every prescribed new-vertex orientation. Thus the families \(T_{11}\) and \(T_q\), \(q\ge19\), realize exactly the same induced diagrams on at most four vertices, and hence agree on all existential-prenex sentences of rank at most four. The earlier transitive-triangle and transitive-four-vertex witnesses separate the remaining two fragment classes.

## Verification

Run `python3 verify_paley_tournaments.py` with Python 3 and no nonstandard dependencies. The script constructs prime-order tournaments for orders \(3,7,11,19,23,31,43\) by modular quadratic residues, and the 27-vertex example as \(\mathbf F_3[u]/(u^3+2u+1)\), whose defining cubic has no root in \(\mathbf F_3\). It uses exhaustive two-vertex extension checks at the three small orders, an exhaustive bit-pattern count of triple extensions, a separate neighborhood-bitset intersection check through order 27, an exact tuple-extension recurrence for rank-four theories, induced four-tournament isomorphism classification, and explicit formula witnesses. Recorded output appears in `verification_output.txt`; it terminates with `VERIFY_OK`.

Finite enumeration here verifies the small cases, witness configurations, and selected large instances; the Hasse–Weil inequality and four-move strategy, not these finite samples, prove the infinite portion. The program also checks the base of the analytic inequality but does not replace the Hasse–Weil theorem.

## Relationship to prior work

Bonato, Gordinowicz, and Prałat (2010) established the minimum order 19 for three-existentially closed tournaments, uniqueness at that order, and the fact that the Paley tournament of order 23 is also 3-e.c. These are foundational inputs but neither an exact finite-family rank-four logical classification nor the existential-fragment threshold is asserted there. Javier, Llano, and Zuazua (2026), Section 4, prove that vertex-transitive doubly regular tournaments satisfy the three-pattern property precisely when they satisfy its one-sided variant and deduce the 3-e.c. property for Paley tournaments of prime order at least 19. This is substantial prior coverage of the tail assertion: the novel content claimed here is *not* discovery of 3-e.c. itself but the field-uniform explicit logical classification, sharp representatives, and the discrepancy between full rank four and the existential-prenex fragment. The all-prime-power character bound gives a separate direct proof of the required extension property and includes the nonprime example \(q=27\).

The classical Ehrenfeucht–Fraïssé extension argument is standard. This application determines precisely where the standard stabilization fails inside this finite-field family and specifies a minimal-alternation separating sentence. Graph Paley results with *symmetric undirected adjacency* do not imply the tournament statement because the arc signatures and permissible field orders differ.

## Limitations

The bound 19 concerns representatives **within this Paley-tournament family**, not all finite tournaments. This is a classification at **quantifier rank four only**, not elementary equivalence at arbitrary rank. “Existential” means the prenex existential fragment with at most four quantifiers, not arbitrary sentences having only positive occurrences of existential quantifiers after unrestricted Boolean negation. The lower bound on character sums uses the standard Hasse–Weil theorem as a named external mathematical input. Computer checks cover finite explicitly listed fields, while the field-uniform claim rests on the written inequalities. Unindexed or inaccessible literature may contain an equivalent combination of these conclusions; no independent scientific validation is claimed.

## References

1. A. Bonato, P. Gordinowicz, and P. Prałat, “Bounds and constructions for n-e.c. tournaments,” *Contributions to Discrete Mathematics* 5(2) (2010), 52–66, DOI: `10.55016/ojs/cdm.v5i2.62061`. Public online date: 2010-09-28.
2. N. Y. Javier, B. Llano, and R. Zuazua, “2- and 3-existentially closed tournaments,” *Contributions to Discrete Mathematics* 21(1) (2026), 73–90, DOI: `10.55016/0sre1423`, especially Corollary 4.3. Later supporting reference; not an archival source.
3. Standard Hasse–Weil bound for elliptic curves over finite fields, applied to the squarefree cubic \(y^2=(z-a)(z-b)(z-c)\).
4. Standard Ehrenfeucht–Fraïssé game characterization of bounded quantifier rank.
