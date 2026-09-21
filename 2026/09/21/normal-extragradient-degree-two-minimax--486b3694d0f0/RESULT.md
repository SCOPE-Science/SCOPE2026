# Exact degree-two minimax and asymmetric extragradient on normal strongly monotone systems

## Setting

Consider the affine variational equation
\[
F(x)=Ax-b=0
\]
in exact arithmetic, where \(A\in\mathbb R^{n\times n}\) is normal,
\[
\frac{A+A^T}{2}\succeq \mu I,\qquad \|A\|_2\le L,
\qquad 0<\mu\le L.
\]
Let \(x_*\) be the unique root and write \(e=x-x_*\). Normality implies that the spectrum lies in the closed half-disk
\[
K_{\mu,L}=\{\lambda\in\mathbb C:\operatorname{Re}\lambda\ge\mu,\ |\lambda|\le L\},
\]
and for every polynomial \(p\),
\[
\|p(A)\|_2=\max_{\lambda\in\sigma(A)}|p(\lambda)|.
\]
The results below therefore concern Euclidean error for normal systems. They do not extend to arbitrary nonnormal matrices merely from spectral inclusion.

## Main theorem: exact real quadratic minimax on the monotone half-disk

Let \(\delta=\mu/L\in(0,1]\), and scale \(z=\lambda/L\). Among all real polynomials
\[
p(z)=1-bz+cz^2,\qquad b,c\in\mathbb R,
\]
the exact minimax value on
\[
K_\delta=\{z\in\mathbb C:\operatorname{Re}z\ge\delta,\ |z|\le1\}
\]
is
\[
\boxed{
\min_{b,c\in\mathbb R}\max_{z\in K_\delta}|1-bz+cz^2|=1-\delta.
}
\]
One minimizer is
\[
\boxed{p_*(z)=1-(1+\delta)z+z^2.}
\]
For \(0<\delta<1\), the same fixed three-dimensional real-normal matrix is a sharp witness for the whole polynomial class:
\[
A_\delta=
\begin{bmatrix}
\delta&0&0\\
0&\delta&-\sqrt{1-\delta^2}\\
0&\sqrt{1-\delta^2}&\delta
\end{bmatrix}.
\]
Its symmetric part is \(\delta I\), its spectral norm is one, and its spectrum is
\(\{\delta,\delta\pm i\sqrt{1-\delta^2}\}\). Thus
\[
\min_{p(0)=1,\ \deg p\le2,\ p\in\mathbb R[z]}\|p(A_\delta)\|_2=1-\delta.
\]
Scaling by \(L\) yields a sharp matrix whose strong-monotonicity and norm bounds are exactly \(\mu\) and \(L\).

### Proof of the upper bound

Set \(q=1-\delta\). The boundary of \(K_\delta\) consists of a unit-circle arc and the vertical chord \(\operatorname{Re}z=\delta\).

On \(|z|=1\), writing \(x=\operatorname{Re}z\in[\delta,1]\),
\[
\frac{p_*(z)}{z}=z+z^{-1}-(1+\delta)=2x-(1+\delta),
\]
so \(|p_*(z)|\le q\).

On the chord \(z=\delta+iy\), put \(s=y^2\in[0,1-\delta^2]=[0,q(2-q)]\). Directly,
\[
\operatorname{Re}p_*(z)=q-s,\qquad
\operatorname{Im}p_*(z)=-qy,
\]
and therefore
\[
|p_*(z)|^2=(q-s)^2+q^2s
=q^2+s\,[s-q(2-q)]\le q^2.
\]
The maximum-modulus principle gives \(|p_*(z)|\le q\) throughout the half-disk. When \(\delta=1\), the set is the singleton \(\{1\}\) and \(p_*(1)=0\).

### Proof of the lower bound

