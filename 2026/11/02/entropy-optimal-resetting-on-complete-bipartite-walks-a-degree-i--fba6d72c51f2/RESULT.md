# Entropy-optimal resetting on complete bipartite walks: a degree-imbalance crossover

## Finding
Let \(K_{m,n}\) have parts \(A\), \(B\) with \(|A|=m\), \(|B|=n\), and let the discrete-time walk reset to one fixed \(o\in A\) with probability \(r\), otherwise taking a uniformly random adjacent edge. For each \(m,n\ge1\), let \(r_{m,n}\) denote **any** global maximizer of its stationary Markov entropy rate \(H_{m,n}(r)\). The exact entropy rate for all \(0\le r\le1\) is
\[
H_{m,n}(r)=\frac{h(r)+(1-r)\log n+(1-r)g_m(r)}{2-r},
\]
where \(h(r)=-r\log r-(1-r)\log(1-r)\) and
\[
g_m(r)=-a\log a-(m-1)b\log b,\qquad a=r+\frac{1-r}{m},\quad b=\frac{1-r}{m}.
\]
Terms \(0\log0\) are zero. All logarithms are natural. The two asymptotic regimes are:

**(I) Fixed opposite part.** For each fixed integer \(n\ge1\), as \(m\to\infty\),
\[
r_{m,n}\sim (m^3n)^{-1/4},\qquad
\max_{0\le r\le1}H_{m,n}(r)-\frac12\log(mn)\sim(m^3n)^{-1/4}.
\]

**(II) Proportional parts.** If \(m,n\to\infty\) and \(n/m\to\rho\in(0,\infty)\), let
\[
t_\rho=\frac{\sqrt{1+4/\sqrt\rho}-1}{2}.
\]
Then every selection of global maximizers obeys
\[
m r_{m,n}\longrightarrow t_\rho,\qquad
m\left[\max_{0\le r\le1}H_{m,n}(r)-\frac12\log(mn)\right]\longrightarrow
 t_\rho-\frac12\log(1+t_\rho).
\]
Thus a fixed opposite part induces \(m^{-3/4}\)-order optimal resetting, whereas proportional communities induce \(m^{-1}\)-order resetting with a nontrivial universal ratio-dependent coefficient.

## Assumptions and scope
The graph is the undirected simple complete bipartite graph with \(m,n\ge1\). At each integer step a **single** transition is made, with a Bernoulli reset of probability \(r\) to the distinguished vertex \(o\in A\), or with the complementary probability an ordinary simple-random-walk step. Reset and ordinary transition probabilities to the same destination must be **added before** calculating the entropy of the observed state transition. The entropy rate is \(-\sum_i\pi_i\sum_jP_{ij}\log P_{ij}\) for the unique stationary distribution at \(0<r<1\); the endpoints are defined by the same exact formula and by continuity. No uniqueness of a finite-size maximizing \(r\) is assumed. The first limit holds for each fixed \(n\), including \(n=1\); the second requires \(0<\rho<\infty\).

## Proof
**1. Stationary law and entropy.** Write \(q=1-r\). The total stationary mass of \(A\) is \(1/(2-r)\), since the class transition probabilities are \(P(A,B)=q\) and \(P(B,A)=1\). The mass of \(B\) is \(q/(2-r)\), uniformly distributed over its \(n\) vertices. Among \(A\), every vertex receives an ordinary inflow \(q^2/[m(2-r)]\), while \(o\) receives the additional resetting inflow \(r\); hence
\[
\pi_o=r+\frac{q^2}{m(2-r)},\quad \pi_i=\frac{q^2}{m(2-r)}\ (i\in A\setminus\{o\}),\quad \pi_j=\frac{q}{n(2-r)}\ (j\in B).
\]
A row out of \(A\) has entropy \(h(r)+q\log n\), since the reset destination lies in \(A\) and ordinary destinations in \(B\). A row out of \(B\) has entropy \(g_m(r)\), since the ordinary walk already has probability \(q/m\) of landing at \(o\), in addition to resetting. The displayed formula follows from weighting these row entropies by the stationary class masses. It gives \(H_{m,n}(0)=\tfrac12\log(mn)\) and \(H_{m,n}(1)=0\). As \(r\downarrow0\) for finite \(m,n\), its gain is \(\tfrac12 r\log(1/r)+O(r)\), so the maximum is attained in the interior.

**2. A global entropy envelope.** Let \(Z\) be the hidden indicator of whether a step out of \(B\) was a reset. Its joint entropy with the chosen destination is \(h(r)+q\log m\), hence
\[
0\le d_m(r):=h(r)+q\log m-g_m(r)=a\,h(r/a)
\le\frac{q}{m}\log\left(\frac{e m a}{q}\right)
\]
for \(0\le r<1\), with the endpoint interpreted continuously. The inequality follows from \(h(x)\le x\log(e/x)\) applied to \(x=(q/m)/a\). Consequently \(H\le U\), where
\[
U_{m,n}(r):=h(r)+\frac{q}{2-r}\log n+\frac{q^2}{2-r}\log m,
\qquad U-H=\frac{q}{2-r}d_m(r).
\]
In particular,
\[
U_{m,n}(r)-\frac12\log(mn)
=h(r)-\frac{r}{2(2-r)}\log n-\frac{r(3-2r)}{2(2-r)}\log m.
\]
The derivative, used for localization, is
\[
U'_{m,n}(r)=\log\frac{1-r}{r}-\frac{\log n+(1-r)(3-r)\log m}{(2-r)^2}.
\]

