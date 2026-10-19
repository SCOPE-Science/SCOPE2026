# Logarithmic reversal cascades and a sharp ballistic-front deficit law

## Finding

Let a one-dimensional persistent walker have independent direction reversals at steps \(k\), with reversal probabilities \(p_k\sim c/(k\log k)\) for a fixed \(c>0\). The walker moves by one lattice unit in its current direction at every step. If \(X_N\) is its position after \(N\) steps, define the distance to the ballistic edge by \(B_N=N-|X_N|\). Then, for every \(0<z<1\),
\[
\lim_{N\to\infty}\Pr\!\left(B_N\le N^z\right)=z^c.
\]
Equivalently, \(\log(1+B_N)/\log N\) converges to a \(\mathrm{Beta}(c,1)\) distribution. More sharply, if \(T_N\) is the last reversal step before \(N\), with the convention \(T_N=1\) when no reversal occurs, then
\[
\frac{B_N}{2T_N}\longrightarrow 1\quad\text{in probability}.
\]
The full hierarchy of recent reversal times also converges: for every fixed positive integer \(m\), the \(m\) largest log-rescaled reversal times converge jointly to
\[
(U_1,\ldots,U_m)=\left(e^{-E_1/c},e^{-(E_1+E_2)/c},\ldots,e^{-(E_1+\cdots+E_m)/c}\right),
\]
where the \(E_j\) are independent unit exponential random variables. This identifies the ballistic-front deficit with the latest level of a scale-invariant Poisson reversal cascade.

## Assumptions and scope

Fix \(c>0\), and independent Bernoulli random variables \(\xi_k\) with \(\Pr(\xi_k=1)=p_k\in[0,1]\) and \(k\log k\,p_k\to c\) as \(k\to\infty\). Finitely many initial probabilities may be arbitrary. Let \(V_0\in\{-1,1\}\) be any initial direction (possibly deterministic), define \(V_k=(-1)^{\xi_k}V_{k-1}\) and \(X_N=\sum_{k=1}^N V_k\). For \(j\ge1\), let \(T_N^{(j)}\) be the \(j\)-th largest index \(k\le N\) such that \(\xi_k=1\); set missing indices to \(1\) when using logarithms, and set the second-last missing index to \(0\) in the pathwise bounds below. The first part of the claim uses \(T_N=T_N^{(1)}\). The limit is independent of the initial direction and of changes to finitely many \(p_k\).

## Proof

**1. Reversal point process.** For each \(N\) consider the random point measure \(\sum_{k\le N:\xi_k=1}\delta_{\log k/\log N}\) on \((0,1]\). For any \(0<a<b\le1\),
\[
\sum_{N^a<k\le N^b}p_k\longrightarrow c\log(b/a),\qquad
\max_{k>N^a}p_k\longrightarrow0.
\]
The first assertion follows by comparison with \(c\sum(k\log k)^{-1}\); uniformity of the relative error follows because all considered indices tend to infinity. Independence and expansion of the logarithm of the Bernoulli Laplace functional show that the point measure converges vaguely on \((0,1]\) to a Poisson point process with intensity \(c\,du/u\). In particular, for every fixed \(m\), its \(m\) largest atoms converge jointly to the \(m\) largest limiting atoms. The limit has infinitely many atoms accumulating only at zero, and no ties. Under \(u=e^{-s/c}\) these atoms correspond to the arrival times of a unit-rate homogeneous Poisson process; hence their ordered values are precisely the displayed exponential products. The first atom has distribution \(\Pr(U_1\le z)=z^c\), \(0<z<1\).

**2. Separation of the last two reversal times.** Joint convergence of the two largest log-scaled times implies that
\[
\frac{\log T_N^{(1)}-\log T_N^{(2)}}{\log N}\ \Longrightarrow\ U_1-U_2>0\quad\text{almost surely}.
\]
Thus \(T_N^{(2)}/T_N^{(1)}\to0\) in probability. Also \(T_N^{(1)}\to\infty\) in probability since \(\sum_k p_k=\infty\), while \(T_N^{(1)}/N\to0\) in probability because \(U_1<1\) almost surely. The convention for missing reversals is irrelevant because the probability of fewer than two reversals vanishes, by divergence of the expected independent reversal count and its variance bound.

