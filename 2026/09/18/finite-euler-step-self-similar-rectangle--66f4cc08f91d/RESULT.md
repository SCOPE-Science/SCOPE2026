# Finite Euler step profiles converge to a universal self-similar rectangle

## Statement

Consider the reduced scale-invariant, odd, $m$-fold symmetric two-dimensional Euler system on one positive sector,
\[
\partial_t g+2G\,\partial_\theta g=0,\qquad
4G+\partial_{\theta\theta}G=g,
\qquad G(t,0)=G(t,\pi/m)=0,
\]
with $m\ge 4$. Let the initial datum be a finite positive step function of the form used in Proposition 2.4 of Suleiman (2026),
\[
g_0(\theta)=\sum_{k=1}^n c_k\mathbf 1_{(a_k,b_k]}(\theta),
\qquad
0<a_1<b_1<\cdots<a_n<b_n<\frac{\pi}{m},
\qquad 0<c_k\le 1.
\]
Transport preserves this form, so write the endpoints as $a_k(t),b_k(t)$ and let $c_*:=c_n$ be the height of the rightmost interval.

Then the source paper's two-sided $O(t^{-1})$ estimate for the rightmost endpoint and sector mass sharpens to the exact laws
\[
\boxed{\lim_{t\to\infty}t\,b_n(t)=\frac1{c_*}},
\qquad
\boxed{\lim_{t\to\infty}t\,\|g(t)\|_{L^1(0,\pi/m)}=1}.
\]
Every other endpoint $x(t)\in\{a_1,b_1,\ldots,a_n\}$ satisfies
\[
\boxed{t\,x(t)\longrightarrow0},
\]
and the weighted moment has the exact asymptotic
\[
\boxed{
\lim_{t\to\infty}t^2\int_0^{\pi/m}\sin(2\theta)g(t,\theta)\,d\theta
=\frac1{c_*}.
}
\]
By odd and $m$-fold extension, the full-circle $L^1$ norm consequently satisfies $t\|g(t)\|_{L^1(\mathbb S^1)}\to2m$.

More structurally, in the similarity variable $y=t\theta$,
\[
F_t(y):=g\!\left(t,\frac yt\right)
\]
converges in $L^1(\mathbb R_+)$ to the universal rectangle
\[
\boxed{
F_*(y)=c_*\mathbf 1_{(0,1/c_*]}(y).
}
\]
Thus all finitely many inner steps disappear at the $t^{-1}$ angular scale; the only datum retained by the leading similarity profile is the height of the rightmost step.

The stream function also has an explicit similarity limit. Uniformly for $y$ in compact subsets of $[0,\infty)$,
\[
\boxed{
t^2G\!\left(t,\frac yt\right)\longrightarrow \mathcal G_*(y)
=-c_*\int_0^{1/c_*}\min(y,z)\,dz,
}
\]
that is,
\[
\mathcal G_*(y)=
\begin{cases}
-y+\dfrac{c_*}{2}y^2,&0\le y\le 1/c_*,\\[1mm]
-\dfrac1{2c_*},&y\ge1/c_*.
\end{cases}
\]
In logarithmic similarity time $\tau=\log t$, the limiting transport velocity is therefore
\[
\boxed{V_*(y)=y+2\mathcal G_*(y)=y(c_*y-1)}
\qquad (0\le y\le1/c_*),
\]
whose two zeros are exactly the two jump locations of $F_*$. The rectangle is therefore a stationary state of the limiting similarity transport equation.

## Proof

Suleiman's Proposition 2.4 gives
\[
b_n(t)\asymp (1+t)^{-1}
\]
and proves that every endpoint other than $b_n$ is integrable on $[0,\infty)$. The Green kernel is negative in the interior, so all endpoint trajectories are positive and nonincreasing. If $x$ is any positive nonincreasing integrable function, then
\[
\frac t2x(t)\le \int_{t/2}^t x(s)\,ds\longrightarrow0.
\]
Hence every endpoint other than $b_n$ is $o(t^{-1})$, and therefore also $o(b_n)$.

For the rightmost endpoint, the exact endpoint equation from the source is
\[
b_n'=
\frac{\sin(2(\pi/m-b_n))}{2\sin(2\pi/m)}
\sum_{k=1}^n c_k\bigl(\cos(2b_k)-\cos(2a_k)\bigr).
\]
As $t\to\infty$, the prefactor tends to $1/2$. For $k<n$, Taylor expansion and $b_k=o(b_n)$ give
\[
\cos(2b_k)-\cos(2a_k)=O(b_k^2)=o(b_n^2).
\]
For the last interval, $a_n=o(b_n)$ and
\[
\cos(2b_n)-\cos(2a_n)
=-2(b_n^2-a_n^2)+O(b_n^4+a_n^4)
=-2b_n^2(1+o(1)).
\]
Consequently
\[
 b_n'=-c_*b_n^2(1+o(1)).
\]
Equivalently,
\[
\left(\frac1{b_n}\right)'=c_*(1+o(1)).
\]
After integration and division by $t$,
\[
\frac1{t b_n(t)}\longrightarrow c_*,
\]
which proves $t b_n\to c_*^{-1}$.

