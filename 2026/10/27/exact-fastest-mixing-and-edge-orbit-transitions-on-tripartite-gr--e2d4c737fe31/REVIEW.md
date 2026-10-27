# Scientific review

## Correctness — PASS

Averaging over a graph-automorphism subgroup is valid because the centered spectral norm is convex. The invariant Laplacian has the four displayed nonzero spectral modes, including all dimensions and multiplicities for \(p,q\ge2\). The lower-bound proof uses valid linear mode and budget inequalities in four exhaustive parameter regions. Equality forces the asserted probabilities and intervals; the feasible candidate for each regime attains the lower bound. Nonnegativity and automorphism averaging extend the mandatory orbit-deletion conclusion from invariant optimizers to **all** unrestricted optimizers for \(q\ge4p\), and likewise imply some equal-parts edge is used by every optimum when \(q<2p\). The checker independently reproduced the predicted SLEM by linear programming and full dense eigendecompositions for selected instances, and checked exact rational endpoint inequalities for 2,478 cases. Its finite checks are supplementary, not an infinite proof.

## Originality — PASS with stated residual risk

The main comparison is Boyd–Diaconis–Parrilo–Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, Section 5.4.2: the full text supplies a general complete multipartite spectral block formula, but no explicit \(K_{p,p,q}\) phase diagram or interval of all invariant optima. The earlier Boyd–Diaconis–Xiao treatment explicitly solves complete bipartite graphs. Jafarizadeh's 2010 multipartite paper treats equal-size path/cycle arrangements; its balanced three-part cycle is an already covered boundary \(q=p\), not the imbalanced parameter family. The exact formulas at balanced parameters and general symmetry reduction are explicitly prior art. Available historical claims and public semantic searches did not identify a stronger covering result. A specialized unindexed paper or another formulation might still duplicate the classification.

## Value — PASS

A complete three-class multipartite network is a natural baseline for symmetric stochastic design. Beyond finding one optimal value, the theorem determines the sharp change from mandatory positive intra-equal-parts transitions to optional removal and then forced removal. It also gives all invariant optimal probabilities, including nonuniqueness across an infinite parameter region. These transitions are not readable directly from a general SDP specification; they provide a reusable exact test family for Markov-chain weight design and consensus protocols.

## Scope and risks

Only uniform-stationary symmetric Markov chains are covered. No claim is made to classify nonsymmetric optimal matrices or nonuniform reversible chains. The balanced \(q=p\) case is a consistency check with pre-existing results. Originality is supported by inspected full texts, search comparisons and ledger-overlap checks but is not a guarantee of uniqueness across unindexed literature.

Self-review: passed. Independent audit: not yet performed.
