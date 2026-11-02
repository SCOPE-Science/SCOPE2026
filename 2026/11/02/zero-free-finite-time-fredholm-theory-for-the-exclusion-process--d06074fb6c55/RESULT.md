# Zero-free finite-time Fredholm theory for the exclusion-process auxiliary walk

## Finding

The Bessel transition kernel in the finite-time one-body reduction of the symmetric exclusion process has a stronger operator structure than is required by its stochastic interpretation. Its killed finite-time operator is positive, self-adjoint after an explicit change of measure, trace class, injective, and **strictly totally positive of every order**. This places every zero of the associated Fredholm determinant on the strictly negative real axis, strictly outside the entire physically admissible current-bias range, and supplies an explicit finite-time inverse bound.

Precisely, for every real \(s>0\), set
\[
p(x,y)=e^{-x-y}\sqrt{\frac yx}\,I_1(2\sqrt{xy}),\qquad 0<x,y<s,
\]
with continuous boundary value \(p(0,y)=ye^{-y}\), and set \((K_sf)(x)=\int_0^s p(x,y)f(y)\,dy\) on \(H_s=L^2((0,s),x\,dx)\). Put
\[
q_s=1-(1+s)e^{-s},\qquad T_s=\int_0^s e^{-2x}I_1(2x)\,dx.
\]
Then \(0<q_s<1\), and all of the following hold:

1. The spectrum of \(K_s\) consists of infinitely many strictly positive eigenvalues \(\lambda_j(s)\) converging to zero (and zero as their only accumulation point); \(\|K_s\|\le q_s\), and \(\sum_j\lambda_j(s)=T_s\sim\sqrt{s/\pi}\) as \(s\to\infty\).
2. For every positive integer \(m\) and strictly increasing positive \(x_1,\dots,x_m\) and \(y_1,\dots,y_m\) in \((0,s)\), \(\det[p(x_i,y_j)]_{i,j=1}^m>0\).
3. The entire function \(D_s(z)=\det(I+zK_s)=\prod_j(1+z\lambda_j(s))\) has only negative real zeros, each no greater than \(-1/q_s\). Thus \(D_s(\omega)>0\) and \(I+\omega K_s\) is invertible for every real \(\omega>-1/q_s\), in particular throughout the physical domain \(\omega\ge-1\).
4. In operator norm on \(H_s\),
\[
\bigl\|(I+\omega K_s)^{-1}\bigr\|\le
\begin{cases}
(1+\omega q_s)^{-1},&-1\le\omega\le0,\\
1,&\omega\ge0.
\end{cases}
\]
For \(|\omega|q_s<1\), the Neumann series has remainder bounded by \((|\omega|q_s)^{N+1}/(1-|\omega|q_s)\) after powers \(0,\ldots,N\). In particular, this convergent series applies for **every** physical negative bias \(-1\le\omega<0\) at **every** finite \(s\).

For the forcing \(g_s(x)=p(x,s)\in H_s\), the microscopic scalar integral equation \((I+\omega K_s)\psi=\omega g_s\) consequently has a unique solution in \(H_s\) at all physical biases, with the stated quantitative conditioning.

## Assumptions and scope

The parameter \(s\) is finite and strictly positive. The kernel is the same auxiliary-walk transition density appearing in the one-body finite-time SEP reduction, not a new model of its many-body dynamics. The physical tilt in that reduction has the product form \(\omega=(1+\rho_-(e^\theta-1))(1+\rho_+(e^{-\theta}-1))-1\), where \(0\le\rho_\pm\le1\) and \(\theta\in\mathbb R\), and therefore \(\omega\ge-1\). The theorem is about the finite-time auxiliary integral operator and the resulting linear equation; no limit of microscopic SEP currents is asserted. A zero eigenvalue need not be an eigenvalue: here it belongs only to the compact spectrum as an accumulation point.

Strict total positivity refers to minors at two independently ordered tuples of strictly positive arguments. Inverse bounds refer to the specified weighted Hilbert space, not automatically to \(L^\infty\) or the microscopic stochastic process itself.

## Proof

**Reversible conjugation and positive factorization.** The kernel obeys \(xp(x,y)=yp(y,x)\). The unitary map \(U:H_s\to L^2(0,s)\), \((Uf)(x)=\sqrt{x}f(x)\), conjugates \(K_s\) to the symmetric operator with kernel
\[
S_s(x,y)=e^{-x-y}I_1(2\sqrt{xy})
=\sum_{k=0}^\infty\frac{h_k(x)h_k(y)}{k!(k+1)!},
\quad h_k(x)=e^{-x}x^{k+1/2}.
\]
The Bessel series converges uniformly on compact squares. Each term is rank-one nonnegative; the sum of their traces is \(\int_0^sS_s(x,x)dx=T_s<\infty\), so \(S_s\), hence \(K_s\), is nonnegative and trace class. If its quadratic form vanishes on \(f\in L^2(0,s)\), then \(\int_0^s f(x)e^{-x}x^{k+1/2}dx=0\) for all \(k\ge0\). Polynomial density in continuous functions on \([0,s]\), applied to the finite signed/complex measure \(f(x)e^{-x}\sqrt{x}\,dx\), gives \(f=0\) a.e. Thus the kernel is injective; compactness and infinite-dimensionality give an infinite sequence of strictly positive eigenvalues with limit zero.

