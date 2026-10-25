# Lorentzian thermal-conductance optimum and an asymmetry-driven pinning transition in a three-oscillator chain

## Finding
For a unit-mass three-oscillator harmonic chain with identical unit neighbor springs, positive terminal substrate spring constants \(p,q>0\), a freely chosen nonnegative middle substrate spring constant \(x\geq0\), and independent unit-friction Langevin heat baths at the terminal oscillators, the nonequilibrium steady heat current is exactly a Lorentzian function of the middle spring constant. Let
\[
u=\frac{p+q}{2},\qquad d=\frac{p-q}{2},\qquad S=u+d^2,\qquad x_0=u-\frac32+\frac1{2(S+1)}.\]
For temperatures \(T_L>T_R>0\) and Boltzmann constant one,
\[
J(x)= (T_L-T_R)\frac{2(S+1)(S+2)}{(S+2)^2(4S+3)+4(S+1)^2(x-x_0)^2}.
\]
It has the **unique global optimum on \(x\geq0\)** at \(x_*=\max\{0,x_0\}\). If \(x_0>0\), this is an interior peak with
\[
\frac{J(x_*)}{T_L-T_R}=\frac{2(S+1)}{(S+2)(4S+3)}.
\]
If \(x_0\leq0\), the unique maximizer is the unpinned middle oscillator \(x=0\), and every increase \(x>0\) strictly reduces the current. The optimum location decreases strictly when the squared terminal-stiffness contrast \(d^2\) increases at fixed mean \(u\):
\[
\frac{\partial x_0}{\partial(d^2)}=-\frac1{2(S+1)^2}<0.
\]
At equal terminal substrate stiffnesses \(p=q=u\), the interior regime begins precisely at \(u>(1+\sqrt{17})/4\). For example, at \(u=1.3\), the equal-stiffness choice has an interior optimum near \(x=0.01739\), whereas \(p=1.8,q=0.8\) places the optimum at the boundary \(x=0\). The result quantifies a transition between resonant central pinning and boundary-optimal absence of pinning.

## Assumptions and scope
Let \(Q=(Q_1,Q_2,Q_3)^\mathsf T\), \(V=(V_1,V_2,V_3)^\mathsf T\). The stochastic equations, with statistically independent Brownian motions at the two ends, are
\[
 dQ=V\,dt,\qquad dV=-KQ\,dt-\Gamma V\,dt+\operatorname{diag}(\sqrt{2T_L},0,\sqrt{2T_R})\,dW,
\]
\[
K=\begin{pmatrix}p+1&-1&0\\-1&x+2&-1\\0&-1&q+1\end{pmatrix},\quad\Gamma=\operatorname{diag}(1,0,1).
\]
Masses, connecting springs, and end bath friction coefficients are normalized to one; site coordinates are linear and classical. The onsite parameters satisfy \(p,q>0\) and \(x\geq0\); temperatures satisfy \(T_L>T_R>0\). The left-bath-to-right-bath stationary mean energy flux equals \(J=T_L-\mathbb E[V_1^2]\), and agrees with \(\mathbb E[Q_1V_2]\) and \(\mathbb E[Q_2V_3]\). The conclusion is for three sites, with no bath on the middle site.

## Proof
**Step 1: Unique stationary covariance.** Write the drift on \((Q,V)\in\mathbb R^6\) as
\[
A=\begin{pmatrix}0&I_3\\-K&-\Gamma\end{pmatrix}.
\]
The stiffness matrix is positive definite because it is the sum of positive terminal on-site springs and the two nearest-neighbor squared-extension forms, with the middle site connected to both ends. Explicitly,
\[
\det K=(pq+p+q+1)x+2pq+p+q>0.
\]
The deterministic energy \(E=(|V|^2+Q^\mathsf TKQ)/2\) satisfies \(\dot E=-V_1^2-V_3^2\). A hypothetical purely imaginary eigenmode with vanishing dissipation has zero terminal velocities and hence, at nonzero frequency, zero terminal displacements; the terminal eigen-equations then force the middle displacement to vanish as well. At zero frequency the positivity of \(K\) likewise excludes a mode. Consequently the finite-dimensional drift \(A\) is Hurwitz, and the Gaussian stationary covariance \(C\) exists uniquely as the solution of
\[
AC+CA^\mathsf T+\operatorname{diag}(0,0,0,2T_L,0,2T_R)=0.
\]
Stationarity and the energy-balance equations give equality of left and right bath currents and the two bond currents. Since the covariance depends linearly on bath temperatures and the common-temperature Gibbs state has zero current, it suffices to evaluate the current at \(T_L=1,T_R=0\) and multiply by \(T_L-T_R\).

