# Sharp coordinate-sampling threshold and unbounded one-step sketched GMRES residual on near-identity SPD systems

## Finding

Let \(n\ge2\) and \(1\le s<n\). If a row sketch \(S\) samples the \(s\) largest-magnitude coordinates of a unit vector \(b\), then a real symmetric positive-definite matrix \(A\) can annihilate the whole sketched image \(SAb\) only if
\[
\kappa_2(A)\ge \kappa_{n,s}:=\frac{1+\sqrt{s/n}}{1-\sqrt{s/n}}.
\]
This sharp, dimension-dependent spectral threshold is attained with equal-magnitude coordinates. The globally best row sketch for the basis-only objective \(\sigma_{\min}(Sb)\) can nevertheless yield an unbounded true residual from the one-dimensional sketched GMRES least-squares problem, even when \(A\) is positive definite and arbitrarily close in spectral condition number to the identity as \(s/n\to0\). The one-row instance coincides with the choice of DEIM and Q-DEIM in the deterministic sketching method of [1]. The extension to \(s>1\) concerns the *global maximizer* of the basis-only criterion, not a claim about all practical oversampling heuristics.

## Assumptions and scope

All statements concern real exact arithmetic. Take integers \(n\ge2\), \(1\le s<n\), and a unit vector \(b\in\mathbb R^n\). Let \(S\in\mathbb R^{s\times n}\) consist of distinct rows of the identity, chosen to maximize \(\sigma_{\min}(Sb)=\|Sb\|_2\) over all \(s\)-row coordinate selectors. Thus its rows select the largest absolute coordinates of \(b\), and \(\theta:=\|Sb\|_2\ge\sqrt{s/n}\). Write \(P=S^\top S\), the coordinate projector.

For a positive-definite \(A\), define \(\kappa_2(A)=\lambda_{\max}(A)/\lambda_{\min}(A)\). With the initial guess \(x_0=0\), one-dimensional Krylov basis \(b\), and \(SAb\ne0\), the sketched GMRES iterate is \(\widehat x=b\widehat t\), where
\[
\widehat t=\underset{t\in\mathbb R}{\arg\min}\,\|S(Abt-b)\|_2.
\]
The ordinary one-step GMRES iterate minimizes \(\|Abt-b\|_2\) instead. Neither an affine-subspace embedding of \(\operatorname{span}\{b,Ab\}\) nor more than one Krylov vector is assumed.

## Proof

**1. Sharp necessary condition.** Let \(0<\mu=\lambda_{\min}(A)\le L=\lambda_{\max}(A)\). Decompose
\[
A=\alpha I+E,\quad \alpha=\frac{L+\mu}{2},\quad \|E\|_2\le\rho:=\frac{L-\mu}{2}.
\]
Because \(\|S\|_2=1\) and \(\|b\|_2=1\),
\[
\|SAb\|_2\ge\alpha\|Sb\|_2-\|SEb\|_2\ge\alpha\theta-\rho.
\]
If \(SAb=0\), then \(\theta\le\rho/\alpha=(\kappa_2(A)-1)/(\kappa_2(A)+1)\). Rearranging gives \(\kappa_2(A)\ge(1+\theta)/(1-\theta)\). Selecting the largest \(s\) squared coordinates of a unit vector gives \(\theta^2\ge s/n\), proving the claimed bound and strict nonvanishing below \(\kappa_{n,s}\).

**2. An attaining involution.** For any \(\theta\in(0,1)\), let \(u=Pb/\theta\), so \(\|u\|_2=1\) and \(u^\top b=\theta\). The vectors
\[
u_+=\frac{b+u}{\sqrt{2(1+\theta)}},\qquad u_-=\frac{b-u}{\sqrt{2(1-\theta)}}
\]
are orthonormal. Therefore \(H=u_+u_+^\top-u_-u_-^\top\) is symmetric, has one eigenvalue \(+1\), one \(-1\), and remaining eigenvalues zero, and direct substitution gives \(Hb=u\) and \(Hu=b\). Thus
\[
A_0=I-\theta H\succ0,\qquad \kappa_2(A_0)=\frac{1+\theta}{1-\theta},\qquad A_0b=b-Pb.
\]
Since \(S(b-Pb)=0\), this attains the stronger vector-specific lower bound. For \(b\) having equal-magnitude coordinates, \(\theta=\sqrt{s/n}\), attaining the dimensionwise threshold. If a unique maximizing subset is desired, choose a slightly nonuniform \(b\), giving arbitrarily close (but not necessarily equal) condition numbers above the threshold.

