# Real upstream spectrum defeats the linear oscillation obstruction in a pseudo-parabolic Fisher--KPP wave
## Finding
Consider the pseudo-parabolic Fisher--KPP traveling-wave equation
\[
-c\varphi'+\tau c\varphi'''=D\varphi''+\varphi(1-\varphi),
\]
with \(D>0\), \(\tau>D\), and speed \(c\ge c^*(\tau,D)\), where \(c^*\) is the minimal speed in Cao--Chen--Jin--Yin. Put \(v=1-\varphi\). The linearization at the upstream equilibrium \(v=0\) is
\[
c v'-\tau c v'''=-D v''+v,
\]
so exponential modes satisfy
\[
Q(\lambda)=\tau c\lambda^3-D\lambda^2-c\lambda+1=0.
\]
For every admissible \(c\), this cubic has three distinct real roots
\[
\lambda_-<0<\lambda_1<\lambda_2<\frac1{\sqrt\tau}.
\]
Hence
\[
w_j(\xi)=e^{\lambda_j\xi},\qquad j=1,2,
\]
are positive, strictly increasing, strictly convex, satisfy \(w_j(0)=1\), tend to zero as \(\xi\to-\infty\), and solve the exact linearized differential equation. Because \(\lambda_j^2<1/\tau\), they also solve the source's equivalent Bessel-convolution linearization.

Section 6 of arXiv:2609.34368v1 instead concludes that no solution of this monotone linearized type can exist. The two exponential modes above are direct counterexamples to that step. Thus the published contradiction argument does not establish Theorem 2.4's oscillatory-tail conclusion. The calculation also shows that throughout the source's admissible wave-speed range the upstream spatial spectrum is real, not focus-type.
## Assumptions and scope
The statement concerns the printed traveling-wave equation in arXiv:2609.34368v1, with \(D>0\), \(\tau>D\), and \(c\ge c^*(\tau,D)\). It is a statement about the exact upstream linearization and the logical validity of the Section 6 contradiction step. It does not by itself prove that every nonlinear traveling profile is globally monotone, nor does it decide whether finite overshoot or undershoot can occur away from the asymptotic upstream tail.

The minimal speed is the source's value. Writing
\[
r=\frac\tau D>1,\qquad y=\frac{c^2}{D},
\]
its square is the positive root \(y_*\) of
\[
F_-(y)=4ry^2+(1-18r-27r^2)y-4=0.
\]
Thus \(c\ge c^*\) is equivalent to \(y\ge y_*\).
## Proof
The standard cubic discriminant of the downstream characteristic polynomial used to define \(c^*\),
\[
P(\lambda)=\tau c\lambda^3-D\lambda^2-c\lambda-1,
\]
is
\[
\operatorname{disc}P=D^3F_-(y).
\]
The upstream polynomial \(Q\) has discriminant
\[
\operatorname{disc}Q
=4D^3+D^2c^2+18D\tau c^2+4\tau c^4-27\tau^2c^2
=D^3F_+(y),
\]
where
\[
F_+(y)=4ry^2+(1+18r-27r^2)y+4.
\]
The two quadratics satisfy the exact identity
\[
F_+(y)=F_-(y)+36ry+8.
\]
Since \(F_-\) has negative constant term, it has exactly one positive root, namely \(y_*\), and \(F_-(y)\ge0\) for \(y\ge y_*\). Therefore
\[
\operatorname{disc}Q=D^3\bigl(F_-(y)+36ry+8\bigr)>0
\]
for every \(c\ge c^*\). Hence \(Q\) has three distinct real roots.

Their product is \(-1/(\tau c)<0\), while their sum is \(D/(\tau c)>0\). Since \(Q(-\infty)<0<Q(0)\), there is a negative root; the sign of the product and the positive sum then force exactly two positive roots. Denote them by \(0<\lambda_1<\lambda_2\).

