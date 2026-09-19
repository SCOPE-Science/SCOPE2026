# Second-order tail trichotomy for weighted porous-medium self-similarity

## Setting

Consider the self-similar profiles studied in Iagar--Munteanu, *A porous medium equation with dominating weighted absorption: three types of self-similar solutions* (arXiv:2609.20397v1):

\[
 u_t=\Delta u^m-|x|^\sigma u^p,\qquad 1<p<m,\quad \sigma>0,\quad N\ge1,
\]

with

\[
 u(x,t)=t^{-\alpha}f(\xi),\qquad \xi=|x|t^\beta,
\]
\[
 \alpha=\frac{\sigma+2}{D},\qquad
 \beta=\frac{m-p}{D},\qquad
 D=\sigma(m-1)+2(p-1).
\]

The profile equation is

\[
 (f^m)''+\frac{N-1}{\xi}(f^m)'+\alpha f-\beta\xi f'-\xi^\sigma f^p=0.
\]

The source paper proves that every bounded self-similar profile in its classification satisfies

\[
 f(\xi)\sim c_*\xi^{-a},\qquad
 a=\frac{\sigma}{p-1},\qquad
 c_*=(p-1)^{-1/(p-1)}.
\]

The next term undergoes a sharp transition at \(m=2p-1\).

Define

\[
 \delta=a(m-1)+2=\frac{D}{p-1},\qquad
 h=\frac1\beta=\frac{D}{m-p},\qquad
 \lambda=am=\frac{m\sigma}{p-1},
\]

and

\[
 d=c_*^{m-1}\lambda(\lambda-N+2).
\]

## Theorem: three second-order regimes

For every bounded source-paper profile with the above far-field limit:

### 1. Diffusion-forced regime: \(p<m<2p-1\)

Here \(\delta<h\), and

\[
 \boxed{
 f(\xi)=c_*\xi^{-a}\left(1+B_*\xi^{-\delta}+o(\xi^{-\delta})\right)
 }
\]

with the profile-independent coefficient

\[
 \boxed{
 B_*=
 \frac{(p-1)c_*^{m-1}\lambda(\lambda-N+2)}{2p-1-m}.
 }
\]

Thus all three origin classes identified in arXiv:2609.20397v1 have the same first relative correction at infinity.

### 2. Resonance: \(m=2p-1\)

Now \(\delta=h=2(\sigma+1)\). The two stable far-field rates coincide and a logarithmic term is forced:

\[
 \boxed{
 f(\xi)=c_*\xi^{-a}
 \left(1+B_{\log}\xi^{-\delta}\log\xi
 +C_f\xi^{-\delta}+o(\xi^{-\delta})\right),
 }
\]

where \(C_f\) may depend on the profile, while

\[
 \boxed{
 B_{\log}=2(\sigma+1)c_*^{m-1}\lambda(\lambda-N+2)
 }
\]

is universal.

### 3. Profile-memory regime: \(m>2p-1\)

Here \(h<\delta\). There is a profile-dependent constant \(C_f\in\mathbb R\) such that

\[
 \boxed{
 f(\xi)=c_*\xi^{-a}
 \left(1+C_f\xi^{-h}+o(\xi^{-h})\right).
 }
\]

The diffusion-forced correction is of smaller order, so the first correction generally retains information about which global profile approaches the common tail.

## Proof mechanism

Write

\[
 f(\xi)=c_*\xi^{-a}(1+\varepsilon(\xi)).
\]

The identities

\[
 \alpha+\beta a=\frac1{p-1}=c_*^{p-1}
\]

show that the linearization of the transport--absorption part in relative error is

\[
 \mathcal L\varepsilon=-\varepsilon-\beta\xi\varepsilon'.
\]

Meanwhile

\[
 \frac{\Delta_r(c_*^m\xi^{-am})}{c_*\xi^{-a}}
 =d\,\xi^{-\delta}.
\]

For a trial \(\varepsilon=B\xi^{-\delta}\),

\[
 \mathcal L\varepsilon
 =(-1+\beta\delta)B\xi^{-\delta},
 \qquad
 -1+\beta\delta=\frac{m-2p+1}{p-1}.
\]

