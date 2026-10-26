# Sharp rank-one spectral-conditioning regret of Bregman log-determinant preconditioning

## Finding

For each \(M>1\) and \(0<\varepsilon<1\), let
\[
S=\operatorname{diag}(\varepsilon,1,M),\qquad
\mathcal P_1=\{I+W:\ W=W^*,\ \operatorname{rank}W\le1,\ I+W\succ0\}.
\]
Define the Bregman log-determinant discrepancy and the symmetric preconditioned condition number by
\[
\mathcal D(S,P)=\operatorname{tr}(SP^{-1})-\log\det(SP^{-1})-3,\qquad
\kappa(S,P)=\frac{\lambda_{\max}(P^{-1/2}SP^{-1/2})}{\lambda_{\min}(P^{-1/2}SP^{-1/2})}.
\]
Put \(\phi(z)=z-\log z-1\). There is a unique \(\varepsilon_*(M)\in(0,1)\) satisfying \(\phi(\varepsilon_*)=\phi(M)\), equivalently
\[
\varepsilon_*e^{-\varepsilon_*}=Me^{-M}.
\]
It obeys \(0<\varepsilon_*(M)<1/M\). The unique divergence-minimizing rank-one preconditioner, except at \(\varepsilon=\varepsilon_*\), is
\[
P_{\mathrm{BLD}}=\begin{cases}
\operatorname{diag}(\varepsilon,1,1),&0<\varepsilon<\varepsilon_*,\\
\operatorname{diag}(1,1,M),&\varepsilon_*<\varepsilon<1.
\end{cases}
\]
At the equality boundary both displayed matrices, and no others, minimize the divergence.

In contrast, the **global** optimum over all Hermitian rank-one corrections (not only diagonal corrections) satisfies
\[
\inf_{P\in\mathcal P_1}\kappa(S,P)=\min\{M,\varepsilon^{-1}\}.
\]
The first displayed preconditioner attains \(M\), and the second attains \(\varepsilon^{-1}\). Hence for the uniquely selected BLD preconditioner the exact condition-number approximation ratio is
\[
\frac{\kappa(S,P_{\mathrm{BLD}})}{\inf_{P\in\mathcal P_1}\kappa(S,P)}
=\begin{cases}
(M\varepsilon)^{-1},&\varepsilon_*(M)<\varepsilon<1/M,\\
1,&0<\varepsilon<\varepsilon_*(M)\ \text{or}\ 1/M\le\varepsilon<1.
\end{cases}
\]
At \(\varepsilon=\varepsilon_*\), the two divergence minimizers have distinct conditioning; the worse has ratio \((M\varepsilon_*)^{-1}\).
For fixed \(M\), the sharp supremum of the ratio over parameter values with a unique BLD minimizer is
\[
\frac{1}{M\varepsilon_*(M)}\sim\frac{e^M}{M^2}\quad(M\to\infty).
\]
Thus divergence-optimal rank-one preconditioning can be arbitrarily worse than rank-one condition-number-optimal preconditioning, even for a diagonal positive-definite matrix with the baseline eigenvalue \(1\) in the spectrum.

## Assumptions and scope

All matrices are finite-dimensional complex Hermitian; the example itself is real and diagonal. The approximate factor is fixed at \(Q=I\), and the admissible preconditioners are exactly positive-definite Hermitian rank-one corrections \(I+W\). The positive-definiteness and low-rank requirements are simultaneous, not relaxed. The baseline middle eigenvalue \(1\) fixes the normalization. The discrepancy is directed as \(\mathcal D(S,P)\), not \(\mathcal D(P,S)\). The theorem covers every real \(M>1\) and every \(\varepsilon\in(0,1)\), with explicit tie conventions. The same construction can be padded with additional unit eigenvalues in any dimension at least three; no general statement for arbitrary spectra is asserted.

## Proof

**1. Divergence optimizer.** Every nonzero Hermitian rank-one correction has the form \(W=wvv^*\), where \(\lVert v\rVert_2=1\), \(w\in(-1,0)\cup(0,\infty)\). Sherman–Morrison and the determinant lemma give
\[
\mathcal D(S,I+wvv^*)-\mathcal D(S,I)
=-\frac{w}{1+w}v^*Sv+\log(1+w).
\]
For fixed \(w>0\), minimizing this expression means maximizing \(v^*Sv\), uniquely selecting the \(M\)-eigenvector. For fixed \(-1<w<0\), the sign reverses and the minimizing direction is uniquely the \(\varepsilon\)-eigenvector. Writing \(u=1+w\), the objective reduction in the selected eigendirection \(\mu\) is optimized at \(u=\mu\), because
\[
\frac{d}{du}\left(-\mu+\frac{\mu}{u}+\log u\right)=\frac{u-\mu}{u^2}.
\]
Relative to \(P=I\), the resulting reduction is \(\phi(\mu)\). Since \(\phi(1)=0\), comparing \(\phi(M)\) with \(\phi(\varepsilon)\) proves the formula for \(P_{\mathrm{BLD}}\). At equal scores, these are the only minimizers because the extremal eigenvalues of \(S\) are simple.

