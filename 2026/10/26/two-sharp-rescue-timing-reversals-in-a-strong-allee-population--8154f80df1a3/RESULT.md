# Two sharp rescue-timing reversals in a strong-Allee population

## Finding
For the classical bistable, density-normalized strong-Allee equation
\[
\dot x=r x(x-a)(1-x),\qquad r>0,\quad 0<a<1,
\]
let \(\Phi_t(x)\) be its time-\(t\) flow. Fix a single translocation pulse \(q\) and a planning horizon \(t\) satisfying
\[
0<q<\min\{a,1-a\},\qquad t>0.
\]
An **early** pulse yields \(E_t(x)=\Phi_t(x+q)\), whereas a **late** pulse yields \(L_t(x)=\Phi_t(x)+q\). For every such \((r,a,q,t)\), there are exactly two numbers
\[
0<x_-(t)<a-q<a<x_+(t)<1-q
\]
with
\[
\begin{aligned}
E_t(x)&>L_t(x)&&\text{if }x_-(t)<x<x_+(t),\\
E_t(x)&=L_t(x)&&\text{if }x=x_-(t)\text{ or }x=x_+(t),\\
E_t(x)&<L_t(x)&&\text{if }0\leq x<x_-(t)\text{ or }x_+(t)<x\leq1-q.
\end{aligned}
\]
The two equality points are distinct and simple. Moreover, writing \(z_t=\Phi_t^{-1}(1-q)\), one has \(a<x_+(t)<z_t<1-q\). Thus both reversals occur even if **both** post-pulse population levels must remain at or below carrying capacity.

Their short- and long-horizon limits are exact:
\[
\lim_{t\downarrow0}x_\pm(t)=
\frac{1+a}{3}-\frac q2\ \pm\frac13\sqrt{1-a+a^2-\frac{3q^2}{4}},
\qquad
\lim_{t\to\infty}x_-(t)=a-q,\quad
\lim_{t\to\infty}x_+(t)=a.
\]
In particular, the range where earlier stocking is better contracts toward the interval of initial populations for which stocking crosses the Allee threshold.

## Assumptions and scope
Here \(x\) is population density divided by carrying capacity, \(a\) is the unstable Allee threshold, and \(r\) sets the time scale. The flow is the unique classical solution on \([0,1]\); its fixed points \(0,a,1\) are respectively attracting, repelling and attracting. A fixed number of immigrants \(q\), expressed in the same carrying-capacity units, is inserted instantaneously, either at the beginning or at the end of one otherwise uncontrolled interval. Exactly one pulse is compared in each scenario, with the same \(x,q,t\). The strict pulse bound is a natural small-release condition ensuring that both a subthreshold and an above-threshold unaugmented interval exist. This is a deterministic, homogeneous, closed target-population model; donor dynamics, immigration mortality, stochastic extinction and release costs are outside its scope.

