# Exact labelled and unlabelled census of normal two-agent someone-knows frames

## Finding

Let \(W\) be a nonempty finite labelled set of \(n\) worlds and let \(E,F\) be **ordered** equivalence relations on \(W\), interpreted as two \(\mathsf{S5}\) knowledge relations. On all propositions \(A\subseteq W\), write
\[
S(A)=\{w\in W:E[w]\subseteq A\ \text{or}\ F[w]\subseteq A\},\qquad
D(A)=\{w\in W:E[w]\cap F[w]\subseteq A\}.
\]
The former means that someone knows the proposition; the latter is distributed knowledge.

The following conditions are equivalent: (a) \(S(A\cap B)=S(A)\cap S(B)\) for all \(A,B\subseteq W\); (b) for every \(w\in W\), either \(E[w]\subseteq F[w]\) or \(F[w]\subseteq E[w]\); (c) \(S=D\) as Boolean-algebra operators; (d) the bipartite incidence graph of the blocks of \(E\) and \(F\) is a disjoint union of stars, with an edge between two blocks when they intersect; and (e) on each equivalence class of the join \(E\vee F\), at least one of the two restricted equivalence relations is the indiscrete relation. Condition (b), as a statement about set partitions, is the previously defined **h-equivalence** property; the present contribution is its complete labelled and unlabelled enumerative application to normality of \(S\).

Let \(B_m\) be the \(m\)-th Bell number, with \(B_0=1\). The exact number \(L_n\) of **ordered, labelled** pairs \((E,F)\) satisfying these conditions has exponential generating function
\[
\boxed{\quad\sum_{n\geq0}L_n\frac{z^n}{n!}
=\exp\!\left(2\exp(e^z-1)-e^z-1\right).\quad}
\]
For \(n\geq1\), it satisfies the finite recurrence
\[
\boxed{\quad L_n=\sum_{j=1}^{n}\binom{n-1}{j-1}(2B_j-1)L_{n-j},\qquad L_0=1.\quad}
\]
Its values for \(n=0,1,\ldots,8\) are
\[
1,\ 1,\ 4,\ 19,\ 111,\ 774,\ 6229,\ 56529,\ 569354.
\]

If \(U_n\) counts the same ordered pairs **up to a simultaneous relabelling of their worlds**, and \(p(m)\) is the number of integer partitions of \(m\), then
\[
\boxed{\quad\sum_{n\geq0}U_n z^n=\prod_{m\geq1}(1-z^m)^{-(2p(m)-1)}.\quad}
\]
The values for \(n=0,\ldots,8\) are
\[
1,\ 1,\ 4,\ 9,\ 24,\ 52,\ 125,\ 268,\ 598.
\]

Write \(H_n=\sum_{\pi\in\Pi_n}\prod_{C\in\pi}B_{|C|}\), where \(\Pi_n\) is the set of partitions of an \(n\)-element set. Exactly \(2H_n-B_n\) of the \(L_n\) pairs have one **globally** finer information partition. The remaining \(L_n-2H_n+B_n\) are locally comparable but globally incomparable. Their first occurrence is at \(n=4\), with exactly **six** ordered labelled pairs; therefore four worlds are a sharp threshold for this distinction. At \(n=4\), \(L_4=111\), \(2H_4-B_4=105\), and \(U_4=24\).

## Assumptions and scope

A relation is \(\mathsf{S5}\) here precisely when it is reflexive, symmetric and transitive. A pair is ordered because the two agents are named and cannot be exchanged when counting. Every subset of \(W\) is admissible as a propositional valuation, so meet preservation is an assertion about the entire powerset algebra, not about a restricted language or a fixed valuation. For the unlabelled count, a permutation must act simultaneously on both equivalence relations and may not exchange the agents.

The join \(E\vee F\) denotes the least equivalence relation containing \(E\cup F\). The incidence graph has one left vertex for each \(E\)-class, one right vertex for each \(F\)-class and a simple edge whenever the two classes have a world in common. A star includes a single edge. The \(n=0\) values are included as formal generating-function constants only: the modal assertion concerns \(n\geq1\).

