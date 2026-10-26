# Sharp non-sticky tumbling-assisted capture in an asymmetric finite interval

## Finding
Consider a one-dimensional run-and-tumble particle with independent symmetric initial velocity signs and two partially absorbing, *instantly reflecting* endpoints. Write its dimensionless initial position as \(x\in(0,1)\), its dimensionless bulk reversal parameter as \(y=\alpha L/v\ge0\), and the two boundary reactivities as \(A,B\in(0,1]\), respectively. An impact is absorbed with probability \(2A/(1+A)\) at the left wall and \(2B/(1+B)\) at the right; a nonabsorbing impact causes immediate reversal, not residence at the wall. The physical reversal rate of velocity is \(\alpha/2\).

Define
\[
S=A+B,\quad P=AB,\quad Q=A(2x-x^2)+B(1-x^2),\quad R=ABx(1-x),\quad \Delta=SQ-2P.
\]
The exact dimensionless mean absorption time is
\[
\mathcal T(y)=\frac{v}{L}\mathbb E[\tau]=\frac{2+Qy+Ry^2}{2(S+Py)}.
\]
Its **unique global minimizer** on \(y\ge0\) is \(y_*=0\) when \(\Delta\ge0\), and otherwise is the finite positive number
\[
y_* =\frac{\sqrt{S^2-\Delta/[x(1-x)]}-S}{P}.
\]
In particular, a beneficial strictly positive reversal rate is possible *without boundary sticking*. More exactly, if \(B>A\), set \(H=A^2-AB+B^2\) and \(x_c=(A+\sqrt H)/(A+B)\). Then \(0<x_c<1\), and \(y_*>0\) holds **if and only if** \(x>x_c\). If \(A>B\), set \(x_c=(A-\sqrt H)/(A+B)\); then \(0<x_c<1\), and \(y_*>0\) holds **if and only if** \(x<x_c\). For \(A=B\) the optimizer is always \(y_*=0\). At either threshold the optimizer is exactly zero.

If \(\Delta<0\), finite positive tumbling improves on strictly ballistic motion exactly for
\[
0<y<-\frac{\Delta}{RS};
\]
it becomes worse again for larger \(y\). With \(B>A\) and fixed reactivities, as \(x\uparrow1\),
\[
y_*\sim\frac{\sqrt{B-A}}{B\sqrt A}(1-x)^{-1/2},\qquad
\mathcal T(y_*)\longrightarrow\frac{1}{2B}<\frac1{A+B}=\mathcal T(0).
\]
The counterpart for \(A>B\) follows by reflection \((A,B,x)\mapsto(B,A,1-x)\).

## Assumptions and scope
The particle moves at speed \(v>0\) between \(0\) and \(L>0\). Its velocity is \(\pm v\), initially equiprobable at the fixed interior site \(xL\), and flips at an independent exponential clock of rate \(\alpha/2\). Collisions at the two walls independently cause absorption with the prescribed positive probabilities; otherwise the velocity reverses instantaneously. There are no wall holding times, external fields, speed fluctuations, starting-orientation biases or spatially variable reversal rates. The parameter \(\alpha\ge0\) is the controlled rate; the two wall reactivities and initial site are fixed. This definition explicitly distinguishes the flip clock from conventions that count orientation-redraw events as tumbles. Every trajectory is absorbed almost surely in finite mean time because either endpoint absorbs with uniformly positive probability at repeated crossings.

## Proof
Write \(U_+(z)\) and \(U_-(z)\) for conditional mean absorption times given velocities \(+v\) and \(-v\), for \(0<z<L\). Their backward equations and instantaneous, independent collision conditions are
\[
vU_+'+\frac{\alpha}{2}(U_--U_+)=-1,\qquad
-vU_-'+\frac{\alpha}{2}(U_+-U_-)=-1,
\]
\[
U_-(0)=\frac{1-A}{1+A}U_+(0),\qquad U_+(L)=\frac{1-B}{1+B}U_-(L).
\]
Let \(m=(U_++U_-)/2\) and \(d=(U_+-U_-)/2\). Addition and subtraction give \(d'=-1/v\) and \(m'=\alpha d/v\). Thus \(d(z)=c-z/v\) and \(m(z)=c/A+(\alpha/v)(cz-z^2/(2v))\). The right collision condition reads \(m(L)=(L/v-c)/B\), whence
\[
\frac{cv}{L}=\frac{A+Py/2}{S+Py},\qquad y=\alpha L/v.
\]
Substitution at \(z=xL\) and elementary collection of powers yields the stated exact rational \(\mathcal T\). The equations are uniquely solvable because \(S+Py>0\); all normalizations and the \(\alpha=0\) boundary are covered.

Direct differentiation gives
\[
\mathcal T'(y)=\frac{\Delta+2RSy+RPy^2}{2(S+Py)^2},
\quad \Delta=B(B-A)+2ASx-S^2x^2.
\]
The derivative numerator increases strictly for every \(y\ge0\), since \(R,S,P>0\). If \(\Delta\ge0\) then \(\mathcal T\) is strictly increasing for \(y>0\). Otherwise that numerator has one positive zero, yielding the stated \(y_*\), with \(\mathcal T\) decreasing before it and increasing thereafter. Moreover \(\mathcal T(y)\to\infty\) as \(y\to\infty\), so this is the unique global minimizer, not just a local stationary point. (When \(\Delta=0\), the derivative vanishes only at \(y=0\).)

