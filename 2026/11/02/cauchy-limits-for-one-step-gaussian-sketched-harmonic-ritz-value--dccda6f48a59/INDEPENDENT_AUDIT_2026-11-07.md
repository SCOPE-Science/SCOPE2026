# Independent mathematical audit

## correctness

PASS

Set u=Ab, w=b, alpha=u·w/||u||^2>0 and delta^2=||w||^2/||u||^2-alpha^2. With Gaussian sketch S independent of fixed b, orthogonal Gaussian components g,h yield R=Theta^(-1)=alpha+delta(g·h)/||g||^2 distributed as alpha+(delta/sqrt(s))T_s. For delta>0 its Student density is smooth and positive at 0, hence Theta=1/R has both sign tails f_R(0)/t, absolute moment cutoff p<1, and no signed first moment. The characteristic function has expansion 1+i m_PV t -pi f_R(0)|t|+o(|t|), so iid arithmetic means converge to nondegenerate Cauchy(m_PV,pi f_R(0)). Independently checked 2D exact SPD example A=diag(1,2), b=(1,1), alpha=3/5, delta=1/5, s=1, f_R(0)=1/(2*pi). Eigenvector delta=0 gives constant exceptional case. This concerns fixed finite s, not simultaneous s,N limits.

## originality

PASS

After independent comparison of statement/implication and the source inspections below, the final claim is original to the best of present knowledge, subject to the named residual risks. The Gaussian consequence is not presented in the prior harmonic reciprocal analysis.

## value

PASS

The precise heavy-tail obstruction to averaging Gaussian-sketch harmonic Ritz values is a natural phenomenon in a broadly used numerical linear-algebra estimator. It distinguishes convergence under sufficient embedding events from unconditional finite-sketch moments and demonstrates that adding independent sketches without increasing sketch dimension cannot consistently average the harmonic estimator, despite the SPD underlying matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
