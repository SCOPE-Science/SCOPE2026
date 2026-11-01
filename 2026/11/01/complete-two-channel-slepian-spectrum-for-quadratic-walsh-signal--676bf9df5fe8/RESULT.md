# Complete two-channel Slepian spectrum for quadratic Walsh signals on majority halfcubes

## Finding
Let \(d\ge3\) be odd. In the uniform Boolean cube \(\Omega_d=\{-1,1\}^d\), concentrate Walsh polynomials of degree at most two on the strict majority halfcube \(H_d=\{x:\sum_{i=1}^d x_i>0\}\). For the corresponding orthogonal compression \(C_d\), set
\[
a_d=2^{-d}\binom{d-1}{(d-1)/2},\qquad
s_d=a_d\sqrt{\frac{3d-1}{2}},\qquad
t_d=a_d\frac{d-1}{\sqrt{d-2}}.
\]
Its **complete spectrum**, including algebraic multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\frac12+s_d,\ \frac12-s_d&1\text{ each}\\
\frac12+t_d,\ \frac12-t_d&d-1\text{ each}\\
\frac12&\binom{d-1}{2}.
\end{array}
\]
Coincident levels are combined. When \(d=3\), \(s_d=t_d=1/2\) and the spectrum is \(1\) (multiplicity three), \(0\) (multiplicity three), and \(1/2\) (multiplicity one). For every odd \(d\ge5\), \(0<t_d<s_d<1/2\), and all five displayed levels are distinct. Thus every nonzero quadratic Walsh polynomial has positive energy in each majority halfcube, with **sharp** concentration bounds
\[
\left(\tfrac12-s_d\right)\|f\|_2^2
\le 2^{-d}\sum_{x\in H_d}|f(x)|^2
\le\left(\tfrac12+s_d\right)\|f\|_2^2,
\]
and the exact restriction-map condition number is
\[
\kappa_d=\sqrt{\frac{\frac12+s_d}{\frac12-s_d}}.
\]
All equality modes and the full spectrum are described in the proof. The two noncentral parameters strictly decrease with odd \(d\), and
\[
\lim_{d\to\infty,\ d\text{ odd}}s_d=\sqrt{\frac3{4\pi}},\qquad
\lim_{d\to\infty,\ d\text{ odd}}t_d=\frac1{\sqrt{2\pi}}.
\]

## Assumptions and scope
The inner product is \(\langle f,g\rangle=2^{-d}\sum_{x\in\Omega_d}f(x)\overline{g(x)}\). For \(S\subseteq[d]\), put \(\chi_S(x)=\prod_{i\in S}x_i\), with \(\chi_\varnothing=1\). Let \(V_2=\operatorname{span}\{\chi_S:|S|\le2\}\), of dimension \(1+d+\binom d2\), and \(P_2\) be orthogonal projection onto it. Then \(C_d=\left.P_2M_{\mathbf1_{H_d}}P_2\right|_{V_2}\). All eigenvalues, singular-value conditions, and equality statements use this normalization and individually labelled cube vertices. The set \(H_d\) is a strict majority halfcube only for odd \(d\); the even-dimensional tie layer is not included in this theorem.

## Proof
**1. Parity reduction and two Fourier coefficients.** Write \(\sigma(x)=\operatorname{sgn}(\sum_i x_i)\). For odd \(d\) there are no ties, \(\sigma(-x)=-\sigma(x)\), and \(\mathbf1_{H_d}=(1+\sigma)/2\). Split \(V_2=E\oplus O\), with \(E\) spanned by the degree-zero and degree-two Walsh characters, and \(O\) spanned by the degree-one characters. Since the Walsh characters are orthonormal, the matrix of \(C_d\) is
\[
C_d=\frac12 I+\begin{pmatrix}0&B\\B^*&0\end{pmatrix},
\]
where \(B\) records the Fourier coefficients of \(\mathbf1_{H_d}\) between opposite parities.

