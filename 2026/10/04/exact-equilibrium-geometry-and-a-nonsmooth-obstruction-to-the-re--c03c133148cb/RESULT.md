# Exact equilibrium geometry and a nonsmooth obstruction to the reported origin Hopf transition
## Finding
Consider the jerk system
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=-z-\frac{3}{10}x^2z+\frac15x^2-c|x|-\frac1{10}y+xy^2-x^3,
\]
with \(c>0\). Its equilibrium and linear-stability geometry can be determined exactly.

The origin is Lyapunov unstable for every \(c>0\). Besides the origin there is always one negative equilibrium
\[
E_-(c)=(x_-(c),0,0),\qquad
x_-(c)=\frac{1-\sqrt{1+100c}}{10}.
\]
There are two further positive equilibria exactly when \(0<c<1/100\):
\[
x_{+,\pm}(c)=\frac{1\pm\sqrt{1-100c}}{10}.
\]
They coalesce at \(x=1/10\) when \(c=1/100\), and no positive nonzero equilibrium exists for \(c>1/100\).

For a nonzero equilibrium with first coordinate \(x\), the characteristic polynomial is
\[
p_x(\lambda)=\lambda^3+\left(1+\frac3{10}x^2\right)\lambda^2+\frac1{10}\lambda+x\left(2x-\frac15\right).
\]
The smaller positive branch is unstable, while the larger positive branch is asymptotically stable for its whole existence interval. The negative branch has one and only one Hopf-type spectral crossing. It occurs at
\[
x_H=\frac{10-3\sqrt{230}}{197}
\]
and therefore at
\[
c_H=x_H^2-\frac15x_H
=\frac{1776}{38809}+\frac{291\sqrt{230}}{194045}
\approx 0.0685059316572857.
\]
At \(c=c_H\), if \(A_H=1+3x_H^2/10\), then
\[
p_{x_H}(\lambda)=(\lambda+A_H)\left(\lambda^2+\frac1{10}\right),
\]
so the spectrum is \(\{-A_H,\,\pm i/\sqrt{10}\}\).

The source's reported origin crossing at \(c=1/10\) comes from differentiating the right smooth extension. The original vector field contains \(|x|\) and is not differentiable at the origin when \(c>0\). Its left smooth extension is already unstable for every positive \(c\), so the actual origin cannot undergo a classical smooth Hopf bifurcation there.

## Assumptions and scope
The parameter slice is exactly \(a=3/10\), \(b=1/5\), \(d=1/10\), with \(c>0\), in the source's system
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=-z-a x^2z+b x^2-c|x|-dy+xy^2-x^3.
\]
All stability statements here are local linear statements for smooth nonzero equilibria, except the separate Lyapunov-instability proof for the nonsmooth origin. “Hopf-type spectral crossing” means a simple imaginary conjugate pair with a third negative eigenvalue at the stated parameter. No first Lyapunov coefficient is claimed, and no periodic orbit is inferred from linearization alone.

## Proof
At equilibrium, \(y=z=0\). If \(x>0\), the remaining equation is
\[
x\left(x^2-\frac15x+c\right)=0,
\]
so positive nonzero roots exist exactly for \(1/25-4c\ge0\), namely \(c\le1/100\), with the two roots above for strict inequality. If \(x<0\), the equation is
\[
x\left(x^2-\frac15x-c\right)=0,
\]
whose quadratic has exactly one negative root \(x_-(c)\) for every \(c>0\).

The nonsmooth origin has two smooth half-space extensions. The right extension has characteristic polynomial
\[
p_+(\lambda)=\lambda^3+\lambda^2+\frac1{10}\lambda+c,
\]
which is the polynomial used by the source when it imposes the smooth Hopf condition \(c=1/10\). The left extension instead has
\[
p_-(\lambda)=\lambda^3+\lambda^2+\frac1{10}\lambda-c.
\]
For every \(c>0\), \(p_-(0)=-c<0\) and \(p_-(\lambda)\to+\infty\) as \(\lambda\to+\infty\), so it has a positive real root \(r\). Its corresponding eigenvector is proportional to \((1,r,r^2)\). The local unstable manifold has a branch tangent to \(-(1,r,r^2)\), hence lying in \(x<0\) sufficiently near the origin. On that branch the left extension and the original absolute-value vector field coincide. A trajectory approaching the origin backward in time therefore leaves every sufficiently small neighborhood forward in time, proving Lyapunov instability of the actual origin.

At a nonzero equilibrium, differentiating within its fixed-sign half-space gives the Jacobian third-row first entry
\[
2\left(\frac15\right)x-c\,\mathrm{sgn}(x)-3x^2.
\]
Using the equilibrium equation to eliminate \(c\,\mathrm{sgn}(x)\) reduces this to \(x(1/5-2x)\), yielding the displayed polynomial \(p_x\).

