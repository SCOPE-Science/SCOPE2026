# Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Consider the semidiscrete one-dimensional heat equation on the infinite uniform lattice,
\[
\dot u=-\frac{\kappa}{h^2}Lu,\qquad (Lu)_j=2u_j-u_{j-1}-u_{j+1},\qquad j\in\mathbb Z.
\]
For a Crank–Nicolson full step of size \(\Delta t\), set
\[
s=\frac{\kappa\Delta t}{2h^2}>0,
\qquad
R_s=(I+sL)^{-1},
\qquad
C_s=(I+sL)^{-1}(I-sL)=2R_s-I.
\]
Here \(R_s\) is exactly one backward-Euler half-step of length \(\Delta t/2\), while \(C_s\) is one Crank–Nicolson full step of length \(\Delta t\).

The composite operator
\[
K_s=C_sR_s=2R_s^2-R_s
\]
is positivity preserving for **every** \(s>0\), even though \(C_s\) alone is not. More precisely, define \(q\in(0,1)\) by
\[
s=\frac{q}{(1-q)^2},
\qquad
q=\frac{1+2s-\sqrt{1+4s}}{2s}.
\]
Then \(R_s\) and \(K_s\) are convolution operators with kernels
\[
r_j=\frac{1-q}{1+q}q^{|j|},
\]
and
\[
k_j=
q^{|j|}\frac{(1-q)^2}{(1+q)^3}
\Bigl(2|j|(1+q)+1-q\Bigr).
\]
Thus \(r_j>0\), \(k_j>0\) for every \(j\in\mathbb Z\), and
\[
\sum_{j\in\mathbb Z}r_j=
\sum_{j\in\mathbb Z}k_j=1.
\]
Consequently both operators preserve nonnegativity and discrete mass.

The same statement holds on every periodic cycle with at least three grid points: the finite-grid kernels are the periodizations of \(r_j\) and \(k_j\), hence are strictly positive for every \(s>0\).

A useful extension follows from commutativity. For all integers \(m\ge k\ge0\),
\[
C_s^kR_s^m=(C_sR_s)^kR_s^{m-k}=K_s^kR_s^{m-k},
\]
so \(C_s^kR_s^m\) is positivity preserving and mass preserving on the infinite or periodic lattice. In particular, two backward-Euler half-steps guarantee nonnegativity through the first two subsequent Crank–Nicolson full steps, uniformly in \(\Delta t/h^2\).

This unconditional statement is boundary-sensitive. For the two-interior-point homogeneous-Dirichlet Laplacian
\[
L_D=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}
\]
and \(s=1\), let \(R=(I+L_D)^{-1}\) and \(C=R(I-L_D)\). Direct calculation gives
\[
CR=\frac1{16}\begin{pmatrix}-1&1\\1&-1\end{pmatrix},
\qquad
CR^2=\frac1{64}\begin{pmatrix}-1&1\\1&-1\end{pmatrix}.
\]
Hence even one or two backward-Euler half-steps do not give an unconditional positivity theorem after a subsequent Crank–Nicolson step for this Dirichlet grid.

## Proof

For the infinite lattice, the resolvent kernel \(r_j\) satisfies
\[
(1+2s)r_j-sr_{j-1}-sr_{j+1}=\delta_{j0}.
\]
Away from the origin the decaying characteristic root is \(q\), where
\(s=q/(1-q)^2\). Symmetry and the equation at the origin give
\[
r_j=a q^{|j|},\qquad a=\frac{1-q}{1+q}.
\]
This also shows \(\sum_j r_j=1\).

For \(n=|j|\), a direct geometric-series calculation yields
\[
(r*r)_j
=q^n\frac{1-q}{(1+q)^3}
\left[n(1-q^2)+1+q^2\right].
\]
Since \(K_s=2R_s^2-R_s\), subtraction gives
\[
\begin{aligned}
k_j
&=2(r*r)_j-r_j\\
&=q^n\frac{(1-q)^2}{(1+q)^3}
\left[2n(1+q)+1-q\right],
\end{aligned}
\]
which is strictly positive. Because \(L\mathbf1=0\), both \(R_s\) and \(C_s\) fix constants; equivalently the displayed kernels have total mass one.

On an \(N\)-cycle, \(N\ge3\), periodizing the absolutely summable infinite-lattice resolvent kernel,
\[
r_j^{(N)}=\sum_{\ell\in\mathbb Z}r_{j+\ell N},
\]
solves the finite circulant resolvent equation. Uniqueness therefore identifies it with \((I+sL_N)^{-1}\). The same argument, or the identity \(K_s=2R_s^2-R_s\), gives
\[
k_j^{(N)}=\sum_{\ell\in\mathbb Z}k_{j+\ell N}>0.
\]
The formula for \(C_s^kR_s^m\) follows because \(C_s\) and \(R_s\) are rational functions of the same operator. Products of nonnegative mass-one convolution kernels remain nonnegative and mass one. The Dirichlet matrices above follow by exact \(2\times2\) inversion and multiplication.

## Why this is not a scalar-stability statement

Crank–Nicolson is A-stable but not positivity preserving for arbitrary large heat-equation steps. The scalar multiplier of the filtered composite is
\[
\frac{1-x}{(1+x)^2},
\]
which is negative for \(x>1\). The theorem therefore does not come from nonnegativity of scalar amplification factors or from absolute monotonicity of the rational function. It is a spatial-kernel fact specific to the nearest-neighbor one-dimensional lattice: negative spectral values coexist with a nonnegative convolution kernel.

