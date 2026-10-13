# An explicit 62.02% bi-entangling certificate for the locally depolarized CNOT
## Finding
Let \(U\) be the two-qubit CNOT and let \(\Lambda_p(\rho)=(1-p)\rho+pI/2\), with \(0\le p\le1\). For the noisy gate
\[
\mathcal C_p=(\Lambda_p\otimes\Lambda_p)\circ\operatorname{Ad}_U,
\]
the gate is bi-entangling, in the sense of Virmani--Huelga--Plenio, for every
\[
p\ge p_*:=\frac{8-2\sqrt6}{5}=0.6202041028867288\ldots .
\]
This is a constructive sufficient bound, not a claim that \(p_*\) is the globally minimal bi-entangling noise. It improves the same-model sufficient bound \(p\ge2/3\) reported in the source.

## Assumptions and scope
Use the normalized four-qubit Choi state in qubit order \(A_1,A_2,B_1,B_2\). A two-qubit channel is called bi-entangling when its Choi state lies in the convex hull of states separable across the three cuts
\[
(A_1B_1)|(A_2B_2),\qquad (A_1B_2)|(A_2B_1),\qquad (A_1A_2)|(B_1B_2),
\]
which correspond respectively to separable, separable-followed-by-SWAP, and entanglement-breaking operations. This is the gate class introduced in arXiv:quant-ph/0408076.

For \(u=(x_1,z_1,x_2,z_2)\in\mathbb F_2^4\), define
\[
|u\rangle=(I_{A_1A_2}\otimes X^{x_1}Z^{z_1}_{B_1}\otimes X^{x_2}Z^{z_2}_{B_2})|J_U\rangle,
\]
where global Pauli phases are irrelevant. Encode \(u\) by the integer \([u]=8x_1+4z_1+2x_2+z_2\). For an affine subset \(S\subseteq\mathbb F_2^4\), put
\[
\tau_S=\frac1{|S|}\sum_{u\in S}|u\rangle\langle u|.
\]

## Proof
The one-qubit channel \(\Lambda_p\) is the Pauli channel with weights
\[
a=1-\frac{3p}{4}\quad\text{on }I,\qquad b=\frac p4\quad\text{on each of }X,Y,Z.
\]
Hence the CNOT Choi state of \(\mathcal C_p\) is diagonal in the basis \(|u\rangle\), with probability \(a^2\) at \([u]=0\), probability \(ab\) when exactly one output Pauli is nonidentity, and probability \(b^2\) when both are nonidentity.

At \(p=p_*\), the state has the exact convex decomposition below. The symbols SEP, SS, and EB mean separability across \((A_1B_1)|(A_2B_2)\), \((A_1B_2)|(A_2B_1)\), and \((A_1A_2)|(B_1B_2)\), respectively.

| class | support \(S\), written as integer labels \([u]\) | weight |
|---|---|---|
| SEP | \(\{0,2\}\) | \((-13+7\sqrt6)/25\) |
| SEP | \(\{0,3,5,6\}\) | \((57-23\sqrt6)/25\) |
| SEP | \(\{0,1,6,7\}\) | \((57-23\sqrt6)/25\) |
| SEP | \(\{0,3,4,7\}\) | \((-7+3\sqrt6)/5\) |
| SEP | \(\{1,3,12,14\}\) | \((-46+19\sqrt6)/25\) |
| SEP | \(\{0,4,8,12\}\) | \((44-16\sqrt6)/25\) |
| SEP | \(\{0,1,4,5\}\) | \((-7+3\sqrt6)/5\) |
| SEP | \(\{0,6\}\) | \((-46+19\sqrt6)/25\) |
| SEP | \(\{1,3,8,10\}\) | \((-46+19\sqrt6)/25\) |
| SS | \(\{0,3,9,10\}\) | \((68-27\sqrt6)/25\) |
| SS | \(\{0,1,14,15\}\) | \((68-27\sqrt6)/25\) |
| EB | \(\{0,1,8,9\}\) | \((-46+19\sqrt6)/25\) |
| EB | \(\{0,3,12,15\}\) | \((-46+19\sqrt6)/25\) |
| EB | \(\{0,3,8,11\}\) | \((22-8\sqrt6)/25\) |
| EB | \(\{0,1,12,13\}\) | \((22-8\sqrt6)/25\) |

