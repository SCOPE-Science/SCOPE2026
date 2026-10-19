# Spatial covariance reversal for Brownian span and point local time

## Finding

Let \(B=(B_s)_{s\ge0}\) be standard one-dimensional Brownian motion with \(B_0=0\). Define the span \(R_t=\sup_{0\le s\le t}B_s-\inf_{0\le s\le t}B_s\), and let \(L_t^x\) be local time normalized by the occupation-density identity \(\int_0^t g(B_s)\,ds=\int_{\mathbb R}g(x)L_t^x\,dx\). Define \(\varphi(u)=(2\pi)^{-1/2}e^{-u^2/2}\), \(Q(u)=\int_u^\infty\varphi(v)\,dv\), and for \(t>0\), \(a\ge0\),
\[
f_t(a)=2\sqrt t\,[\varphi(a/\sqrt t)-(a/\sqrt t)Q(a/\sqrt t)],\qquad
h_t(a)=2t\,[(1+a^2/t)Q(a/\sqrt t)-(a/\sqrt t)\varphi(a/\sqrt t)].
\]
For **every** \(t>0\) and \(x\in\mathbb R\), with \(a=|x|\),
\[
\boxed{\operatorname{Cov}(R_t,L_t^x)=\left(a-\sqrt{\frac{8t}{\pi}}\right)f_t(a)+\frac56h_t(a)+\frac13h_t(2a).}
\tag{1}
\]
The functions are strictly positive for finite \(a\ge0\). In particular,
\[
\boxed{\operatorname{Cov}(R_t,L_t^0)=t\left(\frac76-\frac4\pi\right)<0,\qquad
\operatorname{Cov}(R_t,L_t^x)>0\quad\text{if }|x|\ge\sqrt{8t/\pi}.}
\tag{2}
\]
The continuous, even covariance field consequently has **at least one** zero on each half-line and changes from negative near zero to positive sufficiently far from zero. Uniqueness of the zero is neither claimed nor needed. Brownian scaling makes the transition depend only on the dimensionless distance \(|x|/\sqrt t\).

## Assumptions and scope

All times are deterministic and strictly positive. The Brownian variance parameter is one, so \(\mathbb E B_t^2=t\). Local time uses the occupation-density normalization, not twice this local time or the normalization of an alternative diffusion generator. Statements hold for all deterministic real spatial levels. The formula is an exact finite-time identity, not a large-time expansion. For \(x=0\), no convention for a positive/negative sign is required.

## Proof

**1. Two elementary transforms.** For \(a\ge0\), let \(\tau_a=\inf\{s\ge0:B_s=a\}\). The reflection principle and the heat kernel give
\[
f_t(a)=\mathbb E L_t^a=\int_0^t \frac{e^{-a^2/(2s)}}{\sqrt{2\pi s}}\,ds,
\qquad h_t(a)=\int_0^t\mathbb P(\tau_a\le s)\,ds
=\int_0^t 2Q(a/\sqrt s)\,ds.
\tag{3}
\]
Direct Gaussian integration yields the closed forms preceding (1). Fix \(\lambda>0\) and set \(\kappa=\sqrt{2\lambda}\). For these functions,
\[
\int_0^\infty e^{-\lambda t}f_t(a)\,dt=\frac{e^{-\kappa a}}{\lambda\kappa},\qquad
\int_0^\infty e^{-\lambda t}h_t(a)\,dt=\frac{e^{-\kappa a}}{\lambda^2}.
\tag{4}
\]
Both follow by Tonelli and the Brownian first-hitting transform \(\mathbb E e^{-\lambda\tau_a}=e^{-\kappa a}\).

**2. The maximum/local-time mixed transform.** Put \(M_t=\sup_{s\le t}B_s\). For \(a>0\), \(\{M_t\ge a\}=\{\tau_a\le t\}\), so \(M_t=\int_0^\infty\mathbf1\{\tau_a\le t\}\,da\). The unrestricted resolvent and the resolvent killed at \(a\), for \(x<a\), are
\[
G_\lambda(u,v)=\frac{e^{-\kappa|u-v|}}\kappa,\qquad
G_\lambda^{(<a)}(0,x)=\frac{e^{-\kappa|x|}-e^{-\kappa(2a-x)}}\kappa.
\tag{5}
\]
For \(x<a\), split the local-time increments according to whether they occur before or after \(\tau_a\). A pre-hit increment at spatial point \(x\) receives the future hitting factor \(\mathbb E_xe^{-\lambda\tau_a}=e^{-\kappa(a-x)}\); after hitting, start afresh from \(a\). Hence Tonelli and the strong Markov property imply
\[
\int_0^\infty e^{-\lambda t}\mathbb E[L_t^x\mathbf1\{\tau_a\le t\}]\,dt
=\frac{G_\lambda^{(<a)}(0,x)e^{-\kappa(a-x)}+e^{-\kappa a}G_\lambda(a,x)}{\lambda}.
\tag{6}
\]
For \(x\ge a\), any path accumulating local time at \(x\) must already have hit \(a\), and the corresponding transform equals \(G_\lambda(0,x)/\lambda\). Integrate (6) over \(a>0\), using the two branches \(x\ge0\) and \(x<0\), to obtain
\[
\int_0^\infty e^{-\lambda t}\mathbb E[M_tL_t^x]dt=
\begin{cases}
\displaystyle e^{-\kappa x}\left[\frac{x}{\lambda\kappa}+\frac7{6\lambda\kappa^2}\right],&x\ge0,\\[3pt]
\displaystyle\frac{\frac12e^{-\kappa|x|}+\frac23e^{-2\kappa|x|}}{\lambda\kappa^2},&x<0.
\end{cases}
\tag{7}
\]
For example, if \(x\ge0\), the integral from \(0\) to \(x\) contributes \(xe^{-\kappa x}/(\lambda\kappa)\); from \(x\) to infinity the three exponential integrals have coefficients \(1\), \(1/2\), and \(-1/3\), summing to \(7/6\). If \(x<0\), the pre-hit difference gives \((1-1/3)e^{-2\kappa|x|}\), while the post-hit contribution gives \(e^{-\kappa|x|}/2\).

