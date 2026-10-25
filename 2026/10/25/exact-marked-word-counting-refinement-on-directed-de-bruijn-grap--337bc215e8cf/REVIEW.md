# Scientific assessment: marked de Bruijn shift-graph refinement

## Correctness — PASS

The result is an all-alphabet/all-length theorem with explicitly fixed graph orientation, loop treatment, initial colours, quantifiers, and edge-counting conventions. The proof has two independent directions: collapsed-alphabet word patterns are stable under incoming and outgoing edge counts, and the exact adjacency-operator identity forces every occurrence of a letter named by a marker to be visible in every coordinate within \(3k-3\) refinement rounds. Combining them yields equality of partitions rather than an unproved claim based on examples. The stabilizer group and Stirling-number orbit formulas then follow from the known automorphism-group theorem and direct equality-pattern enumeration. Three standalone finite programs check 925 rooted instances, 1,899 arbitrary-marker instances, and 3,423 operator identities respectively. The mathematical proof, not finite sampling, supplies the universal conclusion.

## Originality — PASS, with residual priority risk

The closest primary source is Boutin–Goliber–Pelto's *Identifying Codes on Directed De Bruijn Graphs* (arXiv:1412.5842), especially its known automorphism-group and determining-set theorems. Those results do not imply a formula for all stable counting-refinement classes or a universal refinement-depth bound. The independently inspected general color-refinement works of Kiefer–Schweitzer–Selman (arXiv:1503.08792) and Berkholz–Bonsma–Grohe (DOI 10.1007/s00224-016-9686-0) supply broad context but no de Bruijn coordinate-collapse theorem. Targeted literature and research-index searches for the equivalent shift-register, equitable-partition, counting-refinement, marked-word, and stabilizer formulations did not identify prior exact coverage. Searches cannot prove absolute priority; less-visible specialised work remains a risk. The known de Bruijn automorphism theorem is expressly cited as background.

## Value — PASS

The theorem closes a natural mathematical gap between determining sets (a purely group-theoretic property), the coarsest stable directed counting partition, and actual automorphism orbits on symbolic shift networks. It provides an exact answer for every alphabet size, word length and arbitrarily labelled marker set, a length-linear refinement bound independent of alphabet size, class sizes, a complete Stirling orbit census, and a sharp condition for orbit exactness. Its clean obstruction—equality among unused alphabet letters—is intrinsic to the shift relation rather than an arbitrary finite parameter slice. This is a substantive structural classification, not a rephrasing of the pre-existing determining-number formula.

## Limitations and closest comparisons

The refinement here is specified operationally with directed neighbour-counts and no added initial loop-status attribute. It is not claimed to equal full \(C^2\) equivalence in a signature that can test \(R(x,x)\), nor is the general \(3k-3\) bound claimed optimal. Independent verification and publication-priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
