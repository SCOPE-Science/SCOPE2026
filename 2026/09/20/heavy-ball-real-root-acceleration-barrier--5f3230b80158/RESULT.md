# Uniform real-root barrier for fixed-parameter heavy-ball acceleration

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Consider the strongly convex quadratic family
\[
f(x)=\tfrac12 x^\top A x-b^\top x,
\qquad \mu I\preceq A\preceq L I,
\qquad 0<\mu<L,
\]
and fixed-parameter heavy-ball iteration
\[
x_{k+1}=x_k-\alpha\nabla f(x_k)+\beta(x_k-x_{k-1}),
\qquad \alpha>0,\quad 0\le \beta<1.
\]
For a scalar curvature \(\lambda\in[\mu,L]\), the error obeys
\[
z_{k+1}=(1+\beta-\alpha\lambda)z_k-\beta z_{k-1},
\]
with characteristic polynomial
\[
p_\lambda(r)=r^2-s_\lambda r+\beta,
\qquad s_\lambda=1+\beta-\alpha\lambda.
\]
Write \(r_\pm(\lambda)\) for its roots and define the interval-robust asymptotic factor
\[
\rho_{[\mu,L]}(\alpha,\beta)
=\sup_{\lambda\in[\mu,L]}\max\{|r_+(\lambda)|,|r_-(\lambda)|\}.
\]
This is the worst modal spectral radius over the full class of quadratic curvatures consistent with the spectral bounds.

### Theorem 1: real-root acceleration barrier

Assume that every characteristic polynomial on the entire spectral interval has real roots:
\[
(1+\beta-\alpha\lambda)^2-4\beta\ge0
\qquad\text{for all }\lambda\in[\mu,L].
\]
Then
\[
\boxed{
\rho_{[\mu,L]}(\alpha,\beta)
\ge \frac{L-\mu}{L+\mu}.
}
\]
Moreover, equality is possible only for
\[
\boxed{
\beta=0,
\qquad
\alpha=\frac{2}{L+\mu},
}
\]
which is the optimal fixed-step gradient-descent choice.

Thus, for interval-robust fixed heavy-ball tuning, any strict improvement over the optimal gradient-descent factor
\[
q_{\rm GD}=\frac{L-\mu}{L+\mu}
\]
forces a nonempty curvature interval on which the heavy-ball characteristic roots are a complex-conjugate pair.

This statement is about the full curvature interval, not merely the eigenvalues of one particular finite matrix. A concrete matrix whose spectrum skips the complex-root interval can have all of its *actual* modal roots real while using parameters that are accelerated in the interval-robust sense.

### Corollary: nonnegative-root frontier

All modal roots are real and nonnegative throughout \([\mu,L]\) if and only if
\[
\boxed{
\alpha L\le (1-\sqrt\beta)^2.
}
\]
For fixed \(t=\sqrt\beta\in[0,1)\), the best interval-robust factor under this nonnegative-root restriction is obtained at
\[
\alpha=\frac{(1-t)^2}{L}
\]
and equals
\[
R_+(t;c)
=\frac12\left[s_c(t)+\sqrt{s_c(t)^2-4t^2}\right],
\qquad
c=\frac{\mu}{L},
\]
where
\[
s_c(t)=1+t^2-c(1-t)^2.
\]
Its global minimum over \(t\in[0,1)\) is
\[
\boxed{
\min_{0\le t<1}R_+(t;c)=1-c=1-\frac\mu L,
}
\]
achieved uniquely at \(t=0\), i.e. \(\beta=0\) and \(\alpha=1/L\). Hence positive momentum strictly worsens the best rate obtainable while forbidding even modal sign reversal.

## Proof of Theorem 1

Set
\[
t=\sqrt\beta\in[0,1),
\qquad
s_\lambda=1+t^2-\alpha\lambda.
\]
The roots are real exactly when \(|s_\lambda|\ge2t\). Because \(s_\lambda\) is continuous and strictly decreasing in \(\lambda\), if the roots are real for every \(\lambda\in[\mu,L]\), the connected interval \(s([\mu,L])\) cannot cross \((-2t,2t)\). Therefore one of two mutually exclusive branches holds:
\[
\text{(P)}\quad s_L\ge2t,
\qquad\text{or}\qquad
\text{(N)}\quad s_\mu\le-2t.
\]
Equivalently,
\[
\text{(P)}\quad \alpha L\le(1-t)^2,
\qquad
\text{(N)}\quad \alpha\mu\ge(1+t)^2.
\]

### Case \(t=0\)

Heavy ball reduces to gradient descent and the roots are \(0\) and \(1-\alpha\lambda\). Hence
\[
\rho_{[\mu,L]}(\alpha,0)
=\max\{|1-\alpha\mu|,|1-\alpha L|\}.
\]
The unique minimax balance is
\[
1-\alpha\mu=-(1-\alpha L),
\]
which gives \(\alpha=2/(L+\mu)\) and
\[
\rho_{[\mu,L]}=\frac{L-\mu}{L+\mu}.
\]

