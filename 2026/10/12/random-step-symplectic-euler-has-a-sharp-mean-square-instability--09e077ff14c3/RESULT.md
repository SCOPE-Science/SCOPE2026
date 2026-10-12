# Random-step symplectic Euler has a sharp mean-square instability dichotomy

## Finding

Consider independent copies \(H_0,H_1,\ldots\) of a positive step random variable \(H\) whose support is a compact subset of \((0,2)\). Apply position-first symplectic Euler to the unit-frequency harmonic oscillator, with a deterministic nonzero initial state \(z_0\). **If and only if the step law is nonconstant, there is a number \(r>1\) and positive constants \(c,C\) such that, for every integer \(n\geq0\),**

\[
c r^n\leq \mathbb E\|z_n\|_2^2\leq C r^n.
\]

The growth rate \(r\) is exactly the spectral radius of the explicit three-dimensional second-moment matrix \(M\) specified below; the same rate applies to every nonzero deterministic initial state. For a constant step, the corresponding energies are instead uniformly bounded above and below. Thus every individual step can be a stable, area-preserving elliptic update while independent, nontrivially randomized steps are exponentially unstable **in mean square** over an infinite number of steps.

For equiprobable steps \(H=h-\varepsilon\) and \(H=h+\varepsilon\), with fixed \(0<h<2\) and sufficiently small \(\varepsilon>0\), the sharp weak-randomness growth law is

\[
r(h,\varepsilon)=1+\frac{2h^2}{4-h^2}\,\varepsilon^2+O_h(\varepsilon^4).
\]

In particular, for equal-probability steps \(1/2\) and \(1\), the growth rate is the unique real root of \(64r^3-66r^2+49r-49=0\), approximately \(1.01797185386451\).

## Assumptions and scope

The continuous oscillator is \(\dot q=p,\ \dot p=-q\), with physical energy \(E(q,p)=(q^2+p^2)/2\). Its position-first symplectic Euler update at step \(h\) is

\[
z'=T(h)z,\qquad T(h)=\begin{pmatrix}1&h\\-h&1-h^2\end{pmatrix},\qquad z=(q,p)^\top.
\]

The steps are independent, identically distributed, independent of the initial state, real-valued, and supported in a compact subset \(K\subset(0,2)\). Compactness ensures all required moments and excludes the degenerate/unstable endpoints. The initial state \(z_0\in\mathbb R^2\setminus\{0\}\) is deterministic. The theorem concerns the exact-arithmetic numerical trajectory over arbitrary integer horizons, not error against the continuous solution at a fixed physical time.

Write \(m_j=\mathbb E[H^j]\) for \(j=1,2,3,4\). For \(S_n=\mathbb E[z_nz_n^\top]\) and \(v_n=(S_{n,11},S_{n,12},S_{n,22})^\top\), independence gives \(v_{n+1}=Mv_n\), where

\[
M=\begin{pmatrix}
1&2m_1&m_2\\
-m_1&1-2m_2&m_1-m_3\\
m_2&2m_3-2m_1&1-2m_2+m_4
\end{pmatrix}.
\]

## Proof

**1. Stability of each fixed step.** For every \(0<h<2\), \(\det T(h)=1\) and \(\operatorname{tr}T(h)=2-h^2\in(-2,2)\); hence its two eigenvalues are distinct complex conjugates on the unit circle. Direct multiplication gives

\[
T(h)S_hT(h)^\top=S_h,\qquad S_h=\begin{pmatrix}1&-h/2\\-h/2&1\end{pmatrix}\succ0.
\]

Every real symmetric positive-definite invariant form for this fixed map is a positive multiple of \(S_h\): the \((1,1)\) equality for a generic symmetric form \(S=(s_{ij})\) forces \(s_{12}=-hs_{22}/2\), and the \((1,2)\) equality then forces \(s_{11}=s_{22}\). The positive-definite invariant form implies that all fixed-step matrix powers, and thus all nonzero fixed-step orbit norms, are uniformly bounded above and below.

**2. A strictly positive covariance eigenmatrix.** Define the positive linear map on real symmetric matrices

\[
\mathcal F(S)=\mathbb E\big[T(H)ST(H)^\top\big].
\]

It sends nonzero positive-semidefinite matrices to nonzero positive-semidefinite matrices, because each \(T(h)\) is invertible. Normalize by trace on the compact convex set \(\{S\succeq0:\operatorname{tr}S=1\}\); Brouwer's fixed-point theorem supplies a nonzero \(S\succeq0\) and \(r>0\) satisfying \(\mathcal F(S)=rS\). This \(S\) cannot have rank one: otherwise all \(T(h)\) would preserve its real range for almost every \(h\), giving a real eigenvector for a matrix with nonreal eigenvalues. Therefore \(S\succ0\). Apply the identical argument to \(\mathcal F^*(P)=\mathbb E[T(H)^\top PT(H)]\), obtaining \(P\succ0\) and positive eigenvalue \(\widetilde r\). The trace pairing between \(P\) and \(S\) gives \(\widetilde r=r\).

**3. The sharp strictness criterion.** The determinant-one property makes \(\det(T(h)ST(h)^\top)=\det S\). Concavity of the square root of the determinant on positive two-by-two matrices yields

\[
r\sqrt{\det S}=\sqrt{\det\mathcal F(S)}\geq\mathbb E\sqrt{\det(T(H)ST(H)^\top)}=\sqrt{\det S}.
\]

Thus \(r\geq1\). If equality held, strict determinant concavity, with identical determinants of the averaging terms, would require \(T(H)ST(H)^\top=S\) almost surely. By the unique-invariant-form computation in Step 1, \(S\) must be proportional to \(S_h\) for almost every supported \(h\); since \(S_h\) depends injectively on \(h\), this is possible only when \(H\) is almost surely constant. Conversely constant steps give \(r=1\). Hence every nonconstant law has \(r>1\).

