# Graph-negation strata and an exact census of fundamental preconditionals on the eight-element Boolean algebra

## Finding

Let \(X=\{1,2,3\}\), and regard the eight-element Boolean algebra as \(\mathcal B=\mathcal P(X)\), with subset order. A **fundamental preconditional expansion** of \(\mathcal B\) is a binary operation \(\to\) satisfying the five preconditional laws (P1)–(P5) below and Chen's additional conditions of conditional identity, semicomplementation, and double-negation inflation. The atoms \(1,2,3\) are distinguished when counting labeled operations.

**Theorem.** Exactly \(1021\) labeled fundamental preconditionals exist on \(\mathcal B\), constituting exactly \(194\) isomorphism classes under permutations of its three atoms. Every operation induces a unique simple graph on the atoms by
\[
\{i,j\}\in E(G)\quad\Longleftrightarrow\quad i\in \bigl(\{j\}\to\varnothing\bigr).
\]
The counts over each *labeled* graph depend only on the graph type:

| Negation graph | Number of such graphs | Operations per graph | Subtotal |
| --- | ---: | ---: | ---: |
| Edgeless | 1 | 729 | 729 |
| One edge | 3 | 81 | 243 |
| Two-edge path | 3 | 16 | 48 |
| Triangle | 1 | 1 | 1 |

More generally, for any set \(Y\) and every simple undirected graph \(G\) on \(Y\), its common-neighbor polarity is induced by some fundamental preconditional on \(\mathcal P(Y)\). An explicit one is
\[
A\to_G B=(A\cap B)\cup N_G(A\setminus B),\qquad
N_G(S)=\{v\in Y:\text{for every }s\in S,\;\{v,s\}\in E(G)\}.
\]
Here \(N_G(\varnothing)=Y\). The unrestricted graph-realization statement does not assert uniqueness of a preconditional extending a prescribed graph.

## Assumptions and scope

The foundational laws, for all \(a,b,c\) in a bounded lattice, are
\[
\begin{aligned}
\mathrm{(P1)}&\quad 1\to a\le a,\\
\mathrm{(P2)}&\quad a\wedge b\le a\to b,\\
\mathrm{(P3)}&\quad a\to b\le a\to(a\wedge b),\\
\mathrm{(P4)}&\quad a\to(b\wedge c)\le a\to b,\\
\mathrm{(P5)}&\quad a\to((a\wedge b)\to c)\le(a\wedge b)\to c.
\end{aligned}
\]
Writing \(\nu(a)=a\to0\), the extra laws are \(a\to a=1\), \(a\wedge\nu(a)=0\), and \(a\le\nu(\nu(a))\). They are exactly the defining algebraic requirements for the \(\mathsf F\)-class in the motivating recent work. No modus ponens, conditional normality, distribution, or weak monotonicity is assumed. The numerical census is **only** for the fixed eight-element Boolean algebra; the graph-realization formula applies to every graph, including infinite graphs. The counts are for binary operations, not just unary negations.

## Proof

**1. From negation to a simple graph.** The preconditional axioms entail antitonicity of \(\nu\): if \(a\le b\) then \(\nu(b)\le\nu(a)\), a standard consequence in the cited primary work. Antitonicity and double-negation inflation imply the self-adjoint polarity law
\[
a\le\nu(b)\quad\Longleftrightarrow\quad b\le\nu(a).
\]
Indeed, applying the order-reversing map to \(a\le\nu(b)\) gives \(\nu\nu(b)\le\nu(a)\), and \(b\le\nu\nu(b)\) finishes one direction; the other is symmetric. Semicomplementation gives \(\nu(1)=0\), and double-negation inflation at \(1\) gives \(\nu(0)=1\). On a powerset, self-adjointness implies
\[
\nu(A)=\bigcap_{i\in A}\nu(\{i\}).
\]
Define \(i\sim j\) iff \(i\in\nu(\{j\})\). Self-adjointness makes this relation symmetric, and semicomplementation rules out loops. Thus the relation is a simple graph and \(\nu(A)=N_G(A)\), including at the empty set.

