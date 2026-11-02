# Scientific review of the three-oscillator critical period law

## Correctness — PASS

The original phase equations reduce exactly to \(\dot x=H_y,\ \dot y=-H_x\), with \(H=\sin x+\sin y-\sin(x+y)\). Direct trigonometric factorization separates two open energy triangles. For each positive regular energy the two explicit branches join to form precisely one simple closed curve; the negative one is its time-reversed counterpart. Both branches are counted in the period integral. The endpoint turning scales are \(x_-(E)\sim E/2\) and \(2\pi-x_+(E)\sim 2E^{1/3}\). Splitting the quadrature into its left boundary, regular interior, and right boundary gives two convergent beta integrals. Their sum is \(2B(1/3,1/2)\). At the other endpoint, the positive center has Hessian determinant \(9/4\), giving period \(4\pi/3\). The supplied program reproduces beta identities and desingularized quadratures at five energy values. The asymptotic result is proved analytically; a finite numerical sequence cannot establish a limit.

## Originality — PASS under inspected literature

The nearest-neighbor model, its conservative limit and its Hamiltonian are already explicitly present in Yan–Ozawa–Kori–Sato, arXiv:2603.02135 (the six-page revised primary PDF and its end matter were examined). Ashwin–Bick–Burylko, 2016, already describe integrability and periodic islands for three identical oscillators with even phase coupling (the relevant full-text theory and \(N=3\) sections were examined). Therefore the integrability or the existence of cycles is **not** claimed as new. Neither inspected work gives the exact three-site energy-period integral with its two unequal turning scales, beta-function separatrix coefficient, and center endpoint. Other published period-function work inspected concerns separable Hamiltonians or a nondegenerate center. Published-record searches for the Hamiltonian, ring, exact period, cubic separatrix and beta prefactor found no result implying the full quantitative statement, but search alone is not priority proof.

The closest earlier finding about an identical sinusoidal four-site ring concerns two first integrals in a different dimension and non-quadrature phase lag; it does not imply this specific physical-time asymptotic. Published work on a discrete oscillator triangle concerns iterated dynamics rather than this continuous Hamiltonian flow. A specialized earlier derivation with different notation remains a plausible residual originality risk.

## Mathematical value — PASS

The explicit slowdown at a degenerate homoclinic boundary addresses time-resolved dynamics at the conservative endpoint of a current oscillator-network model. Both the exponent and normalization matter: a generic hyperbolic separatrix would have logarithmic slowing, whereas this exact ring exhibits \(|E|^{-1/3}\) slowing, and its leading constant receives unequal contributions from the two coordinate ends. The fixed model's precise period law can serve as a benchmark for interpreting conservative critical slowing or numerical phase-ring simulations. This is a natural, complete quantitative invariant of the smallest nontrivial phase ring, rather than an arbitrarily chosen parameter slice or mere restatement of integrability.

## Limits and closest literature

The result is restricted to the exact three-site quadrature model, reduced modulo common phase rotation, and does not establish claims for more sites, off-quadrature dissipation, noisy systems, or intermediate-energy period monotonicity. Prior Hamiltonian structure and the existence of periodic islands are acknowledged. No independent scientific assessment has been made. Relevant sources: arXiv:2603.02135v1/v2; DOI 10.3389/fams.2016.00007; DOI 10.1007/s12346-026-01595-w.

Self-review: passed. Independent audit: not yet performed.