As a concave quadratic in \(x\), \(\Delta\) has roots \((A\pm\sqrt H)/S\), where \(H=A^2-AB+B^2\). If \(B>A\), one root is negative and the other belongs to \((0,1)\), and \(\Delta<0\) occurs exactly to its right. If \(A>B\), the smaller root is in \((0,1)\) and the larger exceeds \(1\), and \(\Delta<0\) occurs exactly to its left. If \(A=B\), the two roots are \(0\) and \(1\), so \(\Delta>0\) throughout the interior. This proves the sharp phase regions.

Subtracting the ballistic mean gives the exact identity
\[
\mathcal T(y)-\mathcal T(0)=\frac{y(\Delta+RSy)}{2S(S+Py)}.
\]
Its sign proves the asserted complete improvement interval. For fixed \(B>A\), \(\Delta\to A(A-B)<0\) as \(x\uparrow1\), whereas \(x(1-x)\sim 1-x\). The optimizer formula therefore yields the square-root divergence. In the same limit \(y_*=O((1-x)^{-1/2})\), \(Q\to A\), and \(Ry_*^2=O(1)\); divide the rational mean numerator and denominator by \(y_*\) to obtain \(\mathcal T(y_*)\to A/(2P)=1/(2B)\). The counterpart under reflection is immediate. No optimization over a wall-sticking rate is involved.

## Verification
Run `python3 check.py` with NumPy and SciPy. Its independent backwards-equation expression was compared against the polynomial closed form at 1,500 random physical configurations, with a largest absolute discrepancy of \(7.11\times10^{-15}\). A centered finite-difference derivative check passed the same 1,500 cases with maximum absolute discrepancy \(1.4\times10^{-10}\); 250 bounded scalar numerical minimizations matched the exact optimum in objective value. Four near-wall scales exhibited the predicted normalized square-root asymptotic trend. Independent event-driven Monte Carlo with 30,000 trajectories at each of three rates agreed with the formula within reported simulation error. For \((A,B,x)=(0.4,1,0.95)\), the exact values are approximately \(y_*=1.604177855\), \(\mathcal T(0)=0.714285714\), and \(\mathcal T(y_*)=0.696823448\). Finite computational checks corroborate but do not replace the complete analytical proof above.

## Relationship to prior work
The *forward* mean absorption formula for a finite run-and-tumble segment with partially reflecting ends is established by Angelani (2015), especially Eq. (36), and its generic-start extension Eq. (37). Angelani (2023) derives a more general boundary-condition mean-time formula, Eq. (47), and its discussion distinguishes non-sticky from sticky-wall cases; at the studied central launch site, non-sticky variants have monotone reversal-rate dependence. Angelani (2024) investigates optimal escapes emphasizing wall trapping and a different set of boundary configurations. These are strong, directly relevant predecessors, not merely adjacent terminology. The contribution claimed here is **only** the all-parameter optimization of that known non-sticky forward model when the initial site is allowed to be off center, namely the sharp asymmetric position threshold, unique finite optimizer, entire ballistic-improvement interval and singular endpoint scaling. The 2015 general formula algebraically contains sufficient information to derive the result, but its existence is not itself an explicit optimized phase classification. No novelty is claimed for the dispersion/telegraph equation, forward mean formula, ballistic limit or ordinary moment differentiation.

## Limitations
The findings concern exact expectations for a homogeneous one-dimensional, constant-speed Markov process. No theorem is asserted for wall sticking, non-Markovian reflection, multidimensional confinement, alternative initial-direction distributions, statistics of estimators, or noisy measurements. The result is a closed-form optimization of already published exact forward statistics; historical papers or later specialized work may have formulated this optimization equivalently, so priority outside the inspected sources is not established. Only self-review has been conducted; independent audit has not been performed.

## References
1. L. Angelani, “Run-and-tumble particles, telegrapher's equation and absorption problems with partially reflecting boundaries,” *J. Phys. A: Math. Theor.* **48**, 495003 (2015), DOI: `10.1088/1751-8113/48/49/495003`; lawful full preprint `https://arxiv.org/pdf/1601.04845`, especially p. 6, Eqs. (36)–(39).
2. L. Angelani, “One-dimensional run-and-tumble motions with generic boundary conditions,” *J. Phys. A* **56**, 455003 (2023), DOI: `10.1088/1751-8121/ad009e`; full OA text `https://iris.cnr.it/retrieve/e1d78abe-8685-4eff-936b-9bcad8ad4c0f/prod_489129-doc_203607.pdf`, especially Eq. (47), §§5–6 and Appendix A.
3. L. Angelani, “Optimal escapes in active matter,” *Eur. Phys. J. E* **47**, 9 (2024), DOI: `10.1140/epje/s10189-023-00402-7`; complete OA article `https://link.springer.com/article/10.1140/epje/s10189-023-00402-7`.
4. P. C. Bressloff, “Encounter-based model of a run-and-tumble particle,” `arXiv:2209.07293` (2022), `https://arxiv.org/pdf/2209.07293`.
