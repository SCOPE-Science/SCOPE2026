# Every longer cycle's generalized universal \(FO^3\) theory is strictly contained in the square's

## Finding

Let \(C_n\) be the simple undirected cycle on \(n\ge4\) vertices, regarded as a structure for one binary relation \(R\). Let \(U_3\) be the generalized universal three-variable fragment used by Andréka, van Benthem, and Németi: formulas use only \(x,y,z\), are built from atomic formulas and negated atomic formulas by conjunction, disjunction, and universal quantification.

Then for every \(n\ge5\),
\[
\boxed{\operatorname{Th}_{U_3}(C_n)\subsetneq \operatorname{Th}_{U_3}(C_4).}
\]
Thus the square is not merely the target of the source paper's pentagon-to-square argument: it absorbs the generalized universal \(FO^3\) theory of every longer finite cycle.

The inclusion is strict. The sentence
\[
\eta:=\forall x\forall y\forall z\,
\bigl(\neg Rxy\lor x=z\lor y=z\lor Rxz\lor Ryz\bigr)
\]
holds in \(C_4\), because any third vertex distinct from the endpoints of an edge is adjacent to one endpoint. For every \(n\ge5\), it fails in \(C_n\) at \(x=0,y=1,z=3\).

## Assumptions and scope

The relation \(R\) is the symmetric, irreflexive adjacency relation of the ordinary cycle graph. The theorem concerns sentences in the generalized universal fragment just described, not arbitrary three-variable first-order sentences. Equality is available, as in the source's main example.

The result is a direct finite-model statement. No asymptotic assumption on \(n\) is used: the proof works uniformly for every \(n\ge5\).

## Proof

Andréka, van Benthem, and Németi prove the case \(n=5\): every generalized universal formula using three variables that is true in the pentagon \(C_5\) is true in the square \(C_4\). Their proof dualizes to existential formulas and uses an extension condition on three-variable evaluations. The same idea extends to every longer cycle after strengthening the evaluation invariant by one metric condition.

Write \(V=\{x,y,z\}\). For evaluations \(v:V\to C_4\) and \(w:V\to C_n\), call \((v,w)\) **tight-alike** when:

1. equality patterns agree;
2. adjacency patterns agree; and
3. whenever \(v(u)\) and \(v(u')\) are opposite vertices of \(C_4\), the vertices \(w(u)\) and \(w(u')\) have cycle distance exactly \(2\) in \(C_n\).

The key extension property is:

> If \((v,w)\) is tight-alike and one variable is rebound in \(C_4\) to any vertex \(a\), then that variable can be rebound in \(C_n\) to some vertex \(b\) so that the new evaluations are again tight-alike.

Only the relation between the two unchanged \(C_4\)-values matters.

If they are equal, choose \(b\) to be respectively the same vertex, a neighbor, or a distance-two vertex according to whether \(a\) is equal to, adjacent to, or opposite the fixed value.

If the two fixed values are adjacent, their images in \(C_n\) are adjacent. Besides the two endpoints, the two remaining vertices of \(C_4\) are the off-edge neighbors of the endpoints. In \(C_n\), choose the corresponding off-edge neighbor. It is adjacent to one endpoint and has distance exactly \(2\) from the other.

If the two fixed values are opposite, their images in \(C_n\) have distance exactly \(2\). If \(a\) is one of the fixed values, copy that endpoint. Otherwise \(a\) is adjacent to both fixed vertices in \(C_4\); choose the midpoint of a length-two path between their images in \(C_n\). For \(n\ge5\) this midpoint is available and has exactly the required adjacency pattern. The fact that \(C_4\) has two possible common neighbors causes no problem: the rebinding step has forgotten the previous value of the moved variable, so either choice can be represented by the same midpoint.

Now let \(E_3\) be the dual existential fragment: atomic and negated atomic formulas, conjunction, disjunction, and existential quantification, again using only \(x,y,z\). We prove by structural induction that for every \(\psi\in E_3\),
\[
C_4\models\psi[v]\quad\Longrightarrow\quad C_n\models\psi[w]
\]
whenever \((v,w)\) is tight-alike. Atomic and negated atomic formulas are preserved by conditions 1--2, conjunction and disjunction are immediate, and the existential step is exactly the extension property above.

For a sentence, begin with any constant tight-alike pair of evaluations. Hence every existential \(E_3\)-sentence true in \(C_4\) is true in \(C_n\). Negating gives the desired universal inclusion
\[
\operatorname{Th}_{U_3}(C_n)\subseteq\operatorname{Th}_{U_3}(C_4).
\]
The sentence \(\eta\) displayed above proves strictness for every \(n\ge5\).

