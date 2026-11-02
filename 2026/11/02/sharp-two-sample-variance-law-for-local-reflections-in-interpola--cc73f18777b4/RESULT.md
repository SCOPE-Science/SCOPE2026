# Sharp two-sample variance law for local reflections in interpolatory stratified Monte Carlo

## Finding

Let \(f\in C^2([0,1])\) and \(m\ge1\) be an integer. Partition \([0,1]\) into \(m\) equal intervals of length \(h=1/m\). On each interval, integrate the endpoint-affine interpolant exactly and correct its residual using the mean of **two** evaluations with uniform marginal positions. Assume different intervals use independent pairs, but impose **no independence requirement inside each pair**.

Among every choice of within-interval bivariate coupling with two uniform marginals, the smallest possible leading asymptotic variance is attained by the *half-cell reflection*

\[
T(u)=\begin{cases}\tfrac12-u,&0\le u<\tfrac12,\\\tfrac32-u,&\tfrac12\le u\le1.\end{cases}
\]

Writing the resulting unbiased quadrature estimate as \(Q_m^{\mathrm{half}}\), we prove the sharp optimality statement

\[
\lim_{m\to\infty}m^5\operatorname{Var}(Q_m^{\mathrm{half}})
=\frac1{11520}\int_0^1(f''(x))^2\,dx,
\]

and for **any** sequence of admissible within-cell couplings independent across cells,

\[
\liminf_{m\to\infty}m^5\operatorname{Var}(Q_m)
\ge\frac1{11520}\int_0^1(f''(x))^2\,dx.
\]

By comparison, two independent uniforms per interval and the usual central antithetic coupling \((U,1-U)\) satisfy, respectively,

\[
\lim_{m\to\infty}m^5\operatorname{Var}(Q_m^{\mathrm{iid}})=\frac1{1440}\int_0^1(f''(x))^2\,dx,
\]
\[
\lim_{m\to\infty}m^5\operatorname{Var}(Q_m^{\mathrm{central}})=\frac1{720}\int_0^1(f''(x))^2\,dx.
\]

Thus, provided \(f''\not\equiv0\), the half-cell reflection has one eighth of the independent-pair leading variance and one sixteenth of the standard-antithetic leading variance; ordinary central antithetics instead double the independent-pair leading variance. For \(f(x)=x^2\), all these ratios and variance constants are **exact for every** \(m\ge1\), not merely asymptotic.

## Assumptions and scope

For \(j\in\{0,\ldots,m-1\}\), put \(a_j=jh\). Let \(L_j(u)=(1-u)f(a_j)+u f(a_j+h)\) and \(r_j(u)=f(a_j+hu)-L_j(u)\), for \(0\le u\le1\). For each \(j\), let \((U_j,V_j)\) have arbitrary joint distribution with both marginals \(\operatorname{Uniform}[0,1]\). Pairs are independent across distinct \(j\). Define

\[
Q_m=\sum_{j=0}^{m-1}h\left[\frac{f(a_j)+f(a_j+h)}2+\frac{r_j(U_j)+r_j(V_j)}2\right].
\]

The local map \(T\) is measure preserving on \([0,1]\) and the designated construction uses \(V_j=T(U_j)\) independently for each cell. The comparisons keep the **same number of function evaluations**: the \(m+1\) shared grid endpoints and two residual evaluations per cell. Couplings between different cells and unequal grids are outside the stated optimality class. All variances are over the random sample positions, not over noisy function evaluations.

## Proof

**1. Unbiasedness.** Each uniform marginal integrates \(r_j\) correctly. The integral of \(L_j\) over the cell is \(h(f(a_j)+f(a_j+h))/2\). Thus \(\mathbb E Q_m=\int_0^1 f(x)\,dx\) for any admissible within-cell coupling.

**2. Exact optimal two-sample residual coupling.** Set \(z(u)=u(1-u)\). For a uniform \(U\), the random variable \(Z=z(U)\) takes values in \([0,1/4]\) with

\[
\Pr(Z\le t)=1-\sqrt{1-4t},\qquad
\mathbb E Z=\frac16,\qquad \operatorname{Var}(Z)=\frac1{180}.
\]

For all pairs \((Z,Z')\) with these marginals, the Fréchet–Hoeffding lower intersection bound, integrated over nonnegative thresholds, minimizes \(\mathbb E ZZ'\) when the two quantiles are oppositely ordered. Indeed, for any \(s,t\),

\[
\Pr(Z>s,Z'>t)\ge\max\{0,\Pr(Z>s)+\Pr(Z'>t)-1\},
\]

and the opposite-quantile construction attains equality simultaneously for all \(s,t\). This is a direct proof of the covariance minimum, without assuming a particular parameterization of the original uniform pair.

Write \(R=|2U-1|\), which is uniform on \([0,1]\). Then \(z(U)=(1-R^2)/4\), and the half-cell reflection gives \(|2T(U)-1|=1-R\), hence \(z(T(U))=(1-(1-R)^2)/4\). The two residual values are opposite quantiles. Direct integration yields