## Proof
Put \(f(x)=x(x-a)(1-x)\) and \(F=\Phi_t\). Scalar ODE uniqueness gives \(F'(x)>0\). Differentiating the variational equation yields
\[
\frac{F''(x)}{F'(x)}=r\int_0^t f''(\Phi_s(x))\Phi_s'(x)\,ds.
\]
Whenever \(f(x)\ne0\), autonomy gives \(\Phi_s'(x)=f(\Phi_s(x))/f(x)\), hence the last expression equals
\[
\frac{f'(F(x))-f'(x)}{f(x)}.
\]
Because \(f'(u)=-3u^2+2(1+a)u-a\), this becomes
\[
\frac{F''(x)}{F'(x)}=
\left[2(1+a)-3\{F(x)+x\}\right]
\frac{F(x)-x}{f(x)}.
\]
The final quotient extends continuously across each fixed point: indeed
\[
\frac{F(x)-x}{f(x)}=r\int_0^t\Phi_s'(x)\,ds>0.
\]
This proves for **all** \(x\in[0,1]\) that
\[
\operatorname{sgn}F''(x)=
\operatorname{sgn}\left(\frac{2(1+a)}3-x-F(x)\right).
\]
The map \(x\mapsto x+F(x)\) is strictly increasing from \(0\) to \(2\). There is therefore one inflection \(c_t\in(0,1)\) satisfying \(c_t+F(c_t)=2(1+a)/3\). Accordingly \(F'\) is strictly increasing before \(c_t\) and strictly decreasing after it.

Set \(D(x)=F(x+q)-F(x)\) on \([0,1-q]\). Its derivative is \(D'(x)=F'(x+q)-F'(x)\). If both arguments are below \(c_t\), then \(D'>0\); if both are above, then \(D'<0\). When \(x<c_t<x+q\), the first term strictly decreases and the second strictly increases as \(x\) increases. Hence \(D'\) can change sign **at most once**, and only from positive to negative: \(D\) is unimodal (with strict increase then strict decrease whenever it has an interior maximum).

The endpoint comparisons are strict. Since \(q<a\), \(F(q)<q\) and therefore \(D(0)-q<0\). Since \(1-q>a\), \(F(1-q)>1-q\) and therefore \(D(1-q)-q<0\). At \(x=a-q\), \(F(x)<x\) and \(F(x+q)=a\), so \(D(x)>q\). At \(x=a\), \(F(x)=a\) and \(F(x+q)>x+q\), again \(D(x)>q\). A strictly unimodal function with these signs crosses level \(q\) exactly twice, in the claimed open intervals. The crossings are simple because the crossing intervals lie on the strictly increasing and strictly decreasing flanks, respectively. These signs prove the ordering in the finding.

For the non-overstocking statement, \(1-q>a\) implies \(F(1-q)>1-q\), whereas \(F(a)=a<1-q\). Hence \(z_t=F^{-1}(1-q)\) lies in \((a,1-q)\). At \(x=z_t\), the late response equals \(1\), while the early response is \(F(z_t+q)<1\). Therefore the upper crossing lies below \(z_t\). For all \(0\le x\le z_t\), both compared terminal population levels lie in \([0,1]\).

For \(t\downarrow0\), smooth dependence of the flow gives uniformly on \([0,1-q]\):
\[
\frac{D(x)-q}{rqt}\longrightarrow
\frac{f(x+q)-f(x)}q
=-3x^2+[2(1+a)-3q]x-a+(1+a)q-q^2.
\]
This concave quadratic has exactly the two roots displayed above, both in \((0,1-q)\) by the same strict endpoint and interior signs. The uniqueness of the two crossings and uniform convergence (or local implicit-function continuity at the simple roots) yield the short-horizon limits.

For \(t\to\infty\), \(F(x)\to0\) for every fixed \(0\le x<a\) and \(F(x)\to1\) for every fixed \(a<x\le1\). At each fixed \(x<a-q\), \(D(x)-q\to-q<0\), whereas at each fixed \(a-q<x<a\), \(D(x)-q\to1-q>0\). Thus \(x_-(t)\to a-q\). Likewise the difference tends to \(1-q>0\) when \(a-q<x<a\) and to \(-q<0\) for fixed \(a<x<1-q\), showing \(x_+(t)\to a\). This proves all stated assertions.

## Verification
The symbolic identity \([f'(y)-f'(x)]/(y-x)=2(1+a)-3(y+x)\) and the short-horizon quadratic are direct polynomial expansions, independently reproduced with symbolic algebra. The accompanying program `verify_allee.py` numerically integrates the autonomous ODE using strict tolerances, checks all endpoint and intermediate signs, locates both roots and tests representative parameters drawn from the full allowed domain; its random tests are finite corroboration, **not** a substitute for the analytic argument.

An exact soluble check occurs at \(a=1/2\), \(r=1\), \(q=1/5\) and \(t=2\log2\). With \(y=2x-1\), the flow is
\[
\Phi_t(x)=\frac12\left(1+\frac{y}{\sqrt{(1+y^2)/2}}\right),
\]
so both boundaries can be evaluated by one-dimensional bisection without integrating an ODE:
\[
x_-(t)\approx0.145029705606619,\qquad
x_+(t)\approx0.654970294393381.
\]
The intermediate value \(x=0.4\) gives \(E_t(x)-L_t(x)\approx0.077350098112615>0\), whereas \(x=0\) or \(x=0.8\) gives a negative difference (about \(-0.063803437554499\)). The two roots sum to \(0.8\) by reflection symmetry in this one example; this symmetry is not claimed for general \(a\).

## Relationship to prior work
Bodine, Gross and Lenhart (2008) use **the same cubic Allee growth law** in a continuous-time two-population species-augmentation optimal-control model. Their equations couple the target to a source population and their main mathematical output is a Pontryagin characterization with numerical control comparisons; the full paper does not state the fixed-single-pulse, all-horizon, two-density-switch theorem proved here. Bodine, Gross and Lenhart (2012) explicitly examine the order of augmentation and growth in **discrete-time** reserve-target models, deriving optimal-control conditions and presenting numerical scenarios; they provide essential conceptual prior art for order sensitivity but not the present exact two-crossing flow classification. Armstrong and Wittmer (2011) explain the ecological motivation for Allee-sensitive releases and their potential conservation costs. More general theorems about S-shaped scalar semiflows or rearrangements might imply aspects of this special cubic result; no mathematical claim of universal historical priority is made.

## Limitations
The theorem does not determine a globally optimal release schedule over arbitrary intervention times or several pulses; it compares only the two endpoints of one specified time interval. The strict small-pulse condition is essential to the stated guaranteed two-crossing domain; pulse sizes outside it are not classified. The result treats abundance, not probabilistic establishment or extinction; no donor-population depletion or release expenses enter the comparison. The short- and long-horizon limits do not assert monotone motion of the switching boundaries. Numerical root values are illustrative approximations; the universal result is proved analytically. Possible implication by broader published scalar-flow or impulse-scheduling theory remains an originality risk.

## References
1. E. N. Bodine, L. J. Gross, S. Lenhart, *Optimal control applied to a model for species augmentation*, Mathematical Biosciences and Engineering **5** (2008), 669–680, DOI: 10.3934/mbe.2008.5.669. Public 2008-10-01. Full paper: https://www.aimspress.com/aimspress-data/mbe/2008/4/PDF/1551-0018_2008_4_669.pdf.
2. E. N. Bodine, L. J. Gross, S. Lenhart, *Order of events matter: comparing discrete models for optimal control of species augmentation*, Journal of Biological Dynamics **6** (2012), 31–49, DOI: 10.1080/17513758.2012.697197. First available online 2012-06-28.
3. D. P. Armstrong, H. U. Wittmer, *Incorporating Allee effects into reintroduction strategies*, Ecological Research **26** (2011), 687–695, DOI: 10.1007/s11284-011-0849-9. Publisher abstract consulted.
