# Two exact temperature-calibration steps and a fourth-moment trap in randomized Hamiltonian Monte Carlo

## Finding

Apply the two-force, triangularly randomized 5/2-order Runge–Kutta–Nyström (rRKN 2.5) position update of Bou-Rabee and Kleppe to the one-dimensional harmonic Hamiltonian with potential \(U(q)=\omega^2q^2/2\), \(\omega>0\). Make one time-integrator step of duration \(h>0\) per unadjusted Hamiltonian Monte Carlo transition, and independently refresh the momentum from \(N(0,1)\) at each transition. Put \(z=\omega^2h^2\) and
\[
D(z)=1-\frac{13z}{36}+\frac{z^2}{18}-\frac{z^3}{288}.
\]
Let \(\rho=7.03678461799370\ldots\) be the unique positive zero of \(D\). For every \(0<z<\rho\), the position chain has a unique invariant probability with finite second moment, and the sharp stationary-to-target variance ratio is
\[
\boxed{\omega^2\operatorname{Var}(Q_\infty)=\frac{(1-z/6)^2}{D(z)}.}
\]
For \(z\ge\rho\), the chain has no invariant probability with finite second moment. Within the finite-variance stability interval, its stationary variance equals the exact Gaussian target variance \(\omega^{-2}\) **if and only if**
\[
\boxed{z=4-2\sqrt2\quad\text{or}\quad z=4+2\sqrt2.}
\]
The variance bias is positive for \(0<z<4-2\sqrt2\), negative between the two roots, and positive again for \(4+2\sqrt2<z<\rho\). At \(z=6\) the invariant law collapses exactly to a point mass at zero.

These two nonzero variance-calibration points **do not yield the Gaussian target distribution**. For every \(0<z<\rho\) except \(z=6\), the invariant distribution is non-Gaussian. More sharply, at the smaller calibration point the invariant fourth moment is finite, but at the larger calibration point its fourth moment is **infinite**, even though its variance agrees exactly with the target. This gives an exact example in which matching the second moment masks a fundamentally heavy-tailed invariant sampler.

## Assumptions and scope

The integrator is exactly rRKN 2.5 from equations (2)–(4) of Bou-Rabee and Kleppe, with the triangular internal variable \(V\) of density \(2v\) for \(0<v<1\). At each outer transition, a fresh independent \(N(0,1)\) momentum is sampled; there is no accept/reject correction. The method takes **one** rRKN substep per outer transition (integration duration \(T=h\)); step size is constant. Stage randomness and momenta are independent across outer transitions. Statements about \(z\) beyond small-step convergence assumptions concern the explicitly defined polynomial algorithm, not error guarantees for the underlying Hamiltonian flow. All claims involve real one-dimensional harmonic potentials and the position marginal only.

## Proof

**1. Exact one-transition law.** In a harmonic potential the force is \(F(q)=-\omega^2q\). The rRKN 2.5 force evaluations are \(F^-=F(q)\) and \(F^+=F(q+Vhv+(Vh)^2F^-/2)\). Substitution in the source position formula
\[
q^+=q+hv+\frac{h^2}{2}F^-+\frac{h^2}{6V}(F^+-F^-)
\]
results in
\[
\boxed{Q_{k+1}=A_kQ_k+B\xi_k,\quad
A_k=1-\frac z2+\frac{z^2}{12}V_k,\quad
B=h\left(1-\frac z6\right),}
\]
where \(V_k\) has density \(2v\), \(\xi_k\sim N(0,1)\), and all variables are mutually independent as stipulated. Thus \(\mathbb EV=2/3\), \(\mathbb EV^2=1/2\), and direct expansion gives
\[
\mathbb EA_k^2=\frac{z^4-16z^3+104z^2-288z+288}{288}
=1-zD(z).
\]

