# Scientific review

## Correctness

PASS. Every labelled edge orientation is uniquely represented by its rim-edge bits and spoke bits; the vertex parity identity determines the spokes from the rim and the prescribed signature. The graph is chordal, so the exact directed-triangle exclusion is equivalent to acyclicity. The four-state transition counts each allowable orientation exactly once. The complete four-subset support transition table proves the odd/even obstruction classification and the exact count of exceptional signatures. Independent literal-orientation enumeration for all orders from two through ten and longer recurrence checks agree. No finite computation is used as an infinite proof.

## Originality

PASS, subject to residual literature risk. The motivating arXiv:2603.09475v1 studies the prescribed-indegree-parity acyclic-orientation problem and its source/sink constraints, and specifically treats Cartesian products of paths and cycles rather than fan-graph parity fibres. Classical total acyclic-orientation counts do not determine counts for individual parity signatures. Chordal-orientation generation results do not themselves supply the adjacent-pair obstruction or the exact parity-fibre recurrence. Existing wheel and multi-theta orientation results treat different graph families and do not imply the stated fan classification under graph isomorphism, edge deletion without parity correction, or parameter specialization. Targeted literature and mathematical-record searches revealed no covering statement. Priority remains subject to a more exhaustive independent bibliography check.

## Value

PASS. The recently studied prescribed-indegree-parity acyclic-orientation problem asks which parity prescriptions are realizable. The result supplies a full if-and-only-if criterion, an exact count for every prescription, and a linear-time counting algorithm on a natural infinite maximal-outerplanar chordal family. The exponential-in-half-order forbidden family for even path order and universal feasibility for odd order sharpen a bare decision algorithm; they reveal a boundary-sensitive parity effect obscured by the total acyclic-orientation count.

## Limits

The theorem is for fans only; it does not establish corresponding results for arbitrary chordal or outerplanar graphs. Code confirms finite instances, not the unrestricted theorem. A covering result under alternative terminology may be absent from the searched corpus; independent expert review is not supplied.

Self-review: passed. Independent audit: not yet performed.
