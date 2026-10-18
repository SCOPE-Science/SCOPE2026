# Dimension-sharp mixing slowdown in a trace-preserving exponential Lindblad step

## Finding

For each \(n\ge2\), the completely positive, trace-preserving full-rank exponential Euler (FREE) step for a uniformly driven directed quantum jump cycle has an exactly computable Hilbert--Schmidt mixing factor. Despite an exact unique stationary state and unconditional positivity, it can relax exponentially more slowly than the corresponding continuous Lindblad dynamics as the step grows. There are sharp dimensional thresholds: full-matrix contraction is strictly worse after \(\gamma\tau>\log3\) in dimension two, after \(\gamma\tau>\log2\) in dimension three, and at every positive step in dimensions four and above.

More precisely, set \(x=\gamma\tau\), \(q=e^{-x}\), and \(a_n=1-\cos(2\pi/n)\). If \(\Pi(X)=\operatorname{tr}(X)I_n/n\), then
\[
\alpha_n(x):=\|\Phi_\tau-\Pi\|_{2\to2}=\max\left\{q,\sqrt{1-2a_nq(1-q)}\right\},\qquad
\beta_n(x):=\|e^{\tau\mathcal L}-\Pi\|_{2\to2}=e^{-x\min\{1,a_n\}}.
\]
The norm is induced by the matrix Hilbert--Schmidt norm, acting on all complex matrices; it also gives the sharp norm on the invariant real space of traceless Hermitian matrices. In each case \(\alpha_n\ge\beta_n\), with equality exactly for \(n=2\) and \(0<x\le\log3\), or \(n=3\) and \(0<x\le\log2\).

For fixed \(n\), the large-step contraction satisfies
\[
\alpha_n(x)=1-a_ne^{-x}+O_n(e^{-2x}),\qquad
\beta_n(x)=e^{-x\min\{1,a_n\}}.
\]
Thus the numerical inverse logarithmic contraction per step is asymptotic to \(e^x/a_n\). The worst-case single-step trace-norm difference has the sharp limit
\[
\lim_{x\to\infty}\ \sup_{\rho\succeq0,\ \operatorname{tr}\rho=1}
\left\|\Phi_{x/\gamma}(\rho)-e^{(x/\gamma)\mathcal L}(\rho)\right\|_1
=2\left(1-\frac1n\right).
\]
The last value approaches the maximal possible distance between quantum states as the dimension grows.

## Assumptions and scope

Work in \(\mathbb C^n\) with an orthonormal basis indexed by \(j=0,\ldots,n-1\), interpreting indices cyclically. The Hamiltonian is zero, every jump has the same fixed rate \(\gamma>0\), and
\[
L_j=|j+1\rangle\langle j|,\qquad
\mathcal L(\rho)=\gamma\sum_{j=0}^{n-1}L_j\rho L_j^\dagger-\frac\gamma2\sum_j\{L_j^\dagger L_j,\rho\}.
\]
Because \(\sum_jL_j^\dagger L_j=I_n\), this is \(\mathcal L=\gamma(\mathcal J-\mathcal I)\) with \(\mathcal J(\rho)=\sum_jL_j\rho L_j^\dagger\). The full-rank method is the exact-integral map in equation (2.6) of Chen et al., not a low-rank, truncated-quadrature, or floating-point implementation. Define \(\Pi(\rho)=\operatorname{tr}(\rho)I_n/n\). All matrix and superoperator formulas use exact arithmetic.

## Proof

**Reduction to one-jump dynamics.** The no-jump operator from the FREE construction is \(A=-\gamma I_n/2\). Substitution into the method's integral gives, for every matrix \(\rho\),
\[
\Phi_\tau(\rho)=e^{-\gamma\tau}\rho+\gamma\int_0^\tau e^{-\gamma s}ds\sum_jL_j\rho L_j^\dagger
=q\rho+(1-q)\mathcal J(\rho).
\]
This is a convex combination of channels and therefore is completely positive and trace preserving. The exact propagator is \(e^{x(\mathcal J-\mathcal I)}\).

**Normal Fourier decomposition.** The Hilbert--Schmidt matrix space splits orthogonally into the scalar identity, diagonal trace-zero matrices, and off-diagonal matrices. On diagonal matrices, \(\mathcal J\) is the directed-cycle permutation \(P_n\); its eigenvalues are \(\zeta_n^k=e^{2\pi i k/n}\). On every off-diagonal matrix, \(\mathcal J\) is zero. It is thus normal. Its eigenvalue \(1\) appears only on scalar matrices; both maps have the unique stationary density \(I_n/n\). The numerical and exact eigenvalues on the other diagonal modes are respectively \(q+(1-q)\zeta_n^k\) and \(e^{x(\zeta_n^k-1)}\); on the off-diagonal modes both are \(q\). The largest diagonal numerical modulus occurs for \(k=1\) or \(k=n-1\), and its square is \(1-2a_nq(1-q)\). The largest exact diagonal modulus is \(e^{-a_nx}\). This proves the two displayed exact formulas for \(\alpha_n\) and \(\beta_n\).

