# Sharp latent-budget escape law for one-zero ReLU matrix completion

## Finding
Consider the positive-one-zero family
\[
X=\begin{pmatrix} A&u\\v^{\mathsf T}&0\end{pmatrix},
\]
where \(A\in\mathbb R_{>0}^{2\times2}\) has rank one and \(u,v\in\mathbb R_{>0}^{2}\). Write
\[
\gamma=v^{\mathsf T}\operatorname{adj}(A)u,
\qquad L=\|A\|_F^2>0.
\]
For a latent-entry budget \(B\ge0\), define the squared rectified rank-two approximation error
\[
E(B)=\inf_{\substack{Z\in\mathbb R^{3\times3},\;\operatorname{rank}Z\le2\\ -B\le Z_{33}\le0}}
\|X-\max(0,Z)\|_F^2,
\]
where the maximum is entrywise. The following is a complete dichotomy on this natural rank-one leading-block stratum.

**Exactness class.** If \(\gamma=0\), then \(X\) itself has rank two, its exact ReLU-rank is two, and \(E(B)=0\) for every \(B\ge0\).

**Escape class.** If \(\gamma\ne0\), then the exact ReLU-rank of \(X\) is three, while the unrestricted rank-two rectified approximation infimum equals zero and is not attained. For every finite \(B\), \(E(B)>0\), and its optimal bounded-latent asymptotic is
\[
\boxed{\lim_{B\to\infty} B^2 E(B)=\frac{\gamma^2}{\|A\|_F^2}.}
\]
Equivalently, defining the least required magnitude of the hidden negative entry at root-mean-square tolerance \(\varepsilon>0\) by
\[
B_{\min}(\varepsilon)=\inf\{B\ge0:E(B)\le\varepsilon^2\},
\]
we have
\[
\lim_{\varepsilon\downarrow0}\varepsilon B_{\min}(\varepsilon)
=\frac{|\gamma|}{\|A\|_F}.
\]
All formulas hold without symmetry, stochastic assumptions, or conditioning bounds on the positive entries. The escape class is relatively open and dense within this positive rank-one-block family.

## Assumptions and scope
The rank of \(A\) is exactly one, and each of the other eight prescribed entries of \(X\) is strictly positive. The only zero prescribed entry is the bottom-right corner. A rank-two latent matrix may have negative entries at this zero, but its negative magnitude is capped by \(B\). The objective compares the **rectified** latent matrix, not the latent matrix itself, against \(X\). No assertion is made about general sparsity patterns, higher latent rank, or arbitrary matrix dimensions.

For a real \(2\times2\) matrix \(A\), \(\operatorname{adj}(A)\) denotes its classical adjugate. If \(A=pq^{\mathsf T}\) with positive \(p,q\in\mathbb R^2\), set \(p_\perp=(p_2,-p_1)^{\mathsf T}\), \(q_\perp=(q_2,-q_1)^{\mathsf T}\). Then
\[
\gamma=(v^{\mathsf T}q_\perp)(p_\perp^{\mathsf T}u).
\]
Consequently, the exactness class consists precisely of alignments \(u\in\operatorname{span}(p)\) or \(v\in\operatorname{span}(q)\). Off these two alignment loci, the lack of exact rank-two completion is generic.

## Proof
**1. Exact rank and nonattainment.** For any scalar \(z\), the block determinant identity gives
\[
\det\begin{pmatrix}A&u\\v^{\mathsf T}&z\end{pmatrix}
=z\det A-v^{\mathsf T}\operatorname{adj}(A)u=-\gamma.
\]
Every exact latent ReLU realization of \(X\) has its first eight entries fixed at those of \(X\) and last entry nonpositive. If \(\gamma\ne0\), all such latent matrices have rank three; since \(X\) itself is a rank-three nonnegative latent realization, its exact ReLU-rank is three. If \(\gamma=0\), then \(X\) has rank at most two. Rank one is impossible because the eight prescribed positive entries force the last product entry of any real rank-one factorization to be positive. Therefore its exact ReLU-rank equals two.

**2. Sharp constructive upper bound.** Let \(N=\operatorname{adj}(A)^{\mathsf T}\) and \(\eta=v^{\mathsf T}A^{\mathsf T}u>0\). For \(2\times2\) matrices with \(\det A=0\), direct expansion gives
\[
\det(A+tN)=t\|A\|_F^2,
\quad\operatorname{adj}(A+tN)=\operatorname{adj}(A)+tA^{\mathsf T},
\quad\|N\|_F=\|A\|_F.
\]
Choose
\[
t_B=-\frac{\gamma}{B\|A\|_F^2+\eta},
\qquad
Z_B=\begin{pmatrix}A+t_BN&u\\v^{\mathsf T}&-B\end{pmatrix}.
\]
The determinant is exactly
\[
\det Z_B=-\big(B\|A\|_F^2+\eta\big)t_B-\gamma=0.
\]
Since \(t_B\to0\) and \(A\) is strictly positive, \(A+t_BN\) is entrywise positive for all sufficiently large \(B\). Rectifying \(Z_B\) then changes only the upper-left block and the negative bottom-right entry, so
\[
E(B)\le \|t_BN\|_F^2
=\frac{\gamma^2\|A\|_F^2}{(B\|A\|_F^2+\eta)^2}.
\]
This gives \(\limsup_{B\to\infty}B^2E(B)\le\gamma^2/\|A\|_F^2\) and proves the unrestricted infimum is zero.

