# Exact stationary bias and spectral inertia of residual-power Kaczmarz on inconsistent scalar systems

## Finding

Residual-weighted Kaczmarz is often motivated by rapid progress toward a solution of a consistent system. On an inconsistent system, repeated exact projection onto a sampled equation need not approach its least-squares minimizer. The following theorem gives the complete invariant law, convergence/periodicity classification, a finite-rank spectral structure for all even integer powers, and the sharp mean-bias/risk consequences for squared-residual sampling.

**Theorem.** Let \(m\ge2\), choose real values \(b_1,\ldots,b_m\), at least two distinct, and fix an integer \(r\ge1\) and \(\varepsilon\ge0\). Consider the normalized scalar equations \(x=b_i\) with full-step projection. From any real \(x_0\), sample row \(j\) with conditional probability
\[
\Pr(I_k=j\mid x_k)=\frac{\varepsilon+|x_k-b_j|^{2r}}{\sum_{h=1}^m[\varepsilon+|x_k-b_h|^{2r}]},
\qquad x_{k+1}=b_j.
\]
Set \(W_{ij}=\varepsilon+(b_i-b_j)^{2r}\), \(d_i=\sum_jW_{ij}\), and \(D=\operatorname{diag}(d_1,\ldots,d_m)\).

1. The row-index chain, after the first projection, has transition matrix \(P=D^{-1}W\), is irreducible and reversible, and has unique stationary vector \(\pi_i=d_i/\sum_jd_j\). It is aperiodic if and only if \(\varepsilon>0\) or at least three distinct observations occur. Otherwise it has exact period two; in every case its Cesàro distributions converge to \(\pi\).
2. If at least \(2r+1\) of the observations are pairwise distinct, then \(\operatorname{rank}P=2r+1\), and its numbers of strictly positive and negative eigenvalues are, respectively,
\[
\left(r+\mathbf{1}_{r\text{ even}},\quad r+\mathbf{1}_{r\text{ odd}}\right).
\]
All remaining \(m-2r-1\) eigenvalues vanish. In particular, under at least three distinct observations, squared-residual weights give precisely one positive eigenvalue (the stationary eigenvalue), with two negative eigenvalues; under at least five distinct observations, fourth-power weights give three positive and two negative eigenvalues. Consequently the fourth-power sampler has two positive nonstationary relaxation modes which cannot occur under squared-residual weights.
3. For squared-residual sampling \(r=1\), let \(\bar b=m^{-1}\sum_i b_i\) and \(\mu_j=m^{-1}\sum_i(b_i-\bar b)^j\). Then \(\mu_2>0\), and under the stationary law
\[
\mathbb E_\pi[X]=\bar b+\frac{\mu_3}{\varepsilon+2\mu_2},
\qquad
\mathbb E_\pi[(X-\bar b)^2]=\mu_2+\frac{\mu_4-\mu_2^2}{\varepsilon+2\mu_2}\ge\mu_2.
\]
Equality in the last inequality holds exactly when all absolute deviations \(|b_i-\bar b|\) are equal; otherwise residual weighting **strictly increases** the stationary least-squares objective over iid uniform full projections.
For fixed \(m\), \(\mu_2>0\) and \(\varepsilon\ge0\), the exact maximal possible stationary mean bias is
\[
\max |\mathbb E_\pi[X]-\bar b|=
\frac{m-2}{\sqrt{m-1}}\frac{\mu_2^{3/2}}{\varepsilon+2\mu_2}.
\]
For \(m>2\), the maximizers are exactly the two-level samples consisting of one outlier and \(m-1\) equal values, up to permutation, affine translation, and nonzero scaling. For \(m=2\), the bias always vanishes. At \(\varepsilon=0\), the stationary probability of the one outlier is exactly \(1/2\), for every \(m\ge2\), whereas its uniform row-sampling probability is \(1/m\).

## Assumptions and scope

