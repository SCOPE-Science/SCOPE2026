# Exact Beta contraction of Gaussian sketch errors under Haar row projection

## Finding

A Haar-orthonormal sketch of a real inconsistent least-squares problem has an **exact finite-sample coefficient-error law** obtained by multiplying the error law of an independent Gaussian sketch by the square root of an independent Beta random variable. This strengthens a known comparison of expected losses to a coupling, strict stochastic domination at every positive threshold, and exact moment and tail formulas.

Let \(n>r\geq1\), \(r\leq\ell\leq n\), and let \(A\in\mathbb R^{n\times r}\) have full column rank. For \(b\in\mathbb R^n\), let \(x_\star=(A^{\mathsf T}A)^{-1}A^{\mathsf T}b\), \(e=b-Ax_\star\), and \(\zeta=\|e\|_2>0\). Fix a thin QR decomposition \(A=QR\) with \(Q^{\mathsf T}Q=I_r\) and invertible \(R\). Independently draw a Haar matrix \(\Omega\in\mathbb R^{n\times\ell}\) with orthonormal columns and a matrix \(S_G\in\mathbb R^{\ell\times n}\) of independent standard real Gaussians. Let
\[
\widehat x_H=(\Omega^{\mathsf T}A)^+\Omega^{\mathsf T}b,\qquad
\widehat x_G=(S_GA)^+S_Gb.
\]
Both sketched designs have full column rank almost surely. Put \(\nu=\ell-r+1\). For \(r\leq\ell<n\), let \(X\sim\chi^2_r\), \(Y\sim\chi^2_\nu\), and \(G\sim N(0,I_r)\) be independent. Independently let
\[
B\sim\operatorname{Beta}\!\left(\frac{n-\ell}{2},\frac{\ell-r}{2}\right)
\]
when \(\ell>r\); define \(B=1\) deterministically when \(\ell=r\). Then, as joint vector-distribution identities (not a claim that the separately sampled estimators are coupled already),
\[
R(\widehat x_H-x_\star)\ \stackrel d=\ \zeta\sqrt B\,\frac{G}{\sqrt Y},\qquad
R(\widehat x_G-x_\star)\ \stackrel d=\ \zeta\frac{G}{\sqrt Y}.
\]
Thus these estimators admit a coupling in which \(\widehat x_H-x_\star=\sqrt B\,(\widehat x_G-x_\star)\) with \(B\) independent of the Gaussian-sketch error. Define normalized **excess full-data squared residual**
\[
T_H=\frac{\|b-A\widehat x_H\|_2^2}{\zeta^2}-1,\qquad
T_G=\frac{\|b-A\widehat x_G\|_2^2}{\zeta^2}-1.
\]
Then \(T_H\stackrel d=B X/Y\), \(T_G\stackrel d=X/Y\), all factors on the right independent. For \(r<\ell<n\), the Haar excess risk is strictly stochastically smaller:
\[
\Pr(T_H>t)<\Pr(T_G>t)\quad\text{for every }t>0.
\]
More generally, this coupling orders every coordinate-error norm and every nondecreasing radial loss; if a moment is infinite, the comparison is interpreted in extended nonnegative reals. At \(\ell=r\) the two normalized vector-error laws coincide; at \(\ell=n\) the Haar solution is exact, so \(T_H=0\).

For \(r\leq\ell<n\), any real \(q>0\) has finite \(q\)-th excess-loss moment **if and only if** \(2q<\nu\). In the finite range,
\[
\mathbb ET_H^q=
\frac{\Gamma((n-\ell)/2+q)\Gamma((n-r)/2)}
{\Gamma((n-\ell)/2)\Gamma((n-r)/2+q)}
\frac{\Gamma(r/2+q)\Gamma(\nu/2-q)}
{\Gamma(r/2)\Gamma(\nu/2)}.
\]
This formula also applies when \(\ell=r\), with the first factor equal to one. Writing \(\alpha=\nu/2\), both distributions have power-law upper tails, with the **exact asymptotic constants**
\[
\lim_{t\to\infty}t^\alpha\Pr(T_G>t)
=\frac{\Gamma((\ell+1)/2)}{\Gamma(r/2)\Gamma(\alpha+1)},\qquad
\lim_{t\to\infty}t^\alpha\Pr(T_H>t)
=\mathbb E[B^\alpha]\frac{\Gamma((\ell+1)/2)}{\Gamma(r/2)\Gamma(\alpha+1)}.
\]
For \(r<\ell<n\) the second tail constant is strictly smaller. In particular, finite expected excess loss requires \(\ell>r+1\), and finite variance of excess loss requires \(\ell>r+3\), for either nontrivial sketch.

## Assumptions and scope

