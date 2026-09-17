# Critical elephant cover times: exact rare-path profiles and mean constants

## Statement

Consider the one-dimensional elephant random walk \((\widetilde S_n)_{n\ge 0}\) at the critical memory parameter \(p=3/4\), with symmetric first step. For \(L\ge2\), let its projection to \(\mathbb Z/L\mathbb Z\) have cover time

\[
\tau_{\rm cov}
=
\inf\left\{n\ge0:
\max_{0\le j\le n}\widetilde S_j-\min_{0\le j\le n}\widetilde S_j
\ge L-1
\right\},
\]

and let

\[
\sigma_L=\inf\{n\ge0:|\widetilde S_n|=L\}.
\]

Qin proved in arXiv:2609.17264v1 that

\[
\mathbb E\tau_{\rm cov}
=
\Theta\!\left(\frac{L^2}{\sqrt{\log L}}\right),
\qquad
\mathbb E\sigma_L
=
\Theta\!\left(\frac{L^2}{\sqrt{\log L}}\right),
\]

and explicitly asked whether the normalized critical cover-time mean has a positive finite limit.

The limit exists. It is described by a Brownian rare-path profile.

Let \(B=(B_u)_{u\ge0}\) be standard Brownian motion. For \(y\in\mathbb R\), define the exponentially damped Brownian path

\[
X^{(y)}_u=e^{-u/2}(y+B_u),\qquad u\ge0.
\]

By the law of the iterated logarithm, \(X^{(y)}_u\to0\) almost surely. Put

\[
M_y=\sup_{u\ge0}|X^{(y)}_u|,
\qquad
R_y=\sup_{u\ge0}X^{(y)}_u-\inf_{u\ge0}X^{(y)}_u.
\]

For \(t>0\), define

\[
\mathcal H_{\rm exit}(t)
=
\frac{1}{2\sqrt\pi}
\int_{\mathbb R}
\mathbb P\!\left(M_y<t^{-1/2}\right)\,dy,
\]

and

\[
\mathcal H_{\rm cov}(t)
=
\frac{1}{2\sqrt\pi}
\int_{\mathbb R}
\mathbb P\!\left(R_y<t^{-1/2}\right)\,dy.
\]

The integrals are finite pointwise, because either event implies \(|y|<t^{-1/2}\).

### Theorem 1: critical rare-path profiles

At every continuity point of the corresponding right-hand side,

\[
\sqrt{\log L}\,
\mathbb P\!\left(
\sigma_L>\lfloor L^2t\rfloor
\right)
\longrightarrow
\mathcal H_{\rm exit}(t),
\]

and

\[
\sqrt{\log L}\,
\mathbb P\!\left(
\tau_{\rm cov}>\lfloor L^2t\rfloor
\right)
\longrightarrow
\mathcal H_{\rm cov}(t).
\]

Each profile has at most countably many discontinuities, so the convergence holds for Lebesgue-a.e. \(t>0\).

### Corollary 2: exact critical mean constants

There are positive finite constants

\[
C_{\rm exit}^{\rm crit}
=
\frac{1}{2\sqrt\pi}
\int_{\mathbb R}\mathbb E[M_y^{-2}]\,dy
\in(0,\infty)
\]

and

\[
C_{\rm crit}
=
\frac{1}{2\sqrt\pi}
\int_{\mathbb R}\mathbb E[R_y^{-2}]\,dy
\in(0,\infty)
\]

such that

\[
\frac{\sqrt{\log L}}{L^2}\,
\mathbb E\sigma_L
\longrightarrow
C_{\rm exit}^{\rm crit}
\]

and

\[
\frac{\sqrt{\log L}}{L^2}\,
\mathbb E\tau_{\rm cov}
\longrightarrow
C_{\rm crit}.
\]

Thus Qin's Question 1 has an affirmative answer.

Since \(0\) belongs to the closure of the range of \(X^{(y)}\),

\[
M_y\le R_y\le2M_y,
\]

and consequently

\[
\frac14\,C_{\rm exit}^{\rm crit}
\le C_{\rm crit}
\le C_{\rm exit}^{\rm crit}.
\]

No closed form for either Brownian integral is asserted.

## Brownian rare-path lemma

The main new ingredient is an exact version of the Brownian tube estimate used for the order bound.

For \(H>0\), let \(W_s=x_H+B_s\), \(0\le s\le H\), where
\(x_H=o(\sqrt H)\). Reverse time and exponentially damp the path:

\[
D_H(u)=e^{-u/2}W_{H-u},
\qquad 0\le u\le H.
\]

For \(u>H\), extend it continuously by

\[
D_H(u)=e^{-u/2}x_H.
\]

Let \(J_\infty(f)=\sup_{u\ge0}|f(u)|\), and let

