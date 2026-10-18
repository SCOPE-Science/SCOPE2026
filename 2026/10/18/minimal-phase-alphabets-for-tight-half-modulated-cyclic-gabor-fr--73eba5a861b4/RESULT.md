# Minimal phase alphabets for tight half-modulated cyclic Gabor frames

## Finding

For every even integer \(N=2M\ge2\) and every integer \(1\le k\le N\), let \(L=\{0,2,\ldots,N-2\}\subset\mathbb Z_N\), \(K=\{0,1,\ldots,k-1\}\), and \(\mu_r=\{e^{2\pi i j/r}:0\le j<r\}\). The smallest integer \(r\ge1\) for which a flat window \(g\in\mathbb C^N\), with \(\sqrt N\,g(j)\in\mu_r\) for all \(j\), gives a tight Gabor frame \(\{M_\ell T_tg:\ell\in L,\ t\in K\}\) is

\[
r_{\min}(N,k)=\begin{cases}
\infty,& k\text{ odd},\\
2,& k\text{ even and }M\text{ even},\\
3,& k\text{ even, }M\text{ odd, and }3\mid\gcd(M,k/2),\\
4,& k\text{ even, }M\text{ odd, and }3\nmid\gcd(M,k/2).
\end{cases}
\]

The first case is stronger than a phase-alphabet exclusion: **no flat complex window of any phases** yields tightness when \(k\) is odd. When tightness is possible the exact frame bound is \(k/2\). In particular, for \(N\equiv2\pmod4\), a ternary phase alphabet is sufficient precisely at the cubic divisibility resonances, while quadrature phases handle every remaining even translation count.

There is also an exact spectral reduction, useful independently of phase quantization. For any flat window \(g\) with arbitrary unimodular entries, put

\[
w_j=N g(j)\overline{g(j+M)},\qquad C_j=\sum_{t=0}^{k-1}w_{j-t},\qquad R=\max_{j\in\mathbb Z_N}|C_j|.
\]

The optimal lower and upper frame bounds (allowing a zero lower bound for a non-frame) are exactly

\[
A(g)=\frac{k-R}{2},\qquad B(g)=\frac{k+R}{2}.
\]

## Assumptions and scope

All indices are interpreted in the cyclic group \(\mathbb Z_N\). Translation and modulation are \((T_tg)(j)=g(j-t)\) and \((M_\ell g)(j)=e^{2\pi i\ell j/N}g(j)\). Flatness means \(|g(j)|=N^{-1/2}\) at every coordinate. The tight-frame condition is \(S_g=(k/2)I\), where \(S_g=\sum_{\ell\in L,t\in K}(M_\ell T_tg)(M_\ell T_tg)^*\). Here the star denotes conjugate transpose. The statement concerns consecutive translations and precisely the even-frequency modulation subgroup, not arbitrary sampling masks or variable-amplitude windows. The phase-order minimization runs over **all positive integers** \(r\), with the alphabet fixed to all \(r\)-th roots of unity; the number of distinct values actually used by a window is a different invariant.

## Proof

**1. Exact spectral reduction.** For indices \(i,j\in\mathbb Z_N\), direct expansion of the frame operator gives

\[
S_g(i,j)=\left(\sum_{\ell\in L}e^{2\pi i\ell(i-j)/N}\right)
\left(\sum_{t=0}^{k-1}g(i-t)\overline{g(j-t)}\right).
\]

The first factor equals \(M\) if \(i\equiv j\pmod M\), and zero otherwise. Under the permutation grouping \(i\) with \(i+M\), the operator splits into \(M\) Hermitian blocks

\[
\frac12\begin{pmatrix}k&C_i\\\overline{C_i}&k\end{pmatrix},\qquad 0\le i<M.
\]

Indeed, the diagonal is \(Mk/N=k/2\), and the off-diagonal is \(M/N\sum_{t=0}^{k-1}w_{i-t}=C_i/2\). Since \(w_{j+M}=\overline{w_j}\), one has \(C_{j+M}=\overline{C_j}\). The eigenvalues of each block are \((k\pm|C_i|)/2\), which establishes the exact frame-bound formula and proves that tightness is equivalent to \(C_i=0\) for every \(i\).

**2. Period and balance lemma.** For any sequence \(w\) on \(\mathbb Z_N\), the moving sums \(C_j=\sum_{t=0}^{k-1}w_{j-t}\) vanish identically if and only if the sequence has period \(d=\gcd(N,k)\) and its sum over one period is zero. Necessity follows from \(0=C_j-C_{j-1}=w_j-w_{j-k}\), which imposes both \(N\)- and \(k\)-periodicity, and then from \(C_j=(k/d)\sum_{u=0}^{d-1}w_u\). Sufficiency is immediate from the same formula. Every unit-modulus sequence obeying \(w_{j+M}=\overline{w_j}\) is realized by a flat window: take \(\sqrt N\,g(j)=w_j\) for \(0\le j<M\) and \(\sqrt N\,g(j+M)=1\). If \(w_j\in\mu_r\), this window uses only \(\mu_r\).

