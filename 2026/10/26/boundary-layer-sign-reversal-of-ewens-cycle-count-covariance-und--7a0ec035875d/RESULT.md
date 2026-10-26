# Boundary-layer sign reversal of Ewens cycle-count covariance under near-maximal-cycle truncation

## Finding
For \(n\ge 2r+4\), \(r\ge1\), and \(\theta>0\), consider an Ewens(\(\theta\)) random permutation of \(n\) labels conditioned to have no cycle larger than \(n-r\). Let \(F\) and \(T\) count cycles of lengths one and two. Write \(c_{n,r}(\theta)=\operatorname{Cov}(F,T\mid\text{all cycles have length at most }n-r)\), and \(g_j(\theta)=(\theta)_j/j!\) for \(j\ge0\), with \(g_j=0\) for negative \(j\).

**Exact finite law.** Put \(a_{n-s}=g_{n-s}-\theta\sum_{j=0}^{r-s-1}g_j/(n-s-j)\) for \(s=0,1,2,3\), with empty sums zero. Then
\[
c_{n,r}(\theta)=\frac{\theta^2}{2a_n^2}\bigl(a_n a_{n-3}-a_{n-1}a_{n-2}\bigr).
\]

**Sharp fixed-\(r\) asymptotic sign classification.** For every fixed \(r\ge1\), as \(n\to\infty\),
\[
\lim_{n\to\infty}n^\theta c_{n,r}(\theta)=-\frac{\theta^3\Gamma(\theta)}2\bigl(g_{r-1}-g_{r-3}\bigr),\qquad 0<\theta<2,\quad \theta\ne1.
\]
At the crossover and beyond,
\[
\lim_{n\to\infty}n^2c_{n,r}(2)=\begin{cases}-8,&r=1,\\-12,&r\ge2,\end{cases}\qquad
\lim_{n\to\infty}n^2c_{n,r}(\theta)=\theta^2(1-\theta),\quad\theta>2.
\]
At \(\theta=1\), \(c_{n,r}(1)<0\) for all admissible \(n,r\); \(\lim n c_{n,r}(1)=-1/2\) for \(r=1,2\), whereas \(\lim n^3c_{n,r}(1)=(3-2r)/2\) for \(r\ge3\).

In particular, for \(0<\theta<1\) the conditional covariance is eventually negative if \(r=1,2\) and eventually **positive if \(r\ge3\)**, despite the strictly positive unconditional covariance. For \(\theta>1\) it is eventually negative for every fixed \(r\). The smallest possible exclusion that restores positive covariance in the subunit Ewens regime is precisely the three giant-cycle sizes \(n,n-1,n-2\).

Additionally, when conditioning only on not being an \(n\)-cycle (\(r=1\)), strict negativity holds for **every \(n\ge3\) and \(\theta>0\)**, not just asymptotically.

## Assumptions and scope
The Ewens distribution assigns a permutation with \(k\) cycles probability proportional to \(\theta^k\). The normalization is \((\theta)_n\), and the exponential cycle-index partition coefficient is \(g_n\). All limits hold for fixed \(r\) and fixed positive \(\theta\), with \(n\to\infty\); no uniformity as \(r\) or \(\theta\) varies is claimed. The exact finite formula uses \(n\ge2r+4\), which makes forbidden giant cycles mutually exclusive. The \(r=1\) strict-sign addendum holds for all \(n\ge3\).

## Proof
For a size-\(k\) permutation, the cycle-index generating function is \(\exp(\theta\sum_{j\ge1}z^j/j)=(1-z)^{-\theta}\); its coefficient is \(g_k\). Under the cutoff \(L=n-r\), write \(a_k=[z^k]\exp(\theta\sum_{j=1}^{L}z^j/j)\). For \(k=n-s\), \(0\le s\le3\), all forbidden cycles have length strictly greater than half of \(k\), so at most one may occur. Marking one such cycle of length \(k-j\) gives the exact subtraction \(a_{n-s}=g_{n-s}-\theta\sum_{j=0}^{r-s-1}g_j/(n-s-j)\). Marking one fixed point, one transposition, and both gives \(\mathbb EF=\theta a_{n-1}/a_n\), \(\mathbb ET=(\theta/2)a_{n-2}/a_n\), \(\mathbb E(FT)=(\theta^2/2)a_{n-3}/a_n\), proving the finite identity.

For the asymptotics, define \(G_k=\sum_{j=0}^{k}g_j\), taking \(G_k=0\) for \(k<0\). For each fixed \(s=0,1,2,3\), since \(g_{n-s}\sim n^{\theta-1}/\Gamma(\theta)\), the relative removed mass is
\[
\frac{g_{n-s}-a_{n-s}}{g_{n-s}}=\theta\Gamma(\theta)n^{-\theta}G_{r-s-1}+o(n^{-\theta}).
\]
Without truncation, direct rising-factorial simplification gives
\[
\operatorname{Cov}(F,T)=\frac{\theta^2(1-\theta)g_{n-1}g_{n-2}}{n(n+\theta-3)g_n^2}=\theta^2(1-\theta)n^{-2}+o(n^{-2}).
\]
In the determinant \(a_na_{n-3}-a_{n-1}a_{n-2}\), its linear relative perturbation is \(\theta\Gamma(\theta)n^{-\theta}(-G_{r-1}-G_{r-4}+G_{r-2}+G_{r-3})\), which telescopes to \(-\theta\Gamma(\theta)n^{-\theta}(g_{r-1}-g_{r-3})\). Quadratic perturbations are \(O(n^{-2\theta})\), and denominator corrections do not affect the stated leading scales. Hence for \(0<\theta<2\) with \(\theta\ne1\) the rare giant-cycle perturbation dominates the baseline; for \(\theta>2\) the baseline dominates; at \(\theta=2\) both contribute, and \(g_j(2)=j+1\) gives the displayed \(-8\) and \(-12\).

