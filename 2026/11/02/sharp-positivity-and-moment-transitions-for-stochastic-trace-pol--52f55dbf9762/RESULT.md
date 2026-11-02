# Sharp positivity and moment transitions for stochastic-trace polynomial preconditioning

## Finding

Fix integers \(n\ge 2\) and \(r\ge1\), and a condition parameter \(\kappa>1\). For the single-spike positive-definite matrix
\[
B_{n,\kappa}=\operatorname{diag}(\kappa,1,\ldots,1),
\]
let \(u_1,\ldots,u_r\) be independent and uniform on the unit sphere in \(\mathbb R^n\), and define the unbiased spherical trace estimate and the corresponding *random first symmetric-polynomial preconditioner* by
\[
\widehat t_r=\frac nr\sum_{j=1}^{r}u_j^{\mathsf T}B_{n,\kappa}u_j,
\qquad \widehat P_r=\widehat t_r I-B_{n,\kappa}.
\]
The exact-trace choice \(P_1=\operatorname{tr}(B_{n,\kappa})I-B_{n,\kappa}\) is positive definite, and the condition number of its symmetrically preconditioned matrix is exactly
\[
\kappa_2(B_{n,\kappa}^{1/2}P_1B_{n,\kappa}^{1/2})
=\frac{\kappa(n-1)}{\kappa+n-2}\le n-1.
\]

**Theorem.** Put \(U_j=(u_j)_1^2\), \(\overline U_r=r^{-1}\sum_j U_j\), and \(V_j=nU_j\). The following statements hold simultaneously.

1. The \(U_j\) are independent \(\operatorname{Beta}(1/2,(n-1)/2)\) variables, and
\[
\widehat P_r\succ0\quad\Longleftrightarrow\quad
\frac1r\sum_{j=1}^{r}V_j>\frac{\kappa-n}{\kappa-1}.
\]
Consequently, \(\widehat P_r\succ0\) almost surely for every \(\kappa\le n\), whereas for every \(\kappa>n\) and every *finite* \(r\), it is indefinite with strictly positive probability. For \(\kappa<n\) the definiteness is uniform in all possible probes; at \(\kappa=n\) the exceptional singular configurations have probability zero.

2. For one probe, the exact probability of loss of positive definiteness is
\[
\Pr(\widehat P_1\not\succ0)=
\begin{cases}
0,&1<\kappa\le n,\\[2mm]
I_{\frac{\kappa-n}{n(\kappa-1)}}\left(\frac12,\frac{n-1}{2}\right),&\kappa>n,
\end{cases}
\]
where \(I_x(a,b)\) is the regularized incomplete-beta integral. In particular, for \(n=3\) and \(\kappa=9\), the failure probability is exactly \(1/2\), even though the exact-trace preconditioned condition number is \(9/5\).

3. At the critical condition parameter \(\kappa=n\), the random preconditioner is positive definite almost surely, but, writing
\[
K_{n,r}=\kappa_2(B_{n,n}^{1/2}\widehat P_rB_{n,n}^{1/2}),
\]
there is a **sharp moment threshold**: for every real \(q>0\),
\[
\mathbb E K_{n,r}^{q}<\infty
\quad\Longleftrightarrow\quad q<\frac r2.
\]
More precisely, with
\[
C_{n,r}=\frac{r^{r/2}}{n^r\Gamma(1+r/2)}
\left[\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}\right]^r,
\]
we have the exact tail equivalent
\[
\Pr(K_{n,r}>t)\sim C_{n,r}\,t^{-r/2}
\qquad(t\to\infty).
\]
Thus one or two independent probes yield an almost surely positive-definite preconditioner with **infinite expected preconditioned condition number** at \(\kappa=n\); three probes are necessary and sufficient for that expectation to be finite.

