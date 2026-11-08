# A depth-induced calibration collapse in Gaussian tree quadrature recombination

## Finding

Consider the recursive Gaussian integral-recombination rule in which a parent has a Gaussian prior on its two child integrals, while each child's **reported posterior mean** is treated as a noisy observation with **noise variance equal to the child's reported posterior variance**. Even with correctly specified local Gaussian processes, correct prior covariances for every pair of child integrals, and noiseless point evaluations, this rule can become arbitrarily miscalibrated as tree depth increases.

For any integer \(h\geq 0\), set \(n=2^h\), fix \(v>0\), and use the Gaussian integrand and complete balanced binary tree defined below. Let \(S\) denote the true total integral; let \(\widehat S_h\) and \(V_h\) be the recursively reported integral estimate and variance. With \(Y=\sum_{i=1}^{n}y_i\), the **exact identities** are

\[
\widehat S_h=\frac{Y}{1+(h+1)v},\qquad
V_h=\frac{nv}{1+(h+1)v}.
\]

By contrast, the coherent Gaussian posterior obtained by conditioning each independent cell on its one genuine point observation, **exactly once**, is

\[
S\mid y_1,\ldots,y_n\sim
N\!\left(\frac{Y}{1+v},\frac{nv}{1+v}\right).
\]

The unconditional actual mean-square error of the recursive estimate, relative to its reported variance, is

\[
\boxed{\frac{\mathbb E[(S-\widehat S_h)^2]}{V_h}
=\frac{1+(h+1)^2v}{1+(h+1)v}\ \longrightarrow\ \infty.}
\]

For any fixed \(z>0\), the actual (prior-predictive) coverage of the reported symmetric interval \([\widehat S_h-z\sqrt{V_h},\widehat S_h+z\sqrt{V_h}]\) is exactly

\[
\boxed{2\Phi\!\left(z\sqrt{\frac{1+(h+1)v}{1+(h+1)^2v}}\right)-1
\ \sim\ \sqrt{\frac{2}{\pi}}\,\frac{z}{\sqrt{h+1}}\longrightarrow 0,}
\]

where \(\Phi\) is the standard-normal distribution function. The coherent posterior interval, in contrast, has its nominal coverage. Thus hierarchy depth alone can drive coverage to zero in this correctly specified Gaussian example.

## Assumptions and scope

Partition \([0,n]\) into unit cells \(D_i=[i-1,i]\) (assign boundary points arbitrarily). Let all \(X_i,Z_i,W_i\), \(1\leq i\leq n\), be independent standard normal variables. On cell \(D_i\), with local coordinate \(t=x-(i-1)\in[0,1]\), define the random integrand

\[
f(x)=X_i+\sqrt v\,[Z_i\cos(2\pi t)+W_i\sin(2\pi t)].
\]

Within each cell this is a mean-zero stationary Gaussian process with the valid covariance kernel

\[
k_i(t,s)=1+v\cos(2\pi(t-s));
\]

cells are independent. Its exact cell integral is \(I_i=\int_{D_i}f(x)\,dx=X_i\). Take one noiseless observation \(y_i=f(i-\tfrac12)=X_i-\sqrt v Z_i\). The Gaussian conditioning at each leaf is exact, with mean \(m_i=y_i/(1+v)\) and variance \(s_i^2=v/(1+v)\). The true prior covariance of two disjoint subtrees of \(m\) cells each is exactly \(C=mI_2\). At **every** binary merge, use this exact prior covariance, rather than fitting or approximating it.

For two child reported means \((a,b)\), child reported variances \((u,w)\), prior covariance matrix \(C\) of child integrals and \(\mathbf1=(1,1)^\mathsf T\), define the parent outputs by

\[
\widehat I=(C\mathbf1)^\mathsf T(C+\operatorname{diag}(u,w))^{-1}
\begin{pmatrix}a\\b\end{pmatrix},\qquad
V=\mathbf1^\mathsf T C\mathbf1-(C\mathbf1)^\mathsf T(C+\operatorname{diag}(u,w))^{-1}(C\mathbf1).
\]

These are the standard Gaussian pseudo-observation-conditioning formulas used in hierarchical integral recombination (Weiland–Karvonen–Hennig, Section 3.2). We assess this **defined algebraic rule**, not the actual adaptive tree-selection, hyperparameter fitting, or default parent-kernel choice in any software implementation. The global prior is piecewise stationary (not stationary across boundaries), and its complete integrals and covariances are known exactly.

## Proof

**Step 1: exact leaf posterior.** Since \(\operatorname{Cov}(X_i,y_i)=1\) and \(\operatorname{Var}(y_i)=1+v\), conditional Gaussianity gives
\[
I_i\mid y_i\sim N\!\left(\frac{y_i}{1+v},\frac{v}{1+v}\right).
\]
Moreover, independence across \(i\) makes the coherent total posterior the sum of these independent conditional normals, giving the stated coherent mean and variance.

