# The adjoint-range gap in a controlled \(K\)-\(g\)-fusion transport criterion

## Finding
Theorem 2.3 of Rahimlou--Sadri--Ahmadi gives an if-and-only-if criterion for transporting a controlled \(K\)-\(g\)-fusion frame through a bounded operator \(U\). Its converse implication is false.

The theorem assumes
\[
R(U)\subseteq R(K)
\]
and tests
\[
\|U^*f\|\ge\delta\|K^*f\|.
\]
The proof then replaces \(\|U^*f\|\) by a quantity involving \(K^*U^*f\) through the Moore--Penrose inverse. That replacement needs information about \(R(U^*)\), not \(R(U)\).

Take
\[
H=\mathbb C^2,\qquad
K=P_{\operatorname{span}\{e_1\}},\qquad
C=C'=I_H.
\]
Use one fusion block
\[
W_1=H,\qquad
v_1=1,\qquad
\Lambda_1=K,
\]
and define
\[
U=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
\]
Then the original family is Parseval and
\[
R(U)=R(K)=\operatorname{span}\{e_1\}.
\]
Also
\[
\|U^*f\|=\|K^*f\|
\]
for every \(f\), so the theorem's numerical condition holds with \(\delta=1\).

Nevertheless,
\[
UW_1=\operatorname{span}\{e_1\}
\]
and
\[
\Lambda_1U^*\pi_{UW_1}=0.
\]
Thus the transformed family has zero analysis energy on every vector and cannot have a positive lower \(K\)-\(g\)-fusion bound.

The missing geometry is
\[
R(U^*)\subseteq R(K).
\]
Adding this adjoint-range hypothesis makes the published pseudo-inverse step valid and repairs the sufficient direction. Alternatively, a direct \(K^*\)-scaled condition on \(U^*\) avoids the problematic conversion altogether.

