# One extra intensity sharply repairs every even-dimensional real Gabor phase-retrieval obstruction

## Finding
For any even integer \(N=2m\ge2\) and \(0<r<1\), define the full-support real cyclic window \(g_j=r^j\) for \(0\le j<N\). Take every cyclic short-time Fourier intensity \(|\langle x,M^bT^ag\rangle|^2\) for \(a,b\in\mathbb Z_N\). This family fails to retrieve all complex vectors up to global phase; its Hermitian lifting kernel is precisely
\[
\left\{i\sum_{j=0}^{m-1}t_j(E_{j,j+m}-E_{j+m,j}):t_j\in\mathbb R\right\}.
\]
It has real dimension \(m\), and the projectors have complex-linear operator-span rank \(N^2-m\).

Augment the entire family by **one** further intensity \(|\langle x,w\rangle|^2\), with any fixed \(w\in\mathbb C^N\). The augmented intensities determine **every** \(x\in\mathbb C^N\) up to one unimodular scalar, including signals with zero coordinates, **if and only if**
\[
\operatorname{Im}(\overline{w_j}w_{j+m})\ne0\qquad(0\le j<m).
\]
For instance, \(w_j=1\) for \(0\le j<m\) and \(w_{j+m}=i\) for \(0\le j<m\) works for every even \(N\). Exactly one extra non-Gabor intensity is minimal for this window. When \(N\ge4\), the augmented projectors span only \(N^2-m+1<N^2\) complex matrix dimensions; thus the sharp nonlinear phase-retrieval completion is not informationally complete for arbitrary matrices. For odd \(N\), the same geometric window's unaugmented Gabor projectors already span every matrix.

## Assumptions and scope
Work over \(\mathbb C^N\) with the standard Hermitian inner product, standard basis \(e_j\), and matrix units \(E_{jk}=e_je_k^*\). Let \(\omega=e^{2\pi i/N}\), \((Tx)_j=x_{j-1\pmod N}\), and \((Mx)_j=\omega^jx_j\). The full indexed Gabor intensity data are \(\bigl(|\langle x,M^bT^ag\rangle|^2\bigr)_{a,b\in\mathbb Z_N}\). Vectors are identified only under multiplication by a complex scalar of modulus one. No assumption of nonzero input coordinates is imposed. The window is unnormalized; scaling it by a nonzero scalar does not change injectivity or operator-span rank.

## Proof
**Ambiguity zero set.** For \(\ell,k\in\{0,\ldots,N-1\}\), consider
\[
A_g(\ell,k)=\sum_{j=0}^{N-1}g_jg_{j-\ell\pmod N}\omega^{kj}.
\]
Partition at \(j=\ell\). The two resulting geometric sums yield, for each \(0\le\ell<N\),
\[
A_g(\ell,k)=\frac{r^{-\ell}(1-r^N)\bigl(r^{2\ell}\omega^{k\ell}+r^N\bigr)}{1-r^2\omega^k}.
\]
The denominator cannot vanish for \(0<r<1\). Equal magnitudes in the numerator's parenthesis are necessary for cancellation, forcing \(2\ell=N\); the phase then must be \(\omega^{k\ell}=-1\). Hence there are no zeros when \(N\) is odd, and when \(N=2m\) the exact zero set is \(\{(m,k):k\text{ odd}\}\), containing \(m\) points.

**Complete matrix kernel.** Finite Weyl operators \(M^kT^\ell\) give an orthogonal basis of the complex matrix space under the Hilbert–Schmidt pairing. The Fourier diagonalization of the full Gabor-projector analysis map shows that its kernel is exactly the span of Weyl operators corresponding to the zeros of \(A_g\) (the eigenvalues of its Gram matrix are \(N|A_g(\ell,k)|^2\), with normalization matching the unnormalized window). Consequently, in even order the complex matrix kernel has dimension \(m\) and consists of operators with potentially nonzero entries only between antipodal pairs \(j,j+m\), and the entries in opposite directions have opposite signs. Explicitly, the characters \(\omega^{kj}\) for odd \(k\), restricted to \(0\le j<m\), are a full Fourier basis of the \(m\) possible antipodal coefficients. Restricting this complex kernel to Hermitian matrices gives exactly
\[
\ker_{\mathrm{Herm}}\mathcal L_g=\bigoplus_{j=0}^{m-1}\mathbb R\,i(E_{j,j+m}-E_{j+m,j}).
\]
Indeed each such block is Hermitian and traceless. A combination with \(s\) nonzero real block coefficients has rank exactly \(2s\), since the antipodal two-dimensional coordinate planes are disjoint.

