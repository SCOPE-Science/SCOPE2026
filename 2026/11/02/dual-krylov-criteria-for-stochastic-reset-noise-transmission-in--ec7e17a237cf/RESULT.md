# Dual Krylov criteria for stochastic-reset noise transmission in finite oscillator networks

## Finding
For a finite connected undirected network of linearly coupled, unwrapped oscillator phases, suppose **at least two vertices are reset simultaneously to zero by one Poisson clock** while at least one other vertex is never reset. There are two distinct exact graph-theoretic tests for fluctuations transmitted to the never-reset vertices:

1. **All-rate silence:** the stationary covariance on the never-reset vertices vanishes at one positive reset rate if and only if it vanishes at every positive reset rate. Its necessary-and-sufficient condition is a finite Krylov annihilation test on the reset-vertex Laplacian block.
2. **Strong-rate transfer:** generically the stationary covariance on the never-reset vertices is of order \(\lambda^{-3}\), with an explicitly computable positive-semidefinite coefficient. The exact rank of this coefficient is a second, *different* Krylov rank, associated with the grounded Laplacian of the never-reset vertices.

The first test is strictly stronger than vanishing of the cubic coefficient: there are connected networks with a zero cubic coefficient but nonzero never-reset covariance at **every** finite positive reset rate. In contrast, another connected network can carry nontrivial randomness on reset vertices while its never-reset subsystem is perfectly deterministic for **all** positive reset rates.

## Assumptions and scope
Let \(V\) be a finite connected undirected graph, possibly with positive symmetric edge weights, and let \(L\) be its real symmetric graph Laplacian. Partition \(V=R\sqcup M\), where \(r=|R|\ge2\) and \(m=|M|\ge1\). Coordinates are ordered with \(R\) first. Take fixed \(\kappa>0\), \(\lambda>0\), and \(\omega\in\mathbb R^{r+m}\). Between events, the *exact linear, unwrapped model* is
\[
\dot X=\omega-\kappa LX.
\]
At the event times of a single homogeneous Poisson process of intensity \(\lambda\), reset **all** \(R\)-coordinates of \(X\) to zero simultaneously and leave all \(M\)-coordinates unchanged. Neither independent clocks for different vertices nor nonlinear sine coupling is asserted. This is the globally linearized variant of synchronized subsystem phase resetting, with \(\kappa=K/|V|\) in the convention of the motivating networked Kuramoto study.

Use the symmetric block notation
\[
L=\begin{pmatrix}H&E^{\mathsf T}\\E&G\end{pmatrix},\qquad
J=\begin{pmatrix}0&0\\0&I_m\end{pmatrix},\qquad P=I-J.
\]
Here \(G=L_{MM}\) is positive definite because the full network is connected and \(R\ne\varnothing\). Define the pinned reference phase, reset forcing, and transmitted forcing by
\[
x_M^0=\kappa^{-1}G^{-1}\omega_M,\qquad
h=\omega_R-\kappa E^{\mathsf T}x_M^0,\qquad g=Eh.
\]
Let \(\mathsf C(\lambda)=\operatorname{Cov}(X)\) denote the unique stationary covariance. Its blocks in the above order are \(U=\mathsf C_{RR}\), \(V=\mathsf C_{RM}\), and \(W=\mathsf C_{MM}\).

**Theorem (exact silence, sharp cubic coefficient and its rank).** For every such fixed network, partition, coupling and frequency vector:

**(a) Existence, uniqueness, means and moments.** The process has a unique invariant probability law with finite second moment. Put \(S=H-E^{\mathsf T}G^{-1}E\succeq0\). Its stationary mean is exactly
\[
\overline x_R=(\lambda I_r+\kappa S)^{-1}h,\qquad
\overline x_M=x_M^0-G^{-1}E\overline x_R.
\]
Its centered covariance is uniquely determined by
\[
\kappa(L\mathsf C+\mathsf C L)+\lambda(\mathsf C-J\mathsf C J)
=\lambda(P\overline x)(P\overline x)^{\mathsf T}.
\]

