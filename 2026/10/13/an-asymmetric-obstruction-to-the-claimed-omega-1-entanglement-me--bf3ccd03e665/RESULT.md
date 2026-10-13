# An asymmetric obstruction to the claimed \(\Omega_1\) entanglement-measurement formula
## Finding
Jiang, Chen, and Ye introduced the entanglement measurement bound \(E_{MB}\) for multipartite pure states and, for the three-qubit family
\[
|\Omega_1\rangle=q_0(|000\rangle+|011\rangle)+q_2(|101\rangle+|110\rangle)+q_4|111\rangle,
\qquad 2q_0^2+2q_2^2+q_4^2=1,
\]
claimed in their Eq. (39) that
\[
E_{MB}(|\Omega_1\rangle)=E_{bi}(|\Omega_1\rangle)
= h_2\!\left(\frac{1+\sqrt{1-C^2}}2\right),
\]
where
\[
C^2=4q_0^2\left(2(1-2q_0^2)-q_4^2\right).
\]
For every asymmetric member with \(q_0\ne q_2\), this equality contradicts the paper's own coarse-graining principle. In fact, its displayed right-hand side is \(S(\rho_A)\), whereas
\[
E_{MB}(|\Omega_1\rangle)\ge \max\{S(\rho_A),S(\rho_B),S(\rho_C)\},
\]
and the two determinants satisfy the exact identity
\[
\det\rho_B-\det\rho_A=(q_0^2-q_2^2)^2.
\]
Therefore \(S(\rho_B)>S(\rho_A)\) whenever \(q_0\ne q_2\). Consequently Eq. (39) can hold only, at most, on the symmetric locus \(q_0=q_2\); no sufficiency claim for that locus is made here.

An explicit normalized witness is
\[
q_0=\frac3{10},\qquad q_2=\frac{\sqrt{39}}{10},\qquad q_4=\frac15.
\]
For it,
\[
\det\rho_A=\frac{18}{125},\qquad
\det\rho_B=\det\rho_C=\frac{117}{500},
\]
so the Eq. (39) value is approximately \(0.6677247\) bits, whereas the rigorous coarse-graining lower bound is approximately \(0.9533283\) bits.

## Assumptions and scope
The state is a pure three-qubit state with real nonnegative coefficients in the family printed as \(|\Omega_1\rangle\) in Jiang--Chen--Ye. The normalization is \(2q_0^2+2q_2^2+q_4^2=1\). Entropies are base-two von Neumann entropies. The entanglement measurement bound is the minimum Shannon entropy over sequential adaptive local orthogonal measurements, with minimization also over the ordering of parties.

The result is a correction to the whole-family equality in Eq. (39). It does not compute the exact \(E_{MB}\) for asymmetric members and does not claim that Eq. (39) becomes correct whenever \(q_0=q_2\). It also does not by itself determine the tripartite relative entropy of entanglement for the counterexample.

## Proof
Tracing out qubits \(B,C\) gives
\[
\rho_A=
\begin{pmatrix}
2q_0^2&q_0q_4\\
q_0q_4&2q_2^2+q_4^2
\end{pmatrix},
\]
while tracing out \(A,C\), or \(A,B\), gives reduced states with the same spectrum,
\[
\rho_B\sim\rho_C\sim
\begin{pmatrix}
q_0^2+q_2^2&q_2q_4\\
q_2q_4&q_0^2+q_2^2+q_4^2
\end{pmatrix}.
\]
Hence
\[
\det\rho_A=q_0^2(4q_2^2+q_4^2),
\qquad
\det\rho_B=(q_0^2+q_2^2)^2+q_0^2q_4^2.
\]
Subtracting gives
\[
\det\rho_B-\det\rho_A=(q_0^2-q_2^2)^2.
\]

The normalization implies
\[
4q_2^2+q_4^2=2(1-2q_0^2)-q_4^2,
\]
so the paper's quantity satisfies
\[
C^2=4\det\rho_A.
\]
A trace-one qubit state with determinant \(d\) has eigenvalues
\[
\frac{1\pm\sqrt{1-4d}}2,
\]
and therefore entropy
\[
h_2\!\left(\frac{1+\sqrt{1-4d}}2\right).
\]
Thus the right-hand side of Eq. (39) is exactly \(S(\rho_A)\).

