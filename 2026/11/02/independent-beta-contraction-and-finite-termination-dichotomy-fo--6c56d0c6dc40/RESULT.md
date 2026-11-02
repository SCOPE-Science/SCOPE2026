# Independent-beta contraction and finite-termination dichotomy for Gaussian-sketch RCGLS

## Finding
For independent real rank-one standard-Gaussian sketches in the exact-line-search randomized conjugate-gradient least-squares (RCGLS) iteration of Zeng, Cai, Han, and Xie, let \(d\) be the full column rank and begin with any deterministic \(x^0\ne x_*\). In exact arithmetic, \(d=1\) gives one-step termination, \(d=2\) gives two-step termination almost surely, whereas \(d\ge3\) gives **zero probability of termination at any finite iteration**. These assertions concern genuine nonzero sketch directions; the probability of a degenerate direction at any finite step is zero.

If additionally \(A^{\mathsf T}A=I_d\), then for every \(d\ge3\) and integer \(k\ge1\), the normalized squared solution error has the **exact independent-factor distribution**
\[
 R_k:=\frac{\|x^k-x_*\|_2^2}{\|x^0-x_*\|_2^2}\ \overset{\mathrm d}=\ U\prod_{j=1}^{k-1}V_j,
\quad U\sim\operatorname{Beta}\left(\frac{d-1}{2},\frac12\right),
\quad V_j\stackrel{\mathrm{iid}}\sim\operatorname{Beta}\left(\frac{d-2}{2},\frac12\right),
\]
where all factors are independent. Consequently,
\[
 \mathbb E R_k=\frac{d-1}{d}\left(\frac{d-2}{d-1}\right)^{k-1},\qquad
 \lim_{k\to\infty}\frac{\log R_k}{k}
 =\psi\left(\frac{d-2}{2}\right)-\psi\left(\frac{d-1}{2}\right)<0
 \quad\text{almost surely},
\]
with \(\psi\) the digamma function. The two-dimensional termination statement is also a consequence of the older full-memory rank-two theory; the proposed new contribution is the finite-memory obstruction in higher dimensions and, especially, the full Gaussian factorization, exact moments, and almost-sure exponent.

## Assumptions and scope
Let \(A\in\mathbb R^{n\times d}\) have full column rank with \(n\ge d\ge1\), let \(b\in\mathbb R^n\) be deterministic, \(H=A^{\mathsf T}A\succ0\), and \(x_*=H^{-1}A^{\mathsf T}b\). Independently sample \(g_k\sim N(0,I_d)\) for integers \(k\ge0\), and take the source method's rank-one sketches \(S_k=g_k\). Write the error \(e_k=x_*-x^k\) and \(\|w\|_H^2=w^{\mathsf T}Hw\). At iteration zero use the direction \(p_0=(g_0^{\mathsf T}He_0)g_0\). Subsequently set
\[
 P_{k-1}=I-\frac{p_{k-1}p_{k-1}^{\mathsf T}H}{p_{k-1}^{\mathsf T}Hp_{k-1}},\qquad
 p_k=(g_k^{\mathsf T}He_k)P_{k-1}g_k\quad(k\ge1),
\]
and perform the exact line search
\[
 e_{k+1}=e_k-\frac{e_k^{\mathsf T}Hp_k}{p_k^{\mathsf T}Hp_k}p_k.
\]
These are algebraically the same directions and steps as Algorithm 1 of arXiv:2605.25034v1, since the method first forms \(S_kS_k^{\mathsf T}A^{\mathsf T}(b-Ax^k)\) and removes the previous \(H\)-direction's component. The finite-termination claims allow any positive-definite \(H\). The beta-factorization additionally requires \(H=I_d\), not merely a bounded condition number; Gaussian sketching is not affine-invariant.

## Proof
**Projection reduction.** Exact line search at step \(k-1\) implies \(e_k^{\mathsf T}Hp_{k-1}=0\), so for \(k\ge1\) we also have \(e_k^{\mathsf T}HP_{k-1}g_k=e_k^{\mathsf T}Hg_k\). The scalar multiplying the direction cancels from the update almost surely. Thus
\[
 e_{k+1}=e_k-\frac{e_k^{\mathsf T}Hw_k}{w_k^{\mathsf T}Hw_k}w_k,\quad
 w_0=g_0,\quad w_k=P_{k-1}g_k\ (k\ge1).
\]
The operator \(P_{k-1}\) is the \(H\)-orthogonal projection onto the \((d-1)\)-dimensional hyperplane \(p_{k-1}^{\perp_H}\). Conditional on the past and nonzero \(e_k\), the law of \(w_k\) has a nondegenerate Gaussian density relative to that hyperplane. Since \(e_k\) lies in that hyperplane, the residual after projection is zero precisely when \(w_k\) is collinear with \(e_k\). For \(d\ge3\), that one-dimensional subset has measure zero in the hyperplane of dimension at least two. The first-step direction similarly misses the error with probability one for \(d\ge2\). By induction and a countable union, no finite step terminates when \(d\ge3\). For \(d=2\), the post-first-step hyperplane is one dimensional and contains \(e_1\), so step two terminates a.s.; the scalar case terminates at step one.