\[
J_{\rm osc}(f)
=
\sup_{u\ge0}f(u)-\inf_{u\ge0}f(u).
\]

For \(J\in\{J_\infty,J_{\rm osc}\}\), put

\[
I_J(r)
=
\int_{\mathbb R}
\mathbb P\!\left(J(X^{(y)})<r\right)\,dy.
\]

### Lemma 3

If \(r>0\) is a continuity point of \(I_J\), then

\[
\sqrt H\,
\mathbb P\!\left(J(D_H)<r\right)
\longrightarrow
\frac{1}{\sqrt{2\pi}}\,I_J(r).
\]

The convergence is uniform over starting points satisfying
\(|x_H|\le r_H\) for any deterministic \(r_H=o(\sqrt H)\).

### Proof

Condition on the terminal value \(W_H=y\). Its density is

\[
p_H(x_H,y)
=
\frac{1}{\sqrt{2\pi H}}
\exp\!\left(-\frac{(y-x_H)^2}{2H}\right).
\]

If \(J(D_H)<r\), then the values \(D_H(0)=y\) and
\(D_H(H)=e^{-H/2}x_H\) differ by less than \(r\) in the oscillation case, and
\(|y|<r\) in the supremum case. Hence only a fixed compact set of \(y\)'s contributes, up to a vanishing enlargement.

Conditional on \(W_H=y\), the reversed path has the Brownian-bridge representation

\[
W_{H-u}
=
y+\frac{u}{H}(x_H-y)+\beta_u^{(H)},
\qquad 0\le u\le H,
\]

where \(\beta^{(H)}\) is a Brownian bridge from \(0\) to \(0\) of duration \(H\).
It may be coupled as

\[
\beta_u^{(H)}
\stackrel d=
B_u-\frac{u}{H}B_H.
\]

After multiplication by \(e^{-u/2}\),

\[
\sup_{0\le u\le H}
e^{-u/2}
\left|\frac{u}{H}B_H\right|
\le
\frac{C|B_H|}{H}
\longrightarrow0
\]

in probability. The deterministic bridge drift also vanishes uniformly because

\[
\sup_{u\ge0}
e^{-u/2}\frac{u}{H}|x_H-y|
\le
\frac{C(|x_H|+|y|)}{H}
=o(1).
\]

Finally,

\[
\sup_{u\ge U}e^{-u/2}|B_u|
\longrightarrow0
\]

in probability as \(U\to\infty\), uniformly in the subsequent limit \(H\to\infty\).
Thus the damped reversed bridge converges, uniformly on the half-line, to
\(X^{(y)}\), uniformly for bounded \(y\) and \(|x_H|\le r_H=o(\sqrt H)\).

At the same time,

\[
\sqrt H\,p_H(x_H,y)
\longrightarrow
\frac{1}{\sqrt{2\pi}}
\]

uniformly on the same sets. Integrating the conditional probabilities in \(y\)
and using an \(r-\varepsilon,r+\varepsilon\) sandwich proves the assertion at
continuity points of \(I_J\). \(\square\)

## Transfer from the critical elephant walk

We now use the Brownian embedding already developed in Qin's critical-regime argument.

Set

\[
a_n=\frac{\Gamma(n)}{\Gamma(n+1/2)}
=
n^{-1/2}+O(n^{-1}),
\qquad
M_n=a_n\widetilde S_n.
\]

Fang's embedding, in the form used by Qin, realizes

\[
M_n=B_{T_n}
\]

for a Brownian motion \(B\). If

\[
A_n=\sum_{k=1}^n a_k^2,
\]

then

\[
A_n=\log n+C+O(n^{-1/2}),
\]

and Qin's Lemma 3.9 gives, for every integer \(r\ge1\),

\[
\mathbb E\!\left[
\sup_{\ell\le k\le n}
\left|
(T_k-T_\ell)-(A_k-A_\ell)
\right|^{2r}
\mid\mathcal F^B_{T_\ell}
\right]
\le
C(r)
\left[
\ell^{-r}
+
\left(
\frac{1+|B_{T_\ell}|^2}{\ell}
\right)^{2r}
\right].
\]

Fix \(t>0\) and put

\[
n=\lfloor L^2t\rfloor,
\qquad
h=\log n,
\qquad
\ell=\lceil h^{16}\rceil,
\qquad
H=A_n-A_\ell.
\]

Then

\[
H=\log(n/\ell)+o(1)\sim\log n\sim2\log L.
\]

We record the quantitative approximation needed below.

### Lemma 4

Let

\[
W_s=B_{T_\ell+s},\qquad s\ge0,
\]

and for \(\ell\le k\le n\) set

\[
u_k=H-(A_k-A_\ell)=A_n-A_k.
\]

