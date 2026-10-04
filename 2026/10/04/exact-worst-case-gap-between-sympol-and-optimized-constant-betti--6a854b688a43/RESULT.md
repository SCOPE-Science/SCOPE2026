# Exact worst-case gap between SymPol and optimized constant betting
## Finding
For an integer \(n\ge 1\) and a finite nonnegative vector \(\mathbf e=(e_1,\ldots,e_n)\), define the normalized elementary symmetric means
\[
A_k(\mathbf e)=\frac{1}{\binom nk}\sum_{I\subseteq\{1,\ldots,n\},\ |I|=k}\prod_{i\in I}e_i,
\qquad A_0(\mathbf e)=1.
\]
Write
\[
S_n(\mathbf e)=\max_{0\le k\le n}A_k(\mathbf e)
\]
for the SymPol statistic and
\[
K_n(\mathbf e)=\sup_{0\le\lambda\le1}\prod_{i=1}^n(1-\lambda+\lambda e_i)
\]
for the optimized constant-bet statistic used in the KL-inf construction.

For \(0\le k\le n\), put
\[
b_{n,k}=\binom nk\left(\frac{k}{n}\right)^k
\left(1-\frac{k}{n}\right)^{n-k},
\]
with \(b_{n,0}=b_{n,n}=1\), and let
\[
b_n=\min_{0\le k\le n}b_{n,k}
=b_{n,\lfloor n/2\rfloor}.
\]
Then every finite nonnegative input satisfies the two-sided comparison
\[
K_n(\mathbf e)\le S_n(\mathbf e)\le \frac{1}{b_n}K_n(\mathbf e).
\]
The constant \(1/b_n\) is optimal as a uniform multiplicative factor over all nonnegative inputs. More precisely, if \(k\) is a central index attaining \(b_n\) and \(\mathbf e_L\) has \(k\) coordinates equal to \(L\) and the remaining \(n-k\) coordinates equal to zero, then
\[
\frac{S_n(\mathbf e_L)}{K_n(\mathbf e_L)}\longrightarrow\frac{1}{b_n}
\qquad\text{as }L\to\infty.
\]
Thus the largest possible multiplicative improvement of the capped SymPol p-value over the capped optimized-product p-value is exactly \(1/b_n\) in the supremum sense:
\[
1\le \frac{p_{\mathrm{KL}}(\mathbf e)}{p_{\mathrm{SP}}(\mathbf e)}\le \frac{1}{b_n},
\]
where \(p_{\mathrm{SP}}=\min\{1,S_n^{-1}\}\) and \(p_{\mathrm{KL}}=\min\{1,K_n^{-1}\}\).

The factor is explicit. If \(n=2m\), then
\[
\frac{1}{b_n}=\frac{4^m}{\binom{2m}{m}}.
\]
If \(n=2m+1\), then
\[
\frac{1}{b_n}=
\frac{(2m+1)^{2m+1}}
{\binom{2m+1}{m}m^m(m+1)^{m+1}}.
\]
In both cases Stirling's formula gives
\[
\frac{1}{b_n}\sim\sqrt{\frac{\pi n}{2}}.
\]
Hence the pointwise advantage established for SymPol over optimized constant betting can grow only on the square-root sample-size scale, and that scale is actually attainable.

## Assumptions and scope
The statement is deterministic and applies to every finite nonnegative vector. Statistical validity is inherited from whichever assumptions make the compared statistics valid in a given application. In particular, the motivating SymPol result is valid for co-valid e-variables, whereas the optimized constant-bet statistic is the Wang--Zhao/Gaffke KL-inf statistic considered in the same source.

The theorem compares the two statistics and their reciprocal capped p-values only. It does not claim that either statistic dominates the later Gaffke p-value under independence, does not compare power under a particular alternative distribution, and does not optimize confidence-interval width after inversion.

## Proof
The Bernstein expansion used in the motivating paper gives, for every \(\lambda\in[0,1]\),
\[
\prod_{i=1}^n(1-\lambda+\lambda e_i)
=
\sum_{k=0}^n
\binom nk\lambda^k(1-\lambda)^{n-k}A_k(\mathbf e).
\]
The coefficients are nonnegative and sum to one. Therefore the product is at most \(S_n(\mathbf e)\) for each \(\lambda\), proving \(K_n\le S_n\).

Choose an index \(k_*\) with \(A_{k_*}(\mathbf e)=S_n(\mathbf e)\). Evaluating the same expansion at \(\lambda=k_*/n\) yields
\[
K_n(\mathbf e)
\ge
b_{n,k_*}S_n(\mathbf e)
\ge
b_nS_n(\mathbf e),
\]
which proves \(S_n\le K_n/b_n\).

