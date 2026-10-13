# Sharp conditioning penalty for gradient-norm sampling in symmetric block Gauss–Seidel

## Finding
Consider one iteration of randomized symmetric Gauss–Seidel (RSGS) for least squares, using the reflected-column pairs and unnormalized squared-gradient sampling of Sha and Zhang (2024). For every real full-column-rank matrix \(A\in\mathbb R^{m\times n}\), with \(m\ge n\ge2\), and every current residual \(r=b-Ax\) satisfying \(A^{\mathsf T}r\ne0\), let \(\Delta_{\mathrm{raw}}\) denote the expected decrease in squared residual under the published sampling rule. Let \(\Delta_{\mathrm{unif}}\) denote the same expected decrease when the distinct reflected blocks are instead sampled uniformly; the *within-block exact least-squares update is identical* in both experiments. Writing \(\kappa=\lambda_{\max}(A^{\mathsf T}A)/\lambda_{\min}(A^{\mathsf T}A)\), the sharp universal comparison is

\[
\boxed{\frac{\Delta_{\mathrm{raw}}}{\Delta_{\mathrm{unif}}}\ge
\frac{4\sqrt{\kappa}}{(1+\sqrt{\kappa})^2}.}
\]

The coefficient cannot be increased for any prescribed \(\kappa\ge1\): equality occurs for an explicit four-column diagonal matrix and residual. In particular, for \(\kappa>1\) the published sampling rule can yield *less* expected one-step progress than uniform block sampling, and the ratio can approach zero as the condition number increases. At \(\kappa=1\) the published rule cannot be worse than uniform sampling. This is a one-step, instance-independent sharp guarantee, not a claim about comparative iteration counts.

## Assumptions and scope
Let \(I_j=\{j,n+1-j\}\) for \(1\le j\le B=\lceil n/2\rceil\), with duplicate indices removed for the central singleton when \(n\) is odd. Define \(C_j=A_{[:,I_j]}\), \(g_j=C_j^{\mathsf T}r\), \(H_j=C_j^{\mathsf T}C_j\),

\[
 d_j=g_j^{\mathsf T}H_j^{-1}g_j,\qquad w_j=\|g_j\|_2^2.
\]

Full column rank makes every \(H_j\) positive definite, and \(\sum_jw_j=\|A^{\mathsf T}r\|_2^2>0\). The RSGS index probability \(\Pr(i)=\bigl((A_i^{\mathsf T}r)^2+(A_{n+1-i}^{\mathsf T}r)^2\bigr)/(2\|A^{\mathsf T}r\|_2^2)\) aggregates over the two reflected indices to the *block* probability \(w_j/\sum_kw_k\); the odd central singleton has the same aggregated expression. Each selected block is minimized exactly in the two or one selected coordinates. Thus

\[
 \Delta_{\mathrm{raw}}=\frac{\sum_jw_jd_j}{\sum_jw_j},\qquad
 \Delta_{\mathrm{unif}}=\frac1B\sum_jd_j.
\]

Both quantities are strictly positive. No orthogonality between different reflected blocks and no consistency of the least-squares system are assumed. The squared-residual decrease is the same as the decrease in squared solution error in the \(A^{\mathsf T}A\)-energy metric.

## Proof
**Exact local progress.** Minimization over the selected coordinates gives the correction \(C_jH_j^{-1}g_j\) to the residual. It is an orthogonal projection onto \(\operatorname{col}(C_j)\), so by the Pythagorean identity the squared-residual reduction is exactly \(d_j\). Aggregating the published index probabilities yields the preceding formulas.

**Curvature and a sharp comparison.** Put \(a=\lambda_{\min}(A^{\mathsf T}A)>0\) and \(b=\lambda_{\max}(A^{\mathsf T}A)\). Every block Gram matrix is a principal submatrix, so \(aI\preceq H_j\preceq bI\). For every block with \(d_j>0\), the Rayleigh quotient

\[
 v_j:=\frac{w_j}{d_j}=\frac{\|g_j\|_2^2}{g_j^{\mathsf T}H_j^{-1}g_j}
\]

satisfies \(a\le v_j\le b\). If \(d_j=0\), also \(w_j=0\), and that block can be assigned any \(v_j\in[a,b]\). Write \(S=\sum_jd_j>0\), \(\theta_j=d_j/S\), and \(t_j=\sqrt{v_j}\). Therefore \(\theta_j\ge0\), \(\sum_j\theta_j=1\), and \(\sqrt a\le t_j\le\sqrt b\). An exact rearrangement and Cauchy–Schwarz give

\[
\frac{\Delta_{\mathrm{raw}}}{\Delta_{\mathrm{unif}}}
 =\frac{B\sum_j\theta_j^2t_j^2}{\sum_j\theta_jt_j^2}
 \ge\frac{\bigl(\sum_j\theta_jt_j\bigr)^2}{\sum_j\theta_jt_j^2}.
\]

For completeness, set \(u=\sqrt a\), \(v=\sqrt b\), and \(\mu=\sum_j\theta_jt_j\in[u,v]\). The pointwise bound \((t_j-u)(v-t_j)\ge0\) implies \(\sum_j\theta_jt_j^2\le(u+v)\mu-uv\). Direct minimization on \([u,v]\) (the critical point is \(\mu=2uv/(u+v)\)) gives

