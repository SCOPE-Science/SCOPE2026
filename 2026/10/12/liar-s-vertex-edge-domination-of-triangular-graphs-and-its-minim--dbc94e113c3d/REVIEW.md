# Scientific review

## Correctness — PASS

The central reduction has a precise quantifier justification: the three edges of each triangle among original pairs \(ab,ac,bc\) have the same closed edge neighborhood, namely all pairs incident to \(\{a,b,c\}\). The two-edge liar constraint forces three monitors in that neighborhood, and the converse implies both original constraints. The optimal edge lower bound uses an exhaustive partition into isolated-vertex cases, two-vertex components, and components of order at least three. Trees on blocks of order at least four attain the lower bound. Defect \(4e-3c\) classifies every optimum for \(n\ge8\) because total defect is at most three; Cayley's formula counts each labeled tree. Small boundaries \(n=3,4\) are treated explicitly. The verifier cross-checks independent formulations, including original graph neighborhoods, but only finite instances. An independent proof audit remains outstanding.

## Originality — PASS, with residual risks

Bhattacharya–Paul (arXiv:2310.07465v1) defines the exact liar's vertex-edge invariant and addresses algorithms and complexity on other graph families, not triangular-graph scalar or minimum-set enumeration. Bhattacharya–Paul (arXiv:2310.07452v1) studies general \(k\)-vertex-edge domination, whose \(k=3\) case is equivalent here; that general definition is not a proof of the exact triangular result. Their subsequent arXiv:2507.04721 treats chordal subclasses, whereas \(T_n\) has an induced four-cycle for \(n\ge5\). Relevant equivalence, line-graph, triangular, incidence-cover, and general \(3\)-ve searches did not locate a dominating exact result. Search failure is not a uniqueness proof, and an equivalent older triple-incidence covering theorem remains a genuine risk.

## Value — PASS

This is a new exact evaluation for a fault-tolerant domination invariant on a classical infinite strongly regular graph family, not a numerical sample. The stronger assertion classifies and counts every optimum configuration for all \(n\ge8\), with a nontrivial exceptional triangle class and an explicit labeled-tree formula. It gives structural information not entailed by general complexity or tree algorithms, and shows a direct graph-design interpretation of the optimum configurations.

## Closest literature and limitations

The closest original sources are arXiv:2310.07465v1 (foundational liar's variant), arXiv:2310.07452v1 (general \(k\)-ve framework), and arXiv:2507.04721v1 (later chordal subclass algorithms). The enumeration begins at \(n=8\); the smaller census is not claimed in general, apart from \(n=4\). There is no claim of a full all-size polynomial, independent validation, or exhaustive novelty certification.

Self-review: passed. Independent audit: not yet performed.