It remains to locate \(b_n\). Symmetry gives \(b_{n,k}=b_{n,n-k}\). For \(1\le k<n\), direct cancellation gives
\[
\frac{b_{n,k+1}}{b_{n,k}}
=
\frac{(1+1/k)^k}{(1+1/(n-k-1))^{n-k-1}},
\]
with the central odd case interpreted by equality. The sequence \((1+1/r)^r\) is strictly increasing in positive integers \(r\). Hence \(b_{n,k}\) decreases as \(k\) moves from the edge toward the center and then increases symmetrically. Also \(b_{n,1}<b_{n,0}=1\) when \(n>1\). Thus the minimum is attained at the central index or central pair, proving \(b_n=b_{n,\lfloor n/2\rfloor}\).

For sharpness, fix a central \(k\) and let \(\mathbf e_L\) contain \(k\) copies of \(L\) and \(n-k\) zeros. Then
\[
A_j(\mathbf e_L)=
\frac{\binom kj}{\binom nj}L^j
\quad(0\le j\le k),
\qquad
A_j(\mathbf e_L)=0
\quad(j>k).
\]
As \(L\to\infty\), the unique largest order is \(A_k(\mathbf e_L)=L^k/\binom nk\), so \(S_n(\mathbf e_L)/A_k(\mathbf e_L)\to1\). The optimized product is
\[
K_n(\mathbf e_L)
=
\sup_{0\le\lambda\le1}
(1-\lambda+\lambda L)^k(1-\lambda)^{n-k}.
\]
After division by \(A_k(\mathbf e_L)\), the objective converges uniformly on \([0,1]\) to
\[
\binom nk\lambda^k(1-\lambda)^{n-k},
\]
whose maximum is \(b_{n,k}=b_n\) at \(\lambda=k/n\). Therefore \(K_n/A_k\to b_n\), and consequently \(S_n/K_n\to1/b_n\). No smaller uniform constant is possible.

For the capped reciprocal p-values, \(S_n\ge K_n\) gives \(p_{\mathrm{SP}}\le p_{\mathrm{KL}}\). The same three cases \(K_n\ge1\), \(K_n<1<S_n\), and \(S_n\le1\), together with \(S_n\le K_n/b_n\), give \(p_{\mathrm{KL}}/p_{\mathrm{SP}}\le1/b_n\). The sharp family eventually lies in the uncapped regime, so the supremum is again \(1/b_n\).

The closed forms follow by substituting the central index. Stirling's formula for the central binomial mass gives \(b_n\sim\sqrt{2/(\pi n)}\), hence \(1/b_n\sim\sqrt{\pi n/2}\).

## Verification
The deterministic script `verify_sympol_gap.py` checks the Bernstein identity, the central minimizer of \(b_{n,k}\) for a range of sample sizes, the universal lower bound obtained by evaluating the product at a maximizing coefficient's mean parameter, the closed-form even and odd constants, and convergence of the sparse sharpness family toward the stated factor.

The proof of optimality is analytic. Numerical checks support transcription and algebra but are not used as a substitute for the uniform argument.

## Relationship to prior work
Ming, Ramdas, Shen, Wang, and Waudby-Smith introduce the SymPol statistic and prove
\[
K_n(\mathbf e)\le S_n(\mathbf e),
\]
using exactly the Bernstein expansion above. They emphasize that SymPol gives a p-value no larger than the optimized constant-bet KL-inf p-value, but the inspected paper does not quantify the largest possible finite-sample ratio between the two statistics or p-values.

The later paper by the same authors on Gaffke's confidence interval proves that, under independence, the Gaffke p-value is no larger than the SymPol p-value. That is a different comparison: it does not give a reverse multiplicative bound between SymPol and KL-inf, and Gaffke validity requires independence rather than the broader co-valid setting of SymPol.

The proof here uses the standard fact that the \(k\)-th Bernstein basis polynomial has maximum at \(k/n\). The nontrivial statistical content is the exact best uniform factor after restricting the Bernstein coefficients to the normalized elementary-symmetric sequence generated by nonnegative e-value inputs; the sparse family shows that the generic single-coefficient obstruction remains asymptotically realizable inside this restricted cone.

Targeted semantic and statement-level searches did not reveal the exact sharp factor \(1/b_n\), its central-binomial form, or the resulting square-root worst-case p-value gap for SymPol versus optimized constant betting. This is not a proof that no equivalent unindexed observation exists.

## Limitations
The factor is a worst-case deterministic envelope. Typical ratios under common statistical models can be much smaller, and the theorem does not assert a power ratio of the same size. Sharpness is approached along sparse vectors with diverging coordinates; no claim is made that such vectors are typical under a null or alternative model.

The result does not compare SymPol with every valid e-to-p merger. In particular, under independence the Gaffke p-value can be smaller than SymPol. The result's main role is to give an exact finite-sample price-of-optimization comparison for the two statistics already linked by the motivating paper.

## References
1. J. Ming, A. Ramdas, Y. Shen, R. Wang, and I. Waudby-Smith, “Combining e-values using demi-supermartingales,” arXiv:2603.10329, first posted 2026-03-11, current version 2026-08-03.
2. J. Ming, A. Ramdas, Y. Shen, R. Wang, and I. Waudby-Smith, “Gaffke's confidence interval for the mean of bounded data is inadmissible but asymptotically efficient,” arXiv:2607.18661, first posted 2026-07-21.