**Step 2: induction through the hierarchy.** At a node of height \(j\) containing \(2^j\) leaves, prove the claimed formulas
\[
\widehat I_j=\frac{\sum_{i\,\mathrm{in\ node}}y_i}{1+(j+1)v},\qquad
V_j=\frac{2^jv}{1+(j+1)v}.
\]
They hold at \(j=0\) by Step 1. For the parent at height \(j\geq1\), each child has \(m=2^{j-1}\) cells and variance \(u=w=mv/[1+jv]\); the correct joint prior of their true integrals is \(C=mI_2\). The Gaussian merge therefore multiplies each child mean by
\[
\frac{m}{m+u}=\frac{1+jv}{1+(j+1)v}.
\]
Applying this common weight to the two child means establishes the claimed parent mean. Its variance is
\[
2m-2\frac{m^2}{m+u}
=\frac{2mv}{1+(j+1)v}=\frac{2^jv}{1+(j+1)v},
\]
closing the induction. Taking \(j=h\) proves the root formulas.

**Step 3: true unconditional mean-square error and coverage.** Write \(D=1+(h+1)v\). Because \(y_i=X_i-\sqrt v Z_i\) and \(S=\sum_i X_i\),
\[
S-\widehat S_h=\frac{D-1}{D}\sum_iX_i+\frac{\sqrt v}{D}\sum_iZ_i.
\]
Both sums are independent centered Gaussians of variance \(n\). Consequently,
\[
\mathbb E[(S-\widehat S_h)^2]=\frac{n[(D-1)^2+v]}{D^2}.
\]
Dividing by \(V_h=nv/D\) gives the exact error-to-reported-variance ratio \([1+(h+1)^2v]/[1+(h+1)v]\). The normalized error is Gaussian with the same variance ratio, yielding the claimed exact coverage expression. For fixed \(v,z>0\), its Gaussian argument is asymptotic to \(z/\sqrt{h+1}\); using \(2\Phi(t)-1\sim\sqrt{2/\pi}\,t\) as \(t\downarrow0\) finishes the proof.

## Verification

The standalone `verification/check.py` performs exact rational arithmetic with \(v\) in six positive rational values, depths \(0\le h\le8\), and six deterministic rational observation vectors per pair. It applies the actual binary merge formula and verifies every displayed finite-depth mean, variance, coherent-posterior, and mean-square identity: **2,268 exact assertions passed**. These checks corroborate rather than replace the analytic induction and Gaussian calculation. The code requires only Python's standard library.

## Relationship to prior work

Weiland, Karvonen, and Hennig (2026, Section 3.2) give the hierarchical Gaussian-conditioning rule and a convergence discussion for quadrature under prescribed regularity. The present result examines its **calibration as tree depth increases** even with oracle local models and exact prior covariance; its formulas are not a statement about that paper's empirical benchmarks or defaults. Deisenroth and Ng (2015) discuss overconfidence in Gaussian-product expert aggregation, a related but different fusion operation on predictions of a common latent. Rullière et al. (2017) analyze nested Kriging using actual covariance and cross-covariance of aggregated predictors, not posterior variances inserted as independent pseudo-observation noise in the present manner. These sources motivate the comparison but do not supply the quantitative tree-depth law proved here.

The mechanism is a **repeated-conditioning mismatch**: a child's posterior estimate is a function of its original observation rather than a fresh independent noisy measurement of its own prior integral. Reintroducing its posterior variance as pseudo-observation noise changes the calibration at each ancestral merge. On this example the simple independent sum of the correct leaf posteriors is itself a correctly calibrated alternative.

## Limitations

The counterexample involves a deliberately chosen finite-rank, periodic stationary kernel within each cell and an independent-cell global prior; the parent covariance is supplied as an exact oracle block matrix. It does **not** prove that typical fitted stationary parent kernels, adaptive partition selection, or real integration problems exhibit this exact law. Heights increase jointly with the number of independent unit cells and the total domain length; this is a family of problems rather than a fixed-domain dense-sampling asymptotic. The coverage statement is unconditional under the specified Gaussian prior, not a frequentist guarantee for every deterministic integrand. No independent mathematical audit or finite-precision analysis is claimed.

## References

1. T. Weiland, T. Karvonen, and P. Hennig, *Hierarchical Bayesian Quadrature*, arXiv:2607.10793, first posted 12 July 2026; *Proceedings of Machine Learning Research* **337** (2026), 7273–7289. https://arxiv.org/abs/2607.10793 and https://proceedings.mlr.press/v337/weiland26a.html
2. M. P. Deisenroth and J. W. Ng, *Distributed Gaussian Processes*, arXiv:1502.02843 (2015). https://arxiv.org/abs/1502.02843
3. D. Rullière, N. Durrande, F. Bachoc, and C. Chevalier, *Nested Kriging predictions for datasets with large number of observations*, arXiv:1607.05432 (2016; revised 2017). https://arxiv.org/abs/1607.05432
