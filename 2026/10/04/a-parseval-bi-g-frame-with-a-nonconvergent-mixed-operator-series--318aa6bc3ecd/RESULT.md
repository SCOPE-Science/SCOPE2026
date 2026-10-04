# A Parseval bi-g-frame with a nonconvergent mixed operator series
## Finding
Under the literal bi-g-frame definition in arXiv:2308.02147, the scalar bi-g-frame inequality does not force the vector series used to define the mixed frame operator to converge in norm. There is a Parseval bi-g-frame on \(H=\ell^2(\mathbb N_0)\) such that, for every nonzero \(f\in H\),
\[
\sum_{j=1}^{\infty}\Gamma_j^*\Lambda_j f
\]
does not converge in norm. Consequently, the general well-definedness assertion for the bi-g-frame operator in Theorem 2.3 of that source is false as stated. If both constituent operator sequences are g-Bessel, the asserted operator and reconstruction formulas are well defined and the stated positivity and inverse bound follow.

## Assumptions and scope
Let \(H=\ell^2(\mathbb N_0)\), let \(S\) be the unilateral shift \(Se_n=e_{n+1}\), take \(J=\mathbb N=\{1,2,\ldots\}\), and put \(V_j=H\) for every \(j\). Define
\[
\Gamma_j=I_H\qquad(j\ge 1),
\]
and
\[
\Lambda_1=I_H+S,\qquad \Lambda_j=S^j-S^{j-1}\qquad(j\ge 2).
\]
Every \(\Lambda_j\) and \(\Gamma_j\) is a bounded operator from \(H\) to \(V_j\). No Bessel assumption on either constituent sequence is used in the source definition being tested.

The correction asserted here is only that simultaneous g-Bessel hypotheses are sufficient to restore the mixed-operator construction. No claim is made that they are the weakest possible hypotheses.

## Proof
For each integer \(N\ge 1\), telescoping gives
\[
\sum_{j=1}^{N}\Gamma_j^*\Lambda_j
=I_H+S^N.
\]
For \(f=(f_0,f_1,\ldots)\in\ell^2(\mathbb N_0)\),
\[
\left|\langle S^Nf,f\rangle\right|
\le
\|f\|_2\left(\sum_{m\ge N}|f_m|^2\right)^{1/2}
\longrightarrow 0.
\]
Therefore
\[
\sum_{j=1}^{\infty}\langle \Lambda_jf,\Gamma_jf\rangle
=
\lim_{N\to\infty}\langle (I_H+S^N)f,f\rangle
=
\|f\|_2^2.
\]
Thus the pair satisfies the displayed bi-g-frame inequality with equal lower and upper bounds \(C=D=1\); in the terminology of the source it is a Parseval bi-g-frame.

On the other hand, the partial sums of the vector series used for the mixed operator are
\[
\sum_{j=1}^{N}\Gamma_j^*\Lambda_j f
=f+S^Nf.
\]
The vectors \(S^Nf\) converge weakly to zero, so if \(f+S^Nf\) converged in norm, its norm limit would have to be \(f\). That would force \(\|S^Nf\|_2\to0\). But \(S\) is an isometry, hence \(\|S^Nf\|_2=\|f\|_2\) for every \(N\). For every nonzero \(f\), the series therefore fails to converge in norm.

Now assume instead that both \(\Lambda=\{\Lambda_j\}\) and \(\Gamma=\{\Gamma_j\}\) are g-Bessel sequences. Their analysis and synthesis operators are bounded, and for every \(f\), the coefficient vector \(T_\Lambda^*f=(\Lambda_jf)_j\) lies in \(\bigoplus_jV_j\). Finite coordinate truncations converge there in norm, so boundedness of \(T_\Gamma\) gives unconditional norm convergence of
\[
\sum_j\Gamma_j^*\Lambda_j f
=
T_\Gamma T_\Lambda^*f.
\]
Write \(S_{\Lambda,\Gamma}=T_\Gamma T_\Lambda^*\). If the bi-g-frame inequality holds with \(0<C\le D<\infty\), then
\[
C\|f\|^2\le \langle S_{\Lambda,\Gamma}f,f\rangle\le D\|f\|^2
\]
for every \(f\). The quadratic form is real, so on a complex Hilbert space the bounded operator \(S_{\Lambda,\Gamma}\) is self-adjoint; it is positive and satisfies \(S_{\Lambda,\Gamma}\ge C I_H\). Hence it is invertible and
\[
\|S_{\Lambda,\Gamma}^{-1}\|\le C^{-1}.
\]
Substituting the norm-convergent operator series then yields the standard reconstruction formulas.

## Verification
The counterexample is symbolic. The scalar series is evaluated exactly by telescoping plus an explicit tail estimate for \(\langle S^Nf,f\rangle\); the failure of strong convergence follows from the exact identity \(\|S^Nf\|_2=\|f\|_2\). No finite computation is used to infer an infinite-dimensional conclusion.

The source text was checked at its definition of a bi-g-frame, its definition of the mixed operator, Theorem 2.3 and the proof step asserting convergence of the operator series from the scalar inequality, and the subsequent reconstruction theorem. A later 2024 paper on bi-g-frame characterizations was also checked: it explicitly recalls that a bi-g-frame may have non-g-Bessel constituents, imports the general positive-invertible mixed operator assertion, and separately studies the safer class in which the constituents are g-Bessel sequences.

## Relationship to prior work
Ramezani's arXiv:2308.02147 introduces bi-g-frames through a scalar mixed quadratic inequality and then defines \(S_{\Lambda,\Gamma}f=\sum_j\Gamma_j^*\Lambda_jf\). Its Theorem 2.3 asserts that this operator is automatically well defined, bounded, positive and invertible. The proof passes from convergence of the scalar quadratic series to convergence of the vector series; the construction above shows that this implication fails.

Fu, Zhang and Tian later study characterizations and constructions of bi-g-frames. Their paper explicitly notes that bi-g-frames can have two non-g-Bessel constituent sequences, while several of their structural results impose g-Bessel or g-frame hypotheses. The counterexample isolates why such hypotheses are sufficient for the operator-theoretic construction.

The earlier biframe literature contains an analogous scalar mixed inequality and an operator construction. A 2025 correction to that literature addresses different statements; the sources inspected did not contain this unilateral-shift counterexample or the g-Bessel repair stated here for the bi-g-frame theorem.

## Limitations
The finding concerns the literal generality of the bi-g-frame definition and operator theorem in arXiv:2308.02147. It does not say that every result in that paper or later bi-g-frame work fails. Results that independently assume enough Bessel control or another hypothesis guaranteeing norm convergence may remain valid. The simultaneous g-Bessel condition supplied here is a clean sufficient repair, not a claimed minimal characterization of all admissible mixed pairs.

A residual literature risk remains that the same strong-versus-weak convergence obstruction has been noted in an unindexed erratum, thesis, lecture note, or informal communication.

## References
1. S. M. Ramezani, *Bi-g-frame and characterizations of bi-g-frame and Riesz basis*, arXiv:2308.02147, first public version 2023-08-04.
2. Y.-L. Fu, W. Zhang, Y. Tian, *On characterization and construction of bi-g-frames*, J. Pseudo-Differ. Oper. Appl. 15 (2024), article 31, DOI 10.1007/s11868-024-00597-z.
3. M. Firouzi Parizi, A. Alijani, M. Dehghan, *Biframes and some of their properties*, J. Inequal. Appl. (2022), DOI 10.1186/s13660-022-02844-7.
4. *Correction: Biframes and some of their properties*, J. Inequal. Appl. (2025), DOI 10.1186/s13660-025-03258-x.
