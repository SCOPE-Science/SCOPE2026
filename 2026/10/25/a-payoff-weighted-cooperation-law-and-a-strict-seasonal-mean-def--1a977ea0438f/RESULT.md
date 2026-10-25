# A payoff-weighted cooperation law and a strict seasonal mean deficit in pairwise eco-evolutionary games

## Finding

For the periodically forced, asymmetric-feedback public-goods model of Jiang et al. [1], the fraction of cooperation has a **payoff-weighted average fixed entirely by the feedback parameter**, independently of forcing shape or period. For the natural pairwise case, this becomes a finite-amplitude **strict deficit in ordinary time-mean cooperation** whenever cooperation fluctuates.

Precisely, for every group size \(N\ge2\) and every interior \(T\)-periodic solution (definitions below),
\[
\frac{\int_0^T x(t)P_D(t)\,dt}{\int_0^T P_D(t)\,dt}
= x_*:=\frac{\theta}{1+\theta}.
\tag{1}
\]
When \(N=2\), the identity is stronger:
\[
\operatorname{Var}_T(x)
=\bar x\left(x_*-\bar x\right),
\qquad \bar x:=T^{-1}\int_0^T x(t)\,dt.
\tag{2}
\]
Thus every nonconstant interior pairwise periodic orbit satisfies \(0<\bar x<x_*\), regardless of the amplitude, period, environmental waveform, or feedback speed. The result is not vacuous: at the explicit parameters in the proof, every sufficiently small nonzero sinusoidal forcing possesses a locally attracting, nonconstant interior periodic orbit. Its mean satisfies
\[
\bar x(\delta)=\frac12-\frac{625}{52372}\delta^2+O(\delta^3),
\qquad \delta\to0.
\tag{3}
\]
The result concerns periodic solutions and not arbitrary boundary-convergent trajectories or stochastic finite populations.

## Assumptions and scope

The model has cooperation frequency \(x\in(0,1)\), adaptive cooperator multiplier \(r\in(\alpha,\beta)\), group size \(N\ge2\), \(1<\alpha<\beta<N\), defector multiplier \(0<r_d\le\alpha\), feedback speed \(\varepsilon>0\), and payoff-balancing parameter \(\theta>0\). The exogenous multiplier \(w(t)>0\) is piecewise continuous and periodic with period \(T>0\), with ordinary smoothness near solutions as needed for differential equations; the constructive example uses analytic forcing. The unit-contribution payoff formulas of [1] are
\[
P_D(x,w)=\frac{r_d}{N}\,B_N(x,w),\qquad
P_C(x,r,w)=\frac rN\bigl[1+wB_N(x,w)\bigr]-1,
\tag{4}
\]
where \(B_N(x,w)=\mathbb E[\sum_{j=0}^{K-1}w^j]\) and \(K\sim\operatorname{Binomial}(N-1,x)\). The empty sum is zero. Equivalently,
\[
B_N(x,w)=
\begin{cases}
\displaystyle\frac{[1+(w-1)x]^{N-1}-1}{w-1},&w\ne1,\\
(N-1)x,&w=1.
\end{cases}
\tag{5}
\]
For all \(x\in(0,1)\), \(w>0\), and \(r_d>0\), one has \(P_D>0\). The dynamics are
\[
\dot x=x(1-x)(P_C-P_D),\qquad
\dot r=\varepsilon(r-\alpha)(\beta-r)
\bigl[-xP_C+\theta(1-x)P_D\bigr].
\tag{6}
\]
A periodic orbit here means a \(T\)-periodic \((x,r)\) remaining in a compact subset of the stated open rectangle. External forcing is \(T\)-periodic as well. A constant environment has the interior cooperation equilibrium coordinate \(x_*\) whenever a physical interior equilibrium exists; its adaptive multiplier can depend on the chosen constant environment [1,2]. The fixed-reference quantity in (1)–(3) is this \(x_*\), not a seasonally averaged equilibrium multiplier.

## Proof

