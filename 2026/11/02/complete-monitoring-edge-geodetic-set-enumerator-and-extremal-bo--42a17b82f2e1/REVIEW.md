# Scientific review

## Correctness — PASS

For every simple cycle of order at least three, all definitions and boundary cases are explicit. Each vertex subset monitors every edge exactly when all its selected cyclic gaps have length strictly below half the cycle. This is derived from the definition using deletion of an edge and uniqueness of shortest paths, including the even antipodal tie. Counting long-gap incidences and correcting the unique antipodal-pair double count gives every coefficient, without extrapolation. The merged-gap argument determines all inclusion-minimal successful sets, and maximal long-gap extension determines every maximal failure. Triple counts and independent-probe reliability follow algebraically. Independent brute-force distance-after-edge-deletion verification checks every subset for orders three through thirteen and prints VERIFY_OK. Finite verification is supporting evidence, not the proof of the infinite range.

## Originality — PASS, subject to prior-art risk

Dev et al., arXiv:2210.03774, establish the scalar minimum MEG-set size of cycles, including the four-cycle exception. That result is not newly claimed. Haslegrave, arXiv:2210.08955, concerns product bounds and complexity, and the inspected 2024 papers arXiv:2403.09122 and arXiv:2409.19067 concern bounds and complexity; their relevant results do not establish this complete size enumerator and both extremal inclusion classifications. The regular-polygon centered-convex-hull and no-closed-semicircle formulations are mathematically equivalent and were searched as well. A combinatorial cycle-arc or polygon-subset formula may already imply the result in different language; available comparisons found no decisive earlier complete statement, so priority remains subject to independent literature review.

## Mathematical value — PASS

The result settles an all-cardinalities placement spectrum and independent-probe reliability for a foundational network monitoring invariant. It also completely identifies the maximal failures (sharp universal guarantee) and the nonuniform minimal successes, including the exceptional even-order antipodal-pair family. These are natural dual boundaries of the same monitoring property, not arbitrary small numerical instances. The previously known scalar minimum is not counted as new.

## Sources and limits

The primary graph literature is Dev et al. (arXiv:2210.03774), Haslegrave (arXiv:2210.08955), and the 2024 bounds/algorithm papers (arXiv:2403.09122, arXiv:2409.19067). The result is for simple, unweighted cycles. Literature-priority uncertainty includes older combinatorics of vertices on a regular polygon and cyclic run enumerators. Full independent audit and independent validation are not performed.

Self-review: passed. Independent audit: not yet performed.
