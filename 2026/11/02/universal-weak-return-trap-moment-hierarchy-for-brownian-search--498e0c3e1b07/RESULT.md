# Universal weak-return-trap moment hierarchy for Brownian search with stochastic returns

## Finding

For the one-dimensional Brownian-search / Ornstein–Uhlenbeck-return process defined below, with **any fixed positive search-interruption rate** \(r>0\), the complete physical completion time \(T_{r,k}\) has the following sharp weak-trap moment law for **every integer** \(n\geq 1\):

\[
\boxed{\lim_{k\downarrow0}k^{n-1/2}\mathbb{E}[T_{r,k}^{n}]=c_n,
\qquad c_n=n\sqrt{\frac{2}{\pi}}\int_0^{\pi/2}
\bigl(\log\sec\theta\bigr)^{n-1}\,d\theta.}
\]

In particular, the mean and variance obey

\[
\mathbb E T_{r,k}\sim\sqrt{\frac\pi2}\,k^{-1/2},\qquad
\operatorname{Var}(T_{r,k})\sim\sqrt{2\pi}\log2\,k^{-3/2}.
\]

The coefficient of variation therefore diverges as

\[
\frac{\sqrt{\operatorname{Var}(T_{r,k})}}{\mathbb E T_{r,k}}
\sim\frac{\sqrt{\sqrt{2\pi}\log2}}{\sqrt{\pi/2}}\,k^{-1/4}.
\]

**Every leading constant is independent of \(r\)**, although the number of search attempts and success probability of a single attempt depend on \(r\). At the boundary \(k=0\), the concatenated trajectory is ordinary Brownian motion stopped at its first arrival at the target, and its completion time has infinite mean; the positive-stiffness limit is singular.

## Assumptions and scope

Fix any \(r\in(0,\infty)\) and return stiffness \(k\in(0,\infty)\). The particle begins at \(0\) in *search mode*, with generator \(\partial_x^2\) on \(( -\infty,1)\) and absorbing target \(1\). A rate-\(r\) exponential clock interrupts only the search mode. If absorption has not occurred, the particle stays at its current position and enters *return mode*, with generator \(\partial_x^2-kx\partial_x\). Return mode ends on the first visit to \(0\) (a new independent search begins) or to \(1\) (successful absorption). No resetting clock operates during return. Motion is continuous; Brownian noise for successive modes and cycles is independent conditional on the switching point, and every newly started search uses a fresh exponential clock.

The total time to first absorption at \(1\), **including all return durations**, is \(T_{r,k}\). All expectations include both trajectories and switching clocks. The limit \(k\downarrow0\) is taken with \(r>0\) fixed and the target distance and diffusivity fixed by the above normalization. Claims of uniformity as \(r\downarrow0\) or \(r\to\infty\) are not made.

## Proof

**1. Search endpoint measure and renewal balance.** Write \(a=\sqrt r\), let \(B_t\) be Brownian motion with generator \(\partial_x^2\) started at \(0\), \(\tau_1=\inf\{t:B_t=1\}\), and let \(R\sim\operatorname{Exp}(r)\) be independent. Standard killed resolvent / reflection gives the joint density for the interruption location on \(\{R<\tau_1\}\):

\[
\rho_r(x)=\frac a2\left(e^{-a|x|}-e^{-a(2-x)}\right),\quad x<1,
\qquad q_r=\mathbb P(\tau_1<R)=e^{-a}.
\]

The first *cycle* lasts \(C=\min(\tau_1,R)+\boldsymbol1_{\{R<\tau_1\}}\tau_{\mathrm{return}}(B_R)\); it succeeds if the target is met during search or return. On a positive return starting at \(0<x<1\), the target-before-origin probability is

\[
h_k(x)=\frac{\int_0^x e^{k u^2/2}\,du}{\int_0^1e^{k u^2/2}\,du}.
\]

A negative return always reaches \(0\) before it can reach \(1\). Thus the cycle success probability is

\[
p_k=q_r+\int_0^1 \rho_r(x)h_k(x)\,dx
\longrightarrow p_0=q_r+\int_0^1x\rho_r(x)\,dx.
\]

