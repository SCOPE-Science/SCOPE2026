# Self-review

## Correctness

PASS. The proof reduces ordinary irredundance to an exact private-neighbor criterion. For a selected \(a_i\), either \(a_i\) is self-private because the selected opposite-side vertices lie in \(\{b_i\}\), or an external witness \(b_j\) must satisfy \(j\notin J\) and \(I\setminus\{i\}\subseteq\{j\}\). The symmetric criterion for \(b_j\) forces the complete classification. The enumerators follow by counting the resulting disjoint index patterns, and maximality follows from explicit one-vertex extension arguments. A direct exhaustive checker agrees with the classification and both enumerators for every \(3\le n\le8\).

Risk: finite computation cannot prove the infinite theorem. The all-\(n\) conclusion instead rests on the structural criterion, whose quantifiers and boundary cases are proved explicitly.

## Originality

PASS. Statement-level and alias searches covered crown graphs, \(K_{n,n}\) minus a perfect matching, \(K_{n,n}\) minus a one-factor, and bipartite Kneser \(H(n,1)\). The closest structural comparison located is the complete-multipartite irredundance classification, which does not cover crowns because \(\operatorname{Cr}_n\) is not complete multipartite for \(n\ge3\). A full searchable-text check of the 2011 bipartite-irredundance paper found no occurrence of “crown”, “complete bipartite”, or “perfect matching”; its principal notions are different bipartite irredundance variants. No checked source stated the all-set crown classification, the maximal-set classification, or the cubic/quartic perturbation layers.

Residual risk: older specialized literature may use only an uncommon equivalent name and may not be indexed by the searched terminology.

## Value

PASS. The theorem isolates a natural structural perturbation phenomenon. The canonical deletion of one perfect matching leaves the lower and upper irredundance numbers of \(K_{n,n}\) unchanged, yet creates entire cubic and quartic layers of irredundant sets and changes maximality among mixed two-sets. The exact private-neighbor classification therefore reveals information invisible to the two scalar irredundance parameters and supplies reusable structure for comparisons of domination-type set systems on crowns.

Self-review: passed. Independent audit: not yet performed.