It remains to locate them below the Bessel-transform singularity. At \(y=1/r\),
\[
F_-(1/r)=\frac5r-22-27r<0,
\]
so \(y_*>1/r\) and therefore \(c>D/\sqrt\tau\). Put \(s=1/\sqrt\tau\). Then
\[
Q(s)=1-\frac D\tau>0,
\qquad
Q'(s)=2\left(c-\frac D{\sqrt\tau}\right)>0.
\]
Moreover \(Q'\) is a quadratic with one negative and one positive zero, so \(Q\) has a unique local minimum on \((0,\infty)\). The point \(s\) lies on the increasing side of that minimum and has \(Q(s)>0\); since the two positive roots straddle the minimum, \(s>\lambda_2\). Thus
\[
0<\lambda_1<\lambda_2<\frac1{\sqrt\tau}.
\]

The source computes the Bessel transform
\[
\Phi(\lambda)=\int_{\mathbb R}B(y)e^{-\lambda y}\,dy
=\frac1{1-\tau\lambda^2},
\qquad \lambda^2<\frac1\tau.
\]
Its limiting linearized convolution equation is
\[
cw'-\frac D\tau w
=\left(1-\frac D\tau\right)B*w.
\]
For \(w=e^{\lambda\xi}\), this equation becomes
\[
c\lambda-\frac D\tau
=\frac{1-D/\tau}{1-\tau\lambda^2},
\]
which is algebraically equivalent to \(Q(\lambda)=0\). Hence each \(w_j=e^{\lambda_j\xi}\) is a valid convolution solution as well as a differential-equation solution. It has \(w_j(0)=1\), \(w_j'>0\), \(w_j''>0\), and \(w_j(\xi)\to0\) as \(\xi\to-\infty\). These are precisely the qualitative properties imposed on the limiting monotone solution in the contradiction step, so the assertion that no such solution exists is false.
## Verification
All identities are exact. The discriminants were independently expanded symbolically before packaging; the proof above gives the same expansions directly. No numerical root approximation or finite experiment is used to infer the universal statement.

Boundary checks are internal: at \(\tau=D\), the upstream polynomial factors as
\[
Q(\lambda)=(D\lambda^2-1)(c\lambda-1),
\]
which is consistent with the strict \(\tau>D\) root ordering approaching the Bessel-transform boundary. The accepted claim deliberately stops at the linearized obstruction and does not infer a complete nonlinear classification from this spectral calculation alone.
## Relationship to prior work
Cao--Chen--Jin--Yin state that \(\tau/D>1\) produces oscillatory traveling waves and, in Section 6, pass to a limiting linearized problem near \(\varphi=1\). Their proof concludes that this problem admits no positive monotone solution decaying at \(-\infty\). The explicit exponential modes above show that this particular conclusion is incompatible with the characteristic polynomial of the very same linearized equation.

Wang--Bai--Cao study the same viscous Fisher--KPP family in the small-viscosity regime using geometric singular perturbation and spectral stability. That work does not analyze the \(\tau>D\) regime of the 2026 theorem or state the admissible-speed upstream root ordering proved here.

Targeted semantic searches found no published correction or equivalent source-specific calculation. The closest retrieved records concern spatial-tail spectra in different wave equations and do not imply this result.
## Limitations
This result invalidates a proof step, not automatically every possible interpretation of finite overshoot in the nonlinear wave. A different argument could in principle establish some weaker non-monotonicity statement. The source's numerical profiles are finite-domain computations and are not used here as evidence for or against an infinite-tail assertion.

The literature search cannot exclude an unindexed or unpublished observation of the same algebraic obstruction. The mathematical conclusion itself is independent of that bibliographic residual risk.
## References
1. Y. Cao, H. Chen, C. Jin, and J. Yin, “A Critical Value for the Viscosity Coefficient: Triggering Oscillatory Traveling Waves in the Pseudo-parabolic Fisher-KPP Equation,” arXiv:2609.34368v1, 2026.
2. L. Wang, X. Bai, and Y. Cao, “Exponential stability of the traveling fronts for a viscous Fisher-KPP equation,” *Discrete and Continuous Dynamical Systems - B* 19 (2014), 801--815, DOI: 10.3934/dcdsb.2014.19.801.
