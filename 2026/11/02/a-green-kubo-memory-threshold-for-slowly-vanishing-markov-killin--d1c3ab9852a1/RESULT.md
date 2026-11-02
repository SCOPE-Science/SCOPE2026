# A Green–Kubo memory threshold for slowly vanishing Markov killing

## Finding

Let \(P\) be a finite-state stochastic matrix with every entry strictly positive, let \(\mu\) be any initial probability distribution, and let \(c:E\to[0,\infty)\) be nonconstant. At step \(k\), a chain occupying state \(i\) survives with probability \(\exp(-c_i/k^\gamma)\), independently conditional on its trajectory, and then makes a \(P\)-transition. Write \(s_n\) for the probability of surviving all \(n\) steps, \(\pi\) for the unique stationary law of \(P\), and

\[
\bar c=\sum_i\pi_i c_i,\qquad
\sigma^2=\operatorname{Var}_\pi(c(X_0))
+2\sum_{j=1}^{\infty}\operatorname{Cov}_\pi(c(X_0),c(X_j)).
\]

The covariance series is absolutely convergent, and \(\sigma^2>0\). For every \(1/3<\gamma\le 1\), every initial law \(\mu\), and \(H_n^{(r)}=\sum_{k=1}^n k^{-r}\), there exists \(C_{\mu,P,c,\gamma}\in(0,\infty)\) such that

\[
\boxed{\displaystyle
s_n=C_{\mu,P,c,\gamma}\,
\exp\left[-\bar c H_n^{(\gamma)}
+\frac{\sigma^2}{2}H_n^{(2\gamma)}\right](1+o(1)).}
\tag{1}
\]

This is a *relative* asymptotic, including a positive finite prefactor, and not merely an estimate of the leading logarithmic rate. The second-order survival enhancement has a sharp transition at \(\gamma=1/2\):

\[
\begin{array}{ll}
1/2<\gamma<1:&s_n\sim C_\gamma\exp[-\bar c n^{1-\gamma}/(1-\gamma)],\\[2pt]
\gamma=1/2:&s_n\sim C_{1/2}\,n^{\sigma^2/2}\exp[-2\bar c\sqrt n],\\[2pt]
1/3<\gamma<1/2:&s_n\sim C_\gamma\exp[-\bar c n^{1-\gamma}/(1-\gamma)+\sigma^2 n^{1-2\gamma}/(2(1-2\gamma))],\\[2pt]
\gamma=1:&s_n\sim C_1 n^{-\bar c}.
\end{array}
\tag{2}
\]

Each constant displayed in (2) is positive and finite; it generally differs from the constant in (1) because the harmonic sums contribute finite Euler--Maclaurin offsets.

The critical power is not bounded by the one-step hazard distribution. For the strictly positive two-state chain

\[
P_\rho=\frac12\begin{pmatrix}1+\rho&1-\rho\\1-\rho&1+\rho\end{pmatrix},
\quad c=(0,2),\quad -1<\rho<1,
\]

all \(\rho\) have identical stationary law and stationary hazard distribution, yet

\[
\bar c=1,\qquad \sigma^2=\frac{1+\rho}{1-\rho},\qquad
s_n\sim C_{\rho,\mu}\,n^{(1+\rho)/(2(1-\rho))}e^{-2\sqrt n}
\quad(\gamma=1/2).
\tag{3}
\]

Every exponent \(\alpha>0\) is achieved by choosing \(\rho=(2\alpha-1)/(2\alpha+1)\). In particular, \(\rho=1/2\) and \(\rho=-1/2\) have a survival-probability ratio asymptotic to a positive constant times \(n^{4/3}\). Above the threshold the corresponding ratio instead has a finite positive limit; below it, its logarithm has a positive leading term of order \(n^{1-2\gamma}\).

## Assumptions and scope