4. With \(n,r\) fixed and \(\kappa\to\infty\), the loss probability converges to the strictly positive value
\[
p_{n,r}^{\infty}=\Pr\left(\frac1r\sum_{j=1}^{r}V_j\le1\right).
\]
For each fixed \(r\), the subsequent large-dimension limit is
\[
\lim_{n\to\infty}p_{n,r}^{\infty}
=\Pr(\chi_r^2\le r).
\]
For each fixed \(n\ge2\), the infinite-spike and infinite-probe limits do not commute:
\[
\lim_{\kappa\to\infty}\lim_{r\to\infty}\Pr(\widehat P_r\not\succ0)=0,
\qquad
\lim_{r\to\infty}\lim_{\kappa\to\infty}\Pr(\widehat P_r\not\succ0)=\frac12.
\]
Here the estimator is recomputed independently for every batch, and the conclusions concern the resulting random preconditioner, not a particular iterative optimization trajectory.

## Assumptions and scope

All matrices and vectors are real, the matrix dimension \(n\ge2\) and probe count \(r\ge1\) are finite unless explicitly taken to a limit, and \(\kappa>1\). A spherical probe is distributed according to normalized rotation-invariant surface measure on the unit sphere. Independent probes are essential for the moment exponent \(r/2\). The term *failure* means failure of **strict positive definiteness**, not numerical breakdown for all solvers. The condition number \(K_{n,r}\) is defined only in the almost-sure positive-definite critical regime.

## Proof

**Spectral calculation.** The exact trace is \(\kappa+n-1\). The eigenvalues of \(P_1\) are \(n-1\) on the spike and \(\kappa+n-2\) on its orthogonal complement. The eigenvalues of \(B^{1/2}P_1B^{1/2}\) are therefore \(\kappa(n-1)\) and \(\kappa+n-2\), giving the stated condition number (the former is at least the latter since \((n-2)(\kappa-1)\ge0\)).

**Spherical distribution and safety boundary.** Write a uniform sphere vector as \(u=g/\|g\|_2\) with independent standard Gaussian coordinates. Then \(U=u_1^2=g_1^2/\sum_i g_i^2\), hence \(U\sim\operatorname{Beta}(1/2,(n-1)/2)\). Since
\[
\widehat t_r=n+n(\kappa-1)\overline U_r,
\]
its associated matrix has one eigenvalue \(n-\kappa+n(\kappa-1)\overline U_r\) and \(n-1\) repeated eigenvalues \(n-1+n(\kappa-1)\overline U_r>0\). Thus strict positive definiteness is equivalent to the displayed inequality. Each \(U_j\) belongs to \((0,1)\) almost surely and has positive density throughout that interval. For \(\kappa<n\) the first eigenvalue is uniformly positive; at equality it is positive almost surely. When \(\kappa>n\), the event that all \(U_j\) are sufficiently close to zero has positive probability and produces a negative eigenvalue. Taking the beta cumulative distribution for \(r=1\) proves the probability formula. At \(n=3\), the beta CDF is \(I_x(1/2,1)=\sqrt x\). For \(\kappa=9\), \(x=1/4\), hence the probability is \(1/2\). The exact-trace condition number is \(2\kappa/(\kappa+1)=9/5\).

**Critical condition-number tail.** Set \(\kappa=n\). The preconditioned eigenvalues are \(n^2(n-1)\overline U_r\) and \((n-1)(1+n\overline U_r)\), so with
\[
R(\overline U_r)=\frac{1+n\overline U_r}{n^2\overline U_r}
\]
we have \(K_{n,r}=\max\{R,R^{-1}\}\). As \(\overline U_r\downarrow0\), \(K_{n,r}\sim(n^2\overline U_r)^{-1}\), while it is bounded on any interval where \(\overline U_r\ge\varepsilon>0\). Let
\[
a_n=\frac{\Gamma(n/2)}{\sqrt\pi\,\Gamma((n-1)/2)}.
\]
The beta density obeys \(f_U(x)\sim a_n x^{-1/2}\) as \(x\downarrow0\). Convolution over the positive simplex (or the Dirichlet integral) gives the small-sum expansion
\[
\Pr(\overline U_r\le x)
\sim \frac{r^{r/2}}{\Gamma(1+r/2)}
\left[\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}\right]^r x^{r/2}.
\]
For sufficiently large \(t\), the event \(K_{n,r}>t\) is equivalent to
\(\overline U_r<[n^2(t-1/n)]^{-1}\); substitution yields \(C_{n,r}t^{-r/2}\). The identity
\(\mathbb E K^q=q\int_0^\infty t^{q-1}\Pr(K>t)\,dt\)
then proves the moment cutoff, including logarithmic divergence at equality.

