# A universal damping-independent optimal impurity mass in a pinned Langevin trimer

## Finding

A three-site classical harmonic conductor with identical end masses and symmetric positive endpoint Langevin friction has a unique heat-current-maximizing *central* mass. With end masses normalized to one, nearest-neighbor spring stiffness \(k>0\), onsite pinning stiffness \(w>0\), and endpoint momentum damping \(\gamma>0\), the maximizer is
\[
u_* = 1+\frac{kw}{(k+w)^2}, \qquad 1<u_*\le\frac54.
\]
The choice is independent of \(\gamma\) and of the two unequal bath temperatures. Equality in the upper mass bound holds precisely for \(k=w\). This is an exact design law for the minimal nontrivial mass-impurity bridge, not an asymptotic small-disorder approximation.

## Assumptions and scope

There are three classical particles with coordinates \(q=(q_1,q_2,q_3)\), momenta \(p=(p_1,p_2,p_3)\), and masses \(M=\operatorname{diag}(1,u,1)\), with \(u>0\). All sites have the same onsite pinning stiffness \(w>0\), and nearest neighbors are coupled by two identical springs of stiffness \(k>0\). Boltzmann's constant is set to one. The Hamiltonian is
\[
H(q,p)=\frac12(p_1^2+p_2^2/u+p_3^2)+\frac{w}{2}\sum_{i=1}^3q_i^2+\frac{k}{2}[(q_1-q_2)^2+(q_2-q_3)^2].
\]
The independent white-noise Langevin reservoirs contact only sites one and three, with \(T_L>T_R\ge0\) and equal *momentum* damping \(\gamma>0\):
\[
 dq=M^{-1}p\,dt,\qquad dp=-Kq\,dt-\Gamma p\,dt+\sqrt{2\gamma T_L}\,e_1\,dW_L+\sqrt{2\gamma T_R}\,e_3\,dW_R,
\]
where
\[
K=\begin{pmatrix}w+k&-k&0\\-k&w+2k&-k\\0&-k&w+k\end{pmatrix},\qquad \Gamma=\operatorname{diag}(\gamma,0,\gamma).
\]
This convention fixes the physical meaning of damping; changing the friction parametrization with mass can define a different optimization problem. The stationary left-to-right heat current is \(j=\gamma(T_L-\mathbb E[p_1^2])\).

## Proof

**Existence and normalization.** Put \(X=(q,p)\) and write \(dX=AX\,dt+B\,dW\), with
\[
A=\begin{pmatrix}0&M^{-1}\\-K&-\Gamma\end{pmatrix},\qquad BB^{\mathsf T}=Q=\operatorname{diag}(0,0,0,2\gamma T_L,0,2\gamma T_R).
\]
The positive mechanical energy decreases along the deterministic flow at rate \(-\gamma(p_1^2+p_3^2)\). An invariant trajectory with zero dissipation must have both endpoint momenta zero. The endpoint equations then force the interior coordinate to be constant, hence also the interior momentum to be zero; since \(K\) is positive definite, the trajectory must be zero. The finite-dimensional invariance principle shows that \(A\) is Hurwitz. Thus the stationary covariance \(C\) is the unique symmetric solution of \(AC+CA^{\mathsf T}+Q=0\). At equal temperatures \(T\), the Gibbs covariance \(\operatorname{diag}(TK^{-1},TM)\) solves this equation and carries zero current. Linearity and reflection therefore reduce the current calculation to \((T_L,T_R)=(1,0)\), multiplied by \(\Delta T=T_L-T_R>0\).

**Exact covariance elimination.** Form the 21 unknown upper-triangular entries \(C_{ij}\) of a symmetric \(6\times6\) covariance, and solve the 21 corresponding upper-triangular equations of \(AC+CA^{\mathsf T}+Q=0\) by exact rational linear algebra. The complete symbolic construction, including exact substitution into all 36 matrix entries, is given in `checker.py`. Set
\[
\begin{split}
a&=k+w,\quad R=k^2+3kw+w^2,\\
B&=k^3+7k^2w+8kw^2+2w^3,\\
E&=2k^3+7k^2w+5kw^2+w^3,\\
D(u)&=\gamma^4uR+\gamma^2(a^3u^2-Bu+E)+k^4.
\end{split}
\]
The solution gives
\[
C_{p_1p_1}=T_L-\Delta T\,\frac{k^2(\gamma^2ua+k^2)}{2D(u)},
\]
and therefore exactly
\[
\boxed{j(u)=\Delta T\,\frac{\gamma k^2(\gamma^2ua+k^2)}{2D(u)}.}
\]
This is a directly checkable algebraic identity, not a fitted expression from numeric covariance solutions.