The state space \(E\) is finite and contains at least two states. All \(P_{ij}>0\); no reversibility is assumed. The hazard \(c\) is bounded because \(E\) is finite, is nonnegative to admit a killing interpretation, and is nonconstant to make the correlation effect nondegenerate. The initial distribution \(\mu\) need not have full support. The exponent \(\gamma\) is fixed in \((1/3,1]\). Conditional on the chain path \((X_0,\ldots,X_n)\), survival has probability

\[
\prod_{k=1}^n\exp(-k^{-\gamma}c(X_{k-1})),\qquad
s_n=\mathbb E_\mu\exp\left[-\sum_{k=1}^n k^{-\gamma}c(X_{k-1})\right].
\tag{4}
\]

The orientation of the potential **before** the transition is part of the definition; the resulting positive matrices are \(A(t)=D(t)P\), where \(D(t)=\operatorname{diag}(e^{-tc_i})\). No result for periodic or merely irreducible, nonpositive, infinite-state, or random-environment transition kernels is claimed. At \(\gamma\le1/3\), third and higher pressure cumulants may require additional divergent counterterms; (1) is not asserted there.

## Proof

**1. Stationary covariance and positive variance.** Strict positivity of \(P\) implies geometric mixing, so the covariance series converges absolutely. Put \(h=c-\bar c\mathbf1\), viewed as a column vector. There is a unique \(\pi\)-centered solution \(g\) of

\[
(I-P)g=h,\qquad \pi g=0,
\tag{5}
\]

given by \(g=\sum_{j\ge0}P^jh\) on the centered subspace. In stationary equilibrium,

\[
\sigma^2=\pi(h^2)+2\pi(hPg)
=\mathbb E_\pi\big[(g(X_1)-(Pg)(X_0))^2\big].
\tag{6}
\]

The equality follows by writing \(h=g-Pg\) and expanding conditional expectations; here \(\pi(h^2)=\sum_i\pi_i h_i^2\). Each conditional variance \(\operatorname{Var}(g(X_1)\mid X_0=i)\) vanishes only if \(g\) is constant on the entire state space, because each row of \(P\) has full support. Thus \(\sigma^2=0\) would force \(h=0\), contrary to the nonconstant-hazard assumption.

**2. The Perron pressure and its second derivative.** For real \(t\in[0,1]\), \(A(t)=D(t)P\) is strictly positive. Let \(\lambda(t)>0\) be its Perron eigenvalue, \(\ell(t)\) its positive left eigenvector normalized by \(\ell(t)\mathbf1=1\), and \(r(t)\) its positive right eigenvector normalized by \(\pi r(t)=1\) near zero. These objects are analytic near zero and \(\ell(t)\) is continuously differentiable on the entire compact interval. At zero,

\[
\lambda(0)=1,\quad\ell(0)=\pi,\quad r(0)=\mathbf1.
\]

Differentiate \(A(t)r(t)=\lambda(t)r(t)\) at zero. Since \(A'(0)=-\operatorname{diag}(c)P\), the normalized derivative satisfies \(r'(0)=-g\) from (5), while \(\lambda'(0)=-\bar c\). A second differentiation, multiplying from the left by \(\pi\), gives

\[
\lambda''(0)=\pi(c^2)+2\pi(cPg).
\]

Consequently, for \(f(t)=\log\lambda(t)\),

\[
f(0)=0,\qquad f'(0)=-\bar c,\qquad f''(0)=\sigma^2,
\]

and the analytic Taylor expansion yields

\[
f(t)=-\bar c t+\tfrac12\sigma^2t^2+O(t^3)
\qquad(t\downarrow0).
\tag{7}
\]

**3. Adiabatic tracking of normalized survivor distributions.** Put \(t_k=k^{-\gamma}\), \(q_0=\mu\), and define the normalized survivor distributions recursively by

\[
q_k=F_{t_k}(q_{k-1}),\qquad
F_t(q)=\frac{qA(t)}{qA(t)\mathbf1}.
\tag{8}
\]

The normalized left Perron eigenvector is the fixed point \(F_t(\ell(t))=\ell(t)\). Every \(q_k\) with \(k\ge1\) is strictly positive. For strictly positive vectors define Hilbert's projective distance \(d_H(u,v)=\log(\max_i u_i/v_i)-\log(\min_i u_i/v_i)\). Right multiplication by a positive diagonal matrix preserves \(d_H\) on rows, and right multiplication by the fixed strictly positive matrix \(P\) contracts it by a constant \(\theta\in[0,1)\) (Birkhoff's projective contraction theorem; explicitly \(\theta=\tanh[\Delta(P)/4]\) with \(\Delta(P)=\log\max_{i,j,k,\ell}P_{ik}P_{j\ell}/(P_{i\ell}P_{jk})<\infty\)). Since \(A(t)=D(t)P\), for every \(t\in[0,1]\),

