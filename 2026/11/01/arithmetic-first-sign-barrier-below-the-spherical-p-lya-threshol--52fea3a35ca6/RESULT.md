# Arithmetic first-sign barrier below the spherical Pólya threshold

## Finding

For a fixed cutoff angle \(0<\vartheta<\pi\), set
\[
I_n(\delta,\vartheta)=\int_0^\vartheta(\vartheta-t)^\delta P_n(\cos t)\sin t\,dt,
\qquad n=0,1,\ldots,
\]
where \(P_n(1)=1\) is the Legendre polynomial. For \(0<\varepsilon<1/4\), define the first negative spectral index
\[
N_-(\varepsilon,\vartheta)=\min\{n\ge1:I_n(3/2-\varepsilon,\vartheta)<0\}.
\]
The minimum exists. Write
\[
m(\vartheta)=\sup_{n\ge0}\sin((n+\tfrac12)\vartheta).
\]
Then \(0<m(\vartheta)\le1\) and the **exact first-sign law** is
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\log N_-(\varepsilon,\vartheta)
=\log\left(\frac{\sqrt{2\vartheta/\sin\vartheta}}{m(\vartheta)}\right).}
\]
The right side is strictly positive. If \(\vartheta/(2\pi)\) is irrational, \(m(\vartheta)=1\). If \(\vartheta/(2\pi)=p/q\) in lowest terms, it is given exactly by
\[
m(\vartheta)=
\begin{cases}
\cos(\pi/(2q)),&q\text{ odd},\\
1,&q\equiv2\pmod4,\\
\cos(\pi/q),&q\equiv0\pmod4.
\end{cases}
\]
Thus the first negative Schoenberg obstruction occurs at an exponentially large harmonic degree as the exponent approaches \(3/2\) from below, and the exact exponent depends discontinuously on rational cutoff-angle resonances. For example, at \(\vartheta=\pi/2\) the logarithmic rate is \(\tfrac12\log(2\pi)\), whereas its limit as irrational cutoff angles approach \(\pi/2\) is only \(\tfrac12\log\pi\).

## Assumptions and scope

The sphere is the standard two-dimensional unit sphere \(\mathbb S^2\), with geodesic distance in \([0,\pi]\). The compactly supported geodesic radial kernel is \(\phi_{\delta,\vartheta}(t)=(\vartheta-t)_+^\delta\), with fixed \(0<\vartheta<\pi\) and real \(\delta=3/2-\varepsilon\). The Fourier–Legendre coefficients have the sign of \(I_n\), because the omitted normalization factors are positive. Schoenberg's characterization therefore identifies \(N_-\) as the least harmonic degree witnessing failure of positive semidefiniteness. The asymptotic is pointwise in fixed \(\vartheta\): no uniformity as \(\vartheta\to0\) or \(\pi\) is asserted. The index \(n=0\) is always positive and is excluded only for convenience.

## Proof