Optional stopping for \(B_{t\wedge\tau_1\wedge R}\) (finite mean stopped time) yields \(q_r+\int_{-\infty}^{1}x\rho_r(x)\,dx=0\). It follows that

\[
p_0=H_r:=\int_{-\infty}^{0}(-x)\rho_r(x)\,dx
=\frac{1-e^{-2a}}{2a}>0.
\]

This identity is the cancellation that removes all \(r\)-dependence from the leading completion-time moment coefficients.

**2. Exact weak-stiffness return law.** On the negative half-line, set the positive initial distance \(y=-x>0\). Let \(Y_t\) solve \(dY_t=-kY_t\,dt+\sqrt2\,dW_t\), \(Y_0=y\), stopped on hitting \(0\). Multiplying by \(e^{kt}\) and applying Brownian time change gives the *exact distributional identity*

\[
\tau_k(y)\overset{d}=\frac1{2k}\log\left(1+\frac{k y^2}{Z^2}\right),
\qquad Z\sim N(0,1).
\]

Indeed, \(e^{kt}Y_t\) has quadratic variation \((e^{2kt}-1)/k\), while standard Brownian motion started at \(y\) hits \(0\) at a time distributed as \(y^2/Z^2\).

For each integer \(n\ge1\), substitute \(|Z|=\sqrt{k}\,y t\) in its half-normal integral. One obtains

\[
k^{n-1/2}\mathbb E[\tau_k(y)^n]
=\frac{\sqrt{2/\pi}}{2^n}\,y\int_0^\infty
 e^{-ky^2t^2/2}\bigl[\log(1+t^{-2})\bigr]^n\,dt.
\]

The integral without the exponential is finite: near \(0\) it grows only as a power of \(|\log t|\), and at infinity it decays as \(t^{-2n}\). Dominated convergence therefore proves, *for every* \(y>0\),

\[
k^{n-1/2}\mathbb E[\tau_k(y)^n]\longrightarrow c_n y,
\qquad 0\le k^{n-1/2}\mathbb E[\tau_k(y)^n]\le c_n y,
\]

with \(c_n=2^{-n}\sqrt{2/\pi}\int_0^\infty[\log(1+t^{-2})]^n\,dt\). Inverting \(t\), integrating by parts, and substituting \(u=\tan\theta\) gives

\[
\int_0^\infty[\log(1+t^{-2})]^n\,dt
=2^n n\int_0^{\pi/2}(\log\sec\theta)^{n-1}\,d\theta.
\]

**3. Cycle moment asymptotics.** Define \(A_k=\boldsymbol1_{\{R<\tau_1,B_R<0\}}\tau_k(-B_R)\), and let \(B_k=C-A_k\). Then \(A_k,B_k\ge0\). The search portion of \(B_k\) is bounded by \(R\), which has moments of every order. Its return portion can only be a diffusion in the compact interval \([0,1]\) killed at the endpoints; for \(0<k\le1\), uniform ellipticity and bounded drift give uniformly bounded exit-time moments of every order. Hence \(\sup_{0<k\le1}\mathbb E B_k^n<\infty\) for each \(n\).

By the interruption density, the preceding domination and \(H_r<\infty\),

\[
\lim_{k\downarrow0}k^{n-1/2}\mathbb E A_k^n
=\int_{-\infty}^0c_n(-x)\rho_r(x)\,dx=H_r c_n.
\]

Since \(\|B_k\|_{L^n}\) is bounded while \(\|A_k\|_{L^n}\to\infty\), the triangle inequality in \(L^n\) gives

\[
\mathbb E C^n\sim H_r c_n k^{-(n-1/2)}.
\]

**4. Full-time renewal moments.** Let \(F\) indicate cycle failure (return to the origin), and let \(T'_{r,k}\) be an independent copy of the full completion time. The regenerative identity is \(T_{r,k}\overset d=C+F T'_{r,k}\). All full moments are finite for every \(k>0\), since \(p_k>0\), the geometric number of cycles has moments of all orders, and each cycle has moments of all orders. Write \(M_n=\mathbb E T_{r,k}^{n}\). The binomial expansion gives exactly

