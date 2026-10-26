# Beta–Bernoulli stationary coupling and universal near-wall motility in a run-and-tumble trap

## Finding

Consider a harmonically confined one-dimensional particle with two running velocities and a zero-velocity tumbling state. The following single theorem gives a latent representation of its stationary joint position–motility law, strict global radial orderings, and a universal conditional near-wall law.

Let \(k,v,r,u>0\), let \(J\in\{-1,0,+1\}\), and let \(X\) evolve by \(\dot X=-kX+vJ\). Each \(J=\pm1\) changes to \(J=0\) at rate \(r\). From \(J=0\), transitions to either sign occur at rate \(u/2\). Define
\[
Y=\frac{kX}{v},\qquad \rho=\frac r k,\qquad \tau=\frac u k,\qquad H={\mathbf{1}}_{\{|J|=1\}}.
\]
There is a unique stationary probability law, and its marginal joint law of \((Y,H)\) can be sampled **exactly**, without simulating paths, by
\[
A\sim\operatorname{Beta}\!\left(\frac\tau2,\frac\rho2\right),\qquad
B\sim\operatorname{Beta}\!\left(\frac12,\frac\rho2\right),\qquad
H\mid A\sim\operatorname{Bernoulli}(A),\qquad Y=S\sqrt{AB},
\]
where \(A,B\) and a fair sign \(S\in\{-1,+1\}\) are mutually independent except for the displayed conditional dependence of \(H\) on \(A\). This equality concerns the *stationary law of position and run/tumble status*; it is not an identification of physical latent variables along trajectories and does not reconstruct the sign of the running velocity.

For every \(0<z<1\), the strict phase ordering is
\[
\Pr(|Y|>z\mid H=1)>\Pr(|Y|>z\mid H=0).
\]
At fixed \(\rho\), increasing \(\tau\) strictly increases \(\Pr(|Y|>z)\) for every such \(z\); at fixed \(\tau\), increasing \(\rho\) strictly decreases it. Hence every even convex position observable is monotonically ordered, without needing to inspect separate peaks or low moments.

Put \(a=\tau/2\), \(c=\rho/2\), \(\lambda=c+\tfrac12-a\), and \(\epsilon=1-y^2\). A regular conditional tumble probability at each \(0<|y|<1\) has the explicit hypergeometric form
\[
\Pr(H=0\mid Y=y)=\frac\epsilon2\frac{{}_2F_1(\lambda,c+1;2c+1;\epsilon)}{{}_2F_1(\lambda,c;2c;\epsilon)}.
\]
In particular, **independently of both positive switching rates**, as \(|y|\uparrow1\),
\[
\Pr(H=0\mid Y=y)=\frac{1-y^2}{2}+O((1-y^2)^2)
=1-|y|+O((1-|y|)^2).
\]
The coefficient is for the normalized position; in physical coordinates, \(|y|=k|x|/v\).

## Assumptions and scope

The trap is linear and deterministic between jumps, the speed is fixed, the two running directions are chosen equiprobably at every exit from tumble, and the run and tumble durations are independent exponential holding times with strictly positive finite rates. There is no additional positional diffusion. Physical time and position are rescaled by \(s=kt\) and \(Y=kX/v\); the stationary position belongs to \((-1,1)\) almost surely, while its closed topological support is \([-1,1]\). All comparisons keep \(k\) and \(v\) fixed and vary only the specified switching rate. The process has three velocity values but only a two-valued motility flag \(H\).

## Proof

**Existence and uniqueness.** The velocity state \(J\) is an irreducible finite-state continuous-time Markov chain, possessing a unique stationary two-sided version. In dimensionless time, let \(J_s\) denote this version and define \(Y_s=\int_{-\infty}^{s}e^{-(s-q)}J_q\,dq\). This provides a stationary solution of \(\dot Y=-Y+J\), with \(|Y|<1\) almost surely. Any two copies of \(J\) can be coupled to coincide after an almost surely finite meeting time; thereafter, differences in \(Y\) contract as \(e^{-s}\). This proves uniqueness. Reflection of the velocity chain proves symmetry in \(Y\) conditional on the flag.

**Exact weighted moment recurrences.** For \(n\ge0\), write \(m_n=\mathbb E[Y^n]\), \(p_n=\mathbb E[JY^n]\), and \(q_n=\mathbb E[J^2Y^n]\). Applying the stationary generator to \(Y^n,JY^n,J^2Y^n\) yields for \(n\ge1\)
\[
m_n=p_{n-1},\qquad (n+\rho)p_n=nq_{n-1},\qquad
(n+\rho+\tau)q_n=np_{n-1}+\tau m_n.
\]
Also \(q_0=\Pr(H=1)=\tau/(\rho+\tau)\). It follows, for \(n\ge1\), that
\[
\frac{m_{2n}}{m_{2n-2}}=
\frac{(2n-1)(2n-2+\tau)}{(2n-1+\rho)(2n-2+\rho+\tau)},\qquad
q_{2n}=\frac{2n+\tau}{2n+\rho+\tau}m_{2n}.
\]
In rising-factorial notation, therefore,
\[
m_{2n}=\frac{(1/2)_n(\tau/2)_n}{((1+\rho)/2)_n((\rho+\tau)/2)_n}.
\]
For the proposed independent Beta variables, \(\mathbb E[(AB)^n]=m_{2n}\) and
\[
\mathbb E[H(AB)^n]=\mathbb E[A^{n+1}]\mathbb E[B^n]
=\frac{2n+\tau}{2n+\rho+\tau}m_{2n}=q_{2n}.
\]
All monomials weighted by either value of \(H\) are thus identical for the physical process and for the sampler. Polynomial density on \([0,1]\) gives joint law equality of \((Y^2,H)\), and reflection symmetry supplies the independent fair sign. This proves the exact representation without assuming that a finite moment table determines an unbounded law.

