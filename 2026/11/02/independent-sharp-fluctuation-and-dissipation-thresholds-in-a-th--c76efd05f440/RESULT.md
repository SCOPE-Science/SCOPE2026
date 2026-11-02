# Independent sharp fluctuation and dissipation thresholds in a three-dimensional skew Langevin chain

## Finding
For a three-coordinate Ornstein–Uhlenbeck chain with adjacent antisymmetric couplings \(b>0\) and \(q>0\), and extra damping \(h\geq0\) acting only on its first coordinate, the stationary total variance \(V(h)\) and stationary entropy production rate \(\Phi(h)\) have **independent sharp monotonicity thresholds**. The variance decreases strictly for all \(h\geq0\) if and only if \(b\leq1\); for \(b>1\), it has exactly one positive global minimizer and increases back to its residual limit. The entropy production decreases strictly for all \(h\geq0\) if and only if \(q\leq2\); for \(q>2\), it has exactly one positive global minimizer and increases back to its residual limit. Consequently all four combinations (both monotone; variance-only re-entrance; dissipation-only re-entrance; both re-entrant) occur in one stable, single-bath model. The dissipation minimizer is explicitly
\[
h_{\Phi}=\frac{b^2+q^2+4}{q-2},\qquad
\Phi(h_{\Phi})=2q^2-\frac{2b^2(q-2)^2}{b^2+4q},
\]
when \(q>2\), while the unique variance minimizer is the positive zero of the explicit quartic given below.

## Assumptions and scope
Every coordinate is even under time reversal. Let \(W_t\) be standard three-dimensional Brownian motion, \(b,q>0\), and \(h\geq0\). Consider
\[
dX_t=M_hX_t\,dt+\sqrt2\,dW_t,\quad
M_h=\begin{pmatrix}-(1+h)&b&0\\-b&-1&-q\\0&q&-1\end{pmatrix}.
\]
Its symmetric drift part is \(-I-h e_1e_1^{\mathsf T}\), so it is Hurwitz for every admitted parameter and has a unique centered stationary Gaussian density \(p_h\) with positive-definite covariance \(S_h\) satisfying \(M_hS_h+S_hM_h^{\mathsf T}=-2I\). Define \(V(h)=\operatorname{tr}(S_h)\) and, in the unit-diffusion normalization,
\[
\Phi(h)=\int_{\mathbb R^3}\frac{\|j_h(x)\|^2}{p_h(x)}\,dx,\quad j_h(x)=(M_h+S_h^{-1})x p_h(x).
\]
This is the standard steady-state probability-current entropy production when all three variables are even. The model also arises as the normalized difference mode of two identical copies with reciprocal diffusive coupling of strength \(h/2\) on the first coordinate: subtracting the two copy equations produces precisely the extra drift \(-h e_1e_1^{\mathsf T}\). It is not an assertion about odd-variable thermodynamic parity or nonlinear systems.