**1. A two-endpoint expansion, uniformly through the critical exponent.** Put \(L=n+\tfrac12\), \(\delta\in[5/4,3/2]\), and
\[
A(\delta,\vartheta)=\Gamma(\delta+1)\sqrt{\frac{2\sin\vartheta}{\pi}},\qquad
B(\delta,\vartheta)=\delta\,\vartheta^{\delta-1}.
\]
For fixed \(\vartheta\in(0,\pi)\) the following expansion holds **uniformly** for \(\delta\) in that closed interval:
\[
\boxed{
L^3 I_n(\delta,\vartheta)=B(\delta,\vartheta)
+A(\delta,\vartheta)L^{3/2-\delta}
\cos\left(L\vartheta-\frac\pi4-\frac{\pi(\delta+1)}2\right)
+O_{\vartheta}\!\left(L^{-1}(1+L^{3/2-\delta})\right).
}
\tag{1}
\]
Here the error constant does not depend on \(n\) or \(\delta\). To obtain (1), change variables to \(x=\cos t\), so the integral is the Legendre coefficient of \(h(x)=(\vartheta-\arccos x)_+^\delta\). Use fixed smooth cutoffs at the distinct points \(x=1\) and \(x=\cos\vartheta\), leaving a smooth middle piece with arbitrarily rapidly decreasing Legendre coefficients. At \(x=1\),
\[
h(x)=\vartheta^\delta-\delta\vartheta^{\delta-1}\sqrt{2(1-x)}+O_\vartheta(1-x),
\]
with the next nonsmooth term of order \((1-x)^{3/2}\). For \(n\ge1\), the exact beta-integral identity
\[
\int_{-1}^{1}(1-x)^{1/2}P_n(x)\,dx
=-\frac1{\sqrt2}\frac{\Gamma(n-1/2)}{\Gamma(n+5/2)}
=-\frac1{\sqrt2}L^{-3}+O(L^{-4})
\]
proves the positive coefficient \(+B L^{-3}\) without a sign-convention ambiguity. Integer powers at this endpoint contribute no algebraic tail. At the interior cutoff, \(h(x)=(\sin\vartheta)^{-\delta}(x-\cos\vartheta)_+^\delta(1+O_\vartheta(x-\cos\vartheta))\). The interior Darboux expansion
\[
P_n(\cos t)\sin t=\sqrt{\frac{2\sin t}{\pi L}}\cos(Lt-\pi/4)+O_\vartheta(L^{-3/2})
\]
on a small fixed neighborhood of \(t=\vartheta\), followed by endpoint Fourier-Watson integration of \(u^\delta\), gives the oscillating term with the displayed gamma coefficient. The next local terms are \(O_\vartheta(L^{-\delta-5/2})\); the next endpoint-at-one term is \(O_\vartheta(L^{-5})\). After multiplication by \(L^3\), these are bounded by the remainder in (1). The local cutoff procedure, integration-by-parts bounds, and gamma factors vary smoothly with \(\delta\) on the stated compact interval, making these estimates uniform. This is the two-leading-contribution specialization of the Legendre singularity-expansion method of Sidi (2011, Theorem 4.2), with its parameter-uniform remainder justified by the same localized estimates. Importantly, the bulk \(O(L^{-3/2})\) remainder in the raw Darboux formula is **not** integrated without oscillatory cancellation; the full asymptotic series and localized Watson bounds are used to recover the stated extra power of \(L^{-1}\).

**2. Critical strict positivity.** Lu's truncated-power result (2024 online publication; Theorem 3.5 and its proof) gives
\[
I_n(3/2,\vartheta)>0\qquad(n\ge0,\ 0<\vartheta\le\pi).
\tag{2}
\]
This provides positivity of any fixed finite list of degrees for all sufficiently small \(\varepsilon\), by continuity in \(\delta\).

**3. Phase arithmetic.** Set \(\delta=3/2-\varepsilon\) in (1). Then
\[
L^3I_n(3/2-\varepsilon,\vartheta)
=B_\varepsilon-A_\varepsilon L^\varepsilon
\sin(L\vartheta+\pi\varepsilon/2)
+O_\vartheta(L^{-1}(1+L^\varepsilon)),
\tag{3}
\]
where \(A_\varepsilon=A(3/2-\varepsilon,\vartheta)\) and \(B_\varepsilon=B(3/2-\varepsilon,\vartheta)\). Both converge to positive constants. Their ratio is
\[
\frac{B_0}{A_0}=\sqrt{\frac{2\vartheta}{\sin\vartheta}}>1.
\]
For irrational \(\vartheta/(2\pi)\), the sequence \((n+1/2)\vartheta\) is dense modulo \(2\pi\), so its sine supremum is one. Every open phase arc is visited with bounded gaps (minimality of irrational circle rotation). For rational angle \(\vartheta=2\pi p/q\), the sequence is periodic modulo \(2\pi\). Inspecting the odd residues \(p(2n+1)\) modulo \(2q\), the nearest attainable angle to \(\pi/2\) lies at distance \(\pi/(2q)\) for odd \(q\), zero for \(q\equiv2\pmod4\), and \(\pi/q\) for \(q\equiv0\pmod4\). This proves the stated formula for \(m\). Uniformly over the entire orbit, a phase perturbation of \(\pi\varepsilon/2\) changes its maximal sine by at most \(\pi\varepsilon/2\).

