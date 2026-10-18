# Exact exponential completion rate in the vanishing-loss careless coupon collector

## Finding
Let \(c>0\) be fixed. In the uniform \(n\)-type post-draw careless coupon collector with independent per-coupon loss probability \(p_n=c/n\), started empty, write \(T_n\) for the first post-loss round at which every coupon is present. For all sufficiently large integers \(n\), \(0<p_n<1\). Set
\[
I(c)=\int_0^1\log\!\left(1+\frac{e^{cx}-1}{x}\right)\,dx,
\]
where the integrand at zero is \(\log(1+c)\). Then
\[
\frac{\log T_n}{n}\xrightarrow{\mathbb P} I(c),\qquad
\lim_{n\to\infty}\frac{\log\mathbb E T_n}{n}=I(c).
\]
In particular \(I(c)>\log(1+c)\) for every \(c>0\). The inequality is a strict exponential discrepancy between the true completion scale and the product of the one-point stationary marginals; it does not assert a limiting exponential distribution under finer time normalization.

## Assumptions and scope
The state \(S_t\subseteq[n]\) lists available coupons immediately **after** the independent losses of round \(t\). Initially \(S_0=\varnothing\). Each round samples a uniformly random label \(J_t\in[n]\), adjoins it to the collection, and then independently retains each present label with probability \(s_n=1-p_n\), including the newly sampled label. Losses and draws are mutually independent across labels and rounds. The first hitting time is \(T_n=\inf\{t\ge1:S_t=[n]\}\). The theorem fixes \(c>0\) as \(n\to\infty\), with \(n>\max\{1,c\}\). It does not cover varying \(c\), heterogeneous sampling, or alternative within-round event orders.

## Proof
**1. Exact stationary full-state probability.** Fix \(n\ge2\) and \(0<p<1\), put \(s=1-p\), and let \(\pi\) denote the unique stationary law of the finite irreducible, aperiodic chain. Uniqueness follows since any state can reach the empty state by sufficiently many losses, and every state can be reached from empty by selecting its constituent labels and retaining them while subsequently eliminating unwanted labels.

By permutation symmetry, for every prescribed set \(A\subseteq[n]\) of size \(k\), \(q_k=\pi\{S\supseteq A\}\) depends only on \(k\), with \(q_0=1\). After one uniform draw, the event that \(A\) is fully present occurs either when the sampled type is outside \(A\) and all of \(A\) was already present, or when the sampled type belongs to \(A\) and its remaining \(k-1\) labels were already present. All \(k\) labels must survive the subsequent loss step, hence stationarity gives exactly
\[
q_k=s^k\!\left[\left(1-\frac{k}{n}\right)q_k+\frac{k}{n}q_{k-1}\right].
\]
Consequently
\[
q_n=\pi\{[n]\}=\prod_{k=1}^n\frac{k s^k}{n-(n-k)s^k}
=\prod_{k=1}^n\left[1+\frac{n}{k}\left(s^{-k}-1\right)\right]^{-1}=:a_n.
\]
The finite stationary inclusion recursion is a standard prerequisite calculation, not the originality claim here.

**2. Sharp logarithmic stationary mass.** Insert \(p_n=c/n\), \(s_n=1-c/n\), and set \(b_n=-n\log s_n\to c\). For \(x\in(0,1]\) define \(f_b(x)=\log(1+(e^{bx}-1)/x)\), continuously extended at \(x=0\) by \(\log(1+b)\). The map \((b,x)\mapsto f_b(x)\) is continuous on any compact rectangle with \(b>0\), using \((e^{bx}-1)/x=b\int_0^1 e^{bxt}\,dt\). Therefore \(f_{b_n}\to f_c\) uniformly on \([0,1]\), and
\[
-\frac1n\log a_n=\frac1n\sum_{k=1}^n f_{b_n}(k/n)\longrightarrow\int_0^1 f_c(x)\,dx=I(c).
\]
Thus \(a_n=\exp(-nI(c)+o(n))\).

**3. A lower bound for the hitting time.** Couple a chain from \(\varnothing\) with an independently drawn stationary initial configuration using the same draws and losses at each future step. Set inclusion is preserved by a common draw and common per-label retention coins, so \(S_t^{\varnothing}\subseteq S_t^{\pi}\) at every time. Hence \(\Pr_{\varnothing}(S_t=[n])\le a_n\) for every \(t\ge0\). The union bound yields \(\Pr_{\varnothing}(T_n\le t)\le t a_n\), for integer \(t\ge1\). In particular for every \(0<\varepsilon<I(c)\),
\[
\Pr(T_n\le e^{n(I(c)-\varepsilon)})\longrightarrow0,
\]
where a noninteger threshold means its integer floor. Also \(\mathbb ET_n\ge e^{n(I(c)-\varepsilon)}(1-o(1))\).

