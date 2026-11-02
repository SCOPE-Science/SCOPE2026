# Review: Minimum odd-neighborhood witnesses in cubic line graphs

## Correctness — PASS
The edge-cut identity reduces odd-neighborhood support to a cut plus internal selected edges. The cycle/girth and cyclic-connectivity hypotheses exhaust all possible support-five cases, and the cubic Moore bound enforces the ten-vertex perfect-matching boundary. The proof covers every finite connected cubic graph satisfying the hypotheses. Two complete, independent stdlib programs verify the low-weight classification and the required small cuts for three classical examples; finite checking is explicitly not the general proof.

## Originality — PASS, qualified
Bohman–Dudek–Frieze–Pikhurko (2009), Javelle–Mhalla–Perdrix (2012) and Cattanéo–Perdrix (2015) establish the graph-flip parameter, local-complementation identity and broader bounds/complexity, while Došlić (2003) establishes fullerene cyclic five-edge-connectivity. The accessible primary texts were examined beyond abstracts and do not state this minimizer classification or the fullerene stabilizer multiplicity. The theorem deliberately excludes all these known ingredients from its novelty claim. Comparisons included odd-neighborhood synonyms, graph-state stabilizers and local minimum degree; an unindexed equivalence remains possible. Searching is not proof of novelty.

## Value — PASS
An exact equality-case theorem over the infinite cyclically robust cubic family distinguishes edge, pentagon and exceptional matching mechanisms. The fullerene corollary locates precisely twelve additional minimum-weight stabilizer elements outside the generators across every fullerene order. This motivated, structural multiplicity refinement is not reducible to the known total number of pentagons without the edge-cut parity theorem.

## Closest earlier work and limitations
- Bohman et al., *Flips in Graphs*, arXiv:0903.2201v1: optimization via odd neighborhoods, random graph focus.
- Javelle et al., arXiv:1204.4564v1, and Cattanéo–Perdrix, arXiv:1503.04702v1: local minimum degree identity, general bounds and computation.
- Došlić, DOI: 10.1023/A:1023299815308: cyclic five-edge-connectivity of fullerenes.
- An inaccessible or unindexed alternative graph-state/additive-code enumeration remains a residual priority risk. The full graph family has a mathematical proof; the supplied finite programs illustrate it without purporting to exhaust the family. No code distance of an independently encoded quantum error-correcting code is asserted.

Self-review: passed. Independent audit: not yet performed.
