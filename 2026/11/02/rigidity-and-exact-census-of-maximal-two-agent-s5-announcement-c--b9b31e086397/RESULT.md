# Rigidity and exact census of maximal two-agent S5 announcement chains

## Finding

Fix the two-agent epistemic formula
\[
\varphi=(p\to\Diamond_a q)\land(q\to\Diamond_b p).
\]
For every integer \(n\geq 1\), there are **exactly \(2n!\)** labelled, \(n\)-world, two-agent \(\mathsf{S5}\) models over the atomic vocabulary \(\{p,q\}\) whose repeated truthful public announcement of \(\varphi\) deletes exactly one world at each of \(n\) consecutive rounds, leaving no worlds. Up to relabelling, these models comprise **exactly two isomorphism types**.

More precisely, if \(w_1,\ldots,w_n\) is the unique order of deletion, then the atomic truth types of these worlds must alternate between \(P=(p\land\neg q)\) and \(Q=(\neg p\land q)\). The \(a\)-equivalence classes of size two are precisely the pairs \(\{w_{i-1},w_i\}\) for which \(i\geq2\) and \(w_i\) has type \(P\). The \(b\)-equivalence classes of size two are precisely the pairs \(\{w_{i-1},w_i\}\) for which \(i\geq2\) and \(w_i\) has type \(Q\). All other equivalence classes are singletons. Conversely, every such alternating path has the asserted deletion order. Its labelling and choice of initial truth type are the only parameters.

For the same formula, if the agents have *the same* equivalence relation, announcements stabilize after at most one round for every finite model. Thus the arbitrarily long finite chains genuinely require two different epistemic partitions.

## Assumptions and scope

Let \(W\) be a fixed labelled set of size \(n\geq1\), and let \(E_a,E_b\) be equivalence relations on \(W\). Let \(V(p),V(q)\subseteq W\) be arbitrary independently chosen truth sets. The models counted are the quadruples \((W,E_a,E_b,V)\) with this fixed two-atom vocabulary, and not structures with additional freely valued atoms. All accessibility relations are restricted to the surviving worlds after each announcement; atom valuations are restricted in the same way. In particular, every nonempty induced submodel is again \(\mathsf{S5}\).

For a set of surviving worlds \(X\subseteq W\), put
\[
F(X)=\{w\in X:(w\notin V(p)\ \text{or}\ [w]_a\cap X\cap V(q)\ne\varnothing)
\ \text{and}\
(w\notin V(q)\ \text{or}\ [w]_b\cap X\cap V(p)\ne\varnothing)\}.
\]
Set \(W_0=W\) and \(W_{t+1}=F(W_t)\). The empty set is used solely as the terminal bookkeeping state; no claim is made that an empty Kripke model has an actual point at which a formula can be evaluated. An \(n\)-round extinction means \(W_{t+1}\subsetneq W_t\) for all \(0\leq t<n\) and \(W_n=\varnothing\). As a trivial size bound, no process can have more than \(n\) strict deletions. The contribution concerns **all equality cases**, their rigidity, and their exact census—not the size bound alone.

## Proof

**1. A fixed dependency digraph.** Partition \(W\) into its four atomic types \(P=p\land\neg q\), \(Q=\neg p\land q\), \(B=p\land q\) and \(Z=\neg p\land\neg q\). Build a digraph \(D\) on \(W\) as follows. From a \(P\)-vertex \(w\), draw an edge to every \(v\in[w]_a\cap V(q)\); from a \(Q\)-vertex \(w\), draw an edge to every \(v\in[w]_b\cap V(p)\). Give every \(B\)- and \(Z\)-vertex a self-loop. This digraph is defined from the *original* model and does not change during iteration.

By induction on \(t\), a vertex belongs to \(W_t\) if and only if it starts a directed walk of length \(t\) in \(D\). The assertion is trivial for \(t=0\). Assuming it for \(t\), a vertex can start a walk of length \(t+1\) if and only if it has a successor in \(W_t\). This implies that it is itself in \(W_t\) by taking the initial segment of the walk. The rule for \(F\) then agrees exactly with the edge-existence condition, for each of the four atomic types. In particular, all \(B\)- and \(Z\)-vertices survive indefinitely, and for a finite model the eventual survivor set is exactly the set of vertices from which some directed cycle is reachable.

**2. Consequences of maximal extinction.** Suppose there are \(n\) strict deletion rounds. Exactly one world must be deleted at each round, because there are only \(n\) worlds. Denote the world deleted in round \(i\) by \(w_i\), for \(1\leq i\leq n\), and write \(d(w_i)=i\). All worlds have type \(P\) or \(Q\), by the self-loop observation.

A \(P\)-world survives one additional round precisely while some \(Q\)-world in its \(a\)-class survives the previous round. Hence its deletion time satisfies
\[
d(w)=1+\max\bigl(\{d(v):v\in[w]_a\cap Q\}\cup\{0\}\bigr)
\qquad (w\in P).
\]
Symmetrically,
\[
d(w)=1+\max\bigl(\{d(v):v\in[w]_b\cap P\}\cup\{0\}\bigr)
\qquad (w\in Q).
\]
These formulas follow directly by comparing the last round with an available witness and the first round without one. Since \(d(w_i)=i\), when \(i>1\) the maximum on the right must be attained by \(w_{i-1}\). Therefore \(w_{i-1}\) has the opposite atomic type from \(w_i\); they are \(a\)-equivalent if \(w_i\in P\), and \(b\)-equivalent if \(w_i\in Q\). Thus the deletion-order types alternate.

