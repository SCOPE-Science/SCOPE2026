# Almost-sure coalescence and shrinking-gap bounds for cusp diffusions

## Statement

Fix \(0<\beta<1/2\). Consider the one-dimensional SDE
\[
 dX_t^x=\sigma(X_t^x)\,dB_t,
\]
with two solutions driven by the same Brownian motion. The result applies to each of the two truncated cusp coefficients
\[
\sigma_+(x)=1+(\min\{x^+,2\})^\beta,
\qquad
\sigma_{\rm sym}(x)=1+(\min\{|x|,2\})^\beta,
\]
and also to their untruncated counterparts \(1+(x^+)^\beta\) and \(1+|x|^\beta\).

For ordered solutions write
\[
D_t=X_t^y-X_t^x\ge0,
\qquad
M_t=\frac{X_t^y+X_t^x}{2},
\qquad
\tau=\inf\{t:D_t=0\}.
\]
Set \(q=1-2\beta\in(0,1)\).

### 1. A tunable local collision bound

There are constants \(d_0>0\) and \(C_{\beta,\sigma}<\infty\) such that, when the pair starts symmetrically from \((-d/2,d/2)\) with \(0<d\le d_0\), and
\[
\rho=\inf\{t:|M_t|\ge1\ \hbox{or}\ D_t\ge1\},
\]
then for every \(a>0\),
\[
\boxed{
 \mathbb P(\tau<\rho)
 \ge e^{-a}-d-C_{\beta,\sigma}\frac{d^q}{a}.
}
\]
Consequently,
\[
\boxed{
 \mathbb P(\tau<\rho)
 \ge 1-d-2\sqrt{C_{\beta,\sigma}}\,d^{q/2}.
}
\]
In particular,
\[
\mathbb P(\tau<\rho)\longrightarrow1
\qquad(d\downarrow0).
\]
Thus the positive-probability collision in Larsen's cusp counterexample becomes asymptotically certain for a shrinking symmetric initial gap.

### 2. Collision-time upper scale

For every \(t>0\), the same symmetric pair satisfies
\[
\boxed{
 \mathbb P(\tau>t)
 \le
 d+2\sqrt{C_{\beta,\sigma}d^q
 \left(1+\sqrt{\frac{2}{\pi t}}\right)}.
}
\]
Hence
\[
\boxed{\tau_d=O_{\mathbb P}(d^{\,2-4\beta})}.
\]
More explicitly,
\[
\limsup_{d\downarrow0}
\mathbb P\!\left(\tau_d>M d^{2-4\beta}\right)
\le
2\sqrt{C_{\beta,\sigma}}\left(\frac{2}{\pi}\right)^{1/4}M^{-1/4},
\]
and therefore, for every \(r<2-4\beta\),
\[
\frac{\tau_d}{d^r}\xrightarrow{\mathbb P}0.
\]
No matching lower scale is claimed.

### 3. Every fixed ordered pair coalesces almost surely

For any deterministic \(x<y\), for each of the four cusp coefficients above,
\[
\boxed{
 \mathbb P_{x,y}(\tau<\infty)=1.
}
\]
By pathwise uniqueness, the two trajectories remain equal after \(\tau\). Thus the failure of strict comparison in the subcritical cusp regime is not merely an exceptional positive-probability event: every fixed pair of synchronously driven trajectories eventually coalesces almost surely.

## Proof

### Tunable local-time threshold

Larsen's proof of Theorem 3.1 introduces a Lyapunov function on the rectangle \(|M|<1,0<D<1\), together with a function \(h\in L^2(\mathbb R)\) and a constant \(\varepsilon>0\), and obtains, for the stopping time at which \(L_t^0(M)\) first reaches level one,
\[
\frac{\varepsilon\|h\|_2^2}{2}
\mathbb E L^0_{\lambda\wedge\rho\wedge\tau}(M)
\le d^q.
\]
Nothing in the stopped Ito argument uses the particular threshold one. For
\[
\lambda_a=\inf\{t:L_t^0(M)\ge a\},
\]
the same calculation gives
\[
\frac{\varepsilon\|h\|_2^2}{2}
\mathbb E L^0_{\lambda_a\wedge\rho\wedge\tau}(M)
\le d^q.
\]
Thus
\[
\mathbb P(\lambda_a<\tau\wedge\rho)
\le C_{\beta,\sigma}\frac{d^q}{a},
\qquad
C_{\beta,\sigma}:=\frac{2}{\varepsilon\|h\|_2^2}.
\]