## Proof

**1. Exact normality criterion.** Each \(S\) is monotone and satisfies \(S(W)=W\), independently of \(E,F\). Assume that \(E[w]\) and \(F[w]\) are incomparable for some \(w\). Take \(A=E[w]\) and \(B=F[w]\). Then \(w\in S(A)\cap S(B)\), while neither \(E[w]\) nor \(F[w]\) is contained in \(A\cap B\), so \(w\notin S(A\cap B)\). Thus meet preservation fails. Conversely, if the two cells are comparable at every world, their smaller cell equals \(E[w]\cap F[w]\); hence for every \(A\subseteq W\),
\[
w\in S(A)\iff E[w]\cap F[w]\subseteq A\iff w\in D(A).\]
The operator \(D\) is an ordinary relational box and preserves all intersections. This proves the equivalence of (a), (b), and (c), including the usual normal-box condition.

**2. The star normal form.** For an intersecting \(E\)-block \(X\) and \(F\)-block \(Y\), any common element \(w\) satisfies \(E[w]=X\), \(F[w]=Y\). If \(X\subseteq Y\), then \(X\) intersects no other \(F\)-block and its incidence vertex has degree one; if \(Y\subseteq X\), the same holds for \(Y\). Conversely, a degree-one incidence vertex represents a block contained in its unique neighboring block. A bipartite graph all of whose edges have a degree-one endpoint is a disjoint union of stars: a connected component with two vertices of degree at least two would contain an edge joining such vertices along the path between them. This proves (b)\(\iff\)(d).

Each incidence component represents a class \(C\) of \(E\vee F\): two worlds are connected under alternating \(E\)- and \(F\)-steps exactly when their associated edges lie in the same graph component. In a star centered on an \(E\)-block, that block contains all worlds of the component, so \(E|_C\) is indiscrete; the analogous assertion holds for an \(F\)-center. Conversely, either indiscrete restriction makes the component a star. This proves (d)\(\iff\)(e).

**3. Labelled enumeration.** A connected join block \(C\) of size \(m\geq1\) has \(B_m\) possible pairs with \(E|_C\) indiscrete and \(B_m\) with \(F|_C\) indiscrete. Their intersection consists of the single pair in which both are indiscrete. Thus the connected-block weight is exactly \(c_m=2B_m-1\). Every admissible pair is uniquely a set of such components, indexed by the classes of \(E\vee F\). Consequently
\[
L_n=\sum_{\pi\in\Pi_n}\prod_{C\in\pi}c_{|C|},
\]
and the exponential formula gives
\[
\sum_{n\geq0}L_n\frac{z^n}{n!}
=\exp\left(\sum_{m\geq1}(2B_m-1)\frac{z^m}{m!}\right)
=\exp\left(2(\exp(e^z-1)-1)-(e^z-1)\right).
\]
Selecting the join component containing a distinguished label yields the displayed recurrence; there are \(\binom{n-1}{j-1}\) choices of its other labels and \(c_j\) choices of local structure.

**4. Unlabelled enumeration.** On one join component of size \(m\), an ordered pair has either \(E\) indiscrete and \(F\) of some integer-partition block-size type, or vice versa; the both-indiscrete case is shared. Hence there are exactly \(2p(m)-1\) isomorphism types of connected components of size \(m\). No two different join components interact, and the simultaneous relabelling action makes the global pair an unordered multiset of connected component types. A multiset of objects of \(2p(m)-1\) types, each of size \(m\), contributes the factor \((1-z^m)^{-(2p(m)-1)}\). Multiplication over all \(m\geq1\) proves the ordinary generating function.

**5. The sharp local/global gap.** The number of ordered pairs for which \(E\) refines \(F\) globally is \(H_n\): choose \(F\), then independently partition each \(F\)-class to obtain \(E\). The same number have \(F\) refining \(E\), and their intersection is the set of \(B_n\) pairs \(E=F\); inclusion-exclusion gives \(2H_n-B_n\).

