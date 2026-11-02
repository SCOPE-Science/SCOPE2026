# Gaussian double-logarithmic depth of the left boundary leaf in critical beta-splitting trees

## Finding

For the ordered discrete-time critical beta-splitting tree with \(n\) consecutively ordered leaves, let \(T_n\) be the number of edges between the root and the *leftmost* leaf. As \(n\to\infty\),
\[
\frac{T_n-2\log\log n}{\sqrt{6\log\log n}}\ \Longrightarrow\ N(0,1),
\qquad \frac{\mathbb E T_n}{\log\log n}\longrightarrow2.
\]
The fluctuation coefficient \(6\) applies to this deterministic boundary label, not to the height of a uniformly chosen leaf. The leading scale \(2\log\log n\) was anticipated heuristically by Aldous and Janson; the normal limit is the central statement here.

## Assumptions and scope

Each clade of size \(m\ge2\) consists of a consecutive interval of the ordered labels. Independently at every internal vertex, split it after the \(i\)-th leaf with probability
\[
q(m,i)=\frac1{2H_{m-1}}\left(\frac1i+\frac1{m-i}\right),\quad 1\le i\le m-1,
\qquad H_j=\sum_{h=1}^j\frac1h.
\]
All logarithms are natural. Edge depth is measured in number of splits; the model is discrete-time, with neither continuous holding times nor random relabeling. The leftmost-leaf subtree size \(X_t\) is a strictly descending Markov chain: \(X_0=n\), \(X_{t+1}=I_{X_t}\) until \(X_t=1\), where \(I_m\) has distribution \(q(m,\cdot)\). Its absorption time is \(T_n\). Primary subject classification: MSC2020 60C05.

## Proof

**1. A harmonic two-branch coupling.** Let \(J\) have \(\Pr(J=j)=1/(jH_{m-1})\), \(1\le j<m\), and let \(B\) be an independent fair bit. Conditional on current size \(m\), define \(I_m=J\) on one outcome of \(B\), and \(I_m=m-J\) on the other. This gives exactly the displayed split law, so it is an identity of Markov kernels, not an approximation.

**2. Potential-drop moments.** Define \(\ell_1=0\) and \(\ell_m=\log H_{m-1}\) for \(m\ge2\), and write \(\Delta_m=\ell_m-\ell_{I_m}\ge0\). For each fixed integer \(r\in\{1,2,3,4\}\),
\[
\mathbb E(\Delta_m^r)=\frac{r!}{2}+O_r\!\left(\frac{1+\ell_m^r}{H_{m-1}}\right). \tag{1}
\]
Here is an explicit justification of this nonstandard moment assertion. Put \(h=H_{m-1}\), \(u_j=H_j/h\) for \(0\le j\le m-1\), and \(f_r(u)=(-\log u)^r\). On the \(I_m=J\) branch, for \(j\ge2\), \(\Delta_m=\log(h/H_{j-1})=f_1(u_{j-1})\); for \(j=1\), the drop is \(\log h\). Because \(u_j-u_{j-1}=1/(jh)\), the expectation is a left-endpoint Riemann sum for \(\int_0^1f_r(u)\,du=r!\), with the singular first cell replaced by \((\log h)^r/h\). Monotonicity bounds the error away from the first cell by \(h^{-1}(\log h)^r\): telescope the excess of left-cell over right-cell rectangles, each cell width at most \(1/h\). On the first cell, the integral has size \(O_r((1+\log^r h)/h)\). Thus the small-branch moment is \(r!+O_r((1+\ell_m^r)/h)\). On the \(I_m=m-J\) branch, for \(J\le m/2\), the inequality \(H_{m-1}-H_{m-J-1}\le\log2+2\) gives \(0\le\Delta_m\le C/h\) for large \(m\). For \(J>m/2\), its probability is \(O(1/h)\), and \(\Delta_m\le\ell_m\). The large-branch contribution is \(O_r(h^{-r}+\ell_m^r/h)\). Averaging the two branches proves (1). In particular,
\[
\mathbb E\Delta_m=\tfrac12+o(1),\qquad
\operatorname{Var}(\Delta_m)=\tfrac34+o(1),\qquad
\sup_{m\ge2}\mathbb E\Delta_m^4<\infty. \tag{2}
\]
The statement about finite \(m\) follows because each \(I_m<m\) and there are only finitely many exceptions to the asymptotic bound.

**3. Stop above a low potential.** Write \(y=\ell_n\), \(b=y^{1/3}\), and take the least integer \(M=M(n)\ge3\) satisfying \(\ell_M\ge b\). Define \(\tau=\inf\{t:X_t<M\}\). For \(t<\tau\) the conditional drift of \(\ell_{X_t}-\ell_{X_{t+1}}\) is uniformly \(1/2+o(y^{-a})\) for every fixed \(a>0\), by (1), since \(H_{M-1}\ge e^b\) and the error bound decays exponentially in \(b\), up to powers of \(y\). In particular the drift is at least \(1/4\) for sufficiently large \(n\). The potential is nonnegative and decreasing, so optional stopping for bounded times and monotone convergence give \(\mathbb E\tau\le4y\). Moreover \(0\le\ell_{X_\tau}<b\), while \(\tau=O_{\mathbb P}(y)\).

