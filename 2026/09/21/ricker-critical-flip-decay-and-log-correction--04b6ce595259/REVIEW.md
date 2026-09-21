# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The global part is separated from the asymptotic part. Positivity and the unimodal maximum put each positive orbit into a compact forward-invariant interval. At r=2, the equation f^2(x)=x reduces to x+f(x)=2. The derivative analysis of q(x)=x+f(x)-2 gives a unique root x=1, so Coppel's theorem yields convergence of every positive orbit to the unique positive fixed point.

For the rate, the shifted one-step map has multiplier -1, while its second iterate has expansion
\[
G(u)=u-\frac43u^3+\frac{8}{15}u^5+\frac49u^6+O(u^7).
\]
The reciprocal-square increment is
\[
G(u)^{-2}-u^{-2}=\frac83+\frac{64}{15}u^2-\frac89u^3+O(u^4).
\]
On either parity subsequence this yields W_{m+1}-W_m=8/3+(64/15)W_m^{-1}+O(W_m^{-3/2}). The first-order growth W_m~(8/3)m makes the remainder summable after subtracting the harmonic term and gives the exact logarithmic coefficient 8/5. The one-step reciprocal-square jump tends to 4/3, which stitches the two parity constants into one constant in the original time index. The symbolic verification artifact independently checks all coefficients used in this argument.

The exceptional-set statement was stress-tested separately: an orbit fails to admit reciprocal-square asymptotics exactly when it lands on u=0 in finite time. Since each backward level of the unimodal map is finite, the union of all such levels is countable. No numerical evidence is used as a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** Ricker (1954) introduced the stock-recruitment relation. May (1975) was inspected at the relevant theorem/calculation level: it gives the strict globally stable regime 0<r<2, identifies r=2 as the boundary at which the period-two branch is born for r>2, and develops the second-iterate equation for the two-cycle. It does not state the critical r=2 algebraic relaxation law or a logarithmic correction.

Luís--Rodrigues (2017) explicitly states global convergence for the scalar Ricker equation for 0<r<=2 via Coppel's theorem and recalls standard local criteria for nonhyperbolic multiplier -1 fixed points. Baigent et al. (2023) and Naderi Yeganeh--Baigent (2026) use the scalar r=2 threshold as background for planar Ricker global-stability work. The checked material establishes the threshold and endpoint attraction but does not give the formula 1/(x_n-1)^2=(4/3)n+(8/5)log n+C+o(1).

Targeted checks using synonymous formulations such as critical Ricker convergence, nonhyperbolic multiplier -1, slow convergence, algebraic convergence, and period-doubling threshold did not locate the displayed asymptotic or its explicit constants. Generic parabolic/neutral fixed-point iteration theory can account for the mechanism after passing to the second iterate, so this record does not claim a new general theorem in local iteration theory. The originality claim is restricted to the Ricker-specific global statement with universal leading coefficient, explicit next-order logarithmic correction, and complete finite-hit exceptional-set classification.

Residual priority risk remains from older model-specific sources. Goh (1977), Fisher--Goh--Vincent (1979), and Greenwell--Ng (1984) are especially relevant to scalar Ricker stability; bibliographic information and accessible descriptions indicate stability criteria as their focus, but complete theorem-level inspection was not available for all of them. They are therefore the most plausible sources that could reduce the priority claim.

## Value

**PASS.** At a flip threshold the linear multiplier alone gives no decay rate. The result turns the qualitative statement “the r=2 equilibrium is still globally attracting” into a sharp all-basin critical law. Both universal coefficients are explicit: the leading population error is sqrt(3)/(2 sqrt(n)), and the first secular correction is encoded by +(8/5) log n in reciprocal square. This quantitatively explains the exceptionally slow convergence observed at the bifurcation boundary and separates it cleanly from the finite-hit exceptional histories.

The logarithmic correction raises the result beyond the routine observation that a cubic parabolic second iterate produces n^{-1/2} decay: it identifies the next non-summable term and proves that the same renormalized constant exists across both alternating parity classes.

## Scientific limitations

The theorem is exact only for the scalar deterministic map at r=2. It does not establish uniform asymptotics as r approaches 2 from either side, nor does it cover stochastic, delayed, harvested, spatial, or multispecies variants. The mechanism is a standard neutral-iteration mechanism once the model-specific second iterate is expanded, so no broad methodological priority is asserted. The literature search is necessarily incomplete, and the older stability papers listed above leave residual priority uncertainty.