For a locally comparable but globally incomparable pair, at least one join component has \(E\) indiscrete and \(F\) non-indiscrete, and a different component has \(F\) indiscrete and \(E\) non-indiscrete. Each must contain at least two worlds, proving \(n\geq4\). At \(n=4\) these components are necessarily two disjoint two-element subsets. There are three pairings of four labels and two assignments of the component orientations, giving exactly six ordered pairs, and all satisfy local comparability. This proves sharpness.

## Verification

Run `python3 checker.py` using Python 3.8 or newer. The independent finite checker generates every set partition of labelled sets of sizes \(1\) through \(6\), tests the local-cell criterion and incidence-graph criterion on all ordered pairs, and compares counts with the Bell-weight recurrence. For up to four worlds it additionally checks the meet equation over **every ordered pair of truth subsets** and checks equality with distributed knowledge as operations. It checks the global-comparability subtraction for all six sizes. For up to five worlds it computes simultaneous-permutation canonical forms and compares the orbit counts to coefficients of the unlabelled product. The output terminates with `ALL_CHECKS_OK`.

These finite enumerations are not an all-size proof; Steps 1–5 prove the formulas for arbitrary finite \(n\).

## Relationship to prior work

The 2026 work of Ding and Yang introduces and axiomatizes the somebody/someone-knows bundled modality over \(\mathsf{S5}\) frames. Its \(\mathtt C^1\) aggregation axiom entails binary meet preservation; that logical implication is **not claimed new** here. Ågotnes and Wáng (2021) previously studied the non-normality of somebody-knows reasoning. Neither inspected source gives the exact paired-partition census displayed above.

Crucially, the set-partition condition in (b) is **already defined** by Tochon (2015) as *h-equivalence*, and reused by Tochon, Dalla Mura and Chanussot (2019): every two intersecting blocks must be nested. Hence the elementary local-comparability condition is not claimed as independently discovered. The added result is the full labelled and unlabelled enumeration, the associated modal-algebra interpretation, and the exact sharp six-pair local-versus-global threshold. The 2019 paper's section on h-equivalence addresses partition hierarchies and braids, not the enumeration obtained here.

Ding, Liu and Wang (2023) give additional broad axiomatizations for someone-knows logics. The available abstract establishes its relevance; its complete text was not accessible for inspection, so priority relative to a concealed equivalent count remains a residual risk. Existing tabulations of pairs of partitions with **discrete meet and indiscrete join** impose different restrictions and do not give the present star-forest class.

## Limitations

This result counts exactly two named agents and all propositions on a finite nonempty world set. With three or more agents, the union-of-boxes meet criterion becomes a different hypergraph dominance condition and the two-partition counting formula need not apply. The reported values for small \(n\) do not constitute an independent proof of the general formulas. The work is not an assertion of historical uniqueness: an older enumeration of h-equivalent partition pairs under different terminology may exist. Independent mathematical auditing has not yet occurred.

## References

1. Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities* (first arXiv version 27 March 2026), arXiv:2603.26268v1, https://arxiv.org/abs/2603.26268; particularly Section 5.1 of the accessible revised manuscript.
2. T. Ågotnes and Y. N. Wáng, *Somebody Knows*, KR 2021, https://proceedings.kr.org/2021/1/kr2021-0001-agotnes-et-al.pdf; doi:10.24963/kr.2021/1.
3. G. Tochon, *Hierarchical analysis of multimodal images*, doctoral thesis, Université Grenoble Alpes (2015), thesis:tel-01242836, Definition 4.8 (h-equivalence).
4. G. Tochon, M. Dalla Mura, and J. Chanussot, *Constructing a Braid of Partitions from Hierarchies of Partitions*, ISMM 2019, pp.111–123, doi:10.1007/978-3-030-20867-7_9, Section 2.3.
5. Y. Ding, J. Liu, and Y. Wang, *Someone knows that local reasoning on hypergraphs is a weakly aggregative modal logic*, Synthese 201 (2023), doi:10.1007/s11229-022-04032-y; abstract consulted, complete text not inspected.
6. E. R. Canfield, *Meet and join in the partition lattice*, Electronic Journal of Combinatorics 8 (2001), R15; related but different pair-partition enumeration, cited via OEIS A181939.
