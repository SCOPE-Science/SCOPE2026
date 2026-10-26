# Geometric–polynomial tails in a confined mutation–selection equilibrium

## Finding

Let the trait space be \(\mathbb Z\). Let \(P\) be convolution with the symmetric discrete-Laplace mutation kernel
\[
p_j=\frac{1-\theta}{1+\theta}\theta^{|j|},\qquad 0<\theta<1,
\]
and let \(D=\operatorname{diag}(\mu_i)\), where \(\mu_{-i}=\mu_i>0\), \(\inf_i\mu_i>0\), and \(\mu_n\sim c n^\alpha\) as \(n\to\infty\), for constants \(c>0\) and \(\alpha>1\). Define \(L=D^{-1}P\). Let \(\varrho=r(L)\) be the principal eigenvalue and let \(\phi\) be its strictly positive eigenvector normalized by \(\sum_{i\in\mathbb Z}\phi_i=1\). Then there is a constant \(K>0\) such that
\[
\phi_{\pm n}\sim K\theta^n n^{-\alpha}.
\]
In particular, the exact equilibrium mass omitted by a symmetric cutoff \(I\) obeys
\[
\sum_{|i|>I}\phi_i\sim\frac{2K}{1-\theta}\theta^{I+1}(I+1)^{-\alpha},
\]
and the exponential moment \(\sum_i e^{s|i|}\phi_i\) is finite exactly when \(s\le -\log\theta\).

## Assumptions and scope

The operator and principal eigenvector are those of the infinite-trait mutation–selection model in Pollett (2026). The stated mortality assumptions imply confinement and \(\sum_{n\ge1}\mu_n^{-1}<\infty\). The claim concerns the infinite-model equilibrium distribution. It does not assert that a finite-section eigenvector has the same error rate, nor does it address asymmetric mortality, non-geometric mutation kernels, or growth exponents \(\alpha\le1\).

## Proof

The principal-eigenvector relation is \(P\phi=\varrho D\phi\). Put \(w_i=(P\phi)_i=\varrho\mu_i\phi_i\). Directly checking the discrete-Laplace kernel at displacement zero and at every nonzero displacement, then using linearity of convolution, gives
\[
(1+\theta^2)w_i-\theta(w_{i-1}+w_{i+1})=(1-\theta)^2\phi_i.
\]
Substitution of \(\phi_i=w_i/(\varrho\mu_i)\) yields, for positive indices,
\[
w_{i+1}+w_{i-1}=\left(\theta+\theta^{-1}-\varepsilon_i\right)w_i,
\qquad \varepsilon_i=\frac{(1-\theta)^2}{\theta\varrho\mu_i}.
\]
Since \(\alpha>1\), \(\sum_i|\varepsilon_i|<\infty\). The limiting characteristic roots of this second-order recurrence are the distinct numbers \(\theta\) and \(\theta^{-1}\). For completeness, the decaying solution can be constructed by writing \(w_i=\theta^i z_i\). With \(\Delta_i=z_i-z_{i-1}\), the recurrence becomes
\[
\Delta_i=\theta^2\Delta_{i+1}+\theta\varepsilon_i z_i.
\]
Imposing \(z_i\to1\) and summing the difference equation backwards gives the explicit Volterra equation
\[
z_n=1-\theta\sum_{j=n+1}^{\infty}\sum_{k=j}^{\infty}\theta^{2(k-j)}\varepsilon_k z_k.
\]
For bounded sequences, the operator on the right has tail norm at most \(\frac{\theta}{1-\theta^2}\sum_{k>N}|\varepsilon_k|\), which tends to zero as \(N\to\infty\). Thus on a sufficiently far tail it is a contraction and produces a solution with \(z_i\to1\), hence \(w_i^{(s)}=\theta^i(1+o(1))\). Reduction of order gives an independent solution growing as \(\theta^{-i}(1+o(1))\). Because \(w=P\phi\) belongs to \(\ell_1(\mathbb Z)\), its growing component is zero; positivity and nonzeroness imply \(w_i\sim A\theta^i\) for some \(A>0\).

Now \(\mu_i\sim c i^\alpha\), so \(\phi_i=w_i/(\varrho\mu_i)\sim [A/(\varrho c)]\theta^i i^{-\alpha}\). Reflection commutes with both \(P\) and \(D\); simplicity of the principal eigenvalue and the normalization force \(\phi_{-i}=\phi_i\). Setting \(K=A/(\varrho c)>0\) proves the two-sided tail law.

Finally, \(\sum_{n>I}\theta^n n^{-\alpha}\sim \theta^{I+1}(I+1)^{-\alpha}/(1-\theta)\), by dividing the series by its first-term scale and applying dominated convergence to the geometric majorant. This proves the omitted-mass asymptotic. The moment criterion follows from comparison of its terms with \((e^s\theta)^n n^{-\alpha}\): below the critical exponent the series converges geometrically, at the boundary it converges because \(\alpha>1\), and above the boundary its terms do not tend to zero.

## Verification

The convolution identity is exact and can be checked on each kernel displacement. The only asymptotic input is the summable perturbation \(\varepsilon_i=O(i^{-\alpha})\) in the displayed recurrence; the Volterra construction above supplies the decaying solution and reduction of order excludes the growing branch from an \(\ell_1\) eigenvector. The tail-mass and moment statements then follow from convergent geometric comparison. No finite enumeration or numerical experiment is used.

## Relationship to prior work

Pollett, “Mutation–selection balance on an infinite trait space: confinement, drift and equilibrium” (arXiv:2609.02086v1, 2 September 2026), proves existence and uniqueness of the strictly positive equilibrium in the confining regime and convergence of finite-section spectral radii. Its discussion explicitly leaves detailed eigenvector analysis aside and notes that convergence of normalized finite-section eigenvectors is not proved. The present statement supplies a tail law for the infinite-model principal eigenvector and an asymptotic for the exact mass removed by a symmetric cutoff. General asymptotic theory for Jacobi recurrences is relevant background; the contribution claimed here is the explicit translation of that recurrence asymptotic into the population-model tail and cutoff-mass formula, not a new general theorem about Jacobi operators.

## Limitations

The result requires symmetric mortality with polynomial growth exponent greater than one and the exact discrete-Laplace mutation kernel. The constant \(K\) is characterized by the eigenvector and is not expressed in closed form. The formula controls the mass of the infinite equilibrium outside a cutoff; it does not, by itself, bound the difference between that equilibrium and the normalized eigenvector of a truncated operator. Whether analogous formulas hold for \(\alpha\le1\), asymmetric mortality, or other mutation kernels remains open here.

## References

1. P. Pollett, “Mutation–selection balance on an infinite trait space: confinement, drift and equilibrium,” arXiv:2609.02086v1, first publicly available 2 September 2026. https://arxiv.org/abs/2609.02086
2. D. Damanik and B. Simon, “Jost functions and Jost solutions for Jacobi matrices, II. Decay and analyticity,” *International Mathematics Research Notices* (2006), Article 19396. https://doi.org/10.1155/IMRN/2006/19396