**2. Sharp condition-number optimum without a commuting assumption.** For \(w>0\), the generalized Rayleigh quotient \(R(x)=x^*Sx/(x^*Px)\) at the first coordinate vector satisfies \(R(e_1)\le\varepsilon\). There is a nonzero vector \(x\in\operatorname{span}\{e_2,e_3\}\cap v^\perp\). For this vector \(Px=x\) and \(R(x)\ge1\). Thus \(\kappa(S,P)\ge1/\varepsilon\). For \(-1<w<0\), \(R(e_3)\ge M\), and a nonzero \(x\in\operatorname{span}\{e_1,e_2\}\cap v^\perp\) gives \(R(x)\le1\); hence \(\kappa(S,P)\ge M\). For \(W=0\), \(\kappa(S,I)=M/\varepsilon\). The explicit matrices \(\operatorname{diag}(1,1,M)\) and \(\operatorname{diag}(\varepsilon,1,1)\) attain the respective lower bounds, establishing \(\min\{M,1/\varepsilon\}\) globally over the full Hermitian rank-one class.

**3. Boundary and sharp gap.** Since \(\phi'(z)=1-1/z<0\) for \(0<z<1\), exactly one \(\varepsilon_*\in(0,1)\) has score \(\phi(M)\). Also
\[
\phi(M)-\phi(1/M)=M-1/M-2\log M>0\quad(M>1),
\]
because this difference vanishes at \(M=1\) and has derivative \((M-1)^2/M^2>0\). Hence \(\varepsilon_*<1/M\). Comparing the divergence choice with the spectral-optimal choice proves the exact mismatch interval and ratio. As \(M\to\infty\), the defining identity implies \(\varepsilon_*(M)\to0\) and \(\varepsilon_*(M)/(Me^{-M})=e^{\varepsilon_*(M)}\to1\), giving the sharp fixed-\(M\) supremum and its exponential asymptotic. A concrete unbounded subfamily is \(M\ge8\), \(\varepsilon=M^{-2}\): here \(\phi(M)>\phi(M^{-2})\), while the spectral optimum selects the small eigenvalue, and the condition-number ratio is exactly \(M\).

## Verification

The standalone `verify.py` checks Sherman–Morrison and derivative identities symbolically, tests the exact rational instance \(M=6\), \(\varepsilon=1/20\), isolates several score-crossing roots numerically, and examines 1,200 random positive-definite signed rank-one updates. Running `python verify.py` reports `VERIFY_OK`. The universal optimality statement, tie analysis, and asymptotic are proved above; finite samples alone would not establish them. For the rational instance, the BLD correction has \(\kappa=20\), whereas the optimal rank-one correction has \(\kappa=6\).

## Relationship to prior work

Bock and Andersen's 2023 preprint (arXiv:2312.06417; subsequently published in 2025) introduces exactly the directed divergence and low-rank BLD truncation used here, and its general theorem supplies the established BLD eigenvalue-selection principle. The present result does **not** claim discovery of that principle. It adds a sharp comparison with the *globally optimal spectral condition number across all Hermitian rank-one corrections*, including an exact parameter region and an exponentially diverging worst-case ratio. Their earlier 2023 preprint (arXiv:2304.12162; SIAM J. Matrix Anal. Appl., 2024) derives conditioning optimality for a positive-semidefinite error setting, whereas the example here has an indefinite error \(S-I\). Dhillon–Tropp developed the broader matrix-nearness framework; Higham–Mary studied different low-rank factorization-error preconditioners. None of the accessible closely relevant results inspected established this full signed rank-one spectral comparison; equivalent results elsewhere remain possible.

## Limitations

This is an exact-arithmetic three-eigenvalue benchmark, not a general performance theorem for BLD truncation or a claim that divergence optimization leads to slow conjugate gradients. Spectral condition number alone does not determine the number of CG iterations or runtime; indeed, in three dimensions exact-arithmetic CG terminates in at most three steps. The sharp regret refers to the condition number and the stated fixed rank-one preconditioner class. The first public source date refers to the earliest arXiv version, not the later journal article. No independent audit has been performed.

## References

1. A. A. Bock and M. S. Andersen, *A New Matrix Truncation Method for Improving Approximate Factorisation Preconditioners*, arXiv:2312.06417, first posted 11 December 2023; journal version, *Numerical Linear Algebra with Applications* 32 (2025), e70012. https://arxiv.org/abs/2312.06417 ; https://doi.org/10.1002/nla.70012 .
2. A. Bock and M. S. Andersen, *Preconditioner Design via the Bregman Divergence*, arXiv:2304.12162 (2023); *SIAM Journal on Matrix Analysis and Applications* 45 (2024), 1148–1182. https://arxiv.org/abs/2304.12162 ; https://doi.org/10.1137/23M1566637 .
3. I. S. Dhillon and J. A. Tropp, *Matrix Nearness Problems with Bregman Divergences*, *SIAM Journal on Matrix Analysis and Applications* 29 (2007), 1120–1146. https://doi.org/10.1137/060649021 .
4. N. J. Higham and T. Mary, *A New Preconditioner that Exploits Low-Rank Approximations to Factorization Error*, *SIAM Journal on Scientific Computing* 41 (2019), A59–A82. https://doi.org/10.1137/18M1182802 .
