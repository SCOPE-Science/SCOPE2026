# A sharp three-query Gaussian trace-estimation crossover on four-dimensional spikes

## Finding
Consider the *Gaussian* three-matrix-vector-product version of Hutch++ and, at the identical product budget, the Gaussian three-probe Girard--Hutchinson trace estimator. For every real symmetric positive-definite matrix whose eigenvalues are \(s\lambda,s,s,s\), with \(s>0\) and \(\lambda\ge1\), both estimators are unbiased for \(\operatorname{tr}A=s(\lambda+3)\). Their exact variances are
\[
\operatorname{Var}(H_{++})=2s^2\frac{\lambda^4+8\lambda^3+7\lambda^2+6\lambda+2}{(\lambda+1)^3},\qquad
\operatorname{Var}(H_3)=\frac{2s^2}{3}(\lambda^2+3).
\]
The variance ratio \(\operatorname{Var}(H_{++})/\operatorname{Var}(H_3)\) is strictly decreasing for \(\lambda>1\), from \(9/4\) at \(\lambda=1\) toward zero. It crosses one **exactly once**, at the unique positive root \(\lambda_*\in(4,5)\) of
\[
\lambda^5-18\lambda^3-11\lambda^2-9\lambda-3=0,
\qquad \lambda_*=4.56842704056585\ldots.
\]
Therefore Gaussian Hutch++ has **larger** mean-square trace error for \(1\le\lambda<\lambda_*\), equal error at \(\lambda_*\), and **smaller** error for \(\lambda>\lambda_*\). The conclusion is unchanged under orthogonal conjugation of \(A\).

## Assumptions and scope
All vectors and matrices are real, and arithmetic is exact. Let \(v\in\mathbb R^4\) satisfy \(\|v\|_2=1\), and write \(A=s[I_4+(\lambda-1)vv^{\mathsf T}]\). Fix \(s>0\), \(\lambda\ge1\). Let \(g,h,h_1,h_2,h_3\) be five mutually independent standard Gaussian vectors in \(\mathbb R^4\). Set \(q=Ag/\|Ag\|_2\), which is well-defined almost surely, and \(P=qq^{\mathsf T}\). Define
\[
H_{++}=q^{\mathsf T}Aq+h^{\mathsf T}(I_4-P)A(I_4-P)h,
\quad
H_3=\tfrac13\sum_{j=1}^3 h_j^{\mathsf T}Ah_j.
\]
For \(H_{++}\), the three products are \(Ag\), \(Aq\), and \(A(I_4-P)h\). For \(H_3\), they are \(Ah_1\), \(Ah_2\), and \(Ah_3\). The result compares precisely these **Gaussian** estimators, not Rademacher probes, independently calibrated alternatives, or the best trace estimator with three queries. Four deterministic canonical-basis queries evaluate the trace of an arbitrary \(4\times4\) matrix exactly; the three-query comparison is the smallest ambient dimension for which that elementary method exceeds the stipulated budget.

## Proof
**1. Unbiasedness and conditional error.** Since \(P^2=P\), the trace identity
\[
\operatorname{tr}A=\operatorname{tr}(PA)+\operatorname{tr}[(I-P)A(I-P)]
\]
holds for each \(q\). Conditional on \(q\), the second term in \(H_{++}\) is a standard Gaussian quadratic form. For a real symmetric matrix \(B\), \(\mathbb E(h^{\mathsf T}Bh)=\operatorname{tr}B\) and \(\operatorname{Var}(h^{\mathsf T}Bh)=2\operatorname{tr}(B^2)\). Thus \(H_{++}\) is unbiased *conditionally* on \(q\), and
\[
\operatorname{Var}(H_{++})=2\mathbb E\operatorname{tr}\bigl([ (I-P)A(I-P) ]^2\bigr).
\]
Independence of three Gaussian quadratic forms gives \(\operatorname{Var}(H_3)=\frac23\operatorname{tr}(A^2)=\frac{2s^2}{3}(\lambda^2+3)\).

**2. Exact residual norm.** Rotational invariance and scaling let us take \(s=1\) and \(v=e_1\). Put \(z=g_1^2\), \(w=g_2^2+g_3^2+g_4^2\), and
\[
u=\frac{w}{\lambda^2z+w}=1-(e_1^{\mathsf T}q)^2.
\]
For \(B=(I-P)A(I-P)\), elementary projector algebra gives
\[
\operatorname{tr}(B^2)=\operatorname{tr}(A^2)-2q^{\mathsf T}A^2q+(q^{\mathsf T}Aq)^2
=3+2(\lambda-1)u+(\lambda-1)^2u^2.
\]
This identity holds pointwise, including \(\lambda=1\).