Now assume \(t>0\).

### Positive branch (P)

All roots are positive. The larger root
\[
\phi(s,t)=\frac{s+\sqrt{s^2-4t^2}}2
\]
is increasing in \(s\ge2t\). Since \(s_\lambda\) decreases with \(\lambda\), the worst curvature is \(\mu\). For fixed \(t\), increasing \(\alpha\) improves this branch, so the best possible choice occurs at the boundary
\[
\alpha=\frac{(1-t)^2}{L}.
\]
Let \(c=\mu/L\in(0,1)\). Then
\[
s_*=1+t^2-c(1-t)^2.
\]
We show that the larger root is strictly greater than \(1-c\). If \(t>1-c\), this is immediate because the geometric mean of the two positive roots is \(t\), so the larger root is at least \(t\).

For \(0<t\le1-c\), evaluate
\[
P(r)=r^2-s_*r+t^2
\]
at \(r_0=1-c\). Direct simplification gives
\[
P(1-c)
=-ct\,[2(1-c-t)+ct]<0.
\]
Thus \(1-c\) lies strictly between the two positive roots, and the larger root exceeds \(1-c\). Consequently
\[
\rho_{[\mu,L]}>1-c>\frac{1-c}{1+c}=q_{\rm GD}.
\]

### Negative branch (N)

All roots are negative. At \(\lambda=L\), set \(u=-s_L>0\). The magnitudes are the positive roots of
\[
r^2-ur+t^2=0.
\]
The branch constraint yields
\[
\alpha\mu\ge(1+t)^2,
\]
so, with \(\kappa=L/\mu\),
\[
u\ge u_*:=\kappa(1+t)^2-(1+t^2)
=(\kappa-1)(1+t^2)+2\kappa t.
\]
The larger positive root is increasing in \(u\), so it is enough to bound the polynomial with \(u=u_*\).

Let
\[
q=\frac{\kappa-1}{\kappa+1}=q_{\rm GD}.
\]
If \(t\ge q\), the larger root is at least \(t\ge q\), and equality cannot occur at \(t=q\) because \(u_*>2q\).

If \(0<t<q\), substitute \(\kappa=(1+q)/(1-q)\). At \(r=q\),
\[
q^2-u_*q+t^2
=-\frac{1+q}{1-q}
\left[q^2+2qt+(2q-1)t^2\right].
\]
The bracket is positive for \(0<t<q\). If \(q\ge1/2\), every displayed contribution is nonnegative and the first two are strictly positive. If \(q<1/2\), the bracket is concave as a function of \(t\), and its endpoint values on \([0,q]\) are
\[
q^2>0,
\qquad
2q^2(1+q)>0.
\]
Hence the polynomial is negative at \(q\), so \(q\) lies strictly between its two positive roots and the larger root is strictly larger than \(q\).

Therefore every \(t>0\) parameter pair whose roots stay real throughout the full spectral interval has
\[
\rho_{[\mu,L]}>q_{\rm GD}.
\]
Together with the \(t=0\) case, this proves both the bound and the equality characterization.

## Proof of the nonnegative-root frontier

With \(t=\sqrt\beta\), real nonnegative roots for a curvature \(\lambda\) require
\[
s_\lambda\ge2t.
\]
Since \(s_\lambda\) decreases with \(\lambda\), this holds throughout \([\mu,L]\) exactly when
\[
s_L\ge2t
\iff
\alpha L\le(1-t)^2.
\]
For fixed \(t\), the larger positive root at \(\mu\) controls the interval worst case and decreases as \(\alpha\) increases, so the optimal admissible step is \(\alpha=(1-t)^2/L\). This gives the stated formula \(R_+(t;c)\). The positive-branch argument above shows
\[
R_+(t;c)>1-c
\qquad (t>0),
\]
while \(R_+(0;c)=1-c\). Hence the unique optimum is zero momentum.

## Classical optimal heavy-ball parameters as a sharp illustration

For
\[
q_{\rm HB}=\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu},
\qquad
\alpha_{\rm HB}=\frac{4}{(\sqrt L+\sqrt\mu)^2},
\qquad
\beta_{\rm HB}=q_{\rm HB}^2,
\]
one has
\[
p_\mu(r)=(r-q_{\rm HB})^2,
\qquad
p_L(r)=(r+q_{\rm HB})^2.
\]
For every strict interior curvature \(\mu<\lambda<L\),
\[
|s_\lambda|<2q_{\rm HB},
\]
so the roots are a complex-conjugate pair of modulus \(q_{\rm HB}\). Since
\[
q_{\rm HB}<q_{\rm GD},
\]
this classical tuning lies on the accelerated side of the barrier. The repeated endpoint roots and complex interior roots for Polyak's optimal quadratic parameters are known; the contribution here is the converse interval-minimax statement that *any* fixed heavy-ball parameters beating optimal gradient descent in worst-case spectral radius over \([\mu,L]\) must enter the complex-root regime somewhere in that interval.

