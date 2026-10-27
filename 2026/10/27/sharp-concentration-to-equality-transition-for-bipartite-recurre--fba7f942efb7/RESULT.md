# Sharp concentration-to-equality transition for bipartite recurrent boosters

## Finding
Consider two equally sized populations which transmit infection only across, and not within, the population boundary. Vaccination resets susceptibility to zero, after which individual susceptibility rises linearly to one in time \(\tau>0\):
\[
\sigma(a)=\min\{a/\tau,1\}.
\]
Individuals in population \(i\) are boosted periodically with frequency \(r_i\geq0\), with uniformly distributed booster phases. Fix the population-average disease-free vaccination rate \(v=(r_1+r_2)/2>0\), and let \(\rho\) be the Perron eigenvalue of the disease-free next-generation contact factor (the factor multiplying the unvaccinated reproduction number).

**Theorem (complete global allocation classification).** Write \(w=v\tau\). The minimum over **all** nonnegative frequency allocations satisfying the budget is
\[
\rho_{\min}(w)=
\begin{cases}
\sqrt{1-w},&0<w\leq\tfrac12,\\
\dfrac{1}{2\sqrt w},&\tfrac12\leq w\leq1,\\
\dfrac{1}{2w},&w\geq1.
\end{cases}
\]
For \(0<w<1\), the only optimal allocations give the *entire* booster budget to one population: \((r_1,r_2)=(2v,0)\) or \((0,2v)\). For \(w>1\), the *unique* optimal allocation is the equal split \(r_1=r_2=v\). At the critical value \(w=1\), **every** feasible split is optimal with \(\rho=1/2\).

For example, at \(w=1/2\), concentrating boosters gives \(\rho=1/\sqrt 2\), whereas equal allocation gives \(3/4\). At \(w=3/2\), equal allocation gives \(1/3\), whereas concentration gives \(1/\sqrt6\).