**3. Inversion and reflection.** Since \(\kappa^2=2\lambda\), inversion using (4) gives
\[
\mathbb E[M_tL_t^x]=
\begin{cases}
\displaystyle x f_t(x)+\frac7{12}h_t(x),&x\ge0,\\[2pt]
\displaystyle\frac14h_t(|x|)+\frac13h_t(2|x|),&x<0.
\end{cases}
\tag{8}
\]
Uniqueness of Laplace transforms justifies (8) for every \(t>0\); continuity in time removes any exceptional time set. Brownian sign symmetry yields \(\mathbb E[(-\inf_{s\le t}B_s)L_t^x]=\mathbb E[M_tL_t^{-x}]\). Add the two branches in (8), and use \(\mathbb E R_t=\sqrt{8t/\pi}\) and \(\mathbb E L_t^x=f_t(|x|)\). This proves (1).

**4. Sign structure and conservation.** At \(a=0\), \(h_t(0)=t\) and \(f_t(0)=\sqrt{2t/\pi}\), yielding \(t(7/6-4/\pi)<0\). For \(a\ge\sqrt{8t/\pi}\), every term in (1) is nonnegative and the \(h\)-terms are strictly positive. The right side is continuous and even in \(x\), proving at least one spatial sign reversal on each half-line. Lastly, Tonelli and \(\int_\mathbb R L_t^x\,dx=t\) show the consistency identity
\[
\int_{\mathbb R}\operatorname{Cov}(R_t,L_t^x)\,dx
=\operatorname{Cov}\left(R_t,\int_{\mathbb R}L_t^x\,dx\right)=0.
\tag{9}
\]
No inference of uniqueness is made from (9).

## Verification

A standalone standard-library script `verify.py` independently computes \(f_t\) via heat-kernel quadrature and \(h_t\) via the first-passage tail, compares a separate time-Laplace numerical integral against (7), and checks the origin value, deterministic positive regime, Brownian scaling, and integral cancellation. Execute `python verify.py`. There are 60 numerical assertions; they are finite consistency checks, not a proof of an identity for all parameters. A separate Brownian-increment simulation was compared qualitatively with the covariance profile, using a finite band approximation for local time; this is not used in the proof.

## Relationship to prior work

Pitman's 1998 technical report gives the joint law of Brownian local time at a fixed level and the *endpoint* of Brownian motion (and related Brownian-bridge conditional distributions), not the covariance of point local time with the entire path span. Mörters and Peres develop the occupation-density, Lévy identity, reflection principle, and Ray–Knight local-time theory used here as background, without an explicit spatial span/local-time covariance profile in the inspected sections. Cox, Hobson, and Obłój analyze inequalities for local time at zero and a **local martingale**, with stopping and embedding objectives; the symbol they use for that martingale does not denote the running maximum. The origin value is consistent with a previously obtained simple-walk maximum/return covariance under diffusive scaling; the spatial formula and forced far-field positivity require a different calculation. The identity here combines a first-hitting/local-time resolvent split with reflection in space.

## Limitations

This is an exact first mixed moment and sign-separation theorem, **not** a joint distribution of the entire local-time field and span. Existence, not uniqueness, of a spatial covariance zero is proved. The theorem assumes zero drift, standard Brownian scaling, and deterministic observation time; extension to drift or different processes has not been established. The specific historical priority of the full spatial profile has not received independent verification; classic broader Brownian local-time literature may contain implicit formulas.

## References

1. J. Pitman, *The distribution of local times of a Brownian bridge*, Berkeley Statistics Technical Report 539 (dated November 3, 1998), https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/539.pdf .
2. P. Mörters and Y. Peres, *Brownian Motion*, Cambridge University Press (2010), Chapters 3 and 6, https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf .
3. A. M. G. Cox, D. Hobson, and J. Obłój, *Pathwise inequalities for local time: Applications to Skorokhod embeddings and optimal stopping*, Annals of Applied Probability **18** (2008), 1870–1896, https://doi.org/10.1214/07-AAP507 .
