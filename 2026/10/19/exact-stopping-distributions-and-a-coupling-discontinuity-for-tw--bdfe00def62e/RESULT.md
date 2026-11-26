# Exact stopping laws for two-coordinate RCGLS with idle draws

## Finding

Consider a two-coordinate, exact-arithmetic variant of the randomized conjugate gradient least-squares (RCGLS) method of Zeng, Cai, Han, and Xie. Use independent label probabilities \(p\) and \(q=1-p\), and count a draw with zero direction as an idle update that clears the stored direction. Write \(h=pq\), let \(T\) be the first completed-update count at which the exact least-squares minimizer is reached, and put \(\mathcal G(z)=\mathbb E[z^T]\). With nonzero off-diagonal coupling in the normal matrix,
\[
\mathcal G_{\mathrm c}(z)=\frac{h z^2(2-2z+z^2-hz^3)}{1-z+hz^2-h^2z^4},\qquad \mathbb E T_{\mathrm c}=1+\frac{1}{h}.
\]
When the normal matrix is diagonal,
\[
\mathcal G_{\mathrm d}(z)=\frac{h z^2(2-z)}{1-z+hz^2},\qquad \mathbb E T_{\mathrm d}=\frac{1}{h}-1.
\]
Thus arbitrarily small nonzero coupling increases the mean exact stopping count by precisely two updates at fixed \(p\). In either regime \(p=1/2\) uniquely minimizes the mean among fixed independent label distributions. For a coupled normal matrix with diagonal entries \(a,b_0\), squared-column-norm probabilities \(p=a/(a+b_0)\) and \(q=b_0/(a+b_0)\) give \(\mathbb E T=3+a/b_0+b_0/a\), arbitrarily larger than the optimal value \(5\) when the column norms become unbalanced. By contrast, on a coupled system with both initial coordinate errors nonzero, standard exact-line-search coordinate descent never reaches the minimizer in finitely many updates along any sequence of coordinate labels.

## Assumptions and scope

Let \(A\in\mathbb R^{m\times 2}\) have full column rank and \(b\in\mathbb R^m\). Write \(x_*\) for the unique least-squares minimizer and \(H=A^{\mathsf T}A=\begin{pmatrix}a&c\\c&b_0\end{pmatrix}\), so \(a,b_0>0\) and \(ab_0-c^2>0\). Let \(e_0=x_0-x_*\) satisfy \((e_0)_1(e_0)_2(He_0)_1(He_0)_2\neq0\); a first draw of either coordinate then makes a nonzero step. At each update sample \(i\in\{1,2\}\), with probabilities \(p\in(0,1)\) and \(q=1-p\), independently of all previous labels. The normalized sketch is \(e_i/\sqrt{H_{ii}}\), where \(e_i\) in that expression denotes the standard basis vector.

The iteration is defined as follows. With error \(e=x-x_*\), gradient \(g=He\), and preceding signed direction \(d_-\) (initially zero), set
\[
s=(g_i/H_{ii})e_i,\qquad
d=s-\frac{\langle s,Hd_-\rangle}{\langle d_-,Hd_-\rangle}d_-,\qquad
e\ \leftarrow\ e-\frac{\langle g,d\rangle}{\langle d,Hd\rangle}d.
\]
In these two formulas we set a quotient with zero denominator to zero. Store the new direction \(d\), even if it is zero. Every draw counts as one completed update; there is no resampling or tolerance stop. The stopping count is \(T=\inf\{t\ge0:x_t=x_*\}\).

For nonzero denominators this is the signed-error form of Algorithm 1 of Zeng et al. with \(d=-p^k\) and the normalized singleton sketches of Remark 2.1. The residual is \(r=b-Ax\), so \(A^{\mathsf T}r=-g\); the search-direction formula and orthogonality of the current gradient to the preceding nonzero direction give \(\langle g,d\rangle=\langle g,s\rangle=\|S_k^{\mathsf T}A^{\mathsf T}r\|^2\). Our zero-denominator rule extends the displayed updates in Algorithm 1. The paper states \(0/0=0\) in its definition of the expected sketch matrix in Eq. (15); we do not rely on that passage as a prescription for the update coefficients. The extra rule matters: after a repeated draw of the just-solved coordinate the next direction is zero while the error is generally nonzero, and the unextended line-search coefficient then has the form \(0/0\).

## Proof

**1. Single-coordinate steps.** A nonzero direction aligned with coordinate \(i\) gives a step that annihilates that coordinate of the normal-equation gradient. Writing the error as \((u,v)\), the first-axis step maps it to \((-cv/a,v)\) and the second-axis step maps it to \((u,-cu/b_0)\). If \(c\ne0\), both coordinates stay nonzero after either projection when both were nonzero initially. The unsampled gradient component does not vanish because \(H\) is invertible and the error does not vanish. If \(c=0\), the chosen coordinate becomes zero permanently. These projections also describe ordinary coordinate descent, including a no-change step when the chosen coordinate already has zero gradient. In the coupled case neither projection can reach the minimizer from an error with both coordinates nonzero.

