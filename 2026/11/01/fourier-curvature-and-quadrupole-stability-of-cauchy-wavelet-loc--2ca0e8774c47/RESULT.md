# Fourier curvature and quadrupole stability of Cauchy-wavelet localization purity

## Finding

Fix \(\lambda>1\) and \(U>0\). On the unit disk \(\mathbb D\), equip the analytic weighted Bergman space \(A^2_{\lambda-2}\) with probability-normalized area weight \((\lambda-1)(1-|z|^2)^{\lambda-2}\,dA(z)/\pi\). Let \(k_z\) denote its unit reproducing kernel, and put
\[
 d\nu(z)=\frac{dA(z)}{(1-|z|^2)^2},\qquad
 L_\Omega=\int_\Omega |k_z\rangle\langle k_z|\,d\nu(z),\qquad
 \mathcal E(\Omega)=\operatorname{Tr}(L_\Omega^2).
\]
The operator is positive and trace class whenever \(\nu(\Omega)<\infty\). Define the hyperbolic area coordinate \(u(z)=|z|^2/(1-|z|^2)\). For a real \(2\pi\)-periodic \(f\in C^2\) with mean zero and sufficiently small real \(\varepsilon\), set
\[
 \Omega_{\varepsilon,f}=\{r e^{i\theta}:0\le u(r)<U+\varepsilon f(\theta)\},\qquad
 D_U=\Omega_{0,f}.
\]
These sets all have exactly the same \(\nu\)-area \(\pi U\). Use Fourier coefficients \(\widehat f_n=(2\pi)^{-1}\int_0^{2\pi}f(\theta)e^{-in\theta}\,d\theta\) and put
\[
 c_n(U,\lambda)=\frac1{2\pi}\int_0^{2\pi}
 \frac{\cos(n\theta)\,d\theta}
 {[1+2U(U+1)(1-\cos\theta)]^\lambda},\qquad n\ge0.
\]
**The exact shape-Hessian theorem** is
\[
 \boxed{\mathcal E(D_U)-\mathcal E(\Omega_{\varepsilon,f})
 =\pi^2\varepsilon^2\sum_{|n|\ge2}
 [c_1(U,\lambda)-c_{|n|}(U,\lambda)]|\widehat f_n|^2
 +o_f(\varepsilon^2).}
\]
For every \(U>0\) and \(\lambda>1\),
\[
 c_0>c_1>c_2>\cdots>0,\qquad \lim_{n\to\infty}c_n=0.
\]
Thus the only zero-curvature directions under the area constraint are the two infinitesimal hyperbolic translations \(\cos\theta\) and \(\sin\theta\). After these modes are excluded, the **sharp quadratic stability coefficient** in the normalization above is \(\pi^2(c_1-c_2)\) per unit \(\sum_{|n|\ge2}|\widehat f_n|^2\), attained exactly by nonzero second harmonics. This is a Hessian-level statement; it does not assert a uniform nonlinear inequality over varying perturbations.

The coefficients have an explicit convergent hypergeometric representation. With \(t=U/(1+U)\),
\[
 c_n(U,\lambda)=\frac{t^n}{(1+U)^{2\lambda}}
 \frac{(\lambda)_n}{n!}
 {}_2F_1(\lambda+n,\lambda;n+1;t^2),\quad n\ge0,
\]
where \((\lambda)_n=\Gamma(\lambda+n)/\Gamma(\lambda)\). For example, when \(U=1\) and \(\lambda=2\),
\[
 c_n=\frac{5+3n}{27\,2^n},\qquad c_1-c_2=\frac5{108},
\]
so that for \(f(\theta)=\cos(2\theta)\),
\[
 \mathcal E(D_1)-\mathcal E(\Omega_{\varepsilon,f})
 =\frac{5\pi^2}{216}\varepsilon^2+o(\varepsilon^2).
\]

## Assumptions and scope

The entire theorem holds for every real \(\lambda>1\), \(U>0\), and fixed real mean-zero \(f\in C^2(\mathbb R/2\pi\mathbb Z)\). The requirement \(U+\varepsilon f(\theta)>0\) is secured by taking \(\varepsilon\) sufficiently small depending on \(U\) and \(f\). The area measure \(d\nu=dA/(1-|z|^2)^2\) is deliberately specified: it is one-quarter of the curvature-minus-one Poincaré area element. The density, coherent states, and operator all use this single convention. The result transfers under the Cayley correspondence to Cauchy-wavelet localization operators, with the expected fixed positive rescaling induced by the chosen hyperbolic area normalization and wavelet normalization. The statement does not concern other wavelet windows or arbitrary nonsmooth shape variations.

