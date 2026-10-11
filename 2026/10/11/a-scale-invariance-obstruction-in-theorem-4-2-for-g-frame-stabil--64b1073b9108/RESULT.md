# A scale-invariance obstruction in Theorem 4.2 for \(g\)-frame stability
## Finding
Rajeswari and George's Theorem 4.2 states that if a \(g\)-frame \(\{\Lambda_i\}\) with bounds \(A,B\) and a sequence \(\{\Gamma_i\}\) satisfy
\[
\sum_i\|(\Lambda_i+\Gamma_i)f\|^2\le \lambda\sum_i\|\Lambda_i f\|^2\qquad(f\in H),
\]
then, in addition to a Bessel characterization, \(\{\Gamma_i\}\) is a \(g\)-frame whenever
\[
\lambda<\frac{A\,\|T_\Lambda^\dagger\|^{-2}}{2B}.
\]
That additional conclusion is false. The obstruction is already one-dimensional, and the correct scale-invariant universal threshold under the same relative inequality is \(\lambda<1\).

More precisely, take \(H=\mathbb C\) with a single coefficient space \(H_1=\mathbb C\), let \(\Lambda_1=2I\), and let \(\Gamma_1=0\). Then \(\{\Lambda_1\}\) is a tight \(g\)-frame with exact bounds \(A=B=4\). Its synthesis operator is \(T_\Lambda=2I\), and because this operator is invertible its pseudoinverse/right inverse is uniquely \(T_\Lambda^\dagger=\tfrac12I\). The relative inequality holds with \(\lambda=1\), while
\[
\frac{A\,\|T_\Lambda^\dagger\|^{-2}}{2B}
=\frac{4\cdot4}{8}=2.
\]
Thus the printed strict hypothesis \(1<2\) is satisfied, but \(\{\Gamma_1\}\) is the zero family and has no positive lower frame bound.

The exact universal repair is
\[
\boxed{\lambda<1}.
\]
Under this condition the family \(\{\Gamma_i\}\) has valid frame bounds
\[
A(1-\sqrt\lambda)^2
\quad\text{and}\quad
B(1+\sqrt\lambda)^2.
\]
The threshold is sharp: for every \(\lambda\ge1\), the zero family \(\Gamma_i=0\) satisfies the relative inequality for every \(g\)-frame \(\{\Lambda_i\}\), but is never a frame on a nonzero Hilbert space.

## Assumptions and scope
Let \(H\) be a Hilbert space, let \(\{H_i\}_{i\in I}\) be Hilbert coefficient spaces, and let \(\Lambda_i,\Gamma_i\in\mathcal L(H,H_i)\). Write
\[
U_\Lambda f=(\Lambda_i f)_i,
\qquad
U_\Gamma f=(\Gamma_i f)_i.
\]
Assume \(\{\Lambda_i\}\) is a \(g\)-frame with bounds \(A,B>0\), so
\[
A\|f\|^2\le\|U_\Lambda f\|^2\le B\|f\|^2.
\]
The corrected statement uses only the same relative condition as the source,
\[
\|(U_\Lambda+U_\Gamma)f\|^2\le\lambda\|U_\Lambda f\|^2
\quad\text{for every }f\in H.
\]
No finite-dimensional assumption is used in the proof. The one-dimensional construction is used only to refute the printed pseudoinverse-dependent sufficient condition and to certify sharpness at the boundary.

## Proof
Assume first that \(0\le\lambda<1\). By the triangle inequality in the Hilbert direct sum,
\[
\begin{aligned}
\|U_\Gamma f\|
&=\|(U_\Lambda+U_\Gamma)f-U_\Lambda f\|\\
&\ge \|U_\Lambda f\|-\|(U_\Lambda+U_\Gamma)f\|\\
&\ge(1-\sqrt\lambda)\|U_\Lambda f\|\\
&\ge(1-\sqrt\lambda)\sqrt A\,\|f\|.
\end{aligned}
\]
Similarly,
\[
\|U_\Gamma f\|
\le\|U_\Lambda f\|+\|(U_\Lambda+U_\Gamma)f\|
\le(1+\sqrt\lambda)\sqrt B\,\|f\|.
\]
Squaring gives the stated lower and upper \(g\)-frame bounds.

