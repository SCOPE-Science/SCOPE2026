# A unique reset-cadence reversal and a logarithmic temperature frontier for Gaussian reset cycles

## Finding

Consider the **endpoint symmetrized Kullback–Leibler divergence** of a Gaussian Ornstein–Uhlenbeck relaxation cycle, with the reset variance strictly between zero and the bath-equilibrium variance. Compare two clocks having the same mean duration: fixed periodic spacing and exponential (Poisson) spacing. The following statements hold for **every** finite variance ratio in the stated range.

**Theorem.** For each \(b>0\), set
\[
q_b(t)=1+b(1-e^{-t}),\qquad
F_b(t)=\frac12\left(q_b(t)+q_b(t)^{-1}-2\right),
\qquad \Delta_b(x)=\int_0^\infty e^{-u}F_b(xu)\,du-F_b(x).
\]
There exists exactly one \(x_b\in(0,\infty)\) such that \(\Delta_b(x_b)=0\). Moreover, \(\Delta_b(x)>0\) for \(0<x<x_b\) and \(\Delta_b(x)<0\) for \(x>x_b\). The crossing is characterized without numerical approximation by the unique positive solution of
\[
 b\left[\frac{x}{1+x}-(1-e^{-x})\right]
 +\int_0^\infty\frac{e^{-u}\,du}{1+b(1-e^{-xu})}
 -\frac1{1+b(1-e^{-x})}=0.
\]
As \(b\to\infty\),
\[
\boxed{\displaystyle
x_b\sim \left(\frac23\right)^{1/3}
\left(\frac{\log b}{b^2}\right)^{1/3}.}
\]
The more precise fixed-scale boundary-layer limit, for each fixed \(\xi>0\), is
\[
\boxed{\displaystyle
\frac{\Delta_b\bigl(\xi(\log b/b^2)^{1/3}\bigr)}
{b^{-1/3}(\log b)^{2/3}}
\longrightarrow -\frac{\xi^2}{4}+\frac{1}{6\xi}.}
\]
In contrast, at every fixed \(x>0\),
\[
\lim_{b\to\infty}\frac{\Delta_b(x)}b
=\frac12\left[\frac{x}{1+x}-(1-e^{-x})\right]<0.
\]
Thus the ordering at arbitrarily fast reset rates reverses the ordering obtained by first taking the zero-width (singular) reset limit.

## Assumptions and scope

Fix an Ornstein–Uhlenbeck process with drift \(\lambda>0\), diffusion strength \(D>0\), and independent Brownian increments:
\[
 dX_t=-\lambda X_t\,dt+\sqrt{2D}\,dB_t.
\]
After every reset, independently redraw \(X\) from \(N(0,v_0)\), where \(v_0=(D/\lambda)c\), \(0<c<1\). Between resets the conditional law remains centered Gaussian, with variance
\[
v(t)=\frac D\lambda\left[1-(1-c)e^{-2\lambda t}\right].
\]
For a mean reset interval \(1/r\), compare periodic intervals \(T=1/r\) with independent exponential intervals \(T\sim\operatorname{Exp}(r)\). Put \(b=(1-c)/c\), \(x=2\lambda/r\). The symmetrized endpoint KL per cycle equals \(F_b(2\lambda T)\). The long-run **endpoint-KL reward rates** (measured in natural information units per unit time) are
\[
R_{\rm per}=r F_b(x),\qquad
R_{\rm Poi}=r\int_0^\infty e^{-u}F_b(xu)\,du.
\]
Consequently \(R_{\rm Poi}-R_{\rm per}=r\Delta_b(x)\): Poisson spacing has strictly larger endpoint-KL rate for \(r>r_b:=2\lambda/x_b\), and strictly smaller rate for \(0<r<r_b\). The critical rate obeys
\[
\frac{r_b}{2\lambda}\sim\left(\frac32\right)^{1/3}
\left(\frac{b^2}{\log b}\right)^{1/3}.
\]
Only the **endpoint Gaussian KL functional** is compared here. This is a coarse-grained thermodynamic benchmark, not a claim that the implementation-dependent physical work or full entropy-production rates share this ordering. The finite post-reset width and independent redraw are essential.

## Proof

**1. Exact reduction.** For positive centered Gaussian variances \(v_0,v\), the sum of the two directed KL divergences is \(\tfrac12(v/v_0+v_0/v-2)\). Since \(v(t)/v_0=q_b(2\lambda t)\), this gives \(F_b\) and the two renewal-reward expressions. A Poisson interval is \(U/r\) with \(U\sim\operatorname{Exp}(1)\). Every reward is bounded by \(F_b(\infty)\), so the renewal-reward limit and all integrals exist.

