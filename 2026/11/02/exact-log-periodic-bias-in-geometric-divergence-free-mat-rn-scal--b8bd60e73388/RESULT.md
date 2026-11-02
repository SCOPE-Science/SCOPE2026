# Exact log-periodic bias in geometric divergence-free Matérn scale mixtures

## Finding

For spatial dimension \(d\in\{2,3\}\), define the standard radial Matérn profile \(\phi(t)=e^{-t}(t^2+3t+3)\) and the divergence-free matrix covariance kernel
\[
K_{d,\ell}(x)=\ell^{8/3}(-\Delta I+\nabla\nabla^\top)\phi(|x|/\ell),\qquad \ell>0.
\]
Here the derivatives act on \(x\); this is the positive-semidefinite, stationary divergence-free kernel used in numerical velocity interpolation. Its trace-increment function at unit length is exactly
\[
S_d(t)=2\operatorname{tr}[K_{d,1}(0)-K_{d,1}(t e_1)]
=2(d-1)\{d-(d+dt-t^2)e^{-t}\}.
\]
For any geometric length ratio \(q>1\), the two-sided *increment* scale sum
\[
T_{d,q}(r)=\sum_{j\in\mathbb Z}q^{2j/3}S_d(rq^{-j}),\qquad r>0,
\]
converges absolutely and satisfies \(T_{d,q}(qr)=q^{2/3}T_{d,q}(r)\). However it is **not** a pure \(r^{2/3}\) power law: the normalized profile \(P_{d,q}(u)=q^{-2u/3}T_{d,q}(q^u)\) is positive, continuous, one-periodic and nonconstant for every \(q>1\). Its complete, absolutely convergent Fourier series is
\[
P_{d,q}(u)=\sum_{k\in\mathbb Z}c_k(d,q)e^{2\pi iku},\qquad
c_k(d,q)=\frac{2(d-1)(d+s_k)\Gamma(2-s_k)}{s_k\log q},
\quad s_k=\frac23+\frac{2\pi i k}{\log q}.
\]
Every coefficient \(c_k\) is nonzero. The mean is
\[
c_0(d,q)=\frac{(d-1)(3d+2)\Gamma(4/3)}{\log q}.
\]
Thus no choice of a constant coefficient yields an exact \(r^{2/3}\) fit for this ideal geometrically sampled family. Quantitatively, with
\[
E_d(q)=\inf_{C\in\mathbb R}\sup_{r>0}\left|\frac{T_{d,q}(r)}{r^{2/3}}-C\right|,
\]
one always has \(E_d(q)\ge |c_1(d,q)|>0\), and the **sharp dense-scale-grid law** is
\[
\boxed{\quad
\frac{E_d(q)}{c_0(d,q)}\sim
\frac{4\sqrt{2\pi}}{(3d+2)\Gamma(4/3)}
\left(\frac{2\pi}{\log q}\right)^{5/6}
\exp\left(-\frac{\pi^2}{\log q}\right)
\quad(q\downarrow1).\quad}
\]
For a physical finite grid of lengths \(\ell_j=q^j\), \(j_-\le j\le j_+\), let \(T_{d,q}^{[j_-,j_+]}\) be the corresponding finite trace increment. For all \(r>0\), the missing-scale error has the explicit rigorous bound
\[
0\le T_{d,q}(r)-T_{d,q}^{[j_-,j_+]}(r)
\le\frac{M_d q^{2(j_--1)/3}}{1-q^{-2/3}}
+\frac{(d-1)(d+2)r^2 q^{-4(j_++1)/3}}{1-q^{-4/3}},
\quad M_d=2(d-1)\left[d+(d+4)e^{-(d+2)}\right].
\]
The finite grid, unlike the infinite sum of covariance amplitudes, is a genuine finite positive-definite covariance mixture.

## Assumptions and scope

The result concerns the matrix-kernel **prior** and its trace covariance increment, not an empirically fitted velocity field. The dimension is exactly \(2\) or \(3\); \(q\) may be any real greater than \(1\); the evaluation separation \(r\) is positive; and the power \(8/3\) in the matrix-kernel mixture includes the two spatial derivatives, leaving a covariance amplitude \(\ell^{2/3}\). The definition of \(T_{d,q}\) is a convergent series of increments only: the two-sided sum of zero-separation covariances has infinite variance and must not be interpreted as a stationary finite-variance covariance. The reference finite-grid covariance remains well defined.

