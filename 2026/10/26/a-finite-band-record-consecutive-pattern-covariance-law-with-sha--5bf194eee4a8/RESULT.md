# A finite-band record–consecutive-pattern covariance law with sharp asymptotic extrema

## Finding
For each uniformly random permutation of length \(n\), the cross-covariance between every left-to-right record indicator and every occurrence indicator of a fixed consecutive pattern \(\sigma\) of length \(k\) vanishes unless the record's position lies *inside* the pattern window. Every nonzero entry is an explicit beta-order-statistic moment. Consequently, for fixed \(k\), the covariance between the total number \(T_n\) of upper records and the number \(N_{\sigma,n}\) of consecutive occurrences has an exact finite sum and converges to
\[
\boxed{\lim_{n\to\infty}\operatorname{Cov}(T_n,N_{\sigma,n})=\frac{1}{k!}\left(\sum_{\substack{b\in M_\sigma\\b<k}}\frac{k}{k-b}-(k-1)\right),}
\]
where \(M_\sigma\) is the set of values that appear as left-to-right maxima of \(\sigma\). This constant is minimal, \(-(k-1)/k!\), exactly for patterns starting with the maximum \(k\), and maximal, \([kH_{k-1}-(k-1)]/k!\), uniquely for the increasing pattern.

For \(k=3\), in order \(123,132,213,231,312,321\), the exact covariance vector for \(n\ge3\) is
\[
\left(\frac{(n-2)(5n-1)}{12n(n-1)},\;-\frac{(n-5)(n-2)}{12n(n-1)},\;\frac{(n-2)^2}{6n(n-1)},\;\frac{(n-2)^2}{6n(n-1)},\;-\frac{(n-2)(2n-1)}{6n(n-1)},\;-\frac{(n-2)(2n-1)}{6n(n-1)}\right).
\]
Thus the \(132\)-pattern covariance is positive for \(n=3,4\), zero for \(n=5\), and negative for every \(n\ge6\), despite all six pattern counts having the same expectation.

## Assumptions and scope
Fix integers \(n\ge k\ge2\), and sample a uniform permutation \(\pi\in S_n\). Equivalently, \(\pi\) is the rank ordering of independent continuous uniform variables \(U_1,\dots,U_n\). Define \(R_i=\mathbf1\{U_i>\max_{h<i}U_h\}\), with \(R_1=1\), and \(T_n=\sum_{i=1}^n R_i\) for the total. Let \(\sigma=(\sigma_1,\dots,\sigma_k)\in S_k\) and let \(P_{\sigma,j}\) indicate that the relative order of \((U_j,\dots,U_{j+k-1})\) equals \(\sigma\), for \(1\le j\le n-k+1\). Then \(N_{\sigma,n}=\sum_jP_{\sigma,j}\).

Use the rising factorial \((a)^{\overline h}=\prod_{s=0}^{h-1}(a+s)\), with empty product one, and \(H_r=\sum_{s=1}^r1/s\), with \(H_0=0\). The indicator \(\eta_{\sigma,r}\) is one when \(\sigma_r=\max(\sigma_1,\dots,\sigma_r)\) and zero otherwise.

The exact positional covariance law for every \(1\le i\le n\) is
\[
\operatorname{Cov}(R_i,P_{\sigma,j})=
\begin{cases}
\displaystyle\frac1{k!}\left[\eta_{\sigma,r}\frac{(\sigma_r)^{\overline{j-1}}}{(k+1)^{\overline{j-1}}}-\frac1{j+r-1}\right],&i=j+r-1,\ 1\le r\le k,\\
0,&i\notin\{j,\dots,j+k-1\}.
\end{cases}
\]
The probability law is independent of the choice of continuous parent distribution, provided observations are independent and identically distributed and ties have probability zero.

## Proof
**1. Locality.** If \(i<j\), \(R_i\) is measurable with respect to samples strictly preceding the indicated pattern block and is independent of its internal order. If \(i>j+k-1\), the record event is invariant under permutations of earlier samples; because their relative orders are uniformly random conditional on their unordered values, conditioning on the internal ranking of the \(k\) samples in the pattern block does not alter \(\Pr(R_i=1)=1/i\). Thus both exterior covariances vanish, not merely asymptotically.

**2. Interior conditional probability.** Fix \(i=j+r-1\). Conditional on \(P_{\sigma,j}=1\), the value \(U_i\) is the \(\sigma_r\)-th order statistic of \(k\) independent uniforms. For it to be a record, it must exceed the other \(r-1\) preceding values within that block, which is equivalent to \(\eta_{\sigma,r}=1\); and it must exceed all \(j-1\) observations before the block. Since those earlier observations remain independent, the conditional record probability is \(\eta_{\sigma,r}\mathbb E[U_i^{j-1}\mid P_{\sigma,j}=1]\). The beta law of that order statistic has parameters \((\sigma_r,k+1-\sigma_r)\), so its moment is exactly \((\sigma_r)^{\overline{j-1}}/(k+1)^{\overline{j-1}}\). Subtracting \(\Pr(R_i=1)\Pr(P_{\sigma,j}=1)=1/[(j+r-1)k!]\) proves the full cross-covariance kernel.

