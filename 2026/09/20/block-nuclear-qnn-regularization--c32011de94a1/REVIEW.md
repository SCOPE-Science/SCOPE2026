# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The universal bound follows directly from the atomic representation. Each quadratic atom \(w w^\top\) has nuclear norm one, while the full lifted atom \([w;1][w;1]^\top\) has nuclear norm two. Triangle inequalities therefore give both \(\|Z\|_*\le\mathcal R\) and \(\frac12\|M(Z,z)\|_*\le\mathcal R\). Nuclear/operator duality with the off-diagonal test matrix gives \(\frac12\|M\|_*\ge\|z\|_2\), so the proposed \(\Omega\) pointwise dominates both source-paper penalties.

The pure-quadratic and pure-linear equalities have explicit two-atom/eigenvector constructions. The aligned rank-one formula follows from two atoms at \(v\) and \(-v\), with the lower bound supplied by the universal norm inequality. For the orthogonal rank-one formula, the three-atom construction reproduces the moments exactly. The matching quadratic dual certificate \(p(y)=1-2((y-r)/(1+r))^2\) has sup norm one on \([-1,1]\), yielding the same lower value. Sign symmetries were checked separately. The published numerical artifact reproduces all identities to floating-point accuracy and finds no violation of the universal bounds in the stated deterministic pseudorandom tests.

Potential hidden hypotheses were checked: the aggregate relation \(\sum_j\alpha_j=\operatorname{tr}Z\) uses unit hidden weights; exact identification with the original training problem requires enough width to realize the atomic decomposition; and \(\Omega\) is only a lower bound in general dimension.

## Originality

**PASS, to the best of our knowledge.** The motivating 2026 paper was inspected at its lower-bound theorems and the remark describing the unpenalized linear aggregate in the nuclear-only formulation. That paper already derives \(\frac12(\|Z\|_*+\|z\|_2)\) and \(\|Z\|_*\) lower-bound penalties; those results and the observation that the latter can approach a linear model are excluded from novelty.

Bartan--Pilanci's exact neural-spectrahedron paper was inspected at the neural cone, the lifted block semidefinite representation, the output-weight \(\ell_1\) constraint, and its one-dimensional illustration. The exact convexification, lifted block variables, and nuclear-norm background are prior art. Searches using the 2026 source identifier, neural-spectrahedron terminology, scalar-input quadratic-network regularization, block nuclear norms, atomic norms, and synonymous formulations did not locate the combined full-block certificate or the aligned/orthogonal induced-gauge formulas. Existing SCOPE records were also searched by the source identifier and these mathematical objects immediately before publication.

The principal residual originality risk is older convex-geometric, moment, or atomic-norm work that may analyze the same neural-spectrahedron gauge under different terminology. Because the scalar and rank-one formulas are elementary once the correct atomic representation is isolated, prior occurrence of an individual formula would narrow the novelty claim. No checked source was found to combine those formulas with the source-specific domination of both 2026 lower bounds. No high-risk inaccessible source was identified.

## Value

**PASS.** The result produces a strictly stronger convex lower bound at essentially the same lifted-variable level as the source nuclear relaxation, and it explains exactly which part of the original output-weight regularization is lost when the linear aggregate is discarded. The scalar-input case collapses the exact regularized training problem from an SDP to a two-variable convex problem with an \(\ell_\infty\) penalty. The orthogonal rank-one family quantifies nontrivial remaining coupling and gives a concrete benchmark where the new block-nuclear bound improves the source lower bounds from \(1\) to the golden ratio while the exact induced regularizer is \(5/3\).

## Limitations

The theorem concerns one-output degree-two polynomial-activation networks with unit hidden weights and \(\ell_1\) output-weight regularization. The new \(\Omega\) relaxation is not generally exact, does not provide the source paper's closed-form least-squares solution, and is not asserted to be computationally preferable to the exact neural-spectrahedron SDP. No statistical, generalization, or finite-precision claims are made.
