# Arithmetic resonance in positive-impulse repairs of cubic cyclic Gabor chirps

## Finding
For every prime \(p\ge5\), every real \(t>0\), and \(\omega=\exp(2\pi i/p)\), consider the unit vector
\[
g_{p,t}(j)=\frac{\omega^{j^3}+t\mathbf1_{\{0\}}(j)}{\sqrt{p+2t+t^2}},\qquad j\in\mathbb Z/p\mathbb Z.
\]
Define its cyclic ambiguity function by \(A_{p,t}(a,b)=\langle g_{p,t},M_bT_a g_{p,t}\rangle\), where \((T_a f)(j)=f(j-a)\), \((M_b f)(j)=\omega^{bj}f(j)\), and the inner product is conjugate-linear in the first argument.

**Exact zero-set classification.** If \(p\equiv3\pmod4\), the ambiguity function is nonzero at every \((a,b)\) for **every** \(t>0\). If \(p\equiv1\pmod4\), let \(\chi_p\) be the quadratic character and let \(r\in\{0,\dots,p-1\}\) represent \(ab/2\pmod p\). Then \(A_{p,t}(a,b)=0\) if and only if all four conditions hold:
\[
 a\ne0,\qquad b^2\equiv-9a^4\pmod p,\qquad
 \chi_p(-3a)\cos(2\pi r/p)<0,\qquad
 t=\frac{\sqrt p}{2|\cos(2\pi r/p)|}.
\]
In particular, the exceptional-positive-amplitude set is finite for each prime. It is empty at \(p=5\) and \(p=13\). Its first nonempty prime is \(p=17\), where it consists of exactly
\[
 t_1=\frac{\sqrt{17}}{2\cos(\pi/17)},\qquad
 t_2=\frac{\sqrt{17}}{2\cos(6\pi/17)}.
\]
At each of these two amplitudes precisely four ambiguity coefficients vanish; at every other positive amplitude none vanish. Consequently, the full Gabor projector tomography operator is injective on the matrix space for every nonexceptional amplitude, while its complex rank falls from \(p^2\) to \(p^2-4\) at either exceptional amplitude for \(p=17\). By the standard nonvanishing-ambiguity criterion, every nonexceptional window also performs phase retrieval. Zero ambiguity coefficients at exceptional amplitudes establish failure of **linear operator tomography**, not necessarily failure of phase retrieval on rank-one inputs.

## Assumptions and scope
Primes are at least five; \(t\) is a strictly positive **real** scalar. The cubic chirp is defined on the prime cyclic group, not on a finite field of composite cardinality or a continuous domain. All congruences are modulo \(p\), and division by \(2\) or \(12a\) means multiplication by the unique modular inverse. The sample system contains the complete \(p^2\) time-frequency orbit. The phrase *informational completeness* refers to the induced **linear** map on complex \(p\times p\) matrices.

## Proof
Put \(K=p+2t+t^2\), let \(c_j=\omega^{j^3}\), and compute with the unnormalized window \(c+t\delta_0\). At zero translation,
\[
 K A_{p,t}(0,b)=\begin{cases}K,&b=0,\\ t(t+2),&b\ne0.\end{cases}
\]
This never vanishes for \(t>0\). For \(a\ne0\), direct expansion separates one complete quadratic Gauss sum and two linear cross terms:
\[
 K A_{p,t}(a,b)=\omega^{-a^3}\left[
 \sum_{j\in\mathbb F_p}\omega^{-3aj^2+(3a^2+b)j}
 +t(1+\omega^{ab})\right].\tag{1}
\]
The coefficient \(-3a\) is nonzero. Completing the square, the classical quadratic Gauss evaluation gives
\[
 \sum_j\omega^{-3aj^2+(3a^2+b)j}
 =\varepsilon_p\chi_p(-3a)\sqrt p\,
 \omega^{(3a^2+b)^2/(12a)},\qquad
 \varepsilon_p=\begin{cases}1,&p\equiv1\pmod4,\\ i,&p\equiv3\pmod4.\end{cases}\tag{2}
\]
The Gauss-sum phase and sign in (2) are fixed by the convention \(\omega=e^{2\pi i/p}\).

