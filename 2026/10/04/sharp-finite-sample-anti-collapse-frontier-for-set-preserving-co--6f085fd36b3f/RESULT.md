# Sharp finite-sample anti-collapse frontier for set-preserving conformal e-calibration

## Finding

Let \(N=n+1\ge 2\), let \(\alpha\in(0,1)\), and assume tie-free conformal scores so that under the null the conformal p-value \(P\) is uniform on the rank grid
\[
\mathcal P_N=\left\{\frac1N,\frac2N,\ldots,1\right\}.
\]
Write
\[
k=\lfloor \alpha N\rfloor,\qquad \theta=\alpha N-k.
\]
The main case is \(0<\theta<1\), which is precisely the non-lattice case used by the positive set-preserving construction of Alami, Zakharia, and Ben Taieb.

Call a map \(F:\mathcal P_N\to(0,\infty)\) an exact level-\(\alpha\) set-preserving grid calibrator when
\[
\frac1N\sum_{j=1}^N F\!\left(\frac jN\right)=1
\]
and the e-value rejection threshold agrees exactly with the conformal p-value rejection threshold:
\[
F\!\left(\frac jN\right)\ge \frac1\alpha
\quad\Longleftrightarrow\quad
j\le k.
\]
Define its worst-rank multiplicative reserve by
\[
m(F)=\min_{1\le j\le N}F\!\left(\frac jN\right).
\]

Then the sharp finite-sample frontier is
\[
m(F)\le m^*
=
\frac{N-k/\alpha}{N-k}
=
\frac{\theta}{\alpha\bigl(N(1-\alpha)+\theta\bigr)}.
\]
Equality holds if and only if, on the rank grid,
\[
F\!\left(\frac jN\right)=
\begin{cases}
1/\alpha,&j\le k,\\
m^*,&j>k.
\end{cases}
\]
Thus the unique grid optimizer is a two-level calibrator. In particular,
\[
m^*\le \frac{1}{\alpha N(1-\alpha)},
\]
so no positive exact set-preserving calibrator can keep all of its conformal-rank e-values uniformly bounded away from zero as the calibration size grows.

At the lattice boundary \(\theta=0\), exactness and set preservation force all post-threshold grid values to be zero. This recovers, quantitatively, why a strictly positive exact construction excludes the case \(\alpha N\in\mathbb N\).

## Assumptions and scope

The result concerns the discrete, tie-free conformal p-value grid. It does not claim that the two-level optimizer is smooth or invertible; rather, it gives the best possible rankwise lower floor over the larger class of all positive exact set-preserving grid calibrators. Therefore it also upper-bounds every smooth strictly decreasing calibrator in the P2E class of Alami, Zakharia, and Ben Taieb. When \(N>2\), equality requires repeated values within at least one side of the threshold and is consequently incompatible with strict decrease.

The criterion is deliberately worst-case over conformal ranks. It is not an average power criterion, an alternative-distribution log-growth criterion, or a statement that small e-values occur frequently. It quantifies the strongest one-step multiplicative reserve that exact set preservation can guarantee uniformly over all rank outcomes.

## Proof

Put
\[
e_j=F\!\left(\frac jN\right),\qquad
m=\min_{1\le j\le N}e_j.
\]
Exact set preservation gives
\[
e_j\ge \frac1\alpha
\quad\text{for }1\le j\le k,
\]
while positivity implies
\[
e_j\ge m
\quad\text{for }k<j\le N.
\]
Exactness therefore yields
\[
N=\sum_{j=1}^N e_j
\ge
\frac{k}{\alpha}+(N-k)m.
\]
Rearranging,
\[
m\le
\frac{N-k/\alpha}{N-k}
=
\frac{\alpha N-k}{\alpha(N-k)}
=
\frac{\theta}{\alpha\bigl(N(1-\alpha)+\theta\bigr)}
=:m^*.
\]