**Global optimality.** The quadratic part of \(D\) has the strictly negative discriminant
\[
B^2-4a^3E=-k^2a^2(7k^2+24kw+8w^2)<0.
\]
Since \(a^3>0\), it is positive for all real \(u\); hence \(D(u)>0\) for every \(u>0\). Exact differentiation factors as
\[
\frac{dj}{du}=-\Delta T\,\frac{\gamma^3k^2}{2D(u)^2}\,(a^2u-R)\,[\gamma^2(a^2u+R)+2k^2a].
\]
Every factor except \((a^2u-R)\) is strictly positive. The derivative therefore changes sign once, from positive to negative, at
\[
\boxed{u_*=\frac{R}{a^2}=1+\frac{kw}{(k+w)^2}.}
\]
The arithmetic-geometric mean inequality \((k+w)^2\ge4kw\) yields \(1<u_*\le5/4\), with equality at the upper bound iff \(k=w\). These inequalities cover *all* positive \(u,k,w,\gamma\), proving uniqueness and global optimality. In the normalized example \(k=w=\gamma=1\), \(\Delta T=1\), the homogeneous center gives \(j(1)=3/22\) while \(j(5/4)=1/7\), an exact current ratio \(22/21\).

## Verification

Run `python checker.py` with Python 3, SymPy, NumPy and SciPy installed. The standalone script reconstructs the exact six-dimensional drift and covariance equations, solves all 21 symmetric Lyapunov unknowns symbolically, checks all 36 residual entries identically, verifies the current and derivative formulas and negative-discriminant identity, and independently solves the numerical Lyapunov equation for twelve strictly positive parameter sets spanning a range of masses, pinning strengths and friction coefficients. The checked numerical maximum absolute flux error is below \(7\times10^{-15}\). The script tests exact examples \(j(1)=3/22\) and \(j(5/4)=1/7\) for unit spring, pinning, friction and temperature difference.

## Relationship to prior work

The finite-dimensional covariance/Lyapunov approach for harmonic chains is established, not claimed as new. Bonetto, Lebowitz and Lukkarinen (2003) analyze a different heat-bath scheme with an additional self-consistent reservoir at each interior site; a three-site endpoint-only chain has none there. Kim (2013) studies quantum Brownian harmonic chains, concentrating on bath coupling and homogeneous particle masses, not central-impurity optimization. Nicacio and collaborators (2014) analyze quantum harmonic chains with several reservoir mechanisms and a spring-mass section, without an identified theorem giving the universal center-mass choice under the classical endpoint-only Langevin convention. Pereira and Solha (2010) are substantially closer: their abstract explicitly addresses chains of alternating masses with boundary baths and mass-contrast decay. Their full article was not accessible for inspection, so it remains a material historical-priority risk; neither absence of the optimum nor incompatibility of their full formulas is asserted. The specific contribution assessed here is the global, all-damping mass optimum and its universal sharp mass bound for this specified three-site model.

## Limitations

This result is classical, linear, three-site, harmonically pinned and Markovian, with equal endpoint masses, equal endpoint momentum friction and no internal reservoir. It is not a general theorem for larger chains, asymmetric springs, quantum baths, unpinned limits or friction coefficients tied to variable mass. No independent scientific audit has been performed. Priority over every inaccessible broader exact solution is unproved.

## References

- F. Bonetto, J. L. Lebowitz and J. Lukkarinen, *Fourier's Law for a Harmonic Crystal with Self-consistent Stochastic Reservoirs*, arXiv:math-ph/0307035 (first submitted 2003-07-17). https://arxiv.org/abs/math-ph/0307035
- E. Pereira and R. B. Solha, *Some properties of the thermal conductivity of chains of oscillators*, Physical Review E 81, 062101 (2010). https://doi.org/10.1103/PhysRevE.81.062101
- I. Kim, *Heat transport through a quantum Brownian harmonic chain beyond the weak-coupling regime: An exact treatment*, arXiv:1304.1283 (first submitted 2013-04-04). https://arxiv.org/abs/1304.1283
- F. Nicacio, A. Ferraro, A. Imparato, M. Paternostro and F. L. Semiao, *Thermal transport in out of equilibrium quantum harmonic chains*, arXiv:1410.7604 (first submitted 2014-10-28). https://arxiv.org/abs/1410.7604
