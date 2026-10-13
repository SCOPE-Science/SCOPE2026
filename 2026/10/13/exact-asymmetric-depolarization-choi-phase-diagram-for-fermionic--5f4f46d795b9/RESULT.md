# Exact asymmetric-depolarization Choi phase diagram for fermionic gates
## Finding
Let \(U\) be a parity-preserving two-qubit unitary with block decomposition \(U=A\oplus B\) in the even and odd parity subspaces, and put
\[
\eta(U)=\frac12|\det A-\det B|\in[0,1].
\]
For independently chosen local depolarizing strengths \(p_1,p_2\in[0,1]\), define
\[
\mathcal E_{U;p_1,p_2}
=(\mathcal D_{p_1}\otimes\mathcal D_{p_2})\circ\operatorname{Ad}_U,
\qquad
\mathcal D_p(X)=(1-p)X+p\operatorname{Tr}(X)I/2.
\]
Here \(\operatorname{Ad}_U(X)=UXU^\dagger\). Let \(\rho_{U;p_1,p_2}\) be the normalized four-mode fermionic Choi state formed with the even Gaussian maximally entangled reference specified by Allison and Coffman, arXiv:2609.09467v1, Eqs. (28)--(32). Define
\[
a_i=1-\frac{3p_i}{4},\qquad b_i=\frac{p_i}{4},\qquad [x]_+=\max(0,x).
\]
The exact even and odd Uhlmann--Wootters fermionic concurrences of this *state* are
\[
\boxed{C_-(\rho_{U;p_1,p_2})=0}
\]
and
\[
\boxed{
C_+(\rho_{U;p_1,p_2})=
\left[
\eta(a_1a_2-b_1b_2)
-\sqrt{\eta^2(a_1b_2-b_1a_2)^2+4a_1b_1a_2b_2}
-4b_1b_2
\right]_+.
}
\]
By the four-mode fermionic state criterion of Oszmaniec--Gutt--Kuś, the Choi state is convex-Gaussian if and only if the bracket in this formula is nonpositive. In addition, \(C_+\) is nondecreasing in the gate parameter \(\eta\) for each fixed noise pair.

For \(\eta=1\), which includes SWAP and CZ, the phase diagram simplifies to
\[
\boxed{C_+(\rho_{U;p_1,p_2})=
\left[1-p_1-p_2+\frac58p_1p_2\right]_+}
\]
and consequently
\[
\boxed{
\rho_{U;p_1,p_2}\text{ is convex-Gaussian}
\iff p_1+p_2-\frac58p_1p_2\ge1.
}
\]
The threshold at any fixed \(p_1\) is thus
\[
p_2\ge\frac{1-p_1}{1-5p_1/8}
\qquad(0\le p_1\le1).
\]
For equal rates \(p_1=p_2=p\) this recovers the source's exact threshold
\[
p_*=\frac{8-2\sqrt6}{5}=0.6202041028\ldots.
\]
An unequal noise split can cross the Choi boundary at a smaller total noise budget: \((p_1,p_2)=(2/5,4/5)\) lies exactly on it, with mean \(3/5\), but the balanced pair \((3/5,3/5)\) still has positive concurrence \(1/40\). In fact, every Choi-convex-Gaussian pair satisfies \(p_1+p_2\ge1\); equality is possible only for \((0,1)\) or \((1,0)\), whereas balanced noise requires total strength \(2p_*>1\). At fixed mean, increasing asymmetry weakly increases the quantity \(p_1+p_2-5p_1p_2/8\), making Choi Gaussianity easier to reach.

## Assumptions and scope
The local noise channels are independently parameterized, but they act as product channels; no cross-mode correlated noise is included. Both rates satisfy \(0\le p_i\le1\) with the source's convention \(\mathcal D_p(X)=(1-p)X+p\operatorname{Tr}(X)I/2\). The gate \(U\) preserves fermionic parity. The four-mode reference state, Majorana conjugation, and parity-sector concurrence normalization are precisely those used in arXiv:2609.09467v1 and arXiv:1406.1577v1. The formula includes degenerate and zero-weight endpoints by continuity.

