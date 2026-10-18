# Scientific review: large-index monomial perturbations of Euler's product

## Correctness — PASS

The identity \(C_{a,j}(z)=Q(z)/(1-a z^jQ(z))\) has nonnegative coefficients and a unique strictly dominant simple pole because consecutive positive powers of \(z\) occur in \(Q(z)\). Residue calculus gives the coefficient constant, and implicit differentiation of the marked bivariate pole gives the first two cumulants and a Gaussian limit for each fixed parameter. The Dedekind eta transformation, positive-root monotonicity, and small-parameter derivative estimates prove the scaled phase limits and fixed-weight logarithmic expansion. The public script independently compares 975 exact coefficient values using two algorithms; it also checks 36 numerical root/profile quantities and eight fixed-weight asymptotic comparisons. This finite evidence supplements, but does not replace, the infinite analytic proof.

## Originality — PASS within inspected literature

Keith, Schneider, and Sills (2024) formulate fixed-parameter exponential growth for the reciprocal as Conjecture 1. The fixed-parameter pole/mean/variance conclusions here are covered in principle by the standard Flajolet–Sedgewick supercritical-sequence framework and are explicitly **not** claimed novel. The contribution tested for originality is the varying-monomial-index regime \(a_j=e^{\gamma\sqrt j}\) and its continuous growth, mass fraction, variance-phase and duality profiles, together with the explicit fixed-weight second-order rate and asymptotic pole amplitude. Comparing the full motivating article, the relevant supercritical-sequence theorem, and Keith's different false-theta reciprocal gives no same statement or stronger result implying these large-index formulas; targeted mathematical-record searches gave no direct match. A general perturbative transfer theorem not located in this search might imply these formulas; publication priority is not independently established.

## Mathematical value — PASS

The 2024 paper supplies a specifically motivated reciprocal family but treats the coefficient growth qualitatively. The sharp large-index analysis identifies a genuine crossover when the marked-token weight varies at the natural exponential-square-root scale, and shows an exact self-dual mass-fraction curve with a symmetric, maximized Gaussian-fluctuation coefficient. The explicit logarithmic correction and asymptotic coefficient constant provide additional quantitative arithmetic content rather than an arbitrary finite specialization. The findings are restricted to the iterated parameter limit and do not claim uniformity in the original coefficient index.

## Evidence and limits

Primary references: Keith–Schneider–Sills, *Composition-Theoretic Series and False Theta Functions*, INTEGERS 24A (2024), A11, DOI 10.5281/zenodo.11352821; Flajolet–Sedgewick, *Analytic Combinatorics*, supercritical-sequence theorem (earlier lecture notes, Section V.3); Kong–Teo, *An Elementary Proof of the Transformation Formula for the Dedekind Eta Function*, arXiv:2302.03280; Keith, *Reciprocals of False Theta Functions*, arXiv:2412.19998. The modular identity and residue calculations are reconstructed in RESULT.md. Numerical checks do not independently certify infinite conclusions. Possible stronger general transfer or saddle-point literature is the main originality risk.

Self-review: passed. Independent audit: not yet performed.
