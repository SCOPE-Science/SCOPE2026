# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The proof reduces the two graph families to established forbidden-subgraph characterisations of ordinary mutual visibility. Inclusion-maximal mutual-visibility sets correspond respectively to K4-saturated subgraphs of K_n and C4-saturated subgraphs of K_{m,n}. Such saturated subgraphs are connected: an edge between distinct components cannot create a new bridgeless forbidden graph because that new copy would contain an old alternate path between the endpoints. In the bipartite case, maximal C4-free graphs first have no isolated vertices, so opposite-side vertices can be chosen in distinct components. Connectivity of the selected host-edge graph is equivalent to connectivity of its line graph, which is the induced graph on the selected vertices. The stated maxima and the 2n-3 lower formula then follow from classical extremal/saturation results. Exhaustive definition-level checks on small instances found no counterexample.

Potential edge cases were checked separately. The main triangular-graph statement is stated for n>=4, where the K4-saturation theorem applies conventionally. The rook statement assumes m,n>=2, exactly the nontrivial complete-bipartite range.

## Originality

PASS, to the best of our knowledge. The September 2026 paper introducing connected mutual visibility was inspected in its accessible full-text rendering; its listed exact families do not include line graphs or Cartesian products of complete graphs, and searches within that rendering found no occurrences of `line graph`, `Cartesian`, `Zarankiewicz`, `complete bipartite`, or `L(K`. External searches combining `connected mutual-visibility` with line graph, rook graph, Hamming graph, Cartesian product, K4-free/C4-free, Turan, and Zarankiewicz returned no prior formula matching the result.

The 2023 Cartesian-product paper and the 2024 diameter-two paper were checked for the ordinary forbidden-subgraph correspondences. The 2024 lower-mutual-visibility paper already proves mu^-(K_m square K_n)=m+n-1 through the Bollobas-Wessel theorem, so that statement is explicitly treated as prior work. Searches did not locate a corresponding published formula mu^-(L(K_n))=2n-3; here it follows by combining the 2024 K4-free translation with the classical Erdos-Hajnal-Moon saturation theorem.

Residual risk is primarily the recency of connected mutual visibility: a parallel observation may be unindexed, or a later revision of arXiv:2609.18877 may add these families. No specific inaccessible paper was found whose known title, abstract, or theorem statement suggests coverage of the connected formulas.

## Value

PASS. The result computes the new connected parameter exactly on two classical diameter-two graph families, one by a closed Turan formula and the other by an exact reduction to the Zarankiewicz problem. The stronger all-maximal connectivity statement shows that the connectivity constraint is automatically satisfied at every terminal ordinary mutual-visibility set, not merely at an extremizer. The triangular-graph argument also yields an exact lower mutual-visibility value that appears not to have been recorded. The proof exposes a reusable saturation-connectivity mechanism rather than relying on case enumeration.

## Limitations

- The rook-graph value remains as hard to evaluate numerically as the classical Zarankiewicz number in general.
- The forbidden-subgraph translations and all classical Turan/saturation/Zarankiewicz ingredients are prior work.
- The proof is short once those translations are available; novelty lies in the connected-visibility consequence and the maximal-set structural upgrade.
- Finite exhaustive verification supports but does not replace the symbolic proof.
- No independent validation is asserted.
