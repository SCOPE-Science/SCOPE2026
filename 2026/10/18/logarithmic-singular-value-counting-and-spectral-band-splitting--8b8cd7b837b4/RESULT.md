# Logarithmic singular-value counting and spectral-band splitting for modulated Cesàro sections

## Finding
Let \(C_N\) be the \(N\times N\) Cesàro matrix, \((C_N)_{jk}=j^{-1}\mathbf 1_{k\le j}\), and let \(D_{\omega,N}=\operatorname{diag}(j^{i\omega})_{j=1}^N\) for real \(\omega\ne0\). Put \(A_{N,\omega}=C_ND_{\omega,N}-D_{\omega,N}C_N\), and let \(M_{N,\omega}(t)\) count its singular values strictly exceeding \(t>0\). With \(w=|\omega|\), for every fixed \(0<t<2\),
\[
\lim_{N\to\infty}\frac{M_{N,\omega}(t)}{\log N}
=\mathcal D_w(t):=\frac{\sqrt{(q_+(w,t))_+}-\sqrt{(q_-(w,t))_+}}{\pi},
\qquad q_\pm(w,t)=\frac{w^2-1}{4}\pm\frac{w}{t}\sqrt{1-\frac{t^2}{4}},
\]
where \((y)_+=\max(y,0)\). For \(t\ge2\) the limit is zero. Equivalently, for all \(t>0\),
\[
\mathcal D_w(t)=\frac1{2\pi}\bigl|\{\xi\in\mathbb R:\sigma_w(\xi)>t\}\bigr|,
\quad \sigma_w(\xi)=\frac{w}{\sqrt{(\xi^2+1/4)((\xi+w)^2+1/4)}}.
\]
For \(0<w\le1\) every nonempty superlevel set is a single interval. For \(w>1\), the superlevel set is the union of two disjoint intervals precisely when \(4w/(1+w^2)<t<2\). Thus the count of singular values above a fixed threshold is logarithmic in the section size, with an explicitly computable two-band transition at \(w=1\).

For every integer \(m\ge1\), the same family has the complete leading even singular-moment law
\[
\lim_{N\to\infty}\frac{\operatorname{tr}(A_{N,\omega}^*A_{N,\omega})^m}{\log N}
=\frac1{2\pi}\int_\mathbb R \sigma_w(\xi)^{2m}\,d\xi.
\]
At order two this coefficient is particularly simple:
\[
\lim_{N\to\infty}\frac{\|A_{N,\omega}\|_{\mathcal S_2}^2}{\log N}
=\frac{2w^2}{1+w^2}.
\]
For \(\omega=0\), every commutator is zero; no limit statement is made at the threshold \(t=0\).

## Assumptions and scope
The matrices act on complex Euclidean spaces with the usual \(\ell^2\) inner product. The frequency \(\omega\) and level \(t>0\) are held fixed as \(N\to\infty\). Counts are not normalized by \(N\); their natural scale is \(\log N\). The superlevel law is asserted at each fixed positive level, not uniformly as the level tends to zero with \(N\). The asserted split concerns the level sets of the explicit limiting singular-value symbol, not any claim about finite-matrix eigenvalue intervals or individual singular-value monotonicity.

## Proof
**Step 1: uniformly Hilbert–Schmidt-close continuous model.** Embed \(\mathbb C^N\) isometrically into \(L^2([1,N+1])\) by mapping the \(j\)-th coordinate to the indicator of \([j,j+1)\). Extend the embedded matrix by zero on the orthogonal complement. Its integral kernel on the pair of unit cells \([j,j+1)\times[k,k+1)\) is
\[
\mathbf1_{k\le j}\frac{k^{i\omega}-j^{i\omega}}j.
\]
Compare it with the continuous finite-interval commutator \(B_N=HM_\omega-M_\omega H\), where \((Hf)(x)=x^{-1}\int_1^x f(y)\,dy\) and \((M_\omega f)(x)=x^{i\omega}f(x)\). Its kernel is \(\mathbf1_{y<x}(y^{i\omega}-x^{i\omega})/x\). On cells with \(k<j\), the mean-value estimate \(|u^{i\omega}-v^{i\omega}|\le w|u-v|/\min(u,v)\) and \(|x^{-1}-j^{-1}|\le j^{-2}\) bound the pointwise kernel error by \(c_w(1/(jk)+1/j^2)\). On diagonal cells, the discrete kernel is zero and the continuous one is bounded by \(w/j^2\). All cells above the diagonal have zero kernel. Therefore
\[
\sup_{N\ge1}\|A_{N,\omega}^{\rm embedded}-B_N\|_{\mathcal S_2}^2
\le c'_w\sum_{j=1}^\infty\left(\frac1{j^2}\sum_{k=1}^j\frac1{k^2}+\frac1{j^3}\right)<\infty.
\]
The finite-matrix and embedded singular values differ only by appended zeros.

