# Complete fixed-spectrum one-pivot risk laws for rank-two randomized Cholesky

## Finding

Let \(0<\lambda_2<\lambda_1\). Apply exactly one step of diagonal-proportional randomly pivoted Cholesky (RPCholesky) to any nonzero real positive semidefinite matrix \(A\) of rank two with nonzero eigenvalues \(\lambda_1,\lambda_2\). Write \(R=\operatorname{tr}(A-A_{:i}A_{i:}/A_{ii})\) for its random residual trace, where index \(i\) is chosen with probability \(A_{ii}/\operatorname{tr} A\) and indices with zero diagonal are not sampled. Define

\[
 a=\lambda_2,\qquad b=\lambda_1,\qquad m=\frac{2\lambda_1\lambda_2}{\lambda_1+\lambda_2}.
\]

**Complete attainable-law theorem.** Every such \(R\) has finite support in \([a,b]\) and mean \(m\). Conversely, **every finitely supported probability distribution** on \([a,b]\) whose mean is \(m\) is exactly the law of \(R\) for some real rank-two positive semidefinite input with nonzero eigenvalues \(\lambda_1,\lambda_2\). A law with \(q\) support points can be realized by a matrix of dimension \(2q\). The dimension is permitted to vary in this converse; this does not classify laws for a fixed matrix dimension.

Consequently, for any convex function \(\varphi:[a,b]\to\mathbb R\),

\[
 \varphi(m)\le\mathbb E\varphi(R)\le
 \frac{\lambda_1}{\lambda_1+\lambda_2}\varphi(\lambda_2)
 +\frac{\lambda_2}{\lambda_1+\lambda_2}\varphi(\lambda_1).
\]

Both bounds are attainable by real matrices with the same two eigenvalues. In particular,

\[
 0\le\operatorname{Var}(R)\le
 \frac{\lambda_1\lambda_2(\lambda_1-\lambda_2)^2}
 {(\lambda_1+\lambda_2)^2},
\]

and both endpoints are attained. The **sharp spectrum-only upper-tail probability**, over all such matrices of arbitrary dimension, is

\[
 \sup_A\Pr(R\ge u)=
 \begin{cases}
 1,&u\le m,\\[1mm]
 \dfrac{m-\lambda_2}{u-\lambda_2},&m<u\le\lambda_1,\\[2mm]
 0,&u>\lambda_1.
 \end{cases}
\]

Every displayed supremum is attained; for \(m<u\le\lambda_1\), at most four nonzero Gram rows suffice. The mean formula itself is known from the standard expected-residual identity; the attainable-law converse and ensuing exact risk envelope are the conclusions here.

## Assumptions and scope

All matrices and factor rows are real. Arithmetic, pivot probabilities, and residual updates are exact. An input of dimension \(N\ge2\) may have zero eigenvalues beyond the two specified nonzero ones. At least one pivot is chosen. The distributional converse varies \(N\); it does not assert that a given prescribed dimension can realize every finite law. If the eigenvalues coincide, the residual trace is deterministically that common eigenvalue, a degenerate case excluded from the nondegenerate statement. No multistep, floating-point, or approximate-pivot rule is covered.

## Proof

**1. Spectral reduction.** Factor \(A=BB^{\mathsf T}\), where \(B\in\mathbb R^{N\times2}\) has row vectors \(b_i\). A right orthogonal change of basis makes \(S=B^{\mathsf T}B=\operatorname{diag}(\lambda_1,\lambda_2)\). Write \(T=\lambda_1+\lambda_2\), \(p_i=\lVert b_i\rVert^2/T\), and, whenever \(p_i>0\),

\[
 t_i=\frac{(b_i)_2^2}{\lVert b_i\rVert^2}\in[0,1].
\]

The residual is \(A-Bb_i^{\mathsf T}b_iB^{\mathsf T}/\lVert b_i\rVert^2\). Its trace, after pivot \(i\), is

\[
 R_i=T-\frac{b_i S b_i^{\mathsf T}}{\lVert b_i\rVert^2}
 =\lambda_2+(\lambda_1-\lambda_2)t_i.
\]

Also

\[
 \sum_i p_it_i=\frac{\sum_i(b_i)_2^2}{T}=\frac{\lambda_2}{T}.
\]

Therefore \(R\in[\lambda_2,\lambda_1]\), and its mean is \(\lambda_2+(\lambda_1-\lambda_2)\lambda_2/T=2\lambda_1\lambda_2/T\). The last mean also follows from the established identity \(\mathbb E(A-\widehat A)=A-A^2/\operatorname{tr}A\); only its use here, not that identity, is needed.

**2. Converse construction.** Let the requested law have atoms \(r_j\in[\lambda_2,\lambda_1]\) of positive masses \(w_j\), \(j=1,\ldots,q\), summing to one and with \(\sum_jw_jr_j=m\). Set

