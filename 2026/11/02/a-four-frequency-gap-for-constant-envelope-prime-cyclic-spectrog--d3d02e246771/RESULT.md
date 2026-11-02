# A four-frequency gap for constant-envelope prime-cyclic spectrograms

## Finding
Let \(p\ge5\) be an odd prime. If \(f,g:\mathbb Z_p\to\mathbb C\) each have a positive constant modulus, then their discrete short-time Fourier transform has a forbidden band of support cardinalities:
\[
\boxed{\left|\operatorname{supp}V_gf\right|=p\quad\text{or}\quad\left|\operatorname{supp}V_gf\right|\ge4p-3.}
\]
The first alternative holds exactly for **matched-curvature quadratic chirps**: with \(\omega=e^{2\pi i/p}\), there exist \(u,a,b\in\mathbb Z_p\) and nonzero complex constants \(A,B\) such that
\[
f(n)=A\omega^{(u/2)n^2+an},\qquad g(n)=B\omega^{(u/2)n^2+bn}\qquad(n\in\mathbb Z_p),
\]
where \(1/2\) means the multiplicative inverse of \(2\) in \(\mathbb Z_p\). More precisely, if no time row has one Fourier coefficient, all \(p\) rows have at least four, giving \(\left|\operatorname{supp}V_gf\right|\ge4p\); otherwise either all rows have one or precisely one has one and the rest have at least four.

The number \(4p-3\) is a **proved lower bound**, not an asserted attained second support level. No amplitude or approximate-support bound is claimed.

## Assumptions and scope
The underlying group is the prime cyclic group \(\mathbb Z_p\), equipped with counting measure. Both signals have full support and constant (possibly different) nonzero magnitudes: \(|f(n)|=\alpha>0\), \(|g(n)|=\beta>0\) for every \(n\). Define
\[
V_gf(j,k)=\frac1{\sqrt p}\sum_{n\in\mathbb Z_p}f(n)\overline{g(n-j)}\omega^{-kn},\qquad (j,k)\in\mathbb Z_p^2.
\]
This normalization does not influence the support. Indices, shifts and quadratic coefficients are all interpreted modulo \(p\). The claim covers arbitrary complex phases, not only a finite phase alphabet.

## Proof
**Lemma (prime-cyclic unimodular Fourier gap).** For prime \(p\ge5\), a function \(h:\mathbb Z_p\to\mathbb C\) of constant positive modulus has Fourier support of cardinality either \(1\) or at least \(4\). Cardinality \(1\) occurs precisely when \(h\) is a nonzero scalar multiple of a character.

To prove the lemma, let \(\widehat h(k)=\sum_n h(n)\omega^{-kn}\) and \(E=\operatorname{supp}\widehat h\). Constancy of \(|h|^2\), together with Fourier inversion, forces the frequency autocorrelations
\[
\tag{1}\sum_{k\in\mathbb Z_p}\widehat h(k+d)\overline{\widehat h(k)}=0\qquad(d\ne0).
\]
If \(E\) has two elements, choose their nonzero difference \(d\). Because \(p\) is odd, exactly one ordered pair of elements of \(E\) has difference \(d\), contradicting (1). If \(E\) has three elements, its six nonzero ordered differences occupy at least four distinct residues. Indeed, the difference set is symmetric under negation; if it contained only \(\{d,-d\}\), all three points would be pairwise adjacent by steps \(\pm d\), which is possible only if \(3d=0\); this contradicts \(p\ge5\). By pigeonhole, at least one nonzero difference occurs exactly once, again contradicting (1). Hence \(|E|\notin\{2,3\}\). Fourier inversion gives the one-frequency characterization. This proves the lemma.