\[
d_H(F_t(u),F_t(v))\le\theta\,d_H(u,v).
\tag{9}
\]

The continuous differentiability and uniform positivity of \(\ell(t)\) imply \(d_H(\ell(t_k),\ell(t_{k-1}))=O(k^{-\gamma-1})\). Recursing (9) for \(k\ge2\),

\[
d_H(q_k,\ell(t_k))
\le\theta^{k-1}d_H(q_1,\ell(t_1))
+O\left(\sum_{j=2}^k\theta^{k-j}j^{-\gamma-1}\right)
=O(k^{-\gamma-1})+O(\theta^{k/2}).
\tag{10}
\]

On the probability simplex, projective and ordinary distances are locally equivalent uniformly around the positive vectors \(\ell(t_k)\). Thus \(\|q_{k-1}-\ell(t_k)\|_1=O(k^{-\gamma-1})+O(\theta^{k/2})\).

**4. Positive convergence of the normalized survival amplitude.** With \(s_0=1\), the one-step mass factor is

\[
\frac{s_k}{s_{k-1}}=q_{k-1}D(t_k)\mathbf1,
\qquad \lambda(t_k)=\ell(t_k)D(t_k)\mathbf1.
\tag{11}
\]

The two rows have total mass one. Therefore, subtracting the common constant vector,

\[
\left|q_{k-1}D(t_k)\mathbf1-\ell(t_k)D(t_k)\mathbf1\right|
\le\|q_{k-1}-\ell(t_k)\|_1\max_i|e^{-t_kc_i}-1|
=O(k^{-2\gamma-1})+O(k^{-\gamma}\theta^{k/2}).
\tag{12}
\]

All mass factors in (11) are bounded below by \(e^{-\max_i c_i}\), so the same bound holds for their logarithms. Consequently

\[
R_n=\log s_n-\sum_{k=1}^n\log\lambda(t_k)
\]

converges to a finite real \(R_\infty\), with tail \(O(n^{-2\gamma})\). In particular, \(\exp(R_\infty)>0\). This step proves that slowly varying eigenvectors do not introduce an unaccounted logarithmic factor.

**5. Summability and the phase transition.** By (7),

\[
\sum_{k=1}^n\log\lambda(t_k)
=-\bar c H_n^{(\gamma)}+\frac{\sigma^2}{2}H_n^{(2\gamma)}
+\sum_{k=1}^n O(k^{-3\gamma}).
\]

For \(\gamma>1/3\) the last sum converges to a real limit, with tail \(O(n^{1-3\gamma})\). Combining it with the finite limit \(R_\infty\) proves (1) and in fact the sharper logarithmic remainder

\[
\log s_n+\bar c H_n^{(\gamma)}-\frac{\sigma^2}{2}H_n^{(2\gamma)}
=\log C_{\mu,P,c,\gamma}+O(n^{-2\gamma}+n^{1-3\gamma}).
\tag{13}
\]

The familiar integral-comparison asymptotics of the generalized harmonic sums imply (2): \(H_n^{(r)}\) has a finite subtraction constant after \(n^{1-r}/(1-r)\) for \(0<r<1\), while \(H_n^{(1)}=\log n+\gamma_{\rm E}+o(1)\). The second-order term converges for \(2\gamma>1\), grows logarithmically for \(2\gamma=1\), and grows as \(n^{1-2\gamma}/(1-2\gamma)\) below that boundary. Strict positivity of \(\sigma^2\) makes the threshold genuine.

