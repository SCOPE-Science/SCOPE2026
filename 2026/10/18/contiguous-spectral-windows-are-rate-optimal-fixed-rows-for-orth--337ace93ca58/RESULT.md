# Contiguous spectral windows are rate-optimal fixed rows for orthogonal-row Kaczmarz

## Finding
For every integer \(d\ge3\), every number \(r\) of active equations with \(2\le r\le d-1\), and every strictly decreasing positive list \(w_1>\cdots>w_d>0\), consider the consistent diagonal system \(Ax=b\) with \(A=\operatorname{diag}(\sqrt{w_1},\ldots,\sqrt{w_d})\). Choose \(d-r\) equations to enforce exactly and perform randomized Kaczmarz on the remaining \(r\) equations, sampling each active row proportionally to its squared norm. The exact minimax expected squared-error ratio at every positive iteration count is attained by enforcing the complement of a **consecutive window** in the sorted row norms. Specifically, put \(J_t=\{t,t+1,\ldots,t+r-1\}\) for \(1\le t\le d-r+1\). Then
\[
\inf_{|J|=r}\sup_{\substack{e_0\ne0\\\operatorname{supp}(e_0)\subseteq J}}
\frac{\mathbb E\|e_k\|_2^2}{\|e_0\|_2^2}
=\left(1-\max_{1\le t\le d-r+1}
\frac{w_{t+r-1}}{\sum_{i=t}^{t+r-1}w_i}\right)^k,
\qquad k\ge1.
\]
Every rate-optimal active set is consecutive when the weights are distinct. Thus one sorted sliding-window scan determines a simultaneously minimax choice for all positive iteration counts.

The row-interpolative-decomposition surrogate that minimizes the residual Frobenius norm instead keeps the \(r\) *smallest* weights. It can be arbitrarily worse in iteration complexity. For \(d=3\), \(r=2\), and \(A_M=\operatorname{diag}(M+1,M,1)\) with integer \(M\ge2\), it keeps the last two coordinates and has exact worst-case one-step factor
\[
\rho_{\mathrm{sur}}(M)=\frac{M^2}{M^2+1}.
\]
The optimal active set is the first two coordinates, with factor
\[
\rho_{\mathrm{opt}}(M)=\frac{(M+1)^2}{(M+1)^2+M^2}.
\]
In particular \(\rho_{\mathrm{sur}}(M)\to1\), \(\rho_{\mathrm{opt}}(M)\to\tfrac12\), and the ratio of the logarithmic convergence exponents \((-\log\rho_{\mathrm{opt}})/(-\log\rho_{\mathrm{sur}})\sim M^2\log2\).

## Assumptions and scope
The rows are one per orthogonal coordinate (diagonal \(d\times d\) matrix), all diagonal entries are strictly positive, the right-hand side is consistent, enforced equations are solved exactly, the remaining rows are sampled independently with fixed probabilities proportional to squared row norms, and each accepted step is an exact orthogonal Kaczmarz projection (relaxation one). The initial error is any nonzero vector supported on the active coordinates; the supremum is taken before random sampling. The result concerns the expected **squared Euclidean error** after any fixed \(k\ge1\), not a samplewise bound or total computational cost including the initial exact constraints. If weights tie, at least one consecutive active set is optimal, but nonconsecutive tied choices may also be optimal.

## Proof
Let \(J\) be any active set of cardinality \(r\) and put \(W_J=\sum_{j\in J}w_j\). The exact row-sampling probabilities are \(p_j=w_j/W_J\) for \(j\in J\). Because rows are orthogonal, sampling row \(j\) sets error coordinate \(j\) to zero and leaves all others unchanged. Independence across steps implies that coordinate \(j\) has survived after \(k\) draws with probability \((1-p_j)^k\), hence
\[
\mathbb E\|e_k\|_2^2=\sum_{j\in J}|(e_0)_j|^2(1-p_j)^k.
\]
The largest ratio over nonzero errors supported on \(J\) is attained by an error supported on a coordinate of smallest sampling probability. Its exact factor is
\[
R_k(J)=\left(1-\frac{\min_{j\in J}w_j}{\sum_{j\in J}w_j}\right)^k.
\]
Thus minimizing \(R_k(J)\) for any \(k\ge1\) is the same as maximizing the smallest weight divided by the total retained weight.

