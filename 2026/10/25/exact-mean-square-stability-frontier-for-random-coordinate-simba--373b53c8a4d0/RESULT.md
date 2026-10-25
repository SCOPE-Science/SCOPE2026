# Exact mean-square stability frontier for random-coordinate Simba near a quadratic minimizer

## Finding
Consider the randomized coarse-coordinate preconditioned momentum update of the Simba algorithm, specialized as in the next section. Put \(q=\ell/n\), \(0<\beta<1\), and \(s=\eta\mu/\sqrt m\). The derivative cocycle at the minimizer is exponentially mean-square stable **if and only if**
\[
0<s<\frac{2(1-\beta^2)}{1+\beta-2\beta q}.
\]
At equality its mean-square transition has spectral radius exactly one; at larger \(s\) the spectral radius is strictly greater than one. The full-coordinate case \(q=1\) has sharp bound \(2(1+\beta)\), whereas every \(q<1\) has a strictly smaller bound. In particular, if \(q<1\) stays fixed and \(\beta\uparrow1\), the stochastic ceiling is asymptotic to \(2(1-\beta)/(1-q)\), while the full-coordinate ceiling tends to four. These are statements about the linearized random dynamics, not global divergence of the nonlinear, normalized algorithm.

## Assumptions and scope
Let \(n\ge3\) and \(2\le\ell<n\) be integers. Take the strictly convex smooth quadratic \(f(x)=\mu\|x\|_2^2/2\), \(\mu>0\), in \(\mathbb R^n\). Let \(m>0\) be the eigenvalue floor, \(\eta>0\) the fixed stepsize, and \(0<\beta<1\) the momentum coefficient. At each iteration independently select \(\ell\) distinct coordinates uniformly without replacement. Form the momentum vector \(G_{k+1}=\beta G_k+\nabla f(x_k)\); restrict it to the sampled coordinates, use the inverse square root of its rank-one outer product after flooring its retained eigenvalue at \(m\), and prolong the preconditioned vector back to the full space (the source's rank-one coarse rule). Restrict initial positions and momentum to a fixed coordinate axis. The inclusion of that axis is then iid Bernoulli with probability \(q=\ell/n\); excluded steps move no coordinate. All quantities are in exact arithmetic.

Writing \(x_k\) for the active-axis position and \(y_k=G_k/\mu\) for normalized momentum gives the **exact nonlinear restricted recurrence**
\[
y_{k+1}=\beta y_k+x_k,\qquad x_{k+1}=x_k-I_k\eta\mu y_{k+1}/\max\{\mu|y_{k+1}|,\sqrt m\}.
\]
Its derivative at the equilibrium \((x,y)=(0,0)\) is \(z_{k+1}=A_{I_k}(s)z_k\), \(z_k=(x_k,y_k)^\mathsf T\), where
\[
A_0=\begin{pmatrix}1&0\\1&\beta\end{pmatrix},\qquad
A_1=\begin{pmatrix}1-s&-s\beta\\1&\beta\end{pmatrix}.
\]
"Exponentially mean-square stable" means there exist \(C<\infty\), \(r<1\) with \(\mathbb E\|z_k\|_2^2\le Cr^k\|z_0\|_2^2\) for every deterministic \(z_0\) and \(k\ge0\). Equivalently the covariance transfer operator \(\mathcal T(S)=qA_1SA_1^\mathsf T+(1-q)A_0SA_0^\mathsf T\) has spectral radius strictly below one.

## Proof
Because the rank-one coarse vector is either zero or supported on the selected active coordinate, its floored inverse-square-root multiplication gives exactly the restricted recurrence above. Near the equilibrium the floor is active, so differentiation gives the two displayed matrices. Put \(X_k=\mathbb Ex_k^2\), \(Y_k=\mathbb E(x_ky_k)\), and \(Z_k=\mathbb Ey_k^2\). A direct expansion gives
\[
\begin{pmatrix}X_{k+1}\\Y_{k+1}\\Z_{k+1}\end{pmatrix}=
M(s)\begin{pmatrix}X_k\\Y_k\\Z_k\end{pmatrix},\quad
M(s)=\begin{pmatrix}
1-2qs+qs^2&2q\beta s(s-1)&q\beta^2s^2\\
1-qs&\beta(1-2qs)&-q\beta^2s\\
1&2\beta&\beta^2
\end{pmatrix}.
\]
Exact determinant expansion yields
\[
\det(I-M(s))=qs\bigl[2(1-\beta^2)-(1+\beta-2\beta q)s\bigr].\tag{1}
\]
The map \(\mathcal T\) preserves the cone of positive-semidefinite symmetric matrices. The finite-dimensional cone Perron theorem therefore makes its spectral radius a nonnegative **real eigenvalue**. Hence whenever the radius equals one, \(M(s)\) must have the eigenvalue \(+1\); a crossing solely through a nonreal unit root or \(-1\) cannot be the first loss of mean-square stability.

At \(s=0\), the three eigenvalues are the simple numbers \(1,\beta,\beta^2\). Direct implicit differentiation of the characteristic equation (or elementary eigenvector perturbation) gives the derivative of the eigenvalue issuing from one as \(-2q/(1-\beta)<0\); the other two stay strictly inside the unit disk. Thus sufficiently small positive \(s\) is mean-square stable. Since \(1+\beta-2\beta q\ge1-\beta>0\), identity (1) has precisely one strictly positive zero, namely the stated \(s_*\). Stability cannot be lost below \(s_*\) by continuity and the cone argument. At \(s_*\), \(1\) is an eigenvalue, so the radius equals one by continuity from below. For sufficiently large \(s\), \(\operatorname{tr}M(s)=qs^2-2q(1+\beta)s+1+\beta+\beta^2\) grows unbounded and thus \(\rho(M(s))>1\). Because any return to spectral radius one above \(s_*\) would require another zero of (1), and there are none, the radius exceeds one throughout \(s>s_*\). This proves the classification.

For \(q=1\), the formula reduces algebraically to \(2(1+\beta)\). For \(q<1\), its denominator exceeds \(1-\beta\), so its bound is strictly smaller. The high-momentum asymptotic follows by expanding numerator and denominator at \(\beta=1\). For \(n=3,\ell=2,\beta=1/2\), the sharp stochastic bound is \(9/5\), while full-coordinate selection permits \(3\).

## Verification
Run `python3 verify.py` from the extracted package. It reproduces 1,403 exact-rational assertions: the determinant identity at a unisolvent grid, and independent covariance-moment expansions for both possible random updates. Both matrix sides have degree at most two in \(q\), six in \(\beta\), and three in \(s\); the rational grid spans more points than these degree bounds, so the zero-polynomial test certifies the algebraic determinant and covariance identities for all real arguments. The code also checks three exact thresholds. The universal spectral classification is proved analytically above; finite enumeration is not used in its place.

## Relationship to prior work
The Simba method of Tsipinakis and Parpas (2023, arXiv:2309.05309v1) introduces gradient-momentum outer-product preconditioning and randomized coarse-coordinate restriction, and analyzes convergence under its own stated assumptions. The precise sharp local mean-square sensitivity of its iid coarse-coordinate momentum specialization is the question studied here. Other mathematical results concerning stochastic gradient compression, Signum, error feedback, and momentum have different state equations and do not immediately imply (1). Mean-square covariance transfer, positive-cone Perron theory, and stability via spectral radius are classical ingredients, not claimed as inventions.

## Limitations
The theorem is for a single active quadratic axis, independent uniform coordinate restrictions, rank-one retained preconditioner, positive eigenvalue floor, and a fixed momentum coefficient. Local mean-square instability of the derivative cocycle does **not** establish divergence of the nonlinear clipped/floored iteration; outside the floor-active neighborhood, that iteration has a different state-dependent update. At \(s=s_*\), only failure of exponential mean-square stability is claimed, not universal growth for every initial perturbation. No direct publication-priority guarantee is asserted; equivalent formulations in stochastic-switching optimization literature may exist.

## References
- N. Tsipinakis and P. Parpas, *Simba: A Scalable Bilevel Preconditioned Gradient Method for Fast Evasion of Flat Areas and Saddle Points*, arXiv:2309.05309v1, first public 2023-09-11, https://arxiv.org/abs/2309.05309.
- J. Li, J. Lu, and W. Su, *Mean-Square Stability and Stabilizability for LTI and Stochastic Systems Connected in Feedback* (related general mean-square methodology), arXiv:2402.04074, https://arxiv.org/abs/2402.04074. The general theory, not a special-case Simba threshold, is used for context.