**1. Exact coboundary.** On the open rectangle define the real-valued observable
\[
H(x,r)=\frac{1}{\varepsilon(\beta-\alpha)}
\log\frac{r-\alpha}{\beta-r}-\log(1-x).
\tag{7}
\]
The fundamental theorem of calculus and (6) give
\[
\begin{aligned}
\frac{dH}{dt}
&=\bigl[-xP_C+\theta(1-x)P_D\bigr]
+x(P_C-P_D)\\
&=[\theta-(1+\theta)x]P_D.
\end{aligned}
\tag{8}
\]
No step assumes a constant environment, a particular waveform, or a small perturbation. On a periodic orbit, \(H(T)=H(0)\), so
\(\int_0^T[\theta-(1+\theta)x(t)]P_D(t)\,dt=0\).
The denominator in (1) is positive, yielding (1). In particular a nonconstant \(x\) must take values strictly on both sides of \(x_*\).

**2. Pairwise rigidity.** For \(N=2\), one other player is sampled. Consequently \(B_2(x,w)=x\), **for every positive \(w\)**, and hence \(P_D=r_d x/2\). Substitution into (8), integration and division by the strictly positive factor \(r_d(1+\theta)T/2\) give
\[
\overline{x^2}=x_*\bar x.
\tag{9}
\]
Subtracting \(\bar x^2\) proves (2). A continuous nonconstant periodic \(x\) has strictly positive variance; since \(\bar x>0\), equation (2) forces \(\bar x<x_*\). This is an equality valid at **finite oscillation amplitude**, rather than an approximation obtained by linearizing about an equilibrium. It is specific to the pairwise reduction when a varying \(w\) is present; for \(N>2\) formula (1) remains valid but \(P_D\) generally depends on \(w\).

**3. Explicit nonconstant seasonal orbits.** Set
\[
N=2,\quad \alpha=\frac65,\quad \beta=\frac95,
\quad r_d=1,\quad\theta=1,\quad\varepsilon=10,
\quad w_\delta(t)=1+\delta\cos t.
\tag{10}
\]
All positivity and multiplier inequalities in the assumptions hold for sufficiently small \(|\delta|<1\). At \(\delta=0\), equations (6) have the interior equilibrium
\((x,r)=(1/2,5/3)\). In \((x,r)\) coordinates its exact Jacobian and determinant are
\[
J=\begin{pmatrix}
1/12&3/16\\
-56/135&-7/30
\end{pmatrix},\qquad
\operatorname{tr}J=-\frac3{20}<0,\qquad
\det J=\frac7{120}>0.
\tag{11}
\]
Thus its eigenvalues have strictly negative real parts and the period-\(2\pi\) return-map derivative has no eigenvalue 1. The smooth implicit-function theorem applied to that return map provides a unique nearby interior \(2\pi\)-periodic solution for every sufficiently small \(\delta\), and its Floquet multipliers remain strictly inside the unit circle. It is not constant for \(\delta\ne0\): if \(x\) were constant, the periodicity of \(r\), its feedback equation, and \(P_D=x/2>0\) would force \(x=1/2\) and then \(r\) constant, whereas \(P_C-P_D=0\) would demand \(r[1+w_\delta(t)x]/2-1=x/2\) for every \(t\), which is impossible for nonconstant \(w_\delta\).

**4. Quantitative small-seasonality coefficient.** The forcing derivative of the vector field at the unforced equilibrium is
\[
B=\left(\frac5{48},-\frac7{54}\right)^{\!T}.
\tag{12}
\]
Writing the first-order periodic response as
\(x(t)=1/2+\delta\xi(t)+O(\delta^2)\), one obtains
\[
\binom{\dot\xi}{\dot\zeta}
=J\binom\xi\zeta+B\cos t.
\tag{13}
\]
The first component of the complex frequency response is
\[
G=\bigl[(iI-J)^{-1}B\bigr]_1
=\frac{i(5/48)}{7/120-1+3i/20},
\qquad |G|^2=\frac{625}{52372}.
\tag{14}
\]
Hence \(\overline\xi=0\) and
\(\operatorname{Var}_{2\pi}(x)=\delta^2|G|^2/2+O(\delta^3)\).
The exact variance identity (2) and \(\bar x\to1/2\) imply (3). The remainder arises from smooth dependence of the periodic solution on \(\delta\). This completes all parts of the theorem.