## Relation to prior literature

Classical work by Lindberg (1971), Luskin--Rannacher--Wendland (1982), Rannacher (1984), Khaliq--Wade (2001), Wade--Khaliq--Siddique--Yousuf (2005), Wade et al. (2007), and Giles--Carter (2006) develops damping/smoothing strategies for trapezoidal or Crank–Nicolson time stepping, especially for nonsmooth data and option-pricing applications. The 2005 work explicitly develops higher-order smoothing based on positivity-preserving Padé schemes. These works establish the broader smoothing context, but the accessible statements checked did not supply the lattice kernel above or the all-\(s\) positivity conclusion for the backward-Euler-filtered Crank–Nicolson composite.

Higueras and Roldán (2023) derive finite-grid necessary and sufficient positivity bounds for Crank–Nicolson itself under homogeneous Dirichlet boundary conditions. That problem is complementary: the result here concerns a backward-Euler-filtered composite and shows both unconditional positivity on translation-invariant one-dimensional lattices and a small Dirichlet obstruction.

Recent work by Itkin and Kazbek (2026) studies positivity of rational maps for Fokker--Planck generators and emphasizes that Crank–Nicolson's stiff-limit sign obstructs unconditional positivity in their setting. The present result exploits a different, lattice-specific mechanism and gives an exact positive Green kernel for the filtered map.

Targeted searches for the exact composite, Rannacher/backward-Euler startup plus positivity, periodic heat-lattice positivity, and equivalent rational forms did not locate this theorem. This originality statement is only to the best of our knowledge. Several historically relevant papers were available only through abstracts, metadata, or partial text during checking, so an equivalent older result could still exist.

## Verification

`artifacts/verify_lattice_positivity.py` independently checks the closed-form kernel against direct convolution, compares periodic finite-grid matrices with periodized kernels for several grid sizes and step ratios, tests the \(m\ge k\) consequence for small powers, and verifies the exact Dirichlet counterexample. `artifacts/verification.txt` records the resulting numerical residuals.

## Limitations

- The unconditional theorem is for the standard nearest-neighbor, uniform one-dimensional heat lattice on \(\mathbb Z\) or a periodic cycle; it is not a theorem for arbitrary M-matrices, finite elements, variable coefficients, nonuniform grids, or higher-dimensional discretizations.
- The condition \(m\ge k\) is a sufficient positivity mechanism, not claimed to be necessary.
- Homogeneous Dirichlet boundaries can destroy the property, as the explicit two-point counterexample shows.
- No claim is made that a finite backward-Euler startup protects every later Crank–Nicolson step.
- The result concerns exact-arithmetic positivity and mass conservation, not floating-point monotonicity, accuracy constants, efficiency, or optimal choice of timestep.
- The startup changes the temporal discretization over its damping interval; no new global convergence-order theorem is claimed here.
- Full theorem-level text was not inspected end-to-end for several older smoothing papers, especially Lindberg (1971), Rannacher (1984), Khaliq--Wade (2001), Wade et al. (2005), and Wade et al. (2007); this leaves residual originality risk.

## References

1. B. Lindberg, “On smoothing and extrapolation for the trapezoidal rule,” *BIT* 11 (1971), 29–52. https://doi.org/10.1007/BF01935326
2. M. Luskin, R. Rannacher, W. Wendland, “On the smoothing property of the Crank-Nicolson scheme,” *Applicable Analysis* 14 (1982), 117–135. https://doi.org/10.1080/00036818208839415
3. R. Rannacher, “Finite Element Solution of Diffusion Problems with Irregular Data,” *Numerische Mathematik* 43 (1984), 309–328. https://doi.org/10.1007/BF01390130
4. A. Q. M. Khaliq, B. A. Wade, “On Smoothing of the Crank–Nicolson Scheme for Nonhomogeneous Parabolic Problems,” *Journal of Computational Methods in Sciences and Engineering* 1 (2001), 107–123. https://doi.org/10.3233/JCM-2001-1104
5. B. A. Wade, A. Q. M. Khaliq, M. Siddique, M. Yousuf, “Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data,” *Numerical Methods for Partial Differential Equations* 21 (2005), 553–573. https://doi.org/10.1002/num.20039
6. M. B. Giles, R. Carter, “Convergence analysis of Crank–Nicolson and Rannacher time-marching,” *Journal of Computational Finance* 9(4) (2006), 89–112. https://doi.org/10.21314/JCF.2006.152
7. B. A. Wade, A. Q. M. Khaliq, M. Yousuf, J. Vigo-Aguiar, R. Deininger, “On smoothing of the Crank–Nicolson scheme and higher order schemes for pricing barrier options,” *Journal of Computational and Applied Mathematics* 204 (2007), 144–158. https://doi.org/10.1016/j.cam.2006.04.034
8. I. Higueras, T. Roldán, “A new insight on positivity and contractivity of the Crank-Nicolson scheme for the heat equation,” arXiv:2301.01066 (2023). https://arxiv.org/abs/2301.01066
9. A. Itkin, R. Kazbek, “Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker--Planck equation,” arXiv:2608.22703 (2026). https://arxiv.org/abs/2608.22703
