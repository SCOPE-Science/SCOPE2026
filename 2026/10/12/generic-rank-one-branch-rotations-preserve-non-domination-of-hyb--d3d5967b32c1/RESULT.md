# Generic rank-one branch rotations preserve non-domination of hybrid quantum codes
## Finding
Fix an integer \(m\ge2\). Let the input space be
\[
\mathcal H=\mathbb C^{m+2}
\]
with orthonormal basis \(e_0,e_1,\ldots,e_{m+1}\), and let the output space be
\[
\mathcal K=\mathbb C^{m+1}
\]
with orthonormal basis \(f_0,f_1,\ldots,f_m\). Put
\[
W=\operatorname{span}\{f_1,\ldots,f_m\},
\]
and choose an arbitrary orthonormal basis \(\phi_1,\ldots,\phi_m\) of \(W\). Define a quantum channel \(\Phi\) by
\[
E_0=|f_0\rangle\langle e_0|+|f_1\rangle\langle e_1|,
\qquad
E_j=|\phi_j\rangle\langle e_{j+1}|\quad(1\le j\le m).
\]
The trace-preserving condition is immediate from
\[
E_0^*E_0=|e_0\rangle\langle e_0|+|e_1\rangle\langle e_1|,
\qquad
E_j^*E_j=|e_{j+1}\rangle\langle e_{j+1}|.
\]
Let
\[
J_0=\{j:\langle f_1,\phi_j\rangle=0\},
\qquad z=|J_0|.
\]
Then \(0\le z\le m-1\), and the maximal transmittable algebra types of \(\Phi\), in the embedding preorder of Salzmann and Singh, are exactly
\[
\mathbb M_2(\mathbb C)\oplus\mathbb C^z
\qquad\text{and}\qquad
\mathbb C^{m+1},
\]
unless \(z=m-1\). In that exceptional case,
\[
\mathbb M_2(\mathbb C)\oplus\mathbb C^{m-1}
\]
is the unique maximal transmittable type and hence is dominating.

Equivalently, a dominating transmittable algebra exists exactly when one branch vector is proportional to \(f_1\), or, equivalently, when the remaining \(m-1\) branch vectors are orthogonal to \(f_1\). If the branch basis is Haar-random in \(W\), then almost surely
\[
z=0,
\]
so the two incomparable maximal types are
\[
\mathbb M_2(\mathbb C)
\qquad\text{and}\qquad
\mathbb C^{m+1}.
\]
Thus failure of domination in the recent four-input/three-output example is not an isolated basis choice: it persists generically in every member of this higher-dimensional rank-one-branch family.

The example displayed by Salzmann and Singh is recovered at \(m=2\) with
\[
\phi_1=\frac{f_1+f_2}{\sqrt2},
\qquad
\phi_2=\frac{f_1-f_2}{\sqrt2},
\]
for which \(z=0\) and the maximal types are exactly \(\mathbb M_2(\mathbb C)\) and \(\mathbb C^3\).

## Assumptions and scope
The theorem concerns exact, one-shot transmission in the sense of finite-dimensional operator-algebra quantum error correction. It uses the equivalent transmittability criterion from arXiv:2609.40054v1: if
\[
S_\Phi=\operatorname{span}_{a,b}\{E_a^*E_b\},
\]
then an algebra \(\bigoplus_k\mathbb M_{d_k}(\mathbb C)\) is transmittable exactly when there are code subspaces \(C_k\) of dimensions \(d_k\) whose projections \(P_k\) satisfy
\[
P_kS_\Phi P_k=\mathbb CP_k,
\qquad
P_kS_\Phi P_\ell=0\quad(k\ne\ell).
\]
The result classifies this explicit channel family only. It does not classify arbitrary rank-one-branch channels, tensor powers of the family, approximate transmission, or capacities with nonzero error.

The integer \(z\) depends on exact orthogonality, not on a small-overlap threshold. Consequently the theorem distinguishes exact transmission from perturbative or approximate error correction.

## Proof
Let
\[
C=\operatorname{span}\{e_0,e_1\}.
\]
The restriction of \(\Phi\) to \(C\) is the isometry \(e_0\mapsto f_0\), \(e_1\mapsto f_1\), so \(\mathbb M_2(\mathbb C)\) is transmittable.

We first show that every noncommutative transmittable block is forced onto this same qubit sector. For each \(j\),
\[
Q_j=E_j^*E_j=|e_{j+1}\rangle\langle e_{j+1}|\in S_\Phi.
\]
Suppose a quantum block of dimension \(d\ge2\) is transmitted on a code projection \(P\). The Knill--Laflamme condition gives
\[
PQ_jP=\lambda_jP.
\]
The left-hand side has rank at most one, whereas \(P\) has rank at least two. Hence \(\lambda_j=0\). Positivity then implies \(Q_jP=0\) for every \(j\), so the code lies in \(C\). Therefore \(d\le2\), and when \(d=2\) the code is exactly \(C\). In particular, two distinct noncommutative blocks cannot occur.

