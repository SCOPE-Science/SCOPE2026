# Sharp transient area-current reversal count in reversible Ornstein–Uhlenbeck networks

## Finding
For every integer \(d\ge2\), consider a stable, **reversible** Ornstein–Uhlenbeck diffusion in \(\mathbb R^d\), with a fixed symmetric positive definite drift matrix and isotropic unit-temperature noise. The transient mean signed-area rate projected onto any chosen plane is either identically zero or changes sign at most \(\binom d2-1\) times on positive time. This bound is **sharp for every dimension**, even among centered Gaussian preparations arbitrarily close to the unique equilibrium. More strongly, every prescribed set of \(\binom d2-1\) distinct positive times can be realized as precisely the simple sign-reversal times of such a projected current.

The reversals reflect relaxation of prepared cross-mode covariances. They do **not** indicate a nonequilibrium stationary probability current: all models in the theorem satisfy detailed balance at equilibrium.

## Assumptions and scope
Let \(d\ge2\), \(A\in\mathbb R^{d\times d}\) be real symmetric positive definite, and let
\[
 dX_t=-AX_t\,dt+\sqrt2\,dW_t,
\]
where \(W_t\) is standard \(d\)-dimensional Brownian motion. Assume \(X_0\) is independent of \(W\) and has finite second moment. Fix orthonormal observations \(p,q\in\mathbb R^d\), and put \(Y_t=p^\top X_t\), \(Z_t=q^\top X_t\). Define the *doubled projected signed-area rate* by
\[
 R_{p,q}(t)=\frac{d}{dt}\,\mathbb E\!\left[\int_0^t (Y_s\circ dZ_s-Z_s\circ dY_s)\right].
\]
The Stratonovich and Itô versions agree because \([Y,Z]_t=2(p^\top q)t=0\). A sign reversal means a strict change of sign across a zero at some \(t>0\). When the rate vanishes identically, the count is defined to be zero. The result concerns deterministic-time expected area production, not the random sample-path signed area, nor an equilibrium probability current.

Write \(A=U\operatorname{diag}(\lambda_1,\ldots,\lambda_d)U^\top\), with \(\lambda_i>0\), columns \(u_i\) of \(U\), and initial second-moment matrix \(M_0=\mathbb E[X_0X_0^\top]\). Define \(B=U^\top M_0U\), \(p_i=p^\top u_i\), \(q_i=q^\top u_i\). Then
\[
 R_{p,q}(t)=\sum_{1\le i<j\le d}
 (\lambda_i-\lambda_j)(p_iq_j-p_jq_i)B_{ij}
 e^{-(\lambda_i+\lambda_j)t}. \tag{1}
\]
Equal exponents are combined. In particular, repeated eigenvalues contribute zero to their own pair and cannot increase the count.

## Proof
**Exact transient expression.** The uncentered second-moment matrix satisfies
\[
 M_t=A^{-1}+e^{-At}(M_0-A^{-1})e^{-At}.
\]
The identity follows by Itô's formula from \(\dot M=-AM-MA+2I\) and holds without a zero-mean assumption. The expected projected area rate is
\[
 R_{p,q}(t)=-p^\top M_tAq+q^\top M_tAp.
\]
Since \(A\) and \(A^{-1}\) commute, the stationary contribution cancels. Diagonalizing \(A\) and symmetrizing the double sum over pairs gives (1). There are at most \(m=\binom d2\) distinct, nonzero decay modes. For \(d=2\), only one mode is possible and the sign cannot reverse.

**The zero bound.** The elementary exponential Chebyshev lemma states that any nontrivial sum \(f(t)=\sum_{j=1}^s a_j e^{-b_jt}\), with distinct real \(b_j\), has at most \(s-1\) real zeros, multiplicities counted, on any interval. Prove by induction: multiply by \(e^{b_1t}\), which preserves zero multiplicities; its derivative has at most \(s-1\) exponential terms. Were the original function to have \(s\) zeros counted with multiplicity, Rolle's theorem would force at least \(s-1\) derivative zeros, contrary to the inductive bound \(s-2\). The constant derivative special case is immediate. Applying this lemma to (1) yields at most \(m-1\) zeros and hence at most \(m-1\) strict reversals.

**Realizability at arbitrary times.** Fix distinct \(0<t_1<\cdots<t_{m-1}\). Choose pairwise distinct eigenvalues \(\lambda_i=2^i\) for \(1\le i\le d\); each unordered pair has a distinct sum by uniqueness of binary expansion. Choose an orthogonal matrix \(U\) whose first row is \(p_i=1/\sqrt d\) and second row is
\[
 q_i=\frac{i-(d+1)/2}{\sqrt{\sum_{j=1}^d(j-(d+1)/2)^2}}.
\]
These rows are orthonormal and extend to a full real orthogonal matrix. Every minor \(p_iq_j-p_jq_i\) and every eigenvalue difference is nonzero. Let \(b_1,\ldots,b_m\) enumerate the pair sums. The \((m-1)\times m\) matrix \(E_{kj}=e^{-b_j t_k}\) has rank \(m-1\): any choice of \(m-1\) of its columns is independent by the zero bound for \(m-1\) exponentials. Hence a nonzero kernel vector \(a\) defines \(f(t)=\sum_j a_je^{-b_jt}\) vanishing at all prescribed times. By the zero bound these are its only zeros and each is simple; thus each is a strict sign reversal.

