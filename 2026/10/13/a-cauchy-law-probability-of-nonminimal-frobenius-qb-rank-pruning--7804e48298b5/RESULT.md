# A Cauchy-law probability of nonminimal Frobenius QB rank pruning

## Finding
Consider the **unpivoted Gaussian, two-column QB block with Frobenius row pruning** of Smith, Do, and Chen [1], in exact arithmetic. Let
\[
 A_\epsilon=\operatorname{diag}(1,\epsilon,0,0)\in\mathbb R^{4\times4},\qquad
 \tau=c\epsilon,\quad c>1,\quad
 0<\epsilon<(2c^2-1)^{-1/2}.
\]
Draw a \(4\times2\) Gaussian block \(\Omega\) with independent \(N(0,1/2)\) entries, take the **unpivoted** thin QR basis \(Q\) of \(A_\epsilon\Omega\), and let \(B=Q^{\mathsf T}A_\epsilon\). The source's Frobenius pruning rule starts at zero residual and deletes the shortest row of \(B\) if its norm is strictly below \(\tau\). Let \(R\in\{1,2\}\) be the number of rows it retains. Define
\[
 u=\frac{\tau^2-\epsilon^2}{1-\epsilon^2}\in(0,1/2).
\]
Then the probability that the rule retains **both** rows is exactly
\[
 \boxed{\Pr(R=2)=\frac2\pi\left[
  \arctan\!\left(\frac1\epsilon\sqrt{\frac{1-u}{u}}\right)
  -\arctan\!\left(\frac1\epsilon\sqrt{\frac{u}{1-u}}\right)
 \right].} \tag{1}
\]
This is genuine over-retention: the minimum rank of any matrix \(X\) satisfying \(\|A_\epsilon-X\|_F<\tau\) is exactly one, whereas \(R=2\) has the positive probability in (1).

The stochastic look-ahead test in the full matrix-free algorithm is also accounted for. Let \(E=\{\|A_\epsilon\Omega\|_F>\tau\}\). On \(E\), the algorithm completes the first two-column block, its second independent look-ahead sees **zero residual**, and its returned rank is \(R\). Therefore
\[
 \boxed{\left|\Pr(E\cap\{R=2\})-\Pr(R=2)\right|
 \le 1-e^{-c^2\epsilon^2}\le c^2\epsilon^2.} \tag{2}
\]
For each fixed \(c>1\), both probabilities consequently converge to
\[
 \boxed{p(c)=\frac2\pi\arctan\frac1{\sqrt{c^2-1}}.} \tag{3}
\]
In particular, at \(c=\sqrt2\) the full algorithm's probability of returning rank two **through this completed-block branch** tends to \(1/2\) as \(\epsilon\downarrow0\), despite the optimum rank being one. The limit \(p(c)\) approaches one as \(c\downarrow1\). This gives a sharp probability law for a basis-dependent pruning decision, not a statement about false residual estimates or finite precision.

## Assumptions and scope
The input is the specified rank-two, real, \(4\times4\) diagonal family; the tolerance is **absolute**, not estimated relative tolerance; \(b=2\); the random block is independent Gaussian with the source's \(1/\sqrt b\) normalization; and QR uses the first sketch column as the first basis direction **without column pivoting**. The row-pruning rule is precisely the source's Algorithm 3 with current residual indicator \(\alpha=0\), since the full two-column span of \(A_\epsilon\) has been found. All equalities concern exact arithmetic. For the statement about the full iteration, the event \(E\) specifies the branch where the first residual test does not stop prematurely. The second residual test is then identically zero. The complementary branch is not assigned a rank in this theorem.

The parameter restriction implies \(\epsilon<\tau<1\) and \(\tau^2<(1+\epsilon^2)/2\), so precisely one of two row removals can occur; the unpivoted Gaussian QR is well-defined with probability one.

