# Sharp directed entropy laws between multidimensional elephant-walk histories

## Finding

Fix an integer \(d\ge2\) and put \(D=2d\). For every \(\theta\in(-1/(D-1),1)\), let \(P_\theta^{(n)}\) be the law of the first \(n\) increments of the \(D\)-direction elephant random walk defined below. For distinct parameters \(\alpha,\beta\) in this interval, put
\[
\mathcal K_n(\alpha\Vert\beta)
=D_{\mathrm{KL}}(P_\alpha^{(n)}\Vert P_\beta^{(n)}).
\]
Then, with natural logarithms,
\[
\boxed{
\mathcal K_n(\alpha\Vert\beta)\sim
\begin{cases}
\dfrac{(D-1)(\alpha-\beta)^2}{2(1-2\alpha)}\log n,&\alpha<1/2,\\[6pt]
\dfrac{(D-1)(\alpha-\beta)^2}{4}(\log n)^2,&\alpha=1/2,\\[6pt]
\dfrac{(D-1)(\alpha-\beta)^2}{2(2\alpha-1)^2\Gamma(2\alpha)}n^{2\alpha-1},&\alpha>1/2.
\end{cases}}
\]
The first regime has the sharper additive error \(O(1)\), and the second has additive error \(O(\log n)\). In particular, for \(\alpha>\beta\),
\[
\lim_{n\to\infty}\frac{\mathcal K_n(\alpha\Vert\beta)}{\mathcal K_n(\beta\Vert\alpha)}
=\begin{cases}
\dfrac{1-2\beta}{1-2\alpha}>1,&\alpha<1/2,\\[6pt]
+\infty,&\alpha\ge1/2.
\end{cases}
\]
(The first case automatically has \(\beta<1/2\).) The reverse cases follow by inversion. Thus the divergence is directionally asymmetric at first order, and becomes unboundedly asymmetric whenever the larger memory parameter is critical or superdiffusive.

## Assumptions and scope

The increment alphabet consists of \(D=2d\) formal nearest-neighbor directions \(\{\pm e_1,\ldots,\pm e_d\}\). The first increment is uniform on the \(D\) directions. At each later step, select one past increment uniformly; with probability \(p\in(0,1)\) reproduce its direction, and with probability \(1-p\) choose uniformly among the other \(D-1\) directions. The associated reinforcement parameter is \(\theta=(Dp-1)/(D-1)\). All choices are made according to the full observed history. The two competing laws have the same uniform first-increment distribution. The result is about **complete ordered increment histories**, not solely their endpoint positions. Both fixed parameters are in the open interval above, so every finite path has positive probability under both laws. The constants implicit in error bounds may depend on the fixed dimension and parameters. When \(\alpha=\beta\), both laws coincide and the divergence equals zero exactly.

## Proof

For \(k\ge1\), write \(N_k(j)\) for the number of occurrences of direction \(j\) among the first \(k\) increments, and \(\Delta_k(j)=N_k(j)-k/D\). Then \(\sum_{j=1}^D\Delta_k(j)=0\), and for any parameter \(\theta\) the next-step conditional distribution is exactly
\[
q_{\theta,k}(j)=\frac1D+\theta\frac{\Delta_k(j)}k.
\tag{1}
\]
Its entries remain uniformly positive for fixed interior \(\theta\), since it is the convex combination, with weights \(p\) and \(1-p\), of the matching and nonmatching historical-direction frequencies.

