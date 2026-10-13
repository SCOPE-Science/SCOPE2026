# Best-increment rates do not imply subsequence iterate rates in proximal multiblock ADMM
## Finding

Theorem 3.4 of Li--Yuan proves the best-increment estimate
\[
\min_{1\le j\le k}
\sum_{i=0}^n
(c_i+\widetilde c_i)
\|x_i^{j+1}-x_i^j\|^2
=
o(1/k).
\]
Immediately afterward, the paper interprets this as implying that among convergent subsequences, the fastest converges at rate \(o(1/k)\); the abstract and conclusion similarly advertise an \(o(1/k)\) convergent-subsequence rate.

That interpretation does not follow from the displayed estimate or from its proof. The proved quantity is a best squared inter-iterate displacement. It is not a distance from an iterate to a KKT point.

The unconditional rate consequence is instead
\[
\min_{1\le j\le k}
\left(
\sum_{i=0}^n
(c_i+\widetilde c_i)
\|x_i^{j+1}-x_i^j\|^2
\right)^{1/2}
=
o(k^{-1/2}).
\]
No distance-to-limit rate follows without an additional regularity estimate linking an iterate error to a step norm or a KKT residual.

A scalar sequence gives a decisive logical counterexample. Let
\[
z_k=\frac1{\log(k+2)}.
\]
Then \(z_k\to0\), its squared increments are summable, and
\[
\min_{1\le j\le k}|z_{j+1}-z_j|^2=o(1/k).
\]
Nevertheless, for every subsequence \(k_\ell\to\infty\),
\[
k_\ell |z_{k_\ell}|
=
\frac{k_\ell}{\log(k_\ell+2)}
\longrightarrow\infty.
\]
Thus no subsequence converges to the limit at rate \(o(1/k_\ell)\), or even \(O(1/k_\ell)\).

The counterexample is to the inference from the proved increment estimate to an iterate-distance rate. It is not claimed to be a trajectory of the source ADMM.

## Assumptions and scope

The source theorem first establishes vanishing primal and dual increments and then derives a summability estimate for weighted squared primal increments. Its averaging argument produces the displayed best-increment \(o(1/k)\) bound.

The source separately establishes that accumulation points are KKT points under its assumptions. Qualitative identification of accumulation points does not supply a quantitative error bound between an iterate and the KKT set.

The result here therefore distinguishes three notions:

1. a best squared step or motion certificate;
2. a stationarity or KKT residual;
3. distance of an iterate to a limiting KKT point.

Only the first receives the displayed \(o(1/k)\) estimate in Theorem 3.4.

## Proof

Define
\[
Q_j=
\sum_{i=0}^n
(c_i+\widetilde c_i)
\|x_i^{j+1}-x_i^j\|^2.
\]
The source proves
\[
\min_{1\le j\le k}Q_j=o(1/k).
\]
Since every \(Q_j\ge0\),
\[
\min_{1\le j\le k}\sqrt{Q_j}
=
\sqrt{\min_{1\le j\le k}Q_j}
=
o(k^{-1/2}).
\]
This is the exact rate that follows merely by taking square roots.

To show that no iterate-distance rate follows from this information alone, consider
\[
z_k=\frac1{\log(k+2)}.
\]
The function
\[
h(t)=\frac1{\log t}
\]
has derivative
\[
h'(t)=-\frac1{t(\log t)^2}.
\]
By the mean-value theorem, for some
\[
\xi_k\in(k+2,k+3),
\]
\[
|z_{k+1}-z_k|
=
\frac1{\xi_k(\log\xi_k)^2}.
\]
Hence
\[
|z_{k+1}-z_k|
=
\Theta\!\left(\frac1{k(\log k)^2}\right)
\]
and
\[
|z_{k+1}-z_k|^2
=
\Theta\!\left(\frac1{k^2(\log k)^4}\right).
\]
Therefore
\[
\sum_{k=1}^{\infty}|z_{k+1}-z_k|^2<\infty
\]
and, simply by selecting the last available index,
\[
\min_{1\le j\le k}|z_{j+1}-z_j|^2
\le
|z_{k+1}-z_k|^2
=
o(1/k).
\]

On the other hand,
\[
z_k\to0
\]
but
\[
k|z_k|
=
\frac{k}{\log(k+2)}
\longrightarrow\infty.
\]
The same statement holds along every subsequence \(k_\ell\to\infty\):
\[
k_\ell|z_{k_\ell}|\to\infty.
\]
Thus no subsequence has distance \(o(1/k_\ell)\) to the limit.

Consequently, square summability, vanishing increments, and a best squared-increment rate of \(o(1/k)\) do not imply an \(o(1/k)\) iterate-distance rate.

An additional relation is necessary. For example, an error bound of the form
\[
\operatorname{dist}(x^k,\mathcal Z^\star)
\le
\omega(R_k),
\]
where \(R_k\) is a controlled step or KKT residual and \(\omega(t)\to0\), can transfer a residual rate into an iterate rate. No such rate-transferring estimate is established in the source proof of Theorem 3.4.

## Verification

The standalone script `artifacts/verify_rate_gap.py` evaluates the counterexample sequence, checks square summability numerically with a rigorous tail bound, verifies the displayed asymptotic upper bound on squared increments, and confirms growth of \(kz_k\).

Those computations are supporting evidence. The quantified separation follows analytically from the mean-value theorem and \(k/\log k\to\infty\).

## Relationship to prior work

The primary source explicitly proves a best weighted squared-increment estimate and then describes it as an \(o(1/k)\) rate for a convergent subsequence.

Earlier multiblock ADMM work by Deng--Lai--Peng--Yin also uses the phrase \(o(1/k)\) convergence, but its rate analysis is framed through algorithmic residual or successive-iterate quantities in a convex setting. It does not provide the missing implication from a best squared increment to distance of a subsequence from a KKT point in the Li--Yuan nonconvex setting.

Targeted searches using the primary arXiv identifier, theorem number, title, \(o(1/k)\) language, best-increment language, and correction or erratum terminology did not locate a published correction of this rate interpretation.

## Limitations

The scalar sequence is a logical counterexample to the rate implication, not an ADMM trajectory. The result therefore does not prove that the Li--Yuan iterates fail to have an \(o(1/k)\) subsequence on every problem.

The proved correction is limited to what follows unconditionally from Theorem 3.4's displayed estimate:
\[
\min_{1\le j\le k}\sqrt{Q_j}=o(k^{-1/2}).
\]
Stronger iterate rates may hold under additional error-bound, metric-subregularity, Kurdyka--Łojasiewicz, strong-convexity, or other problem-specific structure.

## References

1. B. Li, Y.-x. Yuan, *Convergent Proximal Multiblock ADMM for Nonconvex Dynamics-Constrained Optimization*, arXiv:2506.17405v1, first public 20 June 2025; later published in *Optimization*, DOI: 10.1080/02331934.2026.2725054.
2. W. Deng, M.-J. Lai, Z. Peng, W. Yin, *Parallel Multi-Block ADMM with o(1/k) Convergence*, *Journal of Scientific Computing* 71, 712--736, DOI: 10.1007/s10915-016-0318-2; preprint arXiv:1312.3040.