The bound is attainable. Set
\[
e_j^*=
\begin{cases}
1/\alpha,&j\le k,\\
m^*,&j>k.
\end{cases}
\]
Because \(0<\theta<1\), we have \(m^*>0\). Also \(m^*<1/\alpha\), since \(\alpha<1\). Finally,
\[
\sum_{j=1}^N e_j^*
=
\frac{k}{\alpha}+(N-k)m^*
=
N,
\]
so the grid calibrator is exact and set-preserving.

The equality characterization follows from the same sum bound. Equality in
\[
\sum_{j=1}^N e_j
\ge
\frac{k}{\alpha}+(N-k)m
\]
requires simultaneously \(e_j=1/\alpha\) for every \(j\le k\) and \(e_j=m\) for every \(j>k\). Thus the two-level optimizer is the unique grid-value pattern attaining \(m^*\).

Since \(\theta<1\) and \(N(1-\alpha)+\theta\ge N(1-\alpha)\),
\[
m^*
=
\frac{\theta}{\alpha\bigl(N(1-\alpha)+\theta\bigr)}
\le
\frac{1}{\alpha N(1-\alpha)}.
\]
This proves the finite-sample anti-collapse ceiling.

If \(\theta=0\), then \(k=\alpha N\) and the first \(k\) threshold-compatible values already contribute at least
\[
\frac{k}{\alpha}=N
\]
to the exactness sum. Hence all of them must equal \(1/\alpha\), while every remaining nonnegative grid value must equal zero. A strictly positive exact set-preserving calibrator is therefore impossible at the lattice boundary.

## Verification

The argument is an exact finite-dimensional inequality; no simulation is used as proof. The accompanying script `verify_floor.py` checks the algebra on many rational pairs \((N,\alpha)\), verifies exactness and set preservation of the extremal two-level construction, and stress-tests the upper bound against randomly generated feasible grid vectors.

The script also checks the lattice boundary separately. Its finite enumeration is supplementary only; the theorem follows from the exact sum argument above.

## Relationship to prior work

Alami, Zakharia, and Ben Taieb introduce finite-\(n\), level-dependent P2E calibrators specifically to preserve the conformal prediction set while remaining exact, smooth, invertible, and strictly positive. Their motivation explicitly notes that the classical all-or-nothing calibrator takes zero values, causing products of e-values to collapse and giving negative-infinite e-power. Their main construction proves existence in the non-lattice case and pointwise convergence toward the all-or-nothing calibrator as the calibration size grows.

The present result addresses a different question: among all exact set-preserving calibrators on the finite conformal rank grid, how large can the smallest e-value possibly be? The answer is the explicit sharp value \(m^*\). It therefore quantifies an unavoidable worst-rank limitation of positivity that is not supplied by existence, smoothness, pointwise domination, or asymptotic convergence alone.

Classical p-to-e calibration theory, including Vovk and Wang, studies validity and admissible calibration rules for general p-values. The present statement is instead a finite-grid extremal consequence of exactness plus decision-equivalence at one conformal level.

## Limitations

The theorem uses the exact discrete-uniform null law of tie-free conformal ranks. With ties, randomized ranks, conservative p-values, or nonuniform null rank laws, the exactness constraint changes and so does the frontier.

The criterion is a worst-rank floor. A calibrator with a smaller minimum may have better log-growth under a particular alternative, better aggregation behavior, or better numerical properties. The theorem does not rank calibrators under those other objectives.

The two-level optimizer is not smooth or invertible. The result is best interpreted as a sharp upper bound on what any smoother positive construction can guarantee uniformly over all conformal ranks.

## References

Nabil Alami, Jad Zakharia, and Souhaib Ben Taieb. “Set-Preserving Calibration from Conformal P-Values to E-Values.” Proceedings of the 43rd International Conference on Machine Learning, PMLR 306:1680–1705, 2026. arXiv:2606.03600v1.

Vladimir Vovk and Ruodu Wang. “E-values: Calibration, combination, and applications.” Annals of Statistics 49(3):1736–1754, 2021. arXiv:1912.06116.

Aaditya Ramdas and Ruodu Wang. “Hypothesis testing with e-values.” Foundations and Trends in Statistics, 2025. arXiv:2410.23614.
