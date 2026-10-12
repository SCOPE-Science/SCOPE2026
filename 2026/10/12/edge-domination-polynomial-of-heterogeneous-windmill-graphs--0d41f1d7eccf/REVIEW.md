# Scientific review: edge-domination polynomial of heterogeneous windmill graphs

## Correctness — PASS
The independent-set characterization of vertices with zero selected degree converts edge domination into a hub-dependent, blade-local condition. Inclusion-exclusion with exact isolated rim vertices proves the full polynomial. The proof separately classifies equality cases at local minimum cost for even and odd blades; the parity-dependent minimum and exact first coefficient follow without assuming that an optimal edge dominating set is a matching. A standalone integer verifier compares every coefficient with exhaustive edge-subset enumeration on 58 small heterogeneous tuples and cross-checks the symbolic first-coefficient formulas on larger finite collections. The finite computation is supporting evidence, not the infinite proof.

## Originality — PASS
The general minimum edge-dominating-set algorithm of van Rooij–Bodlaender and the general coefficient-extraction construction of Alaeiyan–Mohammadian cover the definitions and computational frameworks but neither supplies the blade-isolation factorization and parity-sensitive nonmatching optimum multiplicities. The known friendship-graph saturation *number* is excluded from the originality basis. The public 2023 friendship-graph article treats connected vertex-edge domination, a different invariant. Semantic database searches for edge domination, line-graph domination, windmills, clique bouquets, parity and matching reductions did not find a dominating explicit theorem. The 2016 edge-domination-polynomial paper and some older sources were not available in full and remain specifically recorded coverage risks.

## Value — PASS
The result determines every cardinality coefficient for the natural infinite class of arbitrary heterogeneous clique bouquets, a tractable benchmark for an NP-hard edge-domination counting/optimization problem. The hub changes the combinatorics, requiring subtraction of spoke-free false positives and replacement by full internal edge covers. The parity threshold and closed nonmatching optimum counts distinguish the new information from a routine scalar bound or a mere matching enumeration. It recovers stars and friendship graphs without asserting novelty for already known special-case scalar values.

## Limits and closest literature
The theorem applies to a shared single hub and clique blades, not all block graphs. The claim does not enumerate only maximal matchings. Closest checked literature: van Rooij–Bodlaender (2011 public online), Alaeiyan–Mohammadian (2011), Chaluvaraju–Chaitra (2016, abstract only), Horton–Kilakos (minimum edge domination, abstract only), Gupta (friendship scalar), and Radhika–Suhi–Jangiti (connected vertex-edge domination, abstract only). Independent mathematical or bibliographic verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