Set
\[
A(x)=1+\frac3{10}x^2,\qquad
C(x)=x\left(2x-\frac15\right).
\]
When \(C(x)>0\), the cubic Routh–Hurwitz criterion is exactly
\[
H(x):=\frac{A(x)}{10}-C(x)
=\frac1{10}+\frac15x-\frac{197}{100}x^2>0.
\]
For the smaller positive root, \(0<x<1/10\), one has \(C(x)<0\), so \(p_x(0)<0\) and a positive real eigenvalue exists. For the larger positive root, \(1/10<x<1/5\), one has \(C(x)>0\). Since \(H\) is concave and
\[
H\left(\frac1{10}\right)=\frac{1003}{10000}>0,
\qquad
H\left(\frac15\right)=\frac{153}{2500}>0,
\]
this whole branch is asymptotically stable.

On the negative branch, \(C(x)>0\), \(H'(x)=1/5-(197/50)x>0\) for \(x<0\), and \(x_-(c)\) decreases strictly as \(c\) increases. Hence \(H(x_-(c))\) decreases strictly from \(1/10\) to \(-\infty\), giving a unique stability boundary. Solving \(H(x)=0\) on \(x<0\) gives
\[
197x^2-20x-10=0,
\qquad
x=x_H=\frac{10-3\sqrt{230}}{197}.
\]
The branch relation \(c=x^2-x/5\) gives the stated exact \(c_H\). At \(H=0\), one has \(C=A/10\), hence
\[
p_x(\lambda)=\lambda^3+A\lambda^2+\frac1{10}\lambda+\frac{A}{10}
=(\lambda+A)\left(\lambda^2+\frac1{10}\right).
\]
Thus the negative equilibrium is asymptotically stable for \(0<c<c_H\), has the displayed simple imaginary pair at \(c=c_H\), and has a two-dimensional unstable subspace for \(c>c_H\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic in the quadratic field \(\mathbb{Q}(\sqrt{230})\). It checks the defining quadratic for \(x_H\), the exact expression for \(c_H\), the Routh boundary \(A/10-C=0\), the two endpoint inequalities on the positive stable branch, and a high-precision decimal enclosure for \(c_H\). Running the file from this package prints `VERIFY_OK`.

The instability proof at the origin is analytic rather than numerical: it depends only on the left-extension polynomial having a positive real root and on the local unstable manifold lying in the half-space where the extension equals the original vector field.

## Relationship to prior work
The introducing article gives the same absolute-value jerk equation, derives equilibrium formulas, and reports Hopf bifurcations at the origin and at nonzero equilibria. Its origin calculation substitutes a single sign into a derivative at \(x=0\), although \(|x|\) is not differentiable there. Its reported positive nonzero Hopf parameter near \(c\approx0.033\) also lies beyond the exact existence range \(0<c\le1/100\) of positive nonzero equilibria on this parameter slice.

A later general study of double-zero bifurcations in smooth jerk systems supplies useful background for smooth jerk bifurcation theory but does not analyze this absolute-value model or imply the half-space argument and exact threshold above. Searches by the exact title, DOI, vector field, equilibrium equations, the threshold expression, and semantically related bifurcation descriptions did not locate a published correction or a statement equivalent to this one. The closest published-result records concern different jerk or third-order feedback systems and do not imply this model-specific equilibrium classification.

## Limitations
The result does not prove chaos, multistability, or the existence, uniqueness, direction, or stability of a periodic orbit. In particular, the exact parameter \(c_H\) is a simple smooth spectral crossing on the negative equilibrium branch; a nondegenerate Hopf bifurcation would additionally require a nonlinear nondegeneracy calculation. The argument treats the stated one-parameter slice rather than all positive \(a,b,c,d\). Literature searches reduce but cannot eliminate the risk of an unindexed or inaccessible prior correction.

## References
1. S. Vaidyanathan, I. M. Moroz, A. A. Abd El-Latif, B. Abd-El-Atty, and A. Sambas, “A new multistable jerk system with Hopf bifurcations, its electronic circuit simulation and an application to image encryption,” *International Journal of Computer Applications in Technology* 67(1), 29–46. DOI: 10.1504/IJCAT.2021.120733. Accepted-manuscript repository record: ORA uuid:a1b4b398-5beb-4718-ab79-639b21d872b5.
2. C. Lăzureanu, “On the Double-Zero Bifurcation of Jerk Systems,” *Mathematics* 11 (2023), 4468. DOI: 10.3390/math11214468.