## Relation to prior literature

Polyak's 1964 paper introduced the heavy-ball method and derived its accelerated asymptotic tuning for strongly convex quadratics. Qian (1999) analyzed the scalar momentum recurrence and the transition between real and complex characteristic roots, including critical damping for an individual curvature. Torii and Hagan (2002) studied stability and convergence changes induced by momentum; Zhang (2015) derived globally optimal double parameters for steepest descent with momentum. Danilova, Kulakova and Polyak (2018/2020) explicitly analyzed the repeated endpoint roots, complex interior roots, and associated non-monotone behavior of the classical optimal heavy-ball choice. Hagedorn and Jarre (2023/2024) give a modern fixed-step spectral-radius analysis in which the real-versus-complex root regimes are explicit. Ugrinovskii, Petersen and Shames (2023) establish worst-case asymptotic optimality of heavy ball on quadratic functions from a robust-control viewpoint.

In the sources inspected, no statement was found that minimizes the interval worst-case spectral radius subject to the constraint that every curvature in \([\mu,L]\) have real characteristic roots, nor the resulting exact conclusion that the constrained optimum collapses to optimal gradient descent. The two older papers most capable of containing an equivalent parameter classification are Torii--Hagan (2002) and Zhang (2015); their abstracts and bibliographic records were inspected, but their full theorem-level text was not available in the checked sources. Accordingly, originality is asserted only to the best of our knowledge.

## Scope and limitations

- The theorem concerns fixed \(\alpha\) and fixed nonnegative \(\beta<1\) for exact-gradient quadratic optimization.
- The rate is the asymptotic modal spectral radius optimized uniformly over every curvature in a *continuous spectral interval*. It is not a statement that every accelerated finite-dimensional instance must contain an oscillatory eigenmode.
- A matrix whose spectrum contains only selected curvatures can avoid the interval where the same parameters would have complex roots. In particular, a spectrum supported only at the two endpoints can use the classical Polyak parameters while its actual endpoint roots are repeated and real.
- No finite-time norm monotonicity is claimed; repeated or nearly repeated roots can produce polynomial transients even when the asymptotic factor is small.
- The result does not cover negative momentum, varying/adaptive parameters, line search, stochastic gradients, nonlinear objectives, Nesterov acceleration, or conjugate-gradient methods.
- No claim is made that complex modal roots are sufficient for acceleration; they are only necessary for strict interval-robust improvement over optimal fixed-step gradient descent.

## Reproducibility

`artifacts/verify_real_root_barrier.py` deterministically evaluates representative condition numbers, confirms the optimal gradient-descent and classical heavy-ball spectral factors, checks the endpoint/interior root pattern of Polyak's parameters, and checks the closed-form nonnegative-root frontier. The numerical checks support the algebra but are not used as a substitute for the proof.

## References

1. B. T. Polyak, “Some methods of speeding up the convergence of iteration methods,” *USSR Computational Mathematics and Mathematical Physics* 4(5), 1964. https://doi.org/10.1016/0041-5553(64)90137-5
2. N. Qian, “On the momentum term in gradient descent learning algorithms,” *Neural Networks* 12, 1999, 145–151. https://doi.org/10.1016/S0893-6080(98)00116-6
3. M. Torii and M. T. Hagan, “Stability of steepest descent with momentum for quadratic functions,” *IEEE Transactions on Neural Networks* 13(3), 2002, 752–756. https://doi.org/10.1109/TNN.2002.1000143
4. N. Zhang, “A study on the optimal double parameters for steepest descent with momentum,” *Neural Computation* 27(4), 2015, 982–1004. https://doi.org/10.1162/NECO_a_00710
5. M. Danilova, E. Kulakova and B. Polyak, “Non-monotone Behavior of the Heavy Ball Method,” arXiv:1811.00658. https://arxiv.org/abs/1811.00658
6. M. Hagedorn and F. Jarre, “Iteration Complexity of Fixed-Step Methods by Nesterov and Polyak for Convex Quadratic Functions,” *Journal of Optimization Theory and Applications* 202, 2024, 456–474. https://doi.org/10.1007/s10957-023-02261-w
7. V. Ugrinovskii, I. R. Petersen and I. Shames, “A robust control approach to asymptotic optimality of the heavy ball method for optimization of quadratic functions,” *Automatica* 155, 2023, 111129. https://doi.org/10.1016/j.automatica.2023.111129
