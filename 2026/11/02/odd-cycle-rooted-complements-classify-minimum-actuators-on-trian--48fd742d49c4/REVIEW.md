# Scientific review: minimum coordinate actuators on triangular graphs

## Correctness

**PASS.** The unsigned incidence identity \(\mathcal L=(2n-2)I-C^{\mathsf T}C\) gives all three eigenspaces without any unproved spectral assumption. The PBH criterion splits into invertibility of an \(n\)-edge unsigned incidence submatrix and injectivity of the zero-sum potential map on the selected edges. The first is equivalent to odd-unicyclic connected components; the second is automatic at the sharp cardinality except for the balanced complete bipartite graph \(K_{3,3}\) at \(n=6\). This proves the full quantifier range \(n\ge5\), with small cases established separately. The executable verifier passed 6600 finite check groups, including exhaustive \(n=5,6\) tests, assembled-Laplacian PBH checks, selected Kalman matrices, and independent exact generating-function coefficients. Finite checks are not substituted for the analytic argument.

## Originality

**PASS on the inspected evidence, with residual literature risk.** Yuan et al. (2013) already establish the general maximum-multiplicity paradigm. Consequently the numerical minimum \(\binom n2-n\) alone is a known-framework consequence, not a separate novelty assertion. The assessed contribution is a complete combinatorial classification of all minimum *coordinate* placements, the sharp \(n=6\) exceptional obstruction, and their exact count. Monshizadeh et al. (2014) prove a zero-forcing equivalence for robust qualitative classes, whereas the constructed placement here has no initial forcing move. Monfared–Mallik (2018) supplies the known unsigned-incidence/odd-cycle ingredient; the further PBH restriction and density exception are not its stated result. Dai (2022) studies different graph families and a reduced leader–follower framework. Relevant published mathematical records and earlier same-topic claims were checked for implications, not only title similarity. Unindexed or inaccessible specialist historical papers remain a genuine originality risk.

## Mathematical value

**PASS.** For the natural triangular graph (the interaction graph of unordered pairs), a general existence-and-rank test is replaced by a complete graph-theoretic description of every optimal independently actuated vertex set. The sharp six-label exception shows that eliminating the largest eigenspace alone is insufficient, and the explicit non-zero-forcing optimum separates fixed-Laplacian design from robust zero-forcing design. The exact counting series and constructive optimum make the classification usable for selecting and enumerating actuator configurations.

## Boundaries and closest literature

The result assumes a fixed unit-weight Laplacian, independent coordinate inputs, and complete-state controllability. No general weighted result or robust structural guarantee is asserted. Most directly related sources are Yuan et al., *Nature Communications* (2013), Monshizadeh–Zhang–Camlibel (2014), Monfared–Mallik (2018), and Dai (2022). No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
