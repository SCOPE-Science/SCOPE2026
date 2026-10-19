# Scientific review

## Correctness — PASS
For all odd dimensions \(n=2r+1\), the Walsh eigenspaces have dimensions \(\binom nj\), giving the exact PBH multiplicity lower bound. The classical Young/Johnson harmonic decomposition into orthogonal pair-difference sectors is explicitly identified and sourced; direct coefficient extraction computes the action of each individual homogeneous Walsh restriction on every sector. The resulting coefficient \((-2)^t(-1)^{\lfloor(j-t)/2\rfloor}\binom{r-t}{\lfloor(j-t)/2\rfloor}\) never vanishes for \(0\le t\le j\le r\). Complementing frequencies covers larger degrees. The even-dimensional full-layer obstruction follows independently from complementary equal-degree Walsh columns. The included checker passed 25,752 exact finite assertions. The proof, not the finite tests, supports the quantified conclusion.

## Originality — PASS with residual risk
The critical comparison is with general grid-controllability criteria, distance-regular leader-selection tests, and harmonic Boolean-slice bases. The examined primary papers establish those background frameworks but do not present this explicit optimal odd-hypercube input layer, complete full-column-rank claim for every homogeneous eigenspace, and even-dimensional parity obstruction. The calculation of the exact restriction scalar on each harmonic sector is the distinctive step. Published Fourier restriction/concentration records on mixed degree bands or nonbinary shells have different premises and do not directly entail the theorem. Closely related older association-scheme identities or later unindexed specialized studies could contain an equivalent reformulation; independent exhaustive literature validation has not been done.

## Value — PASS
This is a natural minimal-sensor/leader placement problem, not an arbitrary matrix rank exercise: spectral multiplicity gives a strong lower bound but not the existence of a vertex-selector input matrix attaining it. The finding constructs such a minimum set for every odd-dimensional hypercube and proves an exact obstruction to all single-shell designs in even dimension. The explicit, dimension-uniform placement avoids combinatorial optimization over \(2^n\) candidate vertices and supplies a useful benchmark for network control and observability.

## Scope and risks
No claim is made about the unrestricted even-dimensional minimum, robustness to edge-weight perturbations, energy-optimality, inputs with shared channels, or an independent audit. The harmonic basis itself is prior literature and is cited rather than claimed as new.

Self-review: passed. Independent audit: not yet performed.
