# Shared Poisson resets produce an unbounded Rényi-two correlation signature in free quantum walks

## Finding

**Theorem (a shared-clock correlation anomaly).** Let two distinguishable, noninteracting continuous-time quantum walkers move on the infinite one-dimensional nearest-neighbor tight-binding lattice with identical hopping strength \(J>0\). Compare resetting each walker to the origin with its own independent Poisson clock, each of rate \(r>0\), against resetting both walkers simultaneously to the product-origin state with one shared Poisson clock of the same rate. In stationarity, the two protocols give *identical one-body density matrices*; the shared-clock two-body state is separable, but differs from the product state at every positive \(r,J\).

Writing \(\rho_1\) for their common one-body state and \(\rho_{\mathrm c}\) for the joint shared-clock state, their purities satisfy
\[
P_1:=\operatorname{tr}(\rho_1^2)=r\int_0^\infty e^{-rt}\mathrm J_0(2Jt)^2\,dt,
\qquad
P_{\mathrm c}:=\operatorname{tr}(\rho_{\mathrm c}^2)=r\int_0^\infty e^{-rt}\mathrm J_0(2Jt)^4\,dt,
\]
where \(\mathrm J_0\) denotes the order-zero Bessel function. For independent reset clocks the joint purity is \(P_{\mathrm i}=P_1^2\), and \(P_{\mathrm c}>P_{\mathrm i}\) strictly.

The positive **Rényi-two correlation contrast** (defined by the difference of collision entropies)
\[
\mathcal I_2(r):=2[-\log P_1]-[-\log P_{\mathrm c}]
=\log\!\left(\frac{P_{\mathrm c}}{P_1^2}\right)
\]
has the sharp weak-reset asymptotic
\[
\boxed{\ \mathcal I_2(r)=\log\!\left(\frac{2\pi^2 J C_4}{r\,[\log(16J/r)]^2}\right)+o(1),\qquad r\downarrow0,\ }
\]
where \(C_4=\int_0^\infty \mathrm J_0(u)^4\,du\in(0,\infty)\). In particular, \(\mathcal I_2(r)=\log(J/r)-2\log\log(J/r)+O(1)\to\infty\). The correlation contrast diverges although both walkers remain noninteracting and the stationary joint state is separable. This quantity is specifically an order-two entropy contrast; it is not being identified with Umegaki quantum mutual information or used as an entanglement witness.

## Assumptions and scope

Work with \(\hbar=1\) on the one-particle Hilbert space \(\ell^2(\mathbb Z)\). Let \(\{|n\rangle:n\in\mathbb Z\}\) be its canonical basis and define the bounded self-adjoint Hamiltonian
\[
H=-J\sum_{n\in\mathbb Z}\bigl(|n+1\rangle\langle n|+|n\rangle\langle n+1|\bigr),\quad J>0,
\quad U_t=e^{-itH},\quad |\psi_t\rangle=U_t|0\rangle.
\]
The two-particle free Hamiltonian is \(H\otimes I+I\otimes H\) on \(\ell^2(\mathbb Z)\otimes\ell^2(\mathbb Z)\). Both particles are distinguishable; no symmetrization or exchange interaction is imposed. At a resetting event the affected walker is replaced by the pure state \(|0\rangle\langle0|\), independently of its previous state, and otherwise evolves unitarily. In the common-clock protocol both are reset simultaneously to \(|0,0\rangle\langle0,0|\). Poisson events are state-independent with constant rate \(r>0\). All statements refer to unique stationary density operators and the \(r\downarrow0\) limit at *fixed* \(J>0\).

## Proof

**1. Exact stationary states and shared one-body marginals.** The elapsed time \(T\) since the last event of a stationary Poisson clock has density \(re^{-rt}\,dt\). The single-walker and joint stationary states therefore are the trace-norm integrals
\[
\rho_1=r\int_0^\infty e^{-rt}|\psi_t\rangle\langle\psi_t|\,dt,
\quad
\rho_{\mathrm c}=r\int_0^\infty e^{-rt}
\bigl(|\psi_t\rangle\langle\psi_t|\bigr)^{\otimes2}\,dt,
\quad
\rho_{\mathrm i}=\rho_1\otimes\rho_1.
\]
The integrands have trace norm one, so the integrals converge in trace class and have unit trace. If two initial trace-one states evolve under the same full reset protocol, the difference of their evolved states is the no-reset term, of trace norm at most \(2e^{-rt}\). Thus the stationary operators above are unique. Partial tracing \(\rho_{\mathrm c}\) over either walker gives \(\rho_1\). The common-clock state is a convex integral of pure product projectors and is therefore separable.

**2. Exact collision probabilities.** Fourier diagonalization of \(H\) gives the return amplitude
\[
\langle0|U_t|0\rangle=\frac1{2\pi}\int_{-\pi}^{\pi}e^{2iJt\cos k}\,dk=\mathrm J_0(2Jt).
\]
Consequently \(|\langle\psi_s|\psi_t\rangle|^2=\mathrm J_0(2J(t-s))^2\). For any bounded measurable even \(F\), direct division of the two positive-time integration quadrants yields
\[
r^2\int_0^\infty\!\int_0^\infty e^{-r(s+t)}F(t-s)\,ds\,dt
=r\int_0^\infty e^{-ru}F(u)\,du.
\]
Trace multiplication of the stationary rank-one projectors and the preceding identity with the second and fourth powers of \(\mathrm J_0\) respectively gives both asserted purities. Independently reset walkers have product stationary state and purity \(P_1^2\).