## Proof
Write \(B=b^2>0\), \(Q=q^2>0\), and
\[
D(h)=(B+(Q+1)(h+1))\bigl(Bh+2B+2h^2+8h+2Q+8\bigr)>0.
\]
Solving the six stationary Lyapunov equations gives
\[
S_{11}(h)=\frac{P(h)}{D(h)},\quad
P(h)=2B^2+B\bigl((3Q+5)h+4Q+10\bigr)+2(Q+1)h^2+8(Q+1)h+2Q^2+10Q+8.
\]
Taking traces in the Lyapunov equation directly gives \(V(h)+h S_{11}(h)=3\), so the **exact variance** is
\[
V(h)=3-\frac{hP(h)}{D(h)}.
\]
In particular \(V(0)=3\), \(V'(0)=-1\), and
\[
V(h)=2+\frac{1-B}{h}+O(h^{-2})\quad(h\to\infty).
\]
Differentiating this expression and collecting powers of \(h\) gives \(V'(h)=-T(h)/D(h)^2\), where \(T(h)=\sum_{j=0}^4 c_jh^j\), with
\[
\begin{aligned}
c_4&=4(1-B)(Q+1)^2,\\
c_3&=4(Q+1)\bigl(8(Q+1)-B^2-BQ+B\bigr),\\
c_2&=B^3(Q-1)+B^2(5Q^2+26Q+25)\\
&\quad+B(4Q^3+56Q^2+156Q+104)+8Q^3+112Q^2+200Q+96,\\
c_1&=4(B+Q+1)(B+Q+4)(3BQ+5B+8Q+8),\\
c_0&=4(B+Q+1)^2(B+Q+4)^2.
\end{aligned}
\]
For \(0<B\leq1\), all five coefficients are nonnegative and \(c_0,c_1,c_2,c_3>0\): the only possibly negative monomial is \(B^3(Q-1)\), and \(B^2(25-B)>0\) absorbs it. Thus \(T(h)>0\) for \(h\geq0\). For \(B>1\), \(c_4<0\) and \(c_0,c_1>0\). If \(c_2\leq0\), necessarily \(0<Q<1\) and \(B>25\), as all remaining terms in \(c_2\) are positive. In this case \(c_3<0\) because \(B^2-B>600>8(Q+1)\) while \(BQ>0\). Therefore the nonzero coefficient sequence of \(T\), in descending powers, has exactly one sign change: if \(c_2>0\), any sign of \(c_3\) is allowed; if \(c_2\leq0\), then \(c_3<0\). Descartes' rule of signs gives at most one positive root. Since \(T(0)>0\) and \(T(h)\to-\infty\), a positive root exists, is unique, and changes the sign of \(V'\) from negative to positive.

Set \(\mathcal Q_h=(M_hS_h-S_hM_h^{\mathsf T})/2\). The steady Gaussian current and Lyapunov identity imply \(M_h+S_h^{-1}=\mathcal Q_hS_h^{-1}\), so
\[
\Phi(h)=\operatorname{tr}\bigl(\mathcal Q_h^{\mathsf T}\mathcal Q_h S_h^{-1}\bigr)
=\frac{4\bigl(B^2+2Bh+2BQ+4B+h^2Q+4hQ+Q^2+4Q\bigr)}{Bh+2B+2h^2+8h+2Q+8}.
\]
Exact differentiation yields
\[
\Phi'(h)=-\frac{4B\,[B+Q+4+(2-q)h]\,[B+Q+4+(2+q)h]}{(Bh+2B+2h^2+8h+2Q+8)^2}.
\]
The second bracket and denominator are strictly positive. The first bracket is positive for every \(h\geq0\) if \(q\leq2\), whereas for \(q>2\) it crosses zero exactly at \(h_{\Phi}\), proving the dissipation classification. Direct substitution gives the stated minimum and \(\Phi(0)=2(B+Q)\), \(\lim_{h\to\infty}\Phi(h)=2Q\). Independently selecting \(b\) on either side of \(1\) and \(q\) on either side of \(2\) produces the four asserted regimes, without changing noise temperature or drift stability. \(\square\)

## Verification
`verify.py` independently constructs the symmetric stationary covariance by solving all six Lyapunov equations, computes the Gaussian current and entropy-production trace, and checks the exact variance, dissipation, both derivatives, their factorization and boundary values symbolically in SymPy. It also checks exact-rational parameter cases straddling each transition. Running `python verify.py` requires Python 3 and SymPy. Finite examples supplement, but do not prove, the global Descartes-sign argument given above.

## Relationship to prior work
Kharbanda, Burnet and Sabass (2026) establish the residual-current mechanism and strong-coupling entropy-production behavior for general linear Langevin systems; their paper already explains why higher-dimensional EPR can approach its residual limit from below and includes four-dimensional examples. None of those generic mechanisms is claimed as new. Godrèche and Luck (2018) give general multivariate OU stationary-state and irreversibility formulae and explicitly tabulate a three-site asymmetric Gaussian spin chain in their Section 4.4. Its fixed-diagonal, asymmetric nearest-neighbor drift is not the present independently parameterized skew chain with one tunable diagonal damping. Both the general formulas and that three-site example are prior work. The present claim is the **exact joint global classification** for the elementary three-site skew chain, including the independent and sharp \(b=1\) variance and \(q=2\) EPR boundaries and the uniqueness of both finite-coupling minima. Known OU formulae are sufficient starting points but their cited statements do not themselves provide these inequalities or the quartic-sign argument. A related exact three-dimensional EPR calculation for a different, non-skew drift is known; it does not yield this joint variance-versus-dissipation theorem by substitution.

## Limitations
This is a specific normalized, isotropically forced three-dimensional linear model with even variables. It does not assert universality over arbitrary OU matrices, detailed-balance thermal parity models, nonlinear interactions, or all covariance functionals. General stochastic linear-systems theory could in principle subsume the elementary algebra; publication priority requires further external expert review. The stationary total variance is a fluctuation proxy, not a thermodynamic free energy. The independent audit has not been performed.

## References
1. V. Kharbanda, A. F. Burnet, and B. Sabass, *Residual dynamics determine dissipation in strongly coupled linear Langevin systems*, arXiv:2610.37030v1 (first submitted 2026-10-27). https://arxiv.org/html/2610.37030v1
2. C. Godrèche and J.-M. Luck, *Characterising the nonequilibrium stationary states of Ornstein-Uhlenbeck processes*, arXiv:1807.00694 (2018). https://arxiv.org/abs/1807.00694
3. L. P. Dadhichi and K. Kroy, *Time-reversal symmetries and equilibriumlike Langevin equations*, Phys. Rev. E 107, 044106 (2023). https://doi.org/10.1103/PhysRevE.107.044106