**2. Exactly one inflection.** Let \(w=1+b\). Then \(q_b'(t)=w-q_b(t)=be^{-t}\). Direct differentiation gives
\[
 F_b''(t)=\frac{be^{-t}}{2q_b(t)^3}
\left[2w-q_b(t)-q_b(t)^3\right].
\]
The bracket strictly decreases from \(2b>0\) at \(t=0\) to \(w-w^3<0\) at \(t=\infty\), because \(q_b\) increases strictly from \(1\) to \(w\). Thus there is one \(t_b\in(0,\infty)\), with \(F_b''>0\) before \(t_b\) and \(F_b''<0\) after it. Also \(F_b(0)=F_b'(0)=0\) and \(F_b''(0)=b^2\).

**3. A single-crossing integral kernel.** Taylor's integral representation and exponential integration yield
\[
\Delta_b(x)=\int_0^\infty F_b''(s)K_x(s)\,ds,\quad
K_x(s)=xe^{-s/x}-(x-s)_+=x h(s/x),
\quad h(v)=e^{-v}-(1-v)_+>0\quad(v>0).
\]
These exchanges are justified by exponential decay of \(F_b''\) and by \(K_x(s)\le x e^{-s/x}+x\). Define \(Q(v)=v h'(v)/h(v)\) away from \(v=1\). On \(0<v<1\),
\[
Q'(v)=\frac{v^2e^{-v}-(1-e^{-v})^2}{(v-1+e^{-v})^2}<0,
\]
using \(2\sinh(v/2)>v\). On \(v>1\), \(Q(v)=-v\), also strictly decreasing; at \(v=1\) it jumps downward from \(e-1\) to \(-1\). Consequently \(Q\) is strictly decreasing on the positive half-line. If \(0<x_1<x_2\), then
\[
\frac{d}{d\log s}\log\frac{K_{x_2}(s)}{K_{x_1}(s)}
=Q(s/x_2)-Q(s/x_1)>0
\]
at every differentiability point. Thus \(K_{x_2}/K_{x_1}\) is strictly increasing in \(s\). If \(\Delta_b(x_1)=0\), let \(C=K_{x_2}(t_b)/K_{x_1}(t_b)\). For \(s<t_b\), \(K_{x_2}(s)-CK_{x_1}(s)<0\), and \(F_b''(s)>0\); for \(s>t_b\), both signs reverse. Hence
\[
\Delta_b(x_2)-C\Delta_b(x_1)
=\int_0^\infty F_b''(s)\bigl[K_{x_2}(s)-CK_{x_1}(s)\bigr]ds<0.
\]
Therefore once \(\Delta_b\) reaches zero it is strictly negative thereafter. (Equivalently, zero-to-positive recrossing is impossible.)

**4. Existence and direction of crossing.** Since \(F_b(t)=\tfrac12 b^2t^2+O_b(t^3)\) at zero and \(\mathbb E U^2=2\),
\[
\Delta_b(x)=\frac12 b^2x^2+O_b(x^3)>0\quad(x\downarrow0).
\]
At the other endpoint set \(L_b=\lim_{t\to\infty}F_b(t)\) and \(H_b(t)=L_b-F_b(t)\). Then \(H_b(t)>0\) and \(\int_0^\infty H_b(t)\,dt\in(0,\infty)\), while \(H_b(x)=O_b(e^{-x})\). Therefore
\[
\Delta_b(x)=H_b(x)-\frac1x\int_0^\infty e^{-t/x}H_b(t)\,dt
=-\frac1x\int_0^\infty H_b(t)\,dt+o_b(x^{-1})<0
\quad(x\to\infty).
\]
Continuity supplies at least one zero. Step 3 rules out a second zero: a later zero contradicts strict negativity after the first one. This also establishes both strict sign regions.

**5. Singular-width asymptotics.** Rewriting the exact difference gives
\[
2\Delta_b(x)=b\left[\frac{x}{1+x}-(1-e^{-x})\right]
+I_b(x)-\frac1{1+b(1-e^{-x})},\quad
I_b(x)=\int_0^\infty\frac{e^{-u}\,du}{1+b(1-e^{-xu})}.
\]
Let \(x=\xi(\log b/b^2)^{1/3}\) for fixed \(\xi>0\), and \(y=bx\). Then \(x\to0\), \(y\to\infty\), and
\[
b\left[\frac{x}{1+x}-(1-e^{-x})\right]=-\frac12 bx^2+O(bx^3).
\]
For \(0\le xu\le1\), the inequalities \(1-e^{-xu}\ge xu/2\) and \(0\le xu-(1-e^{-xu})\le(xu)^2/2\) imply
\[
0\le\frac1{1+b(1-e^{-xu})}-\frac1{1+yu}\le\frac1b.
\]
For \(u>1/x\), the discrepancy is at most one and its exponential probability mass is \(e^{-1/x}\). Thus, uniformly for \(\xi\) in a fixed compact subset of \((0,\infty)\),
\[
I_b(x)=\int_0^\infty\frac{e^{-u}\,du}{1+yu}
+O(b^{-1}+e^{-1/x})
=\frac{e^{1/y}E_1(1/y)}y+O(b^{-1}+e^{-1/x})
=\frac{\log y-\gamma_{\rm E}+o(1)}y+O(b^{-1}),
\]
where \(E_1(z)=\int_z^\infty e^{-t}t^{-1}\,dt\). Since \(\log y\sim(\log b)/3\) and \(1/[1+b(1-e^{-x})]=O(1/y)\), division by \(b^{-1/3}(\log b)^{2/3}\) yields the asserted limit \(-\xi^2/4+1/(6\xi)\). The limiting function is strictly decreasing, positive below \(\xi_*=(2/3)^{1/3}\), and negative above. The already proved unique-zero property pins \(x_b/[\log b/b^2]^{1/3}\to\xi_*\).

Finally, at fixed \(x>0\), the two reciprocal terms in the expression for \(2\Delta_b\) are bounded by one; dividing by \(b\) leaves the claimed negative limit. The strict negativity follows from \(e^x>1+x\), which implies \(1-e^{-x}>x/(1+x)\). This completes the proof.

## Verification

The standalone standard-library script `verify.py` independently integrates the exponential-cycle expression by adaptive quadrature, compares it with the exact reciprocal-integral identity, and numerically locates crossings for several variance ratios. It checks the Gaussian-KL algebra, derivative signs of the variation-diminishing kernel, numerical single-crossing profiles, and the signs in the asymptotic boundary layer. The program's finite tests support but do **not** establish uniqueness or an asymptotic limit; those are established by the proof above. Run with `python3 verify.py`. Representative approximate roots are \(x_1=0.428916361\), \(x_{10}=0.178585708\), and \(x_{1000}=0.014065207\).

## Relationship to prior work

Farago's 2026 *The Resetting Heat Engine* (arXiv:2605.28445, Sections II.C and Eqs. 11, 17–19) provides the harmonic Gaussian endpoint-KL benchmark and periodic and Poisson **singular-width approximations**. Those formulas motivate this question but do not supply the finite-width crossing, its uniqueness or the logarithmic critical scaling. In particular, taking \(b\to\infty\) before increasing reset frequency loses the high-rate ordering reversal.

Olsen, Gupta, Mori and Krishnamurthy (2024) study physical work and its fluctuations under finite-time resetting traps, including general waiting-time schemes; their physical work observable differs from the symmetrized Gaussian endpoint divergence here. Mori, Olsen and Krishnamurthy (2023) study actual stochastic entropy production for random reset positions; their model and entropy observable differ. Gupta, Olsen and Krishnamurthy (2025) optimize finite-duration physical erasure work, not the present endpoint-KL cadence comparison. These distinctions are statements of scope, not proof that no more general published theorem could recover the result.

## Limitations

The theorem pertains to independent Gaussian redraws in one-dimensional, time-homogeneous harmonic relaxation, and only to the endpoint symmetrized KL functional. It is not a prediction for the absolute dissipation of a laboratory reset mechanism, the work of physically switching a trap, trajectory-level entropy production, non-Gaussian exploration, or reset intervals with memory. It does not optimize over all renewal waiting-time laws. Numerics do not prove universal statements. Existing general convex-order or variation-diminishing results might provide alternative abstract derivations; the exact logarithmic \(b^{2/3}\) boundary was not found in the inspected sources. Independent external verification and publication-priority checks remain outstanding.

## References

1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445v1 (first posted 27 May 2026), https://arxiv.org/abs/2605.28445 .
2. K. S. Olsen, D. Gupta, F. Mori and S. Krishnamurthy, *Thermodynamic cost of finite-time stochastic resetting*, Physical Review Research **6**, 033343 (2024), arXiv:2310.11267, https://doi.org/10.1103/PhysRevResearch.6.033343 .
3. F. Mori, K. S. Olsen and S. Krishnamurthy, *Entropy production of resetting processes*, Physical Review Research **5**, 023103 (2023), arXiv:2211.15372, https://arxiv.org/abs/2211.15372 .
4. D. Gupta, K. S. Olsen and S. Krishnamurthy, *Thermodynamic cost of recurrent erasure*, Communications Physics **8**, 355 (2025), https://doi.org/10.1038/s42005-025-02277-w .
5. I. Neri, *Thermodynamic cost of random-time protocols*, Physical Review E **112**, 044114 (2025), https://doi.org/10.1103/8dmt-256h .