## Proof

**1. Coherent-state energy.** The weighted Bergman kernel is \(K(z,w)=(1-z\overline w)^{-\lambda}\), so the normalized overlap satisfies
\[
 |\langle k_z,k_w\rangle|^2
 =\left(\frac{(1-|z|^2)(1-|w|^2)}{|1-z\overline w|^2}\right)^\lambda.
\]
Because \(\operatorname{Tr}(|k_z\rangle\langle k_z|)=1\), the operator-valued integral defining \(L_\Omega\) converges in trace norm on finite-area sets. Tonelli's theorem and the rank-one trace identity give
\[
 \mathcal E(\Omega)=\int_{\Omega\times\Omega}
 |\langle k_z,k_w\rangle|^2\,d\nu(z)d\nu(w).
\]
The density is invariant under disk automorphisms, and the modulus of the normalized kernel overlap is invariant under simultaneous automorphisms. Hence \(\mathcal E\) is unchanged when its domain is moved by a disk automorphism.

**2. Exact area coordinate and the boundary kernel.** Write \(z=r e^{i\theta}\) and \(u=r^2/(1-r^2)\). Then \(d\nu=\tfrac12\,du\,d\theta\). Define
\[
 F(u,v,\psi)=\left[(1+u)(1+v)+uv
 -2\sqrt{uv(1+u)(1+v)}\cos\psi\right]^{-\lambda}.
\]
Consequently,
\[
 \mathcal E(\Omega_{\varepsilon,f})=\frac14
 \int_0^{2\pi}\!\int_0^{2\pi}\!
 \int_0^{U+\varepsilon f(\theta)}\!\int_0^{U+\varepsilon f(\phi)}
 F(u,v,\theta-\phi)\,dv\,du\,d\phi\,d\theta.
\]
The first derivative vanishes for mean-zero \(f\) by rotation invariance of the centered disk. The boundary interaction is
\[
 B(\psi)=F(U,U,\psi)
 =[1+2U(U+1)(1-\cos\psi)]^{-\lambda},
\]
with Fourier coefficients \(c_{|n|}\).

**3. Second derivative and the translation identity.** Differentiating the upper limits twice is legitimate for fixed \(U>0\). Set the finite constant
\[
 C=\int_0^{2\pi}\int_0^U
 \partial_u F(U,v,\psi)\,dv\,d\psi.
\]
The product rule, including both mixed boundary derivatives, yields
\[
 \mathcal E''(0)=\frac C2\int_0^{2\pi}f(\theta)^2\,d\theta
 +\frac12\int_0^{2\pi}\!\int_0^{2\pi}
 f(\theta)f(\phi)B(\theta-\phi)\,d\phi\,d\theta.
\]
For completeness, the identity \(C=-2\pi c_1\) does not require evaluating the potential integral. Move \(D_U\) by the one-parameter disk automorphism \(z\mapsto(z+a)/(1+az)\), with small real \(a\). The translated boundary remains a smooth radial graph in \(u\), whose first derivative at \(a=0\) is the nonzero multiple \(2\sqrt{U(U+1)}\cos\theta\). The moving domains have exactly constant area, so both the first- and second-order boundary-coordinate variations have zero angular mean. Their energy is constant by automorphism invariance; the contribution of the second-order coordinate variation to the second derivative vanishes since the first-variation functional is a constant times angular mean. Thus \(\mathcal E''(0)\) must vanish on \(f=\cos\theta\). Substitution in the preceding formula and the Fourier normalization give precisely \(C=-2\pi c_1\).

Using Parseval and circle convolution,
\[
 \mathcal E''(0)=2\pi^2\sum_{n\in\mathbb Z}
 (c_{|n|}-c_1)|\widehat f_n|^2.
\]
The mean-zero condition deletes \(n=0\), and the two \(|n|=1\) terms vanish. Taylor's theorem gives the asserted deficit formula.

