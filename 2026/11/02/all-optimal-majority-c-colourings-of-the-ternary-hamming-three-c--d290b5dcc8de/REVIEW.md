# Scientific self-review

## Correctness — PASS

The graph and weak-majority convention are specified exactly: a class needs induced minimum degree at least three, not a proper-colouring condition. The exhaustive bit-mask implementation lists every subset of orders one through seven (\(1,285,623\) tests), establishes the exact \(54\) size-six rectangular majority classes and excludes size seven, and thereby forces all four-class sizes to be \((6,6,6,9)\). It then checks all three-box combinations and every possible nine-vertex complement without sampling. An independent rook-quotient enumeration reproduces the count \(288\), an explicit assignment supplies existence, and all \(1296\) alphabet/coordinate automorphisms yield the orbit sizes \((18,54,216)\). All claims are finite and exhaustively covered. Risk: the exhaustive verifier must be run on an ordinary Python 3 interpreter as distributed; the proof relies on exact enumeration, not on an external formal system.

## Originality — PASS, with historical-priority risk

Lu, *Exact majority C-colourings of balanced Hamming graphs and grids*, arXiv:2609.31674, Theorem 1, already proves the maximum is four for this graph and supplies rectangular constructions and the isoperimetric class-size lower bound. Those facts are explicitly **not** new. Full-text comparison of Lu's Sections 1–4 and 7 revealed no classification of all extremizers, \(288\)-partition census, common-coordinate rigidity of every optimum, or three-orbit profile. Bujtás et al., arXiv:2608.27669, motivate the Hamming question, and arXiv:2604.20752 supplies the definitions; neither inspected primary source provides this optimizer census. Indexed research and comparable formulations (majority C-colourings, 0-defensive alliance partitions and equitable/internal partitions) were searched. A close indexed result for complete multipartite graphs applies to a different graph class; another for the ternary distance-two threshold Hamming graph has a different edge relation and invariant. Risk: unindexed or inaccessible specialized work may independently enumerate these same optima; novelty is a best-knowledge assessment, not certification.

## Mathematical value — PASS

The optimum colour number alone leaves the structure and multiplicity of optimizers unknown. Here every optimum is forced to be cylindrical along a single coordinate; the full quotient classification distinguishes rigid line and L-shaped leftover cores, counts all \(288\) optimal partitions and classifies them into \(3\) symmetry types. This is a complete extremizer classification for a natural smallest nontrivial odd-dimensional balanced Hamming graph, not an arbitrary isolated output or a mere recomputation of Lu's known maximum. Risk: no generalization to other dimensions has been proved, and the finding is consequently confined to this canonical finite case.

## Source comparison and limits

The proof is complete for exactly \(27\) vertices and uses transparent exhaustive computation for two finite lemmas. Lu's known scalar theorem and construction are credited. The primary papers and searched records do not prove that the structural optimizer result was previously absent everywhere. No independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
