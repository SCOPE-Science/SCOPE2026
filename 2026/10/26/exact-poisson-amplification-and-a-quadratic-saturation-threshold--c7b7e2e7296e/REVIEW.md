# Scientific review of the rook-graph Poisson endpoint theorem

## Correctness — PASS

The spectrum of the unnormalized Cartesian graph Laplacian decomposes into three orthogonal tensor sectors, giving its Moore--Penrose inverse directly. The four vertex-pair orbit values are independently expanded from that tensor formula. Their exact signs, multiplicities, and the zero-row-sum property give the sharp \(\ell^\infty\) absolute row sum and all equality masks. The numerator of the only variable-sign column orbit has a quadratic discriminant and its integer cutoff is proved irrational for every relevant parameter. The claimed global bound and both scaling limits are algebraic consequences of the exact norm formula. The standalone rational-arithmetic verifier independently inverts several full graph Laplacians after their rank-one regularization; finite tests do not establish the general theorem.

## Originality — PASS within checked evidence

Ellis (2003) gives general Green-function formulas for Cartesian products, which subsume the kernel decomposition but not an evaluated absolute-row endpoint constant or its cutoff. Beveridge (2015) gives general hitting-time and spectral representations; Fontan and Altafini (2021) give general examples and structure of sign-indefinite Laplacian pseudoinverses. The relevant original sections were inspected and the rook-graph max-norm phase diagram, exact saturation, and quadratic scaling corner were not stated there. Searches using Green inverse, Poisson stability, rook/lattice graphs and line-graph aliases did not identify a stronger exact endpoint result. There remains a real risk of an equivalent calculation in unindexed articles or as an unstated corollary of a known general formula; no independently certified priority is asserted.

## Mathematical value — PASS

This is an exact two-parameter stability classification of mean-zero Poisson inversion on an infinite family of highly symmetric graphs. The theorem identifies a finite, sharply located order-of-squared-width threshold at which extending the graph in one direction produces **no further change whatsoever** in worst-case vertexwise amplification, and shows that the optimizer's sign geometry changes at precisely that threshold. The nontrivial cubic-rescaled corner law quantifies how saturation sets in; the universal bound identifies the four-cycle as uniquely most expansive. These are structurally motivated operator-norm facts beyond simply tabulating Green-matrix entries.

## Scope and residual risks

The norm is on all vertex functions (despite the operator annihilating constants) and uses an unnormalized Laplacian. No assertion is made about arbitrary graph products, weighted graphs, normalized Laplacians, other input constraints, or independent validation. The known generic tensor Green formula means the degree of originality depends on the sharp sign-and-norm classification rather than on the kernel itself.

Self-review: passed. Independent audit: not yet performed.
