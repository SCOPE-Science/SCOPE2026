# Sharp potential–kinetic energy covariance boundary for an inertial run-and-tumble oscillator

## Finding
For the stationary harmonically confined inertial run-and-tumble oscillator defined below, the connected covariance of potential and kinetic energies changes sign on exactly one parameter curve. Put \(g=\gamma/\sqrt{m\mu}\) and \(u=\rho\sqrt{m/\mu}\), with all mechanical and flipping parameters strictly positive. For
\[
\begin{aligned}
P(g,u)={}&48u^4+192gu^3+(288g^2+104)u^2\\
&+(138g^3+136g)u+(6g^2-1)(3g^2+9),
\end{aligned}
\]
the exact sign of \(\operatorname{Cov}(U,K)\) is the **opposite** of the sign of \(P(g,u)\). If \(g\geq1/\sqrt6\), the covariance is strictly negative for every \(u>0\). If \(0<g<1/\sqrt6\), it is strictly positive for \(0<u<u_c(g)\), exactly zero at \(u=u_c(g)\), and strictly negative for \(u>u_c(g)\), where \(u_c(g)>0\) is the unique positive zero of \(P(g,\cdot)\). The curve \(u_c\) is strictly decreasing, with limits \(u_c(0+)=1/(2\sqrt3)\) and \(u_c((1/\sqrt6)-)=0\).

This gives a sharp, parameter-independent damping threshold for the existence of positive stationary potential–kinetic energy correlations under dichotomous active forcing.

## Assumptions and scope
Let \(m,\mu,\gamma,a_0,\rho>0\). Consider the piecewise-deterministic stochastic system
\[
\dot X=V,\qquad m\dot V=-\mu X-\gamma V+a_0\sigma_t,
\]
where \(\sigma_t\in\{-1,+1\}\) is a symmetric continuous-time Markov chain with independent exponential sign-change waiting times of rate \(\rho\). There is no additive thermal diffusion. The unique stationary distribution of \((X,V,\sigma)\) is used throughout. Define \(U=\mu X^2/2\), \(K=mV^2/2\). All formulas are exact for finite, strictly positive parameters, not only for overdamped/underdamped asymptotic approximations.

Use dimensionless time \(s=t\sqrt{\mu/m}\), position \(x=\mu X/a_0\), and velocity \(v=\mu V/(a_0\sqrt{\mu/m})\). The dynamics become \(dx/ds=v\), \(dv/ds=-x-gv+\sigma\), with telegraph flip rate \(u\). Since the deterministic matrix has strictly negative real-part eigenvalues for every \(g>0\), convolution against the bounded stationary telegraph process defines a unique bounded stationary solution, so every moment in the proof is finite.

Introduce positive denominators
\[
B=1+2gu+4u^2,\quad C=9+6gu+4u^2,\quad E=1+2g^2+6gu+4u^2,\quad A=3g^2+4.
\]
The complete exact covariance is
\[
\boxed{\operatorname{Cov}(U,K)
=-\frac{a_0^4}{\mu^2}\,\frac{uP(g,u)}{gA B^2CE}.}
\]

## Proof
**Step 1: stationary moment hierarchy.** For nonnegative integers \(i,j\), write \(M_{ij}=\mathbb E[x^iv^j]\), \(S_{ij}=\mathbb E[x^iv^j\sigma]\). The generator of the piecewise-deterministic Markov process, acting on polynomial test functions, gives the exact stationary identities
\[
\begin{aligned}
0={}&iM_{i-1,j+1}-jM_{i+1,j-1}-jgM_{ij}+jS_{i,j-1},\\
0={}&iS_{i-1,j+1}-jS_{i+1,j-1}-(jg+2u)S_{ij}+jM_{i,j-1}.
\end{aligned}
\]
Terms multiplied by zero are omitted. Normalization and symmetry give \(M_{00}=1\), \(S_{00}=0\). The system is triangular by total polynomial degree: the degree-\(d\) equations are a finite linear system whose right side uses only moments of degree \(d-1\). In particular, \(M_{11}=0\),
\[
M_{20}=\frac{g+2u}{gB},\qquad M_{02}=\frac{2u}{gB}.
\]

**Step 2: the genuinely mixed fourth moment.** Solving the degree-three telegraph-weighted equations and then the degree-four unweighted equations gives
\[
M_{22}=\frac{2uQ(g,u)}{g^2 A B C E},
\]
where
\[
\begin{aligned}
Q(g,u)={}&18g^5+66g^4u+72g^3u^2-3g^3+24g^2u^3\\
&+58g^2u+72gu^2+54g+32u^3+72u.
\end{aligned}
\]
Subtraction of \(M_{20}M_{02}\) and exact polynomial simplification yield
\[
M_{22}-M_{20}M_{02}=-\frac{4uP(g,u)}{g A B^2 C E}.
\]
The stationary moment equations and this factorization are reproduced symbolically by the accompanying `CHECK.py`, which independently solves the entire hierarchy through degree four. The physical-energy conversion is \(U=(a_0^2/(2\mu))x^2\), \(K=(a_0^2/(2\mu))v^2\), proving the boxed covariance.