**4. Uniform growth from every state and exact rate.** The positive-definite adjoint eigenmatrix \(P\) satisfies \(\mathbb E[z_n^\top Pz_n]=r^n z_0^\top Pz_0\). Comparing \(z^\top Pz\) with \(\|z\|_2^2\) gives the stated two-sided estimate, with \(c=(z_0^\top Pz_0)/\lambda_{\max}(P)\) and \(C=(z_0^\top Pz_0)/\lambda_{\min}(P)\). Positivity and \(P\succ0\) also bound \(\mathcal F^n\) on the entire symmetric-matrix space by a constant multiple of \(r^n\), by decomposing a symmetric matrix into its positive and negative parts. Therefore \(r\) is the spectral radius of \(\mathcal F\), whose coordinate representation is exactly \(M\).

**5. Small-variance coefficient.** For the symmetric two-point law, the expected covariance map is even analytic in \(\varepsilon\). At \(\varepsilon=0\), its eigenvalue \(1\) is algebraically simple, because the other symmetric-square eigenvalues are the two nontrivial squared eigenvalues of \(T(h)\), neither equal to \(1\). Its right and left eigenmatrices may be taken as \(S_h\) and \(P_h=S_h^{-1}\). The coefficient of \(\varepsilon^2\) in \(\mathcal F_{h,\varepsilon}(S_h)\) is

\[
B_h=\begin{pmatrix}1&-2h\\-2h&3h^2-1\end{pmatrix}.
\]

First-order simple-eigenvalue perturbation in the variable \(\varepsilon^2\) gives the coefficient \(\operatorname{tr}(P_hB_h)/\operatorname{tr}(P_hS_h)=2h^2/(4-h^2)\). Analyticity and the spectral gap show this branch remains the positive-cone spectral radius for small \(\varepsilon\), proving the displayed asymptotic with an \(O_h(\varepsilon^4)\) remainder.

**6. Rational example.** Direct substitution of \(m_j=((1/2)^j+1)/2\) gives

\[
M=\begin{pmatrix}1&3/2&5/8\\-3/4&-1/4&3/16\\5/8&-3/8&9/32\end{pmatrix},
\qquad \det(rI-M)=\frac{64r^3-66r^2+49r-49}{64}.
\]

The derivative of the numerator has negative discriminant and positive leading coefficient, so the cubic is strictly increasing. Its values at \(1\) and \(21/20\) have opposite signs, proving the unique-root assertion and the growth interval.

## Verification

Run `python3 verify.py` using only the Python standard library. The script checks 107 exact-rational facts: fixed-step invariant matrices, covariance-map identities, the perturbation coefficient at 17 rational base steps, the exact rational example's moment matrix and characteristic polynomial, all two-step-law paths up to eight iterations for two initial states, and rational root isolation. Those finite checks independently replay algebra and finite products; the infinite-horizon theorem and strictness rely on Steps 2–4, not on enumeration or simulation.

## Relationship to prior work

Abdulle and Garegnani's random-time-step probabilistic integration construction (arXiv:1801.01340; first public submission 4 January 2018) motivates independent randomized time increments and proves symplecticity and conditional **finite/polynomial-horizon** Hamiltonian bounds. Its Theorem 6 has step-size, scaling, regularity and path-localization hypotheses; it does not supply uniform, all-iteration mean-square stability. The present result is compatible with that theorem and does not challenge its stated finite-horizon guarantee.

Richardson and Finn (arXiv:1108.0322, Section 2) study parametric resonance caused by **deterministic time-dependent** steps in symplectic oscillator integrators. This precedent demonstrates that geometricity alone is not a blanket energy safeguard, but does not imply the universal independent-step mean-square dichotomy or its noise coefficient. Arnold, Papanicolaou and Wihstutz (1986) study almost-sure Lyapunov exponents for a **continuously randomly forced oscillator**. Sturman and Thiffeault (2018/2019) bound Lyapunov/generalized exponents for products of random shear matrices. Neither inspected setting contains this discrete random-time-step covariance classification as a directly stated result. Standard positive-operator and determinant-concavity tools underpin the argument; novelty is claimed only for their source-specific sharp consequence and rate.

## Limitations

This statement concerns one harmonic oscillator, position-first symplectic Euler, independent identically distributed steps supported strictly inside \((0,2)\), exact arithmetic, and **second-moment** growth. It does not prove almost-sure Lyapunov positivity, apply to arbitrary symplectic integrators, cover correlated/adaptive steps, or contradict finite-time convergence bounds in the motivating literature. The proof invokes the standard strict equality case of determinant-root concavity for positive two-by-two matrices. Priority against unindexed or independently derived special cases remains a literature risk.

## References

1. A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340v1 (4 January 2018), revised v4 (2020). Sections 2 and 7, especially Lemma 5 and Theorem 6. https://arxiv.org/abs/1801.01340
2. A. S. Richardson and J. M. Finn, *Symplectic integrators with adaptive time steps*, arXiv:1108.0322 (2011), Section 2. https://arxiv.org/abs/1108.0322
3. L. Arnold, G. Papanicolaou and V. Wihstutz, *Asymptotic analysis of the Lyapunov exponent and rotation number of the random oscillator and applications*, SIAM J. Appl. Math. 46 (1986), 427–450. https://doi.org/10.1137/0146030
4. R. Sturman and J.-L. Thiffeault, *Lyapunov Exponents for the Random Product of Two Shears*, J. Nonlinear Sci. 29 (2019), 593–620; published online September 2018. https://doi.org/10.1007/s00332-018-9497-3
