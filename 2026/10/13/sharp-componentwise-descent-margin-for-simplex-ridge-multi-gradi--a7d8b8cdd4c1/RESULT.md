# Sharp componentwise descent margin for simplex-ridge multi-gradient directions

## Finding

The regularized minimum-norm convex combination of \(m\ge 2\) objective gradients obeys a **sharp per-objective descent-margin inequality**. For arbitrary columns \(g_1,\dots,g_m\in\mathbb R^n\), let \(G=[g_1\ \cdots\ g_m]\), let \(\rho>0\), and define
\[
\lambda_\rho=\operatorname*{argmin}_{\lambda\in\Delta_m}
\left\{\frac12\|G\lambda\|^2+\frac\rho2\|\lambda\|^2\right\},\quad
v=G\lambda_\rho,\quad p=-\frac{v}{\sigma},\quad \sigma>0,
\]
where \(\Delta_m=\{\lambda\in\mathbb R^m:\lambda_i\ge0,\ \sum_i\lambda_i=1\}\). Then **every** component satisfies
\[
\boxed{\langle g_i,v\rangle\ge \|v\|^2-\frac{m-1}{4m}\rho,\qquad i=1,\dots,m.}
\]
Equivalently, \(\langle g_i,p\rangle\le-\sigma\|p\|^2+\rho(m-1)/(4m\sigma)\). Consequently, \(p\) is a strict common first-order descent direction whenever
\[
\boxed{\|v\|^2>\frac{m-1}{4m}\rho.}
\]
For every \(m\ge2\), \(\rho>0\), and \(\sigma>0\), a two-dimensional family attains equality in the componentwise inequality. Even when the gradients admit a strict common descent direction, the computed \(p\) can increase one objective if the displayed condition fails. Therefore neither the error constant nor the strict universal safety threshold can be improved without additional hypotheses.

## Assumptions and scope

This is a pointwise statement about an *exact* Euclidean, unconstrained simplex-ridge subproblem; it does not assume convexity of the underlying objectives, deterministic versus stochastic origins for the supplied gradients, or linear independence of all \(m\) columns. The strictly convex multiplier objective makes \(\lambda_\rho\) unique. No projected feasible-set normal cone or approximate inner solution is included. For differentiable objective functions \(F_i\), take \(g_i=\nabla F_i(x)\) at a common point \(x\). A strict negative directional derivative guarantees decreases for all objectives at sufficiently small positive step fractions; it does not guarantee decrease under an arbitrary finite step size.

## Proof

**First-order variational inequality.** Since \(\lambda_\rho\) minimizes a differentiable convex function on \(\Delta_m\), for every \(\mu\in\Delta_m\),
\[
\langle G^\top v+\rho\lambda_\rho,\mu-\lambda_\rho\rangle\ge0.
\]
Choose the simplex vertex \(\mu=e_i\). The identities \(\langle G^\top v,\lambda_\rho\rangle=\|v\|^2\) and \(\langle G^\top v,e_i\rangle=\langle g_i,v\rangle\) yield
\[
\langle g_i,v\rangle\ge\|v\|^2-\rho\bigl((\lambda_\rho)_i-\|\lambda_\rho\|^2\bigr).
\]

**Exact simplex extremum.** For an arbitrary \(\lambda\in\Delta_m\), fix \(t=\lambda_i\). Cauchy--Schwarz on the remaining \(m-1\) coordinates gives
\[
\lambda_i-\|\lambda\|^2\le t-t^2-\frac{(1-t)^2}{m-1}
=\frac{m-1}{4m}-\frac{m}{m-1}\left(t-\frac{m+1}{2m}\right)^2.
\]
The upper bound is attained at \(\lambda_i=(m+1)/(2m)\) with \(\lambda_j=1/(2m)\) for all \(j\ne i\). Substitution proves the asserted bound. Multiplication by \(-1/\sigma\) gives the equivalent direction inequality and its sufficient condition for strict common descent.

**Sharpness at every number of objectives.** Fix \(m\ge2\), \(\rho>0\), \(s>0\), and \(\delta>0\). Put \(C=(m-1)/(4m)\), \(H=(m+1)/(4m)\), and \(k=(m+1)/(m-1)\). In \(\mathbb R^2\) set
\[
\begin{aligned}
g_1&=(s-\rho C/s,\ \delta),\\
g_j&=(s+\rho H/s,\ -k\delta),&&j=2,\dots,m,\\
\lambda_1&=(m+1)/(2m),&\lambda_j&=1/(2m),&&j=2,\dots,m.
\end{aligned}
\]
Direct summation gives \(G\lambda=(s,0)=v\). Every coordinate of \(G^\top v+\rho\lambda\) equals \(s^2+\rho(m+3)/(4m)\), so the simplex variational inequality is an equality for every competitor. Strict convexity therefore makes this \(\lambda\) the unique minimizer. In addition,
\[
\langle g_1,v\rangle=s^2-\rho C=\|v\|^2-\rho C.
\]
The determinant of the two distinct column vectors is \(-2ms\delta/(m-1)\), which is nonzero. Hence \(0\notin\operatorname{conv}\{g_1,\dots,g_m\}\): the gradients admit a strict common descent direction. Nevertheless \(\langle g_1,p\rangle>0\) whenever \(s^2<\rho C\), and it equals zero when \(s^2=\rho C\). Thus the exact coefficient and strict boundary are globally optimal.