For every unordered pair \(i<j\), set \(H_{ij}=H_{ji}=a_{ij}/[(\lambda_i-\lambda_j)(p_iq_j-p_jq_i)]\) and \(H_{ii}=0\). Now select the centered initial Gaussian covariance
\[
 M_0=U\bigl[\operatorname{diag}(\lambda_i^{-1})+\varepsilon H\bigr]U^\top.
\]
It is strictly positive definite whenever \(\varepsilon>0\) is sufficiently small, because the base equilibrium matrix is positive definite. Equation (1) gives \(R(t)=\varepsilon f(t)\). For every tolerance in any matrix norm, one may take \(\varepsilon\) still smaller, preserving every prescribed reversal. This proves sharpness in all dimensions, arbitrarily close to equilibrium. The choice of observations \(p=e_1,q=e_2\) involves no loss of generality: rotate the constructed coordinates to any fixed orthonormal observation plane.

**Exact three-dimensional witness.** Let
\[
 U=\frac13\begin{pmatrix}1&2&2\\2&1&-2\\2&-2&1\end{pmatrix},\qquad
 A=U\operatorname{diag}(1,2,3)U^\top
 =\frac13\begin{pmatrix}7&-2&0\\-2&6&-2\\0&-2&5\end{pmatrix}.
\]
In the eigenbasis choose the centered Gaussian initial covariance
\[
 B=\operatorname{diag}(1,1/2,1/3)+\frac1{10}
 \begin{pmatrix}0&12/25&-3/4\\12/25&0&3/2\\-3/4&3/2&0\end{pmatrix}.
\]
It is positive definite by strict diagonal dominance. For observation plane \((e_1,e_2)\), direct substitution into (1) gives
\[
 R(t)=\frac1{10}\left(\frac4{25}e^{-3t}-e^{-4t}+e^{-5t}\right)
 =\frac{e^{-3t}}{10}(e^{-t}-1/5)(e^{-t}-4/5).
\]
Thus the two **simple** positive-time reversal points are exactly \(t=\log(5/4)\) and \(t=\log5\). Both the deterministic dynamics and the stationary covariance remain detailed-balanced.

## Verification
The supplied standalone Python checker `CHECKER.py` constructs the rational example, verifies orthogonality, the explicit drift and strict covariance positivity, and compares the closed rate against direct Ornstein–Uhlenbeck covariance evolution via independent matrix exponentials at a range of times. It also numerically exercises the generic interpolation construction at dimensions three and four. The checker completed successfully in the stated environment. The all-dimension and arbitrary-time statements depend on the preceding analytic argument, not finite numerical experiments.

## Relationship to prior work
Filliger and Reimann [1] analyze the steady nonequilibrium Brownian gyrator driven by unequal bath temperatures. Here the bath is single-temperature and the drift symmetric; all stationary area rates vanish. Baldassarri and collaborators [2] examine deliberately controlled finite-time gyrator equilibration with time-dependent traps. Strang [3] reviews stationary area-production diagnostics of Ornstein–Uhlenbeck systems and gives the general transient covariance equation. The covariance solution, detailed balance, and exponential-sum zero lemma are established ingredients. The specific contribution assessed here is the all-dimension **sharp reversal count** for projected transient signed-area production in *reversible, time-independent* networks, including arbitrary prescribed reversal times near equilibrium. No claim is made that the general covariance formula or the classical Chebyshev lemma is new.

## Limitations
The diffusion matrix is a scalar multiple of identity (normalized here to \(2I\)), the drift matrix is symmetric positive definite, observations are orthogonal and fixed, and the result concerns an unconditioned mean transient rate. Nonreversible drifts, anisotropic baths, nonlinear potentials, and noise-normalized current statistics are outside the theorem. The numerical checker is not a substitute for analytic proof. The historical literature comparison is not exhaustive; a broader classical oscillation theorem applied to the covariance dynamics might provide an alternative route, so independent assessment of novelty is still desirable. Independent scientific audit has not been performed.

## References
[1] R. Filliger and P. Reimann, *The Brownian gyrator: a minimal heat engine on the nano-scale* (first public version 2007-10-19), https://arxiv.org/abs/0710.3735 .

[2] A. Baldassarri et al., *Engineered swift equilibration of a Brownian gyrator*, Physical Review E **102**, 030105 (2020), https://doi.org/10.1103/PhysRevE.102.030105 .

[3] A. Strang, *A Theoretical Review of Area Production Rates as Test Statistics for Detecting Nonequilibrium Dynamics in Ornstein–Uhlenbeck Processes* (2024), https://arxiv.org/abs/2411.07613 .