**The added probe.** Equality of intensity data for two vectors \(x,y\) means that \(H=xx^*-yy^*\) belongs to the Hermitian kernel. If \(x\) and \(y\) are not equal up to phase, \(H\ne0\) and \(\operatorname{rank}H\le2\). By the direct-block rank formula, \(H\) must be a nonzero scalar multiple of exactly one block \(i(E_{j,j+m}-E_{j+m,j})\). The extra intensity difference equals \(\operatorname{Tr}(Hww^*)=w^*Hw\), a nonzero real multiple of \(\operatorname{Im}(\overline{w_j}w_{j+m})\). Thus the displayed inequalities rule out every nontrivial ambiguity.

Conversely, if \(\operatorname{Im}(\overline{w_j}w_{j+m})=0\) for some \(j\), the corresponding traceless Hermitian block is invisible to all original intensities and to the extra intensity. Its eigenvalues are one positive and one negative number of the same magnitude, so its spectral decomposition writes it as \(xx^*-yy^*\) for suitable nonzero vectors \(x,y\) that are not unimodular multiples. This constructs a global phase-retrieval failure. Thus the criterion is necessary and sufficient.

**Minimality and odd order.** The even-order original has a nonzero rank-two Hermitian kernel block, so no additional count of zero measurements can suffice; the exhibited single probe suffices. For odd order, the ambiguity sum above has no zeros at all, so the Gabor projectors already span the full matrix space.

## Verification
The accompanying standalone script `verify.py` constructs all Gabor rank-one projectors and verifies their numerical linear ranks for \(2\le N\le12\), with \(r=1/2\). For each even order it confirms the predicted \(N^2-N/2\) rank, the single-probe rank increment, and explicit pairs of signals with identical original intensities but different probe intensities. Its recorded output is `verify_output.txt`. These are finite numerical consistency checks; the proof for every order is the preceding exact geometric-sum, Fourier-basis, and rank argument.

## Relationship to prior work
Goldberger, Kang, and Okoudjou's Gabor POVM analysis gives the Weyl-ambiguity diagonalization and operator-span rank framework used here. Bartusel establishes that even-dimensional real windows cannot yield universal Gabor phase retrieval. Those results do not state the necessary-and-sufficient condition for **one additional arbitrary intensity probe** to repair the failure, nor the sharp separation between rank-deficient linear tomography and universal nonlinear phase retrieval obtained for this explicit geometric full-support family. Existing Gabor-window rank classifications and limited-support phase-retrieval results address different measurement families or do not characterize minimal one-probe completion. This comparison concerns scientific implications, not title matching.

## Limitations
The sharp augmentation theorem concerns the specified geometric real window and full Gabor measurement family, not every real Gabor window; for the latter only the previously known even-order obstruction is used. The theorem proves exact noiseless injectivity, not a stability constant, optimal robustness, or injectivity after erasing some Gabor samples. For \(N\ge4\), one-probe augmentation is **not** informationally complete for arbitrary Hermitian matrices. The novelty assessment is best-knowledge and not an independent literature certification; an older equivalent formulation under phase-retrieval frame-completion terminology remains a risk.

## References
1. D. Goldberger, Y. Kang, and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1, 2021-06-02, https://arxiv.org/abs/2106.01509 .
2. D. Bartusel, *Injectivity conditions for STFT phase retrieval on finite cyclic groups*, arXiv:2206.06729v1, 2022-06-14, https://arxiv.org/abs/2206.06729 .
