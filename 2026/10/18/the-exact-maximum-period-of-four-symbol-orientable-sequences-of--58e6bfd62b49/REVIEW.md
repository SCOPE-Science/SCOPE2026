# Scientific review: exact quaternary order-four orientable periods

## Correctness (PASS)
The theorem quantifies over every cyclic word on exactly four letters subject to nonpalindromic, reversal-unique length-four windows. The degree proof bounds missing reversal classes by \(14\), hence period by \(106\). The proof crucially uses: the two reversal circuits make the included graph Eulerian; at four constant triple vertices an even indegree forces at least four omitted boundary pairs; the twelve repeated-leading-doublet vertices contribute an outgoing-minus-incoming difference of \(12\) in the missing arcs; and only six doublet-doublet reversal pairs can supply two outgoing arcs each. All four steps can be checked directly against the arc definitions. `verify.py` exhaustively checks the exhibited 106-window word, the 120 reversal classes, the 14 missing classes and the doublet vertex degrees. Computation supplies only existence; the universal upper bound is a written proof.

## Originality (PASS within checked evidence)
Mitchell--Wild, *New orientable sequences*, 2025 public preprint/2026 article, Table 6 and conclusions, explicitly display known period \(88\) versus upper bound \(112\) at alphabet size \(4\), order \(4\). A later August 2026 revision of Mitchell--Wild, arXiv:2603.18646, Table 4, retains these two numbers. Gabrić--Sawada's construction Theorem 11 and Table 2 concern broad lower bounds and do not imply the new matching upper bound. Searches for equivalent reversal-unique cyclic windows, graph dual formulations, period \(106\), and exact orientable order-four/quaternary values revealed no covering result. The original 2025/2026 tables were inspected in full primary documents, rather than inferred from search snippets. The lack of a result from searches is not a uniqueness certificate: unindexed, later or differently worded results remain possible.

## Value (PASS)
The paper's stated unresolved \(88\)-to-\(112\) gap at the first nontrivial even-alphabet/order-four case is completely closed, giving the exact natural extremal invariant \(106\). The degree-obstruction argument has a compact structural explanation, and the witness is short enough for direct independent checking. It is a complete finite-parameter result, not a trivial restatement of the existing generic bound.

## Residual limits
Not a general formula for other alphabet sizes and window orders; the full number or orbit structure of maximizers is unknown. Earlier or unindexed work might duplicate it. The explicit witness and same-model reasoning are not an independent external audit.

Self-review: passed. Independent audit: not yet performed.
