# Exact Pell-resonant limsup of the third Cairo high-energy band family
## Finding
For the all-\(R\) Cairo quantum graph of Baradaran–Exner with \(a,\ell_3,\ell_4>0\), let \(\Delta E_{3,n}\) denote the family-(iii) high-energy band width centered at \(k_{3,n}=(\sqrt3+1)n\pi/(2a)\) in Section 3.2 of arXiv:2312.13827v1. Then
\[\limsup_{\substack{n\to\infty\\2\mid n}}\Delta E_{3,n}=\frac{32\sqrt3}{\pi^2\ell_3^2},\qquad\limsup_{\substack{n\to\infty\\2\nmid n}}\Delta E_{3,n}=\frac{16\sqrt3}{\pi^2\ell_3^2}.\]
Both limsups are attained along the Pell denominators \(n_r\) defined by \(m_r+n_r\sqrt3=(2+\sqrt3)^r\), equivalently \(m_r^2-3n_r^2=1\): even \(r\) gives even \(n_r\), and odd \(r\) gives odd \(n_r\). Thus the source's bounded but nonconstant family-(iii) widths have exact positive parity-dependent resonant spikes at arbitrarily high energy.

## Assumptions and scope
The statement concerns the all-\(R\) Cairo lattice model and the third high-energy resonance family analyzed in Section 3.2(iii) of Baradaran–Exner. It uses the source's proved asymptotic band-width formulas
\[
\Delta E_{3,n}=\frac{16}{n\pi\ell_3^2}\left|\csc(\sqrt3 n\pi)\right|+O(n^{-2}),\qquad 2\mid n,
\]
and
\[
\Delta E_{3,n}=\frac{8}{n\pi\ell_3^2}\left|\csc(\sqrt3 n\pi)\right|+O(n^{-2}),\qquad 2\nmid n.
\]
No claim is made about the other two high-energy families, finite-energy bands, or a pointwise limit of \(\Delta E_{3,n}\).

## Proof
Put \(d_n=\operatorname{dist}(\sqrt3 n,\mathbb Z)\), and let \(m_n\) be a nearest integer. Suppose first that a subsequence has bounded \(n d_n\). Then \(d_n\to0\), hence \(m_n/n\to\sqrt3\). Since \(m_n^2-3n^2\) is a nonzero integer,
\[
n d_n=n|\sqrt3 n-m_n|=
\frac{n|m_n^2-3n^2|}{\sqrt3 n+m_n}
\ge \frac1{\sqrt3+m_n/n}.
\]
Therefore every bounded subsequential limit of \(n d_n\) is at least \(1/(2\sqrt3)\); an unbounded subsequence cannot lower the liminf. Since \(\sin(\pi d_n)\sim\pi d_n\) whenever \(d_n\to0\),
\[
\liminf_{n\to\infty}n|\sin(\pi\sqrt3 n)|\ge\frac{\pi}{2\sqrt3}.
\]

For sharpness, define positive integers \(m_r,n_r\) by
\[
m_r+n_r\sqrt3=(2+\sqrt3)^r.
\]
Then \(m_r^2-3n_r^2=1\), so
\[
|\sqrt3 n_r-m_r|=\frac1{\sqrt3 n_r+m_r},
\qquad
n_r|\sqrt3 n_r-m_r|\longrightarrow\frac1{2\sqrt3}.
\]
The recurrence
\[
m_{r+1}=2m_r+3n_r,\qquad n_{r+1}=m_r+2n_r
\]
shows modulo \(2\) that \(n_r\) is odd for odd \(r\) and even for even \(r\). Hence the lower bound is attained separately in each parity class, and
\[
\liminf_{\substack{n\to\infty\\2\mid n}}n|\sin(\pi\sqrt3n)|
=
\liminf_{\substack{n\to\infty\\2\nmid n}}n|\sin(\pi\sqrt3n)|
=\frac{\pi}{2\sqrt3}.
\]
Equivalently,
\[
\limsup_{\substack{n\to\infty\\2\mid n}}\frac1{n|\sin(\pi\sqrt3 n)|}
=
\limsup_{\substack{n\to\infty\\2\nmid n}}\frac1{n|\sin(\pi\sqrt3 n)|}
=\frac{2\sqrt3}{\pi}.
\]
Multiplication by the two source coefficients and the vanishing \(O(n^{-2})\) remainders gives the asserted limsups.

## Verification
The arithmetic step is exact: the Pell recurrence preserves \(m_r^2-3n_r^2=1\) and alternates denominator parity. The bundled script `verify_pell_widths.py` checks those identities for a finite initial segment and evaluates the stable small-angle quantity \(1/[n_r\sin(\pi/(\sqrt3n_r+m_r))]\), which converges to \(2\sqrt3/\pi\). These finite computations corroborate the proof; they are not used as an exhaustive argument.

## Relationship to prior work
Baradaran–Exner derive the two parity-dependent formulas above and conclude, using the quadratic irrationality of \(\sqrt3\), that the family-(iii) high-energy widths remain bounded. Their paper does not identify the sharp limsup or the arithmetic subsequences realizing it. Standard Pell theory supplies exactly the missing sharp arithmetic constant. Searches under the model name together with “Pell”, “limsup band width”, “Diophantine band width”, and the explicit \(\csc(\sqrt3n\pi)\) factor found no published spectral statement giving these constants.

## Limitations
The argument sharpens the source's established family-(iii) asymptotic; it does not rederive the underlying Floquet determinant expansion. The result is a limsup statement, not convergence of the widths. The possibility remains that an equivalent calculation exists in weakly indexed literature under different terminology, although no covering statement was found in the inspected primary source or targeted searches.

## References
1. M. Baradaran and P. Exner, “Cairo lattice with time-reversal non-invariant vertex couplings,” arXiv:2312.13827v1, especially Section 3.2(iii).
2. M. Baradaran and P. Exner, *Journal of Physics A: Mathematical and Theoretical* 57 (2024), article associated with DOI 10.1088/1751-8121/ad52d6.
3. Classical Pell-equation identity for \(x^2-3y^2=1\), used here only through the explicit powers of \(2+\sqrt3\).
