# Two-scale spectral rigidity of the Drury–Arveson semi-hyponormality defect

## Finding

For every integer \(d\ge 2\), let \(S=(S_1,\ldots,S_d)\) be the coordinate-multiplier tuple on the Drury–Arveson space \(H_d^2\). Form the bounded positive operator matrices on \((H_d^2)^d\)
\[
L=(S_j^*S_i)_{1\le i,j\le d},\qquad
R=(S_iS_j^*)_{1\le i,j\le d},\qquad
D=L^{1/2}-R^{1/2}.
\]
Set \(h_n=\binom{n+d-1}{d-1}\), and \(h_{-1}=0\). The degree-\(n\) restriction of \(D\) has precisely the following real eigenvalues, with algebraic (equivalently geometric) multiplicity:

* \(c_n=(n+1)^{-1/2}>0\), of multiplicity \(d h_n-h_{n-1}\), for every \(n\ge0\);
* \(\delta_{n,d}=\sqrt{\frac{n+d}{n+1}}-\sqrt{\frac{n+d-1}{n}}<0\), of multiplicity \(h_{n-1}\), for every \(n\ge1\).

There are no other degree-block eigenvalues. Thus \(D\) is compact and injective, with infinitely many positive and infinitely many negative eigenvalues, and its full spectrum is the closure of the displayed eigenvalues (including \(0\)). The eigenvalues are strictly separated by sign, and each of the two absolute-value sequences decreases as the degree increases.

Let \(D_+\) and \(D_-\) denote the positive and negative parts of \(D\), so \(D=D_+-D_-\), and let \(s_k\) be the nonincreasing singular values counting multiplicities. Then
\[
\lim_{k\to\infty}k^{1/(2d)}s_k(D_+)
=\left(\frac{d-1}{d!}\right)^{1/(2d)},
\qquad
\lim_{k\to\infty}k^{2/d}s_k(D_-)
=\frac{d-1}{2}(d!)^{-2/d}.
\]
Consequently, for every real \(p>0\),
\[
D_+\in\mathcal S_p\iff p>2d,\qquad
D_-\in\mathcal S_p\iff p>d/2,\qquad
D\in\mathcal S_p\iff p>2d.
\]
At the respective critical exponents there are exact logarithmic coefficients:
\[
\lim_{K\to\infty}\frac{1}{\log K}\sum_{k=1}^{K}s_k(D_+)^{2d}
=\frac{d-1}{d!},
\qquad
\lim_{K\to\infty}\frac{1}{\log K}\sum_{k=1}^{K}s_k(D_-)^{d/2}
=\frac{((d-1)/2)^{d/2}}{d!}.
\]

## Assumptions and scope

The underlying complex reproducing-kernel Hilbert space has kernel \(K(z,w)=(1-\langle z,w\rangle)^{-1}\) on the open unit ball in \(\mathbb C^d\). Its normalized monomial basis is
\[
e_\alpha=\sqrt{\frac{|\alpha|!}{\alpha!}}z^\alpha,
\qquad \alpha\in\mathbb N_0^d.
\]
The degree spaces \(\mathcal H_n=\operatorname{span}\{e_\alpha:|\alpha|=n\}\) have dimensions \(h_n\). Every assertion concerns \(d\ge2\) fixed and \(n,k,K\) tending to infinity with \(d\) fixed. Powers and square roots of positive operators are taken by continuous functional calculus. The negative part means \(D_-=(|D|-D)/2\), hence is positive. Schatten \(\mathcal S_p\) includes quasi-ideals for \(0<p<1\). The trace-normalization in the last display is an ordinary logarithmically averaged singular-value sum, without any assertion of an independently defined singular trace.

## Proof