**Sharp dimensional comparison.** For any \(n\ge3\) one has \(0<a_n\le3/2\). Put
\[
F_a(q)=1-2aq(1-q)-q^{2a},\qquad 0<q<1.
\]
For \(0<a\le3/2\), the exponent \(2a-1\le2\), so \(q^{2a-1}\ge q^2\) and
\[
F_a'(q)=2a(2q-1-q^{2a-1})\le-2a(1-q)^2<0.
\]
As \(F_a(1)=0\), it follows that \(F_a(q)>0\) for every \(q<1\). Hence the numerical diagonal factor strictly exceeds the exact diagonal factor in every dimension at least three. For \(n\ge5\), \(a_n<1\) and the exact full-space factor is the diagonal factor, so \(\alpha_n>\beta_n\). For \(n=4\), \(a_n=1\), and the same argument gives strict inequality over the exact factor \(q\).

For \(n=3\), \(a_n=3/2\) and the exact full-space factor is the *off-diagonal* factor \(q\), while
\[
(1-3q(1-q))-q^2=(1-q)(1-2q).
\]
Thus the maximum is strictly greater than \(q\) exactly when \(q<1/2\), equivalently \(x>\log2\); otherwise it equals \(q\). For \(n=2\), \(a_n=2\), the exact factor is also \(q\), and
\[
(1-4q(1-q))-q^2=(1-q)(1-3q).
\]
Consequently strict inequality occurs exactly at \(q<1/3\), or \(x>\log3\). Equalities at the threshold points follow directly from these factorizations.

**Stiff-step and sharp trace distance.** Expansion at \(q=0\) gives \(\sqrt{1-2a_nq(1-q)}=1-a_nq+O_n(q^2)\); this dominates \(q\) for sufficiently small \(q\). In the strong-step limit \(\Phi_\tau\to\mathcal J\), whereas the exact semigroup tends in every operator norm to \(\Pi\), since its only nondecaying Fourier eigenvalue is the scalar one. The channel \(\mathcal J\) maps density matrices onto all diagonal density matrices (with cyclically permuted diagonal). For any diagonal density matrix \(D\), convexity of the trace norm on the probability simplex yields \(\|D-I_n/n\|_1\le2(1-1/n)\), with equality for a basis-state projector. Finite dimensionality makes both channel limits uniform on density matrices, proving the asserted sharp trace-norm limit.

## Verification

The accompanying standalone file `checker.py` reproduces 341 symbolic and numerical checks with SymPy, NumPy and SciPy. It tests the exact two- and three-state threshold identities, direct finite-dimensional FREE superoperator matrices and matrix exponentials, the full Hilbert--Schmidt norms for dimensions two through nine, and the large-step asymptotics and sharp trace-distance witnesses. No finite set of experiments is used to prove the statements for all dimensions, all steps, or all density matrices; those claims follow from the preceding Fourier and inequality arguments.

## Relationship to prior work

Chen et al. (2024) introduce the positivity- and trace-preserving full-rank exponential Euler map and prove consistency/error bounds; their equation (2.6) is the starting point, not a new algorithm here. Cao and Lu (2021) study other Kraus-operator-based structure-preserving schemes, explicitly excluding stiffness from their main analysis. The Fourier spectrum of a directed cycle and the Poissonization of jump chains are standard mathematical tools. What is singled out here is the exact full-density-matrix dimensional contraction classification, the sharp two-versus-three-versus-four-state boundaries, and the limiting worst-case trace-distance degradation for the stated integrator. Earlier Markov and Lindblad work may yield related special cases through reductions, so publication-priority verification beyond the inspected sources remains appropriate.

## Limitations

The theorem only treats a zero-Hamiltonian, equal-jump-rate cyclic family and the exact full-rank first-order map. Its large-step limit diagnoses a stiff-step error; it does not contradict small-step convergence or bounds derived with a fixed final time and shrinking step size. The norm comparison is in the Hilbert--Schmidt induced operator norm, not an unrestricted assertion about every individual initial state. No statement is made about low-rank compression, quadrature error, arbitrary nonuniform jumps, external drive, or later independent review.

## References

1. H. Chen, A. Borzì, D. Janković, J.-G. Hartmann, and P.-A. Hervieux, *Full- and low-rank exponential Euler integrators for the Lindblad equation*, arXiv:2408.13601, first version 2024-08-24; equation (2.6), sections 3--5. https://arxiv.org/abs/2408.13601
2. Y. Cao and J. Lu, *Structure-preserving numerical schemes for Lindblad equations*, arXiv:2103.01194, first version 2021-03-01; sections 2--3. https://arxiv.org/abs/2103.01194
3. L. Boczkowski, Y. Peres, and P. Sousi, *Sensitivity of mixing times in Eulerian digraphs*, SIAM Journal on Discrete Mathematics 32 (2018). https://doi.org/10.1137/16M1073376
