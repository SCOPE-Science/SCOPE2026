# Sharp periodic-preimage lifting spectrum for all elementary cellular automata

## Finding
For each of the 256 binary elementary cellular automata \(F_r\), let \(Y_r=F_r(\{0,1\}^{\mathbb Z})\) be its **one-step spatial image**, and let \(P_n=\{x:\sigma^n x=x\}\), with periods permitted to divide \(n\). Define the lifting index
\[
B(r)=\min\left\{b\ge1:\ \forall n\ge1\ \forall y\in Y_r\cap P_n\ \exists k\in\{1,\ldots,b\}\ \exists x\in P_{kn},\ F_r(x)=y\right\}.
\]
The complete sharp spectrum is
\[
\#\{r:B(r)=1,2,3,4\}=(156,82,16,2),\qquad \max_r B(r)=4.
\]
Exactly the 16 rules
`22, 30, 86, 94, 104, 106, 120, 122, 133, 135, 149, 151, 161, 169, 225, 233`
have \(B(r)=3\). Exactly `90, 165` have \(B(r)=4\). Every other rule has index one or two; `classification.csv` gives its exact index, smallest witness and finite-relation-semigroup cardinality. The sixteen triple-index rules form three orbits of sizes \(4,8,4\) under left-right reflection and independent input/output bit complementation; the quadruple-index rules form a two-element orbit.

The spectrum is already witnessed at **output periods at most three**: for every rule \(r\) with \(B(r)>1\), a word \(w\) of length at most three has \(w^{\mathbb Z}\in Y_r\) but admits no antecedent of period \(k|w|\) for any \(1\le k<B(r)\). The bound three is sharp: the ten rules `41, 97, 105, 107, 121, 134, 148, 150, 158, 214` first attain their worst obstruction at length three. For example, Rule 41 maps the period-six configuration \((010100)^{\mathbb Z}\) onto \((001)^{\mathbb Z}\), but the latter has no period-three antecedent. Rule 90 requires fourfold lifting of the uniform-one output; Rule 165 requires fourfold lifting of the uniform-zero output, both realized by \((0011)^{\mathbb Z}\).

## Assumptions and scope
For every integer \(0\le r<256\), write the Wolfram local rule as
\[
(F_r x)_i=\left\lfloor \frac{r}{2^{4x_{i-1}+2x_i+x_{i+1}}}\right\rfloor\bmod2.
\]
The global map acts on the **bilateral** full shift \(\{0,1\}^{\mathbb Z}\), not on finite zero-boundary intervals. We quantify over every \(n\ge1\) and over every image point of spatial period dividing \(n\). The multiplier \(k\le B(r)\) is allowed to depend on the point; the theorem does **not** claim that exactly \(B(r)n\) works for all points. This is spatial lifting through one application of \(F_r\), not temporal periodicity under iterates of \(F_r\).

## Proof
Construct a four-vertex labeled de Bruijn graph with vertices `00, 01, 10, 11`. For every input triple \(abc\in\{0,1\}^3\), draw the edge \(ab\to bc\), labeled \(f_r(abc)\). Let \(R_r(0)\) and \(R_r(1)\) be the corresponding Boolean \(4\times4\) adjacency matrices. For a finite nonempty output word \(w=w_1\cdots w_n\), define
\[
R_r(w)=R_r(w_1)\odot\cdots\odot R_r(w_n),
\]
where \(\odot\) is Boolean matrix multiplication. The directed graph of \(R_r(w)\) has an edge from a starting de Bruijn state to an ending state precisely when a path labeled \(w\) connects them.

**Period-lifting lemma.** The periodic configuration \(w^{\mathbb Z}\) lies in \(Y_r\) if and only if \(R_r(w)\) has a directed cycle. It admits an antecedent in \(P_{kn}\) if and only if \(R_r(w)^k\) has a nonzero diagonal entry, equivalently if the relation graph has a closed directed walk of length \(k\). To see the forward implication, divide a bi-infinite antecedent path into blocks of \(n\) labeled edges; the resulting bi-infinite walk in a finite directed graph contains a cycle. Conversely, a cycle of length \(k\) in this graph concatenates its \(n\)-step paths into a bi-infinite antecedent with period dividing \(kn\). This proves both directions without assuming that the antecedent of a periodic image was initially periodic.

