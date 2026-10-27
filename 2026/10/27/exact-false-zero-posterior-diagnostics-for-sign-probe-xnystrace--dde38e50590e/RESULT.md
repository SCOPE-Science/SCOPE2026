# Exact false-zero posterior diagnostics for sign-probe XNysTrace on rank-two matrices

## Finding

The conceptual leave-one-out XNysTrace estimator with independent Rademacher probes has an exact finite-sample joint law on a natural rank-two positive-semidefinite matrix family. Its estimator of *squared error* can vanish while its trace estimate is wrong. For every integer \(m\ge 3\), the expected squared trace error is exactly \(m+1\) times the expectation of this reported squared-error diagnostic. For \(m=2\), the diagnostic is always zero and the trace estimate is always wrong.

More precisely, let \(n\ge2\), \(a,b>0\), and
\[
 A=\operatorname{diag}(a,b,0,\ldots,0)\in\mathbb R^{n\times n},\qquad T=\operatorname{tr}A=a+b,\qquad c=\frac{2ab}{a+b}>0.
\]
Draw \(m\ge2\) independent vectors \(\omega_i\in\{-1,1\}^n\) with independent fair entries. Define the Nyström approximation and the basic leave-one-out estimates by
\[
 A\langle X\rangle=AX(X^{\mathsf T}AX)^\dagger X^{\mathsf T}A,
 \qquad t_i=\operatorname{tr}A\langle\Omega_{-i}\rangle
 +\omega_i^{\mathsf T}\bigl(A-A\langle\Omega_{-i}\rangle\bigr)\omega_i,
\]
where \(\Omega_{-i}\) contains every probe except the \(i\)-th and \(\dagger\) denotes the Moore--Penrose pseudoinverse. Set
\[
 \widehat T=\frac1m\sum_{i=1}^m t_i,\qquad
 \widehat Q=\frac{1}{m(m-1)}\sum_{i=1}^m(t_i-\widehat T)^2.
\]
Thus \(\widehat Q\) is the squared version of the posterior error diagnostic, **not** another trace estimate.

For \(m=2\), the joint pair \((\widehat T-T,\widehat Q)\) equals \((-c,0)\) or \((c,0)\), each with probability \(1/2\).

For every integer \(m\ge3\), its *complete* joint distribution is
\[
\begin{array}{c|c}
(\widehat T-T,\widehat Q)&\text{probability}\\\hline
(-c,0)&2^{1-m}\\
(c/m,c^2/m^2)&m\,2^{1-m}\\
(0,0)&1-(m+1)2^{1-m}.
\end{array}
\]
In particular,
\[
 \mathbb E(\widehat T-T)=0,\qquad
 \mathbb E(\widehat T-T)^2=\frac{c^2(m+1)}{m\,2^{m-1}},\qquad
 \mathbb E\widehat Q=\frac{c^2}{m\,2^{m-1}}.
\]
The leave-one-out basic estimates have pairwise correlation \(1/2\) for every \(m\ge3\), while the correlation equals \(1\) when \(m=2\). The probability that \(\widehat Q=0\) *and* \(\widehat T\ne T\) is exactly \(2^{1-m}\) for \(m\ge3\), and it is \(1\) when \(m=2\).

For the full-rank two-dimensional example \(A=I_2\) with \(m=2\), the true trace is \(2\), while the estimate is \(1\) or \(3\), each with probability \(1/2\), and the reported posterior error is exactly zero in both cases.

## Assumptions and scope

All statements concern exact real arithmetic, the mathematical pseudoinverse definition of XNysTrace above, and independent, unnormalized fair-sign probes. The ambient dimension is any integer \(n\ge2\); the matrix has exactly two positive diagonal entries and is positive definite when \(n=2\). The sample count is any integer \(m\ge2\), including \(m>\operatorname{rank}A\); pseudoinverses make the mathematical estimator well-defined for dependent samples. There is no assumption that the sample Gram matrix is invertible. The result does not apply unchanged to Gaussian probes, to rotationally invariant residual resphering, or to a particular finite-precision implementation that replaces pseudoinverses by inverse-based factorizations.

## Proof

**Reduction to two fair projective signs.** Set \(s_i=\omega_{i1}\omega_{i2}\in\{-1,1\}\). The variables \(s_i\) are independent and fair. On the support of \(A\), the vector \(\omega_i\) is, up to a harmless overall sign, \(v_{s_i}=(1,s_i)^{\mathsf T}\). All remaining coordinates are annihilated by \(A\), so neither Nyström approximations nor the held-out quadratic residuals depend on them.

**Residual for a monochromatic sketch.** If every column in \(\Omega_{-i}\) has the same projective sign \(s\), the image of that sketch on the support of \(A\) has rank one. Inserting a representative \(v_s\) into the pseudoinverse definition gives
\[
 A-A\langle\Omega_{-i}\rangle
 =\frac{ab}{a+b}\begin{pmatrix}1&-s\\-s&1\end{pmatrix}
\]
on the active coordinates, with zeros elsewhere. This remains valid if the sketch repeats the direction any number of times: \(A\langle X\rangle=A^{1/2}P_{\operatorname{ran}(A^{1/2}X)}A^{1/2}\), so only the span matters. The residual trace equals \(c\), and a held-out probe with projective sign \(t\) has residual quadratic form \(c(1-st)\). Its basic estimate therefore equals \(T-cst\): it is \(T-c\) when \(t=s\) and \(T+c\) when \(t=-s\).