When \(m\ne2p-1\), cancellation of the order \(\xi^{-\delta}\) residual gives the displayed \(B_*\). At resonance, \(\beta\delta=1\), while

\[
 \mathcal L\left(B\xi^{-\delta}\log\xi\right)
 =-\beta B\xi^{-\delta},
\]

which gives \(B_{\log}=d/\beta\).

To justify which correction is actually leading, use the source paper's center-manifold reduction at its tail critical point. Its logarithmic spatial variable satisfies \(\nu=\log\xi+\mathrm{const}\), and the reduced two-dimensional stable system has decay exponents

\[
 \delta=\frac{D}{p-1},\qquad h=\frac{D}{m-p}.
\]

Standard asymptotic integration of this smooth stable system gives: forced \(e^{-\delta\nu}\) dominance for \(\delta<h\); the resonant \(\nu e^{-\delta\nu}\) term for \(\delta=h\); and a homogeneous, profile-dependent \(e^{-h\nu}\) term for \(h<\delta\). The profile observable is smooth in the center coordinates, and nonlinear terms decay strictly faster than the first displayed correction. This yields the three expansions above.

## Harmonic cancellation

If

\[
 \lambda=N-2,
\]

then \(d=0\). This has a direct structural meaning:

\[
 (c_*\xi^{-a})^m=c_*^m\xi^{2-N}
\]

is radially harmonic away from the origin, so \(f_0=c_*\xi^{-a}\) is an exact singular profile there. Consequently the universal diffusion-forced coefficient vanishes. In the subresonant case the first relative correction is \(o(\xi^{-\delta})\); at resonance the logarithmic coefficient vanishes and the \(C_f\xi^{-\delta}\) term may remain.

## Verification

`artifacts/verify_tail_trichotomy.py` checks symbolically:

- the leading balance and the two decay exponents;
- the threshold \(m=2p-1\);
- the universal subresonant coefficient;
- the resonant logarithmic coefficient;
- consistency with the source paper's center-manifold coordinates; and
- the harmonic-cancellation condition.

The recorded output is in `artifacts/verification.txt`. This symbolic check supports the algebra; it is not independent validation.

## Scope and limitations

The result refines the far-field behavior of the bounded self-similar profiles classified in arXiv:2609.20397v1. It does not address stability of the corresponding PDE solutions, large-time attraction, or unbounded profile branches. The harmonic-cancellation case removes the universal forced term and can require further expansion to identify the next nonzero coefficient.

The novelty claim is intentionally narrow. General center-manifold asymptotics, resonance-generated logarithms, and second-order asymptotic methods are standard. A 2025 paper by Iagar--Laurençot develops second-order asymptotics for a different singular diffusion equation with gradient absorption (arXiv:2406.11518). Earlier homogeneous porous-medium absorption literature, including McLeod--Peletier--Vázquez (1991), is also relevant; its complete text was not fully inspected here. The present claim is the explicit \(m=2p-1\) weighted-tail trichotomy and coefficients for the model of arXiv:2609.20397v1, to the best of our knowledge.

## References

1. R. G. Iagar and D.-R. Munteanu, *A porous medium equation with dominating weighted absorption: three types of self-similar solutions*, arXiv:2609.20397v1 (2026). https://arxiv.org/abs/2609.20397
2. R. G. Iagar and D.-R. Munteanu, *A porous medium equation with spatially inhomogeneous absorption. Part I: Self-similar solutions*, J. Math. Anal. Appl. 543 (2025), 128965; arXiv:2406.00349. https://arxiv.org/abs/2406.00349
3. R. G. Iagar and P. Laurençot, *Second order asymptotics and uniqueness for self-similar profiles to a singular diffusion equation with gradient absorption*, Nonlinearity 38 (2025), 035013; arXiv:2406.11518. https://arxiv.org/abs/2406.11518
4. J. B. McLeod, L. A. Peletier and J. L. Vázquez, *Solutions of a nonlinear ODE appearing in the theory of diffusion with absorption*, Differential and Integral Equations 4 (1991), 1--14.