**(b) Complete silence at every rate.** The following statements are equivalent:
\[
\begin{aligned}
& W(\lambda_0)=0\text{ for some }\lambda_0>0;\\
& W(\lambda)=0\text{ for every }\lambda>0;\\
& EH^j h=0\text{ for }j=0,1,\ldots,r-1.
\end{aligned}
\]
In this case the never-reset vector equals \(x_M^0\) almost surely in the stationary law; the reset subsystem can nevertheless remain random.

**(c) Universal strong-rate orders.** With all graph parameters fixed and \(\lambda\to\infty\),
\[
\begin{aligned}
U&=\lambda^{-2}hh^{\mathsf T}+O(\lambda^{-3}),\\
V&=-\kappa\lambda^{-3}hh^{\mathsf T}E^{\mathsf T}+O(\lambda^{-4}),\\
W&=\lambda^{-3}T+O(\lambda^{-4}),
\end{aligned}
\]
where \(T\) is the unique symmetric solution of
\[
GT+TG=2\kappa gg^{\mathsf T}
\]
and thus has the exact positive-semidefinite representation
\[
T=2\kappa\int_0^\infty e^{-Gt}gg^{\mathsf T}e^{-Gt}\,dt.
\]
The estimates are entrywise or in any fixed finite-dimensional matrix norm and are **not claimed uniformly over growing networks or changing coupling strengths**.

**(d) Exact rank of the transferred cubic coefficient.** With \(m=|M|\),
\[
\boxed{\operatorname{rank}T
=\dim\operatorname{span}\{g,Gg,\ldots,G^{m-1}g\}.}
\]
Consequently, \(T\) is positive definite precisely when this Krylov span is all of \(\mathbb R^m\). It vanishes precisely when \(Eh=0\). Such vanishing need not imply the all-rate silence criterion in (b).

## Proof
**1. Grounding and ergodicity.** The graph Laplacian satisfies \(z^{\mathsf T}Lz=\sum_{\{i,j\}}w_{ij}(z_i-z_j)^2\ge0\), with kernel equal to the constant vectors because the graph is connected. Restricting to vectors zero on \(R\) makes this quadratic form positive definite on \(M\), so \(G\succ0\). Likewise \(2\kappa L+\lambda P\succ0\): its quadratic form has no nonzero common null vector. Under a synchronous coupling of two trajectories using the same Poisson clock, their difference \(Y\) obeys the drift \(\dot Y=-\kappa LY\) and jump \(Y\mapsto JY\). Its squared-norm generator is
\[
\mathcal A\|Y\|^2=-2\kappa Y^{\mathsf T}LY-\lambda\|PY\|^2\le-c\|Y\|^2
\]
for some \(c>0\). This yields exponential contraction in quadratic Wasserstein distance. For the forced process, the same generator estimate with \(2\omega^{\mathsf T}X\) and Young's inequality gives a finite-second-moment Lyapunov bound. Standard finite-dimensional Feller construction and contraction therefore give existence and uniqueness of the invariant law. This argument does not incorrectly infer a Gaussian stationary law: Poisson reset mixtures are generally non-Gaussian.

**2. Exact stationary equations.** Applying the generator to coordinate functions gives \((\kappa L+\lambda P)\overline x=\omega\). The \(M\) block yields \(\overline x_M=x_M^0-G^{-1}E\overline x_R\); substitution into the \(R\) block gives \((\lambda I_r+\kappa S)\overline x_R=h\). The Schur complement \(S\) is positive semidefinite since \(L\succeq0\) and \(G\succ0\). The jump update \(X\mapsto JX\) applied to second moments, followed by subtraction of the mean equation, gives exactly the covariance identity in (a). Its homogeneous linear operator is injective on symmetric matrices, by the same mean-square contraction applied to differences, and hence the stationary covariance solves it uniquely.

