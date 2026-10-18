# Factorial stationary tails for a Stark-localized quantum walk with Poisson resets

## Finding
For a coherently hopping particle on the integer lattice subject to a constant nonzero electric field and independent Poisson resets to its origin, the unique stationary position law has **factorial**, rather than merely exponential, tails. Precisely, for every real \(h\neq0\), \(F\neq0\), and \(r>0\), and every integer \(n\ge0\), the stationary site probabilities are even and satisfy
\[
p_n=r\int_0^\infty e^{-rt}J_n\!\left(\frac{4h}{F}\sin\frac{Ft}{2}\right)^2dt,
\qquad
p_n\sim\frac{r\sqrt\pi}{|F|\sinh(\pi r/|F|)}\frac{(2|h|/|F|)^{2n}}{\sqrt n\,(n!)^2}
\quad(n\to\infty).
\]
Here \(J_n\) is the ordinary Bessel function. The explicit prefactor is positive and finite for each fixed admissible parameter triple.

## Assumptions and scope
The Hilbert space is \(\ell^2(\mathbb Z)\), with canonical orthonormal vectors \(|j\rangle\). Write \(S|j\rangle=|j+1\rangle\) and \(X|j\rangle=j|j\rangle\); set \(H=-h(S+S^*)+FX\), selfadjoint on the domain of \(X\). Between reset events the density matrix evolves by \(U(t)=e^{-itH}\). At independent exponentially distributed waiting times of rate \(r\), the whole state is replaced by \(|0\rangle\langle0|\), irrespective of its prior value. The claim concerns the unconditional stationary position measurement probabilities, not pathwise trajectories or convergence of a single pure state. Parameters \(h,F\) are real and nonzero, \(r>0\), and the limit is at fixed parameters as \(n\to\infty\). Units have \(\hbar=1\), lattice spacing one.

## Proof
**Stationary state.** The reset generator on trace-class density matrices is
\[\mathcal L(\rho)=-i[H,\rho]+r\bigl(|0\rangle\langle0|\operatorname{Tr}\rho-\rho\bigr).\]
The renewal expression
\[\rho_\infty=r\int_0^\infty e^{-rt}U(t)|0\rangle\langle0|U(t)^*\,dt\]
is positive and trace one. Subtracting solutions with equal trace eliminates the rank-one reset term; their trace distance contracts exactly by the factor \(e^{-rt}\) under unitary conjugation. Thus this is the unique stationary normal state, and every initial normal state converges to it.

**Coherent propagator.** Fourier transformation and the accelerated momentum variable give, for each \(n\in\mathbb Z\),
\[|\langle n|U(t)|0\rangle|^2=J_{|n|}\!\left(\frac{4h}{F}\sin\frac{Ft}{2}\right)^2.\]
For example this follows by multiplying the Fourier wave function by the field-driven momentum shift and applying the generating identity \(e^{iz\cos k}=\sum_{j\in\mathbb Z}i^jJ_j(z)e^{ijk}\). Taking diagonal matrix elements of the renewal expression yields the exact integral asserted in Finding and establishes \(p_{-n}=p_n\).

**Uniform fixed-argument Bessel estimate.** Set \(f=|F|>0\) and \(A=4|h|/f\). For each fixed \(A>0\), the absolutely convergent Bessel power series implies, uniformly for real \(|z|\le A\),
\[J_n(z)^2=\frac{(z/2)^{2n}}{(n!)^2}\bigl(1+O_A(n^{-1})\bigr),\]
with the expression interpreted as zero on both sides when \(z=0\). Indeed the ratio of the tail of the series after its leading term to that term is bounded by \(\sum_{k\ge1}(A^2/4)^k/[k!(n+1)^k]=O_A(n^{-1})\). The bound is uniform in the integration variable and can be integrated against the positive exponential weight. Consequently,
\[p_n=\frac{(2|h|/f)^{2n}}{(n!)^2}\,I_n(a)\bigl(1+O_{h,F}(n^{-1})\bigr),\quad a=r/f,\]
where \(I_n(a)=r\int_0^\infty e^{-rt}|\sin(ft/2)|^{2n}dt\).

