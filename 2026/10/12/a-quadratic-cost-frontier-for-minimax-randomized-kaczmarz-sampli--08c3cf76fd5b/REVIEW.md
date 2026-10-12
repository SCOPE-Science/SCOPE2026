# Scientific review — quadratic cost frontier for simplex-frame sampling

## Correctness — PASS

The claimed objective is a precise one-step conditional worst-case squared-error decrease divided by expected row cost. Positive-price homogenization maps probability sampling bijectively to an information-matrix problem. A second scaling turns it into a semidefinite covering problem. The exhibited dual witnesses match exact primal costs in both price regimes and give a universal upper bound. Complementary slackness, linear independence of the regular-simplex dyads, and the exact boundary eigenspace establish the **entire** optimizer set without assuming symmetric sampling. The proof handles every integer dimension at least two and every positive real exceptional price. An independent rational checker confirms 56 finite primal/dual instances; its finite range is not the proof.

## Originality — PASS, with residual risk

The strongest antecedent is Dai, Soltanalian, and Pelckmans, *On the Randomized Kaczmarz Algorithm* (2014), Sections I–V, especially equations (15)–(17). Their unpriced E-optimal sampling SDP is equivalent to the present general covering formulation **only when all row prices are equal**, and does not state the quadratic exceptional-price threshold or complete parameterized optimizer classification. Gower and Richtárik (2015/2016), Section 5.1, likewise present a more general unpriced optimal-sampling SDP; that framework contains the calculation algorithmically once costs are introduced, but does not imply a formula without solving the specialized problem. Strohmer and Vershynin (2007) provide the row-projection contraction foundation, not the priced solution. Previously disclosed regular-simplex reshuffling calculations and planar Kaczmarz sampling results concern different sampling mechanisms, cost conventions, or asymptotic objectives, and do not imply this threshold. These are implication comparisons, not title comparisons. The complete original text of Agaskar, Wang, and Lu's related 2014 conference paper was inaccessible, leaving possible historical specialization as an explicit residual risk. Literature and record searches do not establish absolute novelty.

## Value — PASS

Variable per-row projection costs are a natural feature of heterogeneous data acquisition, storage, and computation. A minimally redundant tight frame is a canonical model for understanding how economic asymmetry affects worst-case guaranteed progress. The result gives an exact resource-allocation decision at a nontrivial quadratic cost ratio, proves a surprising rigidity of uniform sampling on an entire open price interval, and classifies every optimum including the degenerate transition. It avoids repeated numerical SDP solutions for this full dimension-and-price family. The scope is the one-step guarantee per *expected* action cost, not realized runtime or an exact long-horizon annealed decay rate.

## Closest sources and scientific limits

- Strohmer and Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226v1 (2007): rate analysis for row projections.
- Dai, Soltanalian, and Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863v1 (2014): directly relevant full-text unpriced sampling SDP, including homogeneous covering reformulation.
- Gower and Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (2015): broader unpriced sampling optimization.
- Agaskar, Wang, and Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities* (2014): abstract inspected, complete text unavailable; specialization risk remains.

Self-review: passed. Independent audit: not yet performed.