For \(0<\theta<1\), \(g_j\) decreases strictly in \(j\), so \(g_{r-1}-g_{r-3}\) is positive at \(r=1,2\) and negative for \(r\ge3\). For \(1<\theta<2\), \(g_j\) increases, giving a negative leading covariance for all \(r\). The other parameter cases follow from their displayed limits.

For \(\theta=1\), \(g_j=1\). Put \(S=\sum_{k=n-r+1}^{n}1/k\) and \(b=1-S=a_n\). For \(r=1,2\), the exact determinant is \(-1/n\). When \(r\ge3\), set \(u_s=\sum_{j=0}^{s-1}1/(n-j)\); then \(a_{n-s}=b+u_s\) for \(s=0,1,2,3\), and the determinant equals
\[
\frac{2b}{n(n-2)}-\frac{2n-1}{n^2(n-1)}.
\]
Because \(b\le1-3/n\), it is bounded above by \(-(3n-4)/(n^2(n-2)(n-1))<0\). Its expansion is \((3-2r)n^{-3}+O(n^{-4})\). Multiplying by \(1/(2a_n^2)\) proves the claimed strict sign and limits at \(\theta=1\).

Finally for \(r=1\), the determinant factors as
\[
c_{n,1}(\theta)=\frac{\theta^2g_{n-3}}{2na_n^2}\left(\frac{2(1-\theta)g_{n-1}}{n-2}-\theta\right).
\]
The bracket is negative for \(\theta\ge1\). For \(0<\theta<1\), use \(g_{n-1}\le\theta\). If \(n\ge4\), the bracket is at most \(-\theta^2\). At \(n=3\), it equals \(-\theta^3\). Thus the strict negative sign holds for all \(n\ge3\).

## Verification
The companion Python standard-library checker (`verification/verify.py`) compares exact factorial coefficients with exhaustively enumerated Ewens permutations in 12 small cases, executes 2,464 exact rational formula/sign checks across cutoffs, confirms 72 exact coefficient telescoping identities, and checks 15 closed-form instances. Its successful output is recorded in `VERIFICATION.md`. The infinite assertions follow from the displayed algebra and asymptotic estimates, not from finite enumeration.

## Relationship to prior work
Betz, Mühlbauer, Schäfer and Zeindler (2020), arXiv:2004.09904v1, derive cycle-index/generating-function machinery for permutations conditioned to lack macroscopic cycles and develop asymptotics for sublinear length cutoffs; the present fixed-distance cutoff \(n-r\) instead excludes only \(r\) extremely large cycle sizes and yields a covariance sign boundary not stated there. Betz, Schäfer and Zeindler (2017), arXiv:1712.04738, analyze random permutations without macroscopic cycles. Betz and Schäfer (2016), arXiv:1605.08383, study asymptotic normality of the total number of cycles under long-cycle exclusions. Gutmann, Mixer and Morrow (2022), arXiv:2201.04181, treat conditioned fixed points and derangements under different conditioning. General cycle-index coefficients already make the finite moments computable; novelty is claimed only for the sharp cutoff-dependent covariance signs and scaling crossover, subject to priority limitations below.

## Limitations
These are fixed-\(r\), fixed-\(\theta\) asymptotics; no uniform onset bound or monotonicity across all finite \(n\) is proved for \(r\ge2\) outside \(\theta=1\). This analysis does not cover cutoffs growing away from \(n\), joint distributions beyond the stated pair, or unconditional correlation strength beyond the explicit comparison. The use of known cycle-index identities means a stronger or earlier uninspected treatment might imply the classification. Historical priority and independent scientific validation remain open.

## References
- V. Betz, J. Mühlbauer, H. Schäfer, D. Zeindler, *Precise asymptotics of longest cycles in random permutations without macroscopic cycles*, arXiv:2004.09904v1 (first submitted 2020-04-21). https://arxiv.org/abs/2004.09904
- V. Betz, H. Schäfer, D. Zeindler, *Random permutations without macroscopic cycles*, arXiv:1712.04738 (2017). https://arxiv.org/abs/1712.04738
- V. Betz, H. Schäfer, *The number of cycles in random permutations without long cycles is asymptotically Gaussian*, arXiv:1605.08383 (2016). https://arxiv.org/abs/1605.08383
- E. Gutmann, G. Mixer, A. Morrow, *Conditional Probability of Derangements and Fixed Points*, arXiv:2201.04181 (2022). https://arxiv.org/abs/2201.04181