**Exact integral product and sharp constant.** Periodicity reduces this last integral to one period. Put \(K_n(a)=\int_0^\pi e^{-2au}\sin^{2n}u\,du\). Then
\[I_n(a)=\frac{2r}{f(1-e^{-2\pi a})}K_n(a),\qquad K_0(a)=\frac{1-e^{-2\pi a}}{2a}.\]
For every integer \(n\ge1\), integrate the derivative of \(e^{-2au}\sin^{2n-1}u\cos u\) over \([0,\pi]\), and integrate \(e^{-2au}\sin^{2n-1}u\cos u\) by parts once. The vanishing boundary terms give
\[K_n(a)=\frac{n(2n-1)}{2(n^2+a^2)}K_{n-1}(a).\]
Thus \(I_0(a)=1\), and the **exact finite product** is
\[I_n(a)=\frac{\binom{2n}{n}}{4^n}\prod_{j=1}^{n}\left(1+\frac{a^2}{j^2}\right)^{-1}.\]
Stirling's formula gives \(\binom{2n}{n}/4^n=(\pi n)^{-1/2}(1+O(n^{-1}))\). Euler's product \(\sinh(\pi a)/(\pi a)=\prod_{j\ge1}(1+a^2/j^2)\) and the convergent tail bound \(\sum_{j>n}a^2/j^2=O_a(n^{-1})\) imply
\[I_n(a)=\frac{\sqrt\pi\,a}{\sinh(\pi a)\sqrt n}\bigl(1+O_a(n^{-1})\bigr).\]
Substitution completes the proof and gives the claimed strictly positive constant. No finite cutoff or numerical experiment is used to justify this all-\(n\) asymptotic.

## Verification
The accompanying `verify.py` constructs the finite-lattice Hamiltonian and compares its coherent transition probabilities to the Bessel law, then evaluates the exact one-period renewal integral at high precision and compares it with the factorial asymptotic. On three parameter triples and three increasing site indices, the ratios converge toward one. The exact product for \(I_n(a)\) is independently checked against numerical integration. Run `python verify.py` after installing packages listed in `requirements.txt`. These tests corroborate the analytical identities without certifying the infinite lattice or the limit by computation.

## Relationship to prior work
Evans and Majumdar (2011) introduced Poisson resetting for classical diffusion, establishing the renewal motivation. Rose and collaborators (2018) developed a general quantum resetting framework, whose stationary resolvent principle is background rather than the claimed contribution. Wald and Böttcher (2021) studied resetting quantum walks on graphs; their general sampling formulas do not give this nonzero static-field factorial tail. Dattagupta, Das, and Gupta (2022 preprint, 2023 version) studied quantum tight-binding reset dynamics driven by an *oscillating* field \(F_0\cos(\omega t)\); their exact finite-time and stationary formulas concern finite oscillation frequency and do not state the fixed nonzero *static* field's sharp factorial tail prefactor. Acharya and Gupta (2023) studied conditional reset sites and a periodic drive, not this fixed-origin, static-field asymptotic. The familiar unreset Wannier–Stark propagator and the reset renewal integral are not claimed as new; the assessed mathematical fact is the exact factorial asymptotic, including its nontrivial prefactor. Equivalence under singular zero-frequency limits of general driven formulas remains a priority risk, but such an implication alone does not supply the displayed uniform large-distance analysis.

## Limitations
No uniformity is asserted as the field \(F\to0\), the hopping \(h\to0\), or the reset rate \(r\to0\). The limit holds only at fixed nonzero field, rate, and hopping. This result does not address interacting particles, non-Poisson resetting, disordered hopping, off-diagonal stationary density matrix entries, or finite-time first detection. The relationship to all potentially relevant generic driven-system formulas should be independently verified before any claim of publication priority.

## References
- M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704, first posted 2011-02-14, DOI: 10.1103/PhysRevLett.106.160601.
- D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298, DOI: 10.1103/PhysRevE.98.022129.
- S. Wald and L. Böttcher, *From classical to quantum walks with stochastic resetting on networks*, DOI: 10.1103/PhysRevE.103.012122.
- S. Dattagupta, D. Das, and S. Gupta, *Stochastic resets in the context of a tight-binding chain driven by an oscillating field*, arXiv:2209.14117, DOI: 10.1088/1742-5468/ac98c0; preprint model, stated principal results, conclusions and appendix map inspected.
- A. Acharya and S. Gupta, *Tight-binding model subject to conditional resets at random times*, arXiv:2308.14040, DOI: 10.1103/PhysRevE.108.054125.
