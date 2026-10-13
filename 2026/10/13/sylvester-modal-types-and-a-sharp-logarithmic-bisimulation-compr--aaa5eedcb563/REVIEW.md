# Mathematical review

## Correctness — PASS

The finite structures, the color-respecting forward/backward bisimulation relation, and all quantifiers are stated precisely. Descendant descriptors are complete bisimulation invariants on finite outward trees, with different remaining heights separated by modal reachability formulas. The exact type recursion follows from sets of child types and the surjectivity of the assignment of \(q\) children onto each chosen set. The lower exponential estimate for the type count uses a valid binomial lower bound once \(t_k\ge2q\), and the linear affine recurrence in its logarithm yields \(\exp(cq^k)\le t_k\). Splitting levels at logarithmic height proves the uniform \(O(N/\log N)\) upper bound; independently choosing inequivalent colors on disjoint subtrees proves the matching lower bound. The one-color and one-branch boundary cases are separated. The standalone checker was run and reproduced the finite counts; computation is supporting evidence, not a substitute for the proof.

## Originality — PASS, with residual risk

Closest logical source: Figueira–Goren-Roig, arXiv:2307.09679 (2023), whose inspected text develops modal and graded-bisimulation semantics, unravelling and categorical characterization, not the fixed-palette complete-tree quotient extremum. Closest compression source: Ganardi et al., arXiv:1407.4286 / JCSS 2017, whose Section 5.3, Theorem 10 proves a closely related \(O(N/\log N)\) bound for an ordered-subtree DAG. That upper bound is explicitly treated as prior work, not new. An ordered-DAG lower bound does not entail this theorem's lower bound after quotienting by the strictly coarser ordinary bisimulation. Searches for the exact fixed-alphabet greatest-bisimulation quotient lower bound and Sylvester-type count did not yield an equivalent theorem. A prior result under a different coalgebraic or compressed-DAG formulation remains possible; no assertion of exhaustive literature clearance is made.

## Mathematical value — PASS

The quotient size is the actual modal state-space remaining after exhaustive bisimulation minimization, a canonical invariant used to reduce finite models. Complete regular trees of bounded branching and bounded observable alphabet are natural hard inputs rather than an arbitrary restricted computation. The result gives the sharp worst-case logarithmic compression rate—including a constructive lower bound against **all** additional ordinary-bisimulation merging—where a generic DAG upper bound alone cannot decide the issue. The separate exact type census and its binary Sylvester specialization supply reproducible finite refinements and a bridge to extremal modal-model compression.

## Limitations

No exact formula for the finite-height global extremal quotient size is asserted. The theorem requires fixed \(q,a\ge2\) and irreflexive immediate-child edges; it does not cover graded bisimulation or varying palettes. The 43,276 enumerated valuations are finite confirmation only. Independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