## Assumptions and scope
This is an exact theorem about the linear invasion factor evaluated at the **disease-free** stationary booster-age distribution. The populations have equal relative sizes and symmetric, strictly cross-population mixing; the normalized contact matrix is
\[
K=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Vaccines reset susceptibility completely, with linear waning and saturation at one. Each vaccinated population uses a deterministic inter-booster interval; different individuals have uniformly distributed phases so that the disease-free age distribution is stationary. Zero allocated frequency denotes an unboosted population, whose disease-free susceptibility is one. Dose budgets refer to vaccinations administered in the disease-free state, not to a constrained realized rate during an established epidemic. Both the population shares and all contact intensities are held fixed while optimizing.

## Proof
The susceptibility at a uniform age in a periodic booster interval of length \(1/r\) is
\[
S(r)=r\int_0^{1/r}\min\{a/\tau,1\}\,da
=F(\tau r),\qquad
F(x)=\begin{cases}1-x/2,&0\le x\le1,\\1/(2x),&x\ge1.\end{cases}
\]
The formula at zero follows by continuity: \(F(0)=1\). With \(x=\tau r_1\), \(y=\tau r_2\), and \(B=x+y=2w>0\), the invasion matrix is \(K\operatorname{diag}(F(x),F(y))\), so
\[
\rho^2=F(x)F(y),\qquad x,y\ge0,\quad x+y=B.
\]
It therefore suffices to minimize this product on a closed interval.

**Case \(0<B\le1\).** Both arguments are in the first branch, and
\[
F(x)F(y)=1-B/2+xy/4\ge1-B/2=F(B).
\]
For positive \(B\), equality holds only at \(xy=0\).

**Case \(1<B<2\).** If both arguments are at most one, \(xy\ge B-1\), whence
\[
F(x)F(y)\ge(3-B)/4>1/(2B)=F(B),
\]
since \((3-B)/4-1/(2B)=(B-1)(2-B)/(4B)>0\). If instead \(x\ge1\) and \(0\le y\le1\), then
\[
F(x)F(y)-F(B)=
\frac{y(1-B/2)}{2B(B-y)}\ge0,
\]
with equality only at \(y=0\) for \(B<2\). Interchanging \(x,y\) covers the other mixed branch. Thus precisely the two extreme allocations minimize.

**Case \(B=2\).** In every split at least one argument is at least one. With \(x=2-y\ge1\) and \(0\le y\le1\),
\[
F(x)F(y)=\frac{1-y/2}{2(2-y)}=\frac14.
\]
The opposite ordering is identical, so all splits tie exactly.

**Case \(B>2\).** When both arguments are at least one, the product is
\[
F(x)F(y)=\frac1{4xy}\ge\frac1{B^2},
\]
with equality exactly at \(x=y=B/2>1\). Otherwise choose \(y\le1\), so \(x=B-y>1\). The function
\[
F(x)F(y)=\frac{1-y/2}{2(B-y)}
\]
is strictly decreasing in \(y\in[0,1]\) because its derivative is \((1-B/2)/(2(B-y)^2)<0\). Therefore it is at least \(1/[4(B-1)]>1/B^2\), where the last strict inequality follows from \((B-2)^2>0\). Hence the equal allocation is uniquely optimal.

Inserting \(B=2w\) into the attained products, then taking the positive square root, gives exactly the claimed piecewise formula and all equality conditions. \(\square\)

## Verification
Run the accompanying dependency-free Python 3 program `verify.py`. It uses exact rational arithmetic to check the piecewise formula against more than 120,000 rational allocation/budget assertions, including boundary and uniqueness checks. The continuum statement is established by the inequalities above; finite sampling is computational corroboration, not a proof of global optimality.

## Relationship to prior work
Foutel-Rodier, Charpentier and Guérin (2023 preprint; 2025 journal article) derive the general renewal susceptibility and two-population next-generation matrix, and show that equal allocation is optimal for assortative or homogeneous contact mixing \(0\le\alpha\le1\). Their general contact parametrization also allows the fully disassortative endpoint \(\alpha=2\), but their Proposition 6 does **not** assert fairness optimality there. The theorem above fixes precisely that endpoint, a natural piecewise-linear waning profile and deterministic boosters, then globally solves the entire dose-rate budget range, including a flat continuum of optimizers at the transition.

Gavish and Katriel (2022) study sharp vaccine allocation transitions for **one-time leaky vaccination** optimizing the SIR final attack rate as transmissibility varies. That established qualitative motivation differs from the recurrent-booster, linearized invasion-factor problem and does not imply the formula or equality classification here. Gutjahr (2023) studies equity and final-size optimization in heterogeneous SIR vaccination; that objective also differs.

## Limitations
The complete optimization applies to exactly the specified symmetric, fully bipartite contact structure and clipped-linear waning curve. It is not a theorem for all disassortative matrices, waning laws, booster-interval distributions, or unequal group sizes. The disease-free spectral radius governs linear invasion and a branching-process survival threshold; no global stability or nonlinear endemic final-size claim is established. The result is mathematical and does not support inequitable allocation recommendations without clinical, ethical or logistical considerations. Priority against unexamined broader allocation theorems remains open.

## References
1. F. Foutel-Rodier, A. Charpentier and H. Guérin, *Optimal Vaccination Policy to Prevent Endemicity: A Stochastic Model*, arXiv:2306.13633 (first public version 23 June 2023); *Journal of Mathematical Biology* 90, 10 (2025), doi:10.1007/s00285-024-02171-z.
2. N. Gavish and G. Katriel, *Optimal vaccination at high reproductive numbers: sharp transitions and counter-intuitive allocations*, arXiv:2202.03909 (6 February 2022); *Proceedings of the Royal Society B* 289, 20221525 (2022).
3. W. J. Gutjahr, *Fair and efficient vaccine allocation: A generalized Gini index approach*, *Production and Operations Management* 32 (2023), doi:10.1111/poms.14080.