This theorem classifies the four-mode **Choi state's** convex-Gaussianity. It does **not** assume or prove an equivalence with a channel's action on all Gaussian inputs or on arbitrary Gaussian ancillary extensions, and it does not imply a fault-tolerance or circuit-simulability ceiling without such an additional theorem.

## Proof
Write the Pauli Kraus probabilities of the two local depolarizing channels as
\[
\Pr(I\text{ on mode }i)=a_i,
\qquad
\Pr(P\text{ on mode }i)=b_i\quad(P\in\{X,Y,Z\}).
\]
For any parity-preserving \(U=A\oplus B\), the factorization in Appendix A of Allison--Coffman is \(U=V_\delta G\), where \(G\) is a Gaussian unitary, \(V_\delta=\exp(i\delta Z\otimes Z/4)\), and \(\eta=|\sin(\delta/2)|\). The right Gaussian factor can be transferred to the reference half of the maximally entangled Gaussian state; because the noise acts afterward, this remains valid with different \(p_i\). Gaussian conjugation of the reference preserves both parity-sector concurrences. Thus it is enough to treat \(V_\delta\).

Its sixteen Pauli-noise branch vectors form an orthonormal basis, independently of their probabilities. The eight even-parity labels are
\[
II,\ IZ,\ ZI,\ ZZ,\ XX,\ XY,\ YX,\ YY,
\]
and the eight odd labels are
\[
IX,\ IY,\ XI,\ XZ,\ YI,\ YZ,\ ZX,\ ZY.
\]
The four-mode Majorana-conjugation overlap matrix pairs these labels within a parity sector as
\[
\{II,ZZ\},\ \{IZ,ZI\},\ \{XX,YY\},\ \{XY,YX\}
\]
and
\[
\{IX,ZY\},\ \{IY,ZX\},\ \{XI,YZ\},\ \{XZ,YI\}.
\]
In each pair, its diagonal entries have absolute value \(\eta\), its off-diagonal entries have absolute value \(\sqrt{1-\eta^2}\), and the overlap block is unitary. These properties depend only on the noiseless gate, not on the branch probabilities.

For a block associated with Pauli probabilities \(u,v\ge0\), the two nonnegative concurrence singular values are
\[
s_\pm(u,v;\eta)
=\frac12\left[
\sqrt{\eta^2(u-v)^2+4uv}
\pm\eta|u-v|
\right].
\]
Indeed the weighted block has squared Frobenius norm \(\eta^2(u^2+v^2)+2uv(1-\eta^2)\) and determinant of absolute value \(uv\), which determine this pair of singular values.

The four even blocks have the weight pairs
\[
(a_1a_2,b_1b_2),\quad
(a_1b_2,b_1a_2),\quad
(b_1b_2,b_1b_2),\quad
(b_1b_2,b_1b_2).
\]
Since \(a_i\ge b_i\), one has
\[
a_1a_2-b_1b_2\ge|a_1b_2-b_1a_2|.
\]
Both of the first two blocks have the same product of weights, namely \(a_1b_1a_2b_2\). Since \(s_+\) increases with \(|u-v|\) at fixed product, the first block supplies the largest singular value; it also dominates the remaining singular values \(b_1b_2\). The concurrence's largest-minus-other-seven expression therefore becomes
\[
\begin{aligned}
\Delta_+
&=[s_+(a_1a_2,b_1b_2)-s_-(a_1a_2,b_1b_2)]\\
&\quad-[s_+(a_1b_2,b_1a_2)+s_-(a_1b_2,b_1a_2)]-4b_1b_2\\
&=\eta(a_1a_2-b_1b_2)
-\sqrt{\eta^2(a_1b_2-b_1a_2)^2+4a_1b_1a_2b_2}
-4b_1b_2.
\end{aligned}
\]
Hence \(C_+=[\Delta_+]_+\).

The odd blocks appear in two identical pairs of weight types:
\[
(a_1b_2,b_1b_2),\qquad (b_1a_2,b_1b_2).
\]
Thus each odd-sector singular value is repeated at least twice. The largest cannot exceed the sum of the remaining seven, so \(C_-=0\), including all boundary cases.

