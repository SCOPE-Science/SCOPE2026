# Exact Observability and Sharp Query Complexity of Finite KD45 Disagreement

## Finding
Let \(W\) be a labelled set of \(n\geq 1\) worlds and let \(r\geq 2\) agents have serial, transitive, Euclidean accessibility relations. An atomic query chooses a truth set \(X\subseteq W\) and observes, simultaneously at every world, the disagreement predicate
\[
\mathsf{DG}(X)(w)\quad\Longleftrightarrow\quad
\bigvee_{a,b=1}^{r}\bigl(R_a(w)\subseteq X\ \wedge\ R_b(w)\subseteq W\setminus X\bigr).
\]
The object to be identified is the full unary map \(\mathsf{DG}:\mathcal P(W)\to\mathcal P(W)\), not the underlying named accessibility relations.

**Theorem A (sharp reconstruction).** The exact deterministic worst-case number of atomic queries required to identify this map, even with adaptive choice and a full \(n\)-bit answer to each query, is
\[
q(n,r)=2^{n-1}-1.
\]
A nonadaptive query collection identifies every such operator if and only if it meets every complementary pair \(\{X,W\setminus X\}\) with \(\varnothing\subsetneq X\subsetneq W\). Every minimum collection takes exactly one member of each pair; therefore precisely \(2^{2^{n-1}-1}\) minimum query collections exist.

**Theorem B (complete two-agent pointed quotient).** At any fixed world, when \(r=2\), write \(A=R_1(w)\) and \(B=R_2(w)\). The pointed input-output predicate vanishes identically exactly when \(A\cap B\neq\varnothing\). Otherwise it determines the unordered pair \(\{A,B\}\) uniquely: \(A\) and \(B\) are exactly its inclusion-minimal positive inputs. Consequently the number of distinct pointed predicates on a labelled \(n\)-world carrier is
\[
\boxed{u_n=1+\frac{3^n-2^{n+1}+1}{2}}.
\]
Each nonzero predicate has exactly two ordered nonempty successor-pair representations, while the zero predicate has \((2^n-1)^2-(3^n-2^{n+1}+1)\) such representations. Every pointed representation is realizable in a serial, transitive, Euclidean frame, so these are exact counts for the stated semantics, not just abstract set functions. For \(n=1,2,3,4,5,6,7\), the values of \(u_n\) are \(1,2,7,26,91,302,967\).

## Assumptions and scope
The carrier \(W\) is fixed and **labelled**; \(n\geq1\) and the number of named agents \(r\geq2\) is known. Each \(R_a\subseteq W\times W\) is serial, transitive and Euclidean (\(\mathsf{KD45}\)). In a query, a single atomic proposition receives an arbitrary valuation \(X\subseteq W\), and the output is the exact whole-world truth set of the **single, one-step disagreement modality**, with no noise, counterexample queries, extra modalities or nested probes. Queries may depend on all previous observations. The identification target is equality of the induced map on every \(X\), rather than equality or isomorphism of the individual \(R_a\). Theorem B counts distinct truth-value functions at one world, without constraining the observations at other worlds. All logarithms and asymptotics are absent from this result; the formulas are exact for every listed integer \(n\).

## Proof
**1. Symmetry and completeness of a complementary basis.** Seriality says \(R_a(w)\neq\varnothing\) for every agent and world. Hence \(\mathsf{DG}(\varnothing)=\mathsf{DG}(W)=\varnothing\), because neither a nonempty successor set can fit inside \(\varnothing\) nor can one fit inside the complement of \(W\). Interchanging the agent indices in the existential disjunction proves
\[
\mathsf{DG}(X)=\mathsf{DG}(W\setminus X).
\]
Among the \(2^n\) subsets, exactly one complementary pair is \(\{\varnothing,W\}\); the remaining \(2^{n-1}-1\) pairs are nonempty and proper. Querying one representative of each such pair determines the entire map, establishing the upper bound.

**2. Sharp adaptive lower bound and exact determining sets.** For every nonempty subset \(S\subsetneq W\), set \(T=W\setminus S\). The constant-row relation \(R_C=W\times C\) is serial, transitive and Euclidean whenever \(C\neq\varnothing\): its successor set is \(C\) at every world, and the two closure axioms follow because every successor's row is also \(C\). Consider a *zero* model in which all agents have \(R_a=R_W\). Its disagreement map is zero at every input. Consider a *separating* model in which one agent has \(R_S\) and all other agents have \(R_T\). Directly from the definition, its disagreement output is all of \(W\) precisely for inputs \(S\) and \(T\), and empty at every other input.

