# Three escape exponents and a logarithmic memory transition in a reversible quintic Liénard flow

## Finding

Consider the reversible polynomial system
\[
\dot x=y,\qquad \dot y=x^5+b x^3y,
\]
where \(b\in\mathbb R\). For **every** initial condition \(x(0)=x_0>0\), \(y(0)=y_0>0\), its forward maximal time \(T\) is finite and both \(x(t),y(t)\) tend to \(+\infty\) as \(t\uparrow T\). The precise original-time escape law undergoes a three-way transition with \(b\):
\[
\boxed{\begin{array}{ll}
 b>0:&x(t)\sim \left(\dfrac{4}{3b(T-t)}\right)^{1/3},\\[3pt]
 b=0:&x(t)\sim \left(\dfrac{\sqrt3}{2(T-t)}\right)^{1/2},\\[3pt]
 b=-c<0:&x(t)\sim \dfrac{c}{T-t}\quad(c>0).
\end{array}}
\]
The orbit graph \(y=Y(x)\), for \(x\ge x_0\), obeys sharper laws:
\[
\boxed{\begin{array}{ll}
 b>0:&Y(x)=\dfrac b4x^4+\dfrac2b x^2-\dfrac{32}{b^3}\log x+C(x_0,y_0;b)+o(1),\\[4pt]
 b=0:&Y(x)^2-\dfrac{x^6}{3}=y_0^2-\dfrac{x_0^6}{3},\\[4pt]
 b=-c<0:&Y(x)=\dfrac{x^2}{c}-\dfrac{2}{c^3}+o(1).
\end{array}}
\]
Here the positive-damping finite-part constant \(C\) is well-defined and retains strictly ordered initial-condition information. Specifically, fix \(x_0>0\) and two distinct initial speeds \(0<y_{0,1}<y_{0,2}\), and denote their velocity graphs by \(Y_1,Y_2\). Then the gap \(\Delta(x)=Y_2(x)-Y_1(x)>0\) has the exact equation
\[
\Delta'(x)=-\frac{x^5}{Y_1(x)Y_2(x)}\Delta(x).
\]
For \(b>0\), it has a strictly positive limit \(\Delta_\infty>0\) (so \(C(x_0,y_{0,2};b)>C(x_0,y_{0,1};b)\)); for \(b=0\),
\[
\Delta(x)\sim\frac{\sqrt3}{2}\left(y_{0,2}^2-y_{0,1}^2\right)x^{-3};
\]
and for \(b=-c<0\),
\[
\boxed{\log\Delta(x)=-\frac{c^2x^2}{2}+o(x^2).}
\]
Thus positive damping preserves a finite amount of initial-velocity memory at infinity, whereas zero damping erases it algebraically and negative damping erases it at a Gaussian-in-position rate.

## Assumptions and scope

All statements concern the **original physical clock**, with no time rescaling. The complete parameter domain is \(b\in\mathbb R\), and the initial data are in the open positive quadrant. The graph asymptotics and \(o(\cdot)\) remainders are for each fixed initial condition. The memory comparison holds for two initial velocities at the same positive initial position. The labels positive/negative damping refer to the sign of the coefficient multiplying \(x^3y\) in the displayed equation; no physical dissipation sign convention is assumed.

The polynomial vector field is a specialization of the reversible quintic Liénard family with coefficients \(a_0=a_1=b_0=0\), \(a_2=1\), and \(b_1=b\). Its primary dynamical classification is MSC2020 34C23.

## Proof

**1. Global positive orbit graphs.** Since \(\dot x=y>0\) in the positive quadrant, parameterize a positive orbit by position: \(Y(x_0)=y_0\) and
\[
\frac{dY}{dx}=b x^3+\frac{x^5}{Y},\qquad x\ge x_0.
\]
The positive solution exists for all finite \(x\ge x_0\). Indeed, it cannot hit zero at a positive finite \(x\), because \((Y^2)'=2b x^3Y+2x^5\), whose right side is strictly positive whenever \(Y\) is sufficiently small on a bounded positive \(x\)-interval. It cannot diverge at finite \(x\), since \(Y'\le |b|x^3+x^5\) once \(Y\ge1\). The graph is therefore global and strictly positive. Physical time along it is
\[
t(x)=\int_{x_0}^x\frac{ds}{Y(s)}.
\]
Once the polynomial lower growth rates established below are known, \(T=\int_{x_0}^{\infty}ds/Y(s)<\infty\), yielding the asserted finite-time escape and \(x,y\to+\infty\).

