# Review of Minimum super dominating sets of one-leaf coronas

## Correctness
PASS. The half-order lower bound gives \(\gamma_{\mathrm{sp}}(H\circ K_1)\ge |V(H)|\), while both the original vertex set and the pendant-leaf set attain equality. Every minimum set must therefore choose exactly one vertex from each support-leaf pair. If a support is selected and its private leaf is outside, that support must itself witness the leaf; hence it cannot have an outside base neighbor. This proves that the outside supports form a union of connected components. The converse construction from every component union is immediate and verifies both kinds of outside vertices. Exhaustive testing of all labeled base graphs through order five matches the complete classification.

## Originality
PASS. The 2017 corona-product paper determines the super domination number, not the number or complete structure of minimum sets. The 2022 enumeration paper introduces \(N_{\mathrm{sp}}\), treats selected named families, and explicitly asks for counts of minimum super dominating sets in trees; its inspected enumeration and conclusion do not contain this one-leaf-corona formula. A 2026 super-domatic result exhibits the two complementary sets for coronas but studies maximum partitions, not all minimum sets, and does not imply the \(2^{c(H)}\) classification for disconnected bases. Targeted exact-phrase and semantic searches found no equivalent component-union theorem.

## Value
PASS. The theorem completely solves the minimum-set enumeration on a fundamental graph product for every base graph, with the answer depending only on the base component count. For connected bases it proves rigidity—exactly two minima—and for tree bases it supplies an infinite family directly answering part of an explicit literature direction to count minimum super dominating sets in trees. The result is structural rather than a finite table or a restatement of the known scalar corona formula.

Same-model review: passed. Independent audit: not yet performed.