## Proof
**(1) Geometry of the Gaussian QR block.** Write the first two entries of the first Gaussian sketch column, before normalization, as independent \(X,Y\sim N(0,1)\). The first QR vector is
\[
 q_1=\frac{(X,\epsilon Y,0,0)^{\mathsf T}}
 {\sqrt{X^2+\epsilon^2Y^2}}.
\]
Almost surely the two sampled columns span \(\operatorname{span}\{e_1,e_2\}\). Hence the second QR vector is, up to sign, the perpendicular unit vector in that plane. Put \(s=\epsilon^2Y^2/(X^2+\epsilon^2Y^2)\). Direct multiplication by \(A_\epsilon\) yields the squared norms of the two rows of \(B\):
\[
 w_1^2=1-(1-\epsilon^2)s,\qquad
 w_2^2=\epsilon^2+(1-\epsilon^2)s. \tag{4}
\]
The full QR block reconstructs \(A_\epsilon\) exactly, so its residual is zero. The pruning rule removes the smallest row if and only if its norm is \(<\tau\); it cannot remove both, since \(w_1^2+w_2^2=1+\epsilon^2>\tau^2\). Thus it retains both if and only if \(w_1^2\ge\tau^2\) and \(w_2^2\ge\tau^2\), equivalent by (4) to
\[
 u\le s\le1-u. \tag{5}
\]

**(2) Exact probability.** The ratio \(Z=Y/X\) is standard Cauchy: for \(\phi\) the standard normal density, changing variables \((X,Y)=(x,zx)\) gives \(f_Z(z)=\int_{\mathbb R}|x|\phi(x)\phi(zx)\,dx=1/[\pi(1+z^2)]\). Since
\[
 s=\frac{\epsilon^2Z^2}{1+\epsilon^2Z^2},
\]
condition (5) is exactly
\[
 \frac1\epsilon\sqrt{\frac{u}{1-u}}
 \le |Z| \le
 \frac1\epsilon\sqrt{\frac{1-u}{u}}.
\]
The Cauchy distribution satisfies \(\Pr(|Z|\le t)=2\arctan(t)/\pi\) for \(t\ge0\), proving (1). The endpoints have probability zero, so no tie convention affects the probability.

**(3) Global optimum and the rotation comparison.** The two positive singular values of \(A_\epsilon\) are \(1\) and \(\epsilon\). By the Eckart–Young–Mirsky theorem, the best rank-one Frobenius residual is \(\epsilon<\tau\), achieved by \(e_1e_1^{\mathsf T}\). A rank-zero residual is \(\sqrt{1+\epsilon^2}>\tau\). Thus the exact minimum feasible rank is one. Also, since \(Q\) spans the range, an orthogonal internal rotation taking its first vector to \(e_1\) yields a one-row factor with residual \(\epsilon\); the source's fixed-row rule does not make this rotation. This SVD-based alternative is the classical optimal rank-one truncation and is *not* asserted to be new.

**(4) The actual initial sketch test.** Writing the first row of the \(4\times2\) standard Gaussian block as \(X_1,X_2\), the initial estimate obeys
\[
 \|A_\epsilon\Omega\|_F^2
 =\tfrac12(X_1^2+X_2^2+\epsilon^2Y_1^2+\epsilon^2Y_2^2).
\]
Its failure event \(E^c\) implies \(X_1^2+X_2^2\le2c^2\epsilon^2\). The sum has the chi-square law with two degrees of freedom, hence
\[
 \Pr(E^c)\le1-e^{-c^2\epsilon^2}\le c^2\epsilon^2.
\]
On \(E\), the first QR block has full range and the next residual is zero for every second independent Gaussian test block. The returned rank is therefore \(R\), proving (2) by \(0\le\Pr(R=2)-\Pr(E\cap\{R=2\})\le\Pr(E^c)\).

**(5) Sharp small-\(\epsilon\) limit.** With \(\tau=c\epsilon\),
\[
 u=\frac{(c^2-1)\epsilon^2}{1-\epsilon^2}.
\]
The lower Cauchy cutoff tends to \(\sqrt{c^2-1}\), while the upper cutoff diverges to infinity. Substitution in (1) gives (3), and (2) transfers the same limit to the completed-block branch. Setting \(c=\sqrt2\) gives \(p(c)=1/2\). Letting \(c\downarrow1\) in (3) gives one.