**2. Exact stability and variance.** We have \(D'(z)=-(3z^2-32z+104)/288<0\) for all real \(z\), because the displayed quadratic has negative discriminant and positive leading coefficient. With \(D(0)=1\) and \(D(z)\to-\infty\), there is exactly one positive root \(\rho\). For \(0<z<\rho\), \(\mathbb EA^2<1\), and coupling two trajectories with the same fresh coefficient and Gaussian noise gives strict quadratic Wasserstein contraction. Consequently there is exactly one invariant law with finite second moment. Its mean is zero and its second moment obeys
\[
\operatorname{Var}(Q_\infty)=\mathbb EA^2\operatorname{Var}(Q_\infty)+B^2.
\]
Solving this yields the stated exact variance ratio. When \(z\ge\rho\), \(\mathbb EA^2\ge1\) and \(B\ne0\). The same nonnegative stationary second-moment identity rules out any finite-second-moment invariant law; this does **not** assert nonexistence of invariant laws with infinite variance.

**3. Exactly two calibrations.** Subtraction of target variance yields
\[
\boxed{\omega^2\operatorname{Var}(Q_\infty)-1
=\frac{z(z^2-8z+8)}{288D(z)}.}
\]
Since \(D(z)>0\) throughout the stable interval, the nontrivial roots and bias sign follow from the quadratic. Both roots satisfy \(0<4-2\sqrt2<4+2\sqrt2<\rho\), as is verified either directly using \(\mathbb EA^2=(z+1)/9<1\) at either root, or by monotonicity of \(D\). At \(z=6\), \(B=0\), so the unique finite-variance invariant law is \(\delta_0\).

**4. Distributional nonequivalence and infinite fourth moment.** For any \(0<z<\rho\) with \(z\ne6\), the invariant second moment is positive and \(A^2\) is not almost surely constant: \(A\) is a nonconstant affine function of a continuously distributed \(V\). If the invariant law were Gaussian with its actual variance \(s^2>0\), stationarity would express it as a mixture of centered Gaussians with random conditional variance \(A^2s^2+B^2\). This variance is nonconstant, and Jensen's strict inequality for the function \(v\mapsto e^{-t^2v/2}\), at any \(t\ne0\), contradicts equality to the characteristic function of one centered Gaussian. Thus all nondegenerate stationary laws are non-Gaussian.

For the fourth moment, direct expansion using independent normal noise gives the necessary invariant identity
\[
\mathbb E Q_\infty^4=(\mathbb EA^4)\mathbb E Q_\infty^4
+6B^2(\mathbb EA^2)\mathbb E Q_\infty^2+3B^4.
\]
The coefficient is exactly
\[
\mathbb EA^4=\sum_{j=0}^{4}\binom4j
\left(1-\frac z2\right)^{4-j}\left(\frac{z^2}{12}\right)^j\frac2{j+2}.
\]
At either calibration root, reduction modulo \(z^2-8z+8\) gives the exact identity
\[
\mathbb EA^4-1=\frac{2(159z-758)}{1215}.
\]
This is strictly negative at \(z_-=4-2\sqrt2\) and positive at \(z_+=4+2\sqrt2\). At \(z_-\), the affine iteration is contractive in fourth mean because \(\mathbb E|A|^4<1\), so its invariant fourth moment is finite. At \(z_+\), \(B\ne0\) and the identity would have a positive right-hand forcing with a nonpositive coefficient on the fourth moment; therefore no finite fourth moment exists. All these conclusions concern the actual stationary distribution, not just a finite-time simulation.

## Verification

The standalone `verify.py` (dependency in `requirements.txt`) rederives the one-step position formula by symbolic substitution, checks the second and fourth coefficient moment polynomials, verifies the unique positivity interval and both exact calibration identities, confirms opposite fourth-moment signs, and performs independent exact rational moment tests and a seeded Monte Carlo stationary check. The included script printed `PASS: 245 checks`, with a simulated stationary variance close to one at the lower calibration point. The analytic proof establishes the infinite-time and infinite-moment assertions independently of finite numerical experiments.

## Relationship to prior work

Bou-Rabee and Kleppe (2023) define rRKN 2.5, its triangular stage variable, and its use with full momentum refresh in unadjusted HMC, providing global accuracy bounds and Gaussian-target numerical studies. Their Section 3, Remark 1 derives the Gaussian invariant bias of the **Verlet** comparator, not the exact random-coefficient stationary variance or fourth-moment behavior of rRKN 2.5 at one substep. Bou-Rabee and Marsden (2022) treat a related but distinct lower-order randomized time integrator. Other Gaussian harmonic Langevin bias and stationary-covariance results concern different splitting algorithms, not these explicit rRKN 2.5 coefficient moments. The present algebraic special case does not supersede the original global error bounds and does not imply unbiased sampling from the target law. The use of random affine recurrences and the variance/fourth-moment criterion is classical; the new claim is their exact coupling to this specified published integrator, with two distinct target-variance zeros and sharply different fourth-moment behavior.

## Limitations

The result is for a single rRKN 2.5 substep with full independent momentum refresh in one harmonic dimension. The larger calibration point is outside the small-step assumptions of the original accuracy theorem; it is a mathematical diagnostic of the actual polynomial Markov chain, not a recommended practical step size. Fourth moment is proved infinite at the larger calibration despite finite variance, but no exact heavy-tail exponent is asserted. Existence of invariant measures without finite variance beyond \(\rho\) is not addressed. A specialized prior exact harmonic analysis could still precede this statement; searches cannot certify universal novelty. Independent audit is not performed.

## References

1. N. Bou-Rabee and T. S. Kleppe, *Randomized Runge-Kutta-Nyström Methods for Unadjusted Hamiltonian and Kinetic Langevin Monte Carlo*, arXiv:2310.07399, first posted 2023-10-11, https://arxiv.org/abs/2310.07399 .
2. N. Bou-Rabee and M. Marsden, *Unadjusted Hamiltonian MCMC with Stratified Monte Carlo Time Integration*, arXiv:2211.11003, first posted 2022-11-20, https://arxiv.org/abs/2211.11003 .