\[
p_kM_n=\mathbb E C^n
+\sum_{j=1}^{n-1}\binom nj
\mathbb E\left[C^{n-j}F\right]M_j.
\]

Inducting from \(n=1\), the first term has order \(k^{-(n-1/2)}\), while the \(j\)th remainder has at most order \(k^{-(n-j-1/2)}k^{-(j-1/2)}=k^{-(n-1)}\), a lower order. Using \(p_k\to H_r\), we obtain \(k^{n-1/2}M_n\to c_n\) for all \(n\ge1\). Finally, \(\int_0^{\pi/2}\log\sec\theta\,d\theta=(\pi/2)\log2\) gives \(c_1=\sqrt{\pi/2}\) and \(c_2=\sqrt{2\pi}\log2\). Because \((\mathbb E T)^2=O(k^{-1})\), subtracting it does not affect the leading \(k^{-3/2}\) variance. This proves the claim.

At \(k=0\), the two modes have identical Brownian generators and a change of mode never changes position. Concatenating at stopping times gives ordinary Brownian motion started at \(0\), killed at \(1\), with Laplace transform \(\mathbb E e^{-s T_{r,0}}=e^{-\sqrt s}\); this distribution has infinite mean.

## Verification

A standalone deterministic numerical checker in `verify.py` independently evaluates the killed-resolvent balance \(p_0=H_r\), the exact finite-\(k\) renewal formula for the mean, and the scaled negative-return moments for orders one, two, and three using Gaussian–Laguerre quadrature. It tests several fixed interruption rates and decreasing stiffnesses. These are finite checks of the formulas and scale convergence, not proofs of the full moment theorem. Run with Python 3.10+, NumPy and SciPy: `python verify.py`.

## Relationship to prior work

Dubey and Pal, arXiv:2610.18814v1, introduce the switching-harmonic first-passage model and derive the **mean** completion time, including the freely diffusing search limit. Frydel, arXiv:2511.14646v1, independently derives related exact **mean** formulas for its target-visible SR-B protocol and the stochastic harmonic-return law. The renewal decomposition and return-first-passage methods are credited to those works. The present result is specifically the *joint weak-trap, all-integer-moment asymptotic hierarchy*, the exact \(r\)-independent leading constants, and the variance / coefficient-of-variation singularity. In particular, an existing formula for the first moment alone is not claimed as original. The OU hitting-time distribution itself is standard; its integral is used as an input, not presented as a new general diffusion identity.

The earlier linear-return work of Biswas and collaborators (arXiv:2406.08975v1) concerns a distinct return force and primarily mean efficiency. Standard work on OU exit-time transforms, including Grebenkov's review, supplies related first-passage background but not this two-mode renewal asymptotic statement.

## Limitations

The theorem is for strictly positive fixed \(r\), a freely diffusing search, the same diffusion coefficient in both modes, a harmonic return stopped *exactly* at \(0\) or \(1\), and integer moments. No jointly varying \(r,k\) regime is analyzed. It does not establish weak convergence of rescaled completion-time laws or a complete distributional tail limit. Published mean-return formulas provide significant prior coverage of the model; an unlocated broader moment theorem or a derivation from a general renewal theorem remains a possible publication-priority risk. Numerical quadrature is not infinite-domain proof, and no independent mathematical or publication-priority audit has been performed.

## References

1. A. Dubey and A. Pal, “Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols,” arXiv:2610.18814v1 (first publicly posted 2026-10-13). https://arxiv.org/html/2610.18814v1
2. D. Frydel, “Search by Return: Stochastic Resetting in Fluctuating Harmonic Potentials,” arXiv:2511.14646v1 (first publicly posted 2025-11-18), especially §III.4 (SR-B). https://arxiv.org/html/2511.14646v1
3. A. Biswas et al., “Drift-diffusive resetting search process with stochastic returns,” arXiv:2406.08975v1 (2024). https://arxiv.org/html/2406.08975v1
4. D. S. Grebenkov, “First exit times of harmonically trapped particles: a didactic review,” *J. Phys. A* 48 (2015), 013001. https://doi.org/10.1088/1751-8113/48/1/013001
