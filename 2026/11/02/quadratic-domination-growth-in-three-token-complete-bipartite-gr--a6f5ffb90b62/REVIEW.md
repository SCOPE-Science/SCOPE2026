# Self-review

## Correctness — PASS
The domain is all integers \(2\le m\le n\) with \(n\ge4\), and only fixed \(m\) is used in the asymptotic conclusion. The lower bound projects selected one-\(A\)-token configurations to pairs in \(B\); any triangle of the missing-pair graph must be a selected all-\(B\) configuration. Deleting at most one edge per such triangle and applying Mantel yields \(\gamma\ge\binom n2-\lfloor n^2/4\rfloor\). The upper construction has disjoint families of the stated exact sizes. The proof checks all four possible numbers of \(A\)-tokens and the boundary \(m=2\); the same-half choice of a second \(B\)-vertex is available because \(n\ge4\). The finite verifier checks actual graph adjacency for 95 pairs, an exhaustive triangle-deletion inequality on 33,864 labelled graphs, and one exact small optimum. Finite tests corroborate but do not establish the unbounded theorem.

## Originality — PASS, qualified
Chinman et al., arXiv:2610.28936v1, study the same graph and parameter but give only degree/independence bounds at token number at least three; their Theorem 1.2 does not imply the sharp one-quarter coefficient for fixed \(m\). Fabila-Monroy and Gómez-Galicia, arXiv:2509.16448v1, derive a Mantel-based asymptotic for three-token *complete* graphs, a different token graph with a smaller coefficient. Acosta Troncoso, Caldera Caldera, and Rivera, arXiv:2610.31557, solve the two-token bipartite problem, not the current three-token one. The latter manuscript explicitly references work in progress on domination of complete-bipartite token graphs and Turán numbers; that unpublished work has not been compared and remains a material priority risk. Searches for the exact graph, aliases and asymptotic parameters in public research records found no public result covering the claim. Searches alone do not certify priority.

## Mathematical value — PASS
The coefficient \(1/4\) replaces currently published bounds that leave both the leading coefficient and even the quadratic order unresolved from above for fixed \(m\). The result supplies a uniform finite lower bound, an explicit dominating family with only a fixed-\(m\) linear gap, and a natural extremal-graph explanation via triangles. This is a motivated structural improvement on the higher-token problem in the motivating work, not a table lookup or a mere symbolic restatement.

## Limitations and nearest literature
The exact linear and constant terms of the domination number are not proved, and the limit does not cover growing \(m\). The proof does not establish novelty against unpublished related work, which may use the same Turán approach. The computational evidence checks only finite dimensions. See RESULT.md and AUDIT.json for explicit source comparisons and checked hypotheses.

Self-review: passed. Independent audit: not yet performed.
