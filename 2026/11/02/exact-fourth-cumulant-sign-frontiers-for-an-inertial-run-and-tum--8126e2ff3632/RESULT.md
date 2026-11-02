# Exact fourth-cumulant sign frontiers for an inertial run-and-tumble oscillator

## Finding
For a telegraph-driven damped oscillator, both the stationary position and velocity fourth cumulants have exact rational expressions. The velocity fourth cumulant changes sign precisely once as the positive trap stiffness grows, for every persistence parameter. The position fourth cumulant changes sign precisely once only above a sharp persistence-rate threshold; below that threshold it remains strictly negative at all positive stiffnesses.

Specifically, define
\[
\begin{aligned}
P_x(k,u)&=(12-9u)k^2+(33+119u+112u^2+26u^3)k\\
&\quad+18+69u+102u^2+72u^3+24u^4+3u^5,\\
P_v(k,u)&=-9k^3+(-18+16u+26u^2)k^2\\
&\quad+(6u+10u^2+4u^3+3u^4)k\\
&\quad+6u^2+9u^3+3u^4,\\
H(k,u)&=(3+4k)(k+u+u^2)^2(3u+9k+u^2)\\
&\quad\times(2+3u+k+u^2).
\end{aligned}
\]
All factors of \(H\) are strictly positive for positive arguments. The stationary centered fourth cumulants are
\[
\boxed{K_x=-\frac{6P_x(k,u)}{kH(k,u)},\qquad K_v=-\frac{6uP_v(k,u)}{H(k,u)}.}
\]
At fixed \(u>0\), there is exactly one positive root \(k_v(u)\) of \(P_v\), with \(K_v<0\) below it and \(K_v>0\) above it. For \(0<u\le4/3\), \(K_x<0\) for every \(k>0\). For \(u>4/3\), there is exactly one positive root \(k_x(u)\) of \(P_x\), with \(K_x<0\) below it and \(K_x>0\) above it. Equality of the fourth cumulant to zero occurs only at the respective roots. The derivatives of the defining normalized polynomials at those roots are strictly negative, so each crossing is simple.

The limiting standardized excess kurtoses are
\[
\lim_{k\to\infty}\frac{K_x}{(\mathbb E x^2)^2}=\frac{3u-4}{2(1+u)^2},\qquad
\lim_{k\to\infty}\frac{K_v}{(\mathbb E v^2)^2}=\frac3{2u}.
\]
At \(u=2\), the unique positive velocity and position roots are approximately \(14.2215212974\) and \(156.2282406743\), respectively. These are separate population fourth-cumulant crossovers; vanishing kurtosis does not imply a Gaussian law.

## Assumptions and scope
Take \(k>0\), \(u>0\) and the unique stationary solution of
\[
\dot x=v,\quad\dot v=-v-kx+\sigma_t,\quad\sigma_t\in\{-1,+1\},
\]
where the symmetric telegraph drive switches sign independently at rate \(u/2\). In physical units, for \(m\ddot X+\gamma\dot X+\mu X=a_0\sigma_t\) with \(m,\gamma,\mu,a_0>0\) and switching rate \(\lambda>0\), choose the time scale \(m/\gamma\), \(k=m\mu/\gamma^2\), \(u=2m\lambda/\gamma\), the position unit \(ma_0/\gamma^2\), and the velocity unit \(a_0/\gamma\). The sign of standardized fourth cumulants is invariant under these positive rescalings. Both position and velocity are bounded stationary linear functionals of a bounded telegraph drive because the deterministic oscillator is exponentially stable, so stationary moments of every finite order exist. This is an athermal one-dimensional model; no independent Brownian forcing is included.

## Proof
Write \(M_{ij}=\mathbb E[x^iv^j]\) and \(L_{ij}=\mathbb E[x^iv^j\sigma]\) for nonnegative integers \(i,j\). The stationary generator acting on \(x^iv^j\) and \(x^iv^j\sigma\) yields
\[
\begin{aligned}
0&=iM_{i-1,j+1}-jM_{ij}-kjM_{i+1,j-1}+jL_{i,j-1},\\
0&=iL_{i-1,j+1}-(j+u)L_{ij}-kjL_{i+1,j-1}+jM_{i,j-1}.
\end{aligned}
\]
Terms with a negative index have zero coefficient and are omitted. The stationary law is invariant under \((x,v,\sigma)\mapsto(-x,-v,-\sigma)\), which forces odd-total-degree \(M\) and even-total-degree \(L\) to vanish. Beginning from \(M_{00}=1\), solve successively the \(L\) equations at total degree one, the \(M\) equations at degree two, the \(L\) equations at degree three and the \(M\) equations at degree four. The degree-two results are
\[
M_{20}=\frac{1+u}{k(k+u+u^2)},\qquad M_{02}=\frac{u}{k+u+u^2}.
\]
The degree-four solutions, after subtracting three squares of these variances and reducing to common denominators, yield exactly \(K_x=-6P_x/(kH)\) and \(K_v=-6uP_v/H\). These identities are reconstructed from the generator, not posited from sampling. The enclosed standalone symbolic program derives all moment equations and verifies their exact identities from these definitions.

