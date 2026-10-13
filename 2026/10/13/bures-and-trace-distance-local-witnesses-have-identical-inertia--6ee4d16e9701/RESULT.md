# Bures and trace-distance local witnesses have identical inertia for unital qubit dynamics
## Finding
For every differentiable unital qubit evolution with Bloch equation
\[
\dot x(t)=D(t)x(t),
\]
and every full-rank Bloch state \(x\in\mathbb R^3\) with \(\|x\|<1\), define
\[
\bar D=D+D^{\mathsf T},
\qquad
R_x=I+\frac{xx^{\mathsf T}}{1-\|x\|^2}.
\]
If \(J_B\) denotes the infinitesimal Bures/Fisher growth matrix of Hall, Cresser, Li, and Andersson, then
\[
4J_B=R_x\bar D R_x.
\]
Therefore \(J_B\) and \(\bar D\) have exactly the same inertia. In particular, the Bures/Fisher local witness has a positive-growth direction if and only if
\[
\lambda_{\max}(D+D^{\mathsf T})>0,
\]
which is precisely the trace-distance local witness criterion derived in the same source.

For the source's explicit non-Markovian example,
\[
D(t)=\operatorname{diag}(-1+\tanh t,-1+\tanh t,-2),
\]
one has \(D(t)+D(t)^{\mathsf T}\prec0\) for every finite \(t\ge0\). Hence \(J_B\prec0\) for every full-rank Bloch state at every finite time. This gives an analytic proof of the negative-definiteness statement that the source reported only after a numerical check.

## Assumptions and scope
A qubit state is written in Bloch form as \(\rho=(I+x\cdot\sigma)/2\). Full rank means \(\|x\|<1\). The dynamics is assumed differentiable and unital at the time under consideration, so the affine Bloch equation has no translation term and is exactly \(\dot x=D x\). No symmetry or diagonalizability of \(D\) is assumed.

The statement concerns the infinitesimal Bures metric, equivalently the local quantum Fisher metric, and the infinitesimal trace-distance witness. It compares whether a positive local growth direction exists at a fixed time. It does not identify the numerical values of integrated non-Markovianity measures, nor does it claim that Bures and trace distances agree for finitely separated state pairs.

## Proof
Hall, Cresser, Li, and Andersson write the Bures growth matrix for unital qubit dynamics as
\[
4J_B=\bar D
+\frac{\bar Dxx^{\mathsf T}+xx^{\mathsf T}\bar D}{1-\|x\|^2}
+\frac{(x^{\mathsf T}\bar D x)xx^{\mathsf T}}{(1-\|x\|^2)^2},
\]
where \(\bar D=D+D^{\mathsf T}\). Put \(s=1-\|x\|^2>0\). Direct multiplication gives
\[
\left(I+\frac{xx^{\mathsf T}}{s}\right)
\bar D
\left(I+\frac{xx^{\mathsf T}}{s}\right)
=
\bar D
+\frac{\bar Dxx^{\mathsf T}+xx^{\mathsf T}\bar D}{s}
+\frac{(x^{\mathsf T}\bar D x)xx^{\mathsf T}}{s^2}.
\]
Thus
\[
4J_B=R_x\bar D R_x.
\]

For every vector \(v\),
\[
v^{\mathsf T}R_xv=\|v\|^2+\frac{(x^{\mathsf T}v)^2}{s}.
\]
Hence \(R_x\) is positive definite. More explicitly, its eigenvalue is \(1\) on the plane orthogonal to \(x\), and \(1/s\) in the \(x\)-direction, so it is invertible. The displayed factorization is therefore a real congruence transformation. Sylvester's law of inertia implies that \(4J_B\) and \(\bar D\) have the same numbers of positive, zero, and negative eigenvalues. Multiplication by the positive scalar \(1/4\) does not change inertia.

The trace-distance calculation in the source gives positive local growth exactly when \(\lambda_{\max}(\bar D)>0\). Since the positive index of \(J_B\) equals that of \(\bar D\), the Bures/Fisher local witness is positive under exactly the same condition.

For the example matrix, finite \(t\) gives \(\tanh t<1\), so both entries \(-1+\tanh t\) are strictly negative, as is \(-2\). Therefore \(\bar D=2D\prec0\), and the congruence above gives \(J_B\prec0\) for every full-rank state and every finite \(t\ge0\).

## Verification
The proof is symbolic and does not rely on finite enumeration or numerical optimization. The bundled `verify.py` performs an exact-rational consistency check of the rank-one congruence identity for several nonsingular rational Bloch vectors and symmetric test matrices. It also checks the closed-form inverse of \(R_x\) supplied by the Sherman--Morrison identity. These computations are checks of the algebra only; the infinite statement is proved by the displayed identities and Sylvester's law of inertia.

The source equation, its trace-distance criterion, and the motivating numerical statement were checked in the open-access full text. The exact source formula is Eq. (23); the source explicitly states that negative definiteness of \(J_B\) for its example had been checked numerically.

## Relationship to prior work
Hall, Cresser, Li, and Andersson derive the Bloch damping equation, prove that trace-distance backflow occurs exactly when \(D+D^{\mathsf T}\) has a positive eigenvalue, derive the Bures growth matrix, and then numerically check negative definiteness for their explicit example. The factorization above is not stated there and turns the Bures matrix into a congruence of the trace-distance matrix, yielding a general all-unital-qubit equivalence rather than only an analytic verification of one example.

Lu, Wang, and Sun develop quantum Fisher-information flow for time-local master equations and decompose it into channel subflows. Their full text does not formulate the Bloch-matrix congruence above or an equivalence with the trace-distance criterion. Liu, Lu, and Wang later emphasize that trace distance captures the unital aspect while introducing a complementary non-unital measure based on Bures distance; that work likewise does not state the present inertia identity. Later reviews and distance-comparison papers found in targeted searches discuss several non-Markovianity witnesses but did not supply this all-unital-qubit congruence theorem.

## Limitations
The theorem is local in state space and time. The Bures/Fisher metric is written on the full-rank Bloch ball; the pure-state boundary is not needed for the equivalence of existence of an interior positive-growth direction. The theorem does not say that either witness detects all forms of non-Markovianity: Hall, Cresser, Li, and Andersson's own example remains non-Markovian by their canonical-rate criterion while both local witnesses are blind to it.

A literature search cannot prove uniqueness. The principal residual originality risk is a later or differently phrased paper observing the same congruence or the same inertia equivalence without using the searched terminology.

## References
1. M. J. W. Hall, J. D. Cresser, L. Li, and E. Andersson, “Canonical form of master equations and characterization of non-Markovianity,” arXiv:1009.0845; DOI:10.1103/PhysRevA.89.042120.
2. X.-M. Lu, X. Wang, and C. P. Sun, “Quantum Fisher Information Flow in Non-Markovian Processes of Open Systems,” arXiv:0912.0587; DOI:10.1103/PhysRevA.82.042103.
3. J. Liu, X.-M. Lu, and X. Wang, “Non-unital non-Markovianity of quantum dynamics,” arXiv:1301.5763; DOI:10.1103/PhysRevA.87.042103.
