# Scientific review

## Correctness: PASS

The claim precisely concerns unordered edges between labeled binary two-planes, with the associated-neighbor condition requiring \(D=\langle C\cap z^\perp,z\rangle\) and \(z\notin C\cup C^\perp\). The proof first eliminates even intersection lines by the nonzero Gram determinant. For an odd common line, orthogonal complement representatives are unique and have odd norm. Associatedness is reduced in both directions to their cross dot product being one. The characteristic vector \(t+u\) then yields the exact parity-dependent local count. No graph edges can be counted twice because the common intersection line is unique. The special line \(u=t\) when \(n\) is odd, and boundary cases \(n=2,3\), are handled explicitly. Two genuinely different exact implementations agree over the stated finite ranges, but the infinite theorem rests on the proof rather than on enumeration.

## Originality: PASS (priority risk remains)

The 2025 conference source defines associated neighborship and identifies counting associated-neighbor edges as prospective work, without giving the formula. The closest 2026 primary paper, arXiv:2609.07580v1, was inspected through its arXiv HTML full text; it studies the ordinary LCD neighbor graph, its degree, connectedness, and its orthogonal-orbit subgraphs, not the associated construction. A relevant mathematical-research record establishes ordinary-neighbor edge regularity and triangle counts in all dimensions, but neither its statements nor its parameters imply the count for the strictly smaller associated graph. Exact-keyword, alias and theorem-implication searches found no identical associated-graph formula. The earlier April 2025 presentation is documented but its full slides were not read, and undiscovered equivalent formulations remain a real priority risk. These risks do not amount to identified covering results.

## Value: PASS

The precise size of the associated-neighbor graph is explicitly motivated in the source lecture as a natural quantity still to be determined. The theorem answers this problem uniformly for the first nontrivial code dimension, all block lengths, and both parities. It reveals a structural selection rule—only odd intersection lines contribute—and an exceptional characteristic vector when the ambient dimension is even. This is more than a finite census or a reformulation of the ordinary LCD-neighbor degree formula, because associated neighbors depend on the defining orthogonality of the replacement vector.

## Sources and limitations

Closest primary sources: C. Vela, 2025 conference slides (associated graph and proposed edge enumeration); de la Cruz et al., arXiv:2609.07580v1 (ordinary graph and orbit degrees); institutional record dated 2025-04-03 (source chronology). The broad ordinary-graph edge-regularity record and other exact-phrase search results were compared at the level of statements and implications. The archive of an earlier presentation and possible unpublished work are residual novelty risks. No independent audit is claimed; the exact theorem applies only to labeled binary dimension-two LCD codes.

Self-review: passed. Independent audit: not yet performed.