The sampling expression is defined because at least two distinct values make its denominator positive for every real iterate, even when \(\varepsilon=0\). The projection uses **unit row coefficients** and exact full steps: at every iteration the chosen equation is satisfied exactly. Row **indices** are states, so repeated right-hand sides remain distinct states; the displayed stationary law aggregates correctly to observed-value probabilities. For \(\varepsilon>0\) this is a positive-floor variant, while \(\varepsilon=0\) is the original residual-power rule. The least-squares objective is \(F(x)=m^{-1}\sum_i(x-b_i)^2\), minimized uniquely at \(\bar b\). No claims concern higher-dimensional equations, partial relaxation, finite-precision arithmetic, or consistency-preserving variants.

## Proof

**Stationarity and periods.** After one full projection, \(x_k=b_{I_{k-1}}\); consequently the next-index law is precisely \(P_{ij}=W_{ij}/d_i\). Symmetry of the powers gives \(W_{ij}=W_{ji}\), and therefore detailed balance \(\pi_i P_{ij}=W_{ij}/\sum_h d_h=\pi_j P_{ji}\). Each \(d_i>0\). If \(\varepsilon>0\), every transition is strictly positive. If \(\varepsilon=0\), every index connects directly to indices having a different right-hand side; with at least two different values the graph is connected. With exactly two values it is complete bipartite (allowing duplicate labels) and hence has period two. With at least three different values it contains a triangle; connectivity and the available two-step return imply period one. Finite irreducible Markov-chain theory proves uniqueness, convergence when aperiodic, and Cesàro convergence in all cases.

**Full spectral classification.** Write \(s=2r\) and set \(V_{ia}=b_i^a\) for \(0\le a\le s\). The binomial expansion gives the exact matrix factorization
\[
W=VCV^{\mathsf T},\qquad C_{ab}=\mathbf{1}_{a=b=0}\varepsilon+
\mathbf{1}_{a+b=s}(-1)^a\binom{s}{a}.
\]
If at least \(s+1\) values are distinct, \(V\) has full column rank by the Vandermonde determinant. The matrix \(C\) is nonsingular: for each \(a<r\), the pair of coordinates \(a,s-a\) contributes a symmetric off-diagonal two-dimensional block with one positive and one negative eigenvalue; the exceptional pair \(0,s\) has block \(\begin{psmallmatrix}\varepsilon&1\\1&0\end{psmallmatrix}\), also of inertia \((1,1)\), irrespective of \(\varepsilon\). The single central coordinate \(a=r\) contributes the sign of \((-1)^r\binom{2r}{r}\). Thus \(C\) has \(r+\mathbf{1}_{r\text{ even}}\) positive and \(r+\mathbf{1}_{r\text{ odd}}\) negative eigenvalues. Completing the columns of \(V\) to an invertible basis and invoking Sylvester's inertia law gives the same positive and negative counts for \(W\) and \(m-s-1\) zeros. Because \(P\) is similar to the symmetric \(D^{-1/2}WD^{-1/2}\), which is congruent to \(W\), their real eigenvalue sign counts agree. Irreducibility makes eigenvalue \(1\) simple. Hence for \(r=1\) it is the *only* positive eigenvalue; for \(r=2\) two other positive eigenvalues are necessarily present.

**Stationary moments and risk.** Write \(y_i=b_i-\bar b\). For \(r=1\), expansion of the row-sum gives
\[
d_i=m(\varepsilon+\mu_2+y_i^2),\qquad
\sum_i d_i=m^2(\varepsilon+2\mu_2).
\]
Hence \(\pi_i=(\varepsilon+\mu_2+y_i^2)/(m(\varepsilon+2\mu_2))\). The identities \(m^{-1}\sum_i y_i=0\), \(m^{-1}\sum_i y_i^2=\mu_2\) immediately yield the displayed stationary mean and squared-error formulas. By Cauchy–Schwarz, \(\mu_4\ge\mu_2^2\), with equality precisely when the nonnegative values \(y_i^2\) are all equal. IID uniform full projection has next-step law uniform and squared-error risk \(\mu_2\), so the comparison is exact rather than asymptotic in an error-bound constant.

