# Order independence of knowing-whether announcements on arbitrary S5 frames

## Finding
Let \(W\) be a nonempty (possibly infinite) set with two equivalence relations \(E,F\). For any valuation \(P\subseteq W\) of a single atom \(p\), let \(T_E\) be the ordinary public-announcement transformation announcing the proposition that the \(E\)-agent knows whether \(p\), namely \(K_Ep\lor K_E\neg p\). The same convention defines \(T_F\). At each stage, evaluate the announcement again in the current *induced submodel*; the result may be empty. The following are equivalent:

1. For every \(P\subseteq W\), the two updated models \(T_F(T_E(W,P))\) and \(T_E(T_F(W,P))\) have the same surviving worlds (and therefore the same inherited valuation and relations).
2. The two updates agree for every singleton valuation \(P=\{w\}\), \(w\in W\).
3. For every equivalence class \(A\) of \(E\) and every equivalence class \(B\) of \(F\),

\[
|A|\ge 2,\quad |B|\ge 2,\quad A\cap B\ne\varnothing\quad\Longrightarrow\quad A=B.
\]

When these conditions hold, both update orders retain exactly the worlds already satisfying *both* knowing-whether assertions in the original model. If \(H_E(P)\) denotes the union of the \(E\)-classes homogeneous for \(P\), their common output is \(H_E(P)\cap H_F(P)\).

Condition 3 has a sharp three-world obstruction. In \(W=\{0,1,2\}\), use \(E\)-classes \(\{0,1\},\{2\}\) and \(F\)-classes \(\{0\},\{1,2\}\). With \(P=\{1\}\), the \(E\)-then-\(F\) order retains \(\{2\}\), whereas the reversed order retains \(\{0\}\). No frame of size one or two can fail the condition.

On an \(n\)-element labelled carrier, the number \(c_n\) of *ordered* pairs of equivalence relations enjoying universal order independence is characterized by

\[
\sum_{n\ge0}c_n\frac{z^n}{n!}
 =\exp\!\left(z+3(e^z-1-z)\right),
\qquad c_0=1.
\]

The convention \(c_0=1\) concerns the empty combinatorial carrier; the assertion about S5 models assumes \(W\ne\varnothing\). In particular the counts for sizes one through five are \(1,4,13,61,304\). The same integer sequence and generating function were already tabulated independently as OEIS A367888; this is a new semantic characterization of that existing enumeration, not a claim to have discovered the numerical sequence.

For finite frames presented by two class-label arrays of length \(n\), the criterion is recognizable deterministically in \(O(n\log n)\) time and \(O(n)\) space: canonicalize both partitions by sorting labelled classes and check equality of the two non-singleton blocks at every point belonging to both.

## Assumptions and scope
An S5 model has a carrier \(W\), equivalence relations \(E,F\), and a valuation \(P\subseteq W\) of atom \(p\). For \(w\in W\), let \([w]_E\) and \([w]_F\) be its equivalence classes. The formula \(K_Ep\lor K_E\neg p\) is true at \(w\) precisely when \([w]_E\subseteq P\) or \([w]_E\cap P=\varnothing\). Consequently, for a current subset \(U\subseteq W\), with relations and valuation restricted to \(U\), the update \(T_E\) replaces \(U\) by

\[
\mathcal{U}_E(U,P)
=\bigcup\bigl\{A\cap U:\ A\in W/E,\quad
A\cap U\subseteq P\ \text{or}\ (A\cap U)\cap P=\varnothing\bigr\}.
\]

Empty intersections contribute nothing. No designated-world executability premise is assumed: these are whole-model restriction updates, and empty final models are allowed as outputs. The formula under each announcement is re-evaluated after the preceding update. The equivalence is not asserted for arbitrary formulas in place of the fixed factual atom \(p\), for non-equivalence accessibility, or for alternative arrow-deleting/private announcements.

## Proof
**Necessity from a single true world.** Suppose condition 3 fails. Choose \(E\)-class \(A\) and \(F\)-class \(B\) with \(A\cap B\ne\varnothing\), both having at least two elements, and \(A\ne B\). Pick \(w\in A\cap B\) and put \(P=\{w\}\). Then both \(A\) and \(B\) initially mix the two truth values, so \(T_E\) deletes all of \(A\), while \(T_F\) deletes all of \(B\). Every other class, for the relevant first update, is homogeneous false.

If \(B\setminus A\ne\varnothing\), choose \(v\in B\setminus A\). The \(E\)-first update retains \(v\) and deletes \(w\); after it, the surviving part of the \(F\)-class \(B\) is homogeneous false, so the second update retains \(v\). But the \(F\)-first update removes \(v\) at once. Hence the orders differ. If \(B\setminus A=\varnothing\), then \(A\setminus B\ne\varnothing\); exchanging \(E,F\) in the same argument gives a surviving point in the \(F\)-first order that is removed in the \(E\)-first order. Thus agreement on all singleton valuations implies condition 3.

**Sufficiency.** Assume condition 3. Consider any non-singleton \(E\)-class \(A\). Every \(F\)-class meeting \(A\) is either a singleton or exactly \(A\), since a non-singleton meeting class must equal \(A\). Therefore every **non-singleton** \(E\)-class is a union of complete \(F\)-classes. An \(E\)-singleton may lie inside a non-singleton \(F\)-class, but is necessarily homogeneous, hence is never deleted by its own announcement. Consequently, every *deleted* \(E\)-class is a union of whole \(F\)-classes; \(T_E\) never cuts a surviving \(F\)-class into a proper nonempty part. Symmetrically, \(T_F\) never cuts a surviving \(E\)-class.