**3. Strict positivity without entanglement.** Put \(f(t)=\mathrm J_0(2Jt)^2\). For \(T\sim\operatorname{Exp}(r)\), \(P_1=\mathbb Ef(T)\) and \(P_{\mathrm c}=\mathbb Ef(T)^2\). As \(f\) is continuous, equals one at zero, and is not constant for \(J>0\), and the exponential distribution charges every positive open interval, \(\operatorname{Var}(f(T))>0\). Hence \(P_{\mathrm c}>P_1^2\), making \(\mathcal I_2(r)>0\) for every \(r,J>0\). This separates shared-clock classical mixing from quantum entanglement.

**4. Exact one-particle purity and its logarithmic critical scale.** Bessel's addition formula and the elementary Laplace transform yield
\[
\mathrm J_0(x)^2=\frac1\pi\int_0^\pi \mathrm J_0\bigl(2x\sin(\theta/2)\bigr)\,d\theta,
\qquad\int_0^\infty e^{-rt}\mathrm J_0(at)\,dt=(r^2+a^2)^{-1/2},
\]
so, with \(\mathbf K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta\),
\[
P_1(r)=\frac{2r}{\pi\sqrt{r^2+16J^2}}\,
\mathbf K\!\left(\frac{4J}{\sqrt{r^2+16J^2}}\right).
\]
Using the standard \(\mathbf K(k)=\log(4/\sqrt{1-k^2})+o(1)\) as \(k\uparrow1\) gives
\[
P_1(r)=\frac{r}{2\pi J}\bigl[\log(16J/r)+o(1)\bigr].
\]
In particular, only the leading term is needed for the subsequent logarithmic statement.

**5. Fourth-power integrability and the sharp contrast.** The classical large-argument bound \(|\mathrm J_0(u)|\le C(1+u)^{-1/2}\) implies \(0<C_4=\int_0^\infty\mathrm J_0(u)^4du<\infty\). Changing variables \(u=2Jt\) and applying dominated convergence,
\[
\frac{P_{\mathrm c}(r)}r=\frac1{2J}\int_0^\infty e^{-ru/(2J)}\mathrm J_0(u)^4du\longrightarrow\frac{C_4}{2J}.
\]
Combining with the one-body formula gives the full multiplicative asymptotic
\[
\frac{P_{\mathrm c}(r)}{P_1(r)^2}\sim\frac{2\pi^2 JC_4}{r[\log(16J/r)]^2}.
\]
Taking logarithms proves the stated \(o(1)\) remainder, strict positivity, and divergence. The proof requires no finite-lattice truncation, asymptotic fitting, or conjectured cancellation.

## Verification

The independent, executable `verify_coherent_reset.py` checks the Bessel addition identity, a direct truncated-position/age Gram-matrix reconstruction of one-body and shared two-body density-matrix purities, an independent double-age quadrature, and the finite-rate formula against the elliptic-integral expression. It also checks numerically the weak-reset asymptotic trend and the finite positive Bessel fourth-power integral. These finite computations provide consistency checks; the strict inequality and infinite-volume/weak-rate claims are proved analytically above. Requirements: Python 3 with NumPy and SciPy. Run `python3 verify_coherent_reset.py` from a directory containing that file.

## Relationship to prior work

Wald and Böttcher (arXiv:2008.00510, first public 2020-08-02) study continuous-time quantum walks under stochastic resetting on networks and give the renewal framework. Das, Dattagupta and Gupta (arXiv:2106.14181, first public 2021-06-27) derive quantum tight-binding resetting dynamics, Bessel-function site probabilities and stationary single-particle localization; their formula for the origin-site probability already implies the displayed single-body purity as a calculation, which **is not separately claimed as novel**. The claim assessed here is the *two-walker common-versus-independent reset comparison* with identical marginals, strict shared-clock collision contrast and its sharp divergent, logarithmically corrected Rényi-two signature. The screened full texts and mathematical-record searches did not establish a covering result for this joint assertion, but more general renewal/channel entropy results may supply an equivalent formulation. A negative search does not prove priority.

## Limitations

The result concerns two distinguishable noninteracting walkers, global product resetting and the infinite translation-invariant nearest-neighbor chain. It gives a Rényi-two collision-entropy contrast, not von Neumann mutual information or an entanglement measure. Finite-rate numerical tests do not establish infinite-dimensional identities. The asymptotic statement holds at fixed positive hopping amplitude as the reset rate goes to zero; finite-size systems, site-dependent hopping, interacting or indistinguishable particles, and other reset-age laws are not addressed. Scholarly originality awaits independent assessment.

## References

1. S. Wald and L. Böttcher, *From classical to quantum walks with stochastic resetting on networks*, arXiv:2008.00510 (first posted 2020-08-02), https://arxiv.org/abs/2008.00510.
2. D. Das, S. Dattagupta and S. Gupta, *Quantum unitary evolution interspersed with repeated non-unitary interactions at random times*, arXiv:2106.14181 (first posted 2021-06-27), https://arxiv.org/abs/2106.14181.
