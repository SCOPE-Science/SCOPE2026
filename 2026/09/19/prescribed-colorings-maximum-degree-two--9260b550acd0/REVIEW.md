# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The exact characterization has two directions.

For necessity, the extremal graph \(sK_3\sqcup K_m\) has maximum degree two. A color appears at most once in each triangle and at most once in the final \(K_m\). Hence every color class has size at most \(s+1\), and each class of size \(s+1\) must occupy a distinct vertex of \(K_m\), so there are at most \(m\) such classes.

For sufficiency, the already proved smaller-class theorem of Birken handles every vector with all coordinates at most \(s=\lfloor n/3\rfloor\). When a class of size \(s+1\) is present, the proof establishes an independent feedback set of exactly \(s+1\) vertices in every maximum-degree-two graph. Removing it leaves a linear forest. For \(m=1\), all remaining target sizes are at most \(s=\lceil(2s)/2\rceil\); for \(m=2\), they are at most \(s+1=\lceil(2s+1)/2\rceil\). A linear forest embeds in a spanning path, and a multiset with largest multiplicity at most half the length rounded up has a no-equal-adjacencies ordering. This realizes the remaining color classes exactly.

The independent-feedback lemma was checked against its extremal cases: triangle components require one selected vertex each, the number of cycle components is at most \(\lfloor n/3\rfloor\), and a specified vertex of a cycle of length \(\ell\) lies in an independent set of size \(\lfloor\ell/2\rfloor\). Thus the selected cycle-hitting set can always be enlarged inside an independent set to exactly \(\lceil n/3\rceil\).

A definition-level verifier exhaustively generates all maximum-degree-two graph isomorphism types and all target integer partitions through order 12, then solves prescribed-coloring feasibility directly by exact backtracking. It reports no discrepancy with the theorem. Finite verification supports but does not replace the proof.

## Originality

The primary source is Birken, arXiv:2609.18629v1 (16 September 2026). Its Theorem 1 proves prescribed colorings when every class size is at most \(\lfloor n/(r+1)\rfloor\). Its Section 3 then states Conjecture 5 allowing at most \(m\) classes of size \(s+1\) when \(n=s(r+1)+m\), and explicitly gives \(sK_{r+1}\sqcup K_m\) as the sharp obstruction. The inspected text does not state or prove the \(r=2\) case separately.

Kuchukova--Perkins--Povill, arXiv:2603.08259, studies sampling colorings with fixed class sizes and identifies the existence of skewed prescribed colorings as a largely undeveloped direction. Birken's smaller-class theorem resolves their Conjecture 1.8; the remainder-sensitive Conjecture 5 is newer.

External searches included exact and synonymous formulations with prescribed coloring, fixed or given color-class sizes, prescribed multiplicities/cardinalities, skewed coloring, maximum degree two, paths, and cycles. No prior exact universal characterization for \(\Delta\le2\), nor the independent-feedback-set reduction used here, was found.

No concrete inaccessible source was identified as especially likely to contain the same theorem. The main residual risk is terminological: older literature on equitable or cardinality-constrained coloring may encode the degree-two special case under different vocabulary. There is currently no evidence of such coverage. Originality is assessed only **to the best of our knowledge**.

## Value

This settles the full first nontrivial maximum-degree case of a conjecture stated only days earlier. It is stronger than proving the conjectured sufficient condition: the extremal graph gives the converse, so the theorem classifies exactly which prescribed size vectors work for every graph of maximum degree two. The proof also supplies a structural explanation: one large class can be chosen as an independent feedback set, after which prescribed coloring is reduced to the sharp multiset-arrangement condition on a linear forest.

## Limitations

The result does not address \(r\ge3\). It concerns universal feasibility over all graphs with maximum degree at most two, not a characterization of feasible vectors for each individual graph. The smaller-class case uses Birken's Theorem 1 rather than reproving that general theorem. The literature search cannot exclude older equivalences hidden under substantially different terminology. Cross-model review and independent validation have not been performed.