The midpoint is a continuous local martingale. Under the Dambis--Dubins--Schwarz time change,
\[
M_t=W_{\langle M\rangle_t},
\qquad
L_t^0(M)=L^0_{\langle M\rangle_t}(W).
\]
Let \(\eta=\inf\{t:|M_t|=1\}\). Brownian local time at zero accumulated before exiting \((-1,1)\) is exponential with mean one, so
\[
\mathbb P(\lambda_a<\eta)=e^{-a}.
\]
Also \(D\) is a nonnegative local martingale and hence a supermartingale; Ville's inequality gives
\[
\mathbb P\left(\sup_{t\ge0}D_t\ge1\right)\le d.
\]
Repeating Larsen's final event decomposition with \(\lambda_a\) in place of the level-one stopping time yields
\[
\mathbb P(\tau<\rho)
\ge e^{-a}-d-C_{\beta,\sigma}d^q/a.
\]
Taking \(a=\sqrt{C_{\beta,\sigma}}d^{q/2}\) and using \(e^{-a}\ge1-a\) gives the second displayed local bound.

For the untruncated coefficients, Larsen's localization argument applies unchanged: on the local collision event the trajectories stay inside the region where the truncated and untruncated coefficients coincide, and pathwise uniqueness transfers the collision event.

### Time bound

For the symmetric initial pair, write
\[
dM_t=\Sigma_t\,dB_t,
\qquad
\Sigma_t=\frac{\sigma(X_t^y)+\sigma(X_t^x)}2.
\]
All four coefficients satisfy \(\sigma\ge1\), so
\[
\langle M\rangle_t=\int_0^t\Sigma_s^2\,ds\ge t.
\]
If \(T_a^L=\inf\{s:L_s^0(W)\ge a\}\), then \(\lambda_a\le T_a^L\). Levy's identity gives \(L_t^0(W)\stackrel d=|N(0,t)|\), hence
\[
\mathbb P(\lambda_a>t)
\le 2\Phi(a/\sqrt t)-1
\le \sqrt{\frac2\pi}\frac{a}{\sqrt t}.
\]
Combining this with the same event decomposition as above gives
\[
\mathbb P(\tau>t)
\le (1-e^{-a})+d+C_{\beta,\sigma}\frac{d^q}{a}
+\sqrt{\frac2\pi}\frac a{\sqrt t}.
\]
Using \(1-e^{-a}\le a\) and minimizing the two terms of the form \(A/a+Ba\) gives the displayed bound. Substituting \(t=M d^{2q}\) yields the tightness statement.

### Global almost-sure coalescence

Fix \(x<y\). Since \(D\) is a nonnegative local martingale, it converges almost surely to a finite limit \(D_\infty\).

First, \(D_\infty>0\) is impossible. On that event, convergence of the continuous local martingale \(D\) forces \(\langle D\rangle_\infty<\infty\). But
\[
\langle M\rangle_t\ge t,
\]
so the DDS Brownian motion representing \(M\) runs for infinite clock time and is recurrent. If \(D_\infty=d_*>0\), choose a small rectangle around
\[
(M,D)=(d_*/2,d_*).
\]
At its center the two positions are \(0\) and \(d_*\), so
\[
\Delta:=\sigma(M+D/2)-\sigma(M-D/2)
=\sigma(d_*)-\sigma(0)>0.
\]
By continuity, \(|\Delta|\) is bounded below on a sufficiently small rectangle, while \(\Sigma\) is bounded above there. Once \(D_t\) stays close to \(d_*\), recurrence and the Brownian occupation-time formula imply that \(M_t\) spends infinite physical time in the corresponding midpoint interval. Therefore
\[
\langle D\rangle_\infty
=\int_0^\infty \Delta_t^2\,dt
=\infty,
\]
a contradiction. Thus, on the event of no collision, necessarily \(D_t\to0\).