**4. Strict ordering of the Fourier curvatures.** Put \(A=1+2U(U+1)\), \(B_0=2U(U+1)\), so \(A>B_0>0\). The Gamma integral and the generating function of the modified Bessel functions give
\[
 c_n=\frac1{\Gamma(\lambda)}\int_0^\infty
 s^{\lambda-1}e^{-As}I_n(B_0s)\,ds,\qquad n\ge0.
\]
For every \(x>0\) and integer \(n\ge0\), \(I_{n+1}(x)<I_n(x)\). Indeed, the positive ratio \(r_n(x)=I_{n+1}(x)/I_n(x)\) starts below one as \(x\downarrow0\) and satisfies
\[
 r_n'(x)=1-\frac{2n+1}{x}r_n(x)-r_n(x)^2.
\]
At a purported first upward crossing of \(r_n=1\), its derivative would equal \(-(2n+1)/x<0\), a contradiction. Therefore integrating the strict inequality against the positive weight proves \(c_n>c_{n+1}>0\) for every \(n\). The Riemann-Lebesgue lemma gives \(c_n\to0\). Thus the least negative nontranslation curvature is the second Fourier harmonic, with strict inequality for every higher harmonic.

**5. Hypergeometric and elementary coefficients.** Factor the boundary denominator as
\[
 1+2U(U+1)(1-\cos\theta)
 =(1+U)^2|1-t e^{i\theta}|^2,
 \quad t=\frac U{1+U}.
\]
Multiply the absolutely convergent binomial series for the two factors \((1-te^{i\theta})^{-\lambda}\) and \((1-te^{-i\theta})^{-\lambda}\). Selecting Fourier index \(n\ge0\) gives the displayed \({}_2F_1\) representation. For \(\lambda=2\) and \(U=1\), the resulting sum is
\[
 c_n=\frac{2^{-n}}{16}\sum_{j=0}^\infty
 (j+1)(j+n+1)4^{-j}
 =\frac{5+3n}{27\,2^n},
\]
which proves the exact example and its deficit coefficient.

## Verification

The accompanying standalone `checks/check_hessian.py` evaluates the Fourier coefficients independently by angular quadrature and hypergeometric summation; tests their strict ordering on finite ranges and the exact rational test case; and compares the analytical Hessian with symmetric finite differences of the original four-variable coherent-state energy for several angular modes. It also checks that the translation mode has zero quadratic coefficient to the expected finite-difference accuracy. These are finite numerical stress tests, not substitutes for the Gamma-integral, automorphism, or Fourier arguments above.

## Relationship to prior work

Ramos and Tilli proved a Faber–Krahn theorem identifying hyperbolic disks as unique maximizers of **operator-norm** Cauchy-wavelet localization at fixed hyperbolic area (first public arXiv version May 16, 2022). Nicola and Riccardi proved a Hilbert–Schmidt rearrangement theorem for localization operators and its hyperbolic wavelet counterpart, together with quantitative results for the Euclidean Gaussian problem (first public arXiv version January 9, 2024). Their wavelet result establishes the global extremizer but not the exact boundary-perturbation curvature spectrum proved here. Gómez, Kalaj, Melentijević and Ramos subsequently established quantitative stability for the **operator-norm** Cauchy-wavelet concentration problem (November 24, 2024 arXiv version); that does not specify the Hilbert–Schmidt shape Hessian. Older nonlocal isoperimetric second-variation work is a methodological analogue in Euclidean settings with different kernels. The general coherent-state trace identity, hyperbolic invariance, and strict disk maximization are used as known facts, not claimed as discoveries.

## Limitations

This theorem is a fixed-perturbation second-order expansion and exact Hessian diagonalization. It does not prove a new global isoperimetric inequality, a uniform remainder estimate for families of functions with unbounded derivatives, an operator-norm Hessian, or any statement about other wavelet windows. The original status is based on comparison with the inspected sources and targeted research-record searches, not a proof of historical uniqueness. The work has undergone self-review, but no independent audit or validation.

## References

1. J. P. G. Ramos and P. Tilli, *A Faber–Krahn inequality for wavelet transforms*, arXiv:2205.07998v1 (May 16, 2022), https://arxiv.org/abs/2205.07998.
2. F. Nicola and F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert–Schmidt norm of localization operators*, arXiv:2401.04659v1 (January 9, 2024), https://arxiv.org/abs/2401.04659. Relevant: Proposition 3.1 and Section 6.
3. J. Gómez, D. Kalaj, P. Melentijević and J. P. G. Ramos, *Uniform stability of concentration inequalities and applications*, arXiv:2411.16010v1 (November 24, 2024), https://arxiv.org/abs/2411.16010.
4. M. Bonacini and R. Cristoferi, *Local and global minimality results for a nonlocal isoperimetric problem on* \(\mathbb R^N\), arXiv:1307.5269v1 (July 19, 2013), https://arxiv.org/abs/1307.5269 (methodological comparison only).