**2. Coupled-state transitions.** After the initial draw of label \(i\), the stored direction is nonzero and aligned with that label; call this state \(A_i\). If the next label is \(j\ne i\), the sampled gradient is nonzero and aligned with \(j\). Its conjugacy correction gives a nonzero direction \(H\)-orthogonal to the preceding direction. The two directions span the space. The current error is already \(H\)-orthogonal to the preceding direction, and a line search along the new direction makes it \(H\)-orthogonal to both; thus the update terminates. If the next draw from \(A_i\) is instead \(i\), the sampled gradient and its correction are zero, so the iteration stores zero direction and leaves the error unchanged; call the state \(I_i\). Further draws of \(i\) preserve \(I_i\); a draw of \(j\ne i\) makes a fresh coordinate step and enters \(A_j\). Step 1 ensures these cases exhaust the nonterminal transitions.

**3. Coupled stopping law.** Let \(F_i,G_i\) be the generating functions for the additional updates from \(A_i,I_i\), respectively. With \(p_1=p\), \(p_2=q\), and \(j\ne i\),
\[
F_i(z)=z(p_j+p_iG_i(z)),\qquad G_i(z)=z(p_iG_i(z)+p_jF_j(z)).
\]
Hence \(F_i=zp_j+hz^2 F_j/(1-p_i z)\). Solving the two equations and inserting the first draw, \(\mathcal G_{\mathrm c}=z(pF_1+qF_2)\), gives the displayed fraction. A block of three labels \(1,2,1\) forces absorption from any nonterminal state (including the initial state), so independence gives a geometric tail. For the mean, if \(f_i\) denotes the expected number of additional updates from \(A_i\), eliminating the inactive-state means gives \(f_i=1/p_j+p_i f_j\). It follows that \(f_1=(1/q+1)/(1-h)\) and \(f_2=(1/p+1)/(1-h)\); substituting in \(1+pf_1+qf_2\) gives \(1+1/h\).

**4. Diagonal stopping law.** The first draw solves its coordinate and the first draw of the other coordinate terminates. Conditional on the first draw, the additional waiting time is geometric with parameter \(q\) or \(p\), respectively. Thus
\[
\mathcal G_{\mathrm d}=p z\frac{q z}{1-pz}+q z\frac{p z}{1-qz},\qquad \mathbb ET_{\mathrm d}=1+p/q+q/p.
\]
These are the stated expressions after simplification.

**5. Sampling and mean jump.** The product \(pq\) is maximized only at \(p=q=1/2\). For norm-proportional sampling, \(1/(pq)=(a+b_0)^2/(ab_0)\), giving the cited mean. The difference of the coupled and diagonal means is two. For a fixed error with both coordinates nonzero, the initial-gradient assumptions hold at zero coupling and throughout a neighborhood of zero, so this difference is a discontinuity within the nondegenerate regime.

## Verification

The standalone `verify.py` uses Python 3, `fractions.Fraction`, and SymPy. It checks every binary label string of lengths 1 through 10 for three rational positive-definite normal matrices (zero, positive, and negative coupling) and two initial errors per matrix. It compares first-hit times in the stated recursion to the state transitions, checks the symbolic PGFs at one and their derivatives, and compares coefficients through degree nine with exact enumeration for three label probabilities. The proof, not these finite checks, establishes the general stopping law.

## Relationship to prior work and limitations

Zeng, Cai, Han, and Xie introduce RCGLS and obtain conditional mean-square convergence bounds (Theorem 2.4). Those bounds are not exact hitting-time laws. The present result concerns the normalized two-coordinate iteration with the idle-and-clear rule stated here. Related stochastic conjugate-gradient methods for consistent linear systems include a resampling-until-nonzero-gradient rule, which instead discards the idle draws that generate the additional states in this calculation. The two-label coupon-collector law itself is classical.

The result is for exact arithmetic, full column rank, two unknowns, and independent normalized single-coordinate draws from a nondegenerate start. It is not a runtime or floating-point claim, a statement about tolerance stops, or a result for adaptive sampling, a different idle rule, or larger sketches. Other exact-law results in uninspected or unindexed literature are not excluded.

## References

1. Yun Zeng, Jian-Feng Cai, Deren Han, and Jiaxin Xie, *Randomized conjugate gradient least squares*, arXiv:2605.25034v1, https://arxiv.org/html/2605.25034v1 (Algorithm 1, Remark 2.1, Eq. (15), and Theorem 2.4).
2. Yun Zeng, Deren Han, Yansheng Su, and Jiaxin Xie, *On adaptive stochastic heavy ball momentum for solving linear systems*, arXiv:2305.05482v3, https://arxiv.org/html/2305.05482v3 (Section 5.2, Algorithm 4).
