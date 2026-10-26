# A residual stability bound for hyperbola-supported Fourier uniqueness

## Finding

Let \(A=(a_n)_{n\in\mathbb Z}\) and \(B=(b_n)_{n\in\mathbb Z}\) be increasing bi-infinite real sequences with
\[
0<\delta_A\le a_{n+1}-a_n\le\alpha,\qquad
0<\delta_B\le b_{n+1}-b_n\le\beta,\qquad \alpha\beta<1.
\]
Use the unitary Fourier transform
\[
\widehat f(\xi)=2^{-1/2}\int_{\mathbb R}f(t)e^{-\pi i t\xi}\,dt
\]
on \(L^2(\mathbb R)\), with distributional extensions where needed. Define
\[
\mathcal H_0=\{\psi\in L^2(\mathbb R):\widehat\psi\in C_0(\mathbb R)\},
\qquad \varphi(t)=t^{-2}\psi(1/t).
\]
The reciprocal transform is interpreted in the distributional \(\mathcal H_0\) framework, where \(\widehat\varphi\) has a continuous representative. Put
\[
R_A=\left(\sum_{n\in\mathbb Z}|\widehat\psi(a_n)|^2\right)^{1/2},
\qquad
R_B=\left(\sum_{n\in\mathbb Z}|\widehat\varphi(b_n)|^2\right)^{1/2},
\]
and
\[
C_A=\sqrt{\alpha}+\frac{2\alpha}{\pi\sqrt{\delta_A}},
\qquad
C_B=\sqrt{\beta}+\frac{2\beta}{\pi\sqrt{\delta_B}}.
\]
If \(\psi\in\mathcal H_0\) and \(R_A,R_B<\infty\), then
\[
\boxed{\displaystyle
\|\psi\|_2\le
\frac{C_A R_A+\alpha C_B R_B}{1-\alpha\beta}}
\qquad\text{and}\qquad
\boxed{\displaystyle
\|t\psi\|_2\le
\frac{\beta C_A R_A+C_B R_B}{1-\alpha\beta}}.
\]
Thus square-summable nonzero sample residuals give an explicit stability bound and force the weighted \(L^2\) regularity \(t\psi\in L^2\), rather than requiring that regularity as an assumption.

## Assumptions and scope

The sequences are indexed by all integers, are strictly increasing, and have uniform positive lower gap bounds \(\delta_A,\delta_B\) and finite upper gap bounds \(\alpha,\beta\). The theorem is subcritical: \(\alpha\beta<1\). Both residual sequences must belong to \(\ell^2(\mathbb Z)\). No prior assumption that \(t\psi\in L^2\) is made. The constants are explicit but not asserted to be optimal. No conclusion is claimed at \(\alpha\beta\ge1\).

## Proof