Permutation symmetry and oddness show that only the degree-one and degree-three coefficients contribute. Every degree-one coefficient equals
\[
\alpha=\mathbb E[x_1\mathbf1_{H_d}]=\frac12\Pr\left(\sum_{i=2}^d x_i=0\right)
=2^{-d}\binom{d-1}{(d-1)/2}=a_d.
\]
Every degree-three coefficient equals \(\beta=-\alpha/(d-2)\). Indeed, conditioning on \(Y=\sum_{i=4}^d x_i\), the signed sum of \(x_1x_2x_3\mathbf1_{\{Y+x_1+x_2+x_3>0\}}\), over the eight choices of the first three signs, vanishes except when \(Y\in\{-2,0,2\}\), where the sums are respectively \(1,-2,1\). Thus
\[
\beta=\frac{\Pr(Y=2)-\Pr(Y=0)}4
=-\frac{\alpha}{d-2},
\]
using the ratio of the adjacent central binomial coefficients. This calculation also holds at \(d=3\) by interpreting \(Y=0\) identically.

**2. Two singular channels.** Index the rows of \(B\) by \(\varnothing\) and two-element subsets, and its columns by individual indices. The first row is \(\alpha\mathbf1^{\mathsf T}\). For a pair \(\{i,j\}\), the entry in column \(k\) is \(\alpha\) if \(k\in\{i,j\}\), and \(\beta\) otherwise. Let \(R\) be the pair-versus-index incidence matrix and let \(J\) be the all-ones matrix of compatible size. Then
\[
B=\begin{pmatrix}\alpha\mathbf1^{\mathsf T}\\ (\alpha-\beta)R+\beta J\end{pmatrix},
\qquad R^*R=(d-2)I+\mathbf1\mathbf1^{\mathsf T}.
\]
The vector \(\mathbf1/\sqrt d\) and its orthogonal complement are invariant under \(B^*B\). Using \(\beta=-\alpha/(d-2)\), the squared singular value on the constant vector is
\[
\alpha^2\left[d+\frac{\binom d2}{d}\right]
=\alpha^2\frac{3d-1}{2}=s_d^2.
\]
For every vector \(v\in\mathbb C^d\) with \(\sum_i v_i=0\), the lower block acts as \((\alpha-\beta)Rv\), whence
\[
\|Bv\|_2^2=(\alpha-\beta)^2(d-2)\|v\|_2^2
=\alpha^2\frac{(d-1)^2}{d-2}\|v\|_2^2=t_d^2\|v\|_2^2.
\]
Because \(\alpha>0\), \(B\) has full column rank \(d\). The parity-off-diagonal matrix has eigenvalues \(\pm s_d\) once each, \(\pm t_d\) each \(d-1\) times, and zero \(\dim E-\dim O=(1+\binom d2)-d=\binom{d-1}{2}\) times. Adding \(I/2\) gives the asserted spectrum.

**3. Explicit eigenfunctions and sharpness.** Put
\[
o=\frac1{\sqrt d}\sum_i x_i,\qquad
e=\frac{\sqrt d+d^{-1/2}\sum_{i<j}x_ix_j}{\sqrt{(3d-1)/2}}.
\]
These are orthonormal and obey \(Bo=s_de\). Therefore \((e\pm o)/\sqrt2\) have concentrations \(1/2\pm s_d\). Given any \(v\in\mathbb C^d\) with \(\sum_i v_i=0\) and \(\sum_i|v_i|^2=1\), put
\[
o_v=\sum_i v_ix_i,\qquad e_v=\frac1{\sqrt{d-2}}\sum_{i<j}(v_i+v_j)x_ix_j.
\]
Then \(Bo_v=t_de_v\) and \((e_v\pm o_v)/\sqrt2\) are unit eigenfunctions of concentrations \(1/2\pm t_d\). The remaining half-energy eigenfunctions are exactly those even quadratic Walsh polynomials orthogonal to \(e\) and to all the \(e_v\); this is the full kernel of \(B^*\). The simple top/bottom levels for \(d\ge5\) make the displayed \(e\pm o\) the unique sharp extremizing lines.

