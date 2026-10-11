# A singular physical-time impulse law for a high-energy Loud center

## Finding

For the reversible quadratic Loud vector field
\[
\dot x=-y(1-x),\qquad \dot y=x,
\]
restrict to the invariant half-plane \(x<1\). Every positive energy \(E>0\) specified below determines one periodic orbit. Choose its phase origin at the positive turning point of the logarithmic coordinate and denote its original-time minimal period by \(T(E)\). Define
\[
q(t)=-\log(1-x(t)),\quad p(t)=-y(t),\qquad
Q_E(s)=\frac{q(sT(E))}{E},\quad P_E(s)=\frac{p(sT(E))}{\sqrt{2E}},\quad 0\le s\le1.
\]
Then the normalized logarithmic coordinate converges **uniformly** to the hard-impact parabola
\[
Q_\infty(s)=\begin{cases}1-4s^2,&0\le s\le\frac12,\\1-4(1-s)^2,&\frac12\le s\le1.\end{cases}
\]
The normalized momentum converges in \(L^1([0,1])\), and pointwise for \(s\ne1/2\), to
\[
P_\infty(s)=\begin{cases}-2s,&0\le s<\frac12,\\2(1-s),&\frac12<s\le1.\end{cases}
\]
Its jump at \(s=1/2\) has an **exact signed-measure counterpart in the original polynomial coordinate**:
\[
\boxed{\ x(sT(E))\,ds\ \overset{*}{\rightharpoonup}\ ds-\delta_{1/2}\quad\text{as }E\to\infty.\ }
\]
Thus, for every continuous \(\varphi:[0,1]\to\mathbb R\),
\[
\lim_{E\to\infty}\int_0^1\varphi(s)x(sT(E))\,ds
=\int_0^1\varphi(s)\,ds-\varphi(1/2).
\]
Finally, the distribution of the logarithmic energy share sampled uniformly in original time has the exact limiting probability density
\[
\boxed{\ (Q_E)_\#(ds)\ \Rightarrow\
\frac{\mathbf1_{(0,1)}(u)}{2\sqrt{1-u}}\,du.\ }
\]
The familiar high-energy period normalization \(T(E)/(2\sqrt{2E})\to1\) is recovered as an input to the phase limit, **not proposed as a new period result**.

## Assumptions and scope

The sole dynamical assumptions are \(x<1\), the displayed autonomous vector field, and \(E>0\). Introduce the potential
\[
V(q)=q+e^{-q}-1,
\qquad H(q,p)=\frac12p^2+V(q).
\]
The initial condition is \((q(0),p(0))=(a_E,0)\), where \(a_E>0\) is the unique positive solution of \(V(a_E)=E\). Let \(-r_E<0\) denote the negative turning point, with \(V(-r_E)=E\). Period and all measures use the **unmodified original time \(t\)**. The measure \(x(sT(E))\,ds\) is signed and has uniformly bounded total variation, but it does **not** converge in \(L^1\) as a density. For general nonzero phase origins the delta location must be translated accordingly. No claim is made for trajectories on or beyond \(x=1\), nonzero damping, or finite-energy uniform-error constants.

## Proof

