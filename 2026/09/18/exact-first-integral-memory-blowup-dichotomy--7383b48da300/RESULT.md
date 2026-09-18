# Exact first integral reveals a two-sided blow-up dichotomy for exponential memory

## Source and question

Ichida, *Memory-induced blow-up solutions and their dynamical transitions in distributed delay differential equations* (arXiv:2609.15470v1), studies

\[
\dot u(t)=\frac{1}{1-v(t)},\qquad
v(t)=\int_{-\infty}^t \alpha e^{-\beta(t-s)}u(s)\,ds,
\qquad \alpha,\beta>0,
\]

under a positive bounded history \(u(s)=\phi(s)\) for \(s\le 0\). Its Theorem 2 is stated for every such positive history and concludes positive logarithmic blow-up. In the proof, however, the analysis is explicitly restricted to \(0\le v(t)<1\) before the change of variables \(w=(1-v)^{-1}\). The theorem statement does not assume \(v(0)<1\).

The missing initial-memory distinction can be resolved completely, and the same calculation sharpens the stated blow-up constants.

## Exact first integral

The exponential kernel gives the exact linear-chain system

\[
\dot u=\frac1{1-v},\qquad \dot v=\alpha u-\beta v.
\]

On either component \(v<1\) or \(v>1\), set

\[
w=\frac1{1-v},\qquad
\Phi(u)=\frac{\alpha}{2}u^2-\beta u.
\]

Then

\[
\dot u=w,\qquad
\dot w=(\alpha u-\beta)w^2+\beta w.
\]

Since \(w\ne0\), using \(u\) as the independent variable gives the linear equation

\[
\frac{dw}{du}-(\alpha u-\beta)w=\beta.
\]

Hence every trajectory satisfies the exact first integral

\[
\boxed{
\mathcal H(u,w)
=e^{-\Phi(u)}w
-\beta\int_0^u e^{-\Phi(s)}\,ds
=\text{constant}.
}
\]

Equivalently, for initial data \((u_0,v_0)\) with \(v_0\ne1\), \(w_0=(1-v_0)^{-1}\),

\[
\boxed{
w(u)=e^{\Phi(u)}Q(u)},\qquad
Q(u)=w_0e^{-\Phi(u_0)}+\beta\int_{u_0}^u e^{-\Phi(s)}\,ds.
\]

## Complete initial-memory dichotomy

Let

\[
v_0=\alpha\int_{-\infty}^{0}e^{\beta s}\phi(s)\,ds.
\]

Then the following trichotomy holds.

### 1. Subcritical initial memory: \(v_0<1\)

Here \(w_0>0\). For every \(u\ge u_0\),

\[
Q(u)\ge w_0e^{-\Phi(u_0)}>0,
\]

so \(u\) is strictly increasing. It cannot approach a finite limit. Moreover

\[
T-t_0
=\int_{u_0}^{\infty}\frac{e^{-\Phi(u)}}{Q(u)}\,du
<\infty
\]

because \(e^{-\Phi(u)}\) is Gaussian at infinity. Thus

\[
\boxed{u(t)\to+\infty,\qquad v(t)\to1^-}
\]

in finite time. This is the regime analyzed in the source paper.

### 2. Critical initial memory: \(v_0=1\)

The denominator in the original equation already vanishes at \(t=0\). Thus there is no classical solution starting from such a history without an additional singular-solution convention.

### 3. Supercritical initial memory: \(v_0>1\)

Here \(w_0<0\). For every \(u\le u_0\),

\[
Q(u)\le w_0e^{-\Phi(u_0)}<0,
\]

so \(u\) is strictly decreasing. Again it cannot approach a finite limit, and

\[
T-t_0
=\int_{-\infty}^{u_0}\frac{e^{-\Phi(u)}}{-Q(u)}\,du
<\infty.
\]

Consequently

\[
\boxed{u(t)\to-\infty,\qquad v(t)\to1^+}
\]

in finite time. Thus the omitted half-plane does not produce the positive blow-up claimed by Theorem 2 as written; it produces a mirror logarithmic blow-down.

A particularly simple admissible history is obtained with \(\alpha=\beta=1\) and \(\phi(s)\equiv2\). Then \(u_0=v_0=2\), so the equation is initially regular but the solution belongs to the supercritical branch and satisfies \(u(t)\to-\infty\). By contrast, \(\phi(s)\equiv1\) gives \(v_0=1\), for which the right-hand side is singular already at the initial time. Both histories satisfy the positive bounded-history assumption in the source theorem.