**Step 2: Exact elimination.** Put the \(21\) unknown upper-triangular entries \(C_{ij}\) in lexicographic order \(1\leq i\leq j\leq6\), and equate those same \(21\) upper-triangular entries of the Lyapunov equation. Denote the resulting nonsingular matrix by \(M\) and its right-hand side by \(b\). Let \(M_{44}\) be the matrix obtained by replacing the column for the entry \(C_{44}=\mathbb E[V_1^2]\) by \(b\). Define
\[
D=\frac{2(S+2)^2(4S+3)}{S+1}+8(S+1)(x-x_0)^2.
\]
Exact polynomial/rational elimination gives the two reproducible determinant identities
\[
\det M=-64(\det K)D,\qquad \det M-\det M_{44}=-256(\det K)(S+2).
\]
All the denominators are strictly positive since \(p,q>0\), and therefore \(S>0\). Cramer's rule, with \(J(1,0)=1-C_{44}\), yields
\[
J(1,0)=\frac{4(S+2)}D=\frac{2(S+1)(S+2)}{(S+2)^2(4S+3)+4(S+1)^2(x-x_0)^2}.
\]
The accompanying reproducibility script constructs \(M\) from the displayed Langevin generator and verifies both exact determinant identities using symbolic arithmetic, rather than assuming this elimination formula.

**Step 3: Sharp global optimization.** The numerator in the last expression is positive and independent of \(x\); the denominator is the sum of a strictly positive constant and a positive constant times \((x-x_0)^2\). Consequently the unique real-axis maximizer is \(x_0\), and the unique maximizer over \(x\geq0\) is its Euclidean projection \(x_*\). The boundary/interior claims and the maximum value follow directly. At fixed \(u\), the partial derivative with respect to \(d^2\) is negative, proving the contrast-induced shift. When \(d=0\), the strict inequality \(x_0>0\) reduces to \(2u^2-u-2>0\), with positive root \((1+\sqrt{17})/4\). This proves every stated quantifier and endpoint.

## Verification
`checker.py` is a standalone Python 3 program requiring SymPy, NumPy and SciPy. It reconstructs the drift and the full \(21\)-variable Lyapunov system, checks the two claimed determinant equalities symbolically, and checks the derivative and asymmetry identities. It separately solves \(1,400\) independent \(6\)-dimensional Lyapunov equations at randomly selected admissible parameters, comparing four independent representations of flux per sample; another \(700\) samples test five candidate control settings against the exact global optimizer. The final observed execution passed all symbolic assertions and \(9,100\) numerical assertions. Numerical sampling is not used to establish the universal proof, which follows from the exact determinant identities and a positive quadratic denominator.

## Relationship to prior work
The classical covariance/Langevin method and the general harmonic-network transmission formula are established. Eckmann and Zabey (2003) analyze nontrivial flux in a three-oscillator *triangle*; Roy and Dhar (2007) derive currents for long ordered chains with largely uniform onsite potentials; Roy and Dhar (2008) study the effect of *number and location* of pinning centers on asymptotic size dependence in mass-disordered long chains; Saito and Dhar (2010) provide the general arbitrary-network heat-current generating formula; Falasco et al. (2015) study harmonic chains with *local baths on every site* and their energy repartition. Those primary works provide the forward framework and motivating distinction between conduction and pinning. The result here is the **explicit finite three-site conductance Lorentzian with independently variable endpoint substrate strengths, together with its exact globally optimal central stiffness, interior-to-boundary transition, and strict effect of endpoint asymmetry**. It does not claim that the general Lyapunov or Green-function treatment is new. The possibility of an earlier equivalent special-case elimination outside the inspected sources remains a historical-priority limitation.

## Limitations
This is an exact statement only for the specified classical linear finite chain with unit masses, connecting springs and terminal damping, independent Markovian baths, and freely tunable nonnegative central onsite stiffness. It does not address arbitrary friction, non-Markovian reservoirs, quantum bath spectra, mass disorder, anharmonic dynamics, noisy experimental reconstruction, or longer chains. No independent external scientific audit has been performed. The formula can be derived from known general harmonic-network methods; historical priority of the specialized optimized expression is not guaranteed by database searches.

## References
1. J.-P. Eckmann and E. Zabey, *Strange Heat Flux in (An)Harmonic Networks*, arXiv:nlin/0305006, first posted 2003-05-06, https://arxiv.org/abs/nlin/0305006.
2. D. Roy and A. Dhar, *Heat transport in ordered harmonic lattices*, arXiv:0711.4318, first posted 2007-11-27, https://arxiv.org/abs/0711.4318.
3. D. Roy and A. Dhar, *Role of pinning potentials in heat transport through disordered harmonic chains*, arXiv:0806.4693, https://arxiv.org/pdf/0806.4693.
4. K. Saito and A. Dhar, *Generating Function Formula of Heat Transfer in Harmonic Networks*, arXiv:1012.0622, first posted 2010-12-03, https://arxiv.org/abs/1012.0622.
5. G. Falasco et al., *Energy repartition for a harmonic chain with local reservoirs*, arXiv:1505.05088, first posted 2015-05-19, https://arxiv.org/pdf/1505.05088.