**Strict total positivity.** For ordered positive \(x_i\) and \(y_j\), expand the determinant of the finite partial-sum kernel by Cauchy–Binet. Every term indexed by distinct ordered nonnegative exponents \(k_1<\cdots<k_m\) is
\[
\prod_{\ell=1}^m\frac1{k_\ell!(k_\ell+1)!}\,
\det[h_{k_\ell}(x_i)]_{i,\ell=1}^m
\det[h_{k_\ell}(y_j)]_{j,\ell=1}^m.
\]
Both generalized Vandermonde determinants are strictly positive because the nodes and exponents are strictly increasing on the positive half-line; hence every summand is nonnegative and the term \(k_\ell=\ell-1\) is strictly positive. Uniform convergence yields the strictly positive determinant for \(S_s\). Multiplying each row and column by strictly positive factors establishes the same fact for \(p\).

**Explicit strict finite-time contraction bound.** A second representation of the same kernel is
\[
p(x,y)=\sum_{k=0}^\infty
\frac{e^{-x}x^k}{k!}
\frac{e^{-y}y^{k+1}}{(k+1)!}.
\]
Consequently, for fixed \(x\ge0\), \(p(x,\cdot)\) is the mixture of \(\Gamma(k+2,1)\) densities with \(k\sim\operatorname{Poisson}(x)\). Since these gamma variables increase stochastically with \(k\),
\[
\int_0^s p(x,y)\,dy\le
\mathbb P(\Gamma(2,1)\le s)=q_s.
\]
For arbitrary \(f\in H_s\), Cauchy–Schwarz gives \(|K_sf(x)|^2\le q_s\int_0^s p(x,y)|f(y)|^2dy\). Integrating against \(x\,dx\), interchanging integrals, applying detailed balance and the same row-sum bound gives \(\|K_sf\|_{H_s}^2\le q_s^2\|f\|_{H_s}^2\).

**Fredholm zeros, inverse and approximation.** As a positive trace-class operator, \(K_s\) has the canonical genus-zero determinant product above. The eigenvalue bounds \(0<\lambda_j\le q_s\) force every determinant zero to be \(z=-1/\lambda_j\le-1/q_s<-1\). For \(\omega\ge0\), the spectrum of \(I+\omega K_s\) lies in \([1,1+\omega q_s]\). For \(-1\le\omega\le0\), it lies in \([1+\omega q_s,1]\). Spectral calculus yields the claimed inverse estimates, and the geometric-series remainder follows from \(\|\omega K_s\|\le|\omega|q_s<1\). The function \(g_s\) belongs to \(H_s\) because its continuous limit as \(x\downarrow0\) is \(se^{-s}\).

**Growing trace.** The standard large-argument expansion \(e^{-2x}I_1(2x)=(4\pi x)^{-1/2}(1+O(x^{-1}))\) implies \(T_s\sim\sqrt{s/\pi}\) by integration, completing the proof.

## Verification

The standalone `verify.py` checks two independently evaluated forms of the transition kernel, row-mass and gamma-mixture bounds, positivity and spectral bounds of high-order quadrature matrices, finite ordered minors, Fredholm positivity at representative physical biases, the inverse bound, the trace identity and its growing-time asymptotics. Run `python verify.py` in an environment with NumPy and SciPy as listed in `requirements.txt`; expected output is included in `verification_output.txt`. These finite numerical tests support the identities and guard against normalization errors. They do **not** prove the universal spectral, minor or Fredholm assertions; those are proved above.

## Relationship to prior work

Bénichou and Grabsch (2026) derive the exact finite-time microscopic closure for SEP and its auxiliary transition kernel, including the scalar equation and an infinite-determinant representation. The present statement does not claim the kernel, equation or auxiliary-walker interpretation as new. The assessed addition is the **all-order total-positivity theorem**, self-adjoint positive trace-class realization, explicit finite-time \(q_s\)-contraction bound, physical zero-free region and convergent-bias inversion guarantee, together with the trace-growth law. The underlying noncentral gamma/chi-square mixture and the general fact that positive trace-class kernels have negative-real Fredholm zeros are classical; their use here is not claimed as a new general principle. Prior macroscopic SEP correlation closures concern a different time and scale of description.

## Limitations

No claim of independent priority validation, microscopic SEP asymptotics beyond the source, optimality of the \(q_s\) operator-norm estimate, simplicity of all eigenvalues, an explicit closed eigenvalue formula, or conditioning in other function spaces is made. The source's supplementary material may contain implicit consequences not established by the accessible comparison; that originality risk is retained. The asymptotic trace formula is for \(s\to\infty\), whereas invertibility is proved at each finite \(s\).

## References

1. O. Bénichou and A. Grabsch, *Exact Microscopic One-Body Reduction in the Symmetric Exclusion Process*, arXiv:2610.18626v1 (first public 13 October 2026), https://arxiv.org/abs/2610.18626 .
2. A. Grabsch, D. Venturelli and O. Bénichou, *Exact Large-Scale Correlations in Diffusive Systems with General Interactions*, *Physical Review Letters* **135**, 137102 (2025), https://doi.org/10.1103/gwdh-3vqm .
3. E. W. Weisstein, *Noncentral Chi-Squared Distribution*, MathWorld, https://mathworld.wolfram.com/NoncentralChi-SquaredDistribution.html (standard mixture identity; supporting context only).
4. S. Karlin, *Total Positivity*, Vol. I (Stanford University Press, 1968). The proof of strict kernel minor positivity here is self-contained.