All displayed weights are positive and sum to one. Direct coefficient comparison gives exactly the Pauli-error probabilities of \(\mathcal C_{p_*}\).

It remains to certify the three kinds of separability. The CNOT Choi basis is the common eigenbasis of the commuting Pauli generators
\[
G_0=IXIX,\qquad G_1=IZZZ,\qquad G_2=XIXX,\qquad G_3=ZIZI,
\]
in the qubit order \(A_1,A_2,B_1,B_2\). If \(S\) is affine, then \(\tau_S\) is a normalized stabilizer-code projector: it is specified by independent parity constraints on the eigenvalue bits of products of the \(G_j\). If, for a bipartition \(L|R\), the restrictions to \(L\) of those independent stabilizer products commute pairwise, then their restrictions to \(R\) commute as well because the full products commute. Both sides can therefore be simultaneously diagonalized locally, and the stabilizer projector is diagonal in a product basis across \(L|R\). Thus \(\tau_S\) is separable across that cut.

The included `verify.py` reconstructs an independent parity basis for every support in the table and checks this local-commutation criterion on the asserted cut. Therefore every table row belongs to the indicated bi-entangling class, so their convex combination is bi-entangling.

Finally, for \(p\ge p_*\), write
\[
1-p=(1-p_*)(1-r),\qquad r=\frac{p-p_*}{1-p_*}\in[0,1].
\]
Then \(\Lambda_p=\Lambda_r\circ\Lambda_{p_*}\). Postcomposition by local channels preserves each of the three bi-entangling classes and hence their convex hull. Therefore \(\mathcal C_p\) is bi-entangling for every \(p\ge p_*\).

## Verification
Run `python3 verify.py` in the package directory. The checker uses only the Python standard library. It verifies, in exact arithmetic in \(\mathbb Q(\sqrt6)\), that \(p_*\) is the physical root of \(5p^2-16p+8=0\), all fifteen coefficients are positive and sum to one, the sixteen Choi-basis probabilities match exactly, every support is affine, and every asserted cut passes the stabilizer local-commutation certificate. The analytic proof, not finite sampling, establishes the infinite interval \(p\ge p_*\).

## Relationship to prior work
Virmani, Huelga, and Plenio introduced bi-entangling machines and considered exactly the independent replacement-depolarizing model used here. Their Eq. (17) is \((1-p)^2U+p(1-p)(D\otimes I)U+p(1-p)(I\otimes D)U+p^2D\otimes D\), and their Eq. (23) gives the sufficient bound \(p\ge2/3\). Immediately afterward they state that their calculation is not a full optimization over bi-entangling gates and may be improved. The present decomposition supplies such an improvement for the CNOT within the same gate-level model.

Kempe, Regev, Unger, and de Wolf later obtained numerically smaller CNOT noise bounds in a different circuit model and explicitly described their bounds as incomparable with earlier ones. A 2026 fermionic-computation paper independently contains the same algebraic constant \((8-2\sqrt6)/5\), but for convex-Gaussianity of a fermionic resource channel, not for the CNOT bi-entangling polytope. Targeted searches by source identifier, exact constant, decimal value, CNOT/bi-entangling aliases, and the final implication statement did not locate the decomposition or the same-model \(62.02\%\) sufficient bound.

## Limitations
The claim is only a sufficient classical-simulability certificate for this specific independent local depolarizing model. No lower bound proving global optimality of \(p_*\) over the full bi-entangling convex set is claimed. The decomposition is tailored to the CNOT stabilizer-Choi geometry; it is not asserted for arbitrary two-qubit unitaries. The coincidence of the same algebraic constant in a 2026 fermionic setting is numerical/algebraic only and does not supply this CNOT decomposition.

## References
1. S. Virmani, S. F. Huelga, and M. B. Plenio, *Classical simulatability, entanglement breaking, and quantum computation thresholds*, arXiv:quant-ph/0408076v2; Phys. Rev. A 71, 042328 (2005).
2. J. Kempe, O. Regev, F. Unger, and R. de Wolf, *Upper Bounds on the Noise Threshold for Fault-tolerant Quantum Computing*, arXiv:0802.1464.
3. O. Allison and L. Coffman, *Noise Limits on Fault-Tolerant Fermionic Quantum Computing*, arXiv:2609.09467v1 (2026).
