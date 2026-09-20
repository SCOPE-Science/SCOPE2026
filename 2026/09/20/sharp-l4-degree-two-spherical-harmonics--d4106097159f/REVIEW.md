# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Degree-two real spherical harmonics are exactly restrictions of traceless real symmetric quadratic forms \(Y_A(\omega)=\omega^TA\omega\). The second and fourth spherical moments follow exactly from the corresponding centered Gaussian quadratic-form moments after dividing by the independent radial moments. This gives the invariant identity
\[
\frac{\|Y_A\|_4^4}{\|Y_A\|_2^4}
=
\frac{3n(n+2)}{(n+4)(n+6)}
\left(1+4\frac{\operatorname{tr}(A^4)}{\operatorname{tr}(A^2)^2}\right).
\]
The remaining optimization is the finite-dimensional problem of maximizing \(\sum\lambda_i^4\) subject to \(\sum\lambda_i=0\) and \(\sum\lambda_i^2=1\). The Lagrange equations force at most three distinct eigenvalues. A second-variation test on repeated eigenvalues rules out a three-value global maximizer except for a stationary configuration with quotient \(1/2\); the two-value configurations reduce to an explicit multiplicity formula whose maximum occurs at multiplicities \(1\) and \(n-1\). The exceptional dimensions \(n=2,3\) are checked separately, and in both the fourth-power quotient is identically \(1/2\).

For complex harmonics, phase averaging of \(H_\theta=\operatorname{Re}(e^{-i\theta}Y)\) converts the complex fourth norm to an average of real fourth norms. An exact calculation of the averaged squared real \(L^2\) norms, followed by Cauchy–Schwarz, gives the same sharp constant. Equality in that final Cauchy–Schwarz step forces the real and imaginary parts to be linearly dependent, so the complex equality cases are exactly constant-phase copies of the real ones.

Adversarial checks included the normalization of surface measure, the Gaussian radial factors, the \(n=2\) and \(n=3\) degeneracies, the equality conditions in the matrix optimization and complex phase reduction, and the conversion to ordinary surface area on \(\mathbb S^2\). No mathematical gap was found.

## Originality

**PASS, to the best of our knowledge.** Stanton and Weinstein's 1981 paper on the \(L^4\) norm of spherical harmonics was inspected as the main historical source. It establishes a highest-weight local maximum on \(\mathbb S^2\) and explicitly raises the question of the global maximizer. Lu's 1987 note simplifies that local Hessian argument. Sogge's 1986 theorem and the later work of Dai, Feng and Tikhonov determine sharp asymptotic orders in the harmonic degree rather than the exact finite degree-two constant and equality set proved here.

Searches for the exact degree-two problem, traceless-quadratic formulations, the displayed rational constant, matrix fourth-moment formulations, and synonymous reverse-Hölder statements did not locate a source stating the theorem or its complete equality classification. The current SCOPE repository was also checked by spherical-harmonic and degree-two terminology, with no overlapping record found.

The principal residual literature risk is Duoandikoetxea's 1987 paper on reverse Hölder inequalities for spherical harmonics. Its bibliographic record and relevance were identified, but its full theorem text was not inspected. An equivalent finite-dimensional statement could also exist in invariant theory, matrix-moment inequalities, or older quadratic-form literature under notation not indexed as a spherical-harmonic norm problem. Originality is therefore asserted only to the best of current knowledge.

## Value

**PASS.** The result gives an exact finite-degree answer where much of the surrounding literature is asymptotic, supplies a closed-form sharp constant in every dimension, and classifies all complex extremizers. On \(\mathbb S^2\), it completely resolves the degree-two case of the classical global \(L^4/L^2\) extremal question: every nonzero real degree-two harmonic has the same ratio, while a complex extremizer must have constant phase. The traceless-matrix reduction is also reusable for other low-degree spherical moment problems.

## Limitations

- The theorem is exact only for degree two and does not determine global extremizers for arbitrary harmonic degree.
- Duoandikoetxea's 1987 paper is a material residual originality risk because its full theorem text was not inspected.
- An equivalent statement may exist under invariant-theory, matrix-moment, or quadratic-form notation not found by the literature search.
- Independent audit has not been performed.

## Sources inspected

- R. J. Stanton and A. Weinstein, “On the L4 norm of spherical harmonics,” *Mathematical Proceedings of the Cambridge Philosophical Society* **89** (1981), 343–358. DOI https://doi.org/10.1017/S0305004100058229 .
- J.-H. Lu, “A note on a theorem of Stanton-Weinstein on the L4-norm of spherical harmonics,” *Mathematical Proceedings of the Cambridge Philosophical Society* **102** (1987), 561–563. DOI https://doi.org/10.1017/S0305004100067591 .
- C. D. Sogge, “Oscillatory integrals and spherical harmonics,” *Duke Mathematical Journal* **53** (1986), 43–65. DOI https://doi.org/10.1215/S0012-7094-86-05303-2 .
- J. Duoandikoetxea, “Reverse Hölder inequalities for spherical harmonics,” *Proceedings of the American Mathematical Society* **101** (1987), 487–491. DOI https://doi.org/10.2307/2046394 . Bibliographic record inspected; full theorem text was not.
- F. Dai, H. Feng and S. Tikhonov, “Reverse Hölder's inequality for spherical harmonics,” *Proceedings of the American Mathematical Society* **144** (2016), 1041–1051. DOI https://doi.org/10.1090/proc/12986 .
- L. De Carli, D. Gorbachev and S. Tikhonov, “Pitt and Boas inequalities for Fourier and Hankel transforms,” *Journal of Mathematical Analysis and Applications* **408** (2013), 762–774. DOI https://doi.org/10.1016/j.jmaa.2013.06.045 .
