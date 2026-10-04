# Quartic support localization in a minimal mixed-collinearity line multiview configuration

## Finding

For the five cameras \(C_i=[I_3\mid(v_i,0,0)^T]\) with \(v_i=0,1,2,3\) for \(1\le i\le4\) and \(C_5=\begin{psmallmatrix}1&0&0&0\\0&0&1&0\\0&0&0&1\end{psmallmatrix}\), let \(I=I_3(M)\) be the ideal of \(3\times3\) minors of the line-multiview matrix and let \(F\) be the four-collinear-camera quartic correction. Then \(x_5F,z_5F\in I\), while at \(\ell_i=[0:1:v_i^2]\) for \(i\le4\) and \(\ell_5=[0:1:0]\) all minors vanish but \(F=-12\). Hence the class of \(F\) in the determinantal quotient is supported over the fifth-view projected-baseline point: \(F\) is redundant on \(D(x_5)\cup D(z_5)\), but \(F\notin\sqrt I\).

## Assumptions and scope

Work over \(\mathbb C\). For \(i=1,2,3,4\), take
\[
C_i=\begin{pmatrix}1&0&0&v_i\\0&1&0&0\\0&0&1&0\end{pmatrix},
\qquad (v_1,v_2,v_3,v_4)=(0,1,2,3),
\]
and take
\[
C_5=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
\]
The first four centers lie on the baseline \(B=\langle e_1,e_4\rangle\subset\mathbb P^3\), whereas the fifth center \([0:1:0:0]\) does not. Write the image-line coordinates as \(\ell_i=[x_i:y_i:z_i]\), and let
\[
M=(C_1^T\ell_1\;\cdots\;C_5^T\ell_5)
 =\begin{pmatrix}
x_1&x_2&x_3&x_4&x_5\\
y_1&y_2&y_3&y_4&0\\
z_1&z_2&z_3&z_4&y_5\\
0&x_2&2x_3&3x_4&z_5
\end{pmatrix}.
\]
Let \(I=I_3(M)\) and, following the four-collinear correction determinant of Breiding--Duff--Gustafsson--Rydell--Shehu, put
\[
F=\det\begin{pmatrix}
0&0&z_1&y_1\\
z_2&y_2&z_2&y_2\\
2z_3&2y_3&z_3&y_3\\
3z_4&3y_4&z_4&y_4
\end{pmatrix}.
\]
Equivalently,
\[
F=-y_1y_2z_3z_4+4y_1y_3z_2z_4-3y_1y_4z_2z_3-3y_2y_3z_1z_4+4y_2y_4z_1z_3-y_3y_4z_1z_2.
\]
The claim concerns this explicit minimal mixed configuration and this specific quartic; it does not assert a complete defining ideal for arbitrary mixed camera arrangements.

## Proof

For row indices \(r<s<t\) and camera indices \(i<j<k\), write \(\Delta_{rst}^{ijk}\) for the corresponding \(3\times3\) minor of \(M\). Exact expansion gives
\[
\begin{aligned}
x_5F={}&7y_4y_5\Delta_{123}^{123}-6y_3y_5\Delta_{123}^{124}
+4(y_3z_4-y_4z_3)\Delta_{123}^{125}\\
&+3y_2y_5\Delta_{123}^{134}+(y_4z_2-y_2z_4)\Delta_{123}^{135}
-3y_4y_5\Delta_{234}^{123}\\
&+2y_3y_5\Delta_{234}^{124}-y_2y_5\Delta_{234}^{134},
\end{aligned}
\]
and
\[
\begin{aligned}
z_5F={}&6y_4y_5\Delta_{123}^{123}-6y_3y_5\Delta_{123}^{124}+6y_2y_5\Delta_{123}^{134}
-2y_4y_5\Delta_{234}^{123}\\
&+2y_3y_5\Delta_{234}^{124}+4(y_3z_4-y_4z_3)\Delta_{234}^{125}
-2y_2y_5\Delta_{234}^{134}\\
&+(y_4z_2-y_2z_4)\Delta_{234}^{135}.
\end{aligned}
\]
Therefore \(x_5F,z_5F\in I\). On either principal open set \(D(x_5)\) or \(D(z_5)\), the corresponding coordinate is invertible, so \(F\in I\) after localization.

The common baseline \(B\) is mapped by \(C_5\) to the image line \(y=0\), whose dual line coordinate is \([0:1:0]\). Now specialize
\[
\ell_i=[0:1:v_i^2]\quad(1\le i\le4),\qquad \ell_5=[0:1:0].
\]
Then
\[
M=\begin{pmatrix}0&0&0&0&0\\1&1&1&1&0\\0&1&4&9&1\\0&0&0&0&0\end{pmatrix},
\]
which has rank \(2\). Hence every \(3\times3\) minor vanishes, whereas direct substitution gives \(F=-12\neq0\). Thus \(F\notin\sqrt I\). Together with the two syzygies, this proves that the determinantal failure detected by this quartic can only persist over the fifth-view point \([0:1:0]\), exactly the projected common baseline.

## Verification

The accompanying `verify_mixed_collinearity.py` reconstructs \(M\) and \(F\) over the exact rational polynomial ring, expands both displayed syzygies, and checks that their differences from \(x_5F\) and \(z_5F\) are identically zero. It then evaluates all forty \(3\times3\) minors at the displayed witness, confirms matrix rank \(2\), and confirms \(F=-12\).

A separate exact multigraded Macaulay calculation in total multidegree \((1,1,1,1,1)\) gave rank \(142\) for the degree-five minor-multiple span; adjoining \(x_5F\) or \(z_5F\) leaves the rank unchanged, while adjoining \(y_5F\) raises it to \(143\). This last rank check is supplementary and is not used to claim any stronger saturation statement.

## Relationship to prior work

Breiding--Rydell--Shehu--Torres give a complete set-theoretic description for arbitrary camera arrangements and explain the extra component created by collinear centers; their four-collinear example shows that a quartic correction can remove that component. Breiding--Duff--Gustafsson--Rydell--Shehu later give the explicit four-camera determinant used here, prove that minors alone generate the ideal when no four centers are collinear, and prove scheme-theoretic results when all centers are collinear.

The present statement lies between those regimes: exactly four of five centers are collinear. The prior set-theoretic description does not imply the displayed ideal-membership syzygies, while the all-collinear scheme theorem is inapplicable because the fifth center is off the baseline. The new information is the exact support localization of the quartic class with respect to the fifth image: away from the projected baseline, this correction is already forced by the determinantal ideal.

## Limitations

Only the displayed rational five-camera arrangement is proved. No invariance under arbitrary baseline cross-ratio or arbitrary choice of fifth camera is claimed. The result concerns one quartic correction, not the full mixed-collinearity ideal, its radical, primary decomposition, or a universal Gröbner basis. The computation \(y_5F\notin I\) in one multidegree does not establish a statement about all powers of \(y_5\) or about saturation at \((x_5,z_5)\).

## References

1. P. Breiding, F. Rydell, E. Shehu, A. Torres, *Line Multiview Varieties*, arXiv:2203.01694 (first public 2022-03-03); SIAM J. Applied Algebra and Geometry 7 (2023), 470--504, DOI 10.1137/22M1482263.
2. P. Breiding, T. Duff, L. Gustafsson, F. Rydell, E. Shehu, *Line Multiview Ideals*, arXiv:2303.02066 (first public 2023-03-03).