For sharpness, if \(\lambda\ge1\), choose \(\Gamma_i=0\) for every \(i\). Then
\[
\|(U_\Lambda+U_\Gamma)f\|^2=\|U_\Lambda f\|^2
\le\lambda\|U_\Lambda f\|^2,
\]
yet the zero family has no positive lower bound. Hence no universal conclusion based only on the source's relative inequality can extend to \(\lambda\ge1\).

For the source-specific counterexample to its printed threshold, specialize further to one index on \(H=\mathbb C\) and set \(\Lambda_1=2I\), \(\Gamma_1=0\). Then \(A=B=4\), \(T_\Lambda=2I\), and the relation \(T_\Lambda T_\Lambda^\dagger=I\) forces \(T_\Lambda^\dagger=\tfrac12I\). At \(\lambda=1\), the source's relative inequality is equality and its numerical threshold is \(2\), but the conclusion fails.

The scaling mechanism explains why this failure is unavoidable. Replacing a reference frame by \(c\Lambda\) leaves the dimensionless relative ratio
\[
\frac{\|(U_\Lambda+U_\Gamma)f\|^2}{\|U_\Lambda f\|^2}
\]
unchanged when both terms are scaled consistently, whereas the source expression \(A\|T_\Lambda^\dagger\|^{-2}/(2B)\) grows like \(|c|^2\) for an invertible tight synthesis operator. A universal relative stability boundary therefore cannot have that scale dependence.

## Verification
The counterexample requires no numerical approximation. Direct substitution gives the exact identities \(A=B=4\), \(\|T_\Lambda^\dagger\|=1/2\), source threshold \(2\), and relative constant \(\lambda=1\). The corrected bounds follow from two applications of the triangle inequality and the reference frame inequalities.

The target paper's Lemma 2.9 defines \(T^\dagger\) only through the right-inverse identity \(TT^\dagger=I\). In the counterexample \(T_\Lambda=2I\) is invertible, so the right inverse is unique; the example does not depend on any convention for choosing a pseudoinverse of a noninjective synthesis operator.

## Relationship to prior work
Sun's stability theorem for \(g\)-frames proves a more general perturbation result. Taking Sun's perturbed family to be \(-\Gamma\), with perturbation parameters \(\lambda_1=\sqrt\lambda\), \(\lambda_2=0\), and \(\mu=0\), gives exactly the safe region \(\lambda<1\) and the bounds above. Thus the scale-invariant sufficient condition itself is prior art and is not claimed as new.

The contribution here is narrower: it identifies that the 2022 Theorem 4.2 permits \(\lambda\ge1\) after rescaling the reference frame, gives an exact one-dimensional counterexample satisfying its printed pseudoinverse condition, and states the sharp universal correction in the theorem's own notation. Searches of the target title, DOI, theorem number, pseudoinverse formulation, scale-rescaling formulation, and zero-family formulation did not locate an indexed erratum or a prior source-specific correction.

## Limitations
The result does not claim that \(\lambda<1\) is necessary for a particular fixed pair \((\Lambda,\Gamma)\); some pairs with larger admissible constants can still be frames. The statement is about the best universal threshold that can be guaranteed solely from the source's displayed relative inequality.

The literature search cannot exclude an unindexed note, thesis remark, or informal correction. The 2005/2007 Sun theorem already contains the repaired sufficient implication, so originality is limited to the falsification and diagnosis of the later source theorem rather than the general perturbation principle.

## References
1. K. N. Rajeswari and N. George, *G-Frames and Their Stability in Hilbert Space*, South East Asian Journal of Mathematics and Mathematical Sciences 18(2) (2022), 125-134. DOI: 10.56827/SEAJMMS.2022.1802.12.
2. W. Sun, *Stability of G-frames*, ESI Preprint 1739 (2005); Journal of Mathematical Analysis and Applications 326(2) (2007), 858-868. DOI: 10.1016/j.jmaa.2006.03.043.
