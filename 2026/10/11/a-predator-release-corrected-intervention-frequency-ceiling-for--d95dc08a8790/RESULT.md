# A predator-release-corrected intervention-frequency ceiling for a ratio-dependent impulsive cycle
## Finding
Consider the Shi–Wang–Li–Cheng nondimensional model between interventions,
\[
\dot x=x(x-\alpha)(1-x)-\frac{\lambda xy}{x+y},\qquad
\dot y=\frac{\lambda_1xy}{x+y}-\beta y,
\]
with a state-triggered intervention at \(x=h\):
\[
x^+=(1-p)h,\qquad y^+=(1-q)y+\tau.
\]
For every strictly positive order-one periodic orbit, parametrized from immediately after one intervention to its next threshold hit after time \(T\),
\[
L:=\log\!\frac1{1-p}
=\int_0^T\!\left[(x-\alpha)(1-x)-\frac{\lambda y}{x+y}\right]dt.
\]
Define
\[
\rho(\alpha,h)=\sup_{0<x<h}(x-\alpha)(1-x)
=\begin{cases}
(h-\alpha)(1-h),&\alpha<h\le(1+\alpha)/2,\\
(1-\alpha)^2/4,&(1+\alpha)/2<h<1.
\end{cases}
\]
The predator reset gives \(y(0)=(1-q)y(T^-)+\tau>\tau\), while the continuous equation gives \(\dot y\ge-\beta y\). Hence \(y(t)>\tau e^{-\beta t}\). Before the first return one also has \(x(t)<h\). Consequently,
\[
L<F(T):=\rho T-\frac{\lambda}{\beta}\log\!\frac{h+\tau}{h+\tau e^{-\beta T}}.
\]
This is a release-corrected necessary condition for any positive order-one cycle. It implies the simpler explicit floor
\[
T>\frac{L}{\rho}.
\]
If
\[
\rho\ge\frac{\lambda\tau}{h+\tau},
\]
then \(F\) is strictly increasing on \((0,\infty)\), so the equation \(F(T_*)=L\) has a unique solution \(T_*>0\), and every positive order-one cycle satisfies
\[
T>T_*.
\]
For the source example \((\alpha,h,p,\lambda,\beta,\tau)=(0.1,0.61,0.27,0.5,0.55,0.18)\),
\[
T_*=2.3686218445\ldots,
\]
whereas the coarse bound is \(T>1.5541271350\ldots\). Thus the intervention frequency obeys \(T^{-1}<0.4221864298\ldots\). At the reported economic optimum \((\alpha,h,p,\lambda,\beta,\tau)=(0.1,0.46,0.0878,0.5,0.55,0.0737)\),
\[
T_*=0.6782308510\ldots,
\]
versus the coarse bound \(T>0.4727161250\ldots\), giving \(T^{-1}<1.4744242297\ldots\).

## Assumptions and scope
Assume \(0<\alpha<h<1\), \(0<p,q<1\), and \(\lambda,\lambda_1,\beta,\tau>0\). The result is conditional on existence of a strictly positive order-one periodic orbit. Time \(0\) is immediately after its impulse and \(T^-\) is the next threshold hit, so
\[
x(0)=(1-p)h,\quad x(T^-)=h,\quad y(0)=(1-q)y(T^-)+\tau.
\]
Because this is the first threshold return, \(x(t)<h\) on \(0<t<T\). The source's stronger geometric hypotheses used to prove existence and stability are not re-proved here. No statement is made about higher-order cycles or boundary trajectories.

## Proof
Dividing the prey equation by \(x(t)>0\) gives
\[
\frac{d}{dt}\log x=(x-\alpha)(1-x)-\frac{\lambda y}{x+y}.
\]
Integration over one continuous leg yields
\[
\log\frac{x(T^-)}{x(0)}=\log\!\frac1{1-p}=L,
\]
which proves the exact budget.

