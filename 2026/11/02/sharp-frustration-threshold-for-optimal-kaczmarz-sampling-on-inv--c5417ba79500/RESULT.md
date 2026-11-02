# Sharp frustration threshold for optimal Kaczmarz sampling on inverse-Gram cycles

## Finding

For every integer \(n\ge5\), a normalized square Kaczmarz system whose inverse row Gram matrix consists of a positive path and one negative closing edge admits a uniquely optimal *fixed independent* row-sampling distribution. A rank-one/rank-two transition occurs exactly at the closing-edge strength \(t=1/(n-1)\), and an explicit sine-ratio law determines every optimum above that threshold.

## Assumptions and scope

Let \(B\in\mathbb R^{n\times n}\) be real and invertible, with all rows \(b_i^{\mathsf T}\) of Euclidean norm one. Set the positive-definite inverse row Gram matrix \(C=(BB^{\mathsf T})^{-1}\). Suppose its only off-diagonal nonzero entries are \(C_{i,i+1}=C_{i+1,i}=w>0\), for \(1\le i<n\), and \(C_{1,n}=C_{n,1}=-tw\), for \(t>0\). Write \(\ell=n-1\). For \(0<t\le1/\ell\), put \(\theta=0\). For \(t>1/\ell\), let \(\theta\in(0,\pi/\ell)\) be the unique solution of
\[
\sin\theta=t\sin(\ell\theta).
\]
Define
\[
q_1=C_{11}+w(\cos\theta-t\cos(\ell\theta)),\quad
q_n=C_{nn}+w(\cos\theta-t\cos(\ell\theta)),
\]
\[
q_i=C_{ii}+2w\cos\theta\quad(2\le i\le n-1),\qquad
T=\sum_{i=1}^nq_i=\operatorname{tr}C+2w(\ell\cos\theta-t\cos(\ell\theta)).
\]
Then the **unique fixed iid optimal row probabilities** for the sharp worst-direction expected squared-error decrement are \(p_i=q_i/T\). The maximal possible worst-direction expected one-step decrement is \(1/T\), equivalently the minimal sharp worst-direction expected squared-error contraction is \(1-1/T\). The optimal semidefinite slack has nullity one for \(t<1/\ell\) and nullity two for \(t\ge1/\ell\). Such unit-row matrices exist for every \(n\ge5\) and every \(t>0\) when \(w>0\) is sufficiently small. No claim is made about multistep, adaptive, inconsistent or overdetermined Kaczmarz systems.

## Proof

**Exact SDP equivalence.** The normalized row-projection error satisfies \(e^+=e-(b_i^{\mathsf T}e)b_i\). Thus the conditional expectation of the squared error is
\[
\mathbb E_p\|e^+\|^2=\|e\|^2-e^{\mathsf T}B^{\mathsf T}\operatorname{diag}(p)Be.
\]
Its sharp worst-direction decrement is \(\lambda_{\min}(B^{\mathsf T}\operatorname{diag}(p)B)\). Since \(B\) is invertible, the matrix inequality \(B^{\mathsf T}\operatorname{diag}(p)B\succeq\gamma I\) is equivalent to \(\operatorname{diag}(p)\succeq\gamma C\). Rescaling \(q=p/\gamma\) gives the exact primal and dual SDPs
\[
\min_{q}\{\mathbf1^{\mathsf T}q:\operatorname{diag}(q)-C\succeq0\}
=\max_{X\succeq0,\,X_{ii}=1}\langle C,X\rangle.
\]
Strong duality follows from strict primal feasibility using a sufficiently large diagonal and strict dual feasibility at \(X=I\). Feasible \(q\) is automatically positive because \(q_i\ge C_{ii}>0\). At any optimum the original sharp decrement is the reciprocal of the minimizing trace.

**Sine-ratio uniqueness.** For \(0<\theta<\pi/\ell\), the function \(\sin\theta/\sin(\ell\theta)\) is strictly increasing, with endpoint limits \(1/\ell\) and infinity. Indeed its logarithmic derivative is \(\cot\theta-\ell\cot(\ell\theta)>0\), because \(u\mapsto u\cot u\) decreases on \((0,\pi)\). Hence the prescribed positive angle exists and is unique exactly above the critical strength.

**Weak negative edge.** For \(0<t\le1/\ell\) the proposed slack \(S=\operatorname{diag}(q)-C\) is
\[
S=w\bigl(L(P_n)-t(e_1-e_n)(e_1-e_n)^{\mathsf T}\bigr),
\]
where \(L(P_n)\) denotes the unit-weight path Laplacian. Cauchy–Schwarz yields \((x_n-x_1)^2\le\ell\sum_{i=1}^{\ell}(x_{i+1}-x_i)^2\), proving \(S\succeq0\). The constant vector belongs to the kernel, and the rank-one correlation matrix \(X=\mathbf1\mathbf1^{\mathsf T}\) satisfies \(\langle C,X\rangle=T\). Equality of the primal and dual objective establishes the optimum. Equality in the energy estimate gives nullity one for \(t<1/\ell\); at equality, affine path sequences give nullity two.

**Strong negative edge: dual and stationarity.** For \(t>1/\ell\), put \(\phi=\ell\theta\), and take planar unit vectors \(v_i=(\cos((i-1)\theta),\sin((i-1)\theta))\). Their Gram matrix \(X_{ij}=v_i\cdot v_j\) is dual feasible, rank two, and has the objective
\[
\langle C,X\rangle=\operatorname{tr}C+2w(\ell\cos\theta-t\cos\phi)=T.
\]
The proposed slack annihilates both coordinate columns of these vectors: this is the three-term trigonometric recurrence at interior vertices and the relation \(\sin\theta=t\sin\phi\) at the endpoints. Thus \(SX=0\).