**3. All-rate silence.** If \(EH^j h=0\) for \(j=0,\ldots,r-1\), Cayley–Hamilton gives \(Ee^{-\kappa Hs}h=0\) for every \(s\ge0\). Starting immediately after a reset at \((X_R,X_M)=(0,x_M^0)\), the inter-event solution is
\[
X_R(s)=\int_0^s e^{-\kappa Hu}h\,du,\qquad X_M(s)=x_M^0.
\]
The Krylov condition makes \(EX_R(s)=0\), so this trajectory indeed satisfies **both** coupled block equations, and the next common reset returns it to the same reset section. A stationary exponential age therefore produces an invariant law supported on \(X_M=x_M^0\). Uniqueness proves \(W=0\) at every rate.

Conversely, if \(W(\lambda_0)=0\) for some positive rate, stationarity and path continuity of the never-reset block imply that \(X_M(t)=a\) is constant for all times almost surely. Its drift equation makes \(EX_R(t)=\kappa^{-1}\omega_M-Ga\) constant between events. Immediately after a common reset \(X_R=0\), so the constant must be zero and \(a=x_M^0\). From each reset, the reset block follows the displayed analytic formula for \(X_R(s)\), until the next event. Since exponential holding times have positive probability of exceeding any prescribed duration, \(EX_R(s)=0\) for every \(s\ge0\). Differentiating at zero repeatedly yields \(EH^j h=0\) for all nonnegative \(j\), and Cayley–Hamilton reduces the check to \(j<r\). Thus one-rate silence and all-rate silence are equivalent.

**4. Cubic asymptotics.** The mean expression implies \(\overline x_R=\lambda^{-1}h+O(\lambda^{-2})\). The three blocks of the exact covariance equation are
\[
\begin{aligned}
\lambda U+\kappa(HU+UH+E^{\mathsf T}V^{\mathsf T}+VE)&=\lambda\overline x_R\overline x_R^{\mathsf T},\\
\lambda V+\kappa(HV+E^{\mathsf T}W+UE^{\mathsf T}+VG)&=0,\\
GW+WG+EV+V^{\mathsf T}E^{\mathsf T}&=0.
\end{aligned}
\]
Since \(L\succeq0\) and \(\mathsf C\succeq0\), taking the full trace equation gives \(\operatorname{tr}U\le\|\overline x_R\|^2=O(\lambda^{-2})\), so \(U=O(\lambda^{-2})\). The invertible Sylvester operator \(W\mapsto GW+WG\) gives \(\|W\|=O(\|V\|)\). The middle equation then yields \(V=O(\lambda^{-3})\) for sufficiently large \(\lambda\), and hence \(W=O(\lambda^{-3})\). Inserting these bounds back into the block equations yields successively
\[
\lambda^2 U\to hh^{\mathsf T},\qquad
\lambda^3V\to-\kappa hh^{\mathsf T}E^{\mathsf T},
\]
then \(\lambda^3W\to T\), where \(GT+TG=2\kappa(Eh)(Eh)^{\mathsf T}\). Because all finite-dimensional coefficients depend rationally on \(\lambda\), the stated one-additional-power remainder bounds follow. The integral formula for \(T\) follows from \(G\succ0\).

**5. Rank.** For any \(v\in\mathbb R^m\),
\[
v^{\mathsf T}Tv=2\kappa\int_0^\infty(v^{\mathsf T}e^{-Gt}g)^2\,dt.
\]
It vanishes if and only if \(v^{\mathsf T}G^j g=0\) for every integer \(j\ge0\), equivalently just \(j=0,\ldots,m-1\). Orthogonal complementation proves the exact rank identity, with no genericity assumptions.

**6. Explicit witnesses separating the tests.** For the three-vertex star with two reset leaves \(R=\{1,2\}\), one never-reset center \(M=\{3\}\), unit edge weights and \(\kappa=1\), choose \(\omega=(1,-1,0)\). Then \(G=(2)\), \(H=I_2\), \(E=(-1,-1)\), \(h=(1,-1)^{\mathsf T}\). Thus \(EH^j h=0\) for all \(j\); the center is exactly constant while both leaves fluctuate after their common reset.

For a four-vertex graph with \(R=\{1,2,3\}\), \(M=\{4\}\) and edges \(\{1,4\},\{2,4\},\{1,3\}\), choose \(\kappa=1\) and \(\omega=(1,-1,0,0)\). One has \(h=(1,-1,0)^{\mathsf T}\), \(Eh=0\) but \(EHh=-1\ne0\). Hence \(T=0\) while \(W(\lambda)>0\) for every \(\lambda>0\) by part (b). **A vanishing cubic coefficient is not a certificate of perfect noise isolation.**

