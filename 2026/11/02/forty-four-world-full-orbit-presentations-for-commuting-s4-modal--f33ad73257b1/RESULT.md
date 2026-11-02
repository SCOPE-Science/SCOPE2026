# Forty four-world full-orbit presentations for commuting \(\mathrm{S4}\) modalities

## Finding
Let \(W\) be a finite set. For an ordered pair \((P,Q)\) of partial orders on \(W\), use the normal additive possibility operators
\[
\Diamond_P(U)=\{y\in W:\exists x\in U\ (xPy)\},\qquad
\Diamond_Q(U)=\{y\in W:\exists x\in U\ (xQy)\}.
\]
Both operators are extensive and idempotent (thus satisfy the Boolean-algebraic \(\mathrm{S4}\) conditions). Require \(\Diamond_P\Diamond_Q=\Diamond_Q\Diamond_P\) on every subset. For an interpretation \(A\subseteq W\) of one propositional letter, let \(\mathcal O(P,Q,A)\) be all truth sets obtained from that letter using only the three unary operations \(\neg\), \(\Diamond_P\), and \(\Diamond_Q\), with arbitrarily nested applications and **no binary Boolean operations**.

**Theorem (sharp full-orbit threshold and four-world census).** The smallest possible cardinality of \(W\) for which \(|\mathcal O(P,Q,A)|\ge15\) is four. On four worlds the full orbit of all \(16\) subsets is attainable, even with both orders antisymmetric and the modalities commuting. Among the ordered, labelled triples \((P,Q,A)\) on a fixed four-element set, **exactly \(960\)** have \(|\mathcal O(P,Q,A)|=16\). These triples form **exactly \(40\)** isomorphism classes under simultaneous renaming of worlds. Every successful labelled triple has trivial automorphism group.

Every successful four-world triple uses **incomparable** orders; no comparable ordered pair of four-world partial orders has a full sixteen-set unary orbit. Across the successful triples, the seed has cardinality one, two, or three in respectively \(168,624,168\) cases. The least possible combined number of strict relation edges is four, attained by the displayed witness. These are finite-classification consequences of the same exhaustive test.

The exact number of full-orbit triples on fixed labelled universes of sizes \(1,2,3,4\), respectively, is \(2,16,180,960\). These numbers concern full orbits relative to \(2^{|W|}\), not the least threshold for exceeding fourteen. The four-world orbit-size histogram across all commuting ordered partial-order pairs and all seeds, in increasing orbit size \(2,4,6,8,10,12,14,16\), is
\[
(48124,102252,107568,59376,29280,12144,4056,960).
\]