**Strict stochastic orders.** Beta conjugacy gives
\[
A\mid H=1\sim\operatorname{Beta}(a+1,c),\qquad
A\mid H=0\sim\operatorname{Beta}(a,c+1),
\]
while \(B\) remains independent of \((A,H)\). The ratio of the first conditional Beta density to the second is a positive constant times \(w/(1-w)\), strictly increasing for \(0<w<1\). The two laws are therefore strictly ordered at every interior threshold. Multiplication by the independent \(B\), which has positive density throughout \((0,1)\), preserves strict survival inequalities. For changing rates, a Beta law strictly increases stochastically when its first shape increases and strictly decreases when its second shape increases. The two independent factors therefore give strict radial tail monotonicity in \(\tau\) and \(\rho\), as stated. Symmetry converts radial ordering into the corresponding ordering of even convex observables.

**Exact near-wall flag law.** Put \(Z=Y^2=AB\). For \(0<z<1\), the conditional density of \(A=w\) given \(Z=z\) is, up to a normalizing constant,
\[
w^{a-c-1/2}(1-w)^{c-1}(w-z)^{c-1}{\mathbf{1}}_{\{z<w<1\}}.
\]
Setting \(\epsilon=1-z\) and \(T=(1-A)/\epsilon\) converts it to a density proportional to
\[
T^{c-1}(1-T)^{c-1}(1-\epsilon T)^{-\lambda},\qquad 0<T<1.
\]
Because \(H\mid A\) is Bernoulli with success probability \(A\), the conditional tumble probability equals \(\epsilon\,\mathbb E[T\mid Z=z]\). Euler's beta integral gives
\[
\mathbb E[T\mid Z=z]=\frac12\,
\frac{{}_2F_1(\lambda,c+1;2c+1;\epsilon)}{{}_2F_1(\lambda,c;2c;\epsilon)}.
\]
For fixed \(a,c>0\), the tilted Beta integrals are analytic at \(\epsilon=0\) and reduce there to the symmetric \(\operatorname{Beta}(c,c)\) measure with mean \(1/2\). Consequently \(\epsilon\mathbb E[T\mid Z=z]=\epsilon/2+O(\epsilon^2)\). Since the stationary sign is fair and independent of \((Z,H)\), conditioning on \(Y=y\) is the same as conditioning on \(Z=y^2\) for the motility flag. This completes the proof.

## Verification

The standalone `verify.py` (Python 3, NumPy, SciPy) is run with `python verify.py`. It checks 256 diverse positive-rate sets through order 25 of the stationary even moments; six parameter sets of independently reconstructed generator balances; five independent exact-between-jumps simulated Markov velocity trajectories against second/fourth moments and run fractions; latent conditional moments and strict sampled radial tail inequalities; and twenty posterior calculations comparing Gauss–Jacobi quadrature to the Gauss hypergeometric formula, including the limiting coefficient. Observed results are finite numerical diagnostics only. The proof above establishes the universal parameter and threshold quantifiers.

## Relationship to prior work

The 2024 work of Sun, Ye and Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time* (arXiv:2409.00578), already gives the exact marginal characteristic function and a hypergeometric position density for arbitrary positive run and tumble rates; none of those foundational marginal formulas is claimed as new. The 2019 paper of Basu and coauthors (arXiv:1910.10083) exactly solves the equal-rate three-state model. The 2026 paper of Sun, Ye and Chen (arXiv:2610.24961) goes further than the 2024 paper by obtaining complete run- and tumble-resolved densities and must be credited for that prior coverage. The 2026 work of Guéneau, Majumdar and Schehr (arXiv:2602.08436) treats independently refreshed velocities and Dirichlet stick-breaking for a different velocity-transition generator; its three-speed example permits direct inter-speed renewals absent from this alternating run/tumble generator.

The present claim is not first discovery of the model, its full one-time position density, its moments, or separate motility densities. It is the explicit joint beta–Bernoulli coupling of position magnitude and motility flag, rigorous strict ordering of all radial thresholds for all independent switching rates, and the exact universal conditional near-wall coefficient. These follow from, but are not the results stated by, the published special-function formulas. A corresponding characterization elsewhere remains a residual literature risk.

## Limitations

Only one spatial dimension, a symmetric three-state velocity chain with zero-speed tumble, positive finite exponential transition rates, deterministic harmonic confinement, and zero thermal diffusion are covered. The auxiliary beta and Bernoulli variables reproduce a one-time stationary law, not the temporal correlation structure or the sign of the running velocity. The universal wall statement is a position-conditional asymptotic, not a finite-distance identity with exactly constant slope. The mathematical novelty assessment is self-review only and has not undergone independent scientific audit.

## References

1. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, first posted 2024-09-01. Full text: https://arxiv.org/html/2409.00578v2.
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019). Full text: https://arxiv.org/html/1910.10083v1.
3. A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker–Planck equation from the equations of motion*, arXiv:2610.24961 (2026). Full text: https://arxiv.org/html/2610.24961v1.
4. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (2026). Full text: https://arxiv.org/abs/2602.08436.