Finally, for the four-vertex path with \(R=\{1,2\}\), \(M=\{3,4\}\), unit weights, \(\kappa=1\), and \(\omega=(0,1,0,0)\), the coefficient on \(M\) is
\[
T=\begin{pmatrix}2/3&1/3\\1/3&1/3\end{pmatrix},\qquad\det T=1/9>0.
\]
Thus even a **single shared Poisson clock** can produce full-rank leading covariance across two never-reset vertices.

## Verification
A standalone program, `verification/check.py`, reconstructs full centered second moments by solving the finite-dimensional stationary matrix equation, without using the asymptotic block derivation. It checks exact two-node rational formulas (used as an established limit case), the full-rank two-reset path, a noise-silent two-reset star, a graph where cubic noise cancels but every finite-rate variance remains nonzero, and several random connected weighted graphs. The script performs 485 assertions with NumPy and SciPy and prints a single PASS summary. Run `python verification/check.py` after installing dependencies listed in `verification/requirements.txt`. The random checks are not a substitute for the quantified proof above.

## Relationship to prior work
Paramero-Arias and Riascos (2026, arXiv:2610.21842) introduce the connected-network subsystem resetting model, give the exactly pinned infinite-rate linearized grounded-Laplacian dynamics, and numerically study finite rates. Their central reported analytical objective is the pinned synchronization level, not the joint-clock covariance transfer or the all-rate silence criterion. The earlier simultaneous subsystem-reset Kuramoto work by Majumder, Chattopadhyay and Gupta (2024, arXiv:2402.14921) analyzes macroscopic order parameters and explicitly notes omitted subsystem correlations in its finite-rate approximation. Majumder, Acharya and Gupta (2026, arXiv:2604.04769) develop a general continued-fraction treatment of synchronization order parameters for globally coupled models; no finite-graph Krylov covariance classification could be verified from the accessible material.

The classical Lyapunov equation and controllability Gramian are established tools, and the general moment equation is not asserted as independently new. A previous mathematical finding had already proved the one-reset-vertex cubic covariance law and positivity, for a fixed connected graph with \(|R|=1\). The **new scope being evaluated here is \(|R|\ge2\)**: the independent necessary-and-sufficient all-rate silence test, its strict separation from cancellation of the cubic coefficient, and the exact network-mode rank classification for *simultaneously* reset multiple vertices. The one-reset-vertex theorem is acknowledged, not rebranded.

## Limitations
The assertion concerns precisely a finite-dimensional, undirected, symmetric-weight, unwrapped **linear** oscillator model with a *single common* Poisson clock resetting all members of a fixed subset to zero. It is not an exact statement for nonlinear Kuramoto sine coupling, for separate reset clocks, for continuous dynamical noise, or for other reset protocols. No uniformity in graph size, coupling, or frequencies is asserted. The rank formula concerns the leading cubic coefficient; it need not equal the rank of the finite-rate covariance. A zero cubic coefficient alone does not determine the next nonzero exponent. Uniqueness or exact absence of related formulas in the entire literature is not asserted; the priority assessment is qualified by incomplete access to one broad prior source.

## References
1. K. Paramero-Arias and A. P. Riascos, *Synchronization induced by stochastic subsystem resetting in complex networks*, arXiv:2610.21842v1 (first submitted 2026-10-15), https://arxiv.org/abs/2610.21842.
2. R. Majumder, R. Chattopadhyay and S. Gupta, *Kuramoto model subject to subsystem resetting: How resetting a part of the system may synchronize the whole of it*, Physical Review E 109, 064137 (2024), arXiv:2402.14921, https://arxiv.org/abs/2402.14921.
3. R. Majumder, A. Acharya and S. Gupta, *Analytical approach to subsystem resetting in generalized Kuramoto models*, Physical Review E 114, 024108 (2026), arXiv:2604.04769, https://arxiv.org/abs/2604.04769.