For \(0<\delta<1\), it suffices to retain two spectral points
\[
z_0=\delta,\qquad z_1=\delta+i\sqrt{1-\delta^2}.
\]
For \(p(z)=1-bz+cz^2\), define the convex quadratics
\[
h_j(b,c)=|p(z_j)|^2,\qquad H(b,c)=\max\{h_0(b,c),h_1(b,c)\}.
\]
At \((b_*,c_*)=(1+\delta,1)\), both active values equal \(q^2\), and
\[
\nabla h_0=2q(-\delta,\delta^2),\qquad
\nabla h_1=2q(1,-\delta).
\]
Hence
\[
\nabla h_0+\delta\nabla h_1=0,
\]
so zero lies in the subdifferential of the convex function \(H\) at \((b_*,c_*)\). This point globally minimizes \(H\), with minimum \(q^2\). Consequently every admissible real quadratic has
\[
\max_{z\in K_\delta}|p(z)|\ge\max\{|p(z_0)|,|p(z_1)|\}\ge q.
\]
Together with the upper bound, this proves the theorem.

## Corollary: an optimal unequal-step extragradient cycle

Consider the two-evaluation update
\[
y=x-\alpha F(x),\qquad x_+=x-\beta F(y).
\]
Its error polynomial is
\[
e_+=\bigl(I-\beta A+\alpha\beta A^2\bigr)e.
\]
Choosing
\[
\boxed{\alpha_* = \frac1{L+\mu},\qquad
\beta_* = \frac{L+\mu}{L^2}}
\]
gives exactly \(p_*(A/L)\). Therefore
\[
\boxed{
\|x_+-x_*\|_2\le \left(1-\frac\mu L\right)\|x-x_*\|_2.
}
\]
The constant is exact over the stated normal class and, more strongly, this cycle realizes the best possible real degree-two stationary polynomial map with \(p(0)=1\).

The two steps are intentionally unequal except in the degenerate parameter relation that would be required by a common-step formula; the corrector coefficient is
\(\beta_*=(L+\mu)/L^2\), while the predictor coefficient is
\(\alpha_*=1/(L+\mu)\).

## Exact benchmark for classical common-step extragradient

If classical extragradient is restricted to one common nonnegative step \(\eta\), its scaled polynomial is
\[
p_t(z)=1-tz+t^2z^2,\qquad t=\eta L.
\]
The exact best common step on the same half-disk is
\[
\boxed{t_*=\frac1{1+\delta},\qquad \eta_*=\frac1{L+\mu},}
\]
with exact worst-case factor
\[
\boxed{
\rho_{\rm same}^*
=\frac{1+\delta+\delta^2}{(1+\delta)^2}
=\frac{L^2+L\mu+\mu^2}{(L+\mu)^2}.
}
\]
For the lower bound, the real points \(z=\delta\) and \(z=1\) give
\(f(t\delta)\) and \(f(t)\), where \(f(s)=1-s+s^2\); their maximum is minimized exactly when \(t=1/(1+\delta)\). For the matching upper bound, \(|p_t|^2\) is convex along both boundary parameters, so the maximum reduces to the two real endpoints and the circular corner. At \(t_*\), the real endpoints are equal to \(\rho_{\rm same}^*\), while the squared gap over the corner is
\[
(\rho_{\rm same}^*)^2-|p_{t_*}(\delta+i\sqrt{1-\delta^2})|^2
=\frac{2\delta(1-\delta)(\delta+2)}{(1+\delta)^3}\ge0.
\]
Thus the unequal-step optimum improves the best common-step cycle by
\[
\boxed{
\rho_{\rm same}^*-(1-\delta)
=\frac{\delta^2(\delta+2)}{(1+\delta)^2}>0
\quad(0<\delta\le1).
}
\]
At \(\mu=L\), the unequal-step cycle solves the linear system exactly in one cycle, while the best common-step extragradient factor is \(3/4\).

## Relation to known work

The polynomial-minimax viewpoint is classical and is not claimed as new. Manteuffel's nonsymmetric Chebyshev work and the later semi-iterative literature formulate optimal complex-spectrum iterations through minimax polynomials; Manteuffel's 1982 paper specifically relates optimal parameters for linear second-degree stationary recurrences to the Chebyshev minimax problem. The accessible abstract establishes that general framework but does not provide the half-disk finite-degree formula above.

