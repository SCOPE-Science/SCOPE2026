# Independent mathematical audit

## correctness

PASS

For the original saturated-incidence vaccination SIR update, linearization at S0=Lambda/(mu+nu), I=0 gives I′=-c(1-R0)I, c=mu+gamma+delta, 0<R0<1; the exact continuous multiplier is q(h)=exp[-c(1-R0)h]. The source nonlocal infection step linearizes to lambda(phi)=(1+c R0 phi)/(1+c phi)=R0+(1-R0)/(1+c phi), strictly between R0 and 1 for every finite positive phi. Solving q=R0 gives h*=-log(R0)/(c(1-R0)); for every h>=h* q<=R0<lambda, a sharp obstruction within this architecture: for 0<h<h*, q lies strictly between R0 and 1 and the finite positive choice phi=(1-q)/[c(q-R0)] matches the continuous multiplier, establishing sharpness of the architectural threshold. The actual exponential denominator phi=(exp(mu*h)-1)/mu tends to infinity, so lambda->R0 and -log lambda/h->0, whereas exact physical-time decay rate remains c(1-R0). Verified independent exact symbolic algebra and the positive-parameter witness c=3,R0=1/2,h=log(2),phi=1,lambda=5/8,q=1/(2 sqrt(2)). This does not contradict stability or positivity. The source update and denominator were checked against the originating primary text, not inferred from verifier logs.

## originality

PASS

Best-of-knowledge source-specific quantitative decay-fidelity obstruction. Original Suryanto-Darti paper proves qualitative all-step dynamical consistency, not agreement of physical decay exponents. Published NSFD elementary-stability results address equilibrium type rather than exact multipliers. The rational hard floor and h* implication were not identified in relevant original material or independent searches; no priority guarantee.

## value

PASS

The hard lower bound on the discrete infection multiplier identifies when a scheme advertised as dynamically consistent for every step cannot reproduce its ODE’s physical extinction speed. The exact step threshold and asymptotic decay-rate collapse are operationally meaningful quantitative diagnostics, distinguishing stability-type preservation from rate fidelity on a natural infected mode. A short rational calculation is justified by this targeted numerical-analysis motivation rather than by novelty or reproducibility alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
