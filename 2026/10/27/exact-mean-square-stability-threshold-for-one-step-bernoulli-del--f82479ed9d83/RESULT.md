# Exact Mean-Square Stability Threshold for One-Step Bernoulli-Delay Gradient Descent

## Finding

Let \(f(x)=\lambda x^2/2\), where \(\lambda>0\), and let the delay variables \(d_k\in\{0,1\}\) be independent across iterations and independent of the initial pair, with \(\mathbb{P}(d_k=1)=q\). Consider constant-step gradient descent
\[
x_{k+1}=x_k-\eta\nabla f(x_{k-d_k})=x_k-\mu x_{k-d_k},\qquad \mu=\eta\lambda>0.
\]
Define exponential mean-square stability to mean that there are constants \(C<\infty\) and \(\rho\in(0,1)\), depending on the algorithm parameters but not on the initial pair, such that
\[
\mathbb{E}[x_k^2+x_{k-1}^2]\le C\rho^k\mathbb{E}[x_0^2+x_{-1}^2]\quad\text{for every }k\ge0.
\]
Then the recursion is exponentially mean-square stable if and only if
\[
0<\mu<\mu_*(q),\qquad
\mu_*(q)=\begin{cases}
2,&q=0,\\[2pt]
\dfrac{\sqrt{1+8q}-1}{2q},&0<q\le1.
\end{cases}
\]
Equivalently, the exact stability boundary is \(q\mu^2+\mu=2\). The threshold decreases from \(2\) when no gradient is stale to \(1\) when every gradient is one step stale.

For a symmetric positive-definite quadratic \(f(x)=\tfrac12x^\top Hx\), with the same delay variable applied to the entire gradient vector, orthogonal diagonalization gives the equivalent condition \(0<\eta\lambda_{\max}(H)<\mu_*(q)\).

## Assumptions and scope

The state is scalar and real, the objective is a positive-curvature quadratic, the step size is constant and positive, and each update uses either the current iterate or exactly the immediately preceding iterate. The delay choice is iid Bernoulli with a fixed probability \(q\), and there is no additional gradient noise. The vector-valued corollary assumes a symmetric positive-definite Hessian and a common delay choice for the full gradient at each iteration. No assertion is made for correlated delays, delays of length two or more, unbounded delay distributions, stochastic gradient noise, or nonlinear objectives.

## Proof

Put \(z_k=(x_k,x_{k-1})^\top\). The two possible update matrices are
\[
A_0=\begin{pmatrix}1-\mu&0\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&-\mu\\1&0\end{pmatrix},
\]
with probabilities \(1-q\) and \(q\). For the second-moment vector
\[
m_k=\bigl(\mathbb{E}x_k^2,\mathbb{E}(x_kx_{k-1}),\mathbb{E}x_{k-1}^2\bigr)^\top,
\]
one has \(m_{k+1}=Mm_k\), where
\[
M=\begin{pmatrix}
1-2(1-q)\mu+(1-q)\mu^2&-2q\mu&q\mu^2\\
1-(1-q)\mu&-q\mu&0\\
1&0&0
\end{pmatrix}.
\]
Its characteristic polynomial is \(p(r)=r^3+ar^2+br+c\), with
\[
a=(\mu-1)(q\mu-\mu+1),\quad
b=\mu q(q\mu^2-\mu^2-\mu+1),\quad
c=-q^2\mu^3.
\]
In particular, \(p(1)=\mu(2-\mu-q\mu^2)\). Write \(s=2-\mu-q\mu^2\). If \(s<0\), then \(p(1)<0\) and \(p(r)\to+\infty\) as \(r\to+\infty\), so \(M\) has a real eigenvalue greater than \(1\). If \(s=0\), then \(1\) is an eigenvalue. In either case the second moments cannot decay exponentially for every initial state. Thus \(s>0\) is necessary.

For sufficiency, suppose \(s>0\), which implies \(0<\mu<2\), and set
\[
P=\frac1s\begin{pmatrix}
\dfrac{2(1+q\mu)}{\mu}&-2q\\
-2q&2\mu^2q^2-\mu^2q+2\mu q-\mu+2
\end{pmatrix}.
\]
Direct multiplication gives the exact identity
\[
P-(1-q)A_0^\top P A_0-qA_1^\top P A_1=I.
\]
Also \(P_{11}>0\), and
\[
\det P=\frac{2D}{\mu s^2},\quad
D=2-\mu+2\mu q(2-\mu)+\mu q^2(-\mu^2+4\mu-2)+2\mu^3q^3.
\]
For \(2-\sqrt2\le\mu<2\), the coefficient \(-\mu^2+4\mu-2\) is nonnegative, so \(D>0\). For \(0<\mu<2-\sqrt2\), that coefficient is negative and \(q^2\le q\), hence
\[
D\ge 2-\mu+\mu q(2+2\mu-\mu^2)+2\mu^3q^3>0.
\]
Therefore \(P\) is positive definite. With \(V(z)=z^\top Pz\), the identity yields
\[
\mathbb{E}[V(z_{k+1})\mid z_k]=V(z_k)-\|z_k\|^2,
\]
which implies geometric decay of \(\mathbb{E}V(z_k)\) and hence exponential mean-square stability. This proves that stability is equivalent to \(s>0\). Solving \(q\mu^2+\mu-2=0\) gives the stated threshold; the case \(q=0\) gives \(\mu_*(0)=2\) directly. For a positive-definite matrix \(H\), diagonalizing \(H\) reduces each eigenmode to the scalar recurrence, so stability holds exactly when every \(\eta\lambda_i(H)<\mu_*(q)\), equivalently when \(\eta\lambda_{\max}(H)<\mu_*(q)\).

## Verification

The proof is analytic. The included `verify_threshold.py` checks the Lyapunov identity using exact rational arithmetic at representative stable points, checks the characteristic-polynomial sign at a rational unstable point, and confirms the boundary value \(\mu_*(1/2)=\sqrt5-1\) numerically. These finite checks are supplementary and do not substitute for the all-parameter proof.

## Relationship to prior work

Arjevani, Shamir, and Srebro analyze delayed gradient descent with a fixed delay \(\tau\) and give finite-time convergence bounds. The endpoint cases here agree with the familiar fixed-delay models: \(q=0\) is no delay and \(q=1\) is a deterministic one-step delay. Their fixed-delay recurrence does not itself yield the exact necessary-and-sufficient boundary for the iid mixture \(0<q<1\). The present result is a distribution-specific mean-square stability classification, not a general delayed-SGD convergence-rate theorem.

## Limitations

The exact threshold depends on the iid two-point delay law and on deterministic gradients of a quadratic objective. The result does not imply the same formula for a general delay distribution, temporally correlated delays, coordinate-wise asynchronous updates, stochastic gradient noise, or nonlinear objectives. The stability boundary is strict: at equality the covariance operator has eigenvalue \(1\), so exponential mean-square stability fails.

## References

1. Y. Arjevani, O. Shamir, and N. Srebro, “A Tight Convergence Analysis for Stochastic Gradient Descent with Delayed Updates,” Proceedings of ALT 2020, PMLR 117, 111–132; arXiv:1806.10188v1 (first public 2018-06-26).
2. “Towards Understanding the Generalizability of Delayed Stochastic Gradient Descent,” arXiv:2308.09430v1 (related-work source; abstract inspected).