**Step 2: logarithmic convolution.** Put \(L=\log(N+1)\), and use the unitary change of variables \((Uf)(u)=e^{u/2}f(e^u)\) from \(L^2([1,N+1])\) to \(L^2([0,L])\). The transform of \(B_N\) is multiplication by \(e^{i\omega u}\), followed by the finite convolution with
\[
h_\omega(s)=\mathbf1_{s\ge0}e^{-s/2}(e^{-i\omega s}-1).
\]
This multiplication is unitary, so it does not affect singular values. Denote by \(T_h\) convolution by \(h_\omega\) on \(L^2(\mathbb R)\) and by \(P_L\) multiplication by \(\mathbf1_{[0,L]}\). The finite convolution is \(W_L=P_LT_hP_L\), regarded on \(P_LL^2\). Under the Fourier convention \(\widehat f(\xi)=\int_\mathbb R e^{-i\xi s}f(s)\,ds\), its full-line multiplier is
\[
\widehat h_\omega(\xi)=\frac1{1/2+i(\xi+\omega)}-\frac1{1/2+i\xi};
\quad |\widehat h_\omega(\xi)|=\sigma_w(\xi)
\]
up to translation/reflection of \(\xi\), which does not change its distribution.

**Step 3: leading continuous trace moments.** Write \(g=\widetilde h_\omega*h_\omega\), with \(\widetilde h(s)=\overline{h(-s)}\). This is exponentially decaying and \(\widehat g=|\widehat h_\omega|^2\). The exact positive-operator identity
\[
W_L^*W_L=P_LT_gP_L-E_L,
\quad E_L=P_LT_h^*(I-P_L)T_hP_L\ge0
\]
has uniformly bounded trace-class remainder, because causality gives
\[
\operatorname{tr}E_L\le\int_0^\infty s|h_\omega(s)|^2\,ds<\infty.
\]
All operator norms are uniformly bounded by \(\|h_\omega\|_1\). Telescoping positive integer powers and using trace-ideal inequalities therefore changes any fixed trace moment by \(O_{m,w}(1)\). For the compressed full convolution, direct cyclic kernel integration gives
\[
\operatorname{tr}(P_LT_gP_L)^m
=\int_{[0,L]^m}\prod_{r=1}^m g(u_r-u_{r+1})\,du_1\cdots du_m,
\quad u_{m+1}=u_1.
\]
Here \(g\) decays exponentially, so after dividing by \(L\), fixing \(u_1\), and translating the other variables, dominated convergence yields \((g^{*m})(0)=(2\pi)^{-1}\int\sigma_w^{2m}\). The same result for \(m=1\) follows directly from \(\operatorname{tr}(P_LT_gP_L)=Lg(0)\). Thus
\[
\operatorname{tr}(W_L^*W_L)^m=L\frac1{2\pi}\int_\mathbb R\sigma_w(\xi)^{2m}\,d\xi+o(L).
\]
Returning to the discretization, Step 1 gives a uniform \(\mathcal S_2\) error, while \(\|W_L\|_{\mathcal S_2}=O_w(\sqrt L)\) and both operator norms are bounded. Hence \(\|A_{N,\omega}^*A_{N,\omega}-B_N^*B_N\|_{\mathcal S_1}=O_w(\sqrt L)\), and telescoping powers transfers the leading moments to the discrete matrices. Because \(L/\log N\to1\), the claimed moment limits follow.

**Step 4: moments imply all positive-level counts.** Define positive finite measures
\[
\nu_N=\frac1{\log N}\sum_{j=1}^N s_j(A_{N,\omega})^2\,\delta_{s_j(A_{N,\omega})^2}.
\]
The first trace moment bounds their total masses, and the uniform operator bound places all their supports in a common compact interval. Step 3 yields convergence of all polynomial moments, hence weak convergence, to the image of \(\sigma_w(\xi)^2d\xi/(2\pi)\) weighted by \(\sigma_w(\xi)^2\). The limit has no atom at any fixed positive level, since \(\sigma_w\) is a nonconstant real-analytic rational function of \(\xi\). Integrating the bounded function \(\mathbf1_{x>t^2}/x\), whose only discontinuity relevant to the support is at \(x=t^2>0\), now gives
\[
\lim_{N\to\infty}\frac{M_{N,\omega}(t)}{\log N}
=\frac1{2\pi}\bigl|\{\xi:\sigma_w(\xi)>t\}\bigr|.
\]

