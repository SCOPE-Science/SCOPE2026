# An integrable neutral-cycle family with sharp average-risk amplification in symmetric collective-risk games

## Finding

Consider the linear-feedback collective-risk evolutionary game of Liu, Chen, and Szolnoki. When the group size is odd, the collective goal is exactly balanced, and the relative growth coefficient of risk is one, its interior coexistence equilibrium is a **nonlinear center**, not an isolated attracting or repelling Hopf cycle. An explicit first integral produces an annulus of genuine nonconstant periodic cooperation–risk trajectories. On every such orbit the mean cooperation is exactly one half, but the mean failure risk strictly exceeds the equilibrium risk, with an exact sharp variance-scale lower bound.

More precisely, for every integer \(a\ge 1\), \(b,c,\varepsilon>0\), put
\[
N=2a+1,\quad M=a+1,\quad k=b\binom{2a}{a},\quad r_*=\frac{4^a c}{k}.
\]
Assume \(0<r_*<1\). On the open unit square consider
\[
\varepsilon\dot x=x(1-x)\bigl(k[x(1-x)]^a r-c\bigr),
\qquad \dot r=r(1-r)(1-2x).
\]
The only interior equilibrium is \(E=(1/2,r_*)\); it is a nondegenerate center enclosed by a full punctured neighborhood of periodic trajectories. For **every** nonconstant periodic trajectory, averaging in the original physical time over one period gives
\[
\overline{x}=\frac12,\qquad
\overline r=r_*\,\overline{\bigl(1-4(x-\tfrac12)^2\bigr)^{-a}}
>r_*\bigl[1+4a\operatorname{Var}(x)\bigr]>r_*.
\]
The coefficient \(4a r_*\) multiplying the variance is optimal uniformly over these periodic trajectories: as the nonconstant orbits shrink to \(E\), the ratio \((\overline r-r_*)/\operatorname{Var}(x)\) tends to \(4a r_*\). Moreover, writing \(A(x)=k[x(1-x)]^a\), the period covariance satisfies
\[
\operatorname{Cov}(A(x),r)
=c\left[1-\overline{A(x)}\,\overline{1/A(x)}\right]<0.
\]
Thus cyclic maintenance of exactly the equilibrium mean cooperation incurs a strictly higher time-mean failure risk, and the penalty is quantitatively tied to the fluctuations of cooperation.

## Assumptions and scope

The contact group is well mixed, with \(2a+1\ge3\) participants and success threshold \(a+1\). The benefit/endowment \(b\), cooperation cost \(c\), and strategy timescale \(\varepsilon\) are positive; the risk-growth parameter in the linear-feedback law is fixed at \(u=1\). The natural interior-existence hypothesis is \(4^ac<b\binom{2a}{a}\). The dynamics are continuous time and deterministic, and both state variables remain strictly between zero and one. Bars denote averages \(P^{-1}\int_0^P\cdot\,dt\) over the *actual physical-time period* \(P>0\). Variance and covariance refer to this time-uniform measure. Nothing is asserted about the nonlinear/sigmoid feedback law, even group sizes, unequal target counts, or arbitrary \(u\).

## Proof

**1. A conserved quantity.** Write \(s=x(1-x)\), \(q(r)=(1-r)/r\), and \(\lambda=ac/\varepsilon>0\). On \((0,1)^2\), define
\[
H(x,r)=\frac{q(r)^\lambda}{s^a}
+\frac{ak}{\varepsilon}\int_{1/2}^{r}
\frac{q(v)^\lambda}{1-v}\,dv.
\]
This is a well-defined smooth real-valued function; the integral is over a compact subinterval of \((0,1)\) for each point. Direct differentiation yields
\[
H_x=-\frac{a q(r)^\lambda(1-2x)}{s^{a+1}},\qquad
H_r=\frac{a q(r)^\lambda(ks^a r-c)}{\varepsilon s^a r(1-r)}.
\]
Substitution of the displayed differential equations gives \(H_x\dot x+H_r\dot r=0\), with the two terms cancelling exactly. The identity extends across \(x=1/2\), since no division by \(1-2x\) was used.

**2. A genuine center and a period annulus.** At any interior equilibrium \(\dot r=0\) forces \(x=1/2\), and then \(\dot x=0\) forces \(r=r_*\). At \(E\), both first derivatives of \(H\) vanish. Setting \(q_*=q(r_*)\), the Hessian is diagonal with
\[
H_{xx}(E)=2a\,4^{a+1}q_*^\lambda>0,
\qquad
H_{rr}(E)=\frac{a c\,4^a q_*^\lambda}
{\varepsilon(1-r_*)r_*^2}>0,
\qquad H_{xr}(E)=0.
\]
Hence \(E\) is a nondegenerate strict local minimum of \(H\). By the local Morse lemma (equivalently the quadratic normal form for a smooth nondegenerate minimum), all sufficiently small positive regular levels \(H=H(E)+h\) are disjoint simple closed curves surrounding \(E\). Their points lie in \((0,1)^2\), and the vector field never vanishes on them because \(E\) is the sole interior equilibrium. Invariance of \(H\), uniqueness of solutions, and nonzero continuous speed on each compact curve imply a finite-period orbit on every such level. This proves actual nonconstant cycles, rather than merely inferring cycles from imaginary eigenvalues or a numerical diagram.

