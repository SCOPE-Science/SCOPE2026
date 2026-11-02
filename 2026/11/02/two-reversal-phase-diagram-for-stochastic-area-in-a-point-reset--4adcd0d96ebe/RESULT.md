# Two-reversal phase diagram for stochastic area in a point-reset Brownian gyrator

## Finding

In a two-temperature planar Brownian gyrator with complete Poisson relocation to a fixed point, the **total pathwise signed area** (including the straight chords representing the reset jumps) can reverse its stationary production direction twice as the reset rate increases. There is a necessary-and-sufficient inequality for two positive crossings, a unique tangency at its sharp boundary, and no other zero-count possibility.

Write \(T_x,T_y>0\), \(0<u<1\), \(r>0\), and let the fixed reset point be \((a,b)\in\mathbb R^2\). Put
\[
\Delta_T=T_x-T_y,\qquad \Delta_R=a^2-b^2,\qquad s=\sqrt{1-u^2}.
\]
For the stationary total signed area production rate \(J(r)\), normalized as twice the usual geometric area per time,
\[
\boxed{J(r)=\frac{u}{r+2}\left[2\Delta_T+\frac{r(1-u^2)\Delta_R}{(r+1)^2-u^2}\right].}
\]
If \(\Delta_T\ne0\), put \(q=-(1-u^2)\Delta_R/(2\Delta_T)\). Then:

- If \(q<2(1+s)\), the rate \(J(r)\) never vanishes and has the sign of \(\Delta_T\) for all \(r>0\).
- If \(q=2(1+s)\), there is exactly one positive zero, at \(r=s\), of multiplicity two; the sign does not change.
- If \(q>2(1+s)\), there are exactly two simple positive zeros,
\[
 r_\pm=\frac{q-2\pm\sqrt{(q-2)^2-4(1-u^2)}}{2},\qquad r_-r_+=1-u^2.
\]
The sign of \(J\) is that of \(\Delta_T\) outside the interval \((r_-,r_+)\) and its opposite inside. For \(\Delta_T=0\), the sign at every positive reset rate equals that of \(\Delta_R\), or else the rate is identically zero if \(\Delta_R=0\).

For an exact nondegenerate example, take \(u=3/5\), \(T_x=2\), \(T_y=1\), and reset to \((a,b)=(0,5/\sqrt2)\). Then
\[
J(r)=\frac{6(5r-8)(5r-2)}{5(r+2)(5r+2)(5r+8)},
\]
so the only positive direction reversals occur at \(r=2/5\) and \(r=8/5\).

## Assumptions and scope

Between resets the process obeys, with independent standard Brownian drivers,
\[
\begin{aligned}
 dX_t&=(-X_t+uY_t)\,dt+\sqrt{2T_x}\,dW_t^x,\\
 dY_t&=(-Y_t+uX_t)\,dt+\sqrt{2T_y}\,dW_t^y.
\end{aligned}
\]
An independent Poisson clock of intensity \(r\) instantly relocates both coordinates to \((a,b)\), keeping all subsequent Brownian increments independent. Define the full càdlàg signed area functional by the Itô semimartingale integral
\[
\mathcal A_t=\int_{(0,t]}\bigl(X_{s-}\,dY_s-Y_{s-}\,dX_s\bigr).
\]
The jump contribution at a reset from \((x,y)\) to \((a,b)\) is \(xb-ya\), exactly the oriented straight-chord contribution; the continuous contribution is the standard signed stochastic area. The conventional geometric area is \(\mathcal A_t/2\). There is no assumption that instantaneous resetting physically transports a particle along the chord. This is a **geometric observable of the recorded jump path**, not the physical heat, work, or torque done during resetting.

For every stated parameter choice, the point-reset process is regenerative and has a unique stationary probability law with finite moments of all polynomial orders. The result concerns the expectation and almost-sure stationary long-time production rate \(J(r)=\lim_{t\to\infty}\mathcal A_t/t\), which agree; it is not an assertion that finite-window realized areas have a fixed sign.

## Proof

**Stationarity and moments.** At each reset the process restarts at the deterministic point. The independent exponential interreset times and stable linear drift give a unique stationary law, equivalently the exponential-age mixture of the unreset Ornstein–Uhlenbeck transition laws. Its generator on smooth polynomial tests is
\[
Lf=(-x+uy)\partial_x f+(-y+ux)\partial_y f+T_x\partial_{xx}f+T_y\partial_{yy}f+r\{f(a,b)-f(x,y)\}.
\]
Let \(m_x=\mathbb E X\), \(m_y=\mathbb E Y\), and \(Q=\mathbb E(X^2-Y^2)\), all in stationarity. The identities \(\mathbb E(Lx)=\mathbb E(Ly)=\mathbb E(L(x^2-y^2))=0\) yield
\[
\begin{aligned}
(r+1)m_x-um_y&=ra,\\
-um_x+(r+1)m_y&=rb,\\
(r+2)Q&=2\Delta_T+r\Delta_R.
\end{aligned}
\]
The final equation is exact because the two \(2uXY\) drift terms cancel. Inverting the first two equations, whose determinant \((r+1)^2-u^2\) is positive, gives
\[
\begin{aligned}
m_x&=\frac{r[(r+1)a+ub]}{(r+1)^2-u^2},\\
m_y&=\frac{r[ua+(r+1)b]}{(r+1)^2-u^2}.
\end{aligned}
\]

