# A square-root scaling defect breaks a two-operator \(K\)-\(g\)-weaving theorem

## Finding
Theorem 2.6 of Xiang states a perturbation criterion intended to preserve the weaving of two \(K\)-\(g\)-frames after applying two different surjective operators. Its printed smallness condition uses the quadratic frame bounds \(C\) and \(D_\Gamma\) without square roots.

This can make the theorem's qualitative conclusion false.

Let
\[
H=\mathbb C^2,
\qquad
I=\{1,2\},
\qquad
K=\frac14 I_H.
\]
For \(f=(f_1,f_2)\), define
\[
\Lambda_1 f=\Gamma_1 f=f_1,
\qquad
\Lambda_2 f=\Gamma_2 f=f_2.
\]
The two families are identical. Therefore every weaving has coefficient energy
\[
|f_1|^2+|f_2|^2=\|f\|^2.
\]
Since
\[
\|K^*f\|^2=\frac1{16}\|f\|^2,
\]
the pair is \(K\)-woven with valid universal bounds
\[
C=16,
\qquad
D=1.
\]
The Bessel bound of \(\Gamma\) is
\[
D_\Gamma=1.
\]

Now take
\[
U_1=I_H,
\qquad
U_2=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
These operators are unitary, hence surjective, and they commute with the scalar operator \(K\). All kernel hypotheses of Theorem 2.6 hold.

The numerical quantities in the theorem are
\[
\|U_1^\dagger\|=1,
\qquad
\|U_2-U_1\|=2,
\qquad
\|\widetilde{K^*}^{-1}\|=4.
\]
Thus its printed hypothesis becomes
\[
8<16,
\]
so the theorem applies.

For the partition
\[
\sigma_1=\{1\},
\qquad
\sigma_2=\{2\},
\]
however,
\[
\Lambda_1U_1^*f=f_1
\]
and
\[
\Gamma_2U_2^*f=f_1.
\]
The corresponding weaving has energy
\[
2|f_1|^2.
\]
At \(f=e_2\), this is zero while
\[
\|K^*e_2\|^2=\frac1{16}.
\]
Hence this weaving is not a \(K\)-\(g\)-frame.

## Assumptions and scope
The example uses a complex Hilbert space of dimension two, a two-element index set, and invertible operators throughout. There are no closure, convergence, domain, or pseudo-inverse pathologies.

The source definition requires only positive frame-bound constants; it does not require the numerical lower \(K\)-\(g\)-frame bound \(C\) to be less than the ordinary Bessel upper bound \(D\). Here \(C=16\) is the exact \(K\)-relative lower bound because \(K=\frac14 I_H\).

The finding concerns Theorem 2.6 and its quantitative perturbation threshold. It does not challenge the paper's single-operator preservation result, whose scaling is different.

## Proof
The original families satisfy
\[
\sum_{i=1}^2\|\Lambda_i f\|^2
=
\sum_{i=1}^2\|\Gamma_i f\|^2
=
\|f\|^2.
\]
For
\[
K=\frac14 I_H,
\]
this is exactly
\[
16\|K^*f\|^2.
\]
Because \(\Lambda_i=\Gamma_i\) for every \(i\), every partition gives the same family. Therefore \(C=16\) and \(D=1\) are valid universal weaving bounds.

The swap operator \(U_2\) has eigenvalues \(1\) and \(-1\), so
\[
\|U_2-I_H\|=2.
\]
Also,
\[
U_1^\dagger=I_H
\]
and
\[
\widetilde{K^*}^{-1}=4I_H.
\]
The printed smallness condition is therefore
\[
1\cdot2\cdot4
<
\frac{16}{1}.
\]

For the partition selecting the first member of the \(U_1\)-transformed family and the second member of the \(U_2\)-transformed family,
\[
\Lambda_1U_1^*f=f_1
\]
and, because \(U_2^*=U_2\),
\[
\Gamma_2U_2^*f=(U_2f)_2=f_1.
\]
At \(e_2\), both selected coefficients vanish. Since \(K^*e_2\ne0\), no positive lower \(K\)-\(g\)-frame bound exists.

For the repair, let
\[
E(f)
=
\sum_{i\in\sigma_1}\|\Lambda_iU_1^*f\|^2
+
\sum_{i\in\sigma_2}\|\Gamma_iU_2^*f\|^2.
\]
The triangle inequality in the coefficient Hilbert space gives
\[
E(f)^{1/2}
\ge
\left(
\sum_{i\in\sigma_1}\|\Lambda_iU_1^*f\|^2
+
\sum_{i\in\sigma_2}\|\Gamma_iU_1^*f\|^2
\right)^{1/2}
-
\left(
\sum_{i\in\sigma_2}\|\Gamma_i(U_2^*-U_1^*)f\|^2
\right)^{1/2}.
\]
The first term is at least
\[
\sqrt C\,\|K^*U_1^*f\|,
\]
whereas the second is at most
\[
\sqrt{D_\Gamma}\,\|U_2-U_1\|\,\|f\|.
\]
Repeating the source's pseudo-inverse reduction on \(\ker(K^*)^\perp\) yields
\[
E(f)^{1/2}
\ge
\left(
\sqrt C\,\|U_1^\dagger\|^{-1}
-
\sqrt{D_\Gamma}\,\|U_2-U_1\|\,\|\widetilde{K^*}^{-1}\|
\right)
\|K^*f\|.
\]
This proves the corrected sufficient condition and lower bound.

## Verification
The full open-access article was inspected at Definition 1.1, Definition 1.2, Theorem 2.1, the complete statement and proof of Theorem 2.6, and the paper's notation for \(C\), \(D_\Gamma\), pseudo-inverses, and woven bounds.

Definition 1.1 places \(C\) and \(D\) in the squared frame inequality. Theorem 2.6 then takes a square root of a sum of squared coefficient norms but carries \(C\) and \(D_\Gamma\) into the resulting norm inequality without taking square roots. Its stated threshold and lower bound inherit that mismatch.

The two-dimensional counterexample was checked by direct matrix multiplication. No numerical approximation or finite-search inference is involved.

## Relationship to prior work
The earlier paper *Weaving of \(K\)-\(g\)-frames in Hilbert spaces* introduced operator-perturbation questions for woven \(K\)-\(g\)-frames. Theorem 2.6 is a later whole-space, two-operator perturbation statement.

A 2025 paper on operator perturbations of woven \(g\)-frames corrects a different closed-range preservation assertion in ordinary \(g\)-frame theory. Its results do not state the present scale-sensitive counterexample or the square-root repair for Theorem 2.6.

Targeted searches for the exact theorem, its DOI, the two-operator perturbation condition, square-root variants, and correction language did not locate an indexed correction of Theorem 2.6. Searches of nearby \(K\)-frame and \(K\)-\(g\)-frame results returned distinct perturbation, reconstruction, weaving-duality, and range phenomena rather than this scaling obstruction.

## Limitations
The corrected square-root inequality is a sufficient perturbation condition obtained directly from the intended proof. It is not claimed to be the optimal possible condition for every pair of woven \(K\)-\(g\)-frames.

The counterexample exploits the legitimate scale freedom in the operator \(K\). If additional normalizations on \(K\) or on the numerical choice of frame bounds are imposed, the relation between the printed and corrected thresholds may change.

A nonindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. Z.-Q. Xiang, *Some new results on the weaving of \(K\)-\(g\)-frames in Hilbert spaces*, Open Mathematics 19 (2021), 1315--1329, DOI 10.1515/math-2021-0103.
2. X.-C. Xiao, G.-R. Zhou and Y.-C. Zhu, *Weaving of \(K\)-\(g\)-frames in Hilbert spaces*, ScienceAsia 45 (2019), 285--291, DOI 10.2306/scienceasia1513-1874.2019.45.285.
3. Z.-Q. Xiang and C.-X. Lin, *A New View on the Wovenness of \(g\)-Frames Under Operators*, Journal of Mathematics (2025), Article 7185421, DOI 10.1155/jom/7185421.
