# Self-review

## Correctness — PASS

For each two-species competition block, the explicit positive-equilibrium formula has two positive regimes separated by a strict infeasibility interval. Choosing disjoint intervals across \(\lfloor n/2\rfloor\) blocks produces a rigorously interlaced sequence of positive and negative solution witnesses. A finite-matrix resolvent bound proves their persistence under fully positive cross-block interactions, and further coefficient perturbations preserve them on an open set. The Jacobian of an early positive block has negative determinant and hence a positive real eigenvalue, while its other blocks are hyperbolic; stability type persists for small coupling. The final witness is globally attracting by a strictly positive symmetric part of the interaction matrix and a relative-entropy Lyapunov identity. Singular gap points are handled by explicit incompatibility, and the theorem makes no claim about complete perturbed-band classifications. The accompanying exact-arithmetic tests cover ten examples but are not substitutes for the general proof.

## Originality — PASS (best-knowledge, historical risk)

The closest paper, Lechón-Alonso et al. (2026), already reports examples of feasibility re-entry for four species, eventual feasibility at large self-competition, and high-dimensional random-sampling behavior. These established results are **not** relabeled as new. The new implication is an explicit arbitrary-size lower bound on the number of **robust feasible components in completely interacting, strictly positive competitive matrices**, plus contrasting unstable and globally attracting feasible witnesses. The main article text/figures do not give this arbitrary-size construction. The supplementary material was not available for full inspection; it is a genuine priority risk. AlAdwani–Saavedra (2022) supplies a general formalism for feasibility inequalities, not an examined identical lower bound. Searches under component counts, self-regulation reversals, positive Lotka–Volterra interaction matrices, and weakly coupled competitive modules found no implication-equivalent statement. Searches do not prove uniqueness.

## Mathematical value — PASS

The question is motivated by the gap between observed finite-size nonmonotone feasibility and the reported typical single transition in very large random competitive communities. The theorem shows their coexistence with an **unbounded, dimension-linear worst-case count that survives full interspecific connectivity and parameter perturbations**. It distinguishes the existence of positive equilibria from their stability, exhibiting many unstable feasible regimes and an eventual globally attracting regime. This is a structural boundary for interpreting the random-community result, not an arbitrary numerical slice.

## Evidence and limitations

Full body of the motivating article's public main text and Figure 2 statements were compared with the claim; its supplementary appendix was not read. Further references included AlAdwani–Saavedra (2022), mainly available through its public abstract/method excerpt. Complete proof and an executable exact arithmetic checker accompany the claim. Equivalence under a different historical terminology remains possible. No claims of random-ensemble likelihood, exact optimal component count, or stable coexistence in the earlier regimes are made.

Self-review: passed. Independent audit: not yet performed.
