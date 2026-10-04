# Exact certification of the \(5,9\) hole in the order-\(16\) Fourier uncertainty diagram
## Finding
Let \(\zeta=\exp(2\pi i/16)\) and define the discrete Fourier transform by
\[
\widehat f(r)=\sum_{c=0}^{15} f(c)\zeta^{rc},\qquad r\in\mathbb Z_{16}.
\]
There is no nonzero function \(f:\mathbb Z_{16}\to\mathbb C\) satisfying
\[
|\operatorname{supp}f|=5,\qquad |\operatorname{supp}\widehat f|=9.
\]
Equivalently, the exact support pair \((5,9)\) is absent from the Fourier uncertainty diagram of \(\mathbb Z_{16}\).

## Assumptions and scope
The statement concerns the ordinary complex discrete Fourier transform on the cyclic group \(\mathbb Z_{16}\), with no restriction on the nonzero complex amplitudes of \(f\). If \(A\) is the time support, then \(|A|=5\). If \(B\) is the Fourier zero set, then \(|B|=7\), because exact Fourier support size nine is equivalent to exactly seven Fourier zeros.

For sets \(A,B\subseteq\mathbb Z_{16}\), write \(F[B,A]\) for the submatrix \((\zeta^{rc})_{r\in B,c\in A}\). All ranks below are ranks over \(\mathbb C\), computed exactly in the cyclotomic field \(\mathbb Q(\zeta)\).

## Proof
Fix \(|A|=5\) and \(|B|=7\), and put \(M=F[B,A]\) and \(K=\ker M\). A coefficient vector in \(K\) gives a signal supported inside \(A\) whose Fourier transform vanishes on \(B\). Put \(r=\operatorname{rank}M\). There exists a vector in \(K\) with time support exactly \(A\) and Fourier zero set exactly \(B\) if and only if all of the following hold:

1. \(r<5\).
2. For every \(a\in A\),
\[
\operatorname{rank}F[B,A\setminus\{a\}]=r.
\]
3. For every \(y\in\mathbb Z_{16}\setminus B\),
\[
\operatorname{rank}F[B\cup\{y\},A]=r+1.
\]

Indeed, condition 2 says that \(K\) is not contained in any coordinate hyperplane \(c_a=0\); condition 3 says that \(K\) is not contained in the kernel of any additional Fourier row. Over \(\mathbb C\), a finite-dimensional vector space cannot be the union of finitely many proper linear subspaces. Hence these separate noncontainment conditions can be satisfied simultaneously by one vector in \(K\). The converse is immediate from an exact-support vector. This is the rank criterion underlying the support-pair test.

Time translation changes Fourier coefficients only by nonzero phases, while modulation translates the Fourier zero set. Thus \(A\) and \(B\) may be reduced independently modulo cyclic translation. A nontrivial translation stabilizer would partition a set into cycles whose common size divides \(16\); since \(5\) and \(7\) are both coprime to \(16\), every translation orbit of a five-set or seven-set has size \(16\). Therefore the full
\[
\binom{16}{5}\binom{16}{7}=49{,}969{,}920
\]
pairs reduce exactly to
\[
\frac{\binom{16}{5}}{16}\frac{\binom{16}{7}}{16}=273\cdot715=195{,}195
\]
translation-orbit representatives.

The exact enumeration gives the following exhaustive rank census. Of the \(195{,}195\) representative pairs, \(193{,}416\) have \(\operatorname{rank}F[B,A]=5\), so they fail condition 1. The remaining \(1{,}779\) are rank deficient: \(1{,}752\) have rank four and \(27\) have rank three. None of the rank-three cases satisfies all five column-deletion conditions. Exactly \(136\) rank-four cases satisfy every column-deletion condition, but every one of those \(136\) cases fails at least one row-extension condition. Consequently no representative pair satisfies the criterion, and translation/modulation symmetry then excludes every original pair \((A,B)\). Hence no signal has exact support pair \((5,9)\).

## Verification
The standalone verifier `verify_z16_5_9_hole.py` performs the complete enumeration with integer arithmetic. For a square Fourier minor it expands
\[
\det(\zeta^{r_i c_j})=\sum_{\sigma}\operatorname{sgn}(\sigma)\zeta^{\sum_i r_i c_{\sigma(i)}}.
\]
Because \(\Phi_{16}(X)=X^8+1\), every term is reduced using \(\zeta^{e+8}=-\zeta^e\) to an integer coefficient vector in the basis \(1,\zeta,\ldots,\zeta^7\). The determinant is zero if and only if all eight coefficients vanish. Ranks are then determined by exact minor tests, so no numerical tolerance is used.

A replay of the packaged verifier produced

`support_representatives=273`

`zero_set_representatives=715`

`orbit_pairs=195195`

`full_rank=193416`

`rank_deficient=1779`

`rank_histogram={3:27,4:1752}`

`deletion_conditions_pass=136`

`extension_conditions_fail=136`

`admissible_exact_support_pairs=0`

`VERIFY_OK`

## Relationship to prior work
Krahmer, Pfander, and Rashkov formulated the same rank criterion in Lemma 3.4 of arXiv:math/0611493 and used it to study support-pair diagrams. They explicitly singled out the order-\(16\) pair with five nonzero time entries and nine nonzero Fourier entries, saying that their numerical evidence for nonexistence required singular-value calculations for \(49{,}969{,}920\) five-by-seven matrices. Their Figure 1 distinguishes numerically supported nonexistence from proved nonexistence. The result here upgrades that specific numerical observation to an exact finite proof.

Delvaux and Van Barel studied rank-deficient Fourier submatrices and exact uncertainty minima for prime-power orders. Those results control the monotone minimum Fourier support as a function of a time-support bound, but they do not decide whether this particular exact pair \((5,9)\) is attainable.

Yang, Zhang, Wang, Geng, and Chen later proved that discrete-Fourier uncertainty diagrams have no holes on or above \(n_{\mathcal A}+n_{\mathcal B}=d+1\), and they gave additional low-frequency-support classifications. Here \(d=16\) and \(5+9=14<17\), so that theorem does not cover this point.

## Limitations
This result certifies one mathematically motivated hole of the order-\(16\) diagram; it is not a complete classification of all support pairs for \(\mathbb Z_{16}\), nor does the finite computation by itself imply a theorem for other cyclic orders. The originality comparison is limited by the possibility of differently phrased or poorly indexed exact computations not surfaced by the targeted literature searches.

## References
1. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first submitted 2006-11-16; see Lemma 3.4 and the discussion of Figure 2.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, Report TW 470, K.U. Leuven, September 2006; later Linear Algebra Appl. 429 (2008), 1587--1605.
3. Y.-H. Yang, B.-B. Zhang, X.-L. Wang, S.-J. Geng, and P.-Y. Chen, *Characterizing Kirkwood-Dirac nonclassicality and uncertainty diagram based on discrete Fourier transform*, arXiv:2303.17203; Entropy 25 (2023), 1075.
