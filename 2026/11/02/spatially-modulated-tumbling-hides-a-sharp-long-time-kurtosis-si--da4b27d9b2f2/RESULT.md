# Spatially modulated tumbling hides a sharp long-time kurtosis sign transition

## Finding
Consider a one-dimensional run-and-tumble particle with unwrapped position \(X_t\in\mathbb R\), direction \(S_t\in\{-1,+1\}\), fixed speed \(v>0\), and velocity \(dX_t/dt=vS_t\). Reversal of \(S_t\) occurs at the position-dependent Poisson hazard \(\lambda(X_t)\), where \(\lambda\) is spatially periodic with period \(L>0\) and
\[
\lambda(x)=\begin{cases}a+b,&0\le x\bmod L<L/2,\\a-b,&L/2\le x\bmod L<L,\end{cases}\qquad a>|b|\ge0.
\]
For any deterministic initial phase and direction, the long-time second and fourth cumulants satisfy
\[
\boxed{\lim_{t\to\infty}\frac{\kappa_2(X_t)}{t}=\frac{v^2}{a},\qquad
\lim_{t\to\infty}\frac{\kappa_4(X_t)}{t}
=-\frac{3v^4}{a^3}+\frac{L^2b^2v^2}{4a^3}.}
\]
Consequently, the long-time diffusivity \(D_{\rm eff}=v^2/(2a)\) is **independent of the spatial contrast**, yet the long-time fourth-cumulant growth changes sign **exactly** when
\[
\boxed{L|b|=2\sqrt3\,v.}
\]
The long-time excess kurtosis approaches zero from above for \(L|b|>2\sqrt3\,v\), and from below for \(L|b|<2\sqrt3\,v\): more precisely,
\[
\lim_{t\to\infty}t\left(\frac{\mathbb E[(X_t-\mathbb EX_t)^4]}{\operatorname{Var}(X_t)^2}-3\right)=\frac{L^2b^2-12v^2}{4av^2}.
\]
At equality the coefficient of \(t^{-1}\) vanishes; no assertion is made about its next term. Strictly positive fourth-cumulant growth is feasible only when \(aL>2\sqrt3\,v\), because \(|b|<a\).

## Assumptions and scope
The state is a continuous-time piecewise-deterministic Markov process. The convention is that \(\lambda\) itself is the **direction-reversal rate**, not the rate of a tumble that only reverses with probability one-half. At the discontinuity points, any consistent definition of the hazard gives the same law. No spatial drift, rotational diffusion, additional Brownian noise, particle interaction, or resetting is assumed. The two zones have exactly equal physical lengths. Rates are strictly positive because \(a>|b|\). Cumulants refer to the **unwrapped**, not circle-valued, position. Their growth rates are independent of fixed initial conditions; finite-time cumulants need not equal their asymptotic linear approximations.

## Proof
1. Work with phase \(Y_t=X_t\bmod L\) and the two-state orientation. The tilted backward generator acting on \(L\)-periodic vector functions \(f_\pm(y)\) is
\[
(\mathcal L_k f)_s=sv(\partial_y+k)f_s+\lambda(y)(f_{-s}-f_s).
\]
Because both reversal rates have a positive lower bound, the phase-direction process is irreducible and has a Doeblin minorization at a sufficiently long time (a finite sequence of reversals can reach any subinterval with a positive density). Its leading tilted eigenvalue \(\psi(k)\) is simple and analytic near real \(k=0\), and the cumulant growth rates equal \(\psi^{(r)}(0)\). Equivalently, \(\lim_{t\to\infty}t^{-1}\log\mathbb E e^{k(X_t-X_0)}=\psi(k)\) for sufficiently small real \(k\). We use only this local analyticity.

2. The eigenvalue equation \(\mathcal L_kf=\theta f\) has the first-order transfer form
\[
\partial_y\binom{f_+}{f_-}=(-kI+B_{\lambda(y)}(\theta))\binom{f_+}{f_-},\quad
B_r(\theta)=v^{-1}\begin{pmatrix}\theta+r&-r\\r&-\theta-r\end{pmatrix}.
\]
The matrices \(B_r\) are traceless, and \(B_r^2=\theta(\theta+2r)I/v^2\). Across the two half-periods the monodromy, after factoring out \(e^{-kL}\), is
\[
N(\theta)=e^{(L/2)B_{a-b}(\theta)}e^{(L/2)B_{a+b}(\theta)},\qquad\det N(\theta)=1.
\]
A periodic eigenvector exists exactly when \(e^{kL}\) is an eigenvalue of \(N(\theta)\). Thus the principal branch is determined near the origin by
\[
F(\theta):=\tfrac12\operatorname{tr}N(\theta)=\cosh(kL),\qquad \theta=\psi(k).
\]