## Assumptions and scope
A controlled \(K\)-\(g\)-fusion frame is taken exactly in the source's sense. For closed subspaces \(W_i\), positive weights \(v_i\), maps \(\Lambda_i\), and invertible controls \(C,C'\), its energy is
\[
E_\Lambda(f)=
\sum_i v_i^2
\left\langle
\Lambda_i\pi_{W_i}C'f,
\Lambda_i\pi_{W_i}Cf
\right\rangle,
\]
with inequalities
\[
A_{CC'}\|K^*f\|^2
\le
E_\Lambda(f)
\le
B_{CC'}\|f\|^2.
\]

The counterexample uses identity controls, so positivity and commutation issues disappear. The range of \(K\) is one-dimensional and closed, and \(K^\dagger=K\).

The transformed subspace \(UW_1\) is one-dimensional and closed. Thus the counterexample does not rely on the separate issue that the image of a closed subspace under a general bounded operator need not be closed.

## Proof
For
\[
f=xe_1+ye_2,
\]
the original one-block energy is
\[
E_\Lambda(f)
=
\|Kf\|^2
=
|x|^2
=
\|K^*f\|^2.
\]
Therefore the original family is Parseval.

The operator \(U\) satisfies
\[
Ue_1=0,\qquad Ue_2=e_1,
\]
so
\[
R(U)=\operatorname{span}\{e_1\}=R(K).
\]
Its adjoint satisfies
\[
U^*e_1=e_2,\qquad U^*e_2=0.
\]
Hence
\[
U^*(xe_1+ye_2)=xe_2
\]
and
\[
\|U^*f\|=|x|=\|K^*f\|.
\]
The lower condition in Theorem 2.3 therefore holds with \(\delta=1\).

Now
\[
UW_1=\operatorname{span}\{e_1\},
\]
so
\[
\pi_{UW_1}f=xe_1.
\]
The transformed analysis map is \(\Lambda_1\pi_{W_1}U^*\), and \(W_1=H\), giving
\[
\Lambda_1U^*\pi_{UW_1}f
=
K(xe_2)
=
0.
\]
Thus the transformed energy vanishes identically. At \(f=e_1\),
\[
E_\Gamma(e_1)=0
\qquad\text{but}\qquad
\|K^*e_1\|^2=1.
\]
No positive lower controlled \(K\)-\(g\)-fusion bound exists.

For the repair, suppose \(K\) has closed range and
\[
R(U^*)\subseteq R(K).
\]
The Moore--Penrose identity gives
\[
(K^\dagger)^*K^*=P_{R(K)}.
\]
Therefore
\[
U^*f=(K^\dagger)^*K^*U^*f
\]
for every \(f\), and hence
\[
\|U^*f\|
\le
\|K^\dagger\|\|K^*U^*f\|.
\]
If
\[
\|U^*f\|\ge\delta\|K^*f\|,
\]
then
\[
\|K^*U^*f\|
\ge
\delta\|K^\dagger\|^{-1}\|K^*f\|.
\]
The original lower frame inequality applied to \(U^*f\), together with the projection identity used by the source, yields
\[
E_\Gamma(f)
\ge
A_{CC'}\delta^2\|K^\dagger\|^{-2}\|K^*f\|^2.
\]
The source's Bessel estimate gives
\[
E_\Gamma(f)\le B_{CC'}\|U\|^2\|f\|^2.
\]
Thus the added adjoint-range condition repairs the sufficient direction whenever the image subspaces are closed.

The stronger direct condition
\[
\|K^*U^*f\|\ge\eta\|K^*f\|
\]
gives the lower bound
\[
A_{CC'}\eta^2
\]
without any pseudo-inverse conversion.

## Verification
The publisher PDF was inspected at the definition of a controlled \(K\)-\(g\)-fusion frame, Lemma 1.1, Theorems 2.1--2.4, and the complete statement and proof of Theorem 2.3. The theorem assumes \(R(U)\subseteq R(K)\). Its converse proof explicitly writes
\[
\|U^*f\|
=
\|(K^\dagger)^*K^*U^*f\|.
\]
For closed-range \(K\), the operator on the right before \(U^*f\) is the orthogonal projection onto \(R(K)\), so the equality requires \(U^*f\in R(K)\).

The page image containing Theorem 2.3 and the disputed step was visually inspected. All matrices in the counterexample are \(2\times2\), and the frame inequalities and range identities are exact.

No numerical experiment or finite search is used.

## Relationship to prior work
In the same source, Theorem 2.1 transports a controlled \(K\)-\(g\)-fusion frame to a controlled \(UK\)-\(g\)-fusion frame under an invertible operator. Corollary 2.1 adds commutation with \(K^*\) before preserving the same \(K\). Those statements already distinguish operator transport from preservation of the original \(K\)-geometry.

The closely related 2020 paper *Constructions of \(K\)-\(g\)-fusion and their dual in Hilbert spaces* proves an image construction for invertible \(U\) and preserves the same \(K\) only after an additional commutation hypothesis. It also treats \(R(U)\subseteq R(K)\) in a different theorem whose conclusion concerns the original family as a \(U\)-\(g\)-fusion frame, not the transformed image family. It therefore does not imply Theorem 2.3.

Later continuous controlled \(K\)-\(g\)-fusion work uses range and quotient-operator conditions in related characterizations. None of the checked statements supplies the published Theorem 2.3 implication from a lower bound on \(\|U^*f\|\) alone.

Targeted searches using the exact article title, theorem number, \(R(U)\), \(R(U^*)\), Moore--Penrose, controlled \(K\)-\(g\)-fusion, counterexample, correction, and erratum terminology did not locate an indexed correction or the two-dimensional example above.

## Limitations
The finding refutes the sufficient direction of Theorem 2.3 as stated. Its necessary direction remains valid by the source's direct comparison between the transformed lower bound and the original Bessel bound.

The adjoint-range condition
\[
R(U^*)\subseteq R(K)
\]
is a sufficient repair for the source's proof, not claimed to be necessary for every fixed controlled frame. The direct \(K^*\)-scaled condition is another sufficient repair.

For a general bounded \(U\), one must also ensure that the image spaces \(UW_i\) are closed before calling the transformed triple a fusion-frame family. The counterexample avoids this issue because its image space is one-dimensional.

An unindexed note or informal author correction may contain the same adjoint-range observation.

## References
1. G. Rahimlou, V. Sadri and R. Ahmadi, *Construction of controlled \(K\)-\(g\)-fusion frames in Hilbert spaces*, U.P.B. Scientific Bulletin, Series A 82(1) (2020), 111--120.
2. R. Ahmadi, G. Rahimlou, V. Sadri and R. Zarghami Farfar, *Constructions of \(K\)-\(g\)-fusion and their dual in Hilbert spaces*, Bulletin of the Transilvania University of Brasov, Series III 13(62)(1) (2020), 17--32, DOI 10.31926/but.mif.2020.12.61.1.2.
3. P. Ghosh and T. K. Samanta, *Construction of continuous controlled \(K\)-\(g\)-fusion frames in Hilbert spaces*, Acta et Commentationes Universitatis Tartuensis de Mathematica 28(1) (2024), DOI 10.12697/ACUTM.2024.28.04.