If one additionally insists that the state must remain nonnegative, the \(v_0>1\) trajectory crosses \(u=0\) before its negative blow-up; under that convention the positive state-space solution terminates earlier. Either interpretation contradicts a universal positive-blow-up conclusion for all positive bounded histories.

## Universal leading constants and a sharper expansion

The first integral also removes the unspecified leading constants in the source theorem. Let

\[
\sigma=\operatorname{sgn}(1-v_0)\in\{+1,-1\}.
\]

Define

\[
L_+=w_0e^{-\Phi(u_0)}+
\beta\int_{u_0}^{\infty}e^{-\Phi(s)}\,ds
\quad (v_0<1),
\]

and

\[
L_-=-w_0e^{-\Phi(u_0)}+
\beta\int_{-\infty}^{u_0}e^{-\Phi(s)}\,ds
\quad (v_0>1).
\]

Both are positive. Write \(L_\sigma\) for the corresponding quantity and

\[
C_\sigma=\log L_\sigma-\frac{\beta^2}{2\alpha},
\qquad
S=\log\frac1{T-t}.
\]

Since

\[
\Phi(u)=\frac{(\alpha u-\beta)^2}{2\alpha}
-\frac{\beta^2}{2\alpha},
\]

Gaussian-tail asymptotics give, with
\(y=|\alpha u-\beta|\),

\[
T-t
=\frac{e^{-\Phi(u)}}{L_\sigma y}
\left(1+O(y^{-2})\right),
\]

and therefore

\[
S=\frac{y^2}{2\alpha}+\log y+C_\sigma+O(y^{-2}).
\]

Inverting this relation yields

\[
\boxed{
\begin{aligned}
u(t)
={}&\frac{\beta}{\alpha}
+\sigma\sqrt{\frac{2S}{\alpha}}\\
&-\sigma\frac{\tfrac12\log(2\alpha S)+C_\sigma}
{\sqrt{2\alpha S}}
+O\!\left(\frac{(\log S)^2}{S^{3/2}}\right).
\end{aligned}}
\]

Also

\[
\boxed{
\dot u(t)
=\frac{\sigma}{(T-t)\sqrt{2\alpha S}}
\left(1+O\!\left(\frac{\log S}{S}\right)\right)
}
\]

and

\[
\boxed{
1-v(t)
=\sigma (T-t)\sqrt{2\alpha S}
\left(1+O\!\left(\frac{\log S}{S}\right)\right).
}
\]

In particular, on the positive branch the constants denoted \(A_3,A_4\) in Theorem 2 are not free trajectory-dependent constants:

\[
\boxed{A_3=\sqrt{\frac2\alpha},\qquad
A_4=\frac1{\sqrt{2\alpha}}.}
\]

The forgetting rate \(\beta\) does not enter these leading amplitudes. It first appears through the additive shift \(\beta/\alpha\) and the lower-order constant \(C_\sigma\); the initial history enters through \(L_\sigma\).

## Why this matters

The exact first integral gives a global phase foliation for the F2 linear-chain system and converts a one-sided compactification result into a complete classification by the initial memory. It both repairs the missing hypothesis in the source theorem and explains which parts of the logarithmic singularity are universal versus history-dependent.

The correction is source-specific. The linear-chain trick, reduction of planar systems by taking one state as the independent variable, and Gaussian-tail asymptotics are standard and are not claimed as new general techniques.

## Verification

`artifacts/verify.py` checks the first-integral identity symbolically and evaluates both branches for \(\alpha=\beta=1\). For constant histories \(\phi\equiv1/2\) and \(\phi\equiv2\), the computed asymptotic ratios at \(|u|=10\) are already close to one on the predicted positive and negative branches.

## Limitations

This result concerns the source paper's F2 nonlinearity with a single exponential memory kernel. It does not classify F1 or the self-inhibited F3 model. The two-sided statement uses the natural real-valued continuation of the ODE/DDE wherever \(v\ne1\); a biological interpretation that forbids negative \(u\) should instead regard the \(v_0>1\) branch as leaving the admissible state space before the singularity. No claim is made that the elementary first-integral method is new outside this source-specific application.

## References

- Yu Ichida, *Memory-induced blow-up solutions and their dynamical transitions in distributed delay differential equations*, arXiv:2609.15470v1 (2026): https://arxiv.org/abs/2609.15470
- Full HTML of the source paper: https://arxiv.org/html/2609.15470v1