**3. Exact Gaussian angular integration.** The independent laws \(z\sim\chi^2_1\), \(w\sim\chi^2_3\) imply that the angle \(\theta\in(0,\pi/2)\) with \(z/(z+w)=\sin^2\theta\) has density \((4/\pi)\cos^2\theta\). With \(t=\tan\theta\), this yields, for \(k=1,2\),
\[
\mathbb E[u^k]=\frac4\pi\int_0^\infty\frac{dt}{(1+t^2)^2(1+\lambda^2t^2)^k}.
\]
These integrals can be evaluated without any limiting approximation. Start from
\[
J(b,c)=\int_0^\infty\frac{dt}{(t^2+b^2)(t^2+c^2)}
=\frac\pi{2bc(b+c)},\quad b,c>0.
\]
Differentiating with respect to \(b\) inserts the square of \(t^2+b^2\); differentiating once more with respect to \(c\) inserts the square of \(t^2+c^2\). Taking \(b=1,c=1/\lambda\), and including the powers of \(\lambda\) in the denominator, gives the two exact identities
\[
\mathbb E u=\frac{2\lambda+1}{(\lambda+1)^2},\qquad
\mathbb E u^2=\frac{\lambda^2+3\lambda+1}{(\lambda+1)^3}.
\]
Substitution into step 2 yields
\[
\mathbb E\operatorname{tr}(B^2)
=\frac{\lambda^4+8\lambda^3+7\lambda^2+6\lambda+2}{(\lambda+1)^3}.
\]
Returning the \(s^2\) factor establishes both variance formulas.

**4. The exact spectral threshold.** Their difference is
\[
\operatorname{Var}(H_{++})-\operatorname{Var}(H_3)
=-\frac{2s^2}{3(\lambda+1)^3}
(\lambda^5-18\lambda^3-11\lambda^2-9\lambda-3).
\]
The polynomial in parentheses has exactly one positive root by Descartes' rule of signs; it is negative at \(4\) and positive at \(5\). Hence all equality and strict comparison cases above follow. Additionally, writing
\[
R(\lambda)=\frac{3(\lambda^4+8\lambda^3+7\lambda^2+6\lambda+2)}{(\lambda+1)^3(\lambda^2+3)},
\]
direct differentiation gives
\[
R'(\lambda)
=-\frac{3\lambda(\lambda-1)(\lambda^4+15\lambda^3+25\lambda^2+37\lambda+2)}{(\lambda+1)^4(\lambda^2+3)^2}<0
\quad(\lambda>1).
\]
At \(\lambda=1\), \(R=9/4\); and \(R(\lambda)\sim3/\lambda\) as \(\lambda\to\infty\). This proves strict monotonicity and the remaining boundary statements.

## Verification
The standalone `verify.py` uses symbolic differentiation of \(J(b,c)\), exact polynomial identities, 25 independent exact rational \(4\times4\) projector cases, and numerical quadrature at ten selected moments. It also performs five independent seeded finite-sample experiments as secondary checks. Execute `python verify.py` with dependencies in `requirements.txt`. Finite samples and numerical quadrature are not used in place of the analytic proof; the all-parameter statements follow from the displayed identities and sign arguments.

## Relationship to prior work
Meyer, Musco, Musco, and Woodruff, *Hutch++: Optimal Stochastic Trace Estimation* (arXiv:2010.09649, first posted 2020-10-19), introduced the estimator and proved general randomized trace-error guarantees. Persson, Cortinovis, and Kressner, *Improved variants of the Hutch++ algorithm for trace estimation* (arXiv:2109.10659), discussed the flat- versus decaying-spectrum allocation tradeoff and adaptive alternatives. Jiang, Pham, Woodruff, and Zhang, *Optimal Sketching for Trace Estimation* (arXiv:2111.00664), established high-probability complexity bounds for non-adaptive estimators. Epperly, Tropp, and Webber, *XTrace* (arXiv:2301.07825), studied exchangeable trace estimation and general Hutch++ variance bounds. Saibaba, Alexanderian, and Ipsen (arXiv:1605.04893) analyzed an earlier subspace-projection estimator. The general Gaussian quadratic-form identity and conditional residual-variance decomposition are standard and **not** claimed as new. The assessed contribution here is the exact four-dimensional, three-query variance formula, the strictly monotone spectral ratio, and the unique algebraic crossing. These references do not state that exact finite-budget classification in the inspected portions, but a previously overlooked equivalent computation remains possible.

## Limitations
The theorem is a fixed-budget performance comparison for a four-dimensional one-spike positive-definite spectral family; it is not a guarantee for arbitrary spectra or dimensions. It does not compare against Rademacher Hutchinson (which can have zero variance on diagonal matrices), deterministic schemes tailored to a known rank-one spike, or any globally optimal query strategy. No claim of independent review or complete priority certification is made. The rigorous statements concern real, standard Gaussian probes and exact arithmetic; finite-precision effects are outside scope.

## References
1. R. A. Meyer, C. Musco, C. Musco, D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649 (first posted 2020-10-19), https://arxiv.org/abs/2010.09649; open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC8553228/.
2. D. Persson, A. Cortinovis, D. Kressner, *Improved variants of the Hutch++ algorithm for trace estimation*, arXiv:2109.10659, https://arxiv.org/abs/2109.10659.
3. S. Jiang, H. Pham, D. P. Woodruff, R. Zhang, *Optimal Sketching for Trace Estimation*, arXiv:2111.00664, https://arxiv.org/abs/2111.00664.
4. E. N. Epperly, J. A. Tropp, R. J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, arXiv:2301.07825, https://arxiv.org/abs/2301.07825.
5. A. K. Saibaba, A. Alexanderian, I. C. F. Ipsen, *Randomized Matrix-free Trace and Log-Determinant Estimators*, arXiv:1605.04893, https://arxiv.org/abs/1605.04893.