**3. Odd translation counts.** If \(k\) is odd, then \(d=\gcd(2M,k)\) is odd and divides \(M\). Any \(d\)-periodic sequence has \(w_{j+M}=w_j\), so the required half-shift conjugacy forces \(w_j=\overline{w_j}\in\{-1,1\}\). An odd number \(d\) of such signs cannot sum to zero. Thus no flat window is tight, even with continuously variable phases.

**4. Even counts, even half-length.** If \(k\) and \(M\) are both even, take \(w_j=(-1)^j\). Because \(M\) is even, \(w_{j+M}=w_j=\overline{w_j}\); any even-length moving sum vanishes. This gives a binary-phase tight frame via step 2. A one-phase window has constant \(w_j=1\) and never gives zero moving sums, so the minimum order is exactly two.

**5. Even counts, odd half-length.** Now \(M\) is odd and \(k\) is even. Set \(h=\gcd(M,k/2)\), which is odd. Then \(d=\gcd(2M,k)=2h\), and \(M\equiv h\pmod{2h}\). The balance and conjugacy conditions for a tight window become

\[
w_{j+2h}=w_j,\qquad w_{j+h}=\overline{w_j},\qquad
\sum_{j=0}^{h-1}\operatorname{Re}w_j=0.
\]

The one-phase alphabet fails. For the binary alphabet \(\mu_2\), all real parts are signs, whose sum over odd \(h\) cannot vanish. For the ternary alphabet \(\mu_3=\{1,\omega,\omega^2\}\), with \(\omega=e^{2\pi i/3}\), each real part is either \(1\) or \(-1/2\). If exactly \(u\) of the first \(h\) entries equal \(1\), their real-part sum equals \((3u-h)/2\); it vanishes exactly when \(3\mid h\). When this divisibility holds, choose \(h/3\) entries equal to \(1\) and \(2h/3\) entries equal to \(\omega\), extend the next \(h\) entries by conjugation, and then repeat periodically. The realization in step 2 gives the desired ternary window. If \(3\nmid h\), the ternary alphabet is impossible, but one can choose the first \(h\) entries to be \(i\), the next \(h\) to be \(-i\), and repeat: this is a conjugate-half-shift, zero-mean sequence in \(\mu_4\), hence yields a quaternary-phase tight frame. This exhausts the smaller possible alphabet orders and establishes the formula.

All constructions respect \(1\le k\le N\), including \(k=2\), \(k=N\), and the smallest ambient dimension \(N=2\). No numerical or unproved infinite assertion is used in the argument.

## Verification

The standalone file `CHECK.py` reconstructs the entire frame operator from its time-frequency atoms, independently compares its extreme eigenvalues to the exact block formulas, and tests explicit minimizing-alphabet constructions for every even \(2\le N\le40\) and every admissible \(k\). It also exhaustively enumerates phase-correlation assignments for \(N\in\{2,4,6,8,10,12\}\) and alphabets of orders \(1,2,3,4\), verifying the corresponding finite tightness conditions. Run `python CHECK.py` with NumPy installed. These checks test finite instances; the all-dimensional theorem is proved above.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez (2026) prove general block-equivalence for cyclic Gabor systems whenever one sampling set is a subgroup, and give the underlying frame-matrix block formulas. We use that structural perspective but derive the two-coordinate spectrum directly. The distinct claim here is the complete **minimum phase-shift alphabet** for the half-modulated, consecutive-translation model, including the unrestricted odd-count obstruction and the exact ternary divisibility resonance; their inspected theorems do not state this phase-order classification. Magsino (2018) gives a tightness criterion through sparse ambiguity functions for subgroup time-frequency sets and examples using CAZAC sequences. That general criterion does not explicitly classify minimal \(r\)-phase windows for these typically non-subgroup translation masks. An earlier equivalent calculation may exist outside the inspected literature.

## Limitations

Flat windows and the specified mask geometry are essential. The theorem does not optimize conditioning over non-tight frames, handle variable amplitude or arbitrary modulation subgroups, or establish uniqueness of minimizing windows. A generic block formula or ambiguity criterion is not itself new; the asserted distinguishing contribution is the exact arithmetic phase-alphabet boundary. Independent external validation and historical-priority adjudication have not been performed.

## References

1. O. Asipchuk, L. De Carli and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139v1 (first posted 15 May 2026), Sections 1, 3–5. https://arxiv.org/abs/2605.16139
2. M. Magsino, *Constant Amplitude Zero Autocorrelation Sequences and Single Pixel Camera Imaging*, University of Maryland dissertation (2018), Chapter 3, especially Theorem 3.2.7. https://api.drum.lib.umd.edu/server/api/core/bitstreams/64afdadf-1164-4338-bc62-66455280c63b/content
3. L. D. Abreu, P. Balazs, N. Holighaus, F. Luef and M. Speckbacher, *Time-frequency analysis on flat tori and Gabor frames in finite dimensions*, Appl. Comput. Harmon. Anal. 69 (2024), 101622; arXiv:2209.04191.
