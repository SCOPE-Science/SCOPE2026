# Critical fractional-power collapse of the sharp spherical mixed-norm stability gap

## Finding

Let \(d\ge 3\) be an integer, let \(\sigma\) be unnormalized surface measure on \(\mathbb S^{d-1}\), and use the Fourier phase \(e^{-ix\cdot\omega}\). Put
\[
q_c=\frac{2d}{d-1},\qquad \nu=\frac d2-1,\qquad
I_k(q)=\int_0^\infty |J_{\nu+k}(r)|^q r^{d-1-\nu q}\,dr.
\]
For every \(q>q_c\), let \(C_{d,q}\) be the optimal norm of spherical Fourier extension from \(L^2(\mathbb S^{d-1})\) into \(L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}\), and let \(\Gamma_{d,q}\) be the *optimal* coefficient in its global squared-norm stability inequality relative to constant data, as defined below. Define the cosine mean and a positive constant by
\[
 m(p)=\frac{\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma((p+2)/2)},\qquad
 B_d=\frac{2}{d-1}\left(\frac2\pi\right)^{q_c/2}m(q_c).
\]
Then the adjacent-mode critical cancellation integral
\[
 \Delta_d=\lim_{R\to\infty}\int_0^R
 r^{d-1-\nu q_c}\left(|J_\nu(r)|^{q_c}-|J_{\nu+1}(r)|^{q_c}\right)\,dr
\]
exists as an ordinary improper integral and is **strictly positive**, although the two separate integrals diverge logarithmically. Moreover,
\[
 \boxed{\displaystyle
 \lim_{q\downarrow q_c}\frac{\Gamma_{d,q}}{(q-q_c)^{1/d}}
 =(2\pi)^d\frac{2\Delta_d}{q_c B_d^{1/d}}>0.}
\]
There are also two compatible endpoint laws:
\[
 \lim_{q\downarrow q_c}\frac{C_{d,q}^2}{(q-q_c)^{-(d-1)/d}}
 =(2\pi)^d B_d^{(d-1)/d},\qquad
 \lim_{q\downarrow q_c}\frac{\Gamma_{d,q}}{C_{d,q}^2(q-q_c)}
 =\frac{2\Delta_d}{q_c B_d}.
\]
Thus the *absolute* sharp stability gap collapses with a dimension-dependent fractional exponent \(1/d\), whereas the *relative* sharp stability gap collapses linearly at the strong-type threshold.

## Assumptions and scope

For \(f\in L^2(\mathbb S^{d-1},d\sigma)\), define
\[
 (\mathcal Ef)(x)=\int_{\mathbb S^{d-1}} e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),\quad
 \|F\|_{q,2}=\left[\int_0^\infty
 \left(\int_{\mathbb S^{d-1}}|F(r\theta)|^2\,d\sigma(\theta)\right)^{q/2}
 r^{d-1}\,dr\right]^{1/q}.
\]
Let \(P_0\) be orthogonal projection onto constant spherical harmonics. Set
\[
 C_{d,q}=\sup_{f\ne0}\frac{\|\mathcal Ef\|_{q,2}}{\|f\|_2},\qquad
 \Gamma_{d,q}=\inf_{f\ne P_0f}
 \frac{C_{d,q}^2\|f\|_2^2-\|\mathcal Ef\|_{q,2}^2}
 {\|f-P_0f\|_2^2}.
\]
All assertions are for every fixed integer \(d\ge3\) and the one-sided real limit \(q\downarrow q_c\). There is **no** assertion at the inadmissible endpoint \(q=q_c\) that the extension operator is bounded. The \(d=2\) case is not covered, because identifying the largest nonconstant harmonic mode there requires a separate comparison.

## Proof

**1. Exact spectral input.** The spherical Fourier--Bessel decomposition of Carneiro--Oliveira e Silva--Sousa expresses the mixed norm through the weighted Bessel moments \(I_k(q)\). Xu's strict modal ordering and sharp stability theorem (Theorems 1.2--1.3 of arXiv:2610.19648) give, specifically for \(d\ge3\) and every finite \(q>q_c\),
\[
 C_{d,q}^2=(2\pi)^d I_0(q)^{2/q},\qquad
 \Gamma_{d,q}=(2\pi)^d\left(I_0(q)^{2/q}-I_1(q)^{2/q}\right).
\]
These *known* identities and the modal ordering are not asserted as new results. The present finding concerns their singular endpoint asymptotics, including the nonzero renormalized gap.

**2. A common pole of all fixed-order moments.** Fix \(k=0\) or \(1\), and write \(\varepsilon=q-q_c\) and \(a=(d-1)\varepsilon/2\). The fixed-order Hankel expansion yields, uniformly for \(q\) in a compact interval beginning at \(q_c\),
\[
 r^{d-1-\nu q}|J_{\nu+k}(r)|^q
 =\left(\frac2\pi\right)^{q/2}r^{-1-a}
 \left(|\cos(r-\phi_k)|^q+O_d(r^{-1})\right),
 \qquad \phi_k=\frac{\pi(\nu+k)}2+\frac\pi4,
\]
for \(r\ge1\). Uniformity follows because \(t\mapsto|t|^q\) is uniformly Lipschitz on bounded intervals for these exponents. The \(\pi\)-periodic function \(|\cos t|^q-m(q)\) has a uniformly bounded primitive for such \(q\). Integration by parts therefore bounds its integral against \(r^{-1-a}\) over \([R,\infty)\) by \(O_d(R^{-1-a})\) uniformly for small \(a\ge0\). The \(O_d(r^{-1})\) Hankel remainder is absolutely integrable after multiplication by \(r^{-1-a}\). Consequently
\[
 I_k(q)=\frac{(2/\pi)^{q/2}m(q)}{a}+H_k(q),
\]
where each \(H_k(q)\) has a finite continuous limit as \(q\downarrow q_c\). In particular,
\[
 I_k(q)=\frac{B_d}{\varepsilon}+O_d(1),\qquad
 I_0(q)-I_1(q)\longrightarrow\Delta_d.
\]
The convergence of the difference at \(q_c\) is conditional, not absolute; its tail is a zero-mean periodic term divided by \(r\), plus an absolutely integrable remainder. These estimates also prove the existence of the displayed ordinary improper integral independently of any comparison theorem.