Every cyclic directed graph on four vertices has a *simple* directed cycle of length at most four. Consequently \(B(r)\le4\). More precisely let \(g(A)\) be the shortest directed-cycle length of a Boolean relation \(A\), and let \(g(A)=0\) for an acyclic relation. The lemma gives
\[
B(r)=\max\{g(A):A\in\langle I,R_r(0),R_r(1)\rangle,\ g(A)>0\},
\]
where the finite monoid includes the identity and uses Boolean matrix multiplication. Its addition of the empty word does not change the maximum when all words are nonempty. There are only \(2^{16}\) possible Boolean relations, so exhaustive closure terminates and covers **every** finite output word; this is not an inference from a bounded word-length experiment.

`verify.py` makes this finite argument fully reproducible. For each rule, it initializes the identity and repeatedly right-multiplies every newly reached relation by both label matrices, marking every new relation until a complete closure is obtained. One encoding stores each matrix as sixteen integer bits and detects the minimum \(k\in\{1,2,3,4\}\) with a nonzero diagonal in \(A^k\). A second encoding stores four row-bitmasks and independently constructs the closure; a separate exhaustive simple-cycle depth-first search independently computes the girth of each relation. Equality of the two closures and girths is checked for **every** rule and **every** reached relation.

Taking the maximum finite girth gives the four multiplicity classes and the full 256-row table `classification.csv`. Breadth-first parent pointers retain shortest output-word witnesses to each relation. The maximum of these witness lengths over rules with \(B(r)>1\) is three, and the ten first-attaining-length-three rules are exactly those listed above. Input flip, output flip and reflection preserve the lifting index; closing the two exceptional classes under these operations verifies the orbit decomposition stated in the finding. The two direct samples \(F_{90}((0011)^{\mathbb Z})=1^{\mathbb Z}\) and \(F_{165}((0011)^{\mathbb Z})=0^{\mathbb Z}\) explain the sharp fourfold cases. All asserted counts, lists, minimal witnesses and orbit sizes are exact outputs of the finite-closure certificate, not estimates.

## Verification
Run `python3 verify.py` with `classification.csv` beside it. The verifier checks each of 256 rule tables, closes two differently encoded relation semigroups, compares each relation's Boolean-power cycle minimum with a separate four-vertex graph search, checks the entire table and its exceptional lists, recomputes the symmetry orbits, and crosschecks 65,024 finite cyclic output words for all ring lengths one through seven against independently enumerated ring inputs. The last finite-ring checks are supplementary; exhaustive relation closure and the period-lifting lemma certify all lengths. The largest reached semigroup has 2,375 relations. No external numerical library or unstated data are needed.

## Relationship to prior work
Salo and Törmä's *Category Theory of Symbolic Dynamics* (original public preprint 2013) develops symbolic-dynamical structure and periodic-point conditions for sections of block maps. Castillo-Ramírez and Gadouleau study von Neumann regularity of cellular automata and give individual fixed-output obstructions, while Salo's subsequent detailed treatment proves the weak same-period condition for several individual elementary rules and its failure for Rule 41. In particular, Rule 41's specific three-period example already appears in Salo's Proposition 19; it is **not claimed as independently novel** here. Meunier's systematic classification of elementary rules concerns communication complexity rather than optimal spatial-period multipliers. The new assertion is the *complete sharp quantitative lifting-index census across all 256 rules*, the global bound four with its two maximizers, and the universal sharp length-three witness cutoff. Existing conditions about same-period sections or individual examples do not by themselves imply the four-class exact enumeration.

## Limitations
This is a classification of the 256 nearest-neighbor binary rules under the stated index. It does not extend automatically to larger neighborhoods, other alphabets or arbitrary finite-state transducers. An earlier implicit equivalent classification in a less searchable cellular-automaton catalogue cannot be ruled out. The finite closure is exact and exhaustive for each rule, but the scientific priority assessment remains subject to broader historical inspection and independent audit. The calculation does not concern higher temporal iterates or existence of continuous global right inverses.

## References
- V. Salo and I. Törmä, *Category Theory of Symbolic Dynamics*, arXiv:1309.2456, first submitted 2013-09-10. https://arxiv.org/abs/1309.2456
- P.-É. Meunier, *Unraveling simplicity in elementary cellular automata*, arXiv:1406.5306, submitted 2014-06-20. https://arxiv.org/abs/1406.5306
- S. Castillo-Ramírez and M. Gadouleau, *Von Neumann Regular Cellular Automata*, arXiv:1701.02692. https://arxiv.org/abs/1701.02692
- V. Salo, *On von Neumann regularity of cellular automata*, arXiv:2209.13373; *Natural Computing* 22 (2023), 527–538. https://doi.org/10.1007/s11047-022-09935-w