Index rows so that \(w_1>\cdots>w_d\). Fix the largest index \(j=\max J\), corresponding to the minimum retained weight \(w_j\). Since \(|J|=r\), necessarily \(j\ge r\). Of all \(r\)-element sets with largest index \(j\), the unique set with smallest total weight consists of the \(r-1\) indices immediately preceding \(j\), together with \(j\): precisely \(\{j-r+1,\ldots,j\}\). Indeed, replacing any earlier selected index by a missing later index strictly lowers the sum while leaving the minimum unchanged. Hence every optimal active set is one of these contiguous windows. Evaluating the ratio on each window proves the displayed minimax formula for all \(k\).

For the three-mode family, the Frobenius-residual surrogate uniquely removes the first (largest) row and keeps squared weights \(M^2,1\). The candidate windows are \(((M+1)^2,M^2)\) and \((M^2,1)\); keeping the first two is better precisely when \(M^4>(M+1)^2\), which holds for integers \(M\ge2\). Substitution into the exact rate gives the two factors. Finally, \(-\log\rho_{\mathrm{sur}}=\log(1+M^{-2})\sim M^{-2}\), whereas \(-\log\rho_{\mathrm{opt}}\to\log2\). Their exponent ratio therefore grows as claimed. No asymptotic approximation is used in the finite-dimensional formulas.

## Verification
Run `python check_band.py` with Python 3. It enumerates all active subsets for randomly generated strictly ordered spectra in dimensions \(3\) through \(8\), enumerates all draw sequences through four iterations for a concrete four-mode system, and checks the three-mode formulas at several parameters. The recorded local execution passed 1050 exhaustive subset comparisons, 121 exact path-enumeration checks, and five three-mode analytic comparisons. This finite testing is supplementary; the proof applies to every finite dimension and all admissible weights.

## Relationship to prior work
Sun, Qi, Han and Xie (arXiv:2605.29304v1, 28 May 2026) derive subspace-constrained randomized iteration, its row-norm sampling specialization, and a residual-Frobenius surrogate for selecting enforced rows. Their general spectral rate formula supplies the motivation, but the exact all-horizon optimal active-row classification and the diverging surrogate-vs-minimax exponent ratio are additional optimization statements for orthogonal-row systems. Lok and Rebrova (arXiv:2309.04889v2) establish the subspace-constrained randomized Kaczmarz framework, and their later arXiv:2506.09394 paper gives related diagonal-sampling convergence theory for subspace-constrained coordinate descent. Those broader convergence bounds are not being claimed as new. The classification selects rows under the original prescribed norm-proportional sampling rule, rather than optimizing that sampling distribution itself.

## Limitations
This classification is for diagonal systems, which are an exactly tractable benchmark, not for general correlated rows. It does not establish that the ID surrogate is poor on all matrices or for end-to-end time including selecting and solving enforced rows. General purpose algorithms may exploit nontrivial row correlations, approximate pivots, or non-norm-proportional sampling and are outside the result. The possibility of an equivalent spectral-window rule in older literature remains a bibliographic risk; the mathematical claim is not a statement of universal literature uniqueness.

## References
1. Y. Sun, H.-D. Qi, D. Han and J. Xie, *On subspace-constrained preconditioning for randomized iterative methods*, arXiv:2605.29304v1 (first public 28 May 2026), Sections 2–3, especially Section 3.2. https://arxiv.org/abs/2605.29304.
2. J. Lok and E. Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889v2 (2024), Sections 1 and 3. https://arxiv.org/abs/2309.04889.
3. J. Lok and E. Rebrova, *Subspace-constrained randomized coordinate descent for linear systems with good low-rank matrix approximations*, arXiv:2506.09394 (first public June 2025), Sections 1–3. https://arxiv.org/abs/2506.09394.
