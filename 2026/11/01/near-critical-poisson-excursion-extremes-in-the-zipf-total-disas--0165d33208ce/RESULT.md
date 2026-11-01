# Near-critical Poisson excursion extremes in the Zipf total-disaster chain

## Finding
Fix \(c\in\mathbb R\). A horizon-dependent Zipf total-disaster walk has upward transition probability
\[
p_{n,k}=\left(\frac{k+1}{k+2}\right)^{\beta_n},\qquad \beta_n=1+\frac c{\log n}.
\]
With \(K^{(n)}_0=0\), \(b_n=n/\log n\), and
\[
a(c)=\int_0^1 e^{-cu}\,du=\begin{cases}(1-e^{-c})/c,&c\ne0,\\1,&c=0,\end{cases}
\qquad \lambda(c)=\frac{e^{-c}}{a(c)}=\begin{cases}c/(e^c-1),&c\ne0,\\1,&c=0,\end{cases}
\]
let \(L_{n,j}\) denote consecutive return-cycle lengths, \(S_{n,j}=\sum_{i=1}^jL_{n,i}\), \(N_n=\max\{j:S_{n,j}\le n\}\), and \(H_{n,j}=L_{n,j}-1\). The following three assertions hold:

1. \(N_n/b_n\longrightarrow1/a(c)\) in probability.
2. On the locally compact space \([0,1]\times(0,\infty)\), the point measure
\[
\Xi_n=\sum_{j\ge1:S_{n,j}\le n,\ H_{n,j}>0}\delta_{(S_{n,j-1}/n,\,H_{n,j}/b_n)}
\]
converges vaguely in distribution to a Poisson random measure of intensity \(\lambda(c)\,dt\,z^{-2}dz\).
3. For \(M_n=\max_{0\le t\le n}K^{(n)}_t\), at every \(x>0\),
\[
\lim_{n\to\infty}\Pr\{M_n/b_n\le x\}=\exp\left(-\frac{\lambda(c)}x\right).
\]
The coefficient \(\lambda(c)\) decreases strictly from arbitrarily large values to zero as \(c\) moves from negative to positive infinity. Thus the extreme-value law crosses the chain's positive/null recurrence boundary continuously.

## Assumptions and scope
For each integer \(n\ge2\) large enough that \(\beta_n>0\), the entire length-\(n\) observation uses this one fixed \(\beta_n\); the parameter does **not** evolve during an individual path. The chain takes state \(k+1\) from state \(k\) with probability \(p_{n,k}\), and otherwise is reset to state zero, including possible one-step returns from zero to zero. Its independent uniform transition innovations generate iid positive integer return-cycle lengths \(L_{n,j}\). There is no stationarity assumption. The horizon is deterministic \(n\), time points are integer \(0\le t\le n\), and the marked process includes only *completed* excursions. The vague topology tests functions with mark support bounded away from zero.

For \(c<0\) the chain is null recurrent for every sufficiently large \(n\); for \(c=0\) it is at the recurrence boundary; for \(c>0\) it is positive recurrent for every sufficiently large \(n\). These assertions concern a triangular family of chains, not a long-time theorem for one fixed chain.

## Proof
**1. Exact regenerative law.** Along one excursion beginning at zero,
\[
\Pr\{L_{n,1}\ge k\}=\prod_{i=0}^{k-2}p_{n,i}=k^{-\beta_n}\quad(k=1,2,\dots).
\]
Consequently for any integer \(q\ge0\),
\[
\Pr\{H_{n,1}>q\}=\Pr\{L_{n,1}\ge q+2\}=(q+2)^{-\beta_n}.
\]
The product identity follows by telescoping; iid excursions follow from the strong Markov property at visits to zero. These formulas include the trivial length-one excursions.