On the other hand, the coarse-graining property proved in the same paper says that the multipartite measurement bound is no smaller than the measurement bound for every coarser bipartition. For a pure bipartite state that bound equals the reduced-state entropy. Therefore
\[
E_{MB}(|\Omega_1\rangle)\ge S(\rho_A),\qquad
E_{MB}(|\Omega_1\rangle)\ge S(\rho_B),\qquad
E_{MB}(|\Omega_1\rangle)\ge S(\rho_C),
\]
which yields the maximum lower bound displayed above.

For trace-one qubit states, entropy is strictly increasing as a function of determinant on \([0,1/4]\). Hence \(q_0\ne q_2\) implies
\[
\det\rho_B>\det\rho_A
\quad\Longrightarrow\quad
S(\rho_B)>S(\rho_A),
\]
so Eq. (39) cannot hold.

For the explicit witness, normalization is exact because
\[
2\frac9{100}+2\frac{39}{100}+\frac4{100}=1.
\]
The reductions are
\[
\rho_A=
\begin{pmatrix}
9/50&3/50\\
3/50&41/50
\end{pmatrix},
\qquad
\rho_B=\rho_C=
\begin{pmatrix}
12/25&\sqrt{39}/50\\
\sqrt{39}/50&13/25
\end{pmatrix},
\]
with determinants \(18/125\) and \(117/500\), respectively. Therefore
\[
S(\rho_A)=h_2\!\left(\frac{1+\sqrt{53/125}}2\right),
\qquad
S(\rho_B)=h_2\!\left(\frac{1+\sqrt{8/125}}2\right),
\]
and the latter is strictly larger.

## Verification
The bundled `verify_counterexample.py` checks the exact normalization and rational determinants for the explicit witness, verifies the determinant gap, and evaluates the two entropies numerically. The all-parameter obstruction is analytic and follows from the displayed reduced density matrices and determinant identity; the script is only a replay of the exact witness.

## Relationship to prior work
Jiang--Chen--Ye prove that \(E_{MB}\) is nonincreasing under coarser partitions and explicitly note that, for tripartite pure states, the tight bipartition lower bound is the largest of the three bipartite entanglements. Later in the same paper, Eq. (26) is followed by a formula using the minimum of those three quantities, and Eq. (39) identifies the whole \(|\Omega_1\rangle\) family with one such bipartite entropy. The determinant identity above shows that the other two bipartitions are strictly more entangled whenever \(q_0\ne q_2\), so the claimed equality is incompatible with the earlier coarse-graining theorem.

Targeted searches for the paper title together with Eq. (39), \(|\Omega_1\rangle\), the coefficient pattern, and correction/counterexample terms did not locate a published correction or an equivalent determinant-gap observation. Chernyavskiy's earlier minimal-measurement-entropy paper supplies the independent-measurement quantity that Jiang--Chen--Ye compare against, but it does not contain the adaptive \(|\Omega_1\rangle\) formula or this obstruction.

## Limitations
This result is a necessary obstruction, not a complete replacement formula for \(E_{MB}\). The exact value of \(E_{MB}\) for asymmetric \(|\Omega_1\rangle\) states remains unproved here. Equality of the three single-qubit entropies at \(q_0=q_2\) removes this obstruction but does not prove Eq. (39). The source's subsequent equality claim for tripartite relative entropy uses Eq. (39); this finding shows that the argument does not apply off the symmetric locus, but it does not prove a different exact relative-entropy value.

## References
1. L.-z. Jiang, X.-y. Chen, T.-y. Ye, *Entanglement bound for multipartite pure states based on local measurements*, arXiv:1104.3280; Phys. Rev. A 84, 042308 (2011), DOI:10.1103/PhysRevA.84.042308.
2. A. Yu. Chernyavskiy, *Entanglement measure for multipartite pure states and its numerical calculation*, arXiv:0905.0201 (2009).