**3. A unique maximizing sketch and a nonsingular catastrophic update.** Fix \(q>1\) and define
\[
b=\frac{(q\mathbf1_s,\mathbf1_{n-s})^\top}{\sqrt{s q^2+n-s}},\qquad
\theta=\frac{q\sqrt{s}}{\sqrt{s q^2+n-s}}.
\]
The first \(s\) rows are the *unique* maximizer of \(\|Sb\|_2\). Using the involution from step 2, define \(A_\eta=(1+\eta)I-\theta H\) for \(\eta>0\). Its eigenvalues are \(1+\eta-\theta\), \(1+\eta+\theta\), and \(1+\eta\) (the last with multiplicity \(n-2\)); thus it is positive definite with
\[
\kappa_2(A_\eta)=\frac{1+\eta+\theta}{1+\eta-\theta}.
\]
The exact identities
\[
A_\eta b=(1+\eta)b-\theta u,\qquad SA_\eta b=\eta Sb
\]
show that the sketched least-squares coefficient is \(\widehat t=1/\eta\), even though \(SA_\eta b\ne0\). The resulting full residual is
\[
b-\widehat t A_\eta b=-\frac{b-Pb}{\eta},\qquad
\|b-\widehat t A_\eta b\|_2=\frac{\sqrt{1-\theta^2}}{\eta}.
\]
For ordinary GMRES, the minimum residual is the distance from \(b\) to the line spanned by \(A_\eta b\). Since \(b^\top A_\eta b=1+\eta-\theta^2\) and
\[
\|A_\eta b\|_2^2=(1+\eta)^2-(1+2\eta)\theta^2,
\]
its exact value is
\[
\min_t\|b-tA_\eta b\|_2
=\sqrt{1-\frac{(1+\eta-\theta^2)^2}{\|A_\eta b\|_2^2}}
=\frac{\theta\sqrt{1-\theta^2}}{\|A_\eta b\|_2}.
\]
Consequently, the residual ratio is exactly
\[
\frac{\|b-\widehat t A_\eta b\|_2}{\min_t\|b-t A_\eta b\|_2}
=\frac{\|A_\eta b\|_2}{\theta\eta}\xrightarrow[\eta\downarrow0]{}\infty.
\]
For every \(K>\kappa_{n,s}\), choosing \(q>1\) sufficiently close to one makes \((1+\theta)/(1-\theta)<K\); then every \(A_\eta\) has condition number below \(K\). For any fixed \(s\) and fixed \(q>1\), sending \(n\to\infty\) gives \(\theta\sim q\sqrt{s/n}\) and \(\kappa_2(A_\eta)\to1\) uniformly in \(\eta\ge0\). Taking \(\eta\downarrow0\) afterwards retains the unbounded residual ratio. If \(n\ge2s\), a sample of \(s\) rows outside the first group instead gives \(\widehat t=1/(1+\eta)\) and true residual norm \(\theta/(1+\eta)\); the pathology is specific to the basis-maximizing row choice, not every \(s\)-row choice.

## Verification

The accompanying `check.py` builds the stated symmetric involutions, verifies their spectra, the exact sampled/unsampled residual identities, optimal one-step GMRES coefficients, and alternative sampled rows for integers \(2\le n\le26\) and all \(1\le s<n\) using four amplitude ratios and three perturbation sizes. It independently tests the lower spectral bound on seeded random positive-definite examples for \(2\le n\le30\). Run `python check.py` after installing the Python dependency in `requirements.txt`. The observed run completed **62,206 assertions**. Those finite tests are supplementary; the displayed analytic proof establishes the all-dimension/all-parameter statements.

## Relationship to prior work

Bergermann [1, Sections 3–5, especially Algorithm 5] proposes basis-specific deterministic row sketches and the objective of maximizing the smallest singular value of the sampled Krylov basis, while dsGMRES solves a least-squares problem involving the *sampled image* of that basis. The present result identifies a sharp gap between these two objects, including the case of exact global optimization of the basis-only objective. For a single Krylov vector and a single sampled row, the chosen coordinate is exactly that selected by DEIM or Q-DEIM; for more sampled rows the theorem is about the globally best basis-only selector, not a verified execution of a named oversampling heuristic.

Nakatsukasa and Tropp [2] prove residual comparisons under genuine embeddings of the affine residual subspace; here this hypothesis is *not* assumed, and the result does not contradict it. Burke, Carson, and Ma [3] analyze backward stability under appropriate sketch and conditioning assumptions, not this rank-one row-selection threshold. The DEIM/GappyPOD literature [4,5] concerns stable recovery of vectors from samples of their own reduced bases; it does not supply the operator-image zero criterion established here. The norm inequality in step 1 is elementary and is not asserted as independently new.

## Limitations

The result concerns one Krylov dimension, real exact arithmetic, symmetric positive-definite systems, and a global maximizer of a basis-only coordinate-selection objective. It does not prove a failure of randomized embeddings, of all DEIM oversampling heuristics, of higher-dimensional restarted Krylov implementations, or of sketching strategies that explicitly certify the affine residual space. Finite computation does not prove the universal statements. The historical search may miss a specialized published equivalent of the sharp operator-image bound; the claimed contribution is the method-specific threshold and resulting unbounded sketched-versus-unsketched residual behavior.

## References

[1] K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1, first submitted 2026-04-08, https://arxiv.org/abs/2604.07158 .

[2] Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113, https://arxiv.org/abs/2111.00113 .

[3] L. Burke, E. Carson, and Y. Ma, *On the numerical stability of sketched GMRES*, arXiv:2503.19086, https://arxiv.org/abs/2503.19086 .

[4] B. Peherstorfer, Z. Drmač, and S. Gugercin, *Stability of discrete empirical interpolation and gappy proper orthogonal decomposition with randomized and deterministic sampling points*, arXiv:1808.10473, https://arxiv.org/abs/1808.10473 .

[5] Z. Drmač and S. Gugercin, *A New Selection Operator for the Discrete Empirical Interpolation Method*, arXiv:1505.00370, https://arxiv.org/abs/1505.00370 .