**2. Renewal clock near the critical exponent.** Write \(\overline L_{n,j}=L_{n,j}\wedge n\). The tail-sum identity gives
\[
\frac{\mathbb E\overline L_{n,1}}{\log n}
=\frac1{\log n}\sum_{k=1}^n k^{-1-c/\log n}\longrightarrow\int_0^1e^{-cu}\,du=a(c).
\]
Indeed, the sum is a logarithmic Riemann sum after the substitution \(u=\log k/\log n\), with a vanishing Euler-summation error, uniformly for fixed \(c\). Furthermore, using the tail-sum second-moment formula,
\[
\mathbb E\overline L_{n,1}^{\,2}
\le2\sum_{k=1}^n k\Pr\{L_{n,1}\ge k\}
=2\sum_{k=1}^n k^{-c/\log n}\le 2e^{|c|}n.
\]
For any fixed \(T>0\), among the first \(\lfloor Tb_n/a(c)\rfloor\) cycles the probability of any \(L_{n,j}>n\) is bounded by
\[
O_c(n/\log n)\Pr\{L_{n,1}>n\}=O_c(1/\log n).
\]
The variance of the sum of those truncated cycles is \(O_c(n^2/\log n)\), while its expectation divided by \(n\) tends to \(T\). Chebyshev's inequality therefore gives
\[
\frac{S_{n,\lfloor Tb_n/a(c)\rfloor}}n\longrightarrow T
\quad\text{in probability}.
\]
Using a finite time grid and monotonicity of \(S_{n,j}\) strengthens this to
\[
\max_{0\le j\le \lfloor Tb_n/a(c)\rfloor}
\left|\frac{S_{n,j}}n-\frac{j a(c)}{b_n}\right|\longrightarrow0
\quad\text{in probability}.
\]
Bracketing the renewal index \(N_n\) between the indices associated with deterministic times \(1-\varepsilon\) and \(1+\varepsilon\) yields \(N_n/b_n\to1/a(c)\) in probability.

**3. Rare peaks and the spatial Poisson law.** For each fixed \(z>0\),
\[
b_n\Pr\{H_{n,1}/b_n>z\}
=b_n(\lfloor zb_n\rfloor+2)^{-\beta_n}
\longrightarrow\frac{e^{-c}}z,
\]
since \(\log b_n/\log n\to1\) and \(b_n^{1-\beta_n}\to e^{-c}\). Define \(m_n=\lfloor b_n/a(c)\rfloor\). Thus \(m_n\Pr\{H_{n,1}/b_n>z\}\to\lambda(c)/z\). Independence of the cycle marks yields, by direct product expansion of their Laplace functional, the marked rare-event convergence
\[
\sum_{j\ge1}\delta_{(j/m_n,H_{n,j}/b_n)}
\ \Longrightarrow\ \operatorname{PRM}\!\left(\lambda(c)\,dt\,z^{-2}dz\right)
\]
on each fixed compact time window and against continuous nonnegative tests supported a positive distance from mark zero. The limiting mark tail \(\lambda(c)/z\) gives the density \(\lambda(c)z^{-2}\).

The uniform renewal-clock estimate in Step 2 allows replacement of index time \(j/m_n\) by actual excursion start time \(S_{n,j-1}/n\). On the event that the renewal index differs from \(m_n\) by at most \(\varepsilon m_n\), the symmetric difference between the first \(m_n\) excursions and those completed by time \(n\) lies in an index band of at most \(2\varepsilon m_n+O(1)\) cycles. For every fixed mark threshold \(z>0\), the probability that this band contains a mark larger than \(z\) is at most \(2\varepsilon\lambda(c)/z+o(1)\), by a union bound. First let \(n\to\infty\), then \(\varepsilon\downarrow0\). This proves the stated space-time Poisson convergence, including the restriction to completed excursions.

