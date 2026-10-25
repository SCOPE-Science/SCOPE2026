# A sharp Floquet frontier for periodically balanced primal–dual steps

## Finding

Consider the single-block, dual-extrapolated primal–dual hybrid gradient (PDHG) update for the saddle function \(L(x,y)=xy\). At every step impose a constant, strictly subcritical step product \(\tau_k\sigma_k=r\), where \(0<r<1\), while alternating the dual steps between \(s\) and \(ts\), where \(s>0\) and \(t\geq1\); the primal steps are the reciprocally rescaled values. For every initial pair \((x_0,y_0)\), both iterates converge to the unique saddle \((0,0)\) **if and only if**

\[
 t+t^{-1}<\frac{4+5r^2-2r}{3r}. \tag{1}
\]

At equality a nonzero neutral four-periodic mode exists. Above the threshold some (indeed, generic) initial pairs diverge geometrically, despite positive bounded steps and the strict product bound at every step. The spectrum of the two-step map and the complete transition at equality are given explicitly below.

This formula yields a sharp *dimension-independent* restriction. For the bilinear saddle \(L(x,y)=\langle Ax,y\rangle\), with a real invertible square matrix \(A\), let the common step product be \(\eta>0\) with \(\eta\|A\|_2^2<1\). Such an alternating schedule converges from every initial pair if and only if (1) holds for each \(r_i=\eta s_i(A)^2\), where \(s_i(A)\) are the singular values. Uniformly over all such invertible matrices and allowed products, convergence is guaranteed **exactly when**

\[
 t+t^{-1}<\frac{4\sqrt5-2}{3}, \quad\text{equivalently }\quad
 1\leq t<t_*\approx1.7400666842649546. \tag{2}
\]

At or above this universal contrast limit there exists an admissible scalar problem and a nonconvergent orbit. The most vulnerable normalized singular mode is \(r=2/\sqrt5\), strictly inside \((0,1)\).

The instability also occurs with *strictly* strongly convex primal and dual terms: for \(L(x,y)=xy+(x^2-y^2)/200\), the schedule \((\tau_{2m},\sigma_{2m})=(1/2,1)\), \((\tau_{2m+1},\sigma_{2m+1})=(1/6,3)\) has product \(1/2\) throughout but diverges from \((x_0,y_0)=(1,0)\).

## Assumptions and scope

The primal and dual variables are real. Take the deterministic single-block specialization of the variable-step algorithm of Chambolle, Delplancke, Ehrhardt, Schönlieb and Tang. With a harmless shift in applied-step indices, initialize \(\bar y_0=y_0\) and iterate

\[
 x_{k+1}=\operatorname{prox}_{\tau_k g}(x_k-\tau_k\bar y_k),\qquad
 y_{k+1}=\operatorname{prox}_{\sigma_k f^*}(y_k+\sigma_k x_{k+1}),
 \qquad\bar y_{k+1}=2y_{k+1}-y_k. \tag{3}
\]

For the initial theorem \(g=f^*=0\), so the proximal maps are identities. The steps applied at iteration \(k\) are \(\sigma_{2m}=s\), \(\sigma_{2m+1}=ts\), \(\tau_k=r/\sigma_k\). In the source algorithm step sizes are labelled by the destination iterate, rather than the applied iteration; this is a pure reindexing. These explicitly prescribed alternating steps are an admissible *input sequence* of the update structure but **do not** satisfy the source paper's summable relative-change/quasi-increase hypotheses. They are not claimed to arise under its safeguarded adaptive rules.

For the matrix extension replace \(y\) in the first update by \(A^{\mathsf T}y\), and \(x\) in the second by \(Ax\). All matrices in the stated extension are real, square and invertible. All convergence statements refer to the full unaveraged primal and dual iterates in exact arithmetic, not merely ergodic averages.

## Proof

**Scalar reduction and initialization.** In the bilinear case, \(x_{k+1}=x_k-\tau_k(2y_k-y_{k-1})\) for \(k\geq1\) and \(y_{k+1}=y_k+\sigma_k x_{k+1}\). Eliminating \(x_k=(y_k-y_{k-1})/\sigma_{k-1}\), and putting \(q_k=\sigma_k/\sigma_{k-1}\), gives the exact recurrence