The sector mass is
\[
\|g(t)\|_1=\sum_{k=1}^n c_k(b_k-a_k).
\]
All $k<n$ intervals have length $o(t^{-1})$, and $a_n=o(t^{-1})$, so
\[
\|g(t)\|_1=c_*b_n(t)+o(t^{-1}),
\]
which yields $t\|g(t)\|_1\to1$.

For the weighted moment,
\[
M(t)=\frac12\sum_{k=1}^n c_k\bigl(\cos(2a_k)-\cos(2b_k)\bigr).
\]
The inner contributions are $o(t^{-2})$, while the last interval contributes
\[
c_*(b_n^2-a_n^2)+O(b_n^4+a_n^4)
=c_*b_n^2(1+o(1)).
\]
Thus $t^2M(t)\to c_*^{-1}$.

For the profile limit, the scaled endpoints satisfy
\[
tb_n(t)\to1/c_*,\qquad tx(t)\to0
\]
for every other endpoint. The finitely many inner intervals therefore have total scaled length tending to zero, whereas the rightmost interval tends to $(0,1/c_*]$. Since the heights are fixed and bounded, this is exactly
\[
F_t\to c_*\mathbf 1_{(0,1/c_*]}
\quad\text{in }L^1(\mathbb R_+).
\]

Finally, the source Green kernel is
\[
K_m(\theta,\zeta)
=-\frac1{2s_m}
\begin{cases}
\sin(2\theta)\sin(2(\pi/m-\zeta)),&\theta\le\zeta,\\
\sin(2\zeta)\sin(2(\pi/m-\theta)),&\zeta\le\theta,
\end{cases}
\qquad s_m=\sin(2\pi/m).
\]
For bounded $y,z$,
\[
tK_m(y/t,z/t)\longrightarrow-\min(y,z)
\]
uniformly. Since the support of $F_t$ remains in a fixed bounded $y$-interval for all sufficiently large $t$,
\[
t^2G(t,y/t)=\int_0^\infty [tK_m(y/t,z/t)]F_t(z)\,dz
\]
converges locally uniformly in $y$ to $\mathcal G_*$. If $F(\tau,y)=g(e^\tau,e^{-\tau}y)$, the transport equation becomes
\[
\partial_\tau F+\bigl(y+2e^{2\tau}G(e^\tau,e^{-\tau}y)\bigr)\partial_yF=0,
\]
so the limiting velocity on the support is $V_*(y)=y(c_*y-1)$.

## Context and originality boundary

The source preprint proves only comparability estimates $b_n(t)\asymp(1+t)^{-1}$, $\|g(t)\|_1\asymp(1+t)^{-1}$, an $O((1+t)^{-2})$ weighted-moment bound, and integrability of every endpoint except $b_n$. The exact constants, $L^1$ similarity profile, scaled Green-field limit, and limiting similarity transport field above are not stated there.

Earlier work of Elgindi, Murray and Said establishes long-time relaxation of regulated scale-invariant Euler profiles to finite-jump states. That qualitative relaxation theory, the Green-kernel representation, monotonicity, and the general use of similarity variables are not originality claims here. A recent paper by Cao, Fan and Qin treats the distinct $m=3$ case and relaxation to jump profiles. The originality claim is restricted to the source-specific sharp asymptotics and self-similar finite-step mechanism above, to the best of our knowledge.

## Limitations

The theorem concerns finite positive step data satisfying the ordering, sign, and $m\ge4$ hypotheses of the source proposition. It does not establish the same similarity law for arbitrary regulated data, for the source paper's infinite stack used to construct a dense orbit, or for the $m=3$ dynamics. No convergence rate beyond the displayed leading limits is claimed. The limit is formulated on one positive sector; the full-circle statement follows only by the prescribed odd and $m$-fold extension.

## Reproducibility

`artifacts/verify_step_similarity.py` integrates the exact finite endpoint system through the Green kernel for a three-step example and compares the computed quantities with the theorem. `artifacts/verification_output.txt` records the numerical output. This numerical check supports but does not replace the analytic proof.

## References

1. I. Suleiman, *Dense orbits for scale-invariant rotationally symmetric solutions of the 2D Euler equations*, arXiv:2609.20674v1 (2026). https://arxiv.org/abs/2609.20674
2. T. M. Elgindi, R. W. Murray, A. R. Said, *On the long-time behavior of scale-invariant solutions to the 2d Euler equation and applications*, Ann. Sci. Éc. Norm. Supér. 58 (2025), 943–970. https://doi.org/10.24033/asens.2621 ; arXiv:2211.08418.
3. D. Cao, J. Fan, G. Qin, *Gradient growth and relaxation to jump profiles for 3-fold symmetric scale-invariant Euler flows*, arXiv:2608.16755 (2026). https://arxiv.org/abs/2608.16755
4. T. M. Elgindi, I. Jeong, *Symmetries and critical phenomena in fluids*, Comm. Pure Appl. Math. 73 (2020), 257–316.
