# An indefinite controller can hide a non-Bessel sequence from the controlled Gram matrix

## Finding
Lemma 2.6 of Osgooei--Rahimi asserts that if \(U,C\in GL(H)\) and the matrix
\[
\bigl(\langle C f_j,U f_k\rangle\bigr)_{k,j\ge1}
\]
defines a bounded operator on \(\ell^2\), then \(\{f_k\}\) is a Bessel sequence.

This is false under the printed hypotheses.

Let
\[
H=\mathbb C^2,
\qquad
U=I,
\qquad
C=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
v=\frac1{\sqrt2}
\begin{pmatrix}
1\\
1
\end{pmatrix}.
\]
Define
\[
f_k=v
\qquad(k\ge1).
\]
Both \(U\) and \(C\) are bounded and invertible. Moreover
\[
Cv=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
-1
\end{pmatrix}
\]
and therefore
\[
\langle Cv,v\rangle=0.
\]
For every \(j,k\),
\[
\langle C f_j,U f_k\rangle=0.
\]
Thus the controlled Gram matrix is exactly the zero matrix, hence the bounded zero operator on \(\ell^2\).

The sequence itself is not Bessel. Taking \(x=v\),
\[
\sum_{k=1}^{\infty}
|\langle x,f_k\rangle|^2
=
\sum_{k=1}^{\infty}1
=
\infty.
\]

Hence a bounded controlled Gram matrix does not diagnose Besselness when the controller pair is allowed to be indefinite.

A clean repair is obtained if
\[
U^*C\in GL^+(H).
\]
Under that extra hypothesis, boundedness of the controlled Gram matrix is equivalent to Besselness of the underlying sequence.

## Assumptions and scope
The source explicitly works throughout with
\[
U,C\in GL(H),
\]
not only positive operators. Its Example 2.5 also uses sign-changing diagonal controllers, so indefinite controllers are part of the paper's stated framework.

The lemma itself asks whether the entry matrix can certify Besselness before Besselness is known. In the example above the entry matrix is unambiguously well-defined and equals the zero operator on \(\ell^2\).

The corrected equivalence below uses the additional hypothesis
\[
A=U^*C\in GL^+(H).
\]
This is a sufficient structural repair. No claim is made that positivity is the weakest conceivable hypothesis for every controller pair.

## Proof
For the counterexample, all controlled Gram entries coincide with
\[
\langle Cv,v\rangle.
\]
Direct calculation gives
\[
\langle Cv,v\rangle
=
\frac12(1-1)
=
0.
\]
Therefore the controlled Gram operator is zero.

On the other hand, since \(\|v\|=1\),
\[
|\langle v,f_k\rangle|^2=1
\]
for every \(k\), so the Bessel sum diverges.

Now assume instead that
\[
A=U^*C\in GL^+(H).
\]
For all \(j,k\),
\[
\langle C f_j,U f_k\rangle
=
\langle A f_j,f_k\rangle
=
\langle A^{1/2}f_j,A^{1/2}f_k\rangle.
\]
Set
\[
g_k=A^{1/2}f_k.
\]
The controlled Gram matrix of \(\{f_k\}\) is exactly the ordinary Gram matrix of \(\{g_k\}\).

For an arbitrary sequence \(\{g_k\}\), boundedness of its Gram matrix on \(\ell^2\) is equivalent to the Bessel property. Indeed, for every finitely supported scalar sequence \(c=(c_k)\),
\[
\left\|\sum_k c_k g_k\right\|^2
=
\langle Gc,c\rangle
\le
\|G\|\,\|c\|_{\ell^2}^2.
\]
Thus the finite synthesis map is uniformly bounded and extends to a bounded synthesis operator, which is equivalent to the Bessel inequality. The converse is the standard composition of bounded synthesis and analysis operators.

Since \(A^{-1/2}\) is bounded,
\[
f_k=A^{-1/2}g_k.
\]
Therefore \(\{g_k\}\) is Bessel if and only if \(\{f_k\}\) is Bessel. This proves the repaired equivalence.

## Verification
The first public preprint was inspected at the global controller assumptions, Definition 2.1, Example 2.5, the definition of the controlled Gram matrix, and the complete statement and proof of Lemma 2.6.

The proof defines
\[
M=\overline{\operatorname{span}}\{U^*C f_k:k\ge1\}
\]
and in its third case writes a vector as
\[
g=p+h,
\qquad
h\in M^\perp.
\]
It then replaces
\[
\sum_k|\langle p+h,f_k\rangle|^2
\]
by
\[
\sum_k|\langle p,f_k\rangle|^2.
\]
That equality requires
\[
\langle h,f_k\rangle=0
\]
for every \(k\), which is not implied by
\[
h\perp U^*C f_k.
\]

The explicit example realizes this failure exactly:
\[
M=\operatorname{span}\{Cv\}
=
\operatorname{span}\{(1,-1)\},
\]
while
\[
v\in M^\perp.
\]
The term discarded by the proof is therefore the whole non-Bessel component.

The journal record and author-uploaded public full text were also checked against the first public version. The article retains the same diagnostic objective and controller framework.

No numerical approximation, finite truncation, or experimental inference is used.

## Relationship to prior work
For ordinary frames, boundedness of the usual Gram matrix is equivalent to Besselness. The controlled matrix ceases to have this diagnostic property because an indefinite sesquilinear form can have nonzero isotropic vectors.

The positivity repair reduces the controlled matrix to an ordinary Gram matrix after the invertible change of variables
\[
f_k\mapsto (U^*C)^{1/2}f_k.
\]
It therefore recovers precisely the standard Gram-matrix mechanism.

Targeted searches for the exact source, Lemma 2.6, bounded controlled Gram matrices, isotropic-controller counterexamples, and positivity repairs did not locate an indexed correction or a published statement containing this explicit counterexample. Nearby results on cross-Gram matrices, bi-\(g\)-frames, weaving, and controlled-\(K\)-frame perturbations concern different hypotheses and do not imply the present correction.

## Limitations
The result corrects Lemma 2.6. It does not assess every later theorem in the paper.

The condition
\[
U^*C\in GL^+(H)
\]
is a natural exact repair for the stated bounded-Gram-versus-Bessel equivalence, but other coercive hypotheses may also suffice.

A nonindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. E. Osgooei and A. Rahimi, *Gram matrix associated to controlled frames*, arXiv:1709.05641v1, first public version 17 September 2017.
2. E. Osgooei and A. Rahimi, *Gram matrix associated to controlled frames*, International Journal of Wavelets, Multiresolution and Information Processing 16(5) (2018), Article 1850035, DOI 10.1142/S0219691318500352.