**2. Every graph really occurs.** Take any simple graph on any set \(Y\), define \(N_G\) as in the theorem, and use \(A\to_G B=(A\cap B)\cup N_G(A\setminus B)\). This operation is insensitive to parts of \(B\) outside \(A\), so (P3) holds with equality. For (P1), \(N_G(Y\setminus B)\subseteq B\), because a vertex outside \(B\) cannot be adjacent to itself. (P2) is immediate. For (P4), increasing \(B\) increases both \(A\cap B\) and \(N_G(A\setminus B)\), since common-neighbor sets reverse inclusions of their arguments.

For (P5), write \(D=A\cap B\) and \(Z=D\to_G C=(D\cap C)\cup N_G(D\setminus C)\). Irreflexivity implies \(D\setminus C\subseteq A\setminus Z\); hence \(N_G(A\setminus Z)\subseteq N_G(D\setminus C)\subseteq Z\). Thus \(A\to_G Z\subseteq Z\), the desired law. Conditional identity follows from \(N_G(\varnothing)=Y\). The induced negation is exactly \(N_G(A)\), which is a semicomplementation (no loops) and is doubly inflationary (symmetry). This proves realizability without any finiteness assumption.

**3. Reduction to three independent two-atom rows.** Return to \(X=\{1,2,3\}\). For any candidate \(\to\), put \(f_A(C)=A\to C\) for \(C\subseteq A\). From (P3) and (P4) we have \(A\to B=f_A(A\cap B)\), and \(f_A\) is order preserving. By (P1), (P2), and conditional identity,
\[
f_X(C)=C,\qquad f_{\varnothing}(\varnothing)=X,\qquad
f_{\{i\}}(\varnothing)=N_G(\{i\}),\quad f_{\{i\}}(\{i\})=X.
\]
For \(A=\{i,j\}\), let \(k\) be the remaining atom. The bottom and top row entries are fixed as
\[
f_A(\varnothing)=N_G(\{i,j\}),\qquad f_A(A)=X.
\]
Each remaining entry \(f_A(\{i\})\) must contain \(i\) by (P2). Apply (P5) with both antecedents equal to \(A\); it gives \(f_A(f_A(\{i\}))\subseteq f_A(\{i\})\). If \(j\) belonged to \(f_A(\{i\})\), then its \(A\)-section would equal \(A\), so conditional identity would force \(f_A(\{i\})=X\). Therefore the only three initial possibilities are
\[
\{i\},\qquad \{i,k\},\qquad X.
\]
The same alternatives hold with \(i,j\) interchanged. Monotonicity further requires each entry to contain \(N_G(A)\). In the remaining instances of (P5) with a two-atom outer antecedent and singleton inner antecedent, the only nontrivial constraints are
\[
f_A(A\cap N_G(\{i\}))\subseteq N_G(\{i\}),\qquad
f_A(A\cap N_G(\{j\}))\subseteq N_G(\{j\}).
\]
All other instances have outer antecedent \(X\) (where \(f_X\) is the identity), inner antecedent \(\varnothing\) (where the inner output is \(X\)), or the same two-atom antecedent (already handled by the three alternatives). Distinct two-atom antecedents are incomparable; therefore their row choices are independent once \(G\) is fixed. Conversely, the displayed conditions ensure all five laws plus the three additional \(\mathsf F\)-laws. This is an exact normal form, not merely a computational filter.

**4. Enumeration by graph.** If \(G\) is edgeless, every two-atom row offers three choices for each singleton input, hence \(9^3=729\). With a single edge \(\{i,j\}\), the row for antecedent \(\{i,j\}\) is fixed by the singleton-negation constraints, and the other two offer nine choices each: \(9^2=81\). For a path \(i-j-k\), the row on the two endpoints has four choices (both values must contain the central atom), and each incident-edge row has two choices, giving \(4\cdot2\cdot2=16\). In the triangle, all rows are forced, giving one operation. Summing over the labeled graphs gives
\[
729+3\cdot81+3\cdot16+1=1021.
\]