For an arbitrary deterministic adaptive querying strategy, follow its answer path on the zero model. If the strategy does not query at least one member of a complementary pair \(\{S,T\}\), that entire transcript is identical in the corresponding separating model; the strategy cannot identify the correct map. Thus even the zero-model path must query all \(2^{n-1}-1\) nontrivial pairs, proving the lower bound. The same witness shows that a fixed query family is determining only if it intersects every such pair. Together with the upper bound, this proves the if-and-only-if condition. Distinct complementary pairs are disjoint as collections of subsets, so each minimum family independently chooses one of two representatives, giving \(2^{2^{n-1}-1}\) minimum families. When \(n=1\), the empty query family is sufficient and is unique, as the formulas state.

**3. The two-agent pointed profile.** Because each successor set is nonempty, the predicate at a fixed world is
\[
f_{A,B}(X)=[A\subseteq X\ \wedge\ B\cap X=\varnothing]\ \lor\ [B\subseteq X\ \wedge\ A\cap X=\varnothing].
\]
If \(A\cap B\neq\varnothing\), neither disjunct is possible. If \(A\cap B=\varnothing\), the positive inputs consist exactly of the supersets of \(A\) disjoint from \(B\), together with the supersets of \(B\) disjoint from \(A\). Their inclusion-minimal members are exactly \(A\) and \(B\). Therefore two nonzero predicates coincide if and only if their unordered pairs of successor sets coincide.

The number of ordered pairs of **disjoint nonempty** subsets is \(3^n-2\cdot2^n+1\): assign each world one of three states (in the first set, in the second set, neither), then exclude either empty set and restore the doubly excluded configuration. Swapping the two nonempty disjoint sets has no fixed point; the resulting nonzero predicates number half of this count. All overlapping pairs yield exactly one additional, zero predicate. There are \((2^n-1)^2\) total ordered nonempty pairs, so subtraction gives its fiber size. Finally, for any given \(A,B\neq\varnothing\), taking the two constant-row relations \(R_A,R_B\) realizes the pointed profile on a genuine \(\mathsf{KD45}\) frame. No extra local realizability restrictions arise.

## Verification
Run `python3 checker.py` from the package. It enumerates all ordered nonempty two-agent successor pairs for \(1\leq n\leq7\), computes each truth table directly from the semantic definition, verifies every quotient count and the fiber formula, and checks the recovery of inclusion-minimal positive inputs. It also checks complement symmetry and empty/full-input behavior for \(50{,}001\) finite multi-agent configurations, and directly tests the zero-versus-separating lower-bound witnesses through four worlds. The run reports `ALL_CHECKS_OK`. Finite checks are illustrative cross-checks; the exact claims for arbitrary \(n\) and unrestricted adaptivity follow from the proof above.

## Relationship to prior work
The group-disagreement modality and its \(\mathsf{KD45}\) semantics are not new. Ding and Yang (2026) develop generated neighborhoods, expressivity and complete axiomatizations; see particularly their Sections 3 and 5.1 and Proposition 3.2. The two-agent strong-belief-disagreement operator was studied earlier by Chen and Pan (2018). Barlocco and Kupke (2017/2018) study broad coalgebraic learning via logical membership and equivalence queries, with a substantially different query and target model. None of these accessible results states the exact sharp all-world atomic-valuation query bound or the complete two-agent pointed-profile census here. General truth-table complement symmetry and the three-state counting argument are classical proof techniques, not claimed as new. The contribution is the exact combination of the semantics' realizable single-pair obstruction with the worst-case learning boundary and its observational quotient.

## Limitations
The result does not identify named successor relations: even at one world, their order is unobservable, and overlapping pairs collapse to the zero profile. It does not cover higher-order or nested modal tests, other feedback models, probabilistic noise, variable agent sets, or unlabeled-world reconstruction. The 2018 strong-belief-disagreement paper could not be checked throughout in full text, leaving a priority risk, and generic exact-learning results using different terminology may contain an equivalent restriction. No independent validation is asserted.

## References
1. Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268 (first version March 27, 2026); EPTCS 447 (2026), 299–320, doi:10.4204/EPTCS.447.17. https://arxiv.org/html/2603.26268v2
2. Jia Chen and Tianqun Pan, *Logic for Describing Strong Belief-Disagreement Between Agents*, Studia Logica 106 (2018), 35–47, doi:10.1007/s11225-017-9724-1.
3. Simone Barlocco and Clemens Kupke, *Angluin Learning via Logic*, LFCS 2018, Lecture Notes in Computer Science 10703 (2018), 72–90, doi:10.1007/978-3-319-72056-2_5. https://pure.strath.ac.uk/ws/portalfiles/portal/72768698/Barlocco_Kupke_LFCS2018_Angluin_learning_via_logic.pdf
4. Balder ten Cate and Raoul Koudijs, *Characterising Modal Formulas with Examples*, arXiv:2304.06646 (2023); ACM Transactions on Computational Logic. https://arxiv.org/abs/2304.06646