**4. Matching exponential fences.** Write \(C=\log(B_0/(A_0m(\vartheta)))>0\). Fix \(0<\eta<C\). For all large \(n\) with \(L\le\exp((C-\eta)/\varepsilon)\), the right side of (3) is positive: the maximal sine is at most \(m+O(\varepsilon)\), while \(L^\varepsilon\le e^{C-\eta}\); this leaves a uniform positive gap in the leading terms. Choose the lower cutoff \(n_0\) sufficiently large to make the \(O_\vartheta(L^{-1}(1+L^\varepsilon))\) remainder smaller than half this gap. For \(n<n_0\), positivity follows from (2). Thus
\[
N_-(\varepsilon,\vartheta)>\exp((C-\eta)/\varepsilon)+O(1).
\]
Conversely, choose a fixed phase neighborhood in which \(\sin(L\vartheta+\pi\varepsilon/2)\ge m-\rho\), with \(\rho>0\) small depending on \(\eta\). Periodicity in the rational case, or the bounded-gap visit property in the irrational case, gives such an index in every sufficiently long integer interval. In particular, one can choose \(n\) between \(\exp((C+\eta/2)/\varepsilon)\) and \(\exp((C+\eta)/\varepsilon)\). The negative oscillatory term in (3) then strictly exceeds \(B_\varepsilon\), and the uniform remainder tends to zero. Hence
\[
N_-(\varepsilon,\vartheta)\le\exp((C+\eta)/\varepsilon)
\]
for small \(\varepsilon\). Letting \(\eta\downarrow0\) proves the limit and finiteness of the first negative index. \(\square\)

## Verification

The accompanying standard-library script `CHECK.py` independently checks the exact residue-class phase maxima over all reduced rational angles with denominators up to \(150\), numerical positivity of the critical coefficient at representative degrees, a specific first-negative sign pair for near-critical exponents at cutoff \(\pi/2\), and one two-endpoint asymptotic comparison. All checks ran successfully (3,437 assertions). Finite checks are supplementary and do **not** prove the infinite-degree result. The proof rests on (1), strict critical positivity, and the phase-fence argument above. In particular, (1) requires a uniform, not merely pointwise, singularity estimate in \(\delta\).

## Relationship to prior work

Beatson, zu Castell, and Xu formulated the positive-definiteness and Gegenbauer Pólya integral problem. Lu proved strict positivity of truncated powers at the exponent \((d+1)/2\), including \(3/2\) on \(\mathbb S^2\); the later continuous-parameter Pólya extension also concerns sufficiency. Neither yields the first negative degree below the threshold. Sidi developed complete asymptotic expansions of Legendre coefficients for interior and endpoint singularities, supplying the foundational asymptotic method; its fixed-parameter expansion does not itself state the moving-parameter first-sign law, the exponential rate, or the rational-angle resonance. Ge's 2026 study of even-dimensional spherical positive definiteness motivates the quantified spectral obstruction question but concerns different kernels and no such threshold law. The present assertion is the **joint** exponential first-index limit and exact rational-angle classification, not the already-known critical positivity or a fixed-exponent sign-oscillation corollary.

## Limitations

This result concerns fixed cutoff angles strictly between zero and \(\pi\), the two-dimensional sphere, and exponents approaching \(3/2\) from below. No effective finite-\(\varepsilon\) error bound for \(N_-\), higher-sphere generalization, or endpoint-uniform estimate is claimed. The originality assessment remains subject to unindexed prior work on simultaneous parameter-degree asymptotics; an independent mathematical audit has not been performed.

## References

1. Y. Ge, “Isotropic Positive Definite Functions on Spheres: Even-Dimensional Gneiting's Problem,” arXiv:2608.22173, first posted 2026-08-23. https://arxiv.org/abs/2608.22173
2. T. Lu, “Strictly positive definite functions on spheres,” *Journal of Approximation Theory* 306 (2025), 106120, first online 2024-11-15. https://doi.org/10.1016/j.jat.2024.106120
3. A. Sidi, “Asymptotic expansions of Legendre series coefficients for functions with interior and endpoint singularities,” *Mathematics of Computation* 80 (2011), 1663–1684; electronically posted 2010-12-30. https://doi.org/10.1090/S0025-5718-2010-02454-8
4. R. K. Beatson, W. zu Castell, and Y. Xu, “A Pólya criterion for (strict) positive-definiteness on the sphere,” arXiv:1110.2437, first posted 2011-10-11. https://arxiv.org/abs/1110.2437
5. “Boundary positivity for the Gegenbauer Pólya integral at every real parameter,” published mathematical record (2026-09-20). https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-gegenbauer-polya-boundary-all-real-lambda--107c9b8148b4
