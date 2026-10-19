# Exact stopping distributions and a coupling discontinuity for two-coordinate randomized CGLS

## Finding

For the exact-arithmetic two-coordinate version of randomized conjugate gradient least squares (RCGLS) of Zeng, Cai, Han, and Xie, with independent label probabilities \(p\) and \(q=1-p\), the number \(T\) of completed updates until the exact least-squares minimizer is reached has an explicit rational probability-generating function. Write \(h=pq\) and \(\mathcal G(z)=\mathbb E[z^T]\). When the normal-matrix coordinates have nonzero coupling, it is
\[
\mathcal G_{\mathrm c}(z)=\frac{h z^2(2-2z+z^2-hz^3)}{1-z+hz^2-h^2z^4},\qquad \mathbb E T_{\mathrm c}=1+\frac{1}{h}.
\]
When the normal matrix is diagonal, the law instead is
\[
\mathcal G_{\mathrm d}(z)=\frac{h z^2(2-z)}{1-z+hz^2},\qquad \mathbb E T_{\mathrm d}=\frac{1}{h}-1.
\]
Thus every arbitrarily small *nonzero* off-diagonal coupling increases the exact expected stopping count by precisely two updates, independently of the diagonal entries and of \(p\). In either regime \(p=1/2\) uniquely minimizes the mean among fixed independent label distributions. For a coupled system, the often-used squared-column-norm probabilities \(p=a/(a+b)\) and \(q=b/(a+b)\) yield \(\mathbb E T=3+a/b+b/a\), arbitrarily larger than the optimal value \(5\) when the column norms become unbalanced.

A further contrast is sharp: on a coupled system with generic nonzero initial coordinate errors, standard exact-line-search randomized coordinate descent never reaches the minimizer in finitely many updates along *any* coordinate sequence, whereas RCGLS reaches it almost surely with the above finite mean.

## Assumptions and scope

Let \(A\in\mathbb R^{m\times2}\) have full column rank and \(b\in\mathbb R^m\). Its unique least-squares minimizer is \(x_*\); let \(H=A^{\mathsf T}A=\begin{pmatrix}a&c\\c&b_0\end{pmatrix}\) with \(a,b_0>0\) and \(ab_0-c^2>0\). In this document \(b_0\) denotes the second diagonal entry, not the data vector. Let \(e_0=x_0-x_*\) satisfy \((e_0)_1(e_0)_2(He_0)_1(He_0)_2\ne0\); this excludes exceptional initial states for which a coordinate is already solved or an initial sampled gradient vanishes.

Every independent sample is \(S_k=e_{I_k}/\sqrt{H_{I_kI_k}}\), where \(\Pr(I_k=1)=p\in(0,1)\) and \(\Pr(I_k=2)=q=1-p\). Apply *Algorithm 1 of the cited 2026 paper* with exact arithmetic, the paper's \(0/0=0\) convention, and no rejection/resampling of zero-gradient coordinates. The stopping variable counts one completed update per sampled label and is \(T=\inf\{t\ge0:x_t=x_*\}\). No tolerance-based or premature local-gradient stopping rule is used.