**An actual objective-increase example.** Take \(m=n=2\), \(\rho=4\), \(\sigma=1\), \(g_1=(-1/2,1)\), and \(g_2=(7/2,-3)\). The unique multiplier is \(\lambda_\rho=(3/4,1/4)\), giving \(v=(1/2,0)\) and \(p=(-1/2,0)\). For \(F_i(x)=\frac12\|x\|^2+\langle g_i,x\rangle\) at \(x=0\), both objectives are coercive and strongly convex, and
\[
F_1(p)-F_1(0)=3/8>0,\qquad F_2(p)-F_2(0)=-13/8.
\]
The alternative direction \(d=(-2,-2)\) satisfies \(\langle g_1,d\rangle=\langle g_2,d\rangle=-1\). Hence this is an increase produced by the regularized multi-gradient rule at a genuinely non-Pareto-stationary point, not an impossibility of improving both objectives.

## Verification

The standalone `verify.py` checks the exact-rational multiplier, simplex optimality, equality, two-dimensional noncollinearity, and objective differences in the sharp family for \(2\le m\le12\), several positive rational regularizations and scales. It also exhaustively compares a two-gradient closed-form multiplier against rational grid cases. Output on execution: `VERIFY_OK 9216 rational geometry instances; witness objective increase 27/196` and `SHARP_CERTIFICATE_OK m=2..12, exact KKT, noncollinearity, quadratic ascent`. Finite checks are regression tests only; the displayed first-order inequality and sharpness are proved algebraically for every permissible dimension and parameter.

## Relationship to prior work

Li, Wang, and Chen (2026, arXiv:2609.02722v1, Section 3.1) give precisely this unconstrained ridge-multiplier rule as the unconstrained case of their projected method. In Lemma 4.1 and its proof they derive the componentwise estimate \(\langle g_i,p\rangle\le-\sigma\|p\|^2/2+\rho(m-1)/(2m\sigma)\), valid more broadly for constrained displacements. For its **unconstrained specialization**, their sufficient certificate of negative directional derivative requires \(\|v\|^2>\rho(m-1)/m\). The new sharp unconstrained certificate requires only one quarter as large a norm-squared threshold, with a matching obstruction. No improvement to that paper's constrained-case guarantee or its convergence theorem is claimed.

Fernando and collaborators (2022, arXiv:2210.12624, Section 3.1) also use ridge-regularized simplex weights for stochastic multi-objective learning, with a different scaling of the ridge parameter (their displayed objective is \(\|G\lambda\|^2+\rho\|\lambda\|^2/2\)). Their subject is gradient tracking and asymptotic stationarity, not the sharp finite-step componentwise margin. Liu and Vicente (2019/2021) study the unregularized stochastic multi-gradient rule; Xiao, Ban, and Ji (2023) study a different direction-oriented penalty. Related work on ordinary KKT conditions and simplex extrema underlies the proof, but the exact coefficient, all-\(m\) witnesses, and strongly convex ascent example are the additional statements here.

## Limitations

The inequality is for an exact inner multiplier and an unconstrained Euclidean step. The example does not disprove convergence of any adaptive method: a step can increase an objective while aggregate or asymptotic guarantees remain valid. No result is claimed for inaccurate gradient estimates, constrained projections, or stochastic expected descent. Prior equivalent results outside the inspected literature may exist; no independent audit has been performed.

## References

1. Y. Li, L. Wang, X. Chen, *An Adaptive Projected-Gradient Algorithm for Sample-Average Approximations of Stochastic Multi-Objective Optimization*, arXiv:2609.02722v1 (first publicly posted 2026-09-02), Sections 3.1 and 4. https://arxiv.org/html/2609.02722v1
2. H. Fernando, H. Shen, M. Liu, S. Chaudhury, K. Murugesan, T. Chen, *Mitigating Gradient Bias in Multi-objective Learning: A Provably Convergent Stochastic Approach*, arXiv:2210.12624 (2022), Sections 2.2 and 3.1, theory and appendix. https://ar5iv.labs.arxiv.org/html/2210.12624
3. S. Liu, L. N. Vicente, *The stochastic multi-gradient algorithm for multi-objective optimization and its application to supervised machine learning*, arXiv:1907.04472 (2019), Sections 3--5. https://arxiv.org/html/1907.04472v3
4. P. Xiao, H. Ban, K. Ji, *Direction-oriented Multi-objective Learning: Simple and Provable Stochastic Algorithms*, arXiv:2305.18409 (2023), Sections 3--4. https://arxiv.org/html/2305.18409v3