3. Put \(q_\pm=\sqrt{\theta(\theta+2(a\pm b))}/v\) and \(h=L/2\). The matrix exponential identity gives the **exact**, locally analytic scalar relation
\[
F(\theta)=\cosh(hq_+)\cosh(hq_-)
+\frac{\theta(\theta+2a)}{v^2}
\frac{\sinh(hq_+)}{q_+}\frac{\sinh(hq_-)}{q_-}.
\]
The right side is interpreted continuously at \(q_\pm=0\); its power series is analytic in \(\theta\). Expanding the two hyperbolic factors yields
\[
F(\theta)=1+\frac{L^2a}{v^2}\theta
+\frac{L^2(4L^2a^2-L^2b^2+12v^2)}{24v^4}\theta^2+O(\theta^3).
\]
Since \(F'(0)=L^2a/v^2>0\), the analytic implicit-function theorem applies. Comparison with \(\cosh(kL)=1+L^2k^2/2+L^4k^4/24+O(k^6)\) gives
\[
\psi(k)=\frac{v^2}{2a}k^2
+\left(-\frac{v^4}{8a^3}+\frac{L^2b^2v^2}{96a^3}\right)k^4+O(k^6).
\]
The local branch is even in \(k\). Taking the second and fourth derivatives gives the stated cumulant rates. Division of the fourth rate by the square of the variance rate proves the excess-kurtosis limit. The sign comparison is exact because \(a,v>0\); it is attainable inside the admissible parameter set exactly when \(aL>2\sqrt3v\). This completes the proof.

## Verification
The file `verify_monodromy.py` independently evaluates the finite-length transfer-matrix relation at high decimal precision and solves for its leading eigenvalue by monotone bisection. It compares finite-\(k\) fourth-order estimates against the displayed exact coefficient, with six choices of the zone strengths, length and velocity and three perturbation sizes per choice, plus exact sign checks. It uses only Python's standard library and reports 24 passed checks. These computations test the formula in selected parameter cases; **the proof for all \(a>|b|\ge0\), \(L,v>0\) is the analytic transfer expansion above**. To reproduce, run `python verify_monodromy.py` in the directory containing this file.

## Relationship to prior work
Tailleur and Cates, *Statistical Mechanics of Interacting Run-and-Tumble Bacteria* (first preprint 2008-03-07; Phys. Rev. Lett. 100, 218103, 2008; arXiv:0803.1069), treat one-dimensional position-dependent run speeds and tumbling rates, identifying the steady density and approximate drift-diffusion laws. Their equations (1)–(9) do not give the two-zone exact tilted monodromy, fourth cumulant, or its sign transition. The present theorem is about a noninteracting constant-speed particle with **periodic spatial reversal intensity** and the next-to-Gaussian correction, not the collective phase separation they analyze.

Singh, Sabhapandit and Kundu, *Run-and-Tumble particle in inhomogeneous media in one dimension* (arXiv:2004.11041, 2020), analyze power-law and direction-asymmetric reversal profiles on unbounded and bounded geometries, with occupation, survival and exit statistics. Its explicitly studied profiles and observables differ from the positive two-zone periodic model and its long-time fourth-cumulant sign. Angelani and Garra, *Run-and-tumble motion in one dimension with space-dependent speed* (Phys. Rev. E 100, 052147, 2019), is also relevant: only its abstract and bibliographic description were accessible, not its full equations, so possible overlap is a stated priority risk. The earlier treatment of spatially periodic **time** modulation of reversal hazards concerns a different generator and does not imply the spatial two-zone fourth-cumulant law.

## Limitations
The result is not an independence or publication certification. Full-text comparison against Angelani–Garra (2019) could not be completed. Broader historical literature may contain an equivalent transfer-matrix formulation. The theorem is limited to equal-width repeating regions, equal speeds in both directions and strictly positive reversal rates. It does not prove a full finite-time kurtosis sign, a finite-time central limit error bound, or a rate of convergence of higher cumulants. The zero at the critical curve refers only to the leading fourth-cumulant growth rate.

## References
1. J. Tailleur and M. E. Cates, *Statistical Mechanics of Interacting Run-and-Tumble Bacteria*, arXiv:0803.1069 (first submitted 2008-03-07), Phys. Rev. Lett. 100, 218103 (2008). https://arxiv.org/abs/0803.1069; https://doi.org/10.1103/PhysRevLett.100.218103.
2. P. Singh, S. Sabhapandit and A. Kundu, *Run-and-Tumble particle in inhomogeneous media in one dimension*, arXiv:2004.11041 (2020). https://arxiv.org/abs/2004.11041.
3. L. Angelani and R. Garra, *Run-and-tumble motion in one dimension with space-dependent speed*, Phys. Rev. E 100, 052147 (2019). https://doi.org/10.1103/PhysRevE.100.052147.
