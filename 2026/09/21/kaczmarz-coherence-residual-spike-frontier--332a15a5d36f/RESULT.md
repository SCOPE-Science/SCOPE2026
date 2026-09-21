# Sharp coherence frontier for residual spikes in maximal-distance Kaczmarz

## Statement

Let \(A\in\mathbb R^{m\times n}\) have no zero rows. Write
\[
D=\operatorname{diag}(\|a_1\|_2,\ldots,\|a_m\|_2),\qquad
B=D^{-1}A,
\]
so the rows \(b_i^T\) of \(B\) have unit Euclidean norm. For a current iterate \(x\), define the scale-invariant normalized residual
\[
q=D^{-1}(Ax-b).
\]
The maximal-distance (maximal weighted residual) Kaczmarz step chooses
\[
i\in\operatorname*{argmax}_{1\le j\le m}|q_j|
\]
and performs
\[
x_+=x-q_i b_i.
\]
Let the row coherence be
\[
\mu=\max_{j\ne k}|b_j^Tb_k|,
\qquad 0\le\mu<1.
\]
Then every such step satisfies the sharp dimension/coherence bound
\[
\boxed{\frac{\|q_+\|_2}{\|q\|_2}\le \Gamma_m(\mu)},
\]
where, with \(d=m-1\),
\[
\boxed{
\Gamma_m(\mu)^2=
\begin{cases}
\dfrac{d(1+\mu)^2}{d+1},&0\le\mu\le d^{-1},\\[6pt]
1+d\mu^2,&d^{-1}\le\mu<1.
\end{cases}}
\]
The constant is globally sharp as a universal bound over matrices of row coherence at most \(\mu\). In the first branch exact equality can occur with a tied maximal residual; with a unique maximizer the same value is a supremum. In the second branch equality is attained with a unique maximizer whenever \(\mu>d^{-1}\).

Consequently, the normalized residual is guaranteed to be nonincreasing at every maximal-distance Kaczmarz step for every matrix with row coherence at most \(\mu\) if and only if
\[
\boxed{\mu\le \mu_m^*:=\sqrt{\frac{m}{m-1}}-1.}
\]
For every \(\mu>\mu_m^*\), there is a square nonsingular system and a current iterate with a unique maximal normalized residual whose next Kaczmarz step strictly increases \(\|q\|_2\). Thus the threshold is sharp, not merely sufficient.

As \(m\to\infty\),
\[
\mu_m^*=\frac{1}{2(m-1)}+O(m^{-2}).
\]
At the other extreme, \(\Gamma_m(\mu)\to\sqrt m\) as \(\mu\uparrow1\): a single greedy projection can make the total normalized residual almost \(\sqrt m\) times larger even though, for a consistent system, the Euclidean solution error always decreases under an orthogonal Kaczmarz projection.

## Proof

The normalized residual update is exact:
\[
(q_+)_j=q_j-q_i b_j^Tb_i,
\qquad (q_+)_i=0.
\]
If \(q\ne0\), maximality gives \(|q_j/q_i|\le1\). Put
\[
s_j=q_j/q_i\quad(j\ne i),\qquad c_j=b_j^Tb_i,
\]
and \(y=\|s\|_2\). Then \(0\le y\le\sqrt d\), \(|c_j|\le\mu\), and
\[
\frac{\|q_+\|_2^2}{\|q\|_2^2}
=\frac{\|s-c\|_2^2}{1+\|s\|_2^2}.
\]
Using \(\|s\|_1\le\sqrt d\,\|s\|_2\),
\[
\|s-c\|_2^2
\le \sum_{j=1}^{d}(|s_j|+\mu)^2
\le (y+\mu\sqrt d)^2.
\]
Hence it remains to maximize
\[
F(y)=\frac{(y+\mu\sqrt d)^2}{1+y^2},
\qquad 0\le y\le\sqrt d.
\]
For \(\mu>0\),
\[
F'(y)=\frac{2(y+\mu\sqrt d)(1-\mu\sqrt d\,y)}{(1+y^2)^2}.
\]
If \(\mu\le d^{-1}\), the stationary point lies at or beyond the right endpoint and the maximum is
\[
F(\sqrt d)=\frac{d(1+\mu)^2}{d+1}.
\]
If \(\mu\ge d^{-1}\), the maximum is attained at \(y=(\mu\sqrt d)^{-1}\), giving
\[
F=1+d\mu^2.
\]
The case \(\mu=0\) follows directly by continuity or by the same endpoint calculation.