\[
\frac{\mu^2}{(u+v)\mu-uv}\ge\frac{4uv}{(u+v)^2}
=\frac{4\sqrt\kappa}{(1+\sqrt\kappa)^2}.
\]

This also covers the endpoint \(a=b\) by continuity (or directly). The argument uses an elementary bounded-moment inequality, not any unverified asymptotic approximation.

**Exact sharp witness.** For any \(s\ge1\), take \(m=n=4\), \(A_s=\operatorname{diag}(s,1,1,s)\), \(x=0\), and \(b=r=(-1,-\sqrt{s},0,0)^{\mathsf T}\). The reflected blocks are \(\{1,4\}\) and \(\{2,3\}\). Their exact reductions are \(d_1=1\) and \(d_2=s\), with sampling weights \(w_1=s^2\), \(w_2=s\). Therefore

\[
\Delta_{\mathrm{raw}}=\frac{2s}{s+1},\qquad
\Delta_{\mathrm{unif}}=\frac{s+1}{2},\qquad
\frac{\Delta_{\mathrm{raw}}}{\Delta_{\mathrm{unif}}}=\frac{4s}{(s+1)^2}.
\]

Since \(\kappa(A_s^{\mathsf T}A_s)=s^2\), equality holds at each chosen \(\kappa\ge1\). At \(s=4\), the matrix and residual have rational entries, the two expected decreases are \(8/5\) and \(5/2\), and their ratio is \(16/25\). As \(s\to\infty\), the ratio tends to zero. This proves optimality of the full quantified bound.

## Verification
Run `python3 verify.py` in the same directory as this document; the checker uses only the Python standard library. It checks the exact four-dimensional witness, exact equality at \(68\) further rational sharpness instances, and exact projected reductions and sampling comparisons on a seeded collection of nonsingular, generally nonorthogonal integer matrices with \(2\le n\le9\). The check returned `PASS: 1269 exact-projection, sampling, and sharp-frontier cases`. Fraction arithmetic validates projection identities and ratios; floating-point block-eigenvalue calculations are diagnostic checks only. The continuous-parameter and all-dimension assertion is established by the proof, not the finite checker.

## Relationship to prior work
Sha and Zhang (2024), equations (3.1)–(3.6), Algorithm 1, and Theorem 1, supply the reflected-coordinate projection algorithm, its raw-gradient-squared probability law, and convergence guarantees. Their paper does not state the exact sharp one-step ratio to a *uniform reflected-block* competitor. The comparison here concerns the same per-block projection, changing only sampling probabilities.

Gower, Molitor, Moorman, and Needell (2019), Section 2.4 and Theorem 11, already analyze adaptive probabilities proportional to the *sketched loss* (the realized squared projection decrease), rather than the raw gradient norm. In the current notation that established rule is \(\Pr(j)\propto d_j\), yielding \((\sum_jd_j^2)/(\sum_jd_j)\ge(\sum_jd_j)/B\). That known dominance is *not* claimed as new; the present distinction is the exact sharp penalty for the 2024 algorithm's different weighting.

Tian, Khosoussi, Rosen, and How (2019/2021) use squared block-gradient probabilities for a Riemannian block method. Their analysis obtains convergence bounds and empirical comparisons, not the claimed exact least-squares reflected-block extremal factor. The moment inequality used in the proof is classical; its sharp application to the specified paired-coordinate rule and matching construction are the claim. Equivalence under alternative sampling terminology remains a priority risk.

## Limitations
The theorem compares *conditional expected squared-residual decreases for one step* and does not compare wall-clock sampling costs, full trajectories, or asymptotic iteration complexity. Its sharpness is over full-column-rank inputs of specified condition number, not an assertion that all such inputs are worst-case. Uniform sampling here means uniform over the distinct reflected pairs (including any singleton), not uniform over all two-element subsets. The result assumes exact arithmetic and exact block minimization.

## References
1. Fan Sha and Jianbing Zhang, “Randomized symmetric Gauss-Seidel method for solving linear least squares problems,” *AIMS Mathematics* 9(7) (2024), 17453–17463, DOI: `10.3934/math.2024848`. First online publication: 2024-05-23. Primary MSC2020: `65F10`. Full text: https://www.aimspress.com/aimspress-data/math/2024/7/PDF/math-09-07-848.pdf.
2. Robert M. Gower, Denali Molitor, Jacob Moorman, and Deanna Needell, “Adaptive Sketch-and-Project Methods for Solving Linear Systems,” arXiv:`1909.03604` (2019), Section 2.4 and Theorem 11. Full text: https://arxiv.org/html/1909.03604v1.
3. Yulun Tian, Kasra Khosoussi, David M. Rosen, and Jonathan P. How, “Distributed Certifiably Correct Pose-Graph Optimization,” arXiv:`1911.03721` (2019; inspected version v6, 2021), Section 4.1 and convergence appendix. Full text: https://arxiv.org/pdf/1911.03721.