**4. Strict ordering and limits.** Direct simplification gives
\[
s_d^2-t_d^2=\frac{\alpha^2d(d-3)}{2(d-2)},
\qquad\frac{s_{d+2}^2}{s_d^2}=\frac{d^2(3d+5)}{(d+1)^2(3d-1)}<1,
\qquad \frac{t_{d+2}^2}{t_d^2}=\frac{d-2}{d}<1.
\]
The middle strict inequality is equivalent to \((d+1)^2(3d-1)-d^2(3d+5)=d-1>0\). Since \(s_3=t_3=1/2\), it follows that \(0<t_d<s_d<1/2\) for odd \(d\ge5\). The resulting strict positivity and sharp condition number follow from the spectral theorem. Finally the central binomial asymptotic gives \(a_d\sqrt d\to1/\sqrt{2\pi}\), yielding the two asserted limits.

## Verification
The self-contained standard-library program `verify.py` constructs the complete Walsh concentration Gram matrices **exactly** for odd dimensions \(d=3,5,7,9,11,13\), checks all entries against the two majority coefficients, and tests every matrix entry of the proposed two-channel singular-value decomposition without floating-point rounding. It checks the dimension-ratio identities through \(d=9999\). Run `python3 verify.py`; the observed output was `VERIFY_OK dimensions=3,5,7,9,11,13 exact_gram_entries=16215 exact_distinct_walsh_moments=2049 dimension_ratios=4999`. The infinitely many dimensions, strict inequalities, and extremizers follow from the proof, not from finite enumeration.

## Relationship to prior work
Hogan and Lakey [1] introduced Walsh-bandlimited Boolean-cube Slepian concentration on Hamming balls, established general rank properties, and numerically investigated eigenvectors. Hogan and Lakey [2] supplied further invariant-block eigenspace reductions for the Hamming-ball setting. These established constructions and qualitative rank properties are prior results, not new claims here. The present explicit two-singular-channel calculation supplies a closed formula for **all** eigenvalues and multiplicities, all sharp concentration modes and the dimension dependence at degree two on the strict majority halfcube. The first-Walsh-band exact Hamming-ball spectrum [3] covers bandwidth one, not two. The all-band homogeneous halfspace half-energy theorem [4] already gives the central multiplicity and complementary spectral pairing as a special case, but not these off-center eigenvalues or sharp concentration constants. The quadratic-band single-shell classification [5] addresses one fixed-weight layer rather than this halfcube union of layers; its eigenvalues cannot be equated with the present majority-compression eigenvalues. No inspected source directly states the two-channel formula or its sharp extremizers. Broader association-scheme reductions could potentially imply the explicit result after nontrivial specialization; historical priority remains provisional.

## Limitations
The claim is restricted to odd cube dimensions, the uniform cube, homogeneous strict-majority localization, and Walsh bandwidth at most two. No even-dimensional tie-layer formula, larger-band classification, robustness under noisy samples, or minimal sample-count theorem is asserted. At \(d=3\), the restriction is not injective and the explicit zero eigenspace must not be mistaken for a strictly positive lower bound. The theorem establishes exact deterministic energy bounds; it does not claim that its formulas are independent of all prior implicit block-diagonalization methods.

## References
[1] J. A. Hogan and J. D. Lakey, *An Analogue of Slepian Vectors on Boolean Hypercubes*, Journal of Fourier Analysis and Applications **25** (2019), 2004–2020, doi:10.1007/s00041-018-09654-w; published online 20 November 2018. Full text inspected, including its definitions, rank criterion, spectral discussion, and numerical tables.

[2] J. A. Hogan and J. D. Lakey, *Spatio-spectral limiting on hypercubes: eigenspaces*, arXiv:1812.08905v1, first posted 21 December 2018; full text inspected for invariant-block reduction and eigenspace results.

[3] *Exact first-Walsh-band concentration spectra on Boolean Hamming balls*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-first-walsh-band-concentration-spectra-on-boolean-hamming--a2f5ddac5a0f .

[4] *Half-energy spectral rigidity for Walsh concentration on homogeneous halfspaces*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-half-energy-spectral-rigidity-for-walsh-concentration-on-homogen--6fe897560132 .

[5] *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-square-dimension-spectral-resonances-for-quadratic-band-walsh-co--7e1319aedf95 .
