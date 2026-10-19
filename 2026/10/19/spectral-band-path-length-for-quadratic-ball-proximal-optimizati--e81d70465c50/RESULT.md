# Spectral-band path length for quadratic ball-proximal optimization

## Finding

For exact Euclidean ball-proximal minimization of any finite-dimensional positive-definite quadratic, the **total path length is bounded independently of the requested radii by the square root of the number of occupied dyadic eigenvalue bands**. More precisely, let \(H\in\mathbb R^{d\times d}\) be symmetric positive definite, and let \(x^{0}\) be arbitrary. Write \(D=\|x^{0}\|_2\), \(\mu=\lambda_{\min}(H)\), \(\kappa=\lambda_{\max}(H)/\mu\), and \(p=1+\lfloor\log_2\kappa\rfloor\). For every prescribed sequence of positive radii, its stopped exact ball-proximal iterates satisfy

\[
\boxed{\sum_{k\ge0}\|x^{k+1}-x^k\|_2\le D\min\{\sqrt d,\,2\sqrt p\}.}
\]

In particular, for any fixed radius \(h>0\), the number \(N_h\) of ball-oracle calls until the first zero iterate obeys

\[
\boxed{N_h\le1+\frac{D}{h}\min\{\sqrt d,\,2\sqrt p\}.}
\]

The square-root spectral-band dependence is **order sharp**: for each integer \(p\ge2\), the explicit \(p\)-dimensional quadratic with

\[
H_p=\operatorname{diag}(1,2,\ldots,2^{p-1}),\qquad
x^0_p=p^{-1/2}(1,\ldots,1)^\mathsf T
\]

has \(D=1\), \(\kappa=2^{p-1}\), and

\[
\boxed{\liminf_{h\downarrow0}hN_h\ge
(e^{-1/2}-e^{-1})\sqrt p.}
\]

Thus the worst-case spectral-band exponent \(1/2\) cannot be reduced even when every quadratic is strongly convex, the exact oracle is used, and the radius is arbitrarily small.

## Assumptions and scope

The domain is \(\mathbb R^d\) for an arbitrary finite integer \(d\ge1\). The objective is \(f(x)=\tfrac12 x^\mathsf T Hx\) with \(H=H^\mathsf T\succ0\). For any positive radius \(h_k\), define the unique exact update

\[
x^{k+1}=\operatorname*{argmin}_{\|z-x^k\|_2\le h_k}\tfrac12 z^\mathsf THz.
\]

Once \(0\) is reached, the process is stopped and held there. The path-length bound applies equally to runs that do not terminate because of summable radii. If \(x^0=0\), the length and call count are zero. All results use exact arithmetic and exact subproblem solutions. The first public version of the motivating study is September 28, 2026 [1]. Earlier results on the same algorithm [2] and on gradient-flow paths [3] are treated as prior mathematics, not as new contributions.

## Proof

**1. Exact spectral resolvent form.** If \(\|x\|_2\le h\), the unique minimizer is \(0\). Otherwise, the trust-region constraint is active, and the KKT condition for the strictly convex quadratic gives some \(s>0\) such that

\[
y=(I+sH)^{-1}x,\qquad \|x-y\|_2=h.
\]

Indeed the multiplier is positive and \(s\) is its reciprocal. The displacement \(\|x-(I+sH)^{-1}x\|_2\) is continuous and strictly increasing from \(0\) to \(\|x\|_2\) as \(s\) increases from \(0\) to infinity; uniqueness follows. In an orthonormal eigenbasis of \(H\), a nonterminal step therefore multiplies each coordinate by \((1+s\lambda_i)^{-1}\), a number strictly between \(0\) and \(1\).

**2. A uniform one-band estimate.** Fix one nonempty spectral group whose eigenvalues lie in an interval \([a,2a)\). Let \(v\) and \(v'\) be the projections of \(x\) and \(y\) onto that group, and let \(r=\|v\|_2\), \(r'=\|v'\|_2\). For a nonterminal step, define \(c_i=s\lambda_i/(1+s\lambda_i)\) on that group. Writing \(c_-=\min_i c_i\) and \(c_+=\max_i c_i\), the spectral width gives

\[
0<c_-\le c_+<2c_-.
\]

Every coordinate contracts by at least \(c_-\), hence \(r'\le(1-c_-)r\), while \(\|v-v'\|_2\le c_+r\). Consequently

\[
\boxed{\|v-v'\|_2\le2(r-r').}
\]