**Step 3: a complete sign classification.** Every factor outside \(-P\) in the boxed expression is strictly positive. The constant coefficient of \(P\) as a polynomial in \(u\) is \((6g^2-1)(3g^2+9)\); every positive-degree coefficient is positive for \(g>0\). Therefore \(P(g,\cdot)\) increases strictly on \([0,\infty)\) and tends to positive infinity. If \(g\geq1/\sqrt6\) then \(P(g,u)>0\) for every \(u>0\). If \(g<1/\sqrt6\), its value at zero is negative, hence it has exactly one simple positive root \(u_c(g)\). Furthermore, all nonconstant coefficients of \(P(g,u)\) are nondecreasing functions of \(g\), and the constant coefficient is strictly increasing for \(g>0\). Thus \(\partial_gP>0\) for \(g,u>0\); implicit differentiation yields \(u_c'(g)=-\partial_gP/\partial_uP<0\).

At \(g=0\), \(P(0,u)=(12u^2-1)(4u^2+9)\), so the unique positive limiting root is \(1/(2\sqrt3)\). The constant term vanishes at \(g=1/\sqrt6\) and all positive-power coefficients remain strictly positive, proving the second limiting value zero. This completes all parameter cases.

## Verification
The standalone `CHECK.py` performs exact symbolic reconstruction of the stationary moments to degree four, verifies the covariance factorization and endpoint identities, and checks positivity of the polynomial derivative coefficients. It separately computes stationary \(\mathbb E[x^2v^2]\) for four distinct damping/tumbling regimes by integrating the **four-time correlation function** of stationary symmetric telegraph forcing against linear oscillator response kernels. These integrals do not use the stationary moment hierarchy, providing independent computational corroboration. The four parameter pairs are \((g,u)=(0.2,0.1),(0.2,0.3),(1,0.1),(3,0.02)\), spanning both covariance signs and underdamped/overdamped motion. Running `python CHECK.py` passes 25 assertions (exact algebraic and independent-integral checks). Finite tests corroborate the algebra; the strict, global sign theorem follows from the proved positive-coefficient structure, not sampled parameters.

## Relationship to prior work
Dutta, Kundu, Sabhapandit and Basu (2024) establish this inertial one-dimensional run-and-tumble harmonic-trap model, give its stationary moment recursion, and calculate explicit second moments and marginal fluctuation regimes. Those known methods and second moments are antecedents, not claimed here. The present result isolates a different joint observable—the connected covariance between squared position and squared velocity—and establishes an explicit rational formula together with a **complete sharp, monotone sign-boundary classification**. A general moment recursion makes the mixed fourth moment calculable, but does not itself state or classify the sign of the resulting connected quantity. Patel and Chaudhuri (2024) analyze inertial active Brownian particles with orientational diffusion, a different forcing law. Frydel (2023) develops moment recursions for active Brownian harmonic oscillators, primarily in overdamped dynamics; again the telegraph inertial energy-covariance sign diagram is not reported in its examined sections.

## Limitations
This theorem concerns one-dimensional linear harmonic confinement, a stationary symmetric two-state drive, zero independent thermal noise, and strictly positive damping and switching rates. The endpoints \(g=0\), \(u=0\), and infinite switching are limiting parameter values, not included in the stationary theorem. Adding independent Gaussian forcing, correlated switching, nonlinear trapping, or asymmetric drive requires separate analysis. The positivity region is necessarily well inside the underdamped mechanical regime, because \(g<1/\sqrt6<2\). The present scientific novelty assessment is self-review only; independent scholarly priority assessment has not been performed. The source's general moment recursions might be interpreted as algorithmically including some intermediate algebra, which remains a specific priority risk.

## References
1. Debraj Dutta, Anupam Kundu, Sanjib Sabhapandit and Urna Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120 (first public version 2024-06-10), especially Sec. III and Appendices A–D. https://arxiv.org/abs/2406.06120
2. Manish Patel and Debasish Chaudhuri, *Exact moments for trapped active particles: inertial impact on steady-state properties and re-entrance*, arXiv:2404.01107 (2024). https://arxiv.org/abs/2404.01107
3. Derek Frydel, *Active oscillator: recurrence relation approach*, arXiv:2312.05406 (2023). https://arxiv.org/abs/2312.05406