Equivalently, for the error \(e=x-x_*\), gradient \(g=He\), and signed search direction \(d\) (the negative of the paper's \(p^k\)), define the sampled gradient \(s=(g_i/H_{ii})e_i\), set \(d=s-\langle s,Hd_-\rangle d_-/\langle d_-,Hd_-\rangle\) with quotient zero if the denominator vanishes, and update \(e\leftarrow e-\langle g,d\rangle d/\langle d,Hd\rangle\), again with zero quotient for zero denominator. The initial preceding direction is zero. Here \(e_i\) in the formula for \(s\) is the standard basis vector, not the coordinate-error component.

## Proof

**1. Nontermination after a single coordinate on a coupled system.** For a nonzero single-coordinate direction, the exact least-squares line search annihilates that coordinate of the normal-equation gradient. Writing the error components as \((u,v)\), a first-axis step maps it to \((-cv/a,v)\), and a second-axis step maps it to \((u,-cu/b_0)\). When \(c\ne0\), a nonzero pair stays a nonzero pair after either such update. Thus the stated nondegenerate start remains nonzero after each isolated coordinate step, and the unsampled gradient component does not vanish accidentally. For \(c=0\), a coordinate step instead sets its own error component to zero permanently.

**2. Active/inactive automaton.** After the first sample at label \(i\), the RCGLS direction is nonzero and aligned with that label; call the state \(A_i\). If the next label \(j\ne i\) occurs while the direction is active, the new direction is \(H\)-orthogonal to the previous direction and linearly independent of it. The current error is already \(H\)-orthogonal to the previous direction, so the second exact line search annihilates the error in the whole two-dimensional space: termination occurs at that update. By contrast, sampling the same label again after a completed coordinate step gives zero sampled gradient; its conjugacy correction is also zero, so the direction becomes the inactive state \(I_i\), with a zero-size update. Further draws of \(i\) preserve \(I_i\). The first draw of \(j\ne i\) from \(I_i\) gives a fresh nonzero direction aligned with \(j\), hence state \(A_j\). This remains true after any finite sequence of nonterminal draws by Step 1.

**3. Exact generating function.** Let \(F_i(z)\) and \(G_i(z)\) be the generating functions of the additional number of updates until termination starting from \(A_i\) and \(I_i\). Write \(p_1=p\), \(p_2=q\), and let \(j\) be the other label. The exact state transitions give
\[
F_i(z)=z\bigl(p_j+p_iG_i(z)\bigr),\qquad
G_i(z)=z\bigl(p_iG_i(z)+p_jF_j(z)\bigr).
\]
Eliminating the two inactive functions gives \(F_i(z)=zp_j+p_ip_jz^2F_j(z)/(1-p_i z)\). Solving this two-equation linear system and accounting for the first sample, \(\mathcal G_{\mathrm c}(z)=z(pF_1(z)+qF_2(z))\), yields the rational expression in the Finding section. A terminal pattern appears with positive probability in each block of bounded length, so the stopping time is almost surely finite with a geometric tail. In particular the generating function is differentiable at one, and differentiation gives \(\mathbb ET_{\mathrm c}=1+1/(pq)\).

**4. Diagonal case.** If \(c=0\), the first sample sets one initial error component permanently to zero and the first occurrence of the other label terminates exactly. Consequently \(T\) is the two-label coupon-collector stopping time. The elementary geometric mixture gives \(\mathcal G_{\mathrm d}(z)=pqz^2(2-z)/(1-z+pqz^2)\) and \(\mathbb ET_{\mathrm d}=1/(pq)-1\).

**5. Optimized sampling and comparison.** Since \(pq\le1/4\) with equality only for \(p=q=1/2\), both exact means are uniquely minimized by uniform sampling. Substituting \(p=a/(a+b_0)\) yields the displayed norm-proportional formula. Ordinary randomized coordinate descent makes only one coordinate line-search step on every iteration, so Step 1 proves it cannot terminate in finitely many steps when \(c\ne0\) and both initial error coordinates are nonzero. The exact two-update mean jump follows by subtraction.

## Verification

The included standalone `verify.py` requires Python 3 and SymPy. It implements the source method's signed-direction error recursion with exact `fractions.Fraction` arithmetic, exhaustively checks all binary label strings up to length 10 for three rational positive-definite normal matrices (diagonal, positive coupling and negative coupling) with two distinct nondegenerate initial errors, and compares exact first-hit times against the active/inactive automaton. Symbolic differentiation and exact Taylor coefficients verify both rational generating functions and both means; results also agree with direct exact enumeration through degree nine for several distinct sampling probabilities. It completed 12,334 checks. Finite enumeration corroborates but does not prove the all-sequence and infinite-time claims; the proof above does.

## Relationship to prior work

Zeng, Cai, Han and Xie (2026) introduce precisely the randomized CGLS update with the applicable zero-denominator convention, obtain conditional mean-square/linear-convergence inequalities in Theorem 2.4, and compare the method with randomized coordinate descent. Their statements do not provide this two-state-per-label exact finite stopping-time law or its discontinuity across zero coupling. Zeng, Han, Su and Xie (2023/2024) introduce related stochastic conjugate-gradient algorithms for consistent linear systems, including a resampling-until-nonzero-gradient rule; those sample mechanics and stopping quantities differ from the iid zero-draw-inclusive RCGLS studied here. Classical coordinate-descent expected convergence bounds do not imply positive-probability finite absorption, much less the rational generating functions. The probabilistic coupon-collector identity in the diagonal case is classical and is not claimed new.

## Limitations

This is an exact-arithmetic, two-unknown, independent single-coordinate sampling theorem, not a bound on practical floating-point exact termination or on stopping at a finite tolerance. Near-zero coupling is numerically difficult to distinguish from zero; the discontinuity is algebraic. Exceptional initial errors, adaptive or without-replacement sampling, rejected idle draws, different momentum resets, larger dimensions, rank deficiency, and general block sketches require separate analysis. The mathematical result is not a statement about the actual runtime cost of the source's full-dimensional implementation. There is a residual possibility of equivalent results in unindexed literature; self-review does not constitute independent validation.

## References

1. Yun Zeng, Jian-Feng Cai, Deren Han and Jiaxin Xie, *Randomized conjugate gradient least squares*, arXiv:2605.25034v1, 24 May 2026, https://arxiv.org/html/2605.25034v1 (Algorithm 1, Section 2.2; Theorem 2.4; Remark 2.1; zero-denominator convention).
2. Yun Zeng, Deren Han, Yansheng Su and Jiaxin Xie, *On adaptive stochastic heavy ball momentum for solving linear systems*, arXiv:2305.05482v3, https://arxiv.org/html/2305.05482v3 (Section 5.2, Algorithm 4).
3. D. Leventhal and A. S. Lewis, *Randomized methods for linear constraints: convergence rates and conditioning*, Mathematics of Operations Research 35 (2010), 641–654 (background on randomized coordinate updates, cited by Reference 1).