\[
\operatorname{Cov}(z(U),z(T(U)))=-\frac7{1440},
\qquad
\operatorname{Var}\left(\frac{z(U)+z(T(U))}{2}\right)=\frac1{2880}.
\]

For any other uniform-marginal pair \((U,V)\), the last variance is at least \(1/2880\). Two independent uniforms instead give \(1/360\), and \(V=1-U\) makes \(z(V)=z(U)\), giving \(1/180\). Optimality concerns the distribution of the two **residual values**; it does not assert uniqueness of the underlying uniform-coordinate coupling.

**3. Uniform interpolation expansion.** Uniform continuity of \(f''\) on the compact interval implies, uniformly over cells and \(u\in[0,1]\),

\[
r_j(u)=-\frac{h^2}2f''(a_j)z(u)+h^2\varepsilon_{j,m}(u),
\qquad \sup_{j,u}|\varepsilon_{j,m}(u)|\longrightarrow0.
\]

Because all \(z\)-values lie in \([0,1/4]\) and \(f''\) is bounded, the covariance and variance perturbations are \(o(h^4)\), **uniformly over all allowed within-cell couplings**. Consequently, with \(W_j=(z(U_j)+z(V_j))/2\),

\[
\operatorname{Var}\!\left(\frac{r_j(U_j)+r_j(V_j)}2\right)
=\frac{h^4}4(f''(a_j))^2\operatorname{Var}(W_j)+o(h^4).
\]

**4. Sharp global limit.** Pair independence across cells gives

\[
\operatorname{Var}(Q_m)=h^2\sum_{j=0}^{m-1}
\operatorname{Var}\!\left(\frac{r_j(U_j)+r_j(V_j)}2\right).
\]

Apply the universal lower bound \(\operatorname{Var}(W_j)\ge1/2880\), use uniformity of the preceding remainder, multiply by \(m^5\), and take the Riemann-sum limit to obtain the stated lower bound. For the half-cell coupling the local bound is an equality in every cell, yielding equality in the limit. Repeating the same calculation with the independent and central-antithetic local variances produces the two comparison constants.

**5. Exact sharpness for a quadratic.** If \(f(x)=x^2\), then \(r_j(u)=-h^2z(u)\) exactly, for all \(j\) and \(m\). Therefore

\[
\operatorname{Var}(Q_m^{\mathrm{half}})=\frac1{2880m^5},\quad
\operatorname{Var}(Q_m^{\mathrm{iid}})=\frac1{360m^5},\quad
\operatorname{Var}(Q_m^{\mathrm{central}})=\frac1{180m^5}.
\]

This also shows no larger universal asymptotic lower bound is possible within the stated class.

## Verification

The self-contained source file `verify.py` computes polynomial moments with exact rational arithmetic. It checks the local variance values, the exact quadratic formula for several mesh sizes, and convergence toward the three \(C^2\) constants for the cubic test \(f(x)=x^2+x^3\), whose squared-curvature integral is \(28\). Run:

```text
python verify.py
```

The script is a finite consistency check; the proofs in Steps 2–5 establish the infinite and universal claims.

## Relationship to prior work

Kunsch (2023), *Linear Monte Carlo quadrature with optimal confidence intervals*, introduced stratified control variates with local polynomial interpolation and independent residual samples. Its results concern optimal probabilistic rates for Sobolev classes rather than optimal two-sample residual couplings or their exact \(C^2\) variance constants.

Owen (2008), *Local antithetic sampling with scrambled nets*, introduced **local dyadic reflections**, including the one-dimensional half-cell map used here, and analyzed their advantages for randomized digital nets. The map is **not** claimed as new. The result here concerns a distinct cellwise interpolatory residual estimator and proves a sharp copula-optimal variance constant against all uniform-marginal two-sample couplings, rather than a scrambled-net convergence-rate comparison.

The opposite-quantile covariance inequality is classical (Fréchet–Hoeffding); no novelty is claimed for it in isolation. The contribution assessed here is the exact application to a nonmonotone interpolation residual and the universal sharp variance law, including the factor-eight and factor-sixteen comparisons at matched evaluation cost.

## Limitations

This is a one-dimensional, smooth-integrand, equal-cell, noiseless-evaluation result with independent pairs across cells. Its optimality **does not** include cross-cell dependence, other node-allocation models, higher dimensions, or randomized quasi-Monte Carlo point sets. It does not claim a better asymptotic rate than known stratified-control-variate schemes or a novel dyadic reflection map. Other specialized results could contain an equivalent sharp constant; independent publication-priority review remains necessary.

## References

1. R. J. Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals*, arXiv:2309.09059 (first version 16 September 2023). https://arxiv.org/abs/2309.09059
2. A. B. Owen, *Local antithetic sampling with scrambled nets*, Annals of Statistics 36 (2008), 2319–2343, arXiv:0811.0528. https://arxiv.org/abs/0811.0528
3. *Multivariate countermonotonicity and the minimal copulas*, Journal of Computational and Applied Mathematics 317 (2017), 589–602, DOI:10.1016/j.cam.2016.12.032. https://doi.org/10.1016/j.cam.2016.12.032