**3. Fixed \(n\), unbalanced limit.** Put \(s=(m^3 n)^{-1/4}\). For every compact \(t\)-interval in \([0,\infty)\), the expansion \(h(ts)=ts[1-\log(ts)]+O(s^2)\) gives, uniformly,
\[
\frac{U_{m,n}(ts)-\tfrac12\log(mn)}s\longrightarrow t(1-\log t),
\]
with \(t\log t=0\) at zero. The envelope gap is \(O((\log m)/m)=o(s)\) for \(r=ts\) on such a compact interval. The limiting profile has its strict unique global maximum at \(t=1\), with value \(1\).

For completeness, this compact calculation applies to **global** optimizers: on \(0<r<m^{-1/2}\),
\[
U''_{m,n}(r)=-\frac1{r(1-r)}+\frac{2\log(m/n)}{(2-r)^3}<0
\]
for all sufficiently large \(m\) (with fixed \(n\)). On \(m^{-1/2}\le r\le1/2\), the positive logarithm in \(U'\) is at most \(\tfrac12\log m\), whereas the \(\log m\) coefficient subtracted in \(U'\) is at least \(5/9\); on \(r\ge1/2\), \(U'<0\). Therefore \(U\) is globally unimodal, and its maximizing point lies at \(r/s\to1\). Since \(H\le U\) everywhere and \(H(s)=U(s)-o(s)\), the strict separation of the limiting profile forces **every** optimizer of \(H\) to satisfy \(r/s\to1\), and its maximal gain divided by \(s\) tends to \(1\).

**4. Proportional-parts limit.** Put \(n/m=\rho_m\to\rho\) and \(r=t/m\). For \(t\) in a fixed compact interval, uniformly including \(t=0\), elementary Taylor expansions yield
\[
g_m(t/m)=\log m-\frac{(1+t)\log(1+t)-t}{m}+o(m^{-1}),
\]
and then
\[
m\left[H_{m,n}(t/m)-\tfrac12\log(mn)\right]\longrightarrow
\frac12 f_\rho(t),
\]
where
\[
f_\rho(t)=t\left(1-\log t-\tfrac12\log\rho\right)-[(1+t)\log(1+t)-t].
\]
This is strictly concave for \(t>0\), since \(f'_\rho(t)=-\log[t(1+t)\sqrt\rho]\) and \(f''_\rho(t)=-1/t-1/(1+t)<0\). Its unique maximizer satisfies \(t(1+t)=\rho^{-1/2}\), giving \(t_\rho\) as stated and \(f_\rho(t_\rho)=2t_\rho-\log(1+t_\rho)>0\).

Finally, use the envelope identity again to obtain for all \(r\in(0,1]\),
\[
U_{m,n}(r)-\tfrac12\log(mn)=h(r)-r\log m-\frac{r}{2(2-r)}\log(n/m)
\le r\left[1-\log(mr)+\tfrac12|\log(n/m)|\right].
\]
Since \(\log(n/m)\) is bounded, some fixed \(T>t_\rho\) has \(U_{m,n}(r)<H_{m,n}(0)\) for all \(r\ge T/m\) and sufficiently large \(m\). But \(H_{m,n}(t_\rho/m)>H_{m,n}(0)\) eventually, so all global maximizers belong to \([0,T/m]\). Uniform compact convergence and strict uniqueness of the limit's maximizer yield the asserted convergence of both maximizing rate and gain.

## Verification
The accompanying standalone \(`check_entropy.py`\) uses no external packages. It constructs finite transition matrices and checks stationarity and the exact entropy formula against independent row-by-row evaluation; tests both asymptotic optimizer scalings and maximal gains over several sizes and ratios; and compares each numerically optimized rate against additional rates. It reports \(5633\) passed deterministic assertions. These numerical checks are finite diagnostics, **not** proofs of the limiting statements; the global envelope, localization inequalities, and compact convergence above provide the infinite-dimensional reasoning. Run with \(`python3 check_entropy.py`\).

## Relationship to prior work
Wang and Chen (arXiv:2208.05665, first posted August 11, 2022), Sections II–III, introduce resetting Markov entropy and analyze regular networks, Cayley trees, and Barabási–Albert networks. They do not give the complete-bipartite asymptotic optimizer laws above. Our derivation explicitly accounts for the **overlap** between resetting and ordinary transitions from \(B\) to the root, a distinction necessary for evaluating observed-state transition entropy. Riascos et al. (arXiv:1910.13568) treat stationary probabilities and passage times of resetting walks on networks; those general stationary formulas provide context but do not by themselves state the two entropy-optimal scaling regimes. The present entropy formula follows directly from the Markov chain, while the stated contribution is the sharp and differently scaled **optimization** and its global-maximizer justification. Earlier or less easily discoverable entropy-optimization results may overlap, and priority has not been independently certified.

## Limitations
No finite-size uniqueness of the entropy optimizer is claimed. The asymptotic laws do not cover intermediate scalings with both part sizes growing but \(n/m\to0\), nor do they cover nonuniform neighboring steps, a reset distributed across vertices, or multiple reset targets. The result is a self-review, not an independent audit. The quantitative checker covers finite examples only. No inference about entropy-maximizing walks outside this specified reset family is made.

## References
1. Y. Wang and H. Chen, *Entropy rate of random walks on complex networks under stochastic resetting*, arXiv:2208.05665 (2022; earliest public version August 11, 2022), https://arxiv.org/abs/2208.05665.
2. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568 (2019), https://arxiv.org/abs/1910.13568.