**Step 1: Homogeneous action and the Gram identity.** Define the usual bosonic creation and annihilation maps between degree spaces by
\[
a_i^*e_\alpha=\sqrt{\alpha_i+1}\,e_{\alpha+\mathbf e_i},
\qquad
a_ie_\alpha=\sqrt{\alpha_i}\,e_{\alpha-\mathbf e_i}.
\]
The normalized multiplier formulas are
\[
S_i|_{\mathcal H_n}=\frac{a_i^*}{\sqrt{n+1}},
\qquad
S_j^*|_{\mathcal H_n}=\frac{a_j}{\sqrt n}\quad(n\ge1).
\]
Both \(L\) and \(R\) preserve each finite-dimensional space \(\mathcal H_n^d\). On that space, for \(n\ge1\), the canonical commutation relations \(a_j a_i^*=a_i^*a_j+\delta_{ij}I\) give the identity
\[
L_n=\frac{I+nR_n}{n+1},\qquad
R_n=\frac1n(a_i^*a_j)_{i,j=1}^d.
\]
At degree zero, \(L_0=I_d\) and \(R_0=0\). In particular, the positive square root of \(L\) is well defined, even though the analogous operator-matrix positivity does not hold for every arbitrary commuting tuple.

**Step 2: Diagonalize the row Gramian.** For \(n\ge1\), define \(V_n:\mathcal H_{n-1}\to\mathcal H_n^d\) by
\[
V_nf=(a_1^*f,\ldots,a_d^*f).
\]
Then \(R_n=V_nV_n^*/n\). On the homogeneous degree-\(n-1\) space the number-operator identity reads
\[
V_n^*V_n=\sum_{i=1}^d a_i a_i^*=(n+d-1)I_{\mathcal H_{n-1}}.
\]
Hence \(V_n\) is injective, \(\operatorname{rank}R_n=h_{n-1}\), and the only eigenvalues of \(R_n\) are \((n+d-1)/n\) on \(\operatorname{ran}V_n\) and \(0\) on its orthogonal complement. The multiplicities are respectively \(h_{n-1}\) and \(d h_n-h_{n-1}\). Since \(L_n\) is an affine polynomial in \(R_n\), the two square roots have the same spectral projections, and their difference equals the two eigenvalues stated in the finding. For the nonzero range eigenvalue the square-root difference is
\[
\sqrt{\frac{1+(n+d-1)}{n+1}}-\sqrt{\frac{n+d-1}{n}}
=\delta_{n,d}.
\]
It is negative: writing \(a=d-1>0\), we have
\[
\delta_{n,d}=\sqrt{1+\frac{a}{n+1}}-\sqrt{1+\frac{a}{n}}<0.
\]
Both the positive branch \(c_n\) and the magnitude \(|\delta_{n,d}|\) decrease strictly with \(n\), the latter because \(x\mapsto\sqrt{1+a/x}\) is strictly decreasing and strictly convex for \(x>0\). Each branch tends to zero, so the orthogonal direct sum \(D=\bigoplus_{n\ge0}D_n\) is compact; each block is invertible, so \(D\) is injective.

**Step 3: Exact counting functions.** By the hockey-stick binomial identity, counting the positive and negative spectral values through degree \(n\) gives
\[
N_+(n)=\sum_{j=0}^n(dh_j-h_{j-1})
=d\binom{n+d}{d}-\binom{n+d-1}{d}
\sim\frac{d-1}{d!}n^d,
\]
\[
N_-(n)=\sum_{j=1}^n h_{j-1}
=\binom{n+d-1}{d}\sim\frac{1}{d!}n^d.
\]
The endpoints of a single degree level have relative separation \(1+O(n^{-1})\) in these cumulative counts. Therefore, using the monotonicity of the two branches,
\[
c_n\sim n^{-1/2},\qquad
|\delta_{n,d}|\sim\frac{d-1}{2n^2}
\]
converts directly into the two indexed limits in the finding, without making an incorrect identification of the degree index with the singular-value index.

**Step 4: Sharp ideals and logarithmic endpoints.** A positive compact diagonal operator belongs to \(\mathcal S_p\) precisely when the sum of its singular values to the power \(p\) converges, also for \(0<p<1\). The two indexed estimates from Step 3 therefore give the exact thresholds \(p>2d\) and \(p>d/2\); the positive branch controls \(D\). At each critical exponent, the corresponding singular-power sequence is asymptotic to the displayed positive constant divided by its rank index. Summation of a harmonic sequence gives the two logarithmic limits. This requires no finite-dimensional cutoff assumption and proves the assertions for all \(d\ge2\).