The same inequality is immediate at a terminal step, because then \(v'=0\). No common step parameter, step-size lower bound, or finite termination assumption is needed for this estimate.

**3. Telescoping over spectral groups.** Partition the eigenvalues into \(p\) half-open intervals \([2^j\mu,2^{j+1}\mu)\), \(0\le j<p\), allowing empty groups. Write \(P_j\) for the associated orthogonal projectors. Summing the one-band estimate over all steps, including a possible terminal step, gives

\[
\sum_{k\ge0}\|P_j(x^{k+1}-x^k)\|_2
\le2\sum_{k\ge0}(\|P_jx^k\|_2-\|P_jx^{k+1}\|_2)
\le2\|P_jx^0\|_2.
\]

By the triangle inequality and Cauchy--Schwarz,

\[
\sum_{k\ge0}\|x^{k+1}-x^k\|_2
\le 2\sum_j\|P_jx^0\|_2
\le2\sqrt p\,D.
\]

Independently, each coordinate's sign is preserved and its magnitude decreases monotonically. Therefore the total variation in that coordinate is exactly at most its initial magnitude. Summing coordinatewise gives the sharper dimension-dependent alternative

\[
\sum_{k\ge0}\|x^{k+1}-x^k\|_2\le\|x^0\|_1\le\sqrt d\,D.
\]

This proves the path-length bound. In a constant-radius run, each nonterminal displacement is exactly \(h\), and only the terminal displacement may be shorter. If \(N_h\ge1\), then \((N_h-1)h\le\sum_k\|x^{k+1}-x^k\|_2\); the stated finite-call bound follows. If a fixed-radius run were infinite, its length would be infinite, contradicting the bound.

**4. Lower bound through arclength parametrization.** For the explicit family in the finding, the ordinary gradient-flow curve is

\[
w_p(t)=p^{-1/2}(e^{-t},e^{-2t},\ldots,e^{-2^{p-1}t})^\mathsf T,\qquad t\ge0.
\]

For each \(j=0,\ldots,p-1\), use the pairwise disjoint intervals \(I_j=[2^{-j-1},2^{-j}]\subset[0,1]\). The Euclidean arclength on \(I_j\) is at least the decrease of its \(j\)-th coordinate, namely \((e^{-1/2}-e^{-1})/\sqrt p\). Summing these disjoint contributions shows

\[
\int_0^1\|w_p'(t)\|_2\,dt\ge(e^{-1/2}-e^{-1})\sqrt p.
\]

Set \(a(t)=\int_0^t\|Hw_p(s)\|_2\,ds\), and write \(z(a)=w_p(t(a))\). On the finite arclength interval \([0,a(1)]\), the curve stays a positive distance from \(0\), and

\[
\frac{dz}{da}=-\frac{Hz}{\|Hz\|_2}.
\]

The nonterminal ball-proximal recurrence is exactly the backward-Euler step of arclength \(h\) for this vector field:

\[
x^{k+1}=x^k-h\frac{Hx^{k+1}}{\|Hx^{k+1}\|_2}.
\]

On any compact subarc \([0,a_0]\) with \(a_0<a(1)\), the vector field is continuously differentiable and Lipschitz in a neighborhood of that subarc. Its backward-Euler approximation therefore converges uniformly there as \(h\downarrow0\): the local truncation error is \(O(h^2)\), and a discrete Gronwall estimate yields \(O(h)\) error across \(O(h^{-1})\) steps. In particular, for all sufficiently small \(h\), the iterate at index \(\lfloor a_0/h\rfloor\) is nonzero, so \(hN_h\ge a_0-o(1)\). Send \(h\downarrow0\) and then \(a_0\uparrow a(1)\) to obtain

\[
\liminf_{h\downarrow0}hN_h\ge a(1)\ge(e^{-1/2}-e^{-1})\sqrt p.
\]

The continuous gradient-flow spectral lower-bound mechanism is known from [3]; the assertion here is its quantitative transfer to **arbitrary-radius exact ball-proximal trajectories**, with a direct dyadic resolvent length proof and constant-radius call-count consequence.

## Verification

The accompanying `verify.py` is standalone Python (standard library only). Run `python3 verify.py`; it checks exact rational two-coordinate resolvent identities, active-step residuals, every band decrement inequality, telescoped full-trajectory bounds over reproducible randomized diagonal problems and radius schedules, and gradient-flow length inequalities on geometric-spectrum examples. One successful execution produced `PASS: 80671 finite checks`. These checks are diagnostics, not proofs of the universally quantified inequalities or infinite-time limit. The four analytical arguments above supply those proofs.

## Relationship to prior work

Richtárik and Li [1], Sections 1 and 4, establish finite-length geometry and \(O_d(1+D/h)\) finite termination for general convex exact ball-proximal optimization. They do not present a spectral-band parameter or a dimension-independent logarithmic-condition-number bound for quadratic ball-proximal orbits. Gruntkowska et al. [2] introduce the broximal operator and its normalized implicit-proximal formulation and give earlier dimension-free squared-distance termination bounds. Gupta, Balakrishnan, and Ramdas [3], Theorems 10 and 18, prove \(\Theta(\min\{\sqrt d,\sqrt{\log\kappa}\})\) path-length behavior for **ordinary gradient flow and fixed-step gradient descent**, not for ball-proximal or variable-resolvent orbits. The spectral lower-bound construction therefore has a clear antecedent; the new statement concerns a different nonlinear, radius-normalized implicit algorithm and provides an arbitrary-radius nonasymptotic length bound. Published research-record comparisons did not identify an equivalent implication for that algorithm, but absence from a finite search is not a mathematical uniqueness certificate.

## Limitations

This finding addresses strictly positive-definite quadratic objectives with exact Euclidean ball-oracle steps. It does not assert the same spectral-band bound for general smooth strongly convex functions, nonquadratic models, inaccurate subproblem solvers, non-Euclidean balls, or numerical floating-point implementations. The explicit constants \(2\) and \(e^{-1/2}-e^{-1}\) need not be best possible; **only the square-root dependence in the number of spectral bands is order sharp**. The lower limit is proved for a family with \(d=p\), \(\kappa=2^{p-1}\), in the small-fixed-radius limit, not as an assertion about every quadratic of condition number \(\kappa\).

## References

[1] P. Richtárik and H. Li, *A Sharper Theory of Ball-Proximal Optimization: Convergence and Radius Selection*, arXiv:2609.35147v1 (first publicly posted September 28, 2026), https://arxiv.org/abs/2609.35147.

[2] K. Gruntkowska, H. Li, A. Rane, and P. Richtárik, *The Ball-Proximal (=“Broximal”) Point Method: a New Algorithm, Convergence Theory, and Applications*, arXiv:2502.02002 (first publicly posted February 4, 2025), https://arxiv.org/abs/2502.02002.

[3] C. Gupta, S. Balakrishnan, and A. Ramdas, *Path Length Bounds for Gradient Descent and Flow*, arXiv:1908.01089 (first publicly posted August 2, 2019; inspected v4, 2021), https://arxiv.org/pdf/1908.01089.
