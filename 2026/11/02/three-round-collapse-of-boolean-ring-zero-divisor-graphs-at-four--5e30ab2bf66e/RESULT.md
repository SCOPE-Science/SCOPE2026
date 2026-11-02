# Three-round collapse of Boolean-ring zero-divisor graphs at four factors

## Finding

For each integer \(n\ge2\), let \(R_n=\mathbb F_2^n\) and let \(\Gamma_n\) be its **simple** zero-divisor graph: vertices are the nonzero zero-divisors, and distinct vertices are adjacent exactly when their product is zero. Work in the first-order language with equality and a single symmetric irreflexive adjacency relation \(E\), without any named ring operations, vertex colours or constants. Then

\[
\Gamma_m\equiv_3\Gamma_n
\quad\Longleftrightarrow\quad
\min(m,4)=\min(n,4)
\qquad (m,n\ge2).
\]

Thus precisely three quantifier-rank-three theories occur, represented by \(\Gamma_2,\Gamma_3,\Gamma_4\), having respectively \(2,6,14\) vertices. The stabilization cutoff four and the fourteen-vertex representative bound are sharp. Meanwhile all these graphs are pairwise nonisomorphic because they have \(2^n-2\) vertices.

## Assumptions and scope

Identify a nonzero nonunit element of the Boolean ring \(\mathbb F_2^n\) with its support \(A\), a nonempty proper subset of a fixed \(n\)-element universe \(U\). Then \(E(A,B)\) means \(A\cap B=\varnothing\), with the usual requirement \(A\ne B\); disjoint nonempty sets are automatically distinct. The graph signature contains no predicate for containment and no named empty or full set. The notation \(\equiv_3\) denotes agreement on all first-order sentences of quantifier rank at most three, equivalently a Duplicator win in the three-round Ehrenfeucht–Fraïssé game.

## Proof

**Pair-extension lemma.** Fix \(n\ge4\), vertices \(A,B\), and select a third vertex \(C\). The complete atomic diagram of \((A,B,C)\) is determined by equality among the three vertices and their three possible edges. For \(C\notin\{A,B\}\), write its incidence word \((\varepsilon_A,\varepsilon_B)=(\mathbf1_{E(A,C)},\mathbf1_{E(B,C)})\). Every possible ordered pair \((A,B)\) is covered by exactly one of the following nine cases. The displayed set \(T\) gives **all** possible incidence words for third vertices distinct from both \(A,B\).

| Case | Description of \((A,B)\) | \(T\) |
| --- | --- | --- |
| Q | \(A=B\) | \(\{00,11\}\) |
| P | \(A\subsetneq B\) | \(\{00,10,11\}\) |
| P' | \(B\subsetneq A\) | \(\{00,01,11\}\) |
| I | \(A\cap B\ne\varnothing\), incomparable, \(A\cup B=U\) | \(\{00,01,10\}\) |
| I' | \(A\cap B\ne\varnothing\), incomparable, \(A\cup B\ne U\) | \(\{00,01,10,11\}\) |
| D | \(A\cap B=\varnothing\), \(A\cup B\ne U\) | \(\{00,01,10,11\}\) |
| F | \(A\cap B=\varnothing\), \(A\cup B=U\), \(|A|=1\) | \(\{00,10\}\) |
| F' | \(A\cap B=\varnothing\), \(A\cup B=U\), \(|B|=1\) | \(\{00,01\}\) |
| H | \(A\cap B=\varnothing\), \(A\cup B=U\), \(|A|,|B|\ge2\) | \(\{00,01,10\}\) |