## Proof

**1. Radial trace calculation.** The trace of \((-\Delta I+\nabla\nabla^\top)\phi\) is \(-(d-1)\Delta\phi\). Direct differentiation gives \(\phi'(t)=-t(t+1)e^{-t}\) and \(\phi''(t)=(t^2-t-1)e^{-t}\). Therefore
\[
\operatorname{tr}K_{d,1}(te_1)=(d-1)e^{-t}(d+dt-t^2),
\]
which yields \(S_d\) in the finding. Its derivative is
\[
S'_d(t)=2(d-1)t(d+2-t)e^{-t}.
\]
Thus \(S_d\ge0\), is maximized uniquely at \(t=d+2\), and \(S_d(t)\le M_d\). Integrating the derivative bound on \([0,d+2]\) and using the maximum thereafter also gives \(S_d(t)\le(d-1)(d+2)t^2\) for every \(t\ge0\).

**2. Convergence and exact scaling.** Split the integer sum at \(q^j\) comparable to \(r\). The upper bound \(S_d(t)\le M_d\) makes the negative-index tail geometrically summable with ratio \(q^{2/3}\). The quadratic bound makes the positive-index tail summable with ratio \(q^{-4/3}\). Both are locally uniform on compact positive intervals. Shifting the summation index by one proves \(T_{d,q}(qr)=q^{2/3}T_{d,q}(r)\), so \(P_{d,q}\) is well-defined, positive, continuous and one-periodic. Summing the two tail estimates gives exactly the displayed finite-grid error bound.

**3. Mellin transform.** For the strip \(0<\Re s<2\), the endpoint bounds justify integration by parts:
\[
\int_0^\infty t^{-1-s}S_d(t)\,dt
=\frac1s\int_0^\infty t^{-s}S'_d(t)\,dt
=\frac{2(d-1)}s\left[(d+2)\Gamma(2-s)-\Gamma(3-s)\right]
=\frac{2(d-1)(d+s)\Gamma(2-s)}s.
\]

**4. Fourier coefficients.** Write \(L=\log q\) and \(f(v)=e^{-2v/3}S_d(e^v)\). Then \(P_{d,q}(u)=\sum_{j\in\mathbb Z}f(L(u-j))\). The previously established endpoint bounds show that \(f\) and all derivatives needed for Fourier integration are integrable. The \(k\)-th Fourier coefficient of this periodization is
\[
\frac1L\int_{\mathbb R}f(v)e^{-2\pi ikv/L}\,dv
=\frac1L\int_0^\infty t^{-1-s_k}S_d(t)\,dt.
\]
Inserting step 3 gives the stated closed form. Stirling's bound on vertical lines for \(\Gamma(4/3-iy)\) supplies exponential Fourier decay, establishing absolute and uniform convergence.

**5. Nonconstant modulation and minimax error.** Gamma has no zeros; \(\Re s_k=2/3>0\) and \(\Re(d+s_k)>0\). Hence \(c_k\ne0\) for every integer \(k\), especially \(k=1\), proving strict nonconstancy. For any \(C\), the first Fourier coefficient of \(P_{d,q}-C\) has magnitude \(|c_1|\), so \(\sup_u|P_{d,q}(u)-C|\ge|c_1|\). Since \(P\) is real and continuous, the exact minimax constant is its midrange and \(E_d(q)=(\max P-\min P)/2\).

**6. Sharp small-spacing asymptotic.** Stirling's formula for large \(|y|\) gives
\[
|\Gamma(4/3-iy)|\sim\sqrt{2\pi}|y|^{5/6}e^{-\pi|y|/2}.
\]
With \(y=2\pi/\log q\), the additional factor \(|d+s_1|/|s_1|\to1\). Consequently
\[
\frac{|c_1|}{c_0}\sim
\frac{2\sqrt{2\pi}}{(3d+2)\Gamma(4/3)}
\left(\frac{2\pi}{\log q}\right)^{5/6}e^{-\pi^2/\log q}.
\]
The uniform tail \(2\sum_{k\ge2}|c_k|=o(|c_1|)\) follows from the same vertical-line Gamma bound, so the first harmonic is asymptotically dominant. Hence \(\max P-\min P=4|c_1|(1+o(1))\); the midrange identity in step 5 gives \(E_d(q)=2|c_1|(1+o(1))\), proving the stated sharp expression. The mean term itself gives the uniformly valid continuum-scale limit \((\log q)T_{d,q}(r)/r^{2/3}\to(d-1)(3d+2)\Gamma(4/3)\).

## Verification

The standalone \(\texttt{verify.py}\) (Python 3 with \(\texttt{mpmath}\)) computes the Mellin integral and Gamma identity, direct finite approximations to the two-sided increment sum versus the Fourier series, exact discrete scaling, positive finite truncation differences within the proved tail bound, and the small-grid first-harmonic asymptotic. Its current run passed **100** finite numerical checks for both dimensions and several length ratios. For \(q=4.795077\), the calculated relative first-harmonic magnitudes \(|c_1|/c_0\) are approximately \(0.0048935898246312\) in dimension two and \(0.0040159106996802\) in dimension three. These calculations support but do not replace the proofs of infinite identities or asymptotic quantifiers.

## Relationship to prior work

Pluzhnik, Sharma, Burtscher and Shankar (2026), equations (1), (3) and (9), provide precisely the positive divergence-free Matérn kernel and the \(\ell^{8/3}\) physical-scale mixture motivated by the Kolmogorov two-thirds structure-function law; their supplementary material reports finite-range slopes of those kernels. The present result concerns the **underlying ideal geometric length-grid discretization**, its exact nonconstant trace-increment Fourier spectrum, sharp small-grid minimax constant and finite-grid cutoff estimate; it does not claim novelty of the kernel or its conservation property. Sharma, Lowery, Owhadi and Shankar (2026) likewise construct multiscale turbulence-related kernels and examine observed structure functions. Owhadi (2023) predates both with additive multiscale divergence-free Gaussian-process priors.

The general principle that geometric hierarchies yield log-periodic corrections, and the use of Mellin/Poisson/Gamma expansions, are classical and treated explicitly by Sornette (1998), including his Weierstrass–Mandelbrot example; neither discrete scale invariance nor the transform method is claimed as new. The independent specific contribution here is the fully evaluated trace-increment formula for this numerical Matérn mixture, proof of nonvanishing of its every harmonic for every grid ratio, the sharp best-power-law approximation law with its prefactor, and the computable two-sided finite-length truncation guarantee. An earlier highly general kernel-mixture theorem might imply these results by specialization, and this historical-priority risk remains.

## Limitations

The two-sided ideal is not a finite-variance stationary covariance: only its increments converge. Physical finite mixtures need not show a full period of oscillation unless their interior length range is broad enough; the cutoff bound quantifies the difference but does not guarantee observable oscillation at a prescribed finite set of separations. The trace of the covariance is not the empirical structure function of an interpolant or compressed velocity dataset. No claim is made for other radial profiles, nonlinear turbulence dynamics, arbitrary nongeometric length grids, or compression accuracy. A broad mathematical literature on log-periodic scale mixtures could contain a result that subsumes this explicit computation.

## References

1. A. Pluzhnik, R. Sharma, M. Burtscher, V. Shankar, *Property-Preserving Data Compression for Incompressible Flows*, arXiv:2610.02776v1 (public 2026-10-02), https://arxiv.org/html/2610.02776v1 .
2. R. Sharma, M. Lowery, H. Owhadi, V. Shankar, *Fluids You Can Trust: Property-Preserving Operator Learning for Incompressible Flows*, arXiv:2602.15472v5, https://arxiv.org/abs/2602.15472 .
3. D. Sornette, *Discrete Scale Invariance and Complex Dimensions*, *Physics Reports* 297 (1998), 239–270; arXiv:cond-mat/9707012v2, https://arxiv.org/abs/cond-mat/9707012 .
4. H. Owhadi, *Gaussian process hydrodynamics*, *Applied Mathematics and Mechanics* 44 (2023), 1175–1198, https://doi.org/10.1007/s10483-023-2990-9 .