The function \(g(x)=(x-\alpha)(1-x)\) is concave with vertex \((1+\alpha)/2\), giving the displayed formula for \(\rho\). For the predator,
\[
\dot y=y\left(\frac{\lambda_1x}{x+y}-\beta\right)\ge-\beta y.
\]
The reset and positivity give \(y(0)>\tau\), so Grönwall's inequality yields
\[
y(t)>\tau e^{-\beta t}.
\]
Since \(x(t)<h\) before the first return and \(y/(x+y)\) increases with \(y\) and decreases with \(x\),
\[
\frac{y(t)}{x(t)+y(t)}>
\frac{\tau e^{-\beta t}}{h+\tau e^{-\beta t}}.
\]
Therefore
\[
L<\rho T-\lambda\int_0^T\frac{\tau e^{-\beta t}}{h+\tau e^{-\beta t}}dt
=\rho T-\frac{\lambda}{\beta}\log\!\frac{h+\tau}{h+\tau e^{-\beta T}}=F(T).
\]
The correction term is positive, so \(L<F(T)<\rho T\), proving \(T>L/\rho\).

Finally,
\[
F'(T)=\rho-\frac{\lambda\tau e^{-\beta T}}{h+\tau e^{-\beta T}}.
\]
The fraction on the right is strictly decreasing in \(T\). Thus, if \(\rho\ge\lambda\tau/(h+\tau)\), then \(F'(T)>0\) for every \(T>0\). Also \(F(0)=0\) and \(F(T)\to\infty\). Since \(L>0\), exactly one \(T_*>0\) solves \(F(T_*)=L\); strict \(L<F(T)\) then forces \(T>T_*\).

## Verification
The companion script `verify.py` evaluates the exact formulas, checks the monotonicity condition at the two reported parameter sets, and brackets then bisects the unique roots of \(F(T)=L\). It returns
\[
T_*=2.3686218444908107\ldots
\]
for \((0.1,0.61,0.27,0.5,0.55,0.18)\), and
\[
T_*=0.6782308509533814\ldots
\]
for \((0.1,0.46,0.0878,0.5,0.55,0.0737)\). No trajectory integration or finite search is used in the proof.

## Relationship to prior work
The 2019 source formulates this exact ratio-dependent state-feedback model, proves existence and stability results for order-one cycles, and numerically studies their periods and an economic objective divided by period. Its Floquet calculation integrates logarithmic derivatives, but the article does not state the exact prey-reset budget as a stand-alone constraint and does not derive either the release-corrected inequality above or its period floor.

The 2017 Wei–Liu–Chen article uses the same ratio-dependent Allee continuous dynamics but triggers impulses at a predator threshold and multiplicatively harvests both populations. Full-text comparison shows period variation and Floquet calculations, not the release-corrected prey-threshold bound here. Dai–Zhao 2012 treats an Ivlev response and derives boundary-cycle information for a different model. Zhu–Wang–Ouyang 2021 gives a general prey-threshold framework for existence and stability, but not this explicit model-specific quantitative floor.

## Limitations
The result is a necessary condition, not an existence or stability theorem. The release-corrected inequality is always valid under the stated positive-cycle assumptions, but the convenient unique-root formulation requires \(\rho\ge\lambda\tau/(h+\tau)\). When that monotonicity condition fails, the implicit inequality remains valid but is not asserted to define a unique threshold. No sharpness claim is made. Broad impulsive predator–prey literature remains a residual originality risk.

## References
1. Z. Shi, J. Wang, Q. Li, and H. Cheng, “Control optimization and homoclinic bifurcation of a prey–predator model with ratio-dependent,” *Advances in Difference Equations* 2019, Article 2 (2019), DOI 10.1186/s13662-018-1933-z.
2. C. Dai and M. Zhao, “Dynamic Complexity of an Ivlev-Type Prey-Predator System with Impulsive State Feedback Control,” *Journal of Applied Mathematics* 2012, Article 534276 (2012), DOI 10.1155/2012/534276.
3. C. Wei, J. Liu, and L. Chen, “Homoclinic bifurcation of a ratio-dependent predator–prey system with impulsive harvesting,” *Nonlinear Dynamics* 89, 2001–2012 (2017), DOI 10.1007/s11071-017-3567-1.
4. G. Jiang and Q. Lu, “The dynamics of a Prey-Predator model with impulsive state feedback control,” *Discrete and Continuous Dynamical Systems - B* 6, 1301–1320 (2006), DOI 10.3934/dcdsb.2006.6.1301.
5. G. Zhu, Z. Wang, and M. Ouyang, “The state-dependent impulsive control for a general predator–prey model,” *Journal of Biological Dynamics* (2021), DOI 10.1080/17513758.2021.1937721.