Since \(p\) is odd, \(1+\omega^{ab}\ne0\). Write \(r\equiv ab/2\pmod p\) with \(0\le r<p\), and \(C=\cos(2\pi r/p)\ne0\). Then \(1+\omega^{ab}=2C\omega^r\). Combining (1) and (2), the condition \(A_{p,t}(a,b)=0\) is equivalent to
\[
 t=-\frac{\varepsilon_p\chi_p(-3a)\sqrt p}{2C}\,
 \omega^E,\qquad E\equiv\frac{9a^4+b^2}{12a}\pmod p.\tag{3}
\]
For \(p\equiv3\pmod4\), the factor \(i\omega^E\) is never real: no odd-order root of unity is \(i\) or \(-i\). Hence no real \(t>0\) satisfies (3). For \(p\equiv1\pmod4\), an odd-order root \(\omega^E\) is real only when \(E=0\); this is equivalent to \(b^2=-9a^4\). Equation (3) then gives precisely the stated sign condition and positive amplitude, proving both necessity and sufficiency.

If \(p\equiv1\pmod4\), the congruence in the classification has exactly the two solutions \(b=\pm3\iota a^2\), where \(\iota^2=-1\) in \(\mathbb F_p\). Thus there are finitely many candidates. For \(p=5\) and \(p=13\), direct modular enumeration of these candidate pairs shows \(\chi_p(-3a)C>0\) always; the standalone script checks these signs using only integer congruences and integer inequalities for the cosine sign. For \(p=17\), the qualifying pairs are exactly
\[
 (a,b)\in\{(2,3),(2,14),(15,3),(15,14),
 (3,6),(3,11),(14,6),(14,11)\}.
\]
The first four have \(|C|=\cos(6\pi/17)\), and the latter four have \(|C|=\cos(\pi/17)\). These yield the two distinct amplitudes and four zeros at each, with no further possibilities.

For the operator-theoretic conclusion, the Fourier diagonalization of the full Gabor projector Gram matrix gives eigenvalues \(p|A_{p,t}(a,b)|^2\), one per phase-space index (up to permutation). Thus precisely the zero coefficients counted above contribute to its nullity. Invertible lifting implies the usual phaseless uniqueness on vectors; the converse is not claimed.

## Verification
Run \(\texttt{python3 verification.py}\) with standard Python 3. The checker confirms (1)–(3) against direct cyclic sums at all phase-space points for selected primes and positive amplitudes; it verifies the exact finite modular sign tests at \(p=5,13,17\) and the two four-element zero sets at \(p=17\). The checker reports 4,355 finite comparisons. These finite tests are corroboration only: the all-prime theorem is proved by (1)–(3) and the Gauss-sum evaluation.

## Relationship to prior work
Bojarovska and Flinth established the general nonvanishing-ambiguity sufficient condition for cyclic Gabor phase retrieval. Li's 2026 study constructs explicit full-spark phase-retrieving Gabor windows and analyzes constant- and two-site repairs of **quadratic Chu chirps**, including spectral diagonalization. Neither inspected treatment classifies the cancellation amplitudes of a *cubic* chirp with a positive real impulse. The cubic derivative creates a quadratic Gauss sum with a characteristic-dependent phase; that phase produces the precise arithmetic resonance test above. The quadratic Gauss evaluation and the general Gabor spectral diagonalization are prior tools and are not claimed as new.

## Limitations
The result applies to primes at least five, not all cyclic orders. It characterizes zero-free ambiguity and linear tomography, but it does not prove that every exceptional positive amplitude fails nonlinear phase retrieval. It makes no optimal-frame-bound or full-spark claim and does not assert historical priority against unindexed presentations of an equivalent one-impulse cubic-chirp calculation. Finite verification alone does not certify any infinite-prime statement; no independent validation has been performed.

## References
1. D. Li, *Explicit Full-Spark Gabor Windows with Quantitative Phase Retrieval*, arXiv:2609.09614 (first posted 2026-09-09; revised text 2026-09-30), especially Proposition 2.4 and Section 3.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800; J. Fourier Anal. Appl. 22 (2016), 542–567.
3. W. O. Alltop, *Complex sequences with low periodic correlations*, IEEE Trans. Inform. Theory 26 (1980), 350–354.