Now let
\[
H_k=\inf\{t\ge k:M_t=0\}.
\]
Again \(\langle M\rangle_t\ge t\), so recurrence gives \(H_k<\infty\) almost surely. On the no-collision event, \(D_{H_k}>0\) and \(D_{H_k}\to0\). At time \(H_k\) the pair is exactly symmetric, with positions \((-D_{H_k}/2,D_{H_k}/2)\). The two-point process is strong Markov, and the local estimate above therefore implies, whenever \(D_{H_k}\le d_0\),
\[
\mathbb P(\text{no future collision}\mid\mathcal F_{H_k})
\le D_{H_k}+2\sqrt{C_{\beta,\sigma}}D_{H_k}^{q/2}.
\]
For any fixed \(n\) with \(1/n\le d_0\), on the no-collision event we eventually have \(D_{H_k}\le1/n\). Taking \(k\to\infty\) and then \(n\to\infty\) gives
\[
\mathbb P(\tau=\infty)=0.
\]

## Context and originality boundary

Larsen (2026) proves that the cusp families above fail strict comparison for \(0<\beta<1/2\) by showing a finite-time collision with positive probability for sufficiently small symmetric initial gaps. The present statements sharpen that mechanism in three ways: the local collision probability tends to one as the initial gap shrinks; an explicit collision-time upper scale follows from a variable local-time threshold; and recurrence upgrades the local mechanism to almost-sure finite coalescence for every fixed ordered pair.

Almost-sure coalescence under a common Brownian driver is classical in other models. In particular, Barlow, Burdzy, Kaspi and Mandelbaum (2001) prove it for skew Brownian motions, whose singular local-time formulation is different from the continuous uniformly elliptic cusp diffusions considered here. Classical work of Yamada and of Ouknine--Rutkowski develops non-confluence and strong-comparison criteria. Those general themes are not claimed as new.

The originality claim is restricted to the quantitative shrinking-gap bounds and the almost-sure coalescence conclusion for Larsen's four cusp coefficients, to the best of our knowledge.

## Limitations

- The collision-time estimate is an upper-scale statement; no matching lower bound or limiting law is proved.
- The constants inherited from the Lyapunov proof are finite but are not optimized.
- Almost-sure coalescence is asserted for each fixed deterministic pair; no simultaneous statement for all uncountably many starting points is claimed.
- The full texts of Yamada (1986) and Ouknine--Rutkowski (1990) were not directly inspected; their accessible abstracts and bibliographic descriptions concern non-confluence/strong comparison and remain the main residual originality risk.
- The claims use the coefficient families and local Lyapunov estimates in arXiv:2609.19389v1; later revisions may change the source formulation.

## References

1. K. Larsen, *Strict SDE Comparison for Cusp Coefficients and Counterexamples*, arXiv:2609.19389v1 (2026). https://arxiv.org/abs/2609.19389
2. M. T. Barlow, K. Burdzy, H. Kaspi, A. Mandelbaum, *Coalescence of skew Brownian motions*, Seminaire de Probabilites XXXV (2001), 202--205. https://www.numdam.org/item/SPS_2001__35__202_0/
3. T. Yamada, *On the non-confluent property of solutions of one-dimensional stochastic differential equations*, Stochastics 17 (1986), 111--124. https://doi.org/10.1080/17442508608833385
4. Y. Ouknine, M. Rutkowski, *Strong comparison of solutions of one-dimensional stochastic differential equations*, Stochastic Processes and their Applications 36 (1990), 217--230.

Same-model review: passed. Independent audit: not yet performed.