\[
 \binom{y_{k+1}}{y_k}=M_r(q_k)\binom{y_k}{y_{k-1}},
 \quad M_r(q)=\begin{pmatrix}1+q-2r&r-q\\1&0\end{pmatrix}. \tag{4}
\]

The first step has \(y_1=(1-r)y_0+s x_0\). Hence every desired initial recurrence pair \((y_1,y_0)\) is realized by some \((x_0,y_0)\); no hidden constraint discards an unstable mode. Alternation implies \(q_{2m+1}=t\), \(q_{2m+2}=t^{-1}\), so the exact two-step matrix on \((y_{2m+1},y_{2m})\) is \(B=M_r(t^{-1})M_r(t)\).

**Characteristic polynomial and sharp stability boundary.** Write \(S=t+t^{-1}\). Direct multiplication yields

\[
 \operatorname{tr}B=2(1+2r^2-r(1+S)),\qquad
 \det B=1+r^2-rS. \tag{5}
\]

For a real monic quadratic \(z^2-Tz+D\), both roots are strictly inside the unit disk exactly when \(1-T+D>0\), \(1+T+D>0\), and \(1-D>0\). Here these three quantities equal, respectively,

\[
 r(S+2-3r),\quad 4+5r^2-2r-3rS,\quad r(S-r). \tag{6}
\]

The first and third are strictly positive for all \(0<r<1\), \(S\geq2\), leaving precisely (1). The bounded, nonzero dual-step values make convergence of \(y_k\) equivalent to convergence of the full pair \((x_k,y_k)\) to zero. When the middle expression in (6) vanishes, the two multipliers are exactly \(-1\) and \((1+2r^2-2r)/3\), the second lying in \([1/6,1/3)\); a nonzero four-periodic orbit follows. When it is negative, the characteristic polynomial is negative at \(z=-1\) and positive for sufficiently negative \(z\), so an eigenvalue is less than \(-1\). Arbitrary initial recurrence pairs are reachable, proving divergence for generic initial data.

**An exact unstable orbit.** At \(r=1/2\), \(s=1\), \(t=3\),

\[
 B=\begin{pmatrix}7/6&-5/6\\3&-5/2\end{pmatrix},\qquad
 \lambda_-=\frac{-4-\sqrt{31}}6<-1.
\]

With \(y_0=1\) and \(x_0=(2-\sqrt{31})/18\), the first step gives \(y_1=(11-\sqrt{31})/18\); \((y_1,y_0)\) is an eigenvector with eigenvalue \(\lambda_-\), so its magnitude grows exactly like \(|\lambda_-|^m\) after \(m\) two-step periods.

**Sharp all-spectrum threshold.** Under a singular-value decomposition of invertible \(A\), orthogonal changes of primal and dual coordinates decouple (3) into identical scalar recurrences with normalized products \(r_i=\eta s_i(A)^2\). The criterion is therefore necessary and sufficient modewise. Minimizing \(S_c(r)=(4+5r^2-2r)/(3r)=4/(3r)+5r/3-2/3\) over \(0<r<1\) gives its unique minimizer \(r=2/\sqrt5\) and its minimum \((4\sqrt5-2)/3\). This value is attained at an admissible product below one, so strictness in (2) is necessary.

**A strongly convex witness.** Let \(\varepsilon=1/100\), \(g(x)=\varepsilon x^2/2\), \(f^*(y)=\varepsilon y^2/2\), and retain the last alternating schedule. The unique saddle is \((0,0)\). On the state \((x_k,y_k,y_{k-1})\), a step with parameters \((\tau,\sigma)\) acts by

\[
 T(\tau,\sigma)=\begin{pmatrix}
 a&-2a\tau&a\tau\\
 b\sigma a&b(1-2\sigma a\tau)&b\sigma a\tau\\
 0&1&0
 \end{pmatrix},\quad a=(1+\varepsilon\tau)^{-1},\ b=(1+\varepsilon\sigma)^{-1}. \tag{7}
\]

The first step agrees with (7) when \(y_{-1}=y_0\). The exact two-step matrix \(P=T(1/6,3)T(1/2,1)\) has characteristic polynomial

\[
 \det(zI-P)=\frac{z(1256692803z^2+1571570000z-500000000)}{1256692803}. \tag{8}
\]