By the chain rule for relative entropy (and cancellation of the identical first-increment laws),
\[
\mathcal K_n(\alpha\Vert\beta)
=\sum_{k=1}^{n-1}\mathbb E_\alpha\!
\left[D_{\mathrm{KL}}(q_{\alpha,k}\Vert q_{\beta,k})\right].
\tag{2}
\]
For a zero-sum vector \(z\) whose two conditional probability vectors \((1/D+\alpha z_j)\) and \((1/D+\beta z_j)\) are admissible, define
\[
F_{\alpha,\beta}(z)=\sum_{j=1}^D
\left(\frac1D+\alpha z_j\right)
\log\frac{1/D+\alpha z_j}{1/D+\beta z_j}.
\]
Taylor's formula at the origin gives
\[
F_{\alpha,\beta}(z)
=\frac{D(\alpha-\beta)^2}{2}\|z\|_2^2+R(z),
\qquad |R(z)|\le C\|z\|_2^3.
\tag{3}
\]
The remainder bound is **uniform**, not just local: the attainable zero-sum frequency vectors form a compact simplex, both denominators are uniformly positive for the fixed interior parameters, and the quotient of the third-order remainder by \(\|z\|_2^3\) extends boundedly across the origin.

Let \(S_k=\mathbb E_\alpha\|\Delta_k\|_2^2\) and \(b=(D-1)/D\). Conditional on the history, the centered next increment has drift \(\alpha\Delta_k/k\), and every elementary direction satisfies \(\|e_j-D^{-1}\mathbf1\|_2^2=b\). Expanding the squared norm yields the **exact** recurrence
\[
S_1=b,\qquad S_{k+1}=\left(1+\frac{2\alpha}{k}\right)S_k+b.
\tag{4}
\]
Solving it, with \(G_k=\Gamma(k+2\alpha)/(\Gamma(k)\Gamma(1+2\alpha))\), gives
\[
S_k=\begin{cases}
\dfrac{b}{1-2\alpha}\left(k-2\alpha G_k\right),&\alpha\ne1/2,\\[6pt]
bkH_k,&\alpha=1/2,
\end{cases}
\tag{5}
\]
where \(H_k=\sum_{j=1}^k j^{-1}\). The displayed gamma expressions are finite since \(\alpha>-1/(D-1)\ge-1/3\). In particular,
\[
S_k\sim\begin{cases}
bk/(1-2\alpha),&\alpha<1/2,\\
bk\log k,&\alpha=1/2,\\
b k^{2\alpha}/((2\alpha-1)\Gamma(2\alpha)),&\alpha>1/2.
\end{cases}
\tag{6}
\]

To control the accumulated remainder, define positive deterministic numbers \(A_1=1\) and \(A_{k+1}=A_k(1+\alpha/k)\); then \(A_k=\Gamma(k+\alpha)/(\Gamma(k)\Gamma(1+\alpha))\asymp k^\alpha\). The vector process \(M_k=\Delta_k/A_k\) is a martingale, and its coordinate increments are bounded by \(A_{k+1}^{-1}\). Coordinatewise Azuma--Hoeffding inequalities, followed by integration of their tails and the fixed-dimensional norm inequality, show
\[
\mathbb E_\alpha\|\Delta_k\|_2^3\le C\begin{cases}
k^{3/2},&\alpha<1/2,\\
(k\log(k+1))^{3/2},&\alpha=1/2,\\
k^{3\alpha},&\alpha>1/2.
\end{cases}
\tag{7}
\]
Thus \(\sum_{k<n}k^{-3}\mathbb E\|\Delta_k\|_2^3\) remains bounded when \(\alpha\le1/2\) and is \(o(n^{2\alpha-1})\) when \(\alpha>1/2\) (including the possible logarithmic intermediate order). Combining (2)--(3) therefore gives
\[
\mathcal K_n(\alpha\Vert\beta)=\frac{D(\alpha-\beta)^2}{2}
\sum_{k=1}^{n-1}\frac{S_k}{k^2}+\mathcal R_n,
\tag{8}
\]
where \(\mathcal R_n=O(1)\) for \(\alpha\le1/2\) and \(\mathcal R_n=o(n^{2\alpha-1})\) otherwise.