**Limits.** For fixed \(n,r\), the failure threshold \((\kappa-n)/(\kappa-1)\) increases to the mean \(\mathbb E V_j=1\), and the sample-mean distribution has no atom there. Thus its failure probability tends to \(p_{n,r}^{\infty}\). For fixed \(r\), the Gaussian representation yields \(nU_j\Rightarrow\chi_1^2\) as \(n\to\infty\), jointly across the independent probes, giving the \(\chi_r^2\) law. Finally, for each finite \(\kappa>n\), the failure threshold is strictly below the mean, so the strong law makes its probability tend to zero as \(r\to\infty\). At the infinite-spike threshold equal to the mean, the ordinary central limit theorem gives a lower-tail limit of \(1/2\), since \(\operatorname{Var}(V_j)=2(n-1)/(n+2)>0\). This proves the noncommuting limits.

## Verification

Run \(\texttt{python3 verification/check.py}\) from this package. The self-contained script checks the exact preconditioned eigenvalues, the special incomplete-beta formulas for dimensions two and three, the \(n=3,\kappa=9\) half-probability identity, independent finite-sample sphere simulations, numerical consistency with the large-dimension chi-square limit, and exact critical-tail special cases. The analytical proofs above establish the infinite-dimensional and infinite-sample statements; Monte Carlo checks do not certify them.

## Relationship to prior work

Doikov and Rodomanov introduce the exact symmetric-polynomial preconditioner \(P_1=\operatorname{tr}(B)I-B\) and in a footnote to Section 4.1 explicitly mention the unbiased spherical trace estimator \(n u^{\mathsf T}Bu\). Their spectral positivity and condition-number guarantees apply to the exact-trace polynomial; the inspected presentation does not provide a safety classification or moment law for the stochastic substitution. Meyer, Musco, Musco, and Woodruff develop stochastic trace-estimation error guarantees and variance-reduction approaches; their general relative-trace accuracy statements do not directly give this sharp positivity and conditioning transition. The beta law for a spherical squared coordinate is classical; novelty is not claimed for that distribution by itself. The contribution assessed here is the combined exact preconditioner-reliability classification, including the critical heavy-tail cutoff and the noncommuting limits.

## Limitations

The theorem concerns the first symmetric-polynomial preconditioner, independent **spherical** probes, and a one-spike spectral model. It does not describe Hutch++, Rademacher probing, higher polynomial degrees, indefinite input matrices, numerical roundoff, or the performance of a full optimization method under resampled preconditioners. The publication-priority comparison remains qualified: an equivalent specialized stochastic-preconditioner analysis outside the inspected literature could already exist.

## References

1. N. Doikov and A. Rodomanov, *Polynomial Preconditioning for Gradient Methods*, first posted 2023-01-30, arXiv:2301.13194; ICML/PMLR 202 (2023), pp. 8162–8187. https://arxiv.org/abs/2301.13194 ; https://proceedings.mlr.press/v202/doikov23b.html
2. R. A. Meyer, C. Musco, C. Musco, and D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, first posted 2020-10-19, arXiv:2010.09649; SOSA (2021). https://arxiv.org/abs/2010.09649