**3. The limiting covariance.** By summing the kernel over all record positions and windows, with \(m=n-k+1\),
\[
\operatorname{Cov}(T_n,N_{\sigma,n})
=\frac1{k!}\sum_{j=1}^{m}\left[\sum_{r:\eta_{\sigma,r}=1}\frac{(\sigma_r)^{\overline{j-1}}}{(k+1)^{\overline{j-1}}}-\sum_{r=1}^k\frac1{j+r-1}\right].
\]
The global maximum \(k\) occurs at one record position within \(\sigma\). Its moment equals \(k/(j+k-1)\). For every other record value \(b<k\), summing its moments over \(j\ge1\) gives
\[
\sum_{j=1}^{\infty}\frac{(b)^{\overline{j-1}}}{(k+1)^{\overline{j-1}}}
=\mathbb E\left[\frac1{1-B_{b,k}}\right]=\frac{k}{k-b},
\]
where \(B_{b,k}\) has the beta \((b,k+1-b)\) law. The maximum-record term cancels the harmonic divergence of the \(k\) record baselines, leaving
\[
\lim_{m\to\infty}\left[k\sum_{j=1}^m\frac1{j+k-1}-\sum_{r=1}^k\sum_{j=1}^m\frac1{j+r-1}\right]=\sum_{r=0}^{k-1}H_r-kH_{k-1}=-(k-1).
\]
This proves the claimed finite constant; the fixed-\(k\) error is \(O_k(1/n)\), since the uncancelled tail consists of terms \(O_k(j^{-2})\).

**4. Sharp extremizers.** The limiting constant is monotone strictly increasing in the set of proper prefix-record values. That set is empty exactly when \(\sigma_1=k\), giving the minimum; the full set \(\{1,\dots,k-1\}\) is possible only for \(\sigma=12\cdots k\), giving the unique maximum.

**5. Length three and sign reversal.** Substitute all six length-three patterns into the finite sum in step 3, use the identities \(\mathbb E[B_{b,3}^{j-1}]=6/[j(j+1)(j+2)]\) for \(b=1\), \(6/[(j+1)(j+2)]\) for \(b=2\), and \(3/(j+2)\) for \(b=3\), and telescope. The stated rational vector follows, and the \(132\) sign change follows from its exact factor \(-(n-5)(n-2)\).

## Verification
An independent exhaustive finite-sample program, `verify.py`, enumerates each permutation of length \(2\) through \(8\), checking the total-record versus each consecutive-pattern covariance for \(2\le k\le\min(5,n)\). For lengths through \(7\), it also checks every record-position/pattern-window covariance, including all predicted zeros outside the block. It verifies the sharp limiting extremizers for all tested pattern lengths. The program uses exact rational arithmetic and reports 7,472 passed assertions. Finite enumeration corroborates the formulas but the proofs above supply the all-size claims.

## Relationship to prior work
Borga, arXiv:2003.08426 (originally public on 18 March 2020), establishes limit theorems for consecutive patterns in permutation classes encoded by generating trees. It does not supply a covariance kernel between global record indicators and consecutive patterns in unrestricted uniform permutations. Crane and DeSalvo, arXiv:1509.07941, study Poisson approximations and avoidance for pattern occurrences, without the stated record-pattern pairing. Even-Zohar, arXiv:1811.07883, decomposes *classical (not consecutive)* permutation-pattern densities by symmetric-group representations, and its covariance analysis is not a result about left-to-right records. Related published results on fixed-point–descent locality and cycle-count–pattern covariance concern distinct non-equivalent statistics: marginal equidistribution of cycles and records does not establish their joint laws with consecutive patterns. The sharp limiting profile and extremizers follow here from the explicitly reconstructed kernel, not merely from pattern-count marginals.

## Limitations
The result concerns uniform unrestricted random permutations and fixed pattern length when taking \(n\to\infty\), not arbitrary Mallows parameters, growing pattern lengths, or conditioned permutation classes. Bounded covariance alone does not establish asymptotic independence of the full statistics. The originality assessment is based on available primary texts and research records; older equivalent record-pattern identities may exist and historical priority has not been independently certified. No independent mathematical audit was performed.

## References
1. J. Borga, *Asymptotic normality of consecutive patterns in permutations encoded by generating trees with one-dimensional labels*, arXiv:2003.08426 (initial public version: 18 March 2020), §§1–3.
2. H. Crane and S. DeSalvo, *Pattern avoidance for random permutations*, arXiv:1509.07941 (initial public version: September 2015), §§3 and 7.
3. C. Even-Zohar, *Patterns in random permutations*, arXiv:1811.07883 (2018), §§1–4.