For the STFT, put \(G(n)=\overline{g(n)}\) and \(h_j(n)=f(n)G(n-j)\). Each \(h_j\) has constant nonzero modulus, and its Fourier support cardinality \(t_j\) is the number of nonzero STFT entries in row \(j\). By the lemma \(t_j=1\) or \(t_j\ge4\), and
\[
\tag{2}\left|\operatorname{supp}V_gf\right|=\sum_{j\in\mathbb Z_p}t_j.
\]
If no row has \(t_j=1\), equation (2) gives at least \(4p\). Otherwise relabel translations to arrange \(h_0(n)=C\omega^{qn}\) for nonzero \(C\). Define \(r_j(n)=G(n-j)/G(n)\), a well-defined nonvanishing function. Since \(h_j=h_0r_j\), \(t_j\) is the Fourier support cardinality of \(r_j\). The identity
\[
\tag{3}r_{j+d}(n)=r_j(n)r_d(n-j)
\]
shows that \(H=\{j:r_j\text{ is a scalar character}\}\) is a subgroup: it contains \(0\), is closed under addition by (3), and under inverses because \(r_{-j}(n)=1/r_j(n+j)\). Prime cyclicity gives \(H=\{0\}\) or \(H=\mathbb Z_p\). In the first case exactly one time row has \(t_j=1\), while the remaining \(p-1\) rows have \(t_j\ge4\), giving \(1+4(p-1)=4p-3\). In the second case every row has one Fourier coefficient and the total is \(p\). This proves the support dichotomy.

Finally, in the \(p\)-coefficient case \(r_1(n)=c\omega^{un}\). Telescoping its product over all \(n\) yields \(c^p=1\), so \(c=\omega^v\) for some \(v\in\mathbb Z_p\). Iterating \(G(n-1)=c\omega^{un}G(n)\) gives
\[
G(n)=G(0)\omega^{-vn-u n(n+1)/2}.
\]
Thus \(g\) is a quadratic chirp. The relation \(f(n)G(n)=C\omega^{qn}\) shows that \(f\) has **the same quadratic coefficient** as \(g\), with possibly a different linear phase; absorbing linear terms gives the displayed matched-curvature form. Conversely, substituting two matched-curvature chirps shows that each \(h_j\) is a scalar character, so every row has one Fourier coefficient and the total is \(p\). The classification is complete.

## Verification
The proof is exact and applies to every prime \(p\ge5\). The attached, standalone Python standard-library checker `artifacts/verify.py` verifies the combinatorial singleton-difference lemma for all three-point subsets at several small primes, checks matched-curvature chirps and selected unmatched or phase-defect examples, and tests the claimed numerical support gap in fixed finite samples. This program supports reproducibility but **finite tests are not the proof** and do not establish attainability of \(4p-3\).

## Relationship to prior work
Nicola's 2022 preprint on equality cases for the finite cyclic short-time Fourier uncertainty principle classifies arbitrary-pair STFT minimizers of support size \(p\), including quadratic chirps. This result rederives their constant-envelope specialization but does not claim novelty for the characterization itself.

Krahmer–Pfander–Rashkov's finite-Gabor uncertainty arguments and the published result *A sharp support gap above the odd-prime short-time Fourier uncertainty minimum* cover unrestricted complex signals and establish only the dichotomy \(p\) versus at least \(2p\). That unrestricted statement does **not** imply the present \(4p-3\) bound under constant-magnitude restrictions. The key additional ingredient here is the Fourier autocorrelation obstruction to two- and three-term spectral support for unimodular rows, combined with the prime-order character-cocycle subgroup argument. By contrast, *Phase-only four-sparse uncertainty over prime cyclic groups* constrains the four **time** coefficients of a sparse signal and does not control an STFT of two full-support constant-envelope inputs. Related classifications of three-tap ambiguity functions also impose sparse rather than constant-envelope inputs.

## Limitations
Only odd primes \(p\ge5\) and exact nonzero constant-magnitude inputs are addressed. We do not prove that the lower bound \(4p-3\) is attained or characterize the first attainable support above \(p\). No assertion is made about composite-order groups, approximate sparsity, small nonzero coefficients, or reconstruction stability. Despite targeted equivalence and implication searches, an earlier equivalent formulation in the phase-code or periodic-correlation literature remains possible. Independent mathematical validation has not been performed.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1, public 29 April 2022; Journal of Functional Analysis 284 (2023), 109924, DOI 10.1016/j.jfa.2023.109924.
2. F. Krahmer, G. E. Pfander, P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, Applied and Computational Harmonic Analysis 25 (2008), 209–225, DOI 10.1016/j.acha.2007.09.008; arXiv:math/0611493.
3. *A sharp support gap above the odd-prime short-time Fourier uncertainty minimum*, published 11 October 2026, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-a-sharp-support-gap-above-the-odd-prime-short-time-fourier-uncer--c42ba46f36bb/RESULT.md.
4. *Phase-only four-sparse uncertainty over prime cyclic groups*, published 4 October 2026, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-phase-only-four-sparse-uncertainty-over-prime-cyclic-groups--def07c3297e4/RESULT.md.