First prove a sampling lemma. Let \(X=(x_n)_{n\in\mathbb Z}\) have gaps \(\delta\le x_{n+1}-x_n\le L\), and let \(f\) be locally absolutely continuous with \(f'\in L^2(\mathbb R)\) and samples \(s_n=f(x_n)\) in \(\ell^2\). Let \(I f\) be the piecewise-linear interpolant through the samples. On each interval of length \(l_n=x_{n+1}-x_n\), convexity of the squared modulus gives
\[
\|If\|_2^2\le L\sum_n|s_n|^2.
\]
Also,
\[
\|(If)'\|_2^2
=\sum_n\frac{|s_{n+1}-s_n|^2}{l_n}
\le\frac{4}{\delta}\sum_n|s_n|^2.
\]
The function \(g=f-If\) vanishes at both endpoints of every interval. The Poincaré–Wirtinger inequality therefore gives
\[
\|g\|_2\le\frac{L}{\pi}\|g'\|_2
\le\frac{L}{\pi}\bigl(\|f'\|_2+\|(If)'\|_2\bigr).
\]
Consequently \(f\in L^2\) and
\[
\|f\|_2\le\frac{L}{\pi}\|f'\|_2+
\left(\sqrt L+\frac{2L}{\pi\sqrt\delta}\right)\|(f(x_n))\|_{\ell^2}.
\tag{1}
\]

For \(\psi\in\mathcal H_0\), the reciprocal transform satisfies
\[
\|t\varphi\|_2=\|\psi\|_2,
\qquad
\|\varphi\|_2=\|t\psi\|_2
\]
whenever the latter norm is finite. The first identity already holds from the change of variables \(t\mapsto1/t\). Hence \(\widehat\varphi'\in L^2\) and
\(\|\widehat\varphi'\|_2=\pi\|\psi\|_2\), while \(\widehat\varphi\) is continuous in the \(\mathcal H_0\) framework. Apply (1) to \(f=\widehat\varphi\) on \(B\). Since \(R_B<\infty\), this proves \(\widehat\varphi\in L^2\), so Plancherel implies \(\varphi\in L^2\), equivalently \(t\psi\in L^2\). It also gives
\[
\|t\psi\|_2=\|\varphi\|_2
\le\beta\|\psi\|_2+C_B R_B.
\tag{2}
\]

Now \(\widehat\psi\in W^{1,2}(\mathbb R)\) and
\(\|\widehat\psi'\|_2=\pi\|t\psi\|_2\). Apply (1) to \(\widehat\psi\) on \(A\):
\[
\|\psi\|_2\le\alpha\|t\psi\|_2+C_A R_A.
\tag{3}
\]
Combining (2) and (3) yields
\[
(1-\alpha\beta)\|\psi\|_2\le C_A R_A+\alpha C_B R_B.
\]
Division by \(1-\alpha\beta>0\) proves the first estimate. Substitution into (2) proves the second. If \(R_A=R_B=0\), the estimate reduces to \(\psi=0\), consistent with the known uniqueness theorem.

## Verification

The interpolation constants follow from the exact interval bounds for the piecewise-linear interpolant and the Poincaré–Wirtinger inequality. The Fourier normalization is unitary, so \(\|\widehat f\|_2=\|f\|_2\) and \(\|\widehat f'\|_2=\pi\|tf\|_2\). The reciprocal-change-of-variables identities were checked directly. No numerical experiment is used as proof. The estimate is only asserted in the subcritical regime and no optimality of the constants is claimed.

## Relationship to prior work

Radchenko and Ramos prove that the hyperbola and a nonuniform lattice cross form an \(\mathcal H_0\)-Heisenberg uniqueness pair when the product of the two maximum gaps is below one. Their proof uses Poincaré–Wirtinger estimates to obtain uniqueness from exact vanishing. The result here retains their geometry and gap regime but allows nonzero square-summable residuals, gives explicit error constants, and derives the weighted \(L^2\) regularity from those residuals.

Hedenmalm and Montes-Rodríguez established the exact-zero threshold for regular lattice crosses. Yu and Townsend study stability for finite periodic sampling on perturbed grids. These are relevant antecedents, but the inspected statements concern exact-zero uniqueness or finite periodic interpolation, not the residual estimate for the reciprocal hyperbola transform.

## Limitations

The constants are not claimed to be sharp, and the factor \((1-\alpha\beta)^{-1}\) is not proved optimal. No stability estimate is established at the critical boundary \(\alpha\beta=1\), in the supercritical regime, for sequences lacking uniform gap bounds, or for other curves. The estimate is a quantitative extension of the known uniqueness method, not a new uniqueness threshold.

## References

1. D. Radchenko and J. P. G. Ramos, *Perturbed lattice crosses and Heisenberg uniqueness pairs*, arXiv:2410.04557v1, first public 2024-10-06. See Theorem 2 and the proof in Section 4.2; primary MSC 42B10.
2. H. Hedenmalm and A. Montes-Rodríguez, *Heisenberg uniqueness pairs and the Klein–Gordon equation*, Annals of Mathematics 173 (2011), 1507–1527, doi:10.4007/annals.2011.173.3.6.
3. A. Yu and A. Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature*, arXiv:2202.04722v1, first public 2022-02-09; BIT Numerical Mathematics 63 (2023), article 23.
