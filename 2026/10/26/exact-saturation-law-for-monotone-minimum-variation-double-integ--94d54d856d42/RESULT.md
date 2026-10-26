# Exact saturation law for monotone minimum-variation double-integrator controls

## Finding

Consider the double integrator \(y''(t)=u(t)\) on \([0,1]\), with \(y(0)=0\), \(y'(0)=1\), \(y(1)=0\), and \(y'(1)=0\). Impose the amplitude cap \(|u(t)|\le U\) almost everywhere. The full boundary-value problem is feasible if and only if \(U\ge 1+\sqrt{2}\).

Within the class of nondecreasing controls \(u\in BV(0,1)\), the exact minimum total variation is

\[
\min \operatorname{TV}(u)=
\begin{cases}
\dfrac{(U-1)^2}{U-2}, & 1+\sqrt{2}\le U\le 3,\\[5pt]
4, & U\ge 3.
\end{cases}
\]

For \(1+\sqrt{2}\le U\le3\), the unique minimizer (up to equality almost everywhere) is the one-jump control
\[
u(t)=\begin{cases}-U,&0<t<\dfrac{1}{U-1},\\[4pt]\dfrac{1}{U-2},&\dfrac{1}{U-1}<t<1.\end{cases}
\]
For \(U\ge3\), it is \(u(t)=-3\) on \((0,1/2)\) and \(u(t)=1\) on \((1/2,1)\). The two formulas agree at \(U=3\).

## Assumptions and scope

The control is measurable, of bounded variation, nondecreasing, and satisfies the pointwise cap \(|u|\le U\) almost everywhere. The state is absolutely continuous with \(y''=u\) almost everywhere and the four boundary conditions stated above. Total variation is the distributional variation on the open interval; the displayed step controls have one interior jump and no endpoint jump cost. The feasibility threshold is proved for all bounded controls, while the minimum-variation classification is only over the nondecreasing subclass. No global optimality claim is made for nonmonotone controls.

## Proof

Integrating the state equation gives the equivalent moment constraints
\[
\int_0^1u(t)\,dt=-1,\qquad \int_0^1t u(t)\,dt=0.
\]
For feasibility, fix \(U\ge1\) and maximize \(\int_0^1 t u(t)\,dt\) subject to \(\int_0^1u=-1\) and \(|u|\le U\). To justify the maximizer, let \(u^*=-U\) on \((0,\tau)\) and \(u^*=U\) on \((\tau,1)\), where \(\tau=(U+1)/(2U)\) makes its integral equal to \(-1\). For every feasible \(u\), \(\int(u-u^*)=0\), and \( (t-\tau)(u(t)-u^*(t))\le0\) on both sides of \(\tau\); hence \(\int t u\le\int t u^*\). The maximum moment is \(U(1-2\tau^2)/2\). It is nonnegative exactly when \(U\ge1+\sqrt2\). Below that threshold no feasible control can have the required zero first moment. At and above the threshold, a convex combination of the constant control \(u=-1\) and the maximizing bang-bang control realizes zero first moment while preserving the mean and cap; the step controls displayed above also give explicit feasible examples throughout the claimed ranges.

Now restrict to nondecreasing \(u\), and let \(\mu=Du\) be its nonnegative distributional derivative measure, with mass \(T=\mu((0,1))=\operatorname{TV}(u)\). Write \(c=u(0+)\). Fubini's theorem gives
\[
\int_0^1u=c+\int(1-s)\,d\mu(s),\qquad
\int_0^1tu=\frac c2+\frac12\int(1-s^2)\,d\mu(s).
\]
Eliminating \(c\) using the two moment constraints yields
\[
\int_0^1 s(1-s)\,d\mu(s)=1.
\]
Set \(m=\int(1-s)\,d\mu(s)\). Then \(c=-1-m\), so the lower amplitude bound implies \(m\le U-1\). Also \(m>1\), since \(1=m-\int(1-s)^2d\mu\) and the latter square integral cannot vanish when the weighted moment equals one. By Cauchy–Schwarz,
\[
\int(1-s)^2d\mu(s)\ge \frac{m^2}{T},
\]
whence \(1\le m-m^2/T\) and \(T\ge m^2/(m-1)\). The function \(q\mapsto q^2/(q-1)\) is decreasing on \((1,2]\). Therefore, for \(1+\sqrt2\le U\le3\),
\[
T\ge \frac{(U-1)^2}{U-2}.
\]
Equality requires \(m=U-1\) and equality in Cauchy–Schwarz, so \(\mu\) is a single atom at \(\tau=1/(U-1)\), of mass \((U-1)^2/(U-2)\). The resulting levels are \(-U\) and \(1/(U-2)\). The latter lies in \([-U,U]\) exactly when \(U\ge1+\sqrt2\), so the lower bound is attained throughout this range.

For \(U\ge3\), the identity \(\int s(1-s)d\mu=1\) and the bound \(s(1-s)\le1/4\) imply \(T\ge4\). Equality forces \(\mu=4\delta_{1/2}\), which gives the unique control \(-3\) followed by \(+1\). This control is feasible exactly when \(U\ge3\), completing the proof.

## Verification

The moment constraints are checked directly for both candidate controls. In the capped regime, with \(\tau=1/(U-1)\) and \(b=1/(U-2)\), exact algebra gives \(-U\tau+b(1-\tau)=-1\), \(-U\tau^2/2+b(1-\tau^2)/2=0\), and \(-U+(U-1)^2/(U-2)=b\). At \(U=3\), \(\tau=1/2\), \(b=1\), and the variation is \(4\). The feasibility threshold follows from the extremal first-moment calculation above, not from numerical sampling. The proof establishes uniqueness only within the nondecreasing class.

## Relationship to prior work

Kaya's *Optimal Control of the Double Integrator with Minimum Total Variation* studies the same boundary-value problem without an amplitude cap. For these boundary data its pure-TV solution is the midpoint step \((-3,+1)\) with variation \(4\), and the minimum-energy control has variation \(6\). The present formula recovers that solution for \(U\ge3\) and gives the exact cap-dependent monotone benchmark for \(1+\sqrt2\le U<3\), which the unconstrained result does not state. Manns and Schiemann study TV-regularized integer-valued controls on multidimensional domains; that is related in motivation but is a different feasible class and does not supply this capped double-integrator law.

## Limitations

The minimum-TV result is restricted to nondecreasing controls; it does not rule out a lower-TV nonmonotone control under the same cap. The range \(U<1+\sqrt2\) is infeasible for the full boundary-value problem. The result concerns pure total-variation minimization, not the combined energy-plus-TV objective. Related literature on bounded-variation control and switching costs may contain adjacent results; the checked sources did not reveal this exact cap-dependent formula. No independent audit is claimed.

## References

1. C. Y. Kaya, “Optimal Control of the Double Integrator with Minimum Total Variation,” *Journal of Optimization Theory and Applications* 185 (2020), 966–981; first public preprint dated 2019-01-01. https://arxiv.org/abs/1901.00491
2. P. Manns and A. Schiemann, “On Integer Optimal Control with Total Variation Regularization on Multi-dimensional Domains,” arXiv:2212.12226 (2022). https://arxiv.org/abs/2212.12226