**6. Fixed-marginal two-state calibration.** For \(P_\rho\), the stationary distribution is uniform. The centered observable \(h=(-1,1)\) satisfies \(Ph=\rho h\), giving \(\operatorname{Cov}_\pi(c(X_0),c(X_j))=\rho^j\). Therefore \(\sigma^2=1+2\sum_{j\ge1}\rho^j=(1+\rho)/(1-\rho)\). The map \(\rho\mapsto\sigma^2/2\) is a bijection from \((-1,1)\) onto \((0,\infty)\), proving (3) and the asserted relative survival growth. Strict positivity holds throughout this parameter range.

## Verification

A standalone Python 3 verifier, `CHECK.py`, uses only the standard library. It checks exact rational solutions of (5) and (6) for a grid of two-state correlation values, compares finite-horizon matrix recursions with complete path enumeration, checks the second Perron-pressure derivative numerically, and tests finite-size convergence of the normalized log-survival residuals. Running `python3 CHECK.py` produces the independent reproducibility artifact `CHECK_OUTPUT.txt`. These finite tests are not used as a proof of (1)--(3): their infinite claims are established by Steps 1--6.

## Relationship to prior work

Del Moral and Gerber, arXiv:2610.21587v1 (first public date October 15, 2026), develop stability and perturbation bounds for normalized Feynman–Kac flows, including the normalized recursion used in (8). Their main results bound propagated approximation errors; they do not state the correlation-induced logarithmic survival correction (1) or the critical fixed-marginal family (3). Champagnat and Villemonais, arXiv:1603.07477v1, establish exponential contraction and relative limiting survival ratios for time-inhomogeneous penalizations, but their displayed theorems do not compute the full decaying-hazard normalizer or Green--Kubo coefficient. Petersson, arXiv:1603.05889v1, studies near-critical absorption for a *fixed* perturbed semi-Markov kernel as observation horizon and perturbation tend jointly to their limits; that regime differs from changing the killing parameter separately at each step. All these frameworks are acknowledged as predecessors, not claimed as new.

Perron--Frobenius perturbation theory, the Poisson equation, and Birkhoff contraction are standard proof ingredients. The assessed claim is their explicit synthesis into a *positive relative survival asymptotic* with a sharp correlation-memory crossover and an unbounded critical exponent at fixed stationary hazards. Although focused literature comparison did not locate this exact combined statement, a broader older nonstationary multiplicative-functional theorem may implicitly imply it; historical priority remains subject to independent expert review.

## Limitations

The positivity assumption is used for uniform projective contraction and for the strict positivity of the Green--Kubo variance. The restrictions to finitely many states, deterministic power hazards, and \(\gamma>1/3\) are substantive. The constant \(C_{\mu,P,c,\gamma}\) is defined by a convergent limit but is not expressed in general closed form. Equation (13) gives a mathematically controlled asymptotic, not a uniform estimate over all transition matrices approaching reducibility. This proof and its finite computations have not been independently audited. Definitive priority over unpublished or inaccessible classical results is not asserted.

## References

1. P. Del Moral and M. Gerber, *A perturbation theory for Feynman–Kac models and their particle interpretations*, arXiv:2610.21587v1, first publicly submitted October 15, 2026, https://arxiv.org/abs/2610.21587.
2. N. Champagnat and D. Villemonais, *Uniform convergence of penalized time-inhomogeneous Markov processes*, arXiv:1603.07477v1, first publicly submitted March 24, 2016, https://arxiv.org/html/1603.07477v1.
3. M. Petersson, *Quasi-Stationary Asymptotics for Perturbed Semi-Markov Processes in Discrete Time*, arXiv:1603.05889v1, first publicly submitted March 18, 2016, https://arxiv.org/abs/1603.05889.
4. G. Birkhoff, *Extensions of Jentzsch's theorem*, Trans. Amer. Math. Soc. 85 (1957), 219–227; classical projective contraction theorem (used as a standard lemma).