### Sharpness construction

For any \(0\le\mu<1\), take the square unit-row matrix
\[
b_1=e_1,
\qquad
b_j=-\mu e_1+\sqrt{1-\mu^2}\,e_j,
\quad j=2,\ldots,m.
\]
It is nonsingular. Its off-diagonal row inner products are \(-\mu\) between row 1 and every other row and \(\mu^2\) among rows \(2,\ldots,m\), so its row coherence is exactly \(\mu\).

Choose a normalized residual state
\[
q=(1,t,\ldots,t)^T.
\]
Because \(B\) is nonsingular, this state is realized by the consistent homogeneous system \(Bx=0\) at \(x=B^{-1}q\). If row 1 is selected, then
\[
\frac{\|q_+\|_2^2}{\|q\|_2^2}
=\frac{d(t+\mu)^2}{1+dt^2}.
\]
For \(\mu\le d^{-1}\), choosing \(t=1\) gives equality in the first branch. Taking \(t<1\) and letting \(t\uparrow1\) makes row 1 the unique maximizer and approaches the same constant. For \(\mu\ge d^{-1}\), choosing
\[
t=(d\mu)^{-1}\le1
\]
gives exact equality in the second branch; it is a unique maximizer when \(\mu>d^{-1}\).

Finally, the coherence threshold is obtained in the first branch by solving \(\Gamma_m(\mu)\le1\):
\[
d(1+\mu)^2\le d+1
\iff
\mu\le\sqrt{1+d^{-1}}-1.
\]
This value is strictly below \(d^{-1}\), so no second-branch case is missed. The sharp family above proves necessity.

## Approximate maximal-residual oracle

The same calculation gives an exact extension for a \(\theta\)-approximate selector, \(0<\theta\le1\), that is only required to return an index satisfying
\[
|q_i|\ge\theta\|q\|_\infty.
\]
The sharp universal factor becomes
\[
\boxed{
\Gamma_{m,\theta}(\mu)^2=
\begin{cases}
\dfrac{d(\theta^{-1}+\mu)^2}{1+d\theta^{-2}},
&0\le\mu\le\theta/d,\\[6pt]
1+d\mu^2,&\theta/d\le\mu<1,
\end{cases}}
\]
and the exact universal monotonicity threshold is
\[
\boxed{
\mu\le
\sqrt{\theta^{-2}+\frac1{m-1}}-\theta^{-1}.
}
\]
The same matrix family is sharp, with \(t=\theta^{-1}\) in the first branch and \(t=(d\mu)^{-1}\) in the second.

## Equivalent Gauss--Southwell interpretation

When \(B\) has full row rank, let \(G=BB^T\), a positive-definite correlation matrix. Kaczmarz applied in the row space is equivalent to exact coordinate minimization of the quadratic
\[
\phi(y)=\tfrac12y^TGy-b^Ty
\]
under the Gauss--Southwell rule. The normalized residual \(q\) is precisely the gradient \(Gy-b\). The theorem therefore also gives a sharp one-coordinate Euclidean gradient-norm amplification frontier for exact Gauss--Southwell coordinate descent when the Hessian is a correlation matrix with off-diagonal entries bounded by \(\mu\).

This is deliberately a one-step gradient/residual statement. Standard Gauss--Southwell analyses establish objective or energy convergence; those facts do not imply monotonicity of the full Euclidean gradient or residual norm.

## Relation to prior work

Maximal-distance relaxation goes back at least to the 1954 Agmon and Motzkin--Schoenberg relaxation literature. Modern maximal weighted residual Kaczmarz analyses, including Du--Gao (2019), derive convergence estimates in solution error, while modern Gauss--Southwell work such as Nutini et al. (2015) analyzes objective decrease and convergence rates. These guarantees coexist with the present phenomenon because one orthogonal row projection can reduce solution error while increasing several unselected residual components.