**4. Uniform mixing and an upper bound for the hitting time.** Use the same-update coupling from any two initial configurations. A particular initial disagreement at a label survives one step only if that label is neither selected nor lost. Its probability is
\[
\rho_n=\left(1-\frac1n\right)(1-p_n)<1.
\]
A union bound over labels gives
\[
\sup_x\lVert P_n^t(x,\cdot)-\pi_n\rVert_{\mathrm{TV}}\le n\rho_n^t.
\]
Choose the integer block length
\[
b_n^*=\left\lceil\frac{\log(2n/a_n)}{-\log\rho_n}\right\rceil.
\]
Since \(-\log\rho_n=(1+c)/n+O(n^{-2})\) and \(-\log a_n=nI(c)+o(n)\), \(b_n^*=O(n^2)\) and \(n\rho_n^{b_n^*}\le a_n/2\). Consequently, from **every** possible state \(x\),
\[
\Pr_x(S_{b_n^*}=[n])\ge a_n/2.
\]
By the Markov property applied at consecutive block endpoints,
\[
\Pr_{\varnothing}(T_n>m b_n^*)\le(1-a_n/2)^m\quad(m\ge0),
\qquad\mathbb ET_n\le\frac{2b_n^*}{a_n}.
\]
For every \(\varepsilon>0\), the same bound gives \(\Pr(T_n>e^{n(I(c)+\varepsilon)})\to0\). Together with step 3, this proves the claimed convergence in probability and, by the lower and upper expectation bounds, the exact logarithmic mean limit.

**5. Strict departure from independent-marginal rate.** At all \(x\in(0,1]\), \(e^{cx}-1>cx\); hence \(f_c(x)>\log(1+c)\). Integration gives \(I(c)>\log(1+c)\). This inequality is strict for every fixed \(c>0\).

## Verification
Run `python3 check.py` with the Python standard library. The program independently constructs the full \(2^n\)-state transition matrix, solves its stationary linear equations in exact rational arithmetic for \(n=2,3,4\) and two loss probabilities, compares all prescribed-subset inclusion probabilities with the product formula, and checks stationary entrance-flow balance. Numerical Riemann-sum diagnostics for \(c=1\), at \(n=100,500,2000\), approach \(I(1)\approx0.8367278623\), exceeding \(\log2\approx0.6931471806\). These finite calculations do not prove the asymptotic theorem; steps 1–5 do.

## Relationship to prior work
Cruciani and Dudeja, *The Careless Coupon Collector's Problem* (arXiv:2602.20705v1, first submitted 2026-02-24), introduce the identical post-loss process, establish a metastable regime when \(p=c/n\), and state a mean-field scale under a spatial/temporal independence assumption. They do not derive the unconditional exact exponential growth rate in that regime. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors* (arXiv:2605.14511v1, first submitted 2026-05-14), obtains sharp flux and hitting-time laws when the loss probability is **fixed** as \(n\) varies; those asymptotics are not uniform in the triangular family used here. Its general stationary-entry framework motivates the distinction between stationary mass and return-time normalization. The exact stationary inclusion recurrence is also obtainable from the stationarity equations and is not claimed as new. The new claim is the explicit \(c/n\) exponential exponent for the first-passage time and mean, including the provable discrepancy from independent-marginal reasoning.

## Limitations
The result determines only the exponential rate, not the prefactor, the stationary-entry flux prefactor, or a fully normalized exponential limit law. Exact stationary mass does not alone determine a sharp constant-order hitting-time scale because the target may be visited in clusters. The theorem assumes fixed \(c>0\), uniform draws, and post-draw independent loss. Its novelty remains subject to independent priority verification against general metastability and density-dependent Markov-chain literature.

## References
- E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705v1 (2026-02-24), https://arxiv.org/html/2602.20705v1.
- C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1 (2026-05-14), https://arxiv.org/html/2605.14511v1.
- D. Aldous, *Markov chains with almost exponential hitting times*, Stochastic Processes and their Applications (1982), as cited and discussed in Long's Section 2. Classical general rare-set framework; no independent bibliographic/full-text inspection is claimed here.