Azizian, Scieur, Mitliagkas, Lacoste-Julien and Gidel (AISTATS 2020) use exactly the strongly-monotone/Lipschitz spectral set
\(K_{\mu,L}\), represent linear first-order methods by real polynomials, and note that the relevant minimax problem on complex sets can be difficult. For this half-disk they derive an asymptotic lower bound by inscribing a disk and state that the order is already achieved by methods such as extragradient; they do not state an exact degree-two minimax polynomial or an unequal prediction/correction choice in the checked text. Their analysis is an important direct predecessor and also makes clear that the present result is a finite-degree stationary statement, not a long-horizon complexity optimum.

Huang and Zhang (2021) study a broad extra-point framework for strongly monotone variational inequalities, including standard extragradient. Xu and Wang (2023) study sharp stepsize choices for Korpelevich and Popov extragradient algorithms in a different convex-concave/projection setting. No checked source stated the closed form \(p_*(z)=1-(1+\delta)z+z^2\), the factor \(1-\delta\) as the exact degree-two half-disk minimax, or its realization by the unequal pair \((\alpha_*,\beta_*)\).

## Limitations

- The Euclidean contraction statement requires real normal \(A\). Spectral inclusion alone does not control \(\|p(A)\|_2\) for nonnormal matrices.
- The result is for affine linear operators, exact arithmetic, known \(\mu,L\), and one stationary two-evaluation cycle.
- The minimax comparison is among real degree-at-most-two polynomials with \(p(0)=1\); it is not an optimality statement for adaptive, nonstationary, higher-degree, projected, nonlinear, or momentum methods over many evaluations.
- The general complex Chebyshev/semi-iterative literature is broad. In particular, full theorem-level text of Manteuffel (1982) and some older cited work was not available in the checked sources. Historical equivalence of this special closed form therefore remains the main originality uncertainty.

## Reproducibility

`artifacts/verify.py` checks the boundary formula, the fixed real-normal sharp witness, the convex two-point lower certificate against deterministic random coefficients, the common-step benchmark, and dense-boundary maxima. `artifacts/verification.txt` records the verified output and software versions.

## References

1. T. A. Manteuffel, *The Tchebychev iteration for nonsymmetric linear systems*, Numerische Mathematik 28 (1977), 307-327. DOI: https://doi.org/10.1007/BF01389971
2. T. A. Manteuffel, *Optimal Parameters for Linear Second-Degree Stationary Iterative Methods*, SIAM Journal on Numerical Analysis 19(4) (1982), 833-839. DOI: https://doi.org/10.1137/0719058
3. M. Eiermann and W. Niethammer, *On the Construction of Semi-Iterative Methods*, SIAM Journal on Numerical Analysis 20(6) (1983), 1153-1160. DOI: https://doi.org/10.1137/0720085
4. M. Eiermann, W. Niethammer and R. S. Varga, *A study of semiiterative methods for nonsymmetric systems of linear equations*, Numerische Mathematik 47 (1985), 505-533. DOI: https://doi.org/10.1007/BF01389454
5. W. Azizian, D. Scieur, I. Mitliagkas, S. Lacoste-Julien and G. Gidel, *Accelerating Smooth Games by Manipulating Spectral Shapes*, AISTATS 2020. https://proceedings.mlr.press/v108/azizian20a.html
6. W. Azizian, I. Mitliagkas, S. Lacoste-Julien and G. Gidel, *A Tight and Unified Analysis of Gradient-Based Methods for a Whole Spectrum of Differentiable Games*, AISTATS 2020. https://proceedings.mlr.press/v108/azizian20b.html
7. K. Huang and S. Zhang, *A Unifying Framework of Accelerated First-Order Approach to Strongly Monotone Variational Inequalities*, 2021. https://arxiv.org/abs/2103.15270
8. H.-K. Xu and J. Wang, *Stepsize Choice for Korpelevich's and Popov's Extragradient Algorithms for Convex-Concave Minimax Problems*, Carpathian Journal of Mathematics 39(1) (2023). DOI: https://doi.org/10.37193/CJM.2023.01.22
