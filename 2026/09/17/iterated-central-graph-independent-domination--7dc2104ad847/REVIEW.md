# Review: independent domination of higher iterated central graphs

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**Verdict: PASS.**

The proof reduces the higher-iterate claim to Theorem 2.12 of Cabrera-Martínez, López-Carmona, Rios-Villamar and Serrano-Díaz, which gives
\[
i(\mathtt C^2(H))
=
|E(H)|+\binom{|V(H)|}{2}
+\frac{\alpha(H)^2-\alpha(H)(2|V(H)|-3)}2
\]
for connected \(H\) of order at least three.

The additional structural lemma was checked directly from the definition of the central graph. If \(X\) is the set of original vertices in an independent set of \(\mathtt C(H)\), then \(X\) is a clique of \(H\), and all selected subdivision vertices correspond to edges of \(H-X\). Thus the independent set has size at most
\[
|X|+|E(H-X)|.
\]
For connected \(H\) of order at least three, every clique \(X\) is incident with at least \(|X|\) edges, giving the upper bound \(|E(H)|\); all subdivision vertices attain it.

For \(J\) of order \(a\) and size \(b\), the graph \(H=\mathtt C(J)\) has
\[
|V(H)|=a+b,\qquad |E(H)|=b+\binom a2,\qquad \alpha(H)=b
\]
when \(a\ge3\). Substitution into Theorem 2.12 yields
\[
i(\mathtt C^2(H))=2|E(H)|
\]
by exact algebra. The only boundary case not covered by the lemma in this substitution is \(G=K_2,\ k=3\); it reduces to applying Theorem 2.12 to \(P_3=\mathtt C(K_2)\) and gives the same identity.

The restriction to a nontrivial connected starting graph is consistent with the definition of the central-graph operator used in the source.

## Originality

**Verdict: PASS, to the best of our knowledge.**

The closest and most important source is arXiv:2609.16357v1, posted 14 September 2026. Its concluding Theorem 2.12 gives an exact expression for \(i(\mathtt C^2(G))\) in terms of the order, size and independence number of \(G\). The paper introduces the notation \(\mathtt C^2(G)\), but no higher iterate is stated; a full-text check found no occurrence of an iterated-central-graph treatment beyond that second iterate.

Searches using exact and synonymous formulations of “independent domination”, “iterated central graph”, \(\mathtt C^3(G)\), and the independence number of a central graph did not locate a prior theorem implying
\[
i(\mathtt C^k(G))=2|E(\mathtt C^{k-2}(G))|\qquad(k\ge3).
\]
No prior SCOPE record was found for the same mathematical object or claim family.

The lemma \(\alpha(\mathtt C(H))=|E(H)|\) for connected \(H\) of order at least three is elementary enough that it may have appeared independently in older central-graph literature. Accordingly, the originality claim is not placed on that lemma in isolation; it is placed on the all-higher-iterate independent-domination identity, its proof from the second-iterate formula, and the consequence that all connected graphs with the same order and size have identical higher-iterate values.

No inaccessible paper was identified as especially likely to contain the same higher-iterate theorem. Because the motivating preprint is only days old, very recent, not-yet-indexed, or unpublished parallel work remains a residual risk.

## Value

**Verdict: PASS.**

The result converts a second-iterate formula depending on \(\alpha(G)\) into an exact theorem for every higher iterate. From the third iterate onward, all dependence on finer graph structure disappears: the values are governed solely by the deterministic order-size recurrence
\[
n_{r+1}=n_r+m_r,\qquad m_{r+1}=m_r+\binom{n_r}{2}.
\]
This gives a closed structural description of the entire infinite tail rather than a single parameter instance.

## Limitations

The result applies to finite simple connected graphs and does not classify the minimum independent dominating sets themselves. It uses Theorem 2.12 of arXiv:2609.16357v1 as an established input. Originality is asserted only to the best of our knowledge, and the extreme recency of that source leaves a nonzero risk of parallel work.

No independent validation is asserted.