\[
 t_j=\frac{r_j-\lambda_2}{\lambda_1-\lambda_2},\qquad
 b_{j,\pm}=\sqrt{\frac{w_jT}{2}}\left(\sqrt{1-t_j},\ \pm\sqrt{t_j}\right).
\]

Form the \(2q\times2\) matrix \(B\) with these rows and set \(A=BB^{\mathsf T}\). Cancellation of opposite off-diagonal terms gives

\[
 B^{\mathsf T}B=
 T\operatorname{diag}\left(\sum_jw_j(1-t_j),\ \sum_jw_jt_j\right)
 =\operatorname{diag}(\lambda_1,\lambda_2).
\]

Every paired row has squared norm \(w_jT/2\), so the two rows together are pivoted with probability exactly \(w_j\). Step 1 gives residual trace exactly \(r_j\) on either row. Thus the prescribed law is realized, including endpoint and single-atom cases.

**3. Convex order and exact risk.** Jensen gives \(\varphi(m)\le\mathbb E\varphi(R)\). The secant-line inequality on \([a,b]\), averaged at mean \(m\), gives the upper bound with endpoint weights \((b-m)/(b-a)=\lambda_1/T\) and \((m-a)/(b-a)=\lambda_2/T\). The converse construction realizes the constant law \(\delta_m\) and the endpoint Bernoulli law; hence both bounds are sharp. Choosing \(\varphi(x)=(x-m)^2\) yields the variance bound and both extremizers.

For \(u\le m\), the constant law realizes \(\Pr(R\ge u)=1\). For \(m<u\le b\), the elementary inequality \(R-a\ge(u-a)\mathbf1_{\{R\ge u\}}\) gives

\[
 \Pr(R\ge u)\le\frac{m-a}{u-a}.
\]

Equality is achieved by the two-point law placing mass \((m-a)/(u-a)\) at \(u\) and its remaining mass at \(a\), realized by Step 2 with four rows. For \(u>b\), the event is impossible. This proves the formula at all boundary values.

## Verification

For \(\lambda_1=20\), \(\lambda_2=2\), three explicit matrices have identical nonzero spectra but different residual laws:

1. \(A=\operatorname{diag}(20,2)\): \(\Pr(R=2)=10/11\) and \(\Pr(R=20)=1/11\), attaining maximum variance.
2. \(A=\begin{psmallmatrix}11&9\\9&11\end{psmallmatrix}\): \(R=40/11\) with certainty, attaining zero variance.
3. \(A=BB^{\mathsf T}\) with \(B=\begin{psmallmatrix}3&0\\3&0\\1&1\\1&-1\end{psmallmatrix}\): \(\Pr(R=2)=9/11\) and \(\Pr(R=11)=2/11\). This saturates the worst-case threshold bound at \(u=11\).

The included `check.py` performs exact-fraction reconstructions of those one-step laws and 1,116 full-rank integer Gram trials, verifies the exact moment and variance identities, and tests 100 three-atom realizability constructions numerically. Run `python3 check.py` with the standard library. These checks are supplementary: neither sampling nor finite enumeration establishes the general theorem.

## Relationship to prior work

Chen, Epperly, Tropp and Webber (arXiv:2207.06503, Algorithm 1 and Eq. (5.3)) specify diagonal-weighted RPCholesky and derive the one-step matrix expectation. That identity already implies the mean above and is **not** claimed as novel. Epperly (arXiv:2608.20633, Theorem 1.2 and Lemma 4.2) gives multistep error tails and expected convex spectral-function bounds. Divan and Gilles (arXiv:2609.06287, Theorem 3.1) study general pivoted low-rank convergence and approximate sampling. Steinerberger (arXiv:2404.11487) analyzes alternative diagonal-power sampling. These statements do not assert the converse that every fixed-mean finite scalar residual law is realizable by a rank-two PSD input with prescribed spectrum, nor the attained one-step spectral tail envelope. The rank-two Gram-frame construction supplies this missing implication. The construction is elementary but the resulting complete fixed-spectrum uncertainty class is directly relevant to the interpretation of expected-error and confidence guarantees.

## Limitations

The theorem classifies only one exact RPCholesky pivot for real rank-two PSD matrices; dimensions vary in the realizability converse. It does not describe the attainable laws at a *fixed* dimension, non-rank-two matrices, subsequent pivots, or finite-precision implementations. Sharp spectrum-only bounds do not assert that typical kernels exhibit the extreme laws. Priority beyond the inspected literature, including general frame-realization results that could give an equivalent formulation, remains a risk; no independent verification has been performed.

## References

- Y. Chen, E. N. Epperly, J. A. Tropp, and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503, first posted 2022-07-13. https://arxiv.org/abs/2207.06503
- E. N. W. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm*, arXiv:2608.20633, first posted 2026-08-21. https://arxiv.org/abs/2608.20633
- R. Divan and M. A. Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation*, arXiv:2609.06287, first posted 2026-09-05. https://arxiv.org/abs/2609.06287
- S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, arXiv:2404.11487, first posted 2024-04-17. https://arxiv.org/abs/2404.11487