**3. Exact physical-time averages.** Periodicity and \(0<x,r<1\) give
\[
0=\overline{\frac{d}{dt}\log\frac r{1-r}}=1-2\overline x,
\quad\text{so }\overline x=1/2.
\]
Set \(A(x)=ks^a\), and choose any primitive \(F\) satisfying \(F'(x)=1/[x(1-x)A(x)]\). The strategy equation implies
\[
\frac{dF(x)}{dt}=\frac1\varepsilon\left(r-\frac c{A(x)}\right).
\]
Its period integral therefore gives \(\overline r=c\,\overline{1/A(x)}\). Because \(s=\tfrac14-(x-\tfrac12)^2\), this is precisely the risk formula in the finding. A second period identity, obtained from \(d\log(x/(1-x))/dt=(A(x)r-c)/\varepsilon\), is \(\overline{A(x)r}=c\). Combining them gives the covariance identity. Strictly negative covariance follows from strict Cauchy–Schwarz, since \(A(x)\) cannot be constant along a nonconstant continuous periodic orbit (the trajectory's \(x\)-range contains an interval and \(A\) is nonconstant on every interval).

**4. The optimal variance coefficient.** Put \(y=x-1/2\), so \(|y|<1/2\). The elementary strict Bernoulli inequality
\[
(1-z)^{-a}>1+az\quad\text{for }0<z<1,
\]
with equality at \(z=0\), applied to \(z=4y^2\), yields
\[
\overline r-r_*
=r_*\overline{(1-4y^2)^{-a}-1}
>4a r_*\overline{y^2}=4a r_*\operatorname{Var}(x).
\]
The strictness uses nonconstancy and \(\overline{x}=1/2\). On the nested local period annulus from Step 2, \(\max|y|\to0\) at the center. Uniform Taylor expansion gives \((1-4y^2)^{-a}=1+4ay^2+O(y^4)\), and \(\overline{y^4}\le(\max|y|)^2\overline{y^2}\). Dividing the gap by the positive variance proves its stated limiting coefficient and therefore the impossibility of increasing the universal coefficient for this family. No global orbit existence or uniqueness result is required.

## Verification

The accompanying `verify.py` checks the derivative cancellation for symbolic positive parameters and integer exponent, the nondegenerate Hessian, and the strict convex/variance inequality. It also numerically closes small periodic orbits for three independent balanced-group sizes, integrating over one *detected full period*, and checks the two physical-time average identities and the variance bound. Numerical quadrature is supplementary; all quantified claims above are proved analytically. Run `python verify.py` with SymPy, NumPy, and SciPy available. There is no external dataset and no finite enumeration purporting to establish the statements for all integers.

## Relationship to prior work

Liu, Chen, and Szolnoki (2023), arXiv:2305.00253v1 and eLife 12:e82954, introduced exactly this collective-risk payoff and linear feedback, gave the interior fixed point and critical feedback condition \(u=(M-1)/(N-M)\), and studied oscillatory behavior and local Hopf analysis. In the balanced odd-group subfamily this critical condition reads \(u=1\). The present contribution is the **explicit first integral and nonisolated neutral center**, plus the **exact time-mean risk law, strict negative covariance, and sharp cycle-variance coefficient**; none is inferred from the earlier equilibrium/Jacobian formulas alone. The original publication's equations (3)–(7), Results, and relevant appendices were inspected for equivalent statements and stronger coverage. The wider game-environment-feedback theory of Weitz et al. (2016) and Tilman et al. (2020) discusses oscillation and stability for different, principally pairwise, payoff models, not an explicit invariant for this binomial collective-risk subfamily. Searches of available mathematical research records did not identify a direct equivalent. General mathematical techniques such as integrating factors, planar first integrals, and Jensen/Bernoulli inequalities are standard and are not claimed as inventions.

## Limitations

The integrability and center assertion requires exact balance of both the binomial gain polynomial and risk feedback. Neutral cycles are not attracting; their persistence under arbitrary perturbations of group threshold or feedback balance is **not** claimed. The strict average-risk statement applies to full nonconstant interior periodic orbits, not to arbitrary transient observation windows, boundary heteroclinic orbits, or discrete stochastic populations. The variance coefficient is optimal in the small-orbit limit, not an exact equality for a finite-amplitude nonconstant cycle. No priority or independent proof certification is asserted; unidentified general results in the broad eco-evolutionary games literature remain a residual originality risk.

## References

1. Linjie Liu, Xiaojie Chen, and Attila Szolnoki, *Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game*, arXiv:2305.00253v1 (first public 2023-04-29); eLife 12:e82954 (2023), DOI:10.7554/eLife.82954. Full text: https://journal-symfony7.elifesciences.org/articles/82954 ; preprint: https://arxiv.org/html/2305.00253v1.
2. Joshua S. Weitz et al., *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, Proceedings of the National Academy of Sciences 113 (2016), DOI:10.1073/pnas.1604096113. Abstract and accessible indexed sections: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/.
3. Andrew R. Tilman et al., *Evolutionary games with environmental feedbacks*, Nature Communications 11 (2020), DOI:10.1038/s41467-020-14531-6. Indexed model description: https://www.nature.com/articles/s41467-020-14531-6.