**Step 5: two-band algebra.** Shift the Fourier variable to \(v=\xi+\omega/2\). The denominator squared of \(\sigma_w\) becomes
\[
\left(v^2+\frac{\omega^2+1}{4}\right)^2-\omega^2v^2
=v^4+\frac{1-\omega^2}{2}v^2+\frac{(1+\omega^2)^2}{16}.
\]
For \(0<t<2\), the strict inequality \(\sigma_w>t\) is equivalent to \(q_-(w,t)<v^2<q_+(w,t)\), with the quadratic roots displayed in the finding. Measuring this set gives the stated positive-part square-root formula. If \(w\le1\), the quartic is increasing as a function of \(v^2\), producing a single interval whenever nonempty. If \(w>1\), it has a double-well shape, with central height \(4w/(1+w^2)\) and two maxima of height \(2\); precisely the thresholds between those heights split the set into two components. Since \(\sigma_w\le2\), the density is zero for \(t\ge2\).

Finally, Plancherel and the explicit exponential kernel give
\[
\frac1{2\pi}\int_\mathbb R\sigma_w(\xi)^2\,d\xi
=\int_0^\infty e^{-s}|e^{-i\omega s}-1|^2\,ds
=\frac{2w^2}{1+w^2},
\]
proving the second-moment coefficient independently of the quartic integration.

## Verification
The accompanying `verify_spectrum.py` checks the closed-form threshold density against direct Fourier grid counting, tests the symmetry under sign reversal of the frequency, verifies the critical two-band threshold, and compares direct finite-matrix Hilbert–Schmidt sums with the stated logarithmic coefficient. Numerical discretization is not used as a proof of the infinite-dimensional trace or counting limit; those follow from the explicit Hilbert–Schmidt discretization estimate and the kernel trace-moment argument above.

## Relationship to prior work
Classical treatments of Cesàro operators, including Brown–Halmos–Shields and Arvanitidis–Siskakis, give foundational operator norms and spectral information but not the finite-section oscillatory commutator counting law. Bellavita–Stylogiannis's 2026 discrete Mellin calculus identifies a broad sampled-ratio calculus modulo compact or Hilbert–Schmidt error, including Mellin-multiplier norm information; that work is acknowledged and no essential-norm or multiplier-identity novelty is asserted here. Classical continuous Wiener–Hopf/Toeplitz singular-value asymptotics, including Widom's work, underlie the moment principle and are not claimed as new. The particular discrete commutator, uniformly bounded Hilbert–Schmidt transfer to logarithmic convolution, explicit normalized threshold counts, and frequency-dependent one-band/two-band classification are the present assertions.

## Limitations
The result is at fixed positive thresholds and frequencies, not at \(t=t_N\downarrow0\), not at growing frequencies, and not a uniform high-rank eigenvalue asymptotic. It does not determine individual singular values or spectral eigenvalues of the nonnormal commutator, nor does it establish a second-order counting error. A general finite-section asymptotic theorem could imply the moment law after a nontrivial verification of its hypotheses; equivalent historical special-case treatments of the exact oscillatory Cesàro matrices remain a bibliographic risk. Independent checking of originality and proof has not been performed.

## References
1. A. Brown, P. R. Halmos and A. L. Shields, *Cesàro operators*, Acta Sci. Math. (Szeged) 26 (1965), 125–137, https://acta.bibl.u-szeged.hu/14062/1/math_026_fasc_001_002_125-137.pdf.
2. A. G. Arvanitidis and A. G. Siskakis, *Cesaro operators on the Hardy spaces of the half-plane*, arXiv:1006.1520v1, first publicly submitted 2010-06-08; DOI:10.4153/CMB-2011-153-7.
3. C. Bellavita and G. Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453v1, 2026-09-08.
4. H. Widom, *On the Singular Values of Toeplitz Matrices*, Z. Anal. Anwend. 8 (1989), 221–229, DOI:10.4171/ZAA/350.
5. A. Rogozhin, *The Singular Value Behavior of the Finite Sections of Block Toeplitz Operators*, SIAM J. Matrix Anal. Appl. (2006), DOI:10.1137/S0895479804441973.