**4. Path maximum, including the unfinished excursion.** Let \(Q_n=\max_{1\le j\le N_n}H_{n,j}\), with \(Q_n=0\) when \(N_n=0\). The previous step gives \(\Pr\{Q_n/b_n\le x\}\to e^{-\lambda(c)/x}\) for each \(x>0\) (the limiting Poisson process has no points on a fixed mark boundary). The observed path maximum obeys
\[
Q_n\le M_n\le\max\{Q_n,H_{n,N_n+1}\}.
\]
The index of the straddling excursion lies, with probability approaching one as \(\varepsilon\downarrow0\), within \(\varepsilon m_n+O(1)\) of \(m_n\). The same small-band union bound gives \(\Pr\{H_{n,N_n+1}>x b_n\}\le O_x(\varepsilon)+o(1)\). Hence the unfinished excursion does not change the limit, proving the Fréchet law.

**5. Strict crossover monotonicity.** For \(c\ne0\), differentiation yields
\[
\lambda'(c)=\frac{e^c(1-c)-1}{(e^c-1)^2}<0.
\]
The numerator is strictly negative for every nonzero \(c\), since the derivative of \(e^c(1-c)\) is \(-ce^c\), so this function attains its strict global maximum at zero, and the derivative at zero is \(-1/2\) by Taylor expansion. Limits at \(\pm\infty\) complete the assertion.

## Verification
The standalone file `verify.py` telescopes transition probabilities using exact rational arithmetic and checks the truncated-mean and marked-intensity limiting constants at widely separated finite sizes with arbitrary-precision special functions. It also runs reproducible finite-horizon Monte Carlo comparisons in the three recurrence regimes. `verification_output.txt` contains the actual output. These finite experiments are diagnostics, not proofs of the infinite limiting statements; the deterministic bounds and Laplace-functional argument above provide that proof. Run using Python 3 with `numpy` and `mpmath` installed:

```sh
python verify.py
```

## Relationship to prior work
Huillet's 2026 study supplies this exact Zipf total-disaster transition kernel, recurrence classification, return-cycle and excursion formulas and fixed-exponent contact-probability analysis [1]. Goncalves and Huillet's 2021 study develops related birth-catastrophe chains, renewal quantities and a Pareto-Zipf variant [2]. Both give essential model inputs, but the inspected relevant analyses concern fixed parameters rather than \(\beta_n=1+c/\log n\) with a deterministic horizon \(n\), and do not state the corresponding space-time Poisson excursion-extreme limit or the coefficient \(c/(e^c-1)\).

The iid rare-event Poisson limit and extremal point-process machinery are standard tools and are **not** asserted to be new. The claim assessed here is their explicit coupled use with the near-critical regenerative clock of this Markov chain, across both sides of its recurrence transition. A general unlocated triangular-array renewal-extremes theorem might imply the model-specific assertion, so historical novelty remains subject to independent literature review.

## Limitations
The statement is restricted to this exact Zipf transition kernel, fixed \(c\), fresh start at zero, and the triangular exponent \(\beta_n=1+c/\log n\). It does not establish a functional limit for the *entire* height path, moment convergence of maxima, uniformity over unbounded \(c\), or a fixed-parameter asymptotic. The point-process result concerns completed excursions; the path-maximum argument separately controls the straddling excursion. Independent validation has not been performed, and the breadth of general renewal-extremes literature leaves a residual originality risk.

## References
[1] Thierry E. Huillet, *On Divisibility Properties of Zipf Law and Relatives*, arXiv:2610.29974v1, publicly posted 2026-10-21, https://arxiv.org/abs/2610.29974. Section 3, especially the transition kernel and return-cycle law.

[2] Branda Goncalves and Thierry Huillet, *Scaling features of two special Markov chains involving total disasters*, arXiv:2101.03853v1, publicly posted 2021-01-11, https://arxiv.org/html/2101.03853v1. Especially Sections 3 and 4.

[3] Lambert De Monte and Ioannis Papastathopoulos, *A directional Poisson point process for univariate extremes*, Statistics and Probability Letters 235 (2026), 110722, https://doi.org/10.1016/j.spl.2026.110722. General point-process background; only abstract inspected.