There are events \(G_L\) such that

\[
\mathbb P(G_L^c)=o(H^{-1/2})
\]

and, on \(G_L\),

\[
\sup_{\ell\le k\le n}
\left|
\frac{\widetilde S_k}{L}
-
\sqrt t\,e^{-u_k/2}W_{H-u_k}
\right|
=o(1).
\]

Moreover the mesh of \(\{u_k:\ell\le k\le n\}\) tends to zero fast enough that, for \(J=J_\infty\) or \(J_{\rm osc}\),

\[
J\!\left(
\left(\frac{\widetilde S_k}{L}\right)_{0\le k\le n}
\right)
-
\sqrt t\,J(D_H)
\longrightarrow0
\]

on \(G_L\), where \(D_H\) is the damped reversed Brownian path of Lemma 3 with starting point \(x_H=M_\ell\).

Here \(J\) applied to the discrete walk means respectively the running absolute maximum or the running range.

### Proof

The estimates are included to make clear that the approximation error is negligible on the rare-event scale \(H^{-1/2}\), rather than merely \(o(1)\).

The critical concentration estimate gives

\[
\mathbb P\!\left(|M_\ell|>H^{1/4}\right)
\le
C\exp\!\left(
-\frac{cH^{1/2}}{\log\ell}
\right)
=
o(H^{-1/2}).
\]

On \(|M_\ell|\le H^{1/4}\), Lemma 3.9 with \(r=1\), followed by Markov's inequality, gives

\[
\mathbb P\!\left(
\sup_{\ell\le k\le n}
|(T_k-T_\ell)-(A_k-A_\ell)|
>H^{-4}
\;\middle|\;
\mathcal F^B_{T_\ell}
\right)
=
O(H^{-8}).
\]

A standard Brownian reflection/modulus estimate gives, uniformly for
\(|M_\ell|\le H^{1/4}\),

\[
\mathbb P\!\left(
\sup_{\substack{0\le r,s\le H+1\\|r-s|\le H^{-4}}}
|W_r-W_s|>H^{-1}
\right)
=o(H^{-1/2}),
\]

and

\[
\mathbb P\!\left(
\sup_{0\le s\le H+1}|W_s|>H^2
\right)
=o(H^{-1/2}).
\]

The deterministic asymptotics for \(a_k\) and \(A_n-A_k\) imply, uniformly for \(k\ge\ell\),

\[
\frac{1}{La_k}
=
\sqrt t\,e^{-u_k/2}
\left(1+O(\ell^{-1/2})+o(1)\right).
\]

Therefore the clock replacement and the coefficient replacement together change
the scaled path by \(o(1)\), outside an event of probability \(o(H^{-1/2})\).

Also,

\[
u_k-u_{k+1}=a_{k+1}^2=O(\ell^{-1}),
\]

so the deterministic reversed-time grid has mesh \(O(h^{-16})\).
The same Brownian modulus estimate shows that replacing the grid extrema by
continuous extrema changes \(J\) by \(o(1)\), again outside an event of probability
\(o(H^{-1/2})\).

Finally, before time \(\ell\),

\[
\max_{k<\ell}\frac{|\widetilde S_k|}{L}
\le
\frac{\ell}{L}
=o(1),
\]

so the omitted early segment changes neither the limiting supremum nor the limiting
range. \(\square\)

## Proof of Theorem 1

For the exit time,

\[
\{\sigma_L>n\}
=
\left\{
\max_{0\le k\le n}\frac{|\widetilde S_k|}{L}<1
\right\}.
\]

Lemma 4 and an \(\varepsilon\)-sandwich therefore reduce its probability, up to
\(o(H^{-1/2})\), to

\[
\mathbb P\!\left(
J_\infty(D_H)<t^{-1/2}
\right).
\]

For the cover time,

\[
\{\tau_{\rm cov}>n\}
=
\left\{
\max_{k\le n}\widetilde S_k-\min_{k\le n}\widetilde S_k<L-1
\right\},
\]

so the same argument reduces it to

\[
\mathbb P\!\left(
J_{\rm osc}(D_H)<t^{-1/2}
\right),
\]

the difference between \(1-1/L\) and \(1\) being negligible.

The Brownian starting point in these applications is \(x_H=M_\ell\).
The concentration estimate in Lemma 4 restricts it, with error \(o(H^{-1/2})\),
to \(|x_H|\le H^{1/4}=o(\sqrt H)\), exactly the uniform regime of Lemma 3.
Consequently, at continuity points,

\[
\sqrt H\,\mathbb P(\sigma_L>n)
\longrightarrow
\frac{1}{\sqrt{2\pi}}
\int_{\mathbb R}
\mathbb P(M_y<t^{-1/2})\,dy,
\]

and

