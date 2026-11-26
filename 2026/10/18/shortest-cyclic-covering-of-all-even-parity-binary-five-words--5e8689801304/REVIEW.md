# Independent mathematical audit

## correctness

PASS

In the binary overlap graph the vertices are (k-1)-words, and each k-word is its prefix-to-suffix edge. Reading the appended bits of a closed walk gives precisely its cyclic windows. Every feasible walk can be started by traversing the required 0^k loop; lengths below 2^{k-1} cannot supply enough distinct windows (this rules out all lengths below k in the stated cases). Independently used the exact recurrence counting walks from the current suffix with a given set of missing mandatory edges and an exact remaining budget: branch on the two outgoing edges, delete a used required edge from the missing set, and at budget zero count one iff the suffix has returned to 0^{k-1} and the missing set is empty. Pruning only when there are more missing edges than remaining steps, this gives first feasible lengths 4,7,16,24. Reconstructing every successful rooted walk at k=5 gives exactly the eight printed strings. Direct cyclic window counts established exactly one 00000 in each and multiplicity classes (odd, repeated-even)=(5,3) and (7,1), four each. Rotation and reflected-rotation minima give eight necklaces and four bracelets. Independently of the counts, each parity class induces a permutation by rotating its words. If each even edge were used exactly once, the additional odd arcs would themselves be balanced, hence assembled from entire odd cycles. The odd five-cycle of 00001 is required to connect 00000 but does not touch the even 01111 component; the odd loop 11111 cannot connect that component to another. At least one more odd five-cycle is then needed, yielding at least 26 total windows. This supports compulsory even-edge duplication at length 24.

## originality

PASS

The distinct contribution is the exact single-host cover and optimizer census for the union of the even-weight classes, including compulsory reuse of a required window at order five. The overlap-graph and generic shortest-superstring formulations are known, and the smallest orders are simple cases, not strong standalone novelty claims. The closest inspected parity-augmentation record addresses only one weight class on a different range and with differently restricted extra windows. The broad single-circle consequence in Cazaux–Rivals does not give this disconnected-required-edge case.

## value

PASS

The parity language is a natural window requirement: each state has one mandatory incoming and outgoing edge, which invites connecting the resulting permutation cycles only by adding excluded windows. The complete order-five classification shows that this approach is strictly suboptimal: forbidding reuse of any required window raises the length to at least 26, while the true optimum is 24. The eight necklaces and their two multiplicity profiles give concrete minimal test sequences and a finite obstruction example, rather than only a small length table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