**The two area contributions.** Between resets, independent Brownian drivers give zero expected cross-Itô increments. The continuous area drift is
\[
\mathbb E[X(-Y+uX)-Y(-X+uY)]=uQ.
\]
At a reset, the jump area is \(X_{-}(b-Y_{-})-Y_{-}(a-X_{-})=bX_{-}-aY_{-}\). The predictable Poisson compensator therefore contributes the stationary rate \(r(bm_x-am_y)\). Using the preceding moment identities,
\[
\begin{aligned}
J(r)&=uQ+r(bm_x-am_y)\\
&=\frac{u[2\Delta_T+r\Delta_R]}{r+2}-\frac{r^2u\Delta_R}{(r+1)^2-u^2}\\
&=\frac{u}{r+2}\left[2\Delta_T+\frac{r(1-u^2)\Delta_R}{(r+1)^2-u^2}\right].
\end{aligned}
\]
The last equality follows from the exact identity \(r/(r+2)-r^2/[(r+1)^2-u^2]=r(1-u^2)/[(r+2)((r+1)^2-u^2)]\).

**Sharp zero count.** For \(\Delta_T\ne0\), the rate is \(2u\Delta_T/(r+2)\) multiplied by \(1-qh(r)\), where
\[
h(r)=\frac{r}{(r+1)^2-u^2},\quad h'(r)=\frac{1-u^2-r^2}{[(r+1)^2-u^2]^2}.
\]
The function \(h\) is strictly positive, tends to zero at both ends of \((0,\infty)\), and attains its unique maximum \(1/[2(1+s)]\) at \(r=s\). This proves the three regimes including the double-root boundary, without relying on numerical scanning. When \(q>2(1+s)\), solving \(q h(r)=1\) gives the stated roots; Vieta's formula gives their product \(s^2\). The \(\Delta_T=0\) case follows directly from the exact positive-factor expression. Substitution gives the stated example.

**Long-time interpretation.** Successive complete reset cycles form i.i.d. regenerative blocks, with finite expected length and integrable signed area reward. The renewal-reward law establishes the almost-sure cycle-area rate, and the semimartingale compensator calculation gives its expectation; both equal \(J(r)\). The finite-moment exponential-cycle bounds control the incomplete last cycle. Thus the sign classification concerns both stationary expected and almost-sure long-run area production.

## Verification

The accompanying \(CHECK.py\) is self-contained given the declared Python packages. It independently (i) solves the stationary generator equations symbolically, (ii) verifies the complete area identity and the exact boundary example, (iii) checks the derivative and maximum of the controlling rational function, (iv) evaluates eight high-precision independent renewal-reward integrals, and (v) samples three stationary laws using exponential reset ages and exact conditional Gaussian Ornstein–Uhlenbeck distributions. All checks were executed successfully from this exact program. Finite random tests are consistency checks, **not** substitutes for the generator and analytic root-count proof.

## Relationship to prior work

Viot et al., arXiv:2307.05248, study the conventional continuous-path Brownian gyrator and obtain its mean angular-momentum rate \(u(T_x-T_y)\). The current theorem reproduces that result when \(r\downarrow0\), but additionally incorporates instantaneous resets to a fixed, generally off-axis position and the chordal jump terms. Their focus is on fluctuations of angular momentum and angular velocity, not a Poisson-reset-dependent two-reversal phase diagram.

Du Buisson, Mnyulwa and Touchette, arXiv:2307.06245, analyze stochastic area of **continuous linear diffusions**, including general stationary area formulas, but their process has no jump-reset generator. Their formula cannot be directly applied to the chord area accumulated by relocations. Mori, Olsen and Krishnamurthy, arXiv:2211.15372, study entropy production under instantaneous resetting in confining potentials, a different observable without this planar gyrator area classification. These works motivate the objects and methods but do not assert the two-crossing result. This is a best-knowledge literature comparison, not a claim of independently certified publication priority.

## Limitations

The result is restricted to stable symmetric two-dimensional linear drift with \(0<u<1\), diagonal independent thermal forcing, and complete homogeneous-rate Poisson resets to one deterministic point. The area includes **the reset chords by definition**; continuous-only angular momentum need not show the same two crossings. It is not a theorem about physical heat-work conversion, average angular velocity normalized by radius, higher-current fluctuations, or a finite observation window. Further primary-literature discoveries might affect priority; no independent scientific audit has been performed.

## References

1. P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, and G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (first public 2023-07-11), https://arxiv.org/abs/2307.05248.
2. J. du Buisson, T. D. P. Mnyulwa, and H. Touchette, *Large deviations of the stochastic area for linear diffusions*, arXiv:2307.06245 (first public 2023-07-12), https://arxiv.org/html/2307.06245v3.
3. F. Mori, K. S. Olsen, and S. Krishnamurthy, *Entropy production of resetting processes*, arXiv:2211.15372 (first public 2022-11-28), https://arxiv.org/abs/2211.15372.
