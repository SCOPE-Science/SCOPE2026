# Sharp norm distortion for a Möbius sub-Bergman model

## Finding
Let \(\mathcal E\) be a separable Hilbert space and let \(A=A^*\) satisfy \(0\le A\le aI\), where \(a=\|A\|<1\). Define \(B_A(z)=(zI-A)(I-zA)^{-1}\). For every \(\alpha\ge0\), with \(A^2_{-1,\mathcal E}=H^2_{\mathcal E}\) when \(\alpha=0\), the source kernel factorization identifies \(\mathcal A_\alpha(B_A)\) and \(A^2_{\alpha-1,\mathcal E}\) as the same set, and the identity map has the sharp two-sided norm comparison \[c(a)^{-1}\|f\|_{A^2_{\alpha-1,\mathcal E}}\le \|f\|_{\mathcal A_\alpha(B_A)}\le c(a)\|f\|_{A^2_{\alpha-1,\mathcal E}},\qquad c(a)=\sqrt{\frac{1+a}{1-a}}.\] Both factors \(c(a)\) are optimal. For the diagonal operator in Luo--Shen's nonrigidity example, \(a_n=\frac34-\frac1{n+1}\) and \(a=\frac34\), so the exact comparison constant is \(\sqrt7\).

The quantitative point is that the set equality in the Möbius model has an exact distortion depending only on the spectral radius parameter \(a=\|A\|\), not on the Bergman weight \(\alpha\) in the range \(\alpha\ge0\).

## Assumptions and scope
Let \(\mathcal E\) be a separable Hilbert space. Let \(A=A^*\) be positive with \(0\le A\le aI\) and \(a=\|A\|<1\). Put
\[
B_A(z)=(zI-A)(I-zA)^{-1},\qquad
D_A=(I-A^2)^{1/2},\qquad
L_A(z)=D_A(I-zA)^{-1}.
\]
For \(\alpha>0\), \(A^2_{\alpha-1,\mathcal E}\) is the usual vector-valued weighted Bergman space. For \(\alpha=0\), use the standard convention \(A^2_{-1,\mathcal E}=H^2_{\mathcal E}\).

The claim concerns \(\mathcal A_\alpha(B_A)\), not \(\mathcal A_\alpha(B_A^*)\), and only the range \(\alpha\ge0\).

## Proof
Luo--Shen compute for this Möbius model
\[
I-B_A(z)B_A(w)^*
=(1-z\overline w)(I-zA)^{-1}D_A^2(I-\overline w A)^{-1}.
\]
Hence the reproducing kernel of \(\mathcal A_\alpha(B_A)\) is
\[
F_\alpha^{B_A}(z,w)
=L_A(z)\frac{I_{\mathcal E}}{(1-z\overline w)^{\alpha+1}}L_A(w)^*.
\]
A kernel of the form \(L(z)K(z,w)L(w)^*\), with \(L\) pointwise invertible, makes multiplication by \(L\) a unitary map from the RKHS of \(K\) onto the RKHS of the transformed kernel. Therefore
\[
\|f\|_{\mathcal A_\alpha(B_A)}
=\|L_A^{-1}f\|_{A^2_{\alpha-1,\mathcal E}}.
\]

For \(\alpha>0\), the multiplier norm of a bounded analytic operator-valued function on \(A^2_{\alpha-1,\mathcal E}\) equals its \(H^\infty\) norm: the integral model gives the upper bound, while normalized reproducing kernels give the reverse inequality. The same statement holds for \(\alpha=0\) on \(H^2_{\mathcal E}\).

By the spectral theorem, for \(\lambda\in\sigma(A)\subset[0,a]\),
\[
L_A(z)\quad\text{acts spectrally by}\quad
\ell_\lambda(z)=\frac{\sqrt{1-\lambda^2}}{1-z\lambda}.
\]
Thus
\[
\|M_{L_A}\|
=\sup_{|z|<1,\,\lambda\in\sigma(A)}
\frac{\sqrt{1-\lambda^2}}{|1-z\lambda|}
=\sqrt{\frac{1+a}{1-a}}.
\]
Indeed, for fixed \(\lambda\), the supremum is approached as \(z\to1\), and \(a\in\sigma(A)\) because \(A\) is self-adjoint and \(\|A\|=a\). Similarly,
\[
L_A(z)^{-1}=(I-zA)D_A^{-1}
\]
acts spectrally by
\[
\ell_\lambda(z)^{-1}=\frac{1-z\lambda}{\sqrt{1-\lambda^2}},
\]
so
\[
\|M_{L_A^{-1}}\|
=\sup_{|z|<1,\,\lambda\in\sigma(A)}
\frac{|1-z\lambda|}{\sqrt{1-\lambda^2}}
=\sqrt{\frac{1+a}{1-a}},
\]
with the supremum approached as \(z\to-1\) and \(\lambda\to a\) through the spectrum.

Since the identity \(A^2_{\alpha-1,\mathcal E}\to\mathcal A_\alpha(B_A)\) is \(M_{L_A^{-1}}\) after the unitary identification, while the reverse identity is \(M_{L_A}\), the two displayed operator norms are exactly the best constants. For Luo--Shen's diagonal example, \(a=\frac34\), hence
\[
c(a)^2=\frac{1+\frac34}{1-\frac34}=7,
\qquad c(a)=\sqrt7.
\]

## Verification
The proof is symbolic. The kernel factorization is taken from the focal paper's explicit construction. The remaining steps were independently reconstructed from RKHS kernel transport, vector-valued Hardy/Bergman multiplier norms, and the spectral theorem. The endpoint \(\alpha=0\) was checked separately using \(H^2_{\mathcal E}\). No finite numerical experiment is used as evidence for the infinite-dimensional statement.

## Relationship to prior work
Luo--Shen prove equality as sets for their infinite-dimensional Möbius construction but do not state the sharp norm-equivalence constant. Gu--Luo--Ma establish the vector-valued sub-Bergman framework and finite Blaschke--Potapov rigidity phenomena. In the scalar theory, Cheng Chu records a related factor \(\sqrt{(1+|b(0)|)/(1-|b(0)|)}\) in a one-sided RKHS comparison; that scalar estimate does not imply the present operator-valued exact two-sided identity distortion, nor its \(\sqrt7\) specialization for the source's infinite-dimensional example.

## Limitations
The exact multiplier-norm argument is asserted only for \(\alpha\ge0\). No statement is made for \(-1<\alpha<0\), where the shifted RKHS \(A^2_{\alpha-1,\mathcal E}\) is not covered by the same weighted-area multiplier argument. No sharp constant is claimed for \(\mathcal A_\alpha(B_A^*)\). The result does not classify all symbols with a given distortion, and it does not assert that \(\sqrt7\) is universal among nonrigid examples.

## References
1. S. Luo and J. Shen, *Vector-Valued Sub-Bergman Spaces: Range Inclusions and Nonrigidity*, arXiv:2609.34694v1 (2026).
2. C. Gu, S. Luo, and P. Ma, *Vector-valued sub-Bergman spaces on the unit disk*, Mathematische Zeitschrift 312 (2026), Article 1, DOI 10.1007/s00209-025-03888-3.
3. C. Chu, *Hilbert Spaces Contractively Contained in Weighted Bergman Spaces on the Unit Disk*, arXiv:1807.08366; Journal of Mathematical Analysis and Applications 472 (2019), 386--394.