Let
\[
Z_t=(\ell_{X_t}-\ell_{X_{t+1}})-\mathbb E[\ell_{X_t}-\ell_{X_{t+1}}\mid X_t]
\]
for \(t<\tau\), and \(S_\tau=\sum_{t<\tau}Z_t\). Its predictable quadratic variation is \((3/4)\tau+o_{\mathbb P}(y)\), and its conditional fourth moments are uniformly bounded by (2). As \(\mathbb E\tau=O(y)\), the martingale isometry gives \(S_\tau=O_{\mathbb P}(\sqrt y)\). The exact telescope
\[
y-\ell_{X_\tau}=\frac{\tau}{2}+S_\tau+o_{\mathbb P}(1)
\]
then yields \(\tau=2y+O_{\mathbb P}(\sqrt y)\), hence \(\tau/y\to2\) in probability. Consequently the predictable quadratic variation divided by \(y\) converges in probability to \(3/2\). The conditional Lindeberg condition follows from the uniform fourth moments, since for each \(\varepsilon>0\) its expectation is bounded by \(O(\mathbb E\tau/(\varepsilon^2y^2))=O(1/y)\). The stopped martingale central limit theorem therefore gives
\[
\frac{S_\tau}{\sqrt y}\Longrightarrow N(0,3/2),\qquad
\frac{\tau-2y}{\sqrt{6y}}\Longrightarrow N(0,1).
\]
The sign of \(S_\tau\) in the second conclusion is immaterial by normal symmetry.

**4. Negligible terminal segment.** Below \(M\), conditional expected remaining time is \(O(1+\ell_M)=O(1+b)\), uniformly in the starting state. To see this, fix a constant threshold \(m_0\) above which the potential drift is at least \(1/4\); optional stopping gives at most four times the starting potential in expected steps to reach a size below \(m_0\), after which there are at most \(m_0-1\) steps because sizes strictly decrease. Therefore \(T_n-\tau=o_{\mathbb P}(\sqrt y)\), since \(b=y^{1/3}=o(\sqrt y)\). Combining this with the stopped limit proves the CLT with \(y=\log H_{n-1}=\log\log n+o(1)\), which permits replacement of \(y\) in both centering and scaling by \(\log\log n\).

For expectations, bounded stopping first gives \(\mathbb E\tau\le4y\); the centered increments have mean zero under integrable stopping by the uniform second-moment bound. Taking expectations in the telescope and using the uniform drift approximation yields \(\mathbb E\tau=2y+O(y^{1/3})\). Adding the terminal expected time \(O(y^{1/3})\) gives \(\mathbb E T_n=2y+O(y^{1/3})\), establishing the stated first-order mean.

## Verification

The independent exact enumerator and recurrence implementation in `verify_boundary.py` agree through eight leaves. The script checks the harmonic mixture, normalization, moments and finite-size recurrences, and reports 383 passed assertions. All computations are finite consistency checks. The infinite-size central limit theorem rests on the preceding proof, especially the uniform potential-drop moment estimate and martingale Lindeberg argument.

Run with `python3 verify_boundary.py` using the Python standard library; no external packages or datasets are required.

## Relationship to prior work

Aldous and Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems* (arXiv:2303.02529, public since 2023-03-04), discuss the leftmost ordered leaf and heuristically anticipate depth around \(2\log\log n\); the variance coefficient and Gaussian limit here are additional. Aldous and Pittel (arXiv:2302.05066) establish central limit theorems for **uniformly selected** leaves rather than a fixed boundary leaf. Later work by Aldous and Janson (arXiv:2412.12319), Iksanov, Nikitin and Yakymiv (arXiv:2510.17343), and Chorbadzhiyska, Minchev and Savov (arXiv:2608.18320) also addresses random tagged leaves or other heights, and Ma (arXiv:2609.14329) treats the overall maximum. None of the examined statements implies the displayed boundary-leaf Gaussian law. Source comparisons do not constitute proof of historical novelty.

## Limitations

Only the ordered discrete-time critical model and the single extreme boundary leaf are considered. This does not determine the depth of arbitrary fixed internal labels, the maximum leaf height, or continuous-time path length. No Berry--Esseen rate, higher-order mean expansion, or independent mathematical audit is asserted. Historical priority should be checked further, especially across the broad fragmentation literature.

## References

1. David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529 (first public 2023-03-04), https://arxiv.org/abs/2303.02529.
2. David Aldous and Boris Pittel, *The Critical Beta-splitting Random Tree: Heights and Related Results*, arXiv:2302.05066, https://arxiv.org/abs/2302.05066.
3. David Aldous and Svante Janson, *The Critical Beta-splitting Random Tree IV: Mellin analysis of Leaf Height*, arXiv:2412.12319, https://arxiv.org/abs/2412.12319.
4. Alexander Iksanov, Anatolii Nikitin and Roman Yakymiv, *Some central limit theorems for critical beta-splitting tree*, arXiv:2510.17343, https://arxiv.org/abs/2510.17343.
5. Yoana R. Chorbadzhiyska, Martin Minchev and Mladen Savov, *Asymptotics for Beta-Splitting Trees via Homogeneous Fragmentations and Meromorphic Potential Theory*, arXiv:2608.18320, https://arxiv.org/abs/2608.18320.
6. Heng Ma, *The height of discrete-time critical beta-splitting trees*, arXiv:2609.14329, https://arxiv.org/abs/2609.14329.
