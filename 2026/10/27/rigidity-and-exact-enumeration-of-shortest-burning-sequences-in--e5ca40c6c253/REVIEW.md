# Self-review

## Correctness — PASS
The proof explicitly fixes binary vector labels, synchronous previous-round propagation, source validity, and the counting convention. The span obstruction forces the first \(m\) sources of a shortest \((m+1)\)-round sequence to span the entire space, hence be a basis. The basis-prefix identity is proved by induction from all the cross-pair sums, and it gives exactly \(2^{m-1}-1\) valid final redundant choices. The standard product counts ordered bases. A standalone finite source-sequence enumeration reproduces the \(m=3,4\) numbers, and basis trajectories replay at \(m=3,4,5,6\). These finite tests are not substituted for the proof.

## Originality — PASS (provisional priority assessment)
The 2026 original research paper proves the *burning number* and constructs an optimal sequence (Theorem 4.7); the all-optima converse, compulsory redundancy, universal exact trajectory, and arbitrary-dimensional strategy multiplicity are not stated there. The earlier thesis index explicitly supplies the small cases \(504\) and \(141120\), which are not claimed as new. Related published results searches and recoverable earlier records returned no equivalent or stronger all-dimensional source-sequence theorem. The thesis full PDF could not be inspected, so a meaningful historical-priority risk remains; absence of a search hit is not evidence of uniqueness.

## Value — PASS
The natural issue after determining the number of rounds is *which strategies actually achieve it*. The result classifies **all** shortest ordered source sequences of an infinite family, shows that every one has the same exponential size-growth profile, proves that the final move is inevitably redundant, and provides an exact strategy count. This is a structural optimality theorem, not just the existing scalar burning number or a recomputation of the two previously known small samples; its consequence enables exact random-strategy success counting in these designs. It is a focused refinement rather than a broad new burning bound.

## Closest literature and limitations
Burgess et al., arXiv:2608.25627v1, Theorem 4.7, contains the optimal round count and an existence construction. C. W. Jones, *Hypergraph Burning* (MSc thesis), indexed computational-results passages, cover the 7- and 15-point data. The complete thesis could not be opened; general historical priority should be checked independently. Only \(\mathbb F_2^m\setminus\{0\}\) triple systems and the specified synchronous valid-source rule are covered.

Self-review: passed. Independent audit: not yet performed.