**Global positivity via a discrete Dirichlet problem.** For real \(x\), define
\[
E_\theta(x)=\sum_{i=1}^{\ell}\bigl[\cos\theta(x_i^2+x_{i+1}^2)-2x_ix_{i+1}\bigr].
\]
Then
\[
\frac{x^{\mathsf T}Sx}{w}=E_\theta(x)-t\cos\phi(x_1^2+x_n^2)+2t x_1x_n.
\]
For fixed endpoints, the Hessian on the \(n-2\) interior variables is the Dirichlet tridiagonal with positive eigenvalues \(2\cos\theta-2\cos(k\pi/\ell)>0\), for \(1\le k\le\ell-1\), since \(\theta<\pi/\ell\). The unique interior minimizer is
\[
x_j^*=\frac{\sin((n-j)\theta)x_1+\sin((j-1)\theta)x_n}{\sin\phi},\qquad 2\le j\le n-1.
\]
Substituting and simplifying gives the exact boundary energy
\[
\min E_\theta=\frac{\sin\theta}{\sin\phi}\bigl[\cos\phi(x_1^2+x_n^2)-2x_1x_n\bigr]
=t\bigl[\cos\phi(x_1^2+x_n^2)-2x_1x_n\bigr].
\]
It cancels the remaining boundary terms in the slack quadratic form, proving \(S\succeq0\) for **all** dimensions and all strong-edge parameters, with kernel dimension exactly two. Therefore the explicit primal and dual feasible objectives both equal \(T\), proving global sharpness and the claimed rank transition.

**Uniqueness.** For any other primal optimum \(q'\), complementary slackness with the fixed dual optimizer forces \((\operatorname{diag}(q')-C)\mathbf1=0\) in the lower-strength regime and \((\operatorname{diag}(q')-C)v^{(a)}=0\) for both planar coordinate columns in the upper-strength regime. Each coordinate of the constant vector, or at least one coordinate of each nonzero planar unit vector, is nonzero. Thus every diagonal entry \(q_i'\) equals the prescribed \(q_i\). This also works at threshold using the rank-one dual certificate. Hence the probabilities are unique.

**Nonvacuity of the normalization.** At \(w=0\), take \(C=I\). With the off-diagonal entries fixed to \(w\) and \(-tw\), the Jacobian of the map from the diagonal entries of \(C\) to \(\operatorname{diag}(C^{-1})\) equals \(-I\) at \(w=0\). The implicit-function theorem therefore produces, for every fixed \(n\) and \(t>0\), positive-definite matrices with the specified off-diagonals and \(\operatorname{diag}(C^{-1})=\mathbf1\) for sufficiently small \(w>0\). A Cholesky factor of \(C^{-1}\) supplies the required unit-row \(B\).

## Verification

The standalone `verify_signed_cycle.py` program uses Python 3 standard libraries only to build normalized unit-row instances, recompute the candidate slack eigenvalues and nullities, dual certificates, and direct Kaczmarz expected one-step decrement. It checks independently assembled instances in dimensions \(5\le n\le12\) with parameters below, at and above the threshold. The analytic proof above establishes the infinite theorem; no finite test is asserted to prove it.

## Relationship to prior work

Dai, Soltanalian and Pelckmans (2014) supply an optimization-based randomized Kaczmarz framework, but the inspected full text does not evaluate the signed-cycle inverse-Gram optimum. Agaskar, Wang and Lu (2014) optimize an annealed multistep MSE spectral exponent, which differs mathematically from maximizing the sharp one-step worst-direction decrement here. Strohmer and Vershynin (2007) provide the standard randomized Kaczmarz convergence setting rather than this optimizer. Zelazo and Bürger (2014) give a negative-edge effective-resistance criterion, which explains the weak-edge threshold but not the beyond-threshold unique sampling law. General cycle elliptope descriptions and positive-definite cycle completion results treat broader correlation feasibility, not an evaluated optimal probability vector. A separately established four-variable special case is excluded: this theorem starts at \(n=5\), proves the entire dimension-uniform family, and uses nontrivial trigonometric Dirichlet interpolation.

## Limitations

Only real invertible square systems with normalized rows and the stated *inverse*-Gram sparsity are considered. These one-step expected-squared-error optimization results do not establish multistep or adaptive optimality. The verifier uses finite floating-point calculations with tolerances; its tests are not a universal proof. Older specialist literature, including the full 1993 simple-cycle matrix-completion paper and a 2014 optimal-sampling conference contribution, was not fully accessible, leaving historical overlap risk. Independent mathematical validation has not been performed.

## References

1. L. Dai, M. Soltanalian, K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863v1 (first public 2014-02-12), https://arxiv.org/abs/1402.2863.
2. T. Strohmer, R. Vershynin, *A Randomized Kaczmarz Algorithm with Exponential Convergence*, arXiv:math/0702226v1, https://arxiv.org/abs/math/0702226.
3. D. Zelazo, M. Bürger, *On the Definiteness of the Weighted Laplacian and Its Connection to Effective Resistance*, arXiv:1408.2187v1, https://arxiv.org/abs/1408.2187.
4. W. W. Barrett, C. R. Johnson, P. Tarazaga, *The Real Positive Definite Completion Problem for a Simple Cycle*, Linear Algebra and Its Applications 192 (1993), 3–31 (original full text not inspected).
5. M. Laurent, F. Mascarin, S. Telen, *The Algebraic Boundary of Graph Elliptopes*, arXiv:2605.02484v1, https://arxiv.org/abs/2605.02484 (later comparison only).

6. A. Agaskar, C. Wang, Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP 2014, pp. 389–393, https://doi.org/10.1109/GlobalSIP.2014.7032145 (lawful full text: https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content).