**3. No additional equivalence links.** Consider any \(a\)-equivalence class. Two distinct \(P\)-worlds in that class have exactly the same set of \(Q\)-witnesses, so the displayed formula gives them equal deletion times. That cannot happen; therefore each \(a\)-class contains at most one \(P\)-world. Every \(Q\)-world \(w_j\) with \(j<n\) is \(a\)-equivalent to \(w_{j+1}\in P\), by the preceding paragraph. Thus, if an \(a\)-class contains \(w_i\in P\), every \(Q\)-world in the class with index below \(n\) must be \(w_{i-1}\). A possible top-ranked \(Q\)-world \(w_n\) cannot be in any \(a\)-class containing a \(P\)-world, because then the \(P\)-world would have deletion time at least \(n+1\). Therefore every nonsingleton \(a\)-class is exactly one pair \(\{w_{i-1},w_i\}\) with \(w_i\in P\). Classes with no \(P\)-world are singletons, since all \(Q\)-worlds except possibly \(w_n\) have already been paired. The same argument with \(P,Q\) and \(a,b\) interchanged gives the asserted complete classification of \(b\)-classes.

**4. Converse and count.** Conversely, choose any ordering \(w_1,\ldots,w_n\) of \(W\), assign alternating \(P/Q\) types in either of two ways, and form the two equivalence partitions from the stated adjacent pairs plus singletons. In the initial model, \(w_1\) has no required opposite-type witness; all later \(w_i\) have the requisite witness \(w_{i-1}\). After deleting \(w_1\), the same assertion holds on the suffix \(w_2,\ldots,w_n\). Induction gives \(W_t=\{w_{t+1},\ldots,w_n\}\) for \(0\leq t\leq n\). Each ordering and each initial truth type yields a different labelled model, because both are uniquely recoverable from the actual deletion trace and valuations. This gives \(2n!\) models. All are isomorphic to one of the two alternating truth-type patterns, which cannot be isomorphic because their first-deleted worlds differ on \(p\).

**5. Identical-agent boundary.** If \(E_a=E_b=E\), work class-by-class in the partition \(E\). A class containing both a \(p\)-world and a \(q\)-world keeps all its points: each \(p\)-world has a \(q\)-witness, each \(q\)-world has a \(p\)-witness, and the remaining worlds satisfy both implications vacuously. A class with no \(p\)-world loses all \(q\)-only worlds in the first round, and a class with no \(q\)-world loses all \(p\)-only worlds in the first round. What remains after that round is stable. Thus \(F(F(W))=F(W)\), even before restricting to finite carriers, and chains of arbitrarily large strict length require distinct agent relations.

## Verification

The standalone `checker.py` independently enumerates all equivalence relations on labelled sets of up to four worlds, all possible \(p/q\) valuations, and every corresponding deletion trace; it checks the full classification and counts. It also enumerates every pair of equivalence relations and every *exclusive* \(P/Q\) valuation on five worlds (the only possible valuation type in an extremal model). The number of finite models checked in these two tests is respectively \(4,64,1600,57600\) for \(n=1,2,3,4\), plus \(86528\) at \(n=5\). The respective maximal-extinction counts are \(2,4,12,48,240\), matching \(2n!\). The checker tests the walk interpretation directly on all these models, and verifies one-round stabilization for all \(3840\) equal-relation models on four worlds. Running `python3 checker.py` yields `ALL_CHECKS_OK`.

These computations are finite consistency checks, not a substitute for the proof for arbitrary \(n\).

## Relationship to prior work

Yamada's 2026 study of eventual and strong eventual announcement phenomena develops different, general temporal conditions for iterated *believed* announcements on \(\mathsf{K45}\) frames and gives alternating two-peeling examples. These concepts motivate studying prolonged announcements, but neither the \(\mathsf{S5}\) finite extremal classification nor the exact \(2n!\) count follows from the stated results. Yamada's earlier 2026 study classifies truth-pattern validity in several epistemic classes; that is a different quantified property from counting labelled models of the fixed formula. Sadzik's 2006 iterated-update study addresses stabilization of more general epistemic events and games, not this extremal fibre rigidity. Miller and Moss's 2005 work studies undecidability of iterated relativization, not an exact finite census. A previously established finite-state argument already gives the elementary upper bound of \(n\) strict reductions; that upper bound is not claimed here.

## Limitations

The full classification is for the stated fixed formula, two labelled agents, the two-atom vocabulary, finite nonempty \(\mathsf{S5}\) frames, and standard *truthful* public-announcement world restriction. It does not count models modulo bisimulation, extend to additional unconstrained atoms, or establish a universal longest-announcement bound as a function of formula size. It is not a result about believed public announcements, which preserve the carrier while changing arrows. The cited classifications of iterated truth-pattern validity were inspected at the level of accessible abstract and cited discussions, not complete primary full text; an equivalent theorem hidden under a different formulation remains a historical-priority risk. No independent mathematical review has been performed.

## References

1. E. Yamada, *Eventual and Strong Eventual Notions in Public Announcements*, arXiv:2609.24006v1 (first posted 21 September 2026), https://arxiv.org/html/2609.24006v1.
2. E. Yamada, *Classification of \(\sigma\)-Validity in Iterated Announcements*, arXiv:2607.04685v3 (2026), https://arxiv.org/abs/2607.04685.
3. T. Sadzik, *Exploring the Iterated Update Universe*, ILLC Prepublication Series PP-2006-26 (2006), https://eprints.illc.uva.nl/id/document/494.
4. J. S. Miller and L. S. Moss, *The Undecidability of Iterated Modal Relativization*, Studia Logica **79** (2005), 373–407, https://doi.org/10.1007/s11225-005-3612-9.