**5. Isomorphism classes.** Every Boolean-lattice automorphism permutes the three atoms, so use Burnside's lemma for the action of \(S_3\) on the \(1021\) binary operations. The identity fixes all \(1021\). A transposition can preserve only the edgeless graph, its fixed edge, the path centered at its fixed vertex, or the triangle; these contribute \(27,9,4,1\), respectively, giving \(41\) fixed operations. A three-cycle preserves only the edgeless graph and the triangle, giving \(9+1=10\) fixed operations. Hence
\[
\frac{1021+3\cdot41+2\cdot10}{6}=194.
\]
This completes the proof.

## Verification

Two standalone checkers are provided. `verify_exhaustive.cpp` independently constructs every row allowed by (P1)–(P4), conditional identity, and semicomplementation, then checks (P5) and double-negation inflation. It examines all \(512000\) candidate combinations, obtains \(1021\) valid \(\mathsf F\)-operations, computes every graph stratum, and counts permutation fixed points. Its larger intermediate count for the \(\mathsf T\)-class is not part of the claimed finding. `verify_graph.py` independently generates operations graph-first, checks all five original preconditional laws literally on all triples, verifies the \(\mathsf F\)-laws, and computes the same graph and isomorphism counts. It also checks the general graph-construction formula over all \(75\) simple labeled graphs on one through four vertices. The unbounded realization theorem is proved in Section 2, not inferred from these tests.

Reproduce using ordinary tools from the directory containing these source files:

```sh
g++ -std=c++17 -O2 verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
python3 verify_graph.py
```

Expected terminal markers are `DIRECT_CENSUS_OK` and `GRAPH_CLASSIFICATION_OK`.

## Relationship to prior work

Chen's 2026 paper defines the \(\mathsf K\), \(\mathsf T\), and \(\mathsf F\) algebras and proves general proof-theoretic, relational, and finite-model results. Holliday's earlier paper establishes the five preconditional axioms, representation results, the connection to precomplementations, and the rigidity of preconditionals under involutive negation. Neither inspected relevant treatment gives the present eight-element Boolean \(\mathsf F\)-operation count, its graph-resolved row normal form, or the corresponding orbit count. Published related calculations concern finite chains and height-two lattices, including the known four-element Boolean boundary; they do not imply the first three-atom Boolean case. The graph polarity underlying unary weak negations is standard background rather than a claimed new discovery. The claimed contribution is the full **binary conditional** census, the compatibility calculation, and the explicit all-graphs realization under the stronger \(\mathsf F\) laws.

## Limitations

The number \(1021\) is not asserted for arbitrary eight-element bounded lattices or for the weaker \(\mathsf K\) or \(\mathsf T\) classes. No general closed enumeration formula for \(n\)-atom Boolean \(\mathsf F\)-algebras is supplied when \(n\ge4\). Computational exhaustiveness applies only to the specified finite algebra; the universal graph construction relies on the direct proof. An equivalent enumeration could exist in earlier unindexed conditional-algebra or polarity literature, notwithstanding the explicit source and implication comparisons made here. Independent scholarly audit has not been performed.

## References

1. Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221v1, publicly submitted 22 July 2026, especially Definitions 3.1 and 3.3 and Examples 3.6–3.7. https://arxiv.org/abs/2607.20221
2. Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, initial version publicly submitted 3 February 2024; in *The Logica Yearbook 2023* (2025), especially Definition 1, Proposition 4, Proposition 10, and the finite Boolean selection-frame discussion. https://arxiv.org/abs/2402.02296
3. Wesley H. Holliday, *A Fundamental Non-Classical Logic*, *Logics* **1** (2023), 36–79, DOI:10.3390/logics1010004, for the weak-pseudocomplementation background. https://doi.org/10.3390/logics1010004