Here \(Q\) additionally has the unique equality response \(C=A=B\). Every other row has the two equality responses \(C=A\) and \(C=B\). For distinct \(A,B\), their mutual edge is present exactly in rows \(D,F,F',H\). Therefore two pairs belonging to the same row admit precisely the same atomic diagrams of all one-vertex extensions.

For completeness, the table has a direct set-theoretic verification. If \(A\subsetneq B\), a vertex disjoint from \(B\) is disjoint from \(A\), ruling out \(01\); the remaining words are realized by a point of \(B\setminus A\), a point outside \(B\), and a set \(A\cup\{u\}\) for \(u\notin B\). The reverse containment row is symmetric. For incomparable intersecting pairs, points in \(A\cap B\), \(A\setminus B\), and \(B\setminus A\) realize \(00,01,10\), and a point outside their union realizes \(11\) exactly when that outside region is nonempty. For disjoint pairs whose union is proper, a point outside the union realizes \(11\), the union itself realizes \(00\), and suitable subsets meeting exactly one of \(A,B\) realize \(01,10\); adding one outside point when necessary avoids equality with \(A\) or \(B\). For complementary disjoint pairs, \(11\) is impossible; a third vertex that intersects both is obtained by taking one point from each side (the universe has at least four points). A proper nonempty subset of a complementary side realizes the mixed word precisely when that side has at least two points. Finally, if \(A=B\), a complement point realizes \(11\) and a distinct vertex intersecting \(A\) realizes \(00\). These constructions remain valid for every \(n\ge4\).

**One-point lemma.** The set of rows obtainable by choosing a second vertex \(B\), when the first is \(A\), depends only on one of three cardinality categories. All rows indicated below are attainable for *every* \(n\ge4\):

| Category for \(A\) | Attainable pair rows |
| --- | --- |
| S: \(|A|=1\) | \(Q,P,D,F\) |
| M: \(2\le |A|\le n-2\) | \(Q,P,P',I,I',D,H\) |
| L: \(|A|=n-1\) | \(Q,P',I,F'\) |

The table follows by choosing \(B\) as \(A\), a proper subset or superset, a complement, a singleton outside \(A\), or an overlapping set with and without a missing outside point, as indicated by the row definitions. To verify the boundary case \(n=4\) in category M, take \(A=\{1,2\}\); every indicated row has a witness. The same constructions work in each larger universe. The omitted rows are excluded by the defining sizes and containment/disjointness relations.

**Three-round game.** Let \(m,n\ge4\). On the first move Duplicator chooses a vertex in the same category S, M, or L. All three categories occur in both universes. On the second move she chooses a response belonging to the same row of the pair-extension table, possible by the one-point lemma. On the third move she chooses a response realizing the same equality case or incidence word, possible by the pair-extension lemma. Hence all equality and adjacency atoms are preserved after three rounds, proving \(\Gamma_m\equiv_3\Gamma_n\).

**Sharpness.** A triangle of three pairwise adjacent vertices exists exactly when \(n\ge3\), witnessed by three singleton supports. The graph \(\Gamma_2\) has no triangle. A rank-three sentence distinguishes \(\Gamma_3\) from all \(\Gamma_n\) with \(n\ge4\):

\[
\begin{aligned}
\exists x\,\exists y\,[\,&x\ne y\land\neg E(x,y)\\
&\land(\exists z\,[E(x,z)\land E(y,z)])\\
&\land(\exists z\,[E(x,z)\land\neg E(y,z)])\\
&\land(\exists z\,[\neg E(x,z)\land E(y,z)])\,].
\end{aligned}
\]

The first two conditions force intersecting distinct supports. The two asymmetric-neighbour conditions force both \(A\setminus B\) and \(B\setminus A\) to be nonempty, while a common neighbour forces \(U\setminus(A\cup B)\ne\varnothing\). Together with \(A\cap B\ne\varnothing\), these are four disjoint nonempty regions, requiring \(n\ge4\). Conversely, with four ground points take \(A=\{1,2\}\), \(B=\{2,3\}\); witnesses \(\{4\},\{3\},\{1\}\) satisfy the three existential clauses. Thus the three classes are distinct and the threshold and bound are sharp.

## Verification

The standalone `verify_direct.py` enumerates all vertices and complete ordered-triple atomic diagrams, then recursively computes the exact three-round types, for \(2\le n\le7\). `verify_structural.py` independently enumerates all four-region count vectors and all possible extensions, checking the nine-row table and three-category table for every \(4\le n\le12\). `run_verification.sh` runs both with standard Python 3 and produces `verification_output.txt`. These finite checks corroborate, but do not replace, the preceding uniform set-theoretic proof.

## Relationship to prior work

LaGrange (2007), *Complemented zero-divisor graphs and Boolean rings*, studies how Boolean-ring structure is recognized from the **whole graph**, including uniqueness of complements and graph-isomorphism rigidity (Theorem 4.1). Mohammadian (2011), *On zero-divisor graphs of Boolean rings*, extends ring recovery from full graph isomorphisms (Theorem 7). These results distinguish full graphs; neither states or implies the present **quantifier-rank-three** equivalence classification, which permits nonisomorphic graphs to become indistinguishable. A separate published result on the usual **full Boolean-algebra signature** gives the cutoff \(2^q\) for quantifier rank \(q\); its cutoff at rank three is eight, and its richer language does not imply the sharp cutoff four in the adjacency-only graph reduct. Bounded-depth logic on these graphs is a different invariant from graph isomorphism or first-order logic in the complete Boolean-algebra language.

## Limitations

This result applies only to finite Boolean rings with at least two field factors, using the simple zero-divisor graph with exactly one adjacency predicate and equality. It does not treat infinite Boolean rings, the ring-operation language, arbitrary products of fields with nonbinary factors, or quantifier ranks above three. The priority comparison includes accessible primary treatments of the same graph class and targeted record searches; older unindexed model-theoretic treatments remain a possible historical risk. Independent mathematical audit has not been performed.

## References

1. J. D. LaGrange, *Complemented zero-divisor graphs and Boolean rings*, Journal of Algebra **315** (2007), 600–611. DOI: https://doi.org/10.1016/j.jalgebra.2006.12.030 (available online 12 March 2007; full text inspected through an accessible article transcription).
2. A. Mohammadian, *On zero-divisor graphs of Boolean rings*, Pacific Journal of Mathematics **251** (2011), 375–383. DOI: https://doi.org/10.2140/pjm.2011.251.375; open PDF: https://msp.org/pjm/2011/251-2/pjm-v251-n2-p07-p.pdf.
3. *Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras*, publicly indexed mathematical research result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-2-q-atom-visibility-threshold-for-finite-boolean-algebras--938cb5f89dc7 (record summary consulted; complete text not accessible during this comparison).