The quadratic numerator at \(z=-1\) is \(-814877197\), so one nonzero multiplier is below \(-1\); its other nonzero multiplier lies strictly between zero and one. The initial state \((1,0,0)\) excites the expanding mode: the determinant formed by the first two coordinates of \(P(1,0,0)^{\mathsf T}\) and \(P^2(1,0,0)^{\mathsf T}\) is exactly

\[
 \frac{3638000000000000000}{1579276801111996809}>0. \tag{9}
\]

If the unstable coefficient were zero, the two vectors would lie on the same surviving stable eigendirection (the zero eigendirection has vanished after multiplication by \(P\)), contradicting (9). Thus this explicit strictly convex–concave saddle exhibits geometric divergence under constant product \(1/2<1\).

## Verification

Run `python verify.py` with the dependency declared in `requirements.txt`. The program symbolically reconstructs the two-step characteristic polynomial, all three Schur margins, the universal minimum, the exact growing bilinear eigenpair, the direct-versus-eliminated recurrences, and the rational strongly convex monodromy characteristic polynomial and excitation minor. It reports `VERIFY_OK` only after all assertions pass. These checks reproduce the identities supporting the analytic proof; finite trajectories alone are not used to infer the universal claims.

## Relationship to prior work

Chambolle et al., *Stochastic Primal–Dual Hybrid Gradient Algorithm with Adaptive Step Sizes*, arXiv:2301.02511 (first public January 6, 2023), defines precisely the dual-extrapolated update and the reciprocal balancing rule. Their Theorem 2.1 requires both a strict step-product bound and controlled quasi-increasing step sequences. The present period-two schedules violate the latter condition, so this theorem does not contradict their convergence guarantee.

Goldstein et al., *Adaptive Primal-Dual Hybrid Gradient Methods for Saddle-Point Problems* (2013), and Goldstein, Li and Yuan, *Adaptive Primal-Dual Splitting Methods for Statistical Learning and Image Processing* (2015), already explicitly note that a subcritical product alone does not guarantee convergence under changing steps. Accordingly, *existence of variable-step PDHG divergence is prior*. Their papers use a primal-extrapolated update and do not give the sharp period-two stability frontier for the dual-extrapolated update (3), its all-spectrum contrast minimum or the exact strictly convex witness. Bonettini and Ruggiero analyze variable-step image-restoration methods under different convergence assumptions. None of these established statements implies formulas (1)–(9) as an identified theorem. This is a best-knowledge comparison, not proof of global novelty.

## Limitations

The sharp full classification is for deterministic, single-block, dual-extrapolated PDHG on bilinear invertible couplings with exactly two-periodic reciprocal steps, not arbitrary adaptive sequences, noninvertible operators or randomized block sampling. The contrast restriction is dimension-independent as a qualitative stability guarantee but supplies no matrix-uniform convergence rate. The strongly convex case is an explicit instability witness rather than an all-parameter classification. In particular, these results do not assert that the authors' safeguarded balancing rules diverge. Prior warnings about possible nonconvergence of variable-step PDHG are not claimed as new. Stronger algebraically equivalent results under another splitting or Floquet terminology remain a literature risk; no independent validation has been performed.

## References

1. A. Chambolle, C. Delplancke, M. J. Ehrhardt, C.-B. Schönlieb and J. Tang, *Stochastic Primal-Dual Hybrid Gradient Algorithm with Adaptive Step-Sizes*, arXiv:2301.02511, v1 posted 2023-01-06; open journal version DOI:10.1007/s10851-024-01174-1. https://arxiv.org/abs/2301.02511
2. T. Goldstein, M. Li, X. Yuan, E. Esser and R. Baraniuk, *Adaptive Primal-Dual Hybrid Gradient Methods for Saddle-Point Problems*, arXiv:1305.0546, 2013. https://arxiv.org/abs/1305.0546
3. T. Goldstein, M. Li and X. Yuan, *Adaptive Primal-Dual Splitting Methods for Statistical Learning and Image Processing*, NeurIPS 28, 2015. https://proceedings.neurips.cc/paper/2015/file/cd758e8f59dfdf06a852adad277986ca-Paper.pdf
4. S. Bonettini and V. Ruggiero, *On the Convergence of Primal–Dual Hybrid Gradient Algorithms for Total Variation Image Restoration*, Journal of Mathematical Imaging and Vision, 2012. https://scispace.com/pdf/on-the-convergence-of-primal-dual-hybrid-gradient-algorithms-1j3f6hju19.pdf
