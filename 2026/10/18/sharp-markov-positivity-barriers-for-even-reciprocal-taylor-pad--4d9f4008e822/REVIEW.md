# Scientific assessment

## Correctness

**PASS.** The formal Taylor-series calculation gives the first two coefficients beyond fourth or general even order. Directed shortest-path distance controls every off-diagonal entry. In the only borderline case with \(m+2\) states, the first term eliminated by the rational approximation is followed by a negative matrix-power entry, giving a positive next contribution. The \(m+3\)-state pure-birth chain realizes the first negative coefficient. The seven-state exact interval follows from explicitly verifiable rational-function identities, eleven coefficientwise positivity certificates, and a two-chart Descartes proof of uniqueness of the positive polynomial root. The package includes a standalone exact-arithmetic reproducer. The finite checks are not used to infer the general theorem.

## Originality

**PASS under the inspected evidence, with residual risk.** Work on positive systems under diagonal Padé discretization, entrywise matrix exponential evaluation, and published fourth-order \([2/2]\) Markov positivity barriers gives genuine prior context, but the precise rational approximant \([0/m]\), arbitrary-even-order state threshold, and the fourth-order seven-state all-step classification were not covered by the material inspected. Previously reported \([0/2]\) path phenomena are excluded from the new even-order range. A plausible 1996 Padé matrix-exponential paper remained inaccessible in full; equivalent unindexed work is a residual risk. A failed keyword search is not a proof of novelty.

## Mathematical value

**PASS.** The number of Markov states needed before a classical high-order rational exponential update can violate positivity is an intrinsic stability barrier; here it is determined sharply for all even orders at least four. The first fourth-order counterexample additionally has an exact, nonmonotone positivity domain, illustrating the practical danger of assuming that smaller steps always enforce a physical sign constraint. The classification is both structural and exactly checkable.

## Limits and prior literature

The universal claim is local in timestep; only the designated seven-state example has a complete positive-step interval. The finite exact-arithmetic checks support a separately supplied proof rather than establishing the infinite statement. Principal comparisons: Zappavigna–Colaneri–Kirkland–Shorten (2010), Xue–Ye (matrix exponentials of essentially nonnegative matrices), Rossi–Colaneri–Shorten (2011), and the published eight-state \([2/2]\) result. Arioli–Codenotti–Fassino (1996) was not accessible for full comparison. Independent external validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
