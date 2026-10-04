# Review

## Correctness
PASS. The point-convergence contradiction follows directly from Itô's formula for \(\log S\): under convergence to \(E_0\), every deterministic drift term in \(d\log S\) cancels asymptotically except \(-a^2/2\), while \(B_1(t)/t\to0\). This contradicts convergence of \(S\) to a positive constant. The boundary inverse-gamma density solves the zero-current stationary equation exactly, and its moments agree with the bundled rational-arithmetic verification.

## Originality
PASS. Searches for the exact source, disease-free stationary distributions, multiplicative mortality noise, inverse-gamma susceptible laws, and deterministic point convergence found no covering record. The closest 2017 SIRS predecessor has infection-proportional transmission noise, which vanishes on the disease-free face; the closest inspected open stochastic SIR literature establishes stationary-distribution methodology for different diffusions. The classical inverse-gamma family itself is not claimed as new.

## Value
PASS. The correction changes the scientific interpretation of the source's extinction regime: the disease can go extinct without the susceptible population collapsing to a deterministic point. At the paper's own extinction parameters the exact boundary variance is \(2025/79\), making the surviving stochastic spread substantial and directly relevant to the numerical narrative.

## Closest literature and limitations
The closest literature is Cai, Kang, and Wang (2017), DOI 10.1016/j.amc.2017.02.003, which explicitly uses a disease-free stationary distribution but has a different noise structure, and Cao et al. (2019), DOI 10.1038/s41598-019-47131-6, which analyzes stationary distributions for a different stochastic SIR diffusion. The present result does not prove convergence in distribution of all interior solutions to the boundary inverse-gamma law; it proves the exact boundary stationary law and rules out almost-sure convergence to the deterministic disease-free point when susceptible noise is nonzero.

Same-model review: passed. Independent audit: not yet performed.
