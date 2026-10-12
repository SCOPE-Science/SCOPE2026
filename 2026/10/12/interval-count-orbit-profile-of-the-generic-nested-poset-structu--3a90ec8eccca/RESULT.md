# Interval-count orbit profile of the generic nested-poset structure
## Finding
Let \(\mathcal K\) be the class of finite structures \((X,\leq_0,\leq_1)\) in which both relations are partial orders and \(\leq_0\subseteq\leq_1\). Let \(M\) be the Fraïssé limit of \(\mathcal K\). If \(a_n\) is the number of \(\operatorname{Aut}(M)\)-orbits on injective ordered \(n\)-tuples, then
\[
a_n=\#\{(P,Q):P,Q\text{ are partial orders on }[n],\ P\subseteq Q\}.
\]
Thus \(a_n\) is exactly the number of intervals, or equivalently ordered comparable pairs, in the inclusion poset of labeled partial orders on \([n]\). With \(a_0=1\), the first values are
\[
1,\ 1,\ 5,\ 79,\ 3221,\ 301831,\ 60305525
\]
for \(n=0,1,\ldots,6\).

If \(b_n\) counts orbits on all ordered \(n\)-tuples, repetitions allowed, then
\[
b_n=\sum_{k=0}^n {n\brace k}a_k,
\]
so
\[
(b_n)_{n=0}^6=(1,1,6,95,3731,336092,65049621).
\]

## Assumptions and scope
The language has exactly two binary relation symbols interpreted as reflexive partial orders, with the first relation finer than the second. The result concerns the countable Fraïssé limit of all finite such structures. The orbit counts are for ordered tuples; the injective profile uses distinct coordinates, while the second formula includes repeated coordinates.

The existence and ultrahomogeneity of the relevant Fraïssé limit are external inputs. Lipparini proves strong and superamalgamation for comparable partial orders and, for the finite-model Fraïssé limit in the partial-order case, \(\omega\)-categoricity and quantifier elimination. The counting formulas below are deductions from that structural theorem.

## Proof
For an injective tuple \(\bar a=(a_1,\ldots,a_n)\) from \(M\), pull both orders back along the labeling map \(i\mapsto a_i\). This gives a labeled pair \((P_{\bar a},Q_{\bar a})\) of partial orders on \([n]\) with \(P_{\bar a}\subseteq Q_{\bar a}\).

Conversely, every finite nested pair \((P,Q)\) belongs to \(\mathcal K\), hence embeds into the Fraïssé limit. Therefore every such labeled pair occurs as the induced structure on some injective ordered tuple.

If two injective tuples induce the same labeled pair, the coordinatewise bijection between their induced finite substructures is an isomorphism. Ultrahomogeneity extends that isomorphism to an automorphism of \(M\), so the tuples lie in the same orbit. If the induced labeled pairs differ, no automorphism can carry one tuple to the other. This proves the bijection between injective tuple orbits and nested labeled partial orders.

For arbitrary ordered tuples, first record the equality partition of the coordinate set. If it has \(k\) blocks, the \(k\) distinct values carry one of the \(a_k\) injective orbit types. There are \({n\brace k}\) equality partitions, yielding the Stirling transform formula for \(b_n\).

There is also an exact finite computation of \(a_n\). Represent a strict partial order by assigning each unordered pair one of three states: incomparable, forward, or backward. For every transitive orientation \(Q\), let \(t(Q)\) be the number of transitive suborders \(P\subseteq Q\). Then
\[
a_n=\sum_Q t(Q).
\]
On the coordinatewise three-state poset, a zeta transform computes all \(t(Q)\) simultaneously after transitivity has been tested. For \(m={n\choose 2}\), the zeta phase uses \(O(m3^m)\) integer operations.

## Verification
A standalone C++ verifier enumerates all three-state orientations through \(n=6\), checks transitivity directly, and performs the coordinatewise zeta transform. As a control, it independently recovers the classical labeled-poset counts
\[
1,1,3,19,219,4231,130023.
\]
It then recovers the nested-pair counts
\[
1,1,5,79,3221,301831,60305525
\]
and checks the Stirling transform values
\[
1,1,6,95,3731,336092,65049621.
\]
The replay terminates with `VERIFY_OK`. The verifier source and captured output accompany this result.

## Relationship to prior work
Lipparini's 2023 preprint establishes the amalgamation, Fraïssé-limit, model-completion, \(\omega\)-categoricity, and quantifier-elimination framework for pairs of comparable partial orders. The inspected source does not enumerate automorphism orbits. The later published treatment likewise focuses on the structural model theory.

Classical enumeration supplies the number of labeled partial orders themselves, but that is only the diagonal statistic \(\#\{Q\}\). The present profile instead counts all inclusions \(P\subseteq Q\), and then identifies that order-theoretic interval statistic with the injective oligomorphic profile of the generic nested-poset structure.

Targeted searches for the exact values, for comparable-pair enumeration, for intervals in the inclusion poset of partial orders, and for a nested-poset orbit profile did not locate an equivalent published statement. The closest semantic-database result concerns reducts of the ordinary random poset and does not imply this two-order profile.

## Limitations
No closed form or asymptotic estimate for \(a_n\) is claimed. The numerical census is exhaustively verified only through \(n=6\); the orbit-identification theorem itself is valid for every \(n\). The originality assessment is necessarily literature-search based: an equivalent combinatorial sequence could exist under terminology not captured by the searches performed.

## References
1. Paolo Lipparini, *Pairs of partial orders and the amalgamation property*, arXiv:2303.06205, first submitted 2023-03-10. Primary MSC 03C52.
2. Paolo Lipparini, *Structures with Two Partial Orders and the Amalgamation Property*, Bulletin of the Section of Logic, DOI: 10.18778/0138-0680.2026.17.
3. OEIS A001035, number of labeled partial orders on an \(n\)-element set, used only as a verification comparator for the ordinary-poset counts.