**Sharpness of the stationary bias.** Fix \(\sum_i y_i=0\) and \(\sum_i y_i^2=m\mu_2\) with \(\mu_2>0\); this is a compact sphere in the mean-zero hyperplane. At an extremum of \(\sum_i y_i^3\), the constraints have linearly independent gradients because not all \(y_i\) coincide. Lagrange multipliers therefore imply each \(y_i\) solves the *same quadratic* \(3y_i^2=\lambda+2\gamma y_i\). Unless all values coincide (excluded by positive variance), there are exactly two distinct levels. If \(k\) values equal the positive level and the remaining \(m-k\) equal the negative level, normalization yields
\[
\frac{|\mu_3|}{\mu_2^{3/2}}=
\frac{|m-2k|}{\sqrt{k(m-k)}},\qquad 1\le k\le m-1.
\]
This strictly decreases as \(k\) goes from \(1\) to \(\lfloor m/2\rfloor\), so its maximum is \((m-2)/\sqrt{m-1}\), attained exactly for \(k=1\) or \(m-1\). For \(m=2\) the cubic central moment is identically zero. Finally, choosing \(b_1=\cdots=b_{m-1}=0\), \(b_m=T\ne0\), and \(\varepsilon=0\) yields cross-class row-sum balance: the \(m-1\) repeated points together have total degree \((m-1)|T|^{2r}\), equal to the outlier degree, so each class has stationary mass exactly one-half, for every positive integer \(r\).

## Verification

The companion `verify.py` uses exact rational arithmetic to reconstruct the complete transition matrix, reversibility, binomial/Vandermonde factorization, and the \(r=1\) stationary moment and risk identities. It checked 12,006 finite instances covering powers two, four, and six and floors zero, one-seventh, and two, plus 54 exact two-level outlier checks. This is only a finite cross-check; the general proof is the algebraic argument above.

Run `python verify.py` with Python 3. It uses only the Python standard library.

## Relationship to prior work

Steinerberger's residual-power weighted Kaczmarz sampler is the defining input; its results address convergence for consistent systems and identify inconsistent systems as an extension question. The present statement treats its exact full-projection dynamics on the inconsistent one-dimensional unit-row test family. Sparse weighted randomized Kaczmarz literature gives noisy/inconsistent error bounds for distinct algorithms, not this invariant-law/rank/inertia/sharp-risk classification. The detailed-balance step is the standard reversible-random-walk degree argument, and the inertia proof uses the classical Vandermonde factorization and Sylvester's law. Known negative-type properties of squared Euclidean distance matrices explain why the nonstationary squared-residual modes are negative; the fourth-power positive-mode transition and the sampling-specific sharp stationary distortion require the indicated additional calculations. The claim is the integrated exact boundary behavior of this concrete residual-driven algorithm, not invention of reversibility or matrix-inertia theory.

## Limitations

These are finite-state stationary laws and exact spectral signs, not upper bounds on all transient trajectories. In the two-value zero-floor case the stepwise distributions alternate; stationary expectations are Cesàro limits rather than ordinary time-step limits. Although stationary bias is sharp for a fixed dataset size and variance, no universal rate of convergence independent of data separation is claimed. The \(\varepsilon>0\) case explicitly modifies the original zero-floor sampler. Because the algorithm completely projects to one selected scalar equation at every step, the phenomenon does not assert stationary behavior of under-relaxed, averaged, extended, or multi-dimensional Kaczmarz methods. Independent external review is not claimed.

## References

1. S. Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, arXiv:2007.02910v1, first posted 2020-07-06. https://arxiv.org/abs/2007.02910
2. Z. Zhang et al., *A Weighted Randomized Sparse Kaczmarz Method for Solving Linear Systems*, arXiv:2306.06813v1. https://arxiv.org/abs/2306.06813
3. E. Bogomolny, O. Bohigas, C. Schmit, *Spectral properties of distance matrices*, arXiv:nlin/0301044v1. https://arxiv.org/abs/nlin/0301044
4. Standard results invoked: detailed balance and finite irreducible Markov chains; Vandermonde determinants; Sylvester's law of inertia; elementary Lagrange-multiplier theory.
