# Independent mathematical audit

## correctness

PASS

For a two-state generator with exit-rate sum s, write \(Q=-s(I-\Pi)\) with stochastic rank-one projector \(\Pi\). One midpoint half-step is \(\Pi+r(I-\Pi)\), where \(r=(1-hs/4)/(1+hs/4)\); squaring replaces r by \(r^2\in[0,1]\), so every entry is nonnegative for all h and row sums stay one. For the three-state pure-birth generator, exact multiplication gives endpoint entry \(R_{12}=16h(4-h)/(h+4)^3\), while all other entries are nonnegative; therefore positivity holds exactly for \(0\le h\le4\) and fails for every larger h. Independent matrix replay reproduced the transition matrices and sign change.

## originality

PASS

Classical positivity/absolute-monotonicity theory gives a universal radius and the 2015 source records radius four for this method, but no inspected source classifies endpoint positivity by CTMC state dimension. The two-state unconditional cancellation is substantially stronger than the class-wide SSP guarantee, and the explicit three-state pure-birth family proves that three states are the first dimension where endpoint failure can occur. The nearby Resultary eight-state Padé barrier concerns a different rational map.

## value

PASS

The result isolates a sharp low-dimensional exception hidden by class-wide SSP theory: two-state Markov dynamics are endpoint-immune at arbitrary steps, while one extra state is enough to realize the global radius sharply. This is a meaningful minimal-dimension boundary for positivity-preserving time integration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