An \(F\)-class either disappears entirely after \(T_E\), or survives intact with its original \(p\)-colors. Its truth-homogeneity is consequently unchanged whenever it survives. Thus the second \(F\)-test retains exactly the intersection \(H_E(P)\cap H_F(P)\). The reversed update gives the same set. As all remaining structures are simply restrictions, the final models coincide. Conditions 1 and 2 follow, completing the equivalence.

**Three-world minimality.** On fewer than three worlds, any two non-singleton equivalence classes meeting each other must both be all of \(W\), so condition 3 is automatic. The displayed three-world example violates it; the singleton witness shows the two distinct outputs.

**Census.** For a compatible pair \((E,F)\) on a finite carrier, collect all distinct non-singleton equivalence classes appearing in either partition. Condition 3 ensures they are pairwise disjoint, hence form a partial set partition. Give each such block exactly one of three colors according as it belongs only to \(E\), only to \(F\), or to both. All remaining points are singleton classes of both relations. Conversely, every such coloring of a partial set partition into blocks of size at least two gives exactly one compatible ordered pair \((E,F)\). The labelled exponential formula therefore gives one singleton component of weight \(z\) and three available colors of each block of size at least two, yielding \(\exp(z+3(e^z-1-z))\). By classifying the component containing a distinguished label, one also obtains

\[
c_{n+1}=c_n+3\sum_{j=1}^{n}\binom nj c_{n-j}\qquad(n\ge0).
\]

The displayed value \(c_0=1\) makes this recurrence well-defined.

**Finite recognition.** Every violation of condition 3 occurs at a world \(w\) for which both \([w]_E\) and \([w]_F\) are non-singleton but unequal. Form both partitions explicitly from input labels; compare canonical sorted block signatures on each world. Sorting dominates at \(O(n\log n)\) comparisons, with linear storage. No probabilistic hashing is required.

## Verification
The standalone program `verify.py` is self-contained Python 3 and can be run with `python3 verify.py`. It independently enumerates all equivalence relations (set partitions) on up to five labelled worlds, all ordered pairs of partitions, and all \(2^n\) valuations of \(p\) until a semantic inequality appears. It compares direct two-step public-announcement outputs with the asserted block criterion, checks the counts \(1,4,13,61,304\), the explicit minimal counterexample, and the recurrence against the separately published sequence through index eight. On this finite range it reports `VERIFY_OK`; these finite calculations do not prove the arbitrary-carrier theorem, whose proof above is set-theoretic.

## Relationship to prior work
Lerouvillois and Poggiolesi, *Dynamic Proof Theory for Dynamic Epistemic Logic* (arXiv:2609.37440, first posted 2026-09-29), develop dynamic hypersequent proof theory and standard S5 event-update semantics. Sierra Miranda, Wang, and Zenger, *Proof Theory for Non-Contingency Logic* (arXiv:2609.38975, first posted 2026-09-30), study proof systems for non-contingency, also interpreted as knowing whether. Fan, Wang, and van Ditmarsch, *Knowing Whether* (arXiv:1312.0144, 2013), Section 6, develop public-announcement semantics for knowing-whether logic and reduction axioms. These provide the foundational update and modality semantics; the inspected sections do not state this specific universal order-independence classification.

Belardinelli, van Ditmarsch, and van der Hoek, *A Logic for Global and Local Announcements* (2017, EPTCS 251:31–45, DOI:10.4204/EPTCS.251.3), discuss other, including arrow-refining, update operations; their commuting-with-connectives assertions are not order independence of two world-deleting knowing-whether tests. The numerical sequence is **already recorded** as OEIS A367888 (first listed 2023). The semantic interpretation and the precise block criterion, not the sequence alone, constitute the finding.

## Limitations
The update formula must be the knowing-whether assertion for a fixed *atomic* truth assignment; arbitrary changing epistemic formulas need not obey the same criterion. The theorem concerns whole-model restriction outcomes, not a particular designated world or event applicability requirement. The generated counts require labelled finite carriers and ordered pairs of agents; empty-carrier counting is formal only. Independent scientific validation has not been performed. Although relevant primary literature and several search formulations were compared, a logically equivalent older theorem under different terminology cannot be excluded by this search alone.

## References
- Clara Lerouvillois and Francesca Poggiolesi, *Dynamic Proof Theory for Dynamic Epistemic Logic*, arXiv:2609.37440 (2026), https://arxiv.org/pdf/2609.37440.
- Borja Sierra Miranda, Yunsong Wang, and Lukas Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975 (2026), https://arxiv.org/pdf/2609.38975.
- Jie Fan, Yanjing Wang, and Hans van Ditmarsch, *Knowing Whether*, arXiv:1312.0144 (2013), https://arxiv.org/pdf/1312.0144.
- Francesco Belardinelli, Hans van Ditmarsch, and Wiebe van der Hoek, *A Logic for Global and Local Announcements*, EPTCS 251 (2017), 31–45, DOI:10.4204/EPTCS.251.3.
- OEIS Foundation, *A367888*, https://oeis.org/A367888 (pre-existing sequence and exponential generating function).