For \(P_v\), denote its strictly positive coefficients of \(k\) and its constant term by \(B_v(u)\) and \(C_v(u)\). Then
\[
\frac{d}{dk}\left(\frac{P_v}{k^2}\right)
=-9-\frac{B_v(u)}{k^2}-\frac{2C_v(u)}{k^3}<0.
\]
Moreover, \(P_v/k^2\) tends to \(+\infty\) at zero and \(-\infty\) at infinity, proving exactly one simple root and the asserted sign change.

For \(P_x\), its linear and constant coefficients \(B_x(u)\), \(C_x(u)\) are strictly positive. If \(u\le4/3\), its quadratic coefficient is nonnegative, so \(P_x>0\) for all positive \(k\). If \(u>4/3\),
\[
\frac{d}{dk}\left(\frac{P_x}{k}\right)=(12-9u)-\frac{C_x(u)}{k^2}<0,
\]
and the normalized polynomial runs strictly from \(+\infty\) at zero to \(-\infty\) at infinity. This proves the unique simple root and all sign claims. The exact variance formulas above and the leading coefficients of \(P_x,P_v,H\) give the two large-stiffness standardized limits. A similar direct limit gives \(\lim_{k\downarrow0}K_v/(M_{02})^2=-6/(u+3)\). No continuity argument substitutes for the strict polynomial proof.

## Verification
Run `python verify.py` with SymPy installed. The program independently solves the exact stationary monomial-generator systems through total degree four, checks the two variances and fourth-cumulant rational identities symbolically, checks the normalized-polynomial derivative formulas and all three stated standardized limits, and compares 32 further rational-parameter evaluations. All these assertions passed when run on the embedded source. Symbolic algebra verifies polynomial identities; the uniqueness statements follow from the analytic derivative/limit arguments above, not from any finite grid.

## Relationship to prior work
Dutta, Kundu, Sabhapandit and Basu (2024) establish the same inertial telegraph-driven trap and its recursive stationary moments (Sec. III), calculate its second-order stationary moments and investigate qualitative position/velocity distributions. Their numerical cumulant-based Fourier approximations use higher moments but do not state this global fourth-cumulant sign classification, the sharp \(u=4/3\) position threshold, or the one-root theorem for every positive turnover rate. The recurrence itself, second moments, and existence of complex distributional shape changes are **not** presented as new. Patel and Chaudhuri (2024) study fourth moments and kurtosis phase diagrams for inertial active *Brownian* particles in a harmonic trap with continuous-angle rotational noise and translational diffusion: the forcing's fourth-order law and model differ from the binary telegraph problem. The 1993 colored-noise oscillator study emphasizes covariance and spectra, which cannot determine non-Gaussian fourth cumulants by themselves. Existing spectral identifiability results for this same telegraph model concern covariance and support, not fourth-cumulant sign thresholds. The precise new assertion is the all-positive-parameter analytic root-count classification of the *telegraph* oscillator's two fourth cumulants. Priority against all possible related literature remains subject to independent scrutiny.

## Limitations
A negative fourth cumulant does not by itself prove a multimodal density, and a zero fourth cumulant does not imply Gaussianity; thus no modality diagram or thermodynamic phase transition is claimed. The classification assumes pure symmetric telegraph forcing and deterministic linear damping/confinement, without thermal noise, asymmetric tumbling, higher-dimensional orientations, or finite-sample inference. The symbolic checker supports but does not replace the analytical root-count proof. An older broad cumulant classification could imply the result without using identical terminology, which remains the principal originality risk. No independent external scientific audit has been performed.

## References
1. Debraj Dutta, Anupam Kundu, Sanjib Sabhapandit and Urna Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120v1 (first public 2024-06-10), Phys. Rev. E **110**, 044107 (2024). https://arxiv.org/abs/2406.06120
2. Manish Patel and Debasish Chaudhuri, *Exact moments for trapped active particles: inertial impact on steady-state properties and re-entrance*, arXiv:2404.01107v1 (2024-04-01). https://arxiv.org/abs/2404.01107
3. Manish Patel and Debasish Chaudhuri, *Exact moments and re-entrant transitions in the inertial dynamics of active Brownian particles*, arXiv:2310.00802v1 (2023-10-01). https://arxiv.org/abs/2310.00802
4. J. Masoliver and J. M. Porrà, *Harmonic oscillators driven by colored noise: Crossovers, resonances, and spectra*, Phys. Rev. E **48**, 4309 (1993), DOI:10.1103/PhysRevE.48.4309.