All matrices are real. The data \((A,b)\) are deterministic and the only randomness is in the independent Gaussian or uniformly random Haar sketches. The residual is nonzero; if it vanishes, both methods recover the exact solution almost surely. Sampling uses a single right-hand side, full-column-rank \(A\), and \(r\leq\ell\leq n\). The result is distributional in exact arithmetic; no general statement is made about finite-precision implementation or structured fast transforms.

## Proof

**1. Residual and coefficient reduction.** Since \(e\perp\operatorname{range}(A)\), every candidate \(x\) satisfies
\[
\|b-Ax\|_2^2=\zeta^2+\|R(x-x_\star)\|_2^2.
\]
Rotational invariance lets us identify the columns of \(Q\) with the first \(r\) coordinate vectors and \(e/\zeta\) with the first vector of the remaining \(m=n-r\) coordinates. This identification preserves the vector of coefficients \(R(x-x_\star)\).

**2. Haar sketch through its complementary Gaussian plane.** Suppose \(\ell<n\), and put \(p=n-\ell\), so \(1\leq p\leq m\). A standard \(p\times n\) Gaussian matrix \(H\) has a Haar-distributed row space. The orthogonal projector onto its kernel is
\[
P=I-H^{\mathsf T}(HH^{\mathsf T})^{-1}H,
\]
which has the same law as \(\Omega\Omega^{\mathsf T}\). Decompose \(H=[H_1\ H_2]\) into its \(p\times r\) and \(p\times m\) blocks; these are independent standard Gaussian matrices. The sketched coefficient error \(v=R(\widehat x_H-x_\star)\) minimizes \(\|P(Qv-e)\|_2^2\). Using the exact distance-to-a-subspace identity,
\[
\|P(Qv-e)\|_2^2=\min_z\|Qv-e-H^{\mathsf T}z\|_2^2.
\]
First minimizing in \(v\) yields \(v=H_1^{\mathsf T}z\); then minimizing in \(z\) yields \(z=-\zeta(H_2H_2^{\mathsf T})^{-1}H_2u\), where \(u\) is the unit vector along the residual within the \(m\)-dimensional complement. The inverse exists almost surely because \(p\leq m\). Conditional on \(H_2\), \(v\) is centered isotropic Gaussian with covariance \(\|z\|_2^2I_r\), so it remains to identify \(\|z\|_2^2/\zeta^2\).

**3. Independent Beta/chi-square factorization.** Let \(M=H_2^{\mathsf T}\in\mathbb R^{m\times p}\), and set \(W=M^{\mathsf T}M\). Write the Gaussian polar decomposition \(M=VW^{1/2}\). The matrix \(V\) is uniformly distributed on the Stiefel manifold of \(p\)-frames in \(\mathbb R^m\), independent of \(W\), and \(W\) has real Wishart law with \(m\) degrees of freedom. The squared projection \(B=\|V^{\mathsf T}u\|_2^2\) is \(\operatorname{Beta}(p/2,(m-p)/2)\); at \(p=m\) it is one almost surely. For \(p<m\), decompose \(V^{\mathsf T}u=\sqrt B\,s\), where \(s\) is uniform on the unit sphere of \(\mathbb R^p\), independent of \(B,W\). Hence
\[
\frac{\|z\|_2^2}{\zeta^2}=B\,s^{\mathsf T}W^{-1}s.
\]
The Wishart law is orthogonally invariant, so for each fixed unit \(s\), the variable \(s^{\mathsf T}W^{-1}s\) has the law of \(e_1^{\mathsf T}W^{-1}e_1\). If \(M=[g_1\ M_2]\), the Schur-complement identity gives
\[
(e_1^{\mathsf T}W^{-1}e_1)^{-1}
=g_1^{\mathsf T}(I-\Pi_{M_2})g_1\sim\chi^2_{m-p+1},
\]
because \(g_1\) is an independent standard Gaussian and \(I-\Pi_{M_2}\) has rank \(m-p+1=\nu\). This conditional law does not depend on \(s\) or \(B\), so \(\|z\|_2^2/\zeta^2\stackrel d=B/Y\) with independent \(B,Y\). Independence of \(H_1\) from \(H_2\) produces an additional independent \(G\sim N(0,I_r)\), proving the Haar vector law, including \(\ell=r\).