**Isotropic factorization.** Under \(H=I_d\), conditional on the entire past, \(u_k=w_k/\|w_k\|_2\) is uniform on the unit sphere in the allowed subspace, of dimension \(d\) at step zero and dimension \(d-1\) thereafter. Moreover \(e_k\) is a nonzero deterministic vector in the allowed hyperplane once the past is fixed. Its normalized projection onto \(u_k\) has squared magnitude distributed as \(\operatorname{Beta}(1/2,(m-1)/2)\) in an \(m\)-dimensional sphere, from the ratio of two independent chi-square variables. Orthogonal subtraction thus leaves a squared-norm factor \(\operatorname{Beta}((m-1)/2,1/2)\). Here \(m=d\) for the first iteration and \(m=d-1\) at every later iteration. Crucially these conditional factor laws do not depend on the past. Induction on conditional expectations therefore proves mutual independence of all factors, not just equality of their marginal laws.

**Moments and asymptotic rate.** The mean of a \(\operatorname{Beta}(a,b)\) variable is \(a/(a+b)\), giving the displayed exact expectation. For each \(d\ge3\), the logarithm of a later factor is integrable, and its mean is \(\psi((d-2)/2)-\psi((d-1)/2)\), which is negative because \(\psi\) is strictly increasing. The strong law for the independent identically distributed later logarithmic factors proves the almost-sure limit, as the single initial factor has vanishing normalized logarithmic contribution. Every finite factor is strictly positive almost surely, fully consistent with infinite exact nontermination.

## Verification
Run `python3 verify.py` with Python 3 and NumPy. The program uses exact rational arithmetic for nonorthogonal two- and three-dimensional positive-definite instances, tests 450 independently seeded two-dimensional Gaussian runs, and compares empirical factor expectations on 40,000 simulated length-three paths at dimensions \(3,4,7,12\). The two-dimensional floating-point residuals remain at round-off scale and empirical factor means match the exact beta means within the declared tolerances. The infinite claims, independence, and nontermination probability are proved above, not inferred from finite experiments.

## Relationship to prior work
Zeng, Cai, Han, and Xie (arXiv:2605.25034v1, Section 2, especially Algorithm 1 and Theorem 2.4) introduce RCGLS and establish conditional expected linear-contraction bounds, with Gaussian sketches permitted. Their theorem is an inequality and does not give this exact isotropic independent-factor law or an almost-sure nontermination dichotomy.

Sun, Han, and Xie (arXiv:2505.20602v1, Sections 2–3, Remark 3.6) analyze a projected sketching iteration with limited previous-iterate memory that is equivalent to the present two-direction projection after an appropriate change of least-squares coordinates. They give expected-rate bounds and a finite-termination guarantee when memory reaches the rank; their rank-two case already covers the dimension-two endpoint and is **not** claimed as new. Their stated results do not determine the beta-factor law or prove the higher-dimensional finite-memory nontermination property. The older projection-based least-squares methods of Brust and Saunders (arXiv:2207.07615) retain substantially more history and have a different finite-termination mechanism. Prior knowledge of spherical beta ratios and chi-square laws is treated as standard, not independently novel.

## Limitations
The full law is for independent continuous Gaussian rank-one sketches and exactly orthonormal design columns. The termination dichotomy extends to any SPD normal-equation Hessian, but no equivalent beta factorization is asserted there. The normal equations must have a unique solution; finite-precision stopping criteria may trigger in finitely many iterations even where exact mathematical termination has probability zero. No new claim is made about the known two-dimensional memory-rank finite-termination principle. Literature overlap beyond the inspected sources, especially other randomized projection analyses, remains a priority risk. This has not undergone independent mathematical review.

## References
1. Y. Zeng, J.-F. Cai, D. Han, J. Xie. *Randomized conjugate gradient least squares*. arXiv:2605.25034v1, first public 2026-05-24. https://arxiv.org/html/2605.25034
2. Y. Sun, D. Han, J. Xie. *Connecting randomized iterative methods with Krylov subspaces*. arXiv:2505.20602v1, first public 2025-05-27. https://arxiv.org/html/2505.20602v1
3. J. Brust, M. A. Saunders. *A Projected Linear Systems Solver for Large-Scale Linear Systems*. arXiv:2207.07615. https://arxiv.org/abs/2207.07615