**2. Positive coefficient and logarithmic term.** Fix \(b>0\), set \(A=b/4\) and \(Q=2/b=1/(2A)\). The orbital equation gives \(Y'\ge b x^3\), hence \(Y\ge(A/2)x^4\) for large \(x\). Consequently \(Y'=b x^3+O(x)\), so \(Y=Ax^4+O(x^2)\). Substituting this back into the orbital equation yields
\[
Y'=b x^3+\frac{x}{A}+O(x^{-1}),\quad
Y=Ax^4+Qx^2+O(\log x).
\]
A second substitution gives the sharper, **integrably small remainder**
\[
Y'=b x^3+\frac{x}{A}-\frac{Q}{A^2x}+O\!\left(\frac{\log x}{x^3}\right).
\]
Integration now proves the existence of a finite orbit-dependent constant and
\[
Y=Ax^4+Qx^2-\frac{Q}{A^2}\log x+C+o(1).
\]
Since \(Q/A^2=32/b^3\), this is the first displayed expansion. In particular \(Y\sim (b/4)x^4\).

**3. Hamiltonian coefficient.** At \(b=0\), multiply the orbital equation by \(2Y\) and integrate:
\[
\frac{d}{dx}\left(Y^2-\frac{x^6}{3}\right)=0.
\]
Because the positive square root is selected, \(Y(x)\sim x^3/\sqrt3\), establishing the middle graph law.

**4. Negative coefficient and the attracting orbital nullcline.** Put \(b=-c<0\) and \(D(x)=Y(x)-x^2/c\). Direct differentiation gives an **exact equation**
\[
D'=x\left(-\frac{c^2D}{1+cD/x^2}-\frac2c\right),\qquad
1+cD/x^2=\frac{cY}{x^2}>0.
\]
For fixed \(x\), the factor in parentheses is strictly decreasing in \(D\). Its unique zero is
\[
D_*(x)=-\frac{2}{c^3+2c/x^2}\longrightarrow d_*=-\frac2{c^3}.
\]
Choose any \(\varepsilon>0\). For all sufficiently large \(x\), both constant barriers \(d_*-\varepsilon\) and \(d_*+\varepsilon\) lie in the admissible positive-\(Y\) domain, and there is \(\delta>0\) for which \(D'\ge\delta x\) below the lower barrier and \(D'\le-\delta x\) above the upper barrier. These one-sided inequalities force entry into the strip and prohibit departure, because \(\int^\infty x\,dx=\infty\). Since \(\varepsilon\) is arbitrary, \(D(x)\to-2/c^3\), proving the third graph expansion and \(Y\sim x^2/c\).

**5. Finite physical blow-up and the three exponents.** The preceding results imply \(Y(x)\sim kx^p\) with \((p,k)=(4,b/4),(3,1/\sqrt3),(2,1/c)\) in the three regimes. Each \(p>1\) makes the original-time integral converge, and
\[
T-t(x)=\int_x^\infty\frac{ds}{Y(s)}\sim\frac{x^{1-p}}{k(p-1)}.
\]
Inverting gives, respectively, \(x\sim[4/(3b(T-t))]^{1/3}\), \(x\sim[\sqrt3/(2(T-t))]^{1/2}\), and \(x\sim c/(T-t)\). Moreover, in each case \(Y(x)\to+\infty\), establishing both coordinate limits.