Recent Kaczmarz literature explicitly describes a residual-entry "seesaw effect": selecting a large residual can increase smaller residual entries, motivating double-greedy and related variants. The present result gives, for the single-row maximal-distance rule, an exact total-normalized-residual amplification factor, its sharp coherence threshold for complete stepwise residual monotonicity, and the corresponding approximate-oracle frontier.

To the best of our knowledge, searches of maximal weighted residual Kaczmarz, Kaczmarz--Motzkin, remotest-set control, Gauss--Southwell coordinate relaxation, row coherence/correlation, residual monotonicity, and the recent seesaw-effect literature did not locate these exact formulas or the sharp threshold \(\sqrt{m/(m-1)}-1\). This is an originality assessment, not a proof of absence.

## Computational model and limitations

- Exact arithmetic and one standard Kaczmarz orthogonal projection are assumed.
- Row norms are treated as available, and the exact rule assumes access to the current normalized residual maximum; the \(\theta\)-version models an approximate selection oracle.
- The norm controlled is \(\|D^{-1}(Ax-b)\|_2\). For unit-row systems this is the ordinary Euclidean residual norm. No analogous claim for an arbitrarily row-scaled raw residual is made.
- The upper bounds do not require consistency or full row rank. The sharp witnesses are square nonsingular consistent systems.
- The theorem concerns one-step worst-case residual behavior, not iteration complexity, finite-precision stability, asynchronous implementations, block projections, or noisy/inconsistent convergence.
- Pairwise coherence is intentionally coarse. Matrix-specific correlation structure can yield much smaller amplification.
- The Du--Gao publisher source inspected here exposes the abstract and introductory material but not the complete theorem text in a convenient HTML representation; later literature restates its MWRK convergence estimate as a solution-error estimate. Older relaxation and coordinate-relaxation literature is broad, so historical-equivalence risk remains.

## Reproducibility

`artifacts/verify.py` checks the sharp family, the threshold crossing, the approximate-oracle extension, and 6,000 random unit-row instances. `artifacts/verification.txt` records the deterministic output, including software versions and seed. Numerical checks support the proof but are not used as proof.

## References

1. S. Agmon, *The Relaxation Method for Linear Inequalities*, Canadian Journal of Mathematics 6 (1954), 382--392. https://doi.org/10.4153/CJM-1954-037-2
2. T. S. Motzkin and I. J. Schoenberg, *The Relaxation Method for Linear Inequalities*, Canadian Journal of Mathematics 6 (1954), 393--404. https://doi.org/10.4153/CJM-1954-038-x
3. J. Nutini, M. Schmidt, I. Laradji, M. P. Friedlander, H. Koepke, *Coordinate Descent Converges Faster with the Gauss--Southwell Rule Than Random Selection*, ICML 2015. https://arxiv.org/abs/1506.00552
4. C. Popa, *A note on Kaczmarz algorithm with remotest set control sequence*, 2017/2018. https://arxiv.org/abs/1702.02729
5. K. Du and H. Gao, *A New Theoretical Estimate for the Convergence Rate of the Maximal Weighted Residual Kaczmarz Algorithm*, Numer. Math. Theory Methods Appl. 12 (2019), 627--639. https://doi.org/10.4208/nmtma.OA-2018-0039
6. J. Haddock and A. Ma, *Greed Works: An Improved Analysis of Sampling Kaczmarz--Motzkin*, SIAM J. Math. Data Sci. 3 (2021), 342--368. https://arxiv.org/abs/1912.03544
7. R.-R. Li and H. Liu, *The global block Kaczmarz method using double greedy strategy*, Numerical Algorithms 101 (2026), 1949--1963. https://doi.org/10.1007/s11075-025-02069-x
8. A. Panchal and R. Behera, *RGDBEK: Randomized Greedy Double Block Extended Kaczmarz Algorithm With Hybrid Parallel Implementation and Applications*, Numerical Linear Algebra with Applications 33 (2026), e70102. https://doi.org/10.1002/nla.70102
