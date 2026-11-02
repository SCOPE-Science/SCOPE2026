# Scientific review

## Correctness

PASS. The identity \(\operatorname{SW}(C)=2e(C)/|C|\) follows by double-counting. For every hub-free coalition, degree and girth bounds give welfare at most half its vertex count, with equality only for an edge. For the hub coalition, the five small sizes and the strict quadratic inequality for sizes at least six force precisely hub-plus-edge or hub-plus-induced-three-vertex-path. Every equality partition therefore corresponds bijectively to a motif deletion followed by a perfect matching. The unilateral deviation check distinguishes hub, selected motif vertices and outside matched vertices; it explicitly uses exclusion of triangles and four-cycles. Exact-rational exhaustive checks of fans, wheels and all eligible graph-atlas bases through seven vertices passed. Neither a finite check nor a simulated search is offered as an infinite proof.

## Originality

PASS with residual risk. The primary 2023 paper concerns bounded-treewidth optimization procedures rather than this explicit matching-certifiable universal-vertex structural theorem. The 2018 Nash-stability theorem applies to trees, while the constructed networks generally have triangles. The 2021 dense graph partitioning results cover degree-at-most-two **whole** graphs and high-minimum-degree graphs, not this general apex family. Searches for wheel/fan formulas, matching-deletion equivalences and equivalent dense graph partitioning formulations identified no directly covering theorem. Earlier work on other exact graph classes and unindexed specialized notes remain possible; absence of a database match does not prove novelty. The IJCAI 2015 full PDF could not be retrieved through the attempted primary-page links; its accessible abstract and related later citations were inspected, and it remains a residual source risk.

## Mathematical value

PASS. The certificate supplies an exact threshold-attainment criterion, a count of all maximizing coalition structures, and the stronger property that **every** sharp maximizer is Nash stable. This is a natural graph clustering problem where a hub can change an otherwise path/cycle matching optimum; it identifies exactly when the one-unit hub gain can be realized. Fans, wheels and disconnected sparse bases provide a structural benchmark beyond the previously established tree stability case. It makes no claim of a general result for all graphs or for graphs without a certificate.

Self-review: passed. Independent audit: not yet performed.