If \(\alpha<1/2\), equations (5) and \(G_k=O(k^{2\alpha})\) give
\[
\sum_{k<n}\frac{S_k}{k^2}=
\frac{b}{1-2\alpha}\log n+O(1).
\]
At \(\alpha=1/2\), the exact identity
\[
\sum_{k=1}^{n-1}\frac{S_k}{k^2}
=b\sum_{k=1}^{n-1}\frac{H_k}{k}
=\frac b2\left(H_{n-1}^2+H_{n-1}^{(2)}\right)
=\frac b2(\log n)^2+O(\log n)
\]
applies, with \(H_m^{(2)}=\sum_{j=1}^m j^{-2}\). When \(\alpha>1/2\), (5) and summation of powers yield
\[
\sum_{k<n}\frac{S_k}{k^2}
\sim\frac{b}{(2\alpha-1)^2\Gamma(2\alpha)}n^{2\alpha-1}.
\]
Multiplication by \(D(\alpha-\beta)^2/2\) and \(Db=D-1\) proves all three divergence formulas. Dividing the formulas with exchanged parameters proves the stated directional classification: in the diffusive--diffusive case the squared separation cancels, while every larger source parameter at or above criticality has strictly faster entropy growth than its smaller comparator. \(\square\)

## Verification

The accompanying `verify.py` is a standalone Python 3 deterministic checker. It independently enumerates small multidimensional direction-count states with exact rational probabilities, verifies recurrence (4), compares direct finite-history path divergence to the chain rule (2), checks the exact critical second-moment identity, and tests the quadratic local expansion numerically. Run it using `python3 verify.py`. The archived output records 8,482 passing assertions. These are finite structural tests; equations (1)--(8) provide the infinite-asymptotic justification.

## Relationship to prior work

Shuo Qin's 2026 work on elephant-walk cover times and ranges (arXiv:2609.17264v1, first public September 15, 2026) uses path relative-entropy comparisons to an independent uniform walk, bounding the divergence in the three memory regimes. The present claim concerns **exact constants for every pair of distinct interior memory parameters**, including neither necessarily representing an independent walk, together with directional comparison and its sharp phase boundary. The common conditional law and information-theoretic chain rule are not claimed as novel.

Bernard Bercu and Lucile Laulin (arXiv:2112.10405, 2021) derive one-dimensional elephant-walk likelihoods and local asymptotic normality/mixed normality for memory estimation, with Fisher information rates. Those local one-dimensional statistical results are important related information geometry, but their stated theorems do not give the fixed-separated, multi-direction, all-regime ordered pairwise divergence and exact directional ratio proved here. The exact empirical-frequency moment method is elementary and relies on known elephant-walk martingale ideas. Schütz and Trimper's 2004 study supplies the original walk and variance phase transition. The theorem should be viewed as a self-contained, specialized full-history information refinement of these results, not as a new reinforcement model.

## Limitations

All parameters are fixed and strictly interior, and \(d\ge2\); there is no claim of uniformity when parameters approach the boundary, grow close at an \(n\)-dependent rate, or when dimension changes with \(n\). The conclusion pertains to complete increment histories, not endpoint marginals, estimators, testing exponents, total variation, or general reinforced walks. The method proves only leading constants (plus the stated additive errors), not an exact finite-time entropy formula. Historical priority cannot be established from search results alone; a general likelihood comparison theorem might implicitly imply parts of the classification. Independent validation has not been performed.

## References

1. S. Qin, *Cover times and ranges of elephant random walks*, arXiv:2609.17264v1 (2026), https://arxiv.org/abs/2609.17264. First publicly submitted 2026-09-15.
2. B. Bercu and L. Laulin, *How to estimate the memory of the Elephant Random Walk*, arXiv:2112.10405 (2021), https://arxiv.org/abs/2112.10405.
3. G. M. Schütz and S. Trimper, *Elephants can always remember: Exact long-range memory effects in a non-Markovian random walk*, Physical Review E 70 (2004), 045101, https://doi.org/10.1103/PhysRevE.70.045101.
4. Y. Peres and S. Qin, *Transition probabilities of step-reinforced random walks*, arXiv:2604.07227 (2026), https://arxiv.org/abs/2604.07227.