## Verification

The original submission reports that its accompanying checker exhaustively replays the tight-alike extension lemma for all three-variable assignments between \(C_4\) and \(C_n\) for \(5\le n\le16\). It separately checks the three canonical fixed-pair cases (equal, adjacent, opposite) for every \(5\le n\le1000\), and verifies the strictness sentence \(\eta\) on \(C_4\) and its explicit counterexample on every \(C_n\) in the same range.

The original recorded output is:

`VERIFY_OK 217057 exact assertions`

The finite replay is a consistency check. The proof above is uniform in \(n\) and establishes the theorem for all \(n\ge5\).

## Relationship to prior work

Andréka, van Benthem, and Németi's 2023 note gives the exact pentagon/square instance. Their Lemma 2 proves that every generalized universal three-variable formula true in \(C_5\) is true in \(C_4\), by showing that existential three-variable truth transfers from \(C_4\) to \(C_5\). They use this in a counterexample to a finite-variable Łos--Tarski preservation property. The paper explicitly presents the construction as an early 1992 example and surveys the broader finite-variable preservation literature.

The additional statement here is the uniform extension from the pentagon to every finite cycle \(C_n\) with \(n\ge5\), together with strictness of the theory inclusion for each \(n\). The extra distance-two clause is what makes the source's “alike evaluations” argument stable when the target cycle grows beyond five vertices.

The original submission recorded exact-phrase searches for universal \(FO^3\) theories of cycles, broader finite-variable/preservation searches, a semantic published-finding corpus search under cycle, square/pentagon, and submodel-preservation aliases, and the current and preceding owned ledgers found the source \(C_5\to C_4\) lemma but no equivalent all-cycle statement. The main residual originality risk is uncatalogued folklore: once the correct invariant is written down, the proof is short.

The comparison was subsequently checked against the complete 2023 note. In C6, an ordinary alike evaluation can send opposite square vertices to vertices 0 and 3. A square common neighbor then has no possible response, so the source’s invariant cannot simply be reused for arbitrary n. The distance-two strengthening above repairs precisely this obstruction. General pebble-game preservation characterizations provide a proof framework; they do not supply this family-specific strategy. Likewise, the stronger failures of preservation surveyed in Section 2 concern other structures and do not imply this prescribed all-cycle inclusion.

Actual corpus queries under generalized universal theory, three-variable cycles, square/pentagon and one-sided game aliases, and comparisons with prior research and published SCOPE records, found no equivalent family statement. The only matching prior research record was this original finding itself. A published pentagonal-antiprism matching-complex result concerns different objects and invariants. No numerical invariant table is applicable to this uniform logical inclusion. The 1995 chapter was not read in full: the repository bibliographic record had no download link, and the attempted author-hosted PDF was unavailable. Its coverage remains a residual priority risk. See AUDIT.json for the exact source-inspection limits and the four originality comparisons.

A separately reconstructed finite check of the distance-preserving assignment relation reproduced the 217057 assertions described above without executing the uploaded checker. This corroborates only the stated finite ranges.

## Limitations

The theorem is one-directional theory inclusion. It does not classify generalized universal \(FO^3\) theory inclusion among two distinct cycles \(C_m,C_n\) with \(m,n\ge5\), and it does not claim that \(C_4\) and longer cycles are equivalent in full \(FO^3\).

The argument uses the very special degree-two geometry of cycles. It should not be read as a general theorem for graphs of maximum degree two without separately treating paths and disjoint unions.

## References

1. H. Andréka, J. van Benthem, I. Németi, *A note on the submodel preservation property in fragments of first-order logic*, arXiv:2303.13222, first submitted 23 March 2023. In particular, Section 1 and Lemma 2 give the pentagon-to-square case and the evaluation-extension proof template.
2. H. Andréka, J. van Benthem, I. Németi, *Submodel Preservation Theorems in Finite-Variable Fragments*, in *Modal Logic and Process Algebra*, CSLI Lecture Notes 53, 1995, pp. 1--11. This is the earlier preservation-theorem context cited by the 2023 note.
3. S. Abramsky, A. Dawar, P. Wang, *The Pebbling Comonad in Finite Model Theory*, LICS 2017, arXiv:1704.05124. This provides broader finite-variable/pebble-game context; the proof above is self-contained and does not depend on its categorical machinery.
