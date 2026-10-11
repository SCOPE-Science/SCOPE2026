# Sharp logarithmic critical relaxation at the bullying-index threshold

## Finding

Consider the planar model
\[
\dot x=A-\beta x-bxy,\qquad
\dot y=y(\alpha x-c),
\]
with \(A,\beta,b,c,\alpha>0\). At the exact threshold
\[
\alpha A=c\beta,
\]
write
\[
x_*=\frac{c}{\alpha}=\frac{A}{\beta}.
\]
Every interior solution with \(x(0)>0\) and \(y(0)>0\) obeys
\[
\frac1{y(t)}=\frac{bc}{\beta}\,t+
\frac{b(c-\beta)}{\beta^2}\log t+o(\log t)
\qquad (t\to\infty),
\]
and
\[
t\bigl(x(t)-x_*\bigr)\longrightarrow-\frac1\alpha.
\]
Consequently,
\[
t\,y(t)\longrightarrow\frac{\beta}{bc}.
\]
Thus the nonhyperbolic threshold has a universal \(t^{-1}\) relaxation law, while the first logarithmic correction detects the mismatch between the two linear loss rates \(c\) and \(\beta\).

## Assumptions and scope

All five parameters are strictly positive, the threshold relation \(\alpha A=c\beta\) is exact, and the initial condition is interior: \(x(0)>0\), \(y(0)>0\). The conclusion is asymptotic as \(t\to\infty\). The invariant boundary \(y=0\) is excluded from the claimed asymptotics because there the approach to \(x_*\) is exponential rather than algebraic.

The source defines the threshold quantity \(R_0=\alpha A/(c\beta)\), so the parameter surface here is precisely \(R_0=1\).

## Proof

Set
\[
q=\frac{x}{x_*}-1,\qquad k=\frac b\beta.
\]
At \(\alpha A=c\beta\), the equations become
\[
\dot q=-\beta q-b(1+q)y,\qquad
\dot y=cqy. \tag{1}
\]

First, every interior solution converges to \((q,y)=(0,0)\). Indeed,
\[
V=x-x_*-x_*\log\frac{x}{x_*}+\frac b\alpha y
\]
satisfies the exact identity
\[
\dot V=-\beta\,\frac{(x-x_*)^2}{x}\le0. \tag{2}
\]
Its interior sublevel sets are compact in \(x>0,\ y\ge0\). On the set where \(\dot V=0\), one has \(x=x_*\); then \(\dot x=-bx_*y\), so the largest invariant subset is the single equilibrium \((x_*,0)\). LaSalle's invariance principle therefore gives \(q(t)\to0\) and \(y(t)\to0\).

For the leading rate, define
\[
r=q+\frac b\beta y.
\]
A direct differentiation using (1) gives
\[
\dot r=-\beta r+\frac{b(c-\beta)}\beta qy. \tag{3}
\]
Since \(\dot y/y=cq\to0\), for every sufficiently small \(\varepsilon>0\) and all large \(t\ge s\),
\[
\frac{y(s)}{y(t)}\le e^{\varepsilon(t-s)}.
\]
Variation of constants in (3), together with \(q(t)\to0\), then yields
\[
\frac{r(t)}{y(t)}\longrightarrow0.
\]
Hence
\[
\frac qy\longrightarrow-\frac b\beta. \tag{4}
\]
With \(w=1/y\), equation (1) gives
\[
\dot w=-c\,\frac qy\longrightarrow\frac{bc}\beta=:\lambda.
\]
Therefore \(w(t)/t\to\lambda\), and thus
\[
t\,y(t)\longrightarrow\frac1\lambda=\frac{\beta}{bc},
\qquad
tq(t)\longrightarrow-\frac1c.
\]
Because \(x-x_*=x_*q=(c/\alpha)q\), this proves
\[
t(x(t)-x_*)\longrightarrow-\frac1\alpha. \tag{5}
\]