**1. Exact conjugacy and periodicity.** Since \(1-x=e^{-q}\), differentiation gives
\[
\dot q=\frac{\dot x}{1-x}=-y=p,
\qquad\dot p=-\dot y=-x=e^{-q}-1=-V'(q).
\]
The transformation is smooth and invertible on \(x<1\), with no time change. Direct differentiation yields \(\dot H=0\). The potential has \(V(0)=V'(0)=0\), \(V''(q)=e^{-q}>0\), and \(V(q)\to\infty\) at both ends. Hence each \(H=E>0\) is a simple closed Hamiltonian oval, providing exactly one periodic orbit and its two turning points. The turning-point equations are
\[
a_E+e^{-a_E}-1=E,\qquad e^{r_E}-r_E-1=E.
\]
They imply \(a_E=E+1+o(1)\) and \(r_E=O(\log E)\) as \(E\to\infty\).

**2. Passage-time bounds with uniform control.** Write the positive-side and negative-side one-way passage times as
\[
 t_+(E)=\int_0^{a_E}\frac{dq}{\sqrt{2(E-V(q))}},\qquad
 t_-(E)=\int_{-r_E}^0\frac{dq}{\sqrt{2(E-V(q))}}.
\]
On the positive branch put \(w=a_E-q\). The exact identity
\[
E-V(a_E-w)=w-e^{-a_E}(e^w-1)
\]
holds for \(0\le w\le a_E\). Since \((e^w-1)/w\) increases for \(w>0\),
\[
0\le\frac{e^{-a_E}(e^w-1)}w\le
\eta_E:=\frac{1-e^{-a_E}}{a_E}=O(E^{-1}).
\]
Consequently, if \(t(q)\) denotes elapsed time from \(a_E\) down to any \(q\in[0,a_E]\),
\[
\sqrt{2(a_E-q)}\le t(q)\le
\frac{\sqrt{2(a_E-q)}}{\sqrt{1-\eta_E}}.
\tag{1}
\]
In particular \(t_+(E)=\sqrt{2E}(1+O(E^{-1}))\).

On the negative branch put \(w=q+r_E\) and \(Z_E=e^{r_E}=E+r_E+1\). Then
\[
E-V(-r_E+w)=Z_E(1-e^{-w})-w.
\]
For sufficiently large \(E\), this expression is bounded below by \(cEw\) on \(0\le w\le1\) and by \(cE\) on \(1\le w\le r_E\), with a constant \(c>0\) independent of \(E\). Therefore
\[
t_-(E)=O\!\left(\frac{1+r_E}{\sqrt E}\right)
=O\!\left(\frac{\log E}{\sqrt E}\right).
\]
A full orbit makes each passage twice, so
\[
T(E)=2(t_+(E)+t_-(E))=2\sqrt{2E}\,(1+o(1)).\tag{2}
\]

**3. Uniform coordinate waveform.** By (1), throughout descent from \(a_E\) to \(0\), the scaled elapsed time satisfies
\[
\frac{t(q)^2}{2E}=\frac{a_E-q}{E}\,(1+O(E^{-1})),
\]
where the error is uniform over that entire segment. As \(T(E)/(2\sqrt{2E})\to1\), the phase-normalized positive descent converges uniformly to \(1-4s^2\). The negative excursion from \(0\) to \(-r_E\) and back occupies a phase interval of width \(2t_-(E)/T(E)=O((\log E)/E)\), centered at \(s=1/2\), and throughout that interval \(|q|/E\le r_E/E\to0\). Time reversal gives the reflected positive ascent and its limit \(1-4(1-s)^2\). These observations also control transitions at the two ends of the shrinking excursion and prove \(\|Q_E-Q_\infty\|_\infty\to0\).

**4. Momentum and jump.** The energy identity gives \(|P_E(s)|\le1\). Off \(s=1/2\), for sufficiently large \(E\) one has \(q(sT(E))>0\) except possibly at fixed endpoints; energy and the sign of the descending/ascending branch yield
\[
P_E(s)=\pm\sqrt{1-\frac{V(q(sT(E)))}E}
\longrightarrow P_\infty(s).
\]
The value at \(s=1/2\) is immaterial. Bounded convergence yields \(P_E\to P_\infty\) in \(L^1\).

**5. Singularity in a physical observable.** From \(\dot p=-x\) and \(s=t/T(E)\),
\[
x(sT(E))\,ds=-\frac{\sqrt{2E}}{T(E)}\,dP_E(s).
\]
For a \(C^1\) test function, integration by parts (using \(P_E(0)=P_E(1)=0\)) gives
\[
\int_0^1\varphi(s)x(sT(E))\,ds=
\frac{\sqrt{2E}}{T(E)}\int_0^1\varphi'(s)P_E(s)\,ds.
\]
By (2) and step 4, the limit is half the last integral with \(P_\infty\) substituted. Its piecewise linear derivative equals \(-2\,ds+2\delta_{1/2}\); equivalently direct integration on the two half-intervals gives \(\int_0^1\varphi(s)\,ds-\varphi(1/2)\).

To extend from \(C^1\) to all continuous test functions, note \(x=1-e^{-q}\le1\), so its positive part is at most one. Since \(\dot p=-x\) and the orbit is periodic, \(\int_0^1x(sT(E))\,ds=0\). Its negative and positive total masses therefore agree and both are at most one. Thus \(\int_0^1|x(sT(E))|\,ds\le2\) uniformly. Density of \(C^1\) in \(C([0,1])\) now proves the asserted weak-* limit. Moreover \(x(sT(E))\to1\) pointwise for every \(s\ne1/2\), but its integral is always zero, excluding \(L^1\)-convergence to the pointwise limit.

**6. Physical-time distribution.** The first convergence implies \((Q_E)_\#ds\Rightarrow(Q_\infty)_\#ds\). For \(0<u<1\), the two preimages under \(Q_\infty\) have inverse-derivative magnitudes \(1/(4\sqrt{1-u})\) each. Their sum is the stated \(1/(2\sqrt{1-u})\), which integrates to one and creates no endpoint atoms.

## Verification

The proof uses exact conservation, elementary inequalities for passage integrals, bounded convergence and an explicitly bounded total variation; it does not infer an infinite-energy theorem from numerical trials. A standalone standard-library checker (`check.py`) verifies the coordinate conjugacy and energy derivative at sample points, turning-point identities, and exact quadrature numerics at \(E=16,64,256\). Its output is `CHECK_OK`, including period ratios approximately \(1.159338,1.050719,1.015438\) and shrinking negative-phase proportions approximately \(0.110024,0.040806,0.013278\). These finite calculations are sanity checks only; all limit assertions follow from the preceding bounds.

## Relationship to prior work

Marín and Villadelprat (2022, arXiv:2203.12966v1) study critical periods at the outer boundary in the two-parameter reversible Loud family; our parameter \((D,F)=(0,0)\) is a member of their family. Their question is period criticality, not a signed physical-time phase-impulse limit. Kouznetsov, Bisson, Li and Ueda (2007) analyze the **same** undamped Toda oscillator after reversing the logarithmic coordinate: they provide the energy quadrature, high-amplitude period behavior, and accurate finite-amplitude waveform approximations. These antecedents are credited rather than rebranded as discoveries. The present mathematical claim is the **rigorously normalized full-phase waveform together with weak-* concentration of the original polynomial force and its limiting time-sampling law**. The signed delta statement is not asserted in the inspected original-results material. Chouikha (2005) studies period monotonicity for Loud quadratic centers and transformations to conservative equations; this does not determine the signed force-measure limit. Jelbart et al. (2021) develop singular-exponential techniques for different dissipative models, not the conserved Toda oval considered here.

## Limitations

This is an exact asymptotic theorem for **one natural Loud parameter**, not the full reversible quadratic-center family. The period leading term and Toda quadrature are prior knowledge. The limits are asymptotic and do not claim explicit finite-energy error constants for the measures. The delta is a signed-measure limit; neither a pointwise density limit at its concentration phase nor an ordinary \(L^1\) limit is claimed. Full priority relative to all general hard-impact or singular-oscillator literature cannot be guaranteed by a finite literature search. Numerical checks support elementary implementation only and do not certify the analysis independently.

## References

1. D. Marín and J. Villadelprat, *The criticality of reversible quadratic centers at the outer boundary of its period annulus*, arXiv:2203.12966v1 (first posted 24 March 2022), https://arxiv.org/abs/2203.12966.
2. D. Kouznetsov, J.-F. Bisson, J. Li and K. Ueda, *Self-pulsing laser as oscillator Toda: approximations through elementary functions*, Journal of Physics A 40 (2007), 2107–2124, https://doi.org/10.1088/1751-8113/40/9/016; lawful author-hosted paper https://mizugadro.mydns.jp/PAPERS/toda.pdf.
3. A. R. Chouikha, *Monotonicity of the period function for some planar differential systems. Part I: Conservative and quadratic systems*, application to Loud centers, https://www.impan.pl/shop/en/publication/transaction/download/product/84396.
4. S. Jelbart, K. U. Kristiansen, P. Szmolyan and M. Wechselberger, *Singularly Perturbed Oscillators with Exponential Nonlinearities*, Journal of Dynamics and Differential Equations (published online 19 July 2021), https://doi.org/10.1007/s10884-021-10041-1.