Now suppose a classical block is placed on a line \(L=\operatorname{span}\{x\}\) in the orthogonal complement of \(C\), with
\[
x=\sum_{j=1}^m x_j e_{j+1}.
\]
Write
\[
\alpha_j=\langle f_1,\phi_j\rangle.
\]
Because
\[
E_0^*E_j=\alpha_j|e_1\rangle\langle e_{j+1}|,
\]
the cross-block condition \(P_CS_\Phi P_L=0\) forces
\[
\alpha_jx_j=0\qquad(1\le j\le m).
\]
Thus every classical block that can coexist with the qubit block is supported inside
\[
B_0=\operatorname{span}\{e_{j+1}:j\in J_0\},
\qquad \dim B_0=z.
\]
Hence at most \(z\) mutually orthogonal classical blocks can accompany \(\mathbb M_2(\mathbb C)\). Conversely, the coordinate lines \(\operatorname{span}\{e_{j+1}\}\) for \(j\in J_0\) satisfy all cross conditions, because \(\alpha_j=0\) and the branch outputs \(\phi_j\) are mutually orthogonal. Therefore
\[
\mathbb M_2(\mathbb C)\oplus\mathbb C^z
\]
is transmittable and dominates every transmittable algebra having a noncommutative block.

There is also a classical code with \(m+1\) messages: use the input lines
\[
\operatorname{span}\{e_0\},
\operatorname{span}\{e_2\},\ldots,
\operatorname{span}\{e_{m+1}\}.
\]
Their output supports are respectively
\[
\operatorname{span}\{f_0\},
\operatorname{span}\{\phi_1\},\ldots,
\operatorname{span}\{\phi_m\},
\]
which are pairwise orthogonal. Hence \(\mathbb C^{m+1}\) is transmittable. No classical algebra \(\mathbb C^r\) with \(r>m+1\) can be transmittable, because exact decoding requires \(r\) nonzero pairwise orthogonal output supports inside the \((m+1)\)-dimensional output space. Thus \(\mathbb C^{m+1}\) dominates every commutative transmittable type.

It remains only to compare these two maximal candidates. A noncommutative algebra cannot embed into a commutative algebra, so
\[
\mathbb M_2(\mathbb C)\oplus\mathbb C^z
\not\le \mathbb C^{m+1}.
\]
Conversely, \(\mathbb C^{m+1}\) embeds into \(\mathbb M_2(\mathbb C)\oplus\mathbb C^z\) exactly when its \(m+1\) scalar blocks can be packed into the two one-dimensional corners of the \(2\times2\) block together with the \(z\) scalar blocks, namely exactly when
\[
m+1\le z+2.
\]
Since \(f_1\in W\) is nonzero, an orthonormal basis of \(W\) cannot have all \(m\) vectors orthogonal to \(f_1\), so \(z\le m-1\). Hence comparability occurs exactly at \(z=m-1\). At that point the hybrid algebra is dominating; otherwise the two candidates are incomparable and both are maximal.

Finally, \(z=m-1\) holds exactly when the branch basis contains \(f_1\) up to phase. Indeed, if \(m-1\) basis vectors are orthogonal to \(f_1\), the remaining unit vector spans their orthogonal complement in \(W\), namely \(\mathbb Cf_1\). For Haar-random bases, each equation \(\langle f_1,\phi_j\rangle=0\) defines a measure-zero condition, so \(z=0\) almost surely.

## Verification
The proof is analytic and uses only the exact transmittability criterion and finite-dimensional rank arguments. The accompanying `artifacts/verify.py` constructs the Kraus operators for three representative cases: the \(m=2\) Hadamard basis from the recent source, an aligned \(m=2\) basis, and an \(m=3\) partially aligned basis. It checks trace preservation, computes \(z\), verifies the cross products \(E_0^*E_j\), and confirms the predicted maximal-type counts for those examples. Running the file with the Python standard library returns `VERIFY_OK`.

These finite checks are corroborative only; they are not used to prove the all-\(m\) classification or the Haar-generic statement.

## Relationship to prior work
Salzmann and Singh, arXiv:2609.40054v1, introduce transmittable finite-dimensional \(C^*\)-algebras, prove the blockwise Knill--Laflamme characterization used above, and exhibit a \(4\)-input/\(3\)-output channel whose only maximal transmittable types are \(\mathbb M_2(\mathbb C)\) and \(\mathbb C^3\). Their displayed channel uses the two Hadamard-rotated rank-one outputs \((f_1\pm f_2)/\sqrt2\). The present result contains that channel as \(m=2\), \(z=0\), but classifies an arbitrary number of rank-one branches and an arbitrary orthonormal branch basis, yielding an exact criterion for when domination returns and showing that non-domination is Haar-generic.

B\'eny, Kempf, and Kribs, arXiv:quant-ph/0608071v2, provide the operator-algebra quantum error-correction framework and the algebraic Knill--Laflamme condition for hybrid quantum-classical information. Duan, Severini, and Winter, DOI 10.1109/TIT.2012.2221677, develop the associated noncommutative-graph viewpoint for exact zero-error communication. These works supply the general language and criteria but do not state the branch-basis classification above.

## Limitations
The theorem is exact and one-shot. It does not quantify approximate recovery when the nominally zero overlaps \(\langle f_1,\phi_j\rangle\) are merely small. It does not address tensor powers, entanglement-assisted encoding, or asymptotic hybrid capacities. The maximal-type classification also uses the special rank-one branch structure and the protected qubit sector of the displayed family; different higher-rank branches can produce additional hybrid blocks.

## References
1. R. Salzmann and S. Singh, *Transmitting algebras through quantum channels*, arXiv:2609.40054v1 (first public 2026-09-30).
2. C. B\'eny, A. Kempf, and D. W. Kribs, *Generalization of Quantum Error Correction via the Heisenberg Picture*, arXiv:quant-ph/0608071v2; Phys. Rev. Lett. 98, 100502 (2007).
3. R. Duan, S. Severini, and A. Winter, *Zero-Error Communication via Quantum Channels, Noncommutative Graphs, and a Quantum Lov\'asz Number*, IEEE Trans. Inf. Theory 59, 1164--1174 (2013), DOI 10.1109/TIT.2012.2221677.