**3. The coefficient is nonzero and positive.** Theorem 3.9 and its proof in Xu, arXiv:2610.19648, establish a more precise *finite-cell* statement: for every real \(\nu\ge0\), every \(q>2\), and every positive Bessel zero \(z_n=j_{\nu+1,n}\), the integral of
\[
 r^{2\nu+1}\left(|r^{-\nu}J_\nu(r)|^q-|r^{-\nu}J_{\nu+1}(r)|^q\right)
\]
over each complete cell \([z_{n-1},z_n]\), with \(z_0=0\), is strictly positive. This follows there from the adjacent-order Bessel recurrences, a convex scalar flux, and a reflected Wronskian comparison. Apply the *proved finite-cell statement* at \(q=q_c>2\). The successive truncations of our critical difference integral at \(z_N\) form a strictly increasing sequence whose first term is positive. Step 2 proves that they converge to the same improper-integral limit \(\Delta_d\). Therefore \(\Delta_d>0\). Positivity is **not** inferred from finite experiments or from the inequality between the separately divergent moments.

**4. Extract the fractional law.** By the real mean-value theorem, for every \(q>q_c\),
\[
 I_0(q)^{2/q}-I_1(q)^{2/q}
 =\frac2q\,\xi(q)^{2/q-1}\big(I_0(q)-I_1(q)\big),
\]
with \(\xi(q)\) between the two positive moments. Step 2 implies \(\varepsilon\xi(q)\to B_d\) and Step 3 implies \(I_0-I_1\to\Delta_d>0\). As \(2/q_c=(d-1)/d\), we have
\[
 \varepsilon^{-1/d}\xi(q)^{2/q-1}\longrightarrow B_d^{-1/d};
\]
the varying exponent causes no extra factor because \(\varepsilon\log\varepsilon\to0\). Substitution gives the displayed sharp constant. The sharp extension-norm law follows from \(I_0(q)\sim B_d/\varepsilon\). Finally, dividing the two leading expressions gives the exact relative-gap coefficient \(2\Delta_d/(q_cB_d)\). All limits are for fixed \(d\).

## Verification

The reproducibility script `verify.py` numerically evaluates the finite-cutoff critical difference and nearby noncritical Bessel moments for \(d=3,4,5\), with a leading Hankel mean used only to accelerate the *noncritical* tails. Its output compares the scaled sharp gap with the predicted coefficient and checks the trend as \(q\downarrow q_c\). The script is supplementary: finite cutoff and numerical quadrature do **not** prove the positive infinite integral, the sharp modal ordering, or the limiting theorem. Steps 1--4 are the mathematical proof.

## Relationship to prior work

Carneiro--Oliveira e Silva--Sousa (2017, arXiv:1710.10365) reduced sharp radial--angular spherical Fourier extension to weighted Bessel moments and identified modal maximizers in important exponent ranges. Carneiro--Negro--Oliveira e Silva (initially made public on 2024-10-30, arXiv:2410.23106) developed related sharp extension and spectral stability questions in all dimensions, but for a different ordinary \(L^4\) extension functional. Xu (first public 2026-10-14, arXiv:2610.19648, Theorems 1.2, 1.3, and 3.9) established the global sharp finite-exponent mixed-norm stability gap and its key finite-cell Bessel positivity. **Those results are inputs, not new claims here.** The present finding is the strict positive *critical cancellation integral*, and the exact fractional- and linear-collapse laws as \(q\downarrow 2d/(d-1)\); these limits are not stated in the inspected works.

## Limitations

The proof uses the nontrivial adjacent-order finite-cell positivity theorem of Xu as a cited input rather than offering a second independent derivation. The coefficient \(\Delta_d\) is a convergent improper Bessel integral, not a closed-form elementary number. Neither the bound at the strong-type critical endpoint nor the dimension-two ordering problem is resolved here. Historical priority is not independently certified, and genuinely unindexed equivalent asymptotics remain a residual risk. The supplementary quadrature does not certify infinite-integral signs. No independent scientific audit has been performed.

## References

1. E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365 (first public 2017-10-28), especially Theorem 1 and the Fourier--Bessel decomposition. https://arxiv.org/abs/1710.10365
2. E. Carneiro, G. Negro, D. Oliveira e Silva, *On sharp Fourier extension from spheres in arbitrary dimensions*, arXiv:2410.23106 (first public 2024-10-30). https://arxiv.org/abs/2410.23106
3. Z. Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648 (first public 2026-10-14), especially Theorems 1.2, 1.3 and the complete-cell argument in Theorem 3.9. https://arxiv.org/abs/2610.19648
4. NIST Digital Library of Mathematical Functions, Chapter 10, especially the fixed-order large-argument Hankel asymptotics for Bessel \(J\). https://dlmf.nist.gov/10.17