## Verification

A standalone finite-block checker, `spectral_check.py`, constructs the Drury–Arveson multipliers between successive homogeneous degrees without assuming the Gram identity. It forms the independent matrix blocks \(S_j^*S_i\) and \(S_iS_j^*\), computes matrix square roots by spectral decomposition, and compares the full spectra with the predicted eigenvalues and multiplicities. It checks several dimensions and degrees and separately checks combinatorial counts. Execute `python spectral_check.py` with Python 3 and NumPy. The checker passed 1,012 finite assertions. Exact infinite-dimensional conclusions, including compactness and the Schatten endpoints, are proved analytically above; the finite checker is not an exhaustive or independent validation.

As a normalization cross-check, \(d=2\), \(n=1\) gives eigenvalues \(2^{-1/2}\) and \(\sqrt{3/2}-\sqrt2\), whose product is approximately \(-0.133975\), agreeing with the negative determinant reported for the motivating paper's first homogeneous compression.

## Relationship to prior work

Curto and Yoon's *Semi-hyponormality of commuting pairs of Hilbert space operators* develops the matrix-root definition and proves in Theorem 3.18 that the two-variable Drury–Arveson pair is not semi-hyponormal by examining one degree-one two-dimensional compression. That theorem establishes nonpositivity but does not give the full spectrum, dimensions beyond two, a compactness assertion for the difference of roots, spectral multiplicities, separated positive/negative Schatten classes, or critical coefficients. The present result calculates each of these from a degreewise scalar-polynomial relation between the two matrix Gramians.

Arveson's work on \(p\)-summable commutators of \(d\)-shifts and the essential-normality literature address commutators such as \([S_i,S_j^*]\), not the distinct nonlinear operator \(L^{1/2}-R^{1/2}\). In particular, an \(\mathcal S_p\) estimate on those individual commutators cannot by itself imply the sharp asymmetric spectra here. Hartz and Shalit's 2025 survey records the coordinate-multiplier and symmetric-Fock framework; its accessible abstract does not provide the present defect-spectrum theorem. Published research-record and earlier-claim searches found no directly equivalent or stronger theorem under the tested descriptions.

## Limitations

The theorem concerns precisely the uncompressed, unweighted Drury–Arveson coordinate tuple, not arbitrary pure row contractions, quotients, other homogeneous modules, or arbitrary commuting tuples for which \(L\) may fail positivity. The stated source-first date is the exact verified arXiv first-version posting date, May 4, 2026; bibliographic records also identify an earlier 2025 journal publication whose exact first public day was not established in the accessible material. Accordingly, no claim is made that the arXiv date is the earliest dissemination of that article. Prior results under different terms may exist and require independent priority review. No external mathematical audit has been performed.

## References

1. R. E. Curto and J. Yoon, *Semi-hyponormality of commuting pairs of Hilbert space operators*, arXiv:2605.02197 (first arXiv version May 4, 2026), especially Definition 1.1 and Theorem 3.18. Earlier journal publication: *Bulletin des Sciences Mathématiques* 205 (2025), 103718, DOI: 10.1016/j.bulsci.2025.103718. Accessible primary full text: https://arxiv.org/html/2605.02197v2.
2. W. Arveson, *p-Summable commutators in dimension d*, *Journal of Operator Theory* 54 (2005), 101–117; arXiv:math/0308104. Bibliographic description: https://jot.theta.ro/jot/archive/2005-054-001/2005-054-001-006.html.
3. M. Hartz and O. M. Shalit, *Operator Theory and Function Theory in Drury-Arveson Space and Its Quotients*, online February 8, 2025, DOI: 10.1007/978-3-0348-0692-3_60-2.
4. M. Kennedy and O. M. Shalit, *Essential normality, essential norms and hyperrigidity*, *Journal of Functional Analysis* 268 (2015), 2990–3016, DOI: 10.1016/j.jfa.2015.03.014.
