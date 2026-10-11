# Local positivity is a necessary missing hypothesis for the controlled-fusion analysis operator

## Finding
Shakoory--Ahmadi--Behzadi--Nami define a \(CC'\)-controlled fusion frame using only a global quadratic inequality, but then use coordinate coefficients
\[
(C^*\pi_{W_i}C')^{1/2}f
\]
to define the controlled analysis operator. The global inequality does not imply that each local operator \(C^*\pi_{W_i}C'\) is positive, so this square-root construction is not defined on the whole class admitted by the definition.

Take
\[
H=\mathbb R^2,\qquad
W_1=\operatorname{span}\{e_1\},\qquad
W_2=\operatorname{span}\{e_2\},
\]
with weights \(v_1=v_2=1\), and put
\[
C=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad
C'=C^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}.
\]
Both controllers are positive definite.

For \(f=(x,y)\),
\[
\langle \pi_{W_1}C'f,\pi_{W_1}Cf\rangle
=(x-y)(2x+y)
=2x^2-xy-y^2,
\]
and
\[
\langle \pi_{W_2}C'f,\pi_{W_2}Cf\rangle
=(-x+2y)(x+y)
=-x^2+xy+2y^2.
\]
Adding gives
\[
\sum_{i=1}^2
\langle \pi_{W_i}C'f,\pi_{W_i}Cf\rangle
=x^2+y^2=\|f\|^2.
\]
Therefore this is a Parseval \(CC'\)-controlled fusion frame according to the displayed Definition 3.1.

Nevertheless
\[
A_1:=C^*\pi_{W_1}C'
=\begin{pmatrix}2&-2\\1&-1\end{pmatrix},
\]
so
\[
A_1^*
=\begin{pmatrix}2&1\\-2&-1\end{pmatrix}
\ne A_1.
\]
Moreover
\[
\langle A_1e_2,e_2\rangle=-1.
\]
Hence \(A_1\) is not positive. In particular, it has no positive square root, and the coefficient-norm identity used to pass from the controlled quadratic form to a direct-sum analysis operator cannot hold: its right-hand side equals \(-1\) at \(f=e_2\), whereas a squared norm is nonnegative.

Thus local positivity
\[
C^*\pi_{W_i}C'\ge0\qquad(i\in I)
\]
is an additional necessary hypothesis for the paper's positive-square-root coefficient representation. It is also sufficient.

## Assumptions and scope
The example is real and two dimensional, so no convergence or domain subtlety is involved. Both \(C\) and \(C'\) are not merely invertible but positive definite; the obstruction is therefore not caused by allowing arbitrary nonselfadjoint controllers.

The finding concerns the coordinatewise analysis/synthesis framework built from positive square roots of \(C^*\pi_{W_i}C'\). It does not say that the global quadratic definition is internally contradictory. A family can satisfy that global inequality by cancellation between locally indefinite terms, exactly as the example does.

No claim is made that every later theorem in the paper fails. Results whose hypotheses independently guarantee the relevant positivity may remain valid. The precise conclusion is that the square-root operator model cannot be asserted for every family covered by Definition 3.1 unless local positivity is included.

## Proof
The determinants of the two controller matrices are
\[
\det C=\det C'=1,
\]
and their traces are positive, so both are positive definite. Direct multiplication gives
\[
CC'=C'C=I.
\]

Let \(P_1=\pi_{W_1}\) and \(P_2=\pi_{W_2}\). Since \(P_1+P_2=I\),
\[
\sum_{i=1}^2 C^*P_iC'
=C^*(P_1+P_2)C'
=C^*C'
=CC'
=I.
\]
Taking quadratic forms gives the Parseval identity
\[
\sum_{i=1}^2
\langle P_iC'f,P_iCf\rangle
=\|f\|^2.
\]
The coordinate expansions displayed above verify the same identity term by term.

For the first local operator,
\[
C^*P_1C'
=CP_1C'
=\begin{pmatrix}2&-2\\1&-1\end{pmatrix},
\]
which is not self-adjoint. Positivity of a bounded operator on a real or complex Hilbert space implies self-adjointness; the explicit negative value
\[
\langle C^*P_1C'e_2,e_2\rangle=-1
\]
also directly rules out positivity.

If a positive square root \(R_1=(C^*P_1C')^0.5\) existed in the sense required by the coefficient construction, then
\[
\|R_1e_2\|^2
=\langle C^*P_1C'e_2,e_2\rangle=-1,
\]
which is impossible. Hence the direct-sum coefficient formula is not available for this Definition 3.1 frame.

Conversely, if \(C^*P_iC'\ge0\) for every \(i\), each operator has a unique bounded positive square root \(R_i\). Then
\[
\|R_if\|^2
=\langle C^*P_iC'f,f\rangle
=\langle P_iC'f,P_iCf\rangle.
\]
Therefore the controlled-frame inequality becomes
\[
A\|f\|^2
\le
\sum_i v_i^2\|R_if\|^2
\le
B\|f\|^2,
\]
which is exactly the bounded and bounded-below direct-sum analysis-operator estimate used by the framework.

## Verification
Every matrix computation is exact:
\[
C^-1=C',
\qquad
C^*P_1C'=
\begin{pmatrix}2&-2\\1&-1\end{pmatrix},
\qquad
C^*P_2C'=
\begin{pmatrix}-1&2\\-1&2\end{pmatrix},
\]
and
\[
C^*P_1C'+C^*P_2C'=I.
\]
Thus the global Parseval identity and the local failure of positivity hold simultaneously.

The target article was read at Definition 3.1 and the immediately following analysis-operator construction. The paper itself first states the coefficient norm formula conditionally when \(C^*\pi_{W_i}C'\) is positive for each \(i\), then proceeds to define the square-root analysis operator. The example shows that this condition is not automatic from the preceding controlled-frame definition.

The 2012 precursor by Khosravi--Musazadeh was also inspected at its controlled-fusion-frame definition and square-root analysis construction. It likewise displays local positivity immediately before using the local positive square roots. This is treated as prior structural guidance, not as a new positivity principle.

## Relationship to prior work
Khosravi--Musazadeh's 2012 controlled-fusion-frame paper already records the implication
\[
T^*\pi_{W_i}U\ge0
\quad\Longrightarrow\quad
\|(T^*\pi_{W_i}U)^{1/2}f\|^2
=
\langle \pi_{W_i}Uf,\pi_{W_i}Tf\rangle
\]
before defining its coordinatewise controlled analysis operator. The present claim does not seek novelty for that sufficient condition.

The source-specific contribution is the strict separation between the 2021/2022 paper's global Definition 3.1 and its later coordinatewise operator model: the explicit positive-controller Parseval example satisfies the definition but violates local positivity. Targeted searches for the exact source, its analysis operator, local positivity, nonselfadjoint local operators, and square-root counterexamples did not locate an indexed correction or the same counterexample.

## Limitations
The local positivity condition is exact for the positive-square-root coordinate representation. Other operator formulations that do not require local square roots may be possible and are not excluded.

The result does not classify all controller/subspace configurations for which local positivity holds, and it does not audit every downstream theorem in the source. An unindexed erratum, thesis remark, or informal note may already contain the same source-specific observation.

## References
1. H. Shakoory, R. Ahmadi, N. Behzadi and S. Nami, *Controlled Fusion Frames in Hilbert Spaces and Their Dual*, Journal of Mathematical Extension 16(9), 2022, DOI 10.30495/JME.2022.1476. First public publisher date: 10 November 2021. Primary AMS classification: 42C15.
2. A. Khosravi and K. Musazadeh, *Controlled fusion frames*, Methods of Functional Analysis and Topology 18(3), 2012, 256--265.