\[
\sqrt H\,\mathbb P(\tau_{\rm cov}>n)
\longrightarrow
\frac{1}{\sqrt{2\pi}}
\int_{\mathbb R}
\mathbb P(R_y<t^{-1/2})\,dy.
\]

Since \(H\sim2\log L\),

\[
\frac{\sqrt{\log L}}{\sqrt H}\longrightarrow\frac{1}{\sqrt2}.
\]

Multiplying the last two displays by this factor produces
\(1/(2\sqrt\pi)\), proving Theorem 1.

## Proof of Corollary 2

Qin's Proposition 3.5 provides an integrable envelope, uniform in \(L\), for

\[
\sqrt{\log L}\,
\mathbb P(\tau_{\rm cov}>\lfloor L^2t\rfloor)
\]

and for the corresponding exit-time tail. Qin's Corollary 3.6 therefore permits
dominated convergence using the a.e. tail limits of Theorem 1. This proves existence,
finiteness and positivity of both normalized mean limits.

For the alternative formulas, Tonelli's theorem gives, for \(Z>0\),

\[
\int_0^\infty
\mathbf 1_{\{Z<t^{-1/2}\}}\,dt
=
Z^{-2}.
\]

Applying this with \(Z=M_y\) and \(Z=R_y\) yields

\[
C_{\rm exit}^{\rm crit}
=
\frac{1}{2\sqrt\pi}
\int_{\mathbb R}\mathbb E[M_y^{-2}]\,dy
\]

and

\[
C_{\rm crit}
=
\frac{1}{2\sqrt\pi}
\int_{\mathbb R}\mathbb E[R_y^{-2}]\,dy.
\]

The inequalities between the constants follow from
\(M_y\le R_y\le2M_y\).

## Context and originality

The September 2026 preprint of Qin proves only the order

\[
\mathbb E\tau_{\rm cov}
=
\Theta(L^2/\sqrt{\log L})
\]

at \(p=3/4\), and poses the existence of the exact normalized mean constant as
Question 1. It also observes that an a.e. limit for the rescaled \(L^2\)-time tail
would settle the question. Its critical lower bound uses a Brownian embedding and
a two-sided estimate of order \(H^{-1/2}\) for an expanding Brownian tube.

The present result identifies that missing tail limit. The distinction from the
usual critical fluctuation limit is important: Qin proves

\[
\tau_{\rm cov}\log L/L^2
\Longrightarrow
(2B_1^2)^{-1},
\]

whose limit has infinite mean. The exact expectation is instead governed by much
rarer trajectories living on the longer \(L^2\) scale. Their asymptotic law is the
endpoint mixture of a reversed Brownian bridge, which produces the
\(X^{(y)}\) profile above.

André and Zuaznábar study symmetric-interval escape times and obtain exact mean
asymptotics in the diffusive regime together with exponential tail bounds; their
stated exact-mean theorem does not cover the critical parameter. Fang studies
critical returns to the origin and provides Brownian-embedding tools, not the
critical cover-time or exit-time constant.

Searches for the critical mean cover-time constant, the critical exact exit-time
constant, and equivalent Brownian-profile formulations did not locate a prior
solution. The claim of originality is therefore to the best of our knowledge.
The Brownian-bridge disintegration itself uses standard probability theory; the
claimed contribution is its rare-event asymptotic, its quantitative transfer
through the critical ERW embedding, and the resulting solution of the explicit
cover-time question.

## Limitations

- The theorem concerns the classical one-dimensional elephant random walk exactly at \(p=3/4\).
- The constants are represented by Brownian path integrals; no closed form or certified numerical value is provided.
- Tail convergence is stated at continuity points of the profile, which is sufficient for the mean asymptotic. No claim is made here that every positive radius is a continuity point.
- The proof uses Qin's critical concentration, uniform-integrability, and Brownian-clock estimates, together with the Brownian embedding attributed there to Fang.
- No second-order correction, convergence rate for the mean, or joint critical limit for other path statistics is claimed.

## References

1. Shuo Qin, *Cover times and ranges of elephant random walks*, arXiv:2609.17264v1 (2026). https://arxiv.org/abs/2609.17264
2. Morgan André and Leonel Zuaznábar, *Estimates on Escape Times for the Elephant Random Walk*, arXiv:2602.18953 (2026). https://arxiv.org/abs/2602.18953
3. Zheng Fang, *How often does a critical elephant random walk return to origin*, Electronic Communications in Probability 29 (2024), DOI 10.1214/24-ECP636. https://doi.org/10.1214/24-ECP636
4. Cristian F. Coletti, Renato Gava and Gunter M. Schütz, *A strong invariance principle for the elephant random walk*, arXiv:1707.06905 (2017). https://arxiv.org/abs/1707.06905
