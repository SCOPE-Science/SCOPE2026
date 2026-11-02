# Review of two-sided fluctuation bounds for acyclic color classes

## Correctness
PASS. The proof reconstructs the independent edge coloring and the exact de Bruijn cycle criterion. Negative association is proved directly for each edge's one-hot indicators and then propagated through independent unions and the common-direction decreasing acyclicity maps. The variance upper bound and Chernoff estimate follow from this established dependence property. Conditioning on the labels of all self-loops gives the exact identity \(\mathbb E[M\mid\mathcal L]=(q/a)Z\); the law of total variance gives the finite-size lower bound. The occupancy variance and its limit are elementary exact computations. The stated Airy constant and one-color asymptotic are taken from Gravner--Kulhanek, not recomputed here. Exhaustive exact-rational tests for \(s=2,3\) support the finite-dimensional formulas, but finite tests do not prove the general theorem.

## Originality
PASS, qualified. Gravner--Kulhanek's full text, especially Theorem 3 and Proposition 48, was examined for the one-color acyclicity asymptotic and missing-count expectation. It does not state the present two-sided variance inequalities, loop-occupancy obstruction, or normalized almost-sure law. Joag-Dev--Proschan's established negative-association machinery implies the upper-bound mechanism; that ingredient is not claimed original. The added comparison is the exact conditional loop-occupancy lower bound and its explicit positive order-\(s^{1/3}\) coefficient, combined with concentration on the \(s^{2/3}\) deficit scale. Targeted mathematical-record searches for equivalent or dominating statements did not identify one; full access to the older general negative-association article was not obtained. Historical priority and possible general dependent-occupancy implications remain limitations.

## Mathematical value
PASS. The expected number of missing constant images is of order \(s^{2/3}\) in the critical two-neighbor model, while the source paper's principal convergence statement concerns the much larger \(s\) scale. The theorem gives a quantitative almost-sure law on the natural missing-count scale and shows that fluctuations cannot collapse arbitrarily: the independent self-loop labels alone force a positive polynomial lower bound on total variance. It is a motivated structural limitation on any future sharp fluctuation theorem. It does not determine the optimal variance exponent or a central limit theorem, and the upper bound alone is a standard consequence of negative association.

## Closest literature and limits
- Gravner and Kulhanek, *Random Cellular Automata and deBruijn Graphs*, arXiv:2610.31764v1 (2026), Theorem 3 and Proposition 48: exact single-color asymptotic and the expectation/weak large-scale convergence.
- Joag-Dev and Proschan, *Negative Association of Random Variables with Applications* (1983): general negative-association framework, relevant to the upper bound.
- The proof is self-contained apart from the cited single-color asymptotic; the limiting variance order is not established.

Self-review: passed. Independent audit: not yet performed.