To obtain the first correction, set
\[
a_2=\frac{b^2(\beta-c)}{\beta^3},\qquad
s=q+\frac b\beta y-a_2y^2.
\]
Exact differentiation gives
\[
\begin{aligned}
\dot s={}&
\left[
-\beta+\frac{b(c-\beta)}\beta y
+\frac{2b^2c(c-\beta)}{\beta^3}y^2
\right]s\\
&-\frac{b^3(\beta-c)(\beta-3c)}{\beta^4}y^3
-\frac{2b^4c(\beta-c)^2}{\beta^6}y^4. \tag{6}
\end{aligned}
\]
The coefficient of \(s\) tends to \(-\beta\), while the forcing is \(O(y^3)\). Repeating the variation-of-constants estimate, now after division by \(y(t)^2\), gives
\[
\frac{s(t)}{y(t)^2}\longrightarrow0.
\]
Therefore
\[
\frac qy=-\frac b\beta+a_2y+o(y). \tag{7}
\]
Since \(w=1/y\), (7) yields
\[
\dot w=\lambda-\frac{ca_2}w+o\!\left(\frac1w\right). \tag{8}
\]
The already proved relation \(w(t)\sim\lambda t\) converts (8) into
\[
w(t)=\lambda t-\frac{ca_2}\lambda\log t+o(\log t).
\]
Finally,
\[
-\frac{ca_2}\lambda=\frac{b(c-\beta)}{\beta^2},
\]
which is the asserted logarithmic correction.

## Verification

The standalone file `verify.py` symbolically differentiates the Lyapunov function and both defect variables, checks identities (2), (3), and (6), and checks the final logarithmic coefficient exactly. A replay of that packaged file returns `VERIFY_OK`.

As an illustrative numerical stress test only, at \(\beta=2\), \(c=3\), \(b=5\), \(\alpha=7\), \(A=6/7\), the computed limits approach \(t\,y(t)=2/15\) and \(t(x(t)-3/7)=-1/7\); after subtraction of the leading linear term in \(1/y\), the observed logarithmic slope approaches \(5/4\). This numerical check is not used as proof.

## Relationship to prior work

Ashi's source paper introduces exactly this two-dimensional bullying model, defines \(R_0=\alpha A/(c\beta)\), proves global stability for \(R_0<1\), and identifies the exchange at \(R_0=1\) as transcritical. Its displayed Lyapunov derivative in equation (3.2) remains strictly negative away from the bullying-free equilibrium even at equality \(R_0=1\), so qualitative critical attraction is already implicit in that calculation. The present claim does not re-claim that fact. It gives the sharper source-specific critical law: the exact \(t^{-1}\) constants and the first logarithmic correction.

Crokidakis studies a later four-compartment school-bullying model with different state variables and equations, so its threshold analysis does not imply the asymptotic formula above. Sari's chemostat work supplies useful broader consumer-resource context for global threshold stability, but the inspected result does not give these source-specific critical constants or logarithmic correction.

## Limitations

The result is confined to the exact critical surface and strictly positive initial \(y\). It gives asymptotic equivalents and the first logarithmic correction, not a finite-time error bound. The leading algebraic slowing is compatible with generic transcritical normal-form intuition; the originality claimed here is the global source-specific derivation of the constants and the explicit subleading coefficient \(b(c-\beta)/\beta^2\). Older consumer-resource literature may contain related critical-rate calculations under different notation, so that alias risk remains.

## References

H. A. Ashi, *Stability analysis of a simple mathematical model for school bullying*, AIMS Mathematics 7(4), DOI 10.3934/math.2022274. First public publisher date used here: 2021-12-28.

N. Crokidakis, *A mathematical model for the bullying dynamics in schools*, arXiv:2501.04752.

T. Sari, *A Lyapunov function for the chemostat with variable yields*, Comptes Rendus Mathématique, DOI 10.1016/j.crma.2010.06.008.