**4. Gaussian sketch law.** In the same coordinates, write the Gaussian sketch as \([D\ h\ \cdots]\), with \(D\in\mathbb R^{\ell\times r}\), \(h\in\mathbb R^\ell\) independent standard Gaussian arrays. The coefficient error is \(v_G=\zeta(D^{\mathsf T}D)^{-1}D^{\mathsf T}h\). Conditional on \(D\), the normalized variable \(v_G/\zeta\) is Gaussian with covariance \((D^{\mathsf T}D)^{-1}\). The Wishart matrix \(D^{\mathsf T}D\) has density proportional to \(\det(W)^{(\ell-r-1)/2}e^{-\operatorname{tr}(W)/2}\). Multiplying by the conditional Gaussian density and integrating over positive definite \(W\) gives, via the standard Wishart normalization and the matrix determinant lemma, the exact unconditional density
\[
f(t)=\frac{\Gamma((\ell+1)/2)}{\pi^{r/2}\Gamma((\ell-r+1)/2)}
(1+\|t\|_2^2)^{-(\ell+1)/2}.
\]
This is exactly the density of \(G/\sqrt Y\), where \(Y\sim\chi^2_{\ell-r+1}\) is independent of \(G\). Thus the Gaussian and Haar coefficient laws can be realized using the same \(G,Y\) and an additional independent \(B\). As \(R\) is invertible, the same scalar coupling holds for the original coefficient errors.

**5. Loss, strict order, moments, and tails.** Step 1 gives \(T_H=\|v\|_2^2/\zeta^2\), and the independent Gaussian radius has \(\|G\|_2^2=X\sim\chi^2_r\). For \(r<\ell<n\), \(B\in(0,1)\) almost surely and \(X/Y\) has a strictly positive density on every positive interval; therefore \(\Pr(BX/Y>t)<\Pr(X/Y>t)\) for every \(t>0\). The moment formula follows by multiplying the standard Beta, chi-square, and inverse-chi-square moments; the latter diverges at \(q\geq\nu/2\), proving necessity as well as sufficiency. Finally the near-zero chi-square law gives
\[
\Pr(Y<y)\sim\frac{y^{\nu/2}}{2^{\nu/2}\Gamma(\nu/2+1)}\quad(y\downarrow0).
\]
Conditioning on \(X\) and dominated convergence yields the Gaussian tail coefficient, then conditioning on independent \(B\) multiplies it by \(\mathbb EB^{\nu/2}\). When \(\ell=n\), the Haar projector is the identity and its error vanishes. This completes all cases.

## Verification

Run `python verify_beta_sketch.py` with NumPy and SciPy. It checks projected normal equations against the complementary-plane construction on nonorthogonal matrices; tests independently generated Haar sketch errors against the stated Beta times chi-square ratio; verifies moment thresholds and the established expected-error formula; and checks the strict finite-dimensional Beta mean contraction. The program prints a deterministic count of successful assertions. These finite calculations test implementation and boundary conventions only; they do not prove the probability laws or asymptotic tail statements.

For \(\ell>r+1\), the mean formula above reduces exactly to
\[
\mathbb ET_H=\frac{n-\ell}{n-r}\frac{r}{\ell-r-1},\qquad
\mathbb ET_G=\frac{r}{\ell-r-1},
\]
matching the real-case expected-error comparison in the motivating source.

## Relationship to prior work

Epperly and Webber (2026), Theorem 2.1 and Section 5, identify the exact **expected** sketch-and-solve residual error and minimax properties of Haar embeddings using inverse Wishart and matrix-Beta identities. Those results and the Gaussian mean comparison are prior work, not new claims here. The new statement is a full finite-sample **vector law** with one **independent scalar Beta contraction**, implying complete tail order and sharp higher-moment and tail-constant statements for deterministic nonzero residuals. Dobriban and Liu (2019) establish asymptotic sketching efficiency comparisons, not this fixed-instance exact law. Ahfock, Astle, and Richardson (2021) derive Gaussian complete-sketch Student laws; these are a component of the current comparison. The Beta and Wishart identities used in the proof are classical. Equivalent presentations in matrix-variate distribution or multivariate-regression literature have not been ruled out exhaustively.

## Limitations

The result covers one real response and unweighted exact sketch-and-solve, not multiple correlated right-hand sides, general elliptically distributed sketches, arbitrary structured fast transforms, or nonlinear models. Mean and variance thresholds refer to the normalized **excess** squared full-data residual, not to the unnormalized coefficient covariance. The coupling is an equality in joint distribution that can be constructed, not pathwise domination for independently sampled Gaussian and Haar experiments. High-order moments remain infinite even though Haar sketches have strictly smaller finite-threshold tails. Novelty is assessed against accessible literature and requires independent bibliographic review.

## References

- E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096v1 (first posted 2026-05-18), Theorem 2.1 and Sections 5.1–5.4. https://arxiv.org/html/2605.19096v1
- E. Dobriban and S. Liu, *Asymptotics for Sketching in Least Squares Regression*, arXiv:1810.06089, Sections 2 and A. https://arxiv.org/html/1810.06089v2
- D. C. Ahfock, W. J. Astle and S. Richardson, *Statistical properties of sketching algorithms*, Biometrika (2021), especially the exact Gaussian complete-sketch coefficient distribution. https://api.repository.cam.ac.uk/server/api/core/bitstreams/4c9976e5-dc31-430b-98a7-cb7002705ee4/content