For monotonicity in \(\eta\), set \(A=a_1a_2-b_1b_2\), \(D=a_1b_2-b_1a_2\), and \(Q=4a_1b_1a_2b_2\). We have \(A\ge|D|\) and, where the square root is positive,
\[
\frac{\partial\Delta_+}{\partial\eta}
=A-\frac{\eta D^2}{\sqrt{\eta^2D^2+Q}}
\ge A-|D|\ge0.
\]
Continuity handles zero-weight endpoints.

When \(\eta=1\), the square root becomes \(a_1b_2+b_1a_2\), giving
\[
\Delta_+=a_1a_2-a_1b_2-b_1a_2-5b_1b_2
=1-p_1-p_2+\frac58p_1p_2.
\]
The four-mode state theorem of Oszmaniec--Gutt--Kuś identifies simultaneous vanishing of \(C_+\) and \(C_-\) with convex-Gaussianity of the **state**, establishing the phase diagram.

For fixed mean \(\bar p=(p_1+p_2)/2\) and half-difference \(d=(p_1-p_2)/2\), the maximal-gate criterion becomes
\[
2\bar p-\frac58(\bar p^2-d^2)\ge1,
\]
which makes the effect of asymmetry explicit. The minimum total noise is \(1\): the inequality requires \(p_1+p_2\ge1+(5/8)p_1p_2\), with equality at \((0,1)\) and \((1,0)\).

## Verification
All assertions are algebraic for every allowed gate and noise pair. The bundled standalone Python checker reconstructs the four-mode Gaussian-reference vector, the Pauli-noise branch vectors, and Majorana conjugation matrices directly. For representative \(\eta\), it tests the exact overlap pairing structure independently of the singular-value formula, then compares all computed concurrence singular values with the analytic expression for a fixed rational grid of noise strengths, including zero and full depolarization. It also checks the symmetric-source specialization and the unequal-noise examples. Finite tests corroborate the complete symbolic argument; they do not prove the continuum result.

## Relationship to prior work
Allison and Coffman, arXiv:2609.09467v1, derive the complete single-rate concurrence curve for all parity-preserving two-qubit gates, assuming equal local depolarizing strength \(p\) on both output qubits. Their Appendix A provides the Gaussian reduction to \(\eta\), while Appendix B gives the Pauli-noise overlap blocks and a general two-by-two singular-value formula. Their conclusion explicitly lists replacement of the local depolarizing model by more general noise models as a direction for further study. The present theorem resolves the basic physically asymmetric extension \((p_1,p_2)\) without assuming equal noise, producing the full three-parameter Choi-concurrence surface and a complete unequal-noise phase region for maximally resourceful gates.

Oszmaniec, Gutt, and Kuś, arXiv:1406.1577v1, prove the necessary and sufficient two-concurrence condition for a **four-mode fermionic state** to be convex-Gaussian. Their paper studies a different, globally depolarized resource state, not the independently depolarized parity-preserving gate Choi family. In particular it does not compute this asymmetric two-mode channel Choi-state phase surface.

The four-mode state criterion alone is not an equivalence for arbitrary channel notions; no statement about an unconditional channel-level or computational fault-tolerance threshold follows from the calculation without a justified channel--Choi connection.

## Limitations
The theorem concerns only independent product depolarization following a parity-preserving two-qubit unitary and the corresponding four-mode Choi state. Correlated Pauli noise, amplitude damping, and larger system gates are outside scope. The state criterion is sharp, but the interpretation as a circuit-simulability threshold requires additional channel-level hypotheses and proofs that are not supplied here. No assertion is made that all unequal-noise channels with Gaussian Choi states admit a Gaussian mixture decomposition as channels on arbitrary ancillary extensions.

## References
1. O. Allison and L. Coffman, *Noise Limits on Fault-Tolerant Fermionic Quantum Computing*, arXiv:2609.09467v1, first public 2026-09-08, Appendix A and Appendix B.
2. M. Oszmaniec, J. Gutt, and M. Kuś, *Classical simulation of fermionic linear optics augmented with noisy ancillas*, arXiv:1406.1577v1; Physical Review A 90, 020302(R) (2014), DOI 10.1103/PhysRevA.90.020302.