**6. Initial-speed memory.** For fixed \(x_0\), distinct positive solutions never intersect by uniqueness of the orbital initial-value problem, so \(\Delta=Y_2-Y_1>0\). Subtracting their orbital equations gives
\[
\frac{d}{dx}\log\Delta(x)=-\frac{x^5}{Y_1(x)Y_2(x)}.
\]
When \(b>0\), both denominators grow as \((b/4)x^4\), making the integrand \(O(x^{-3})\). The accumulated integral converges, so \(\Delta\to\Delta_\infty>0\). Subtracting the already-proved expansions identifies this positive limit with the difference of the finite parts \(C\). When \(b=0\), subtract the exact energy formulas and rationalize the square roots to obtain \(\Delta=(y_{0,2}^2-y_{0,1}^2)/(Y_1+Y_2)\sim(\sqrt3/2)(y_{0,2}^2-y_{0,1}^2)x^{-3}\). When \(b=-c\), the integrand is \(c^2x(1+o(1))\); integration yields \(\log\Delta=-c^2x^2/2+o(x^2)\), completing the proof.

## Verification

The standalone `verification/check_coefficients.py` uses SymPy to check the logarithmic residual, the exact coefficient identities, the negative-coefficient algebraic slow-graph residual, and the Hamiltonian identity; invoking `python verification/check_coefficients.py` prints `CHECK_OK`. The optional `verification/numerical_probe.py` uses SciPy to integrate the graph equation for two initial velocities in each regime and prints `NUMERICAL_PROBE_OK`. These are reproducibility diagnostics. The all-parameter theorem and global escape statements are proved analytically above, not inferred from finite sampling.

## Relationship to prior work

Cao, Sadri, Tang, and Wang (2026, arXiv:2610.26699) classify global phase portraits, periodic annuli, and separatrices in the encompassing five-parameter reversible quintic Liénard family. In particular their Lemma 4.7 uses Poincaré compactification to describe the local dynamics at infinity, and Section 3 analyzes different critical branches. These geometric results motivate but do not explicitly supply the present positive-quadrant **physical-time three-exponent law, third-order logarithmic correction, or initial-speed-memory classification** in their accessible full HTML text. No independent assertion of the earlier paper's phase-portrait classifications is made here.

Dumortier and Herssens (1999) develop polynomial Liénard dynamics near infinity; their broader qualitative theory is an important priority risk for the leading scaling classes, but a complete lawful text was not obtained for a line-by-line check. A related published exact blow-up theorem for a **different sign** of the quintic restoring force treats \(\dot x=-y,\;\dot y=x^{2n-1}+b(x)y\), so its oriented escape system has \(\dot v=-z^{2n-1}+\tilde b(z)v\), in contrast to the positive restoring term here. That theorem proves an open-wedge, leading/two-term escape law, whereas the present statement covers all positive initial conditions, all signs of the cubic damping, a third-order logarithmic coefficient, and differences of two orbit graphs. General numerical blow-up landscapes and other finite-part blow-up formulas likewise concern distinct vector fields. Results from those works are not claimed as new.

## Limitations

The global claim concerns only positive-quadrant initial data and the exact one-parameter quintic specialization, not every orbit or the whole five-parameter family. The logarithmic finite part is orbit-dependent but is not generally given in elementary closed form. No uniform error bounds over initial data are established. The theorem is not a classification of all Poincaré-disc sectors or periodic orbits. Published and database searches do not establish absolute historical priority; formulas implicit in older infinity analyses or independently unindexed literature remain a risk. Independent mathematical audit has not been performed.

## References

1. C. Cao, N. Sadri, Y. Tang, and Z. Wang, *Global Dynamics and Periodic-Annulus Bifurcations in a Reversible Quintic Liénard System*, arXiv:2610.26699 (first posted 19 October 2026), https://arxiv.org/abs/2610.26699.
2. F. Dumortier and C. Herssens, *Polynomial Liénard equations near infinity*, Journal of Differential Equations 153 (1999), 1–29, DOI: 10.1006/jdeq.1998.3543.
3. K. Matsue, *Geometric treatments and a common mechanism in finite-time singularities for autonomous ODEs*, Journal of Differential Equations 267 (2019), 7313–7368, arXiv:1806.08487.
4. S. Graf, I. G. Kevrekidis, and A. Townsend, *Blow-up Parameter Landscapes for Polynomial Dynamical Systems*, arXiv:2607.14269 (2026).