**3. Matching global lower bound.** Assume \(\gamma\ne0\). Choose rank-two latent matrices \(Z_B\), with \(-B\le (Z_B)_{33}\le0\), whose squared losses approach \(E(B)\) to within \(o(B^{-2})\). Step 2 supplies losses \(O(B^{-2})\); hence the root errors \(\delta_B=\|X-\max(0,Z_B)\|_F\) are \(O(B^{-1})\). Strict positivity of all eight observed entries ensures that, for large \(B\), the first eight entries of each \(Z_B\) are positive and equal to the observed entries plus perturbations of combined Frobenius norm at most \(\delta_B\). Write the blocks as \(A+H_B,u+e_B,(v+f_B)^{\mathsf T}\). Polynomial continuity yields
\[
(v+f_B)^{\mathsf T}\operatorname{adj}(A+H_B)(u+e_B)
=\gamma+O(\delta_B).
\]
The rank-two determinant identity implies, because the last entry has magnitude at most \(B\),
\[
B\,|\det(A+H_B)|\ge|\gamma|-O(\delta_B).
\]
Again using \(\det A=0\), the exact two-by-two determinant expansion and the Frobenius Cauchy–Schwarz inequality give
\[
|\det(A+H_B)|
\le\|A\|_F\|H_B\|_F+\tfrac12\|H_B\|_F^2
\le\|A\|_F\delta_B+\tfrac12\delta_B^2.
\]
Multiplying through and using \(\delta_B=O(B^{-1})\) proves \(\liminf_{B\to\infty}B\delta_B\ge|\gamma|/\|A\|_F\). The upper bound proves equality, and then gives the claimed squared-error limit.

**4. Finite-budget strictness and inverse law.** If some fixed finite budget had zero infimum, a sequence of losses approaching zero would force the first eight latent entries to converge to the positive observations while the last latent entries remain in the compact interval \([-B,0]\). A convergent subsequence would give a rank-at-most-two exact latent completion, contradicting \(\gamma\ne0\). Hence \(E(B)>0\) for each finite \(B\). The function \(E(B)\) is nonincreasing and its sharp positive asymptotic can be inverted by elementary two-sided bounds, proving the tolerance formula.

The alignment factorization follows by directly computing \(\operatorname{adj}(pq^{\mathsf T})=q_\perp p_\perp^{\mathsf T}\). These two proper alignment loci have empty relative interior, establishing the genericity statement.

## Verification
A standalone exact-arithmetic script, `check_math.py`, constructs 400 seeded positive rank-one matrices, independent positive border vectors, and four budgets per matrix. It checks 1,600 exact determinant/rank-witness identities, plus adjugate, nullspace-factorization and squared-error identities. For large budgets it verifies the predicted leading coefficient numerically. The complete terminal output is embedded as `verification_output.txt`.

For the published example
\[
X=\begin{pmatrix}1&1&1\\1&1&2\\1&2&0\end{pmatrix},
\]
we have \(L=4\), \(\gamma=1\), \(\eta=9\). The explicit rank-two witness has perturbation \(t_B=-1/(4B+9)\), giving
\[
E(B)\le\frac{4}{(4B+9)^2},\qquad
\boxed{\lim_{B\to\infty}B^2E(B)=\tfrac14.}
\]
Thus the previously exhibited one-entry perturbation path is not asymptotically sharp: balanced correction of the rank-one leading block improves its leading error coefficient. Finite calculations are checks of the witness, not proofs of the global asymptotic or genericity; these follow from the determinant argument above.

## Relationship to prior work
Seraghiti, Vandaele and Gillis (2026, arXiv:2610.22255v1, Proposition 2.1) established direct Frobenius ReLU nonattainment using the displayed \(3\times3\) example and a one-entry perturbation. The present result treats the entire strictly positive one-zero rank-one-block stratum, identifies the exact/no-exact alignment transition, and gives the **optimal global** leading latent-budget error coefficient; neither a single feasible path nor a rank argument alone supplies the lower bound needed for that coefficient. Saul et al. (2026, arXiv:2608.21607v1) study exact subzero decompositions, geometric constructions, large-scale algorithms, and latent rather than directly rectified losses. Gillis, Porcelli and Seraghiti (2025, arXiv:2503.23832v1) discuss nonattainment in a different latent-variable formulation, including a rank-one example. Classical structured matrix completion literature studies related rank constraints, but does not directly imply the sharp rectified-loss clipping coefficient under the conditions considered here.

## Limitations
The leading error law is asymptotic; the displayed finite-budget witness is an upper bound, not an asserted globally exact optimizer at finite \(B\). The only capped latent coordinate is the sole observed zero. The theorem does not characterize factor-norm penalties, optimization convergence, arbitrary zero patterns or higher-dimensional blocks. Priority requires independent checking against possible equivalent perturbative matrix-completion results. No independent audit is claimed.

## References
1. G. Seraghiti, A. Vandaele, N. Gillis, *The ReLU Matrix Decomposition: NP-Hardness, Ill-Posedness, and ReLU-Rank*, arXiv:2610.22255v1 (first posted 2026-10-15), especially Section 2.1, Proposition 2.1. https://arxiv.org/html/2610.22255v1
2. L. K. Saul, N. Huang, D. Bollweg, J. Soules, D. C. Halikias, *Subzero matrix completion for sparse data analysis: large-scale learning of latent low-rank structure*, arXiv:2608.21607v1 (2026). https://arxiv.org/html/2608.21607v1
3. N. Gillis, M. Porcelli, G. Seraghiti, *An extrapolated and provably convergent algorithm for nonlinear matrix decomposition with the ReLU function*, arXiv:2503.23832v1 (2025). https://arxiv.org/abs/2503.23832
4. E. N. Epperly, N. Govindarajan, S. Chandrasekaran, *Minimal rank completions for overlapping blocks*, Linear Algebra and its Applications 627 (2021), 185–198. https://doi.org/10.1016/j.laa.2021.06.011