## Verification
The independent, standard-library-only script `verify.py` checks the exact row-norm identities with rational arithmetic, the interval equivalence in the theorem with rational thresholds, the Cauchy formula against direct integration, and the small-\(\epsilon\) limit. It additionally simulates unpivoted Gaussian first blocks and the *actual initial look-ahead acceptance event*, comparing observed frequencies with (1) and the rigorous (2) bound. Invoke with `python3 verify.py` (Python 3.9+). Numerical tests are not evidence for a universal probability identity; the Cauchy law and chi-square argument above provide that proof.

## Relationship to prior work
Smith, Do, and Chen [1, Algorithms 2–3, Theorem 8] introduce the matrix-free Gaussian QB method, the randomized residual test, and the final-block Frobenius rank-pruning rule based on sorted row norms; their theorem proves the Frobenius error identity for *fixed* basis rows. The exact rank-over-retention probability (1), its full-look-ahead limit (3), and its critical Cauchy scaling are not claims of [1]. Their spectral-norm scheme *already* uses an SVD of the final block [1, Section 4.2]; the present comparison concerns the distinct, inexpensive Frobenius row-pruning scheme.

Yu, Gu, and Li [2] analyze adaptive QB and Frobenius residual tracking, including standard postprocessing by SVD, but not the specific row-pruning decision or its probability law. Liu and Yu [3] investigate blocked randomized numerical-rank detection via singular-value gaps and deflation, not the Gaussian orientation law of this final-block row selection. Martinsson and Voronin [4] develop randomized blocked rank-revealing QB methods and motivate the shared approach, but [4] is not claimed as a source for (1). Classical SVD rank optimality is fully credited. Published mathematical-record searches and nearby randomized matrix approximation findings have been checked for equivalent parameterizations; no identical conditional Cauchy rank-pruning law was located. Absence from search results is not proof of global novelty.

## Limitations
The law is not a worst-case high-dimensional lower bound: it treats an exact rank-two diagonal matrix embedded in dimension four, fixed \(b=2\), unpivoted QR, an absolute tolerance, and a particular row-norm pruning policy. The probability (1) is for the completed QR block; for the actual algorithm, the unconditional **joint** event has the limiting probability (3), with the explicit finite-error bound (2). It does not assign behavior to executions stopped by the first randomized look-ahead or to implementations that pivot QR columns. Rotating by SVD requires additional small-block work, so the theorem does not compare wall-clock costs. No finite-precision, spectral-norm, or adjoint-free claim is made. Equivalent observations under other rank-revealing terminology may exist.

## References
[1] Arnel I. Smith, Elly Do, Chao Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, arXiv:2607.06758v1, first public 2026-07-07. Full text: https://arxiv.org/html/2607.06758v1. Companion source, `randQB_MF_Fro.m` and `Prune_Rank_Fro.m`: https://github.com/SMART-Algebra/Adaptive-Matfree-Lowrank.

[2] Wenjian Yu, Yu Gu, Yaohang Li, *Efficient Randomized Algorithms for the Fixed-Precision Low-Rank Matrix Approximation*, arXiv:1606.09402, first public 2016-06-30; SIAM J. Matrix Anal. Appl. 39 (2018). Full text: https://ar5iv.labs.arxiv.org/html/1606.09402.

[3] Qiaohua Liu, Yuejuan Yu, *Efficient adaptive randomized algorithms for fixed-threshold low-rank matrix approximation*, arXiv:2508.07553v1, first public 2025-08-11. Full text: https://arxiv.org/html/2508.07553v1.

[4] Per-Gunnar Martinsson, Sergey Voronin, *A randomized blocked algorithm for efficiently computing rank-revealing factorizations of matrices*, arXiv:1503.07157, first public 2015-03-24; SIAM J. Sci. Comput. 38 (2016), S485–S507.