If \(\Omega_{-i}\) contains both projective signs, the two active directions span the range of \(A\), hence \(A\langle\Omega_{-i}\rangle=A\) exactly. In that case \(t_i=T\).

**Classification of all sign configurations.** When \(m\ge3\), precisely three disjoint cases arise. If all projective signs coincide, every basic estimate is \(T-c\), giving \((\widehat T-T,\widehat Q)=(-c,0)\). If exactly one sign differs from all others, the exceptional held-out probe has basic estimate \(T+c\) and all remaining basic estimates equal \(T\), giving \((c/m,c^2/m^2)\). Otherwise each sign appears at least twice, every leave-one-out sketch spans both active directions, and all basic estimates are \(T\). There are, respectively, \(2\), \(2m\), and \(2^m-2m-2\) such configurations among the \(2^m\) equiprobable projective sign vectors. This proves the complete law and all moment identities. When \(m=2\), the leave-one-out sketch always has one projective direction. Both basic estimates coincide, equaling \(T-c\) when the projective signs agree and \(T+c\) when they differ, proving the stated exceptional law.

**Correlation.** For \(m\ge3\), the basic estimate \(t_i\) is different from \(T\) precisely when the remaining \(m-1\) signs coincide; this has probability \(2^{2-m}\). Conditional on that event, the held-out sign gives equally likely errors \(\pm c\). Thus \(\operatorname{Var}(t_i)=c^2 2^{2-m}\). Combining this with the just-computed variance of their average and exchangeability gives \(\operatorname{Corr}(t_i,t_j)=1/2\) for all distinct \(i,j\). At \(m=2\), the basic estimates agree almost surely, so the correlation is \(1\).

## Verification

The standalone, standard-library-only script `check_xnys.py` constructs each Nyström approximation from its exact active-span matrix, evaluates every basic estimate and posterior diagnostic as rational numbers, and enumerates every projective sign configuration for \(2\le m\le9\), for four distinct positive rational eigenvalue pairs. Its expected output is `VERIFY_OK 4080 exhaustive projective-sign configurations`. The enumeration tests the stated joint probabilities, unbiasedness, mean-square and posterior moments, and false-zero probabilities. The infinite family of sample counts follows from the combinatorial proof above, not from finite enumeration.

## Relationship to prior work

Epperly, Tropp, and Webber introduced the conceptual XNysTrace estimator and its leave-one-out posterior error diagnostic in arXiv:2301.07825, equations (7)--(9) and Section 3.1. Their Proposition 2 provides a general expected-error-diagnostic identity in terms of the pairwise correlation of the basic estimates, and reports that the correlation is small in the examples examined. The present result uses the same estimator rather than proposing a new one. It determines an exact joint distribution, an exact correlation of \(1/2\) independent of sample count, and the precise false-zero diagnostic probability in a rank-two sign-probe family; none of these values follows from the general correlation identity without analyzing the Nyström pseudoinverse and the discrete sign geometry.

Epperly's 2025 dissertation, Chapters 14--15 and Proposition 15.4, revisits XNysTrace and the general posterior correlation formula, with examples of underestimation. The inspected relevant sections did not contain the finite-sample rank-two Rademacher law given here. General leave-one-out and jackknife diagnostics for other randomized matrix computations are related in motivation but are not the same scalar trace diagnostic.

## Limitations

The phenomenon is an exact statement about the pseudoinverse-based *conceptual* estimator with discrete sign probes. Fast factorization implementations may assume an invertible sample Gram matrix or add regularization; repeated sign sketches can violate those implementation assumptions. The result does not diagnose a defect in the published general correlation identity or claim that all choices of probes, matrices, or posterior diagnostics behave this way. The absolute mean-square error here decays exponentially with \(m\), even though its ratio to the expected reported squared diagnostic grows linearly. An undiscovered equivalent calculation in prior work remains possible.

## References

1. E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the most of every sample in stochastic trace estimation*, arXiv:2301.07825, first submitted 19 January 2023; SIAM Journal on Matrix Analysis and Applications 45 (2024), 1--23. https://arxiv.org/abs/2301.07825 ; full-text equations (7)--(9), Proposition 2, Sections 3.1 and 5.6.
2. E. N. Epperly, *Make the Most of What You Have: Resource-Efficient Randomized Algorithms for Matrix Computations*, Caltech dissertation (2025), Chapters 14--15, especially Proposition 15.4. https://tropp.caltech.edu/dissertations/Epp25-Making-Most.pdf .
3. E. N. Epperly and J. A. Tropp, *Efficient error and variance estimation for randomized matrix computations*, arXiv:2207.06342, first submitted 13 July 2022. https://arxiv.org/abs/2207.06342 .
