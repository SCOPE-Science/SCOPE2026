# Assessment of the matching-subdivision negative-type theorem

## Correctness

**PASS.** The graph distance categories are verified independently by shortest-path computation, and the proof decomposes the entire zero-sum space without omitting modes. The paired-standard quadratic block has determinant \(2[b(2-a)-2(a-1)^2]\), whose unique zero in \((0,1)\) gives the universal threshold. The only potentially competing global modes are **strictly** negative at the critical exponent: their \(2\)-by-\(2\) determinant is \(2r(1-c)k+(r/t)[6-2c+4(r-1)k]>0\) when unmatched original vertices exist; otherwise their form is \(-2r[3-c+2(r-1)k]x^2\). The remaining modes are negative, so the nullity and the embedding dimensions follow. The general negative-type interval theorem supplies strictness for smaller powers; explicit standard-mode positive vectors rule out larger powers. The standalone checker passed 136 supplementary tests in 16 independently reconstructed graphs, but the proof is analytical and all-order.

## Originality

**PASS, with historical-priority uncertainty.** Obata–Zakiyyah, Theorem 3.9 (2018), concerns the graph from which a matching has only been deleted, not subdivided; its unpowered endpoint result does not imply the universal variable-exponent law for the larger metric containing intermediate vertices separated by distance three. Młotkowski–Obata (2024), Lou–Obata–Huang (2020), and Choudhury–Nandi (2023) discuss quadratic embedding constants and particular graph operations; inspection of their primary text did not identify the two-parameter result. The present family for at least two matching subdivisions is not a nontrivial complete-join graph, excluding the main structural assumptions of the first two join papers. Li–Weston (2009) gives only the generic interval theory. Semantic searches also did not identify an equivalent known claim or directly dominating formula. This is a best-knowledge originality assessment, not a proof of literature uniqueness.

## Mathematical value

**PASS.** A matching is a canonical edge set on which to test subdivision of a dense graph. The exact exponent's **independence of both graph order and number of subdivided edges** is a structural classification not read from conventional quadratic embedding constants. The equality space increases in dimension with the matching while the critical Hilbert embedding dimension remains exactly the number of original clique vertices. These facts quantify how multiple minimal path substitutions change finite-metric Hilbert embeddability and distinguish subdivision from mere deletion.

## Closest literature and limitations

The closest motivating published theorem is Obata–Zakiyyah's 2018 deleted-matching computation; the most plausible broader comparisons are the 2020 and 2024 join-QEC papers, with their applicability explicitly checked. Li–Weston's theorem is used for the interval step. The result is limited to unit-edge graphs formed by once subdividing at least two pairwise disjoint edges. The checker is finite and does not certify all parameters. Historical priority remains to be independently examined.

Self-review: passed. Independent audit: not yet performed.
