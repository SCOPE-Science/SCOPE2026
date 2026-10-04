# Sharp Neumann-truncation asymptotics for a biased delta interface
## Finding
Let \(\alpha>0\) and consider the one-dimensional transverse operator
\[
h_{N,d}=-\frac{d^2}{dx^2}-\alpha\delta_0+V_0\mathbf 1_{(0,d)}
\]
on \((-d,d)\) with Neumann boundary conditions. Let \(\mu_d<0\) be its ground-state eigenvalue.

If \(0<V_0<\alpha^2\), define
\[
a=\frac{\alpha^2-V_0}{2\alpha},\qquad b=\frac{\alpha^2+V_0}{2\alpha},\qquad \mu=-a^2.
\]
Then
\[
\lim_{d\to\infty}e^{2ad}(\mu-\mu_d)=\frac{4a^2b}{\alpha},
\]
or equivalently
\[
\mu_d=\mu-\frac{4a^2b}{\alpha}e^{-2ad}(1+o(1)).
\]
At the critical bias \(V_0=\alpha^2\), where the full-line transverse problem has threshold energy \(0\) and a bounded non-square-integrable zero-energy solution,
\[
\lim_{d\to\infty}\left(d+\frac1{2\alpha}\right)e^{2\alpha d}(-\mu_d)=2\alpha,
\]
that is,
\[
-\mu_d=\frac{2\alpha e^{-2\alpha d}}{d+1/(2\alpha)}(1+o(1)).
\]
The critical law therefore has an additional inverse-length prefactor that is absent for a genuine subcritical bound state.

## Assumptions and scope
The operator is the finite-interval transverse model used in Lemma 3.1 of Exner's biased-surface analysis. The potential step is on the positive half-interval and the endpoint conditions are Neumann. The subcritical statement assumes strictly positive bias \(0<V_0<\alpha^2\); the unbiased symmetric endpoint \(V_0=0\) has two equal exponential tails and is intentionally not included in the displayed subcritical coefficient. The critical statement is exactly \(V_0=\alpha^2\). No assertion is made for \(V_0>\alpha^2\).

## Proof
Put \(k_d=\sqrt{-\mu_d}\) and \(q_d=\sqrt{V_0+k_d^2}\). Continuity at the delta interaction and the derivative jump condition give the exact eigenvalue equation
\[
k_d\tanh(k_dd)+q_d\tanh(q_dd)=\alpha.
\]
The left side is strictly increasing in \(k_d\), so the negative ground-state root is unique.

In the subcritical case, the infinite-volume equation is \(a+b=\alpha\), with \(b=\sqrt{V_0+a^2}\). Monotonicity in \(d\) and the limiting scalar equation imply \(k_d\to a\), and the source's inequality \(\mu_d<\mu\) gives \(k_d>a\). Rearranging the exact equation gives
\[
k_d+q_d-\alpha=k_d\bigl(1-\tanh(k_dd)\bigr)+q_d\bigl(1-\tanh(q_dd)\bigr).
\]
Near \(k_d=a\), the left side is comparable to \(k_d-a\), while the right side is \(O(e^{-2ad})\); hence \(x_d:=k_d-a=O(e^{-2ad})\). Now
\[
q_d=b+\frac{a}{b}x_d+O(x_d^2)
\]
and \(\tanh z=1-2e^{-2z}+O(e^{-4z})\), so the exact eigenvalue equation becomes
\[
\left(1+\frac ab\right)x_d
=2a e^{-2ad}(1+o(1))+2b e^{-2bd}(1+o(1))+O(x_d^2).
\]
Because \(V_0>0\) gives \(b>a\), the second exponential is lower order, and \(1+a/b=\alpha/b\). Hence
\[
x_d=\frac{2ab}{\alpha}e^{-2ad}(1+o(1)).
\]
Using \(\mu_d=-k_d^2\) and \(\mu=-a^2\) gives
\[
\mu-\mu_d=k_d^2-a^2=\frac{4a^2b}{\alpha}e^{-2ad}(1+o(1)).
\]

At criticality, \(V_0=\alpha^2\). Set \(y_d=k_d^2=-\mu_d\) and \(q_d=\sqrt{\alpha^2+y_d}\). Since \(q_d\ge\alpha\), the root equation gives
\[
k_d\tanh(k_dd)\le \alpha\bigl(1-\tanh(\alpha d)\bigr)=O(e^{-2\alpha d}).
\]
If \(k_dd\ge1\), the left side is at least \(d^{-1}\tanh(1)\), impossible for large \(d\). Hence eventually \(k_dd<1\); using \(\tanh z\ge z/2\) for \(0\le z\le1\) then yields \(y_dd=O(e^{-2\alpha d})\), and consequently \(k_dd\to0\). Therefore
\[
k_d\tanh(k_dd)=y_dd+O(y_d^2d^3).
\]
Also
\[
q_d=\alpha+\frac{y_d}{2\alpha}+O(y_d^2)
\]
and
\[
q_d\tanh(q_dd)=\alpha+\frac{y_d}{2\alpha}-2\alpha e^{-2\alpha d}+o(y_d)+o(e^{-2\alpha d}).
\]
Substitution yields
\[
y_d\left(d+\frac1{2\alpha}\right)=2\alpha e^{-2\alpha d}(1+o(1)),
\]
which is the critical formula.

## Verification
The accompanying script solves the exact scalar spectral equation by bisection for several subcritical and critical parameter choices and compares the rescaled errors with the proved constants. These finite computations are only corroborative; the proof above establishes the asymptotic limits.

## Relationship to prior work
Exner's Lemma 3.1 proves only the rough lower estimate \(\mu_d\ge\mu-c_0d^{-1}\), obtained from a coarse lower bound on \(\tanh\). The paper immediately remarks that the Neumann-boundary error is in fact exponentially small, referring to the related strong-coupling interval estimate of Exner--Yoshitomi, but it does not state the leading coefficient for the biased step model or analyze the critical resonance separately. Exner--Yoshitomi treat a different symmetric transverse operator and give a coarse exponential enclosure rather than the present asymmetric coefficient. The earlier asymmetric-wire paper supplies the same full-line transverse threshold structure but not this finite-Neumann asymptotic. General finite-volume bound-state formulas in periodic boxes concern a different boundary geometry and do not imply the critical Neumann resonance law here.

## Limitations
The result concerns only the one-dimensional transverse truncation used in the bracketing argument; it does not sharpen the geometric error terms of the full three-dimensional surface operator. The \(o(1)\) remainders are not replaced here by explicit uniform constants. The subcritical coefficient is not asserted at \(V_0=0\), where the two exponential tails have equal rate. A targeted literature search did not locate the displayed coefficients, but an unindexed one-dimensional point-interaction calculation could contain an equivalent expansion.

## References
P. Exner, *On the spectrum of leaky surfaces with a potential bias*, arXiv:1701.06288v1 (2017), later in *The Mathematics of the Uncertain*, EMS Series of Congress Reports (2018), DOI 10.4171/186-1/8.

P. Exner and K. Yoshitomi, *Asymptotics of eigenvalues of the Schrödinger operator with a strong delta-interaction on a loop*, arXiv:math-ph/0103029v1 (2001), J. Geom. Phys. 41 (2002), 344--358.

P. Exner and S. Vugalter, *On the existence of bound states in asymmetric leaky wires*, arXiv:1505.02347v1 (2015).

S. König and D. Lee, *Volume Dependence of N-Body Bound States*, arXiv:1701.00279v1 (2017), Phys. Lett. B 779 (2018), 9--15.
