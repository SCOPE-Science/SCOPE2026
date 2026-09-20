# Review

## Correctness

**PASS.**  The standard-model equality classification follows from an exact
reading of the two single-class comparisons in the proof of arXiv:2609.19728.
A cyclic auxiliary graph gives strict inequality.  If an auxiliary graph is a
tree, its zero-edge quotient size is controlled by independent Bernoulli edge
increments with parameters \(2/(2^{t_e}+2)\le1/2\).  Since the path expected-range
sequence \(b_j\) is strictly increasing, equality forces every \(t_e=1\).
Applying this to both bipartition classes forces maximum degree at most two;
cycles of length at least six violate the auxiliary-tree condition, while
\(C_4\) violates the codegree-one condition.  Hence only a path can attain
equality.

The gap-transfer inequality follows from the zero-edge contraction identity
\(h(G)=\mathbb E\widehat h(G/A_f)\), the BHM inequality on every quotient, and
the event \(A_f=\varnothing\).  Its probability is
\(|\mathcal H(G,o)|/|\mathcal L(G,o)|\), and on that event the quotient is \(G\)
itself.  Zhu's contraction comparison then bounds the intermediate path
expectation by \(h(P_n)\).  This yields the claimed lower bound on the lazy gap.
Combining it with the standard strictness handles every non-path bipartite
graph; Zhu's already-proved cycle strictness handles every connected
nonbipartite graph.  Small-order boundary cases are consistent with the proof.

The proof is general and does not rely on computation.

## Originality

**PASS, to the best of our knowledge.**  The direct 2026 source proves the
non-strict BHM inequality and the LNR inequality, with LNR strictness for graphs
containing a cycle.  It does not state a BHM equality classification or a unique
maximizer theorem, and Remark 5.6 explicitly leaves open the possibility that
the first contraction inequality is strict on trees.  Searches using
"unique maximizer", "equality case", standard/lazy expected range, graph-indexed
random walk, graph homomorphism, and the BHM/LNR names found no theorem covering
the two complete equality classifications or the displayed gap-transfer
inequality.

Wu--Xu--Zhu (2016) proves both inequalities for trees, and Bok--Nešetřil (2018)
extends them to unicyclic graphs.  The complete 2016 manuscript was not inspected
in full; accessible theorem statements record non-strict inequalities, leaving
a residual risk that a tree-only equality observation appears in the body.
Even if so, it would not imply the all-connected-bipartite BHM equality
classification or the general gap-transfer inequality.  The main 2026 source is
new, so very recent unindexed parallel work is another residual risk.

## Value

**PASS.**  The result upgrades two newly completed extremal expectation
inequalities from existence of a path maximizer to uniqueness of the maximizer.
The exact single-class equality criterion identifies the obstruction inside the
new proof rather than merely checking examples.  The standard-to-lazy gap
transfer is a quantitative statement that applies to every connected bipartite
graph and may be useful for future stability questions.

## Limitations

- Originality is only to the best of our knowledge.
- The complete 2016 Wu--Xu--Zhu manuscript was not inspected in full.
- The stronger stochastic-domination form of BHM is not addressed.
- No sharp universal lower bound on the nonzero expectation gap as a function of
  \(n\) alone is claimed.
- No independent validation has been performed.

**Same-model review: passed. Independent audit: not yet performed.**