The same coboundary also gives, for every finite time \(L>0\) along an interior trajectory, the exact identity
\[
\int_0^L[\theta-(1+\theta)x(t)]P_D(t)\,dt=H(L)-H(0),
\tag{15}
\]
and for any compactly interior invariant distribution in the time-periodic skew-product system it yields (1) with integration replaced by expectation. The periodic-orbit theorem above does not require this extension.

## Verification

The companion `verify.py` checks (8) symbolically with generic payoffs, checks the binomial reduction in (4) for \(N=2,\ldots,8\), verifies the exact equilibrium and matrices (11)–(12), and reconstructs the rational number (14). Independent numerical Poincaré shooting at \(\delta=0.04,0.08,0.12,-0.12\) reproduces the strict deficit and verifies (2). At \(\delta=0.12\), the numerical orbit has \(\bar x\approx0.499828306469\) and \(\operatorname{Var}(x)\approx0.000085817286862\), consistent with the predicted identity to within numerical quadrature error. These finite calculations corroborate the closed-form reasoning; the existence theorem uses the implicit-function theorem, not numerical shooting.

Reproduction: install dependencies in `requirements.txt` and run `python verify.py` from the directory containing the two files. No network data or externally prepared certificate is required.

## Relationship to prior work

Jiang et al. [1] formulate the nonlinear public-goods payoffs, asymmetric environmental feedback, and externally changing synergy, and investigate equilibrium stability and numerically observed oscillatory behavior for multi-person groups. Shao, Wang, and Fu [2] introduce the earlier asymmetric-feedback public-goods framework with a constant linear synergy law and identify the interior equilibrium coordinate \(\theta/(1+\theta)\). Those contributions are the basis of this result, not new claims here.

Equations (1), (2), and the seasonally forced nonvacuity and coefficient (3) address a different quantitative question: the **time-integrated cooperation level** of recurrent behavioral fluctuations versus the model's stationary reference. In the accessible primary main texts and relevant mathematical-search records, no theorem implying this all-amplitude payoff-weighted law or the pairwise strict time-mean loss was identified. Source supplements not fully accessible and equivalent derivations under alternate terminology remain bibliographic risks; these searches do not certify exhaustive novelty.

## Limitations

The strict ordinary time-mean deficit is proved for the pairwise case \(N=2\); the all-group result is payoff-weighted rather than an unqualified inequality for ordinary time averages. The branch construction only guarantees small nonzero sinusoidal forcing in the explicit parameter family and local attraction near the branch, not existence or global attraction for all forcing parameters. No conclusion is asserted for trajectories approaching \(x=0,1\) or \(r=\alpha,\beta\), stochastic processes, nonperiodic forcings without an invariant probability distribution, or mechanisms outside equations (4)–(6). The proof is independently reproducible in its algebraic steps but has not undergone an independent mathematical audit.

## References

[1] Y. Jiang, X. Wang, L. Liu, M. Wei, J. Zhao, Z. Zheng, and S. Tang, “Nonlinear eco-evolutionary games with global environmental fluctuations and local environmental feedbacks,” *PLOS Computational Biology* **19** (2023), e1011269, https://doi.org/10.1371/journal.pcbi.1011269; first public preprint, arXiv:2212.06497, December 13, 2022, https://arxiv.org/abs/2212.06497.

[2] Y. Shao, X. Wang, and F. Fu, “Evolutionary dynamics of group cooperation with asymmetrical environmental feedback,” *Europhysics Letters* **126** (2019), 40005, https://doi.org/10.1209/0295-5075/126/40005; arXiv:1904.11081, April 24, 2019, https://arxiv.org/abs/1904.11081.