**3. The ballistic-front identity.** Put \(T=T_N^{(1)}\), and let \(L\) be the second-last reversal index, or \(0\) if absent. For any realization, the final velocity is constant from the most recent reversal onward. The block of steps after the second-last reversal and before the last reversal has velocity opposite to the terminal velocity; all steps with opposite terminal velocity occur strictly before the last reversal. Consequently, with \(Q_N=N-V_N X_N\),
\[
2\bigl(T-\max\{L,1\}\bigr)\le Q_N\le2T.
\]
On the event \(T/N<1/2\), one has \(Q_N<N\) (apart from a harmless boundary equality), so \(X_N\) has the sign of \(V_N\) and \(B_N=Q_N\). Since \(L/T\to0\), \(T\to\infty\), and \(T/N\to0\) in probability, squeezing yields \(B_N/(2T)\to1\) in probability. It follows that \(\log(1+B_N)/\log N-\log T/\log N\to0\) in probability. Slutsky's theorem proves the \(\mathrm{Beta}(c,1)\) logarithmic deficit and its distribution-function version for \(0<z<1\).

## Verification

The standalone `verify_edge.py` computes the exact finite-size survival product for the most recent reversal, simulates independent reversal histories under \(p_k=c/(k\log k)\), and checks the pathwise front bounds. At \(N=300000\), six independent comparisons across three distinct values of \(c\) agree with the exact finite-size calculations within prescribed Monte Carlo tolerance. These finite tests corroborate the mechanism but do not establish the infinitely large limit. To repeat: run `python verify_edge.py` with NumPy installed. Only this script is required to reproduce the reported calculations.

## Relationship to prior work

Pradhan, Ray, and Roy (2026) introduce time-dependent reversal protocols, specifically list logarithmically corrected inverse-time rates, and discuss the diffusive-to-ballistic transition; their article does not state this logarithmic ballistic-front deficit law or the point-process hierarchy. Engländer, Volkov, and Wang (2019/2020) prove that in the strongly critical regime \(p_k=o(1/k)\) with divergent total reversal rate the rescaled path converges to a random ballistic ray. Their known ray limit applies here and is not claimed as new. The present result specifies a finer observable invisible to that weak path limit: the random power at which the residual distance to the ballistic boundary grows, together with the exact reversal-age hierarchy that determines it. General Poisson convergence and extreme-order-statistic principles are standard ingredients and are not presented as new.

## Limitations

The result concerns independent reversals and the specified \(k\log k\) asymptotic; it does not cover correlated reversals, state-dependent rates, or finite-speed turnaround dynamics. The theorem establishes convergence in distribution for the logarithmic exponent and in probability for the normalized deficit, not a uniform finite-size error bound or almost-sure convergence. At finite \(N\) there may be no reversal, and convergence for the logarithmically slow rate can be very slow. The novelty assessment concerns the sharp ballistic-front observable, not the known ballistic limiting ray or the general Poisson-limit machinery; broader related renewal/extreme-value literature may contain implicit versions.

## References

1. A. Pradhan, P. Ray, and R. Roy, *Diffusive-to-Ballistic transition in a Persistent Random Walk*, arXiv:2605.20116v1 (first public 2026-05-19), https://arxiv.org/abs/2605.20116.
2. J. Engländer, S. Volkov, and Z. Wang, *The coin-turning walk and its scaling limit*, arXiv:1904.10953v1 (2019); Electronic Journal of Probability 25 (2020), article 3, https://arxiv.org/abs/1904.10953.
3. F. Bouguet and B. Cloez, *Fluctuations of the empirical measure of freezing Markov chains*, Electronic Journal of Probability 23 (2018), https://doi.org/10.1214/17-EJP130 (general cooling-chain background; no originality claimed for its Dirichlet limits).