## Assumptions and scope
An isomorphism \((P,Q,A)\cong(P',Q',A')\) is a permutation of worlds preserving both **named and ordered** relations and taking \(A\) to \(A'\). The calculation ranges over *all* reflexive, transitive, antisymmetric binary relations on labelled sets; it does not identify the two modalities with one another, permit swapping them, or impose any relationship between their two orders beyond commutation of their induced operators. The closure orientation is stipulated by the displayed forward-image definition; standard Kripke predecessor semantics gives the equivalent statement with both relations reversed.

## Proof
**Algebraic reduction.** A partial order is reflexive and transitive, so its forward-image operator is extensive and idempotent. It preserves the empty set and all unions, hence is a normal modal possibility operator. Conversely, every extensive idempotent normal additive operator on a finite powerset arises uniquely from its singleton images, which define a reflexive transitive relation; antisymmetry is precisely the \(T_0\) restriction. The operators commute on all subsets exactly when they commute on singletons, because they preserve arbitrary unions on a finite set.

**Four-world witness.** Take \(W=\{0,1,2,3\}\). In addition to all reflexive pairs, take exactly these strict comparisons:
\[
P:\quad 0P1,\qquad Q:\quad 0Q2,\ 0Q3,\ 1Q2.
\]
Neither order has any other strict comparison. Both are transitive and antisymmetric. The image row masks, with bit \(i\) representing world \(i\), are respectively \((3,2,4,8)\) and \((13,6,4,8)\). Directly on singleton generators, both composites give \(\{0,1,2,3\}\) at \(\{0\}\), \(\{1,2\}\) at \(\{1\}\), \(\{2\}\) at \(\{2\}\), and \(\{3\}\) at \(\{3\}\). Hence the two operators commute on all subsets.

Set \(A=\{0,2\}\), binary mask \(5\). Here are explicit words producing each of the sixteen truth-set masks; `c` denotes complement, `p` and `q` denote the corresponding possibility operations, `e` the identity, and the rightmost symbol acts first:

```text
mask:word
0:cqp   1:cqc   2:cq    3:pcqc
4:cpcqcq 5:e     6:qcq   7:p
8:cp    9:cqcq  10:c    11:pcqcq
12:cpcqc 13:q   14:qc   15:qp
```

Each word is evaluated against the stated two edge relations and the single initial valuation. The expressions have distinct values, so \(|\mathcal O(P,Q,A)|=16\). If \(|W|\le3\), then \(\mathcal O(P,Q,A)\subseteq\mathcal P(W)\) has at most eight elements. This proves the sharp threshold.

**Exhaustive four-world enumeration.** The standalone `checker.py` is a direct finite exhaustive proof for the exact counts. For size \(n\) it lists the \(2^{n(n-1)}\) off-diagonal relation bit patterns once each, adds all reflexive edges, and retains precisely those satisfying the quantified antisymmetry and transitivity tests. For every ordered pair it evaluates each induced operator on all \(2^n\) subsets and retains exactly the commuting pairs. For every seed it then computes the least subset of \(\mathcal P(W)\) containing that seed and closed under the three unary operations using a finite queue until no new mask is produced. This is exactly the definition of \(\mathcal O\), with no depth cutoff. There are \(219\) labelled partial orders on four points and \(22735\) commuting ordered pairs; checking all sixteen seeds per pair gives the stated histogram and exactly \(960\) full-orbit triples. The checker performs the analogous exhaustive calculations for \(n=1,2,3\). Every loop has explicitly finite, exhaustive bounds and uses only exact integer bit operations.

**From labelled count to isomorphism classes.** The permutation group \(S_4\) acts on the successful triples. Suppose a permutation fixes a successful triple. As it preserves the relations, it commutes with both unary modal operators; preserving the seed makes it fix every member of the unary orbit. Since the orbit is the entire powerset, it fixes in particular all singleton subsets, so it is the identity permutation. Thus every isomorphism orbit has \(|S_4|=24\) labelled triples. It follows that the number of isomorphism classes is exactly \(960/24=40\). The checker also verifies this directly by relabelling all successful triples.

## Verification
Run `python3 checker.py` with standard Python 3 and no external dependencies. The executable enumerates all labelled partial orders through four worlds, tests operator commutation on every subset, computes all least unary orbits, checks the four-world witness, and relabels the maximal triples. Its expected final line is `ALL_CHECKS_OK`; all asserted counts must agree. The finite census is exhaustive, not a sample or heuristic, because it examines every off-diagonal binary relation bit pattern and every interpretation of the single variable. The separate short proof of the threshold and the free group action does not require trusting the count of \(960\).

## Relationship to prior work
Agnew (2026) investigates local finiteness and finite partitions of complex modal algebras on transitive frames, motivating exact small-model generation questions. It studies a single operator and general structural criteria, not this ordered commuting-pair full-orbit census. Shallit and Willard (2011) show that two **abstract** commuting closure operators can produce infinitely many sets on an infinite carrier. Their examples do not impose both finitary topological union preservation and antisymmetric finite relations, and they do not give the four-world minimum or its \(40\) classes. Banakh et al. (2015) prove operator-monoid bounds for **comparable** pairs of topologies and discuss incomparable examples. The present four-world orders are incomparable; their global operator-monoid bounds do not imply the fixed-valuation, four-world maximal-orbit count. The classical Kuratowski theorem concerns one closure and complement, for which the global upper bound is fourteen. None of these cited statements alone entails the exact finite census here.

## Limitations
The \(960\) and \(40\) numbers are proved by a reproducible, finite exhaustive calculation, not by a closed-form enumeration by structural classes. The orbit-generation operation deliberately excludes Boolean conjunction and disjunction. The result does not classify higher carrier sizes, the case of arbitrary preorders with nontrivial clusters, or the effect of exchanging the two named modalities in the isomorphism notion. A historically older finite-topology classification under another terminology may subsume the census; the accessible literature comparison does not establish absolute priority. All conclusions are mathematical statements about the described finite models, not claims of independent certification.

## References
1. Gabriel Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941, first version 2026-06-01. https://arxiv.org/abs/2606.02941
2. Jeffrey Shallit and Ross Willard, *Kuratowski's Theorem for Two Closure Operators*, arXiv:1109.1227, first version 2011-09-06. https://arxiv.org/pdf/1109.1227
3. T. Banakh, O. Chervak, T. Martynyuk, M. Pylypovych, A. Ravsky and M. Simkiv, *Kuratowski monoids of n-topological spaces*, arXiv:1508.07703, first version 2015-08-31. https://arxiv.org/pdf/1508.07703
4. K. Kuratowski, *Sur l'opération A de l'Analysis Situs*, Fundamenta Mathematicae 3 (1922), 182–199.
