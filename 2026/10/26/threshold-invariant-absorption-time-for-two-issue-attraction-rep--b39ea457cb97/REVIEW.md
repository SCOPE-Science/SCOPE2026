# Independent mathematical audit

## correctness

PASS

Equal-parity pairs are identical or complements and never change. An unlike-parity pair agrees on one issue and differs on one. Away from weight ties it has exactly one update-causing issue, the differing issue for copying and the agreeing issue for opposition, so it independently converts the focal parity to that of the target with probability 1/2. Thus the entire parity dynamics is a lazy voter step, with probabilities i(N−i)/(2N²) each way and the other attempts retained as holding probability. With distinct agents the denominator is 2N(N−1). Endpoints are exactly the union of consensus and complementary-pair configurations; each interior state has a positive-probability path to an endpoint, implying finite mean absorption for fixed N. The bounded martingale fixes at N with probability a/N. Killing on endpoints gives Q^t 1 for survival. Taking first differences of the Poisson recurrence yields d_{i+1}−d_i=−2N(1/i+1/(N−i)); d_i=2N(H_{N−i}−H_{i−1}) telescopes and sums to zero across the N differences. Summation by parts gives the equivalent mean 2N[N H_N−a H_a−(N−a)H_(N−a)], yielding the claimed entropy limit from H_k=log k+γ+O(1/k) and an O(N²) maximum. The two-agent example has success probability 1/4 each attempted step, with copying giving consensus and opposition giving strict polarization; a similarity tie can instead freeze both parities. Inspected verify.py: exact finite lumping and mean checks, not the universal proof; not executed.

## originality

PASS

The specific projection and resulting attempted-update invariance across strict shared thresholds are the distinct claim. The update model, absorbing categories, and neutral voter-chain calculations are prior. Mintz et al. do give qualitative L=2 absorption-time discussion in the inspected v2, but no equivalent exact law was found. An isolated attracting interior point of the type in their schematic cannot attract different initial parity masses in the frozen regime, whose deterministic drift preserves total parity mass. The caption alone does not specify an actual threshold/rate experiment in that regime.

## value

PASS

This motivates a structural invariant in the stochastic two-issue model rather than a new gambler's-ruin computation. Researchers comparing parameter-dependent convergence can know exactly when attraction versus opposition is invisible even to the full attempted-update absorption law, while still changing consensus versus polarization. The finite-N distribution and uniform polynomial mean bound rule out a plausible metastability mechanism in the stated regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
